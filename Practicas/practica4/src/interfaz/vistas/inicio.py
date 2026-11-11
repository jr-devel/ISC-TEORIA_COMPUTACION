"""Pantalla de bienvenida con accesos directos a cada sección."""

from __future__ import annotations

import flet as ft

from ..componentes import titulo
from ..tema import RADIO, Paleta, pantalla
from .base import Vista


class Inicio(Vista):
    CLAVE = "inicio"
    TITULO = "Inicio"
    ICONO = ft.Icons.HOME_OUTLINED
    DESCRIPCION = "Elija una herramienta. Cada sección explica sus pasos con el botón «¿Cómo se usa?»."

    def contenido(self) -> ft.Control:
        tarjetas = []
        for clave, nombre, icono, descripcion in self.sesion.secciones:
            if clave == self.CLAVE:
                continue
            tarjetas.append(ft.Container(
                ft.Column([
                    ft.Container(ft.Icon(icono, color=Paleta.GUINDA, size=26), bgcolor=Paleta.GUINDA_CLARO,
                                 border_radius=12, padding=10),
                    titulo(nombre, 16),
                    ft.Text(pantalla(descripcion), size=13, color=Paleta.TENUE),
                    ft.Row([ft.Text("Abrir", color=Paleta.GUINDA, weight=ft.FontWeight.W_600),
                            ft.Icon(ft.Icons.ARROW_FORWARD, color=Paleta.GUINDA, size=18)], spacing=4)],
                    spacing=10),
                bgcolor=Paleta.SUPERFICIE, border_radius=RADIO, border=ft.Border.all(1, Paleta.BORDE), padding=18,
                col={"xs": 12, "md": 6, "xl": 4}, ink=True,
                on_click=lambda e, c=clave: self.sesion.navegar(c)))
        flujo = self._flujo()
        return ft.Column([flujo, ft.ResponsiveRow(tarjetas, spacing=16, run_spacing=16)], spacing=20)

    def _flujo(self) -> ft.Control:
        claves = [c for c, *_ in self.sesion.secciones]
        if "editor" in claves:
            pasos = [("1", "Cree o abra un autómata", "Editor o Biblioteca"),
                     ("2", "Pruébelo con palabras", "Simulador"),
                     ("3", "Transfórmelo o conviértalo", "secciones de algoritmos")]
        else:
            pasos = [("1", "Escriba un alfabeto", "por ejemplo a, b"),
                     ("2", "Escriba una palabra o una longitud", "el resultado aparece al instante"),
                     ("3", "Guarde el resultado", "archivo .txt en salidas/")]
        piezas = []
        for numero, accion, detalle in pasos:
            piezas.append(ft.Row([
                ft.Container(ft.Text(numero, color=Paleta.SUPERFICIE, weight=ft.FontWeight.BOLD), width=30, height=30,
                             border_radius=15, bgcolor=Paleta.DORADO, alignment=ft.Alignment.CENTER),
                ft.Column([ft.Text(accion, weight=ft.FontWeight.W_600, size=14),
                           ft.Text(detalle, size=12, color=Paleta.TENUE)], spacing=0)], spacing=10, tight=True))
            piezas.append(ft.Icon(ft.Icons.CHEVRON_RIGHT, color=Paleta.BORDE))
        return ft.Container(ft.Row(piezas[:-1], wrap=True, spacing=14), bgcolor=Paleta.SUPERFICIE,
                            border_radius=RADIO, border=ft.Border.all(1, Paleta.BORDE), padding=18)
