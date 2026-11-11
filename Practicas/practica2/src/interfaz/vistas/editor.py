"""Definición interactiva de un autómata (Práctica 2, 3.1)."""

from __future__ import annotations

import flet as ft

from nucleo.automata import EPSILON, LAMBDA, Automata, Clasificador
from nucleo.errores import ErrorTC
from nucleo.lenguajes import separar

from ..componentes import boton, tabla, tarjeta
from ..diagrama import Diagrama
from ..tema import MONO, Paleta, pantalla
from .base import Vista

EJEMPLOS = {
    "par": ("AFD · número par de aes", "a, b", "P, I", "P", ["P"],
            {("P", "a"): "I", ("P", "b"): "P", ("I", "a"): "P", ("I", "b"): "I"}),
    "ab": ("AFN · termina en ab", "a, b", "q0, q1, q2", "q0", ["q2"],
           {("q0", "a"): "q0, q1", ("q0", "b"): "q0", ("q1", "b"): "q2"}),
    "lambda": ("AFN-λ · a*b* ∪ c", "a, b, c", "s, A, B, C", "s", ["B", "C"],
               {("s", ""): "A, C", ("A", "a"): "A", ("A", ""): "B", ("B", "b"): "B", ("C", "c"): "C"}),
}


class Editor(Vista):
    CLAVE = "editor"
    TITULO = "Editor"
    ICONO = ft.Icons.EDIT_SQUARE
    DESCRIPCION = "Defina la quíntupla (Q, Σ, δ, q₀, F) llenando una tabla; la vista previa se actualiza sola."
    USA_AUTOMATA = True
    PASOS = [
        "Escriba Σ y Q separando con comas. La tabla de transiciones se ajusta sola y conserva lo ya escrito.",
        "Elija el estado inicial y marque los de aceptación tocando sus pastillas.",
        "En cada celda escriba los destinos separados por comas; una celda vacía significa «sin transición».",
        "Active «Transiciones λ» para agregar la columna λ. El tipo (AFD, AFN o AFN-λ) se deduce solo.",
        "Pulse «Usar este autómata» para simularlo o transformarlo en las demás secciones.",
    ]

    def contenido(self) -> ft.Control:
        self.sigma = ft.TextField(label="Alfabeto Σ", value="a, b", width=220, on_change=lambda e: self._estructura())
        self.estados = ft.TextField(label="Estados Q", value="q0, q1", width=260, on_change=lambda e: self._estructura())
        self.inicial = ft.Dropdown(label="Inicial q₀", width=160, on_select=lambda e: self._previa())
        self.con_lambda = ft.Switch(label="Transiciones λ", value=False, on_change=lambda e: self._estructura())
        self.nombre = ft.TextField(label="Nombre", value="mi-automata", width=200)
        self.finales = ft.Row(wrap=True, spacing=6)
        self._marcados: set[str] = set()
        self.rejilla = ft.Column(spacing=6)
        self._celdas: dict[tuple[str, str], ft.TextField] = {}
        self.tipo = ft.Container()
        self.diagrama = Diagrama(720, 340)
        self.tabla = ft.Column()
        self.ejemplo = ft.Dropdown(label="Cargar un ejemplo", width=240,
                                   options=[ft.DropdownOption(key=k, text=v[0]) for k, v in EJEMPLOS.items()],
                                   on_select=lambda e: self.ejecutar(lambda: self.cargar_ejemplo(e.control.value)))
        componentes = tarjeta(ft.Column([
            ft.Row([self.sigma, self.estados, self.inicial, self.nombre], wrap=True, spacing=12),
            ft.Row([ft.Text("Aceptación F:", size=13, color=Paleta.TENUE), self.finales], wrap=True),
            ft.Row([self.con_lambda, self.ejemplo,
                    boton("Editar el autómata activo", ft.Icons.DOWNLOAD, lambda: self.ejecutar(self.editar_activo),
                          False)], wrap=True, spacing=16)], spacing=12),
            "1 · Componentes", ft.Icons.LIST)
        transiciones = tarjeta(ft.Row([self.rejilla], scroll=ft.ScrollMode.AUTO), "2 · Función de transición δ",
                               ft.Icons.GRID_ON)
        previa = tarjeta(ft.Column([self.tipo, self.diagrama, self.tabla,
                                    ft.Row([boton("Usar este autómata", ft.Icons.CHECK, lambda: self.ejecutar(self.usar)),
                                            boton("Ir al simulador", ft.Icons.PLAY_CIRCLE_OUTLINE,
                                                  lambda: self.sesion.navegar("simulador"), False)])],
                                   spacing=12), "3 · Vista previa", ft.Icons.VISIBILITY)
        self.cargar_ejemplo("par", refrescar=False)
        return ft.Column([componentes, transiciones, previa], spacing=16)

    # ------------------------------------------------------------------
    def _simbolos(self) -> list[str]:
        simbolos = separar(self.sigma.value)
        return simbolos + ([EPSILON] if self.con_lambda.value else [])

    def _estructura(self, valores: dict[tuple[str, str], str] | None = None, refrescar: bool = True) -> None:
        """Rehace selector inicial, pastillas de F y rejilla conservando lo escrito."""
        estados, simbolos = separar(self.estados.value), self._simbolos()
        previos = {k: c.value for k, c in self._celdas.items()}
        if valores is not None:
            previos = valores
        self.inicial.options = [ft.DropdownOption(key=q, text=q) for q in estados]
        if self.inicial.value not in estados:
            self.inicial.value = estados[0] if estados else None
        self._marcados &= set(estados)
        self.finales.controls = [ft.Chip(label=ft.Text(q), selected=q in self._marcados,
                                         selected_color=Paleta.GUINDA_CLARO,
                                         on_select=lambda e, q=q: self._alternar_final(q)) for q in estados]
        encabezado = [ft.Container(ft.Text("δ", weight=ft.FontWeight.BOLD), width=90)]
        encabezado += [ft.Container(ft.Text(a or LAMBDA, weight=ft.FontWeight.BOLD, color=Paleta.GUINDA), width=150)
                       for a in simbolos]
        filas = [ft.Row(encabezado)]
        self._celdas = {}
        for q in estados:
            fila = [ft.Container(ft.Text(("→ " if q == self.inicial.value else "") + q +
                                         (" *" if q in self._marcados else ""), font_family=MONO), width=90)]
            for a in simbolos:
                campo = ft.TextField(value=previos.get((q, a), ""), width=150, dense=True, hint_text="—",
                                     text_style=ft.TextStyle(font_family=MONO), on_change=lambda e: self._previa())
                self._celdas[(q, a)] = campo
                fila.append(campo)
            filas.append(ft.Row(fila))
        self.rejilla.controls = filas
        self._previa(refrescar)

    def _alternar_final(self, q: str) -> None:
        self._marcados ^= {q}
        self._estructura()

    def construir(self) -> Automata:
        tabla_delta = {clave: separar(campo.value) for clave, campo in self._celdas.items()}
        return Automata.desde_tabla(separar(self.estados.value), separar(self.sigma.value), self.inicial.value or "",
                                    sorted(self._marcados), tabla_delta, self.nombre.value.strip() or "sin-nombre")

    def _previa(self, refrescar: bool = True) -> None:
        try:
            m = self.construir()
            self.diagrama.dibujar(m)
            self.tabla.controls = [tabla(*m.tabla())]
            color = {"AFD": Paleta.EXITO, "AFN": Paleta.INFO}.get(m.tipo, Paleta.DORADO)
            self.tipo.content = ft.Row([
                ft.Container(ft.Text(m.tipo, color=Paleta.SUPERFICIE, weight=ft.FontWeight.BOLD), bgcolor=color,
                             border_radius=20, padding=ft.Padding.symmetric(horizontal=12, vertical=4)),
                ft.Text(pantalla(Clasificador.motivo(m)), size=13, color=Paleta.TENUE, expand=True)])
        except ErrorTC as exc:
            self.diagrama.dibujar(None)
            self.tabla.controls = []
            self.tipo.content = ft.Row([ft.Icon(ft.Icons.WARNING_AMBER, color=Paleta.ERROR),
                                        ft.Text(pantalla(str(exc)), color=Paleta.ERROR, expand=True)])
        if refrescar:
            self.refrescar()

    # -- acciones -------------------------------------------------------------------
    def usar(self) -> None:
        m = self.construir()
        self.sesion.usar(m)
        self.aviso.mostrar(f"«{m.nombre}» es ahora el autómata activo: {m.tipo} con {len(m.estados)} estados.", "ok")

    def cargar(self, m: Automata, refrescar: bool = True) -> None:
        self.sigma.value = ", ".join(m.alfabeto)
        self.estados.value = ", ".join(m.estados)
        self.inicial.value = m.inicial
        self.nombre.value = m.nombre or "sin-nombre"
        self.con_lambda.value = m.tiene_lambda
        self._marcados = set(m.finales)
        valores = {(q, a): ", ".join(m.orden(m.destinos(q, a))) for q in m.estados for a in m.columnas()}
        self._estructura(valores, refrescar)

    def cargar_ejemplo(self, clave: str, refrescar: bool = True) -> None:
        _, sigma, estados, inicial, finales, delta = EJEMPLOS[clave]
        self.sigma.value, self.estados.value = sigma, estados
        self.con_lambda.value = any(a == "" for _, a in delta)
        self.inicial.value = inicial
        self._marcados = set(finales)
        self.nombre.value = f"ejemplo-{clave}"
        self._estructura(dict(delta), refrescar)

    def editar_activo(self) -> None:
        self.cargar(self.exigir_automata())
        self.aviso.mostrar("Se cargó el autómata activo; los cambios se aplican al pulsar «Usar este autómata».", "info")
