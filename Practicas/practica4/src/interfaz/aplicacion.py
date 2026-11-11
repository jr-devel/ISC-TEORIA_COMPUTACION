"""Ventana principal: menú lateral, barra de estado y área de contenido."""

from __future__ import annotations

import os
from typing import Sequence

import flet as ft

from .sesion import Sesion
from pathlib import Path

from .tema import FUENTES, Paleta, pantalla, tema
from .vistas.base import Vista


class Aplicacion:
    """Arma la ventana con las secciones que habilita cada práctica.

    Variables de entorno opcionales: ``TC_SECCION`` abre directamente una
    sección por su clave (por ejemplo ``simulador``) y ``TC_AUTOMATA`` carga
    un autómata al iniciar (ruta relativa a la carpeta de la práctica).
    """

    def __init__(self, page: ft.Page, titulo: str, subtitulo: str, vistas: Sequence[type[Vista]]) -> None:
        self.page = page
        self.sesion = Sesion()
        self.sesion.navegar = self.ir_a
        self.sesion.secciones = [(c.CLAVE, c.TITULO, c.ICONO, c.DESCRIPCION) for c in vistas]
        self.vistas = [clase(self.sesion) for clase in vistas]
        for v in self.vistas:
            v.page = page
        self.titulo, self.subtitulo = titulo, subtitulo
        self.area = ft.Container(expand=True, padding=ft.Padding.only(left=28, right=28, top=22, bottom=10))
        self.estado = ft.Text("", size=13, color=Paleta.TENUE)
        self.chip = ft.Container(visible=any(v.USA_AUTOMATA for v in self.vistas))
        self.menu = ft.NavigationRail(
            selected_index=0, extended=True, min_extended_width=230, bgcolor=Paleta.SUPERFICIE,
            indicator_color=Paleta.GUINDA_CLARO, label_type=None, group_alignment=-0.9,
            leading=self._marca(), on_change=lambda e: self._seleccionar(e.control.selected_index),
            destinations=[ft.NavigationRailDestination(icon=v.ICONO, label=v.TITULO) for v in self.vistas])
        self.sesion.al_cambiar(lambda m: self._actualizar_chip())
        self._actualizar_chip()

    def _marca(self) -> ft.Control:
        return ft.Container(ft.Column([
            ft.Row([ft.Container(ft.Text("TC", size=16, weight=ft.FontWeight.BOLD, color=Paleta.SUPERFICIE),
                                 bgcolor=Paleta.GUINDA, border_radius=10, padding=ft.Padding.symmetric(horizontal=10, vertical=8)),
                    ft.Column([ft.Text("Laboratorio de", size=11, color=Paleta.TENUE),
                               ft.Text("Autómatas", size=16, weight=ft.FontWeight.BOLD, color=Paleta.GUINDA)],
                              spacing=0)], spacing=10),
            ft.Container(ft.Text(self.subtitulo, size=11, color=Paleta.SUPERFICIE, weight=ft.FontWeight.W_600),
                         bgcolor=Paleta.DORADO, border_radius=20, padding=ft.Padding.symmetric(horizontal=10, vertical=3))],
            spacing=10), padding=ft.Padding.only(left=16, top=18, bottom=18, right=8))

    def _actualizar_chip(self) -> None:
        m = self.sesion.automata
        if m is None:
            contenido = [ft.Icon(ft.Icons.INFO_OUTLINE, size=16, color=Paleta.TENUE),
                         ft.Text("Sin autómata activo", size=13, color=Paleta.TENUE)]
        else:
            contenido = [ft.Icon(ft.Icons.MEMORY, size=16, color=Paleta.GUINDA),
                         ft.Text(pantalla(f"{m.nombre or 'sin nombre'} · {m.tipo} · {len(m.estados)} estados"),
                                 size=13, color=Paleta.GUINDA, weight=ft.FontWeight.W_600)]
        self.chip.content = ft.Row(contenido, spacing=6, tight=True)
        self.chip.padding = ft.Padding.symmetric(horizontal=12, vertical=6)
        self.chip.border_radius = 20
        self.chip.bgcolor = Paleta.GUINDA_CLARO if m else "#EFEBED"
        self.chip.tooltip = "Autómata con el que trabajan el simulador y los algoritmos"

    def _barra(self) -> ft.Control:
        return ft.Container(ft.Row([
            ft.Text(self.titulo, size=13, color=Paleta.TENUE), ft.Container(expand=True), self.chip]),
            padding=ft.Padding.symmetric(horizontal=28, vertical=10), bgcolor=Paleta.SUPERFICIE,
            border=ft.Border.only(bottom=ft.BorderSide(1, Paleta.BORDE)))

    def _seleccionar(self, indice: int) -> None:
        vista = self.vistas[indice]
        self.menu.selected_index = indice
        self.area.content = vista.control()
        vista.al_mostrar()
        self.page.update()

    def ir_a(self, clave: str) -> None:
        for i, v in enumerate(self.vistas):
            if v.CLAVE == clave:
                self._seleccionar(i)
                return

    def montar(self) -> None:
        p = self.page
        p.title = f"Laboratorio de Autómatas · {self.subtitulo}"
        p.fonts = FUENTES
        p.theme = tema()
        p.theme_mode = ft.ThemeMode.LIGHT
        p.bgcolor = Paleta.FONDO
        p.padding = 0
        p.add(ft.Row([self.menu, ft.VerticalDivider(width=1, color=Paleta.BORDE),
                      ft.Column([self._barra(), self.area], expand=True, spacing=0)], expand=True, spacing=0))
        self._precargar(os.environ.get("TC_AUTOMATA", ""))
        inicial = os.environ.get("TC_SECCION", "")
        indice = next((i for i, v in enumerate(self.vistas) if v.CLAVE == inicial), 0)
        self._seleccionar(indice)


    def _precargar(self, ruta: str) -> None:
        """Abre un autómata al iniciar si ``TC_AUTOMATA`` indica un archivo."""
        if not ruta:
            return
        try:
            from nucleo.formatos import Archivos
        except ImportError:          # la Práctica 1 no incluye autómatas
            return
        destino = Path(ruta)
        self.sesion.usar(Archivos.abrir(destino if destino.is_absolute() else self.sesion.raiz / destino))


def iniciar(titulo: str, subtitulo: str, vistas: Sequence[type[Vista]]) -> None:
    """Punto de entrada: escritorio por omisión; navegador si ``FLET_FORCE_WEB_SERVER`` está activo."""

    def principal(page: ft.Page) -> None:
        Aplicacion(page, titulo, subtitulo, vistas).montar()

    ft.run(principal, assets_dir=str(Path(__file__).resolve().parent / "recursos"))
