"""De expresión regular a AFD mínimo (Práctica 4, Ejercicio 2)."""

from __future__ import annotations

import flet as ft

from nucleo.errores import ErrorTC, ExpresionInvalida
from nucleo.expresiones import Clases, ExpresionRegular
from nucleo.formatos import Archivos
from nucleo.kleene import ConstruccionThompson

from ..componentes import Veredicto, VisorEtapas, metrica, tarjeta
from ..diagrama import Diagrama
from ..tema import MONO, Paleta, pantalla
from .base import Vista

EJEMPLOS = {
    "Lista 3 · 241": "0 + 1", "Lista 3 · 242": "0* + 1", "Lista 3 · 243": "(0 + 1)*", "Lista 3 · 244": "0(0 + 1)",
    "Lista 3 · 245": "0(0 + 1)*", "Lista 3 · 246": "0*(0 + 1)", "Lista 3 · 247": "(01)* + 1*",
    "Lista 3 · 248": "(0* + 1)0", "Lista 3 · 249": "(0* + 1)0*", "Lista 3 · 250": "0*1* + 1*0",
    "Lista 3 · 251": "(0 + 1*)0 + 1*1", "Lista 3 · 252": "(0 + 1)*(00 + 11) + (00 + 11)(0 + 1)*",
    "Lista 3 · 253": "(0 + (11 + 00)*)(11 + 10 + 01)*(λ + 110)",
    "Lista 4 · 272a": "a + b*", "Lista 4 · 272b": "(ab)*a", "Lista 4 · 272c": "(a + b)*abb",
    "Lista 4 · 272d": "a(ba)* + b", "Lista 4 · 272e": "(a + λ)(b + ∅)", "Lista 4 · 278": "(a + b)*b",
}
ETAPAS = [("thompson", "Parte I (Thompson)"), ("lambda", "Quitar λ"), ("subconjuntos", "Subconjuntos"),
          ("minimo", "AFD mínimo")]


