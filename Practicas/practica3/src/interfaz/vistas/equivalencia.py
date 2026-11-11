"""¿Reconocen dos autómatas el mismo lenguaje? (Práctica 3, 2.4)."""

from __future__ import annotations

from pathlib import Path

import flet as ft

from nucleo.algoritmos import Equivalencia as Prueba
from nucleo.errores import ErrorTC
from nucleo.formatos import Archivos

from ..componentes import Veredicto, tabla, tarjeta
from ..tema import Paleta
from .base import Vista

ACTIVO = "__activo__"


class Equivalencia(Vista):
    CLAVE = "equivalencia"
    TITULO = "Equivalencia"
    ICONO = ft.Icons.COMPARE_ARROWS
    DESCRIPCION = "Compara dos autómatas por sus AFD mínimos y, si difieren, da la palabra más corta que los separa."
    USA_AUTOMATA = True
    PASOS = [
        "Elija el primer autómata (puede ser el activo) y el segundo de la biblioteca; escriba en la lista para filtrar.",
        "Pulse «Comparar». Ambos se llevan a AFD mínimo completo sobre la unión de sus alfabetos.",
        "Si los mínimos coinciden salvo el nombre de los estados, son equivalentes y se muestra la correspondencia.",
        "Si no, se muestra el contraejemplo más corto: una palabra que uno acepta y el otro no.",
    ]

    def contenido(self) -> ft.Control:
        self.primero = ft.Dropdown(label="Primer autómata", width=420, enable_filter=True, editable=True)
        self.segundo = ft.Dropdown(label="Segundo autómata", width=420, enable_filter=True, editable=True)
        self.veredicto = Veredicto()
        self.detalle = ft.ResponsiveRow(spacing=16)
        return ft.Column([
            tarjeta(ft.Column([ft.Row([self.primero, self.segundo], wrap=True, spacing=16),
                               ft.FilledButton("Comparar", icon=ft.Icons.COMPARE_ARROWS,
                                               on_click=lambda e: self.ejecutar(self.comparar))], spacing=12),
                    "Autómatas", ft.Icons.LIBRARY_BOOKS),
            self.veredicto, self.detalle], spacing=16)

    def al_mostrar(self) -> None:
        opciones = [ft.DropdownOption(key=ACTIVO, text="◆ autómata activo")] if self.sesion.automata else []
        biblioteca = self.sesion.biblioteca
        if biblioteca.is_dir():
            opciones += [ft.DropdownOption(key=str(p), text=str(p.relative_to(biblioteca)))
                         for p in sorted(biblioteca.rglob("*")) if p.suffix in Archivos.extensiones()]
        self.primero.options = opciones
        self.segundo.options = [o for o in opciones if o.key != ACTIVO]
        if self.primero.value is None and opciones:
            self.primero.value = opciones[0].key

    def _cargar(self, valor: str | None):
        if not valor:
            raise ErrorTC("Elija los dos autómatas.")
        if valor == ACTIVO:
            return self.exigir_automata()
        return Archivos.abrir(Path(valor))

    def comparar(self) -> None:
        a, b = self._cargar(self.primero.value), self._cargar(self.segundo.value)
        v = Prueba(a, b).resolver()
        self.veredicto.mostrar(v.equivalentes, v.explicacion, "EQUIVALENTES" if v.equivalentes else "NO EQUIVALENTES")
        bloques = [tarjeta(ft.Column([ft.Text(e.explicacion, size=13, color=Paleta.TENUE),
                                      tabla(e.encabezados, e.filas) if e.encabezados else ft.Container()]),
                           e.titulo, ft.Icons.TABLE_CHART, col={"xs": 12, "lg": 4}) for e in v.etapas]
        self.detalle.controls = bloques
