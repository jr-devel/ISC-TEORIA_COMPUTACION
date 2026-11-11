"""De autómata a expresión regular: eliminación de estados y lema de Arden (Práctica 4, Ejercicio 3)."""

from __future__ import annotations

from pathlib import Path

import flet as ft

from nucleo.errores import ErrorTC
from nucleo.expresiones import ExpresionRegular
from nucleo.formatos import Archivos
from nucleo.kleene import EliminacionDeEstados, SistemaArden, comparar, verificar_determinismo
from nucleo.lenguajes import separar

from ..componentes import Veredicto, VisorEtapas, tarjeta
from ..diagrama import Diagrama
from ..tema import MONO, Paleta, pantalla
from .base import Vista

ACTIVO = "__activo__"


class AutomataAER(Vista):
    CLAVE = "afd-er"
    TITULO = "AFD → ER"
    ICONO = ft.Icons.SWAP_HORIZ
    DESCRIPCION = "Obtiene la expresión regular de un AFD eliminando estados (o con el lema de Arden), paso a paso."
    USA_AUTOMATA = True
    PASOS = [
        "Elija el AFD: el activo o uno de la biblioteca. Si no es determinista se indica qué estado y símbolo lo impiden.",
        "Elija el método. En la eliminación puede fijar el orden (por ejemplo «B, C, A»); si lo deja vacío se usa "
        "el estado que crea menos aristas.",
        "Recorra los pasos: después de eliminar cada estado se muestra el autómata generalizado como tabla.",
        "Para comparar con el resultado de JFLAP, péguelo en «Comparar con» y pulse el botón: ambas expresiones se "
        "convierten en AFD mínimos y se prueban por equivalencia.",
    ]

    def contenido(self) -> ft.Control:
        self.fuente = ft.Dropdown(label="Autómata", width=420, enable_filter=True, editable=True,
                                  on_select=lambda e: self.ejecutar(self.revisar))
        self.metodo = ft.SegmentedButton(segments=[ft.Segment(value="eliminacion", label=ft.Text("Eliminación de estados")),
                                                   ft.Segment(value="arden", label=ft.Text("Lema de Arden"))],
                                         selected=["eliminacion"])
        self.orden = ft.TextField(label="Orden de eliminación (opcional)", width=360)
        self.determinismo = ft.Row()
        self.diagrama = Diagrama(640, 280)
        self.visor = VisorEtapas()
        self.resultado = ft.Text("", font_family=MONO, size=18, weight=ft.FontWeight.BOLD, color=Paleta.GUINDA,
                                 selectable=True)
        self.otra = ft.TextField(label="Comparar con (por ejemplo, la expresión de JFLAP)", expand=True,
                                 text_style=ft.TextStyle(font_family=MONO))
        self.veredicto = Veredicto()
        self._automata = None
        self._expresion = None
        return ft.Column([
            tarjeta(ft.Column([ft.Row([self.fuente, self.orden], wrap=True, spacing=16), self.determinismo,
                               self.diagrama, ft.Row([self.metodo], scroll=ft.ScrollMode.AUTO),
                               ft.FilledButton("Obtener la expresión", icon=ft.Icons.PLAY_ARROW,
                                               on_click=lambda e: self.ejecutar(self.convertir))], spacing=12),
                    "Autómata", ft.Icons.ACCOUNT_TREE),
            tarjeta(ft.Column([self.visor, ft.Divider(), ft.Text("Expresión obtenida", size=13, color=Paleta.TENUE),
                               self.resultado], spacing=10), "Pasos", ft.Icons.STAIRS),
            tarjeta(ft.Column([ft.Row([self.otra, ft.FilledButton("Comparar", icon=ft.Icons.COMPARE_ARROWS,
                                                                  on_click=lambda e: self.ejecutar(self.comparar))]),
                               self.veredicto], spacing=10), "Comparación", ft.Icons.COMPARE)], spacing=16)

    def al_mostrar(self) -> None:
        opciones = [ft.DropdownOption(key=ACTIVO, text="◆ autómata activo")] if self.sesion.automata else []
        if self.sesion.biblioteca.is_dir():
            opciones += [ft.DropdownOption(key=str(p), text=str(p.relative_to(self.sesion.biblioteca)))
                         for p in sorted(self.sesion.biblioteca.rglob("*.jff"))]
        self.fuente.options = opciones
        if self.fuente.value is None and opciones:
            self.fuente.value = opciones[0].key
            self.ejecutar(self.revisar)

    def revisar(self) -> None:
        valor = self.fuente.value
        if not valor:
            raise ErrorTC("Elija un autómata.")
        m = self.exigir_automata() if valor == ACTIVO else Archivos.abrir(Path(valor))
        self._automata = m
        ok, mensaje = verificar_determinismo(m)
        self.determinismo.controls = [ft.Icon(ft.Icons.CHECK_CIRCLE if ok else ft.Icons.WARNING_AMBER,
                                              color=Paleta.EXITO if ok else Paleta.ERROR),
                                      ft.Text(pantalla(mensaje), color=Paleta.EXITO if ok else Paleta.ERROR, expand=True)]
        self.diagrama.dibujar(m)
        self.orden.hint_text = ", ".join(m.estados)

    def convertir(self) -> None:
        if self._automata is None:
            self.revisar()
        m = self._automata
        ok, mensaje = verificar_determinismo(m)
        if not ok:
            raise ErrorTC(mensaje + " Conviértalo primero en AFD (sección Transformaciones).")
        if next(iter(self.metodo.selected)) == "arden":
            r = SistemaArden(m).resolver()
        else:
            orden = separar(self.orden.value or "")
            r = EliminacionDeEstados(m, orden or None).resolver()
        self._expresion = r.expresion
        self.visor.cargar(r.etapas)
        self.resultado.value = pantalla(r.notacion)
        self.aviso.mostrar(f"Orden usado: {', '.join(r.orden)}. Longitud de la expresión: {len(r.notacion)} caracteres.",
                           "ok")

    def comparar(self) -> None:
        if self._expresion is None:
            raise ErrorTC("Obtenga primero la expresión.")
        otra = ExpresionRegular(self.otra.value or "")
        v = comparar(self._expresion.notacion(), otra)
        self.veredicto.mostrar(v.equivalentes, v.explicacion, "EQUIVALENTES" if v.equivalentes else "NO EQUIVALENTES")