class Expresion(Vista):
    CLAVE = "expresion"
    TITULO = "ER → AFD"
    ICONO = ft.Icons.FUNCTIONS
    DESCRIPCION = "Analiza una expresión regular, construye su AFN-λ por partes y lo lleva hasta el AFD mínimo."
    USA_AUTOMATA = True
    PASOS = [
        "Escriba la expresión: + es unión, la yuxtaposición concatena, * es la estrella; λ (o ε) y ∅ (o Ø).",
        "Mientras escribe se revisa la sintaxis; un error se señala con ^ bajo el carácter que lo provoca.",
        "Pulse «Construir» y recorra cada etapa con «Anterior/Siguiente»: casos básicos, uniones, concatenaciones…",
        "«Guardar .jff» exporta el autómata de la etapa elegida; «Usar» lo vuelve el autómata activo.",
        "Pruebe palabras abajo: se validan con el AFD mínimo y se comparan con re.fullmatch.",
    ]

    def contenido(self) -> ft.Control:
        self.entrada = ft.TextField(label="Expresión regular", value="(a + b)*abb", expand=True,
                                    text_style=ft.TextStyle(font_family=MONO, size=16),
                                    on_change=lambda e: self.revisar(), on_submit=lambda e: self.ejecutar(self.construir))
        self.ejemplos = ft.Dropdown(label="Casos de prueba", width=230,
                                    options=[ft.DropdownOption(key=k, text=k) for k in EJEMPLOS],
                                    on_select=lambda e: self._ejemplo(e.control.value))
        self.marca = ft.Text("", font_family=MONO, size=14, color=Paleta.ERROR)
        self.info = ft.Column(spacing=4)
        self.metricas = ft.Row(wrap=True, spacing=10)
        self.selector = ft.SegmentedButton(segments=[ft.Segment(value=k, label=ft.Text(t)) for k, t in ETAPAS],
                                           selected=["thompson"], on_change=lambda e: self._mostrar())
        self.visor = VisorEtapas(lambda m: Diagrama(760, 330).dibujar(m))
        self.palabra = ft.TextField(label="Palabra", width=300, text_style=ft.TextStyle(font_family=MONO),
                                    on_change=lambda e: self.ejecutar(self.probar), hint_text="vacío = λ")
        self.veredicto = Veredicto()
        self._etapas: dict[str, object] = {}
        clases = ", ".join(f"{n} = {d}" for n, d in Clases.catalogo())
        return ft.Column([
            tarjeta(ft.Column([ft.Row([self.entrada, self.ejemplos]), self.marca, self.info,
                               ft.Text(f"Clases disponibles: {clases}.", size=12, color=Paleta.TENUE),
                               ft.Row([ft.FilledButton("Construir", icon=ft.Icons.BUILD,
                                                       on_click=lambda e: self.ejecutar(self.construir))])],
                              spacing=10), "Expresión", ft.Icons.EDIT),
            tarjeta(ft.Column([self.metricas, ft.Row([self.selector], scroll=ft.ScrollMode.AUTO), self.visor,
                               ft.Row([ft.FilledButton("Usar", icon=ft.Icons.CHECK,
                                                       on_click=lambda e: self.ejecutar(self.usar)),
                                       ft.OutlinedButton("Guardar .jff", icon=ft.Icons.SAVE_ALT,
                                                         on_click=lambda e: self.ejecutar(self.guardar)),
                                       ft.OutlinedButton("Guardar las cuatro", icon=ft.Icons.SAVE,
                                                         on_click=lambda e: self.ejecutar(self.guardar_todas))])],
                              spacing=12), "Construcción paso a paso", ft.Icons.STAIRS),
            tarjeta(ft.Column([self.palabra, self.veredicto], spacing=10), "Probar palabras", ft.Icons.KEYBOARD)],
            spacing=16)

    def al_mostrar(self) -> None:
        if not self._etapas:
            self.revisar(refrescar=False)
            self.ejecutar(self.construir)

    def _ejemplo(self, clave: str) -> None:
        self.entrada.value = EJEMPLOS[clave]
        self.revisar(refrescar=False)
        self.ejecutar(self.construir)

    def revisar(self, refrescar: bool = True) -> ExpresionRegular | None:
        texto = self.entrada.value or ""
        try:
            e = ExpresionRegular(texto)
            self.entrada.error = None
            self.marca.value = ""
            self.marca.visible = False
            self.info.controls = [
                ft.Text(pantalla(f"Notación normalizada: {e.notacion}"), font_family=MONO, size=13, selectable=True),
                ft.Text(f"Patrón para re: {e.python}", font_family=MONO, size=12, color=Paleta.TENUE, selectable=True),
                ft.Text(f"Σ = {{{', '.join(e.alfabeto)}}}" if len(e.alfabeto) < 20 else f"|Σ| = {len(e.alfabeto)}",
                        font_family=MONO, size=12, color=Paleta.TENUE)]
        except ExpresionInvalida as exc:
            e = None
            self.entrada.error = exc.detalle
            self.marca.value = texto + "\n" + " " * exc.posicion + "^"
            self.marca.visible = True
            self.info.controls = []
        if refrescar:
            self.refrescar()
        return e

    def construir(self) -> None:
        e = self.revisar(refrescar=False)
        if e is None:
            raise ErrorTC("Corrija la expresión antes de construir.")
        thompson = ConstruccionThompson(e).resolver()
        cadena = thompson.hacia_minimo()
        self._thompson, self._cadena, self._expresion = thompson, cadena, e
        self._etapas = {"thompson": (thompson.etapas, thompson.automata), "lambda": None, "subconjuntos": None,
                        "minimo": (cadena.minimo.etapas, cadena.minimo.salida)}
        if cadena.sin_lambda:
            self._etapas["lambda"] = (cadena.sin_lambda.etapas, cadena.sin_lambda.salida)
        if cadena.determinista:
            self._etapas["subconjuntos"] = (cadena.determinista.etapas, cadena.determinista.salida)
        conteos = [("thompson", "AFN-λ"), ("lambda", "AFN"), ("subconjuntos", "AFD"), ("minimo", "AFD mínimo")]
        piezas = []
        for clave, nombre in conteos:
            par = self._etapas[clave]
            if piezas:
                piezas.append(ft.Icon(ft.Icons.ARROW_FORWARD, color=Paleta.BORDE))
            piezas.append(metrica(str(len(par[1].estados)) if par else "—", nombre))
        self.metricas.controls = piezas
        self.selector.selected = ["thompson"]
        self._mostrar(refrescar=False)
        self.aviso.mostrar(f"{e.notacion}: {len(thompson.etapas)} construcciones; el AFD mínimo tiene "
                           f"{len(cadena.afd_minimo.estados)} estados.", "ok")

    def _mostrar(self, refrescar: bool = True) -> None:
        par = self._etapas.get(next(iter(self.selector.selected)))
        self.visor.cargar(par[0] if par else [])
        if refrescar:
            self.refrescar()

    def _automata_actual(self):
        par = self._etapas.get(next(iter(self.selector.selected)))
        if not par:
            raise ErrorTC("Esta etapa no aplica a la expresión (no produjo un autómata).")
        return par[1]

    def usar(self) -> None:
        m = self._automata_actual()
        self.sesion.usar(m)
        self.aviso.mostrar(f"El {m.tipo} de {len(m.estados)} estados es ahora el autómata activo.", "ok")

    def guardar(self) -> None:
        etapa = next(iter(self.selector.selected))
        ruta = Archivos.guardar(self._automata_actual(), self.salida(f"er-{etapa}.jff"))
        self.aviso.mostrar(f"Guardado en {ruta}", "ok")

    def guardar_todas(self) -> None:
        rutas = [Archivos.guardar(par[1], self.salida(f"er-{k}.jff")) for k, par in self._etapas.items() if par]
        self.aviso.mostrar(f"Se guardaron {len(rutas)} autómatas en {rutas[0].parent}", "ok")

    def probar(self) -> None:
        if not self._etapas:
            raise ErrorTC("Construya primero el autómata.")
        texto = (self.palabra.value or "").strip()
        texto = "" if texto in ("λ", "ε") else texto
        m = self._cadena.afd_minimo
        ajenos = sorted({c for c in texto if c not in m.alfabeto})
        if ajenos:
            self.veredicto.mostrar(False, f"Usa {' '.join(ajenos)}, que no está en Σ.")
            return
        r = m.recorrer(texto)
        coincide = self._expresion.coincide(texto)
        detalle = (f"AFD mínimo: {'acepta' if r.aceptada else 'rechaza'} · re.fullmatch: "
                   f"{'coincide' if coincide else 'no coincide'}"
                   + ("" if coincide == r.aceptada else "  ⚠ los modelos difieren"))
        self.veredicto.mostrar(r.aceptada, detalle)
