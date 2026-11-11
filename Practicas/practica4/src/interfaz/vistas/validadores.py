"""Validadores construidos con expresiones regulares y autómatas (Práctica 4, Ejercicio 4)."""

from __future__ import annotations

import flet as ft

from nucleo.validadores import CATALOGO

from ..componentes import Veredicto, chips, metrica, tarjeta
from ..diagrama import Diagrama
from ..tema import MONO, Paleta, pantalla
from .base import Vista


class Validadores(Vista):
    CLAVE = "validadores"
    TITULO = "Validadores"
    ICONO = ft.Icons.VERIFIED_OUTLINED
    DESCRIPCION = "Correo, teléfono y URL: la expresión del curso, su traducción a re y el AFD que valida."
    PASOS = [
        "Elija el validador en la barra.",
        "Escriba un texto: se valida con el AFD mínimo mientras escribe y se indica dónde falla.",
        "Toque un ejemplo para probarlo. Abajo se listan los casos que la expresión deja fuera a propósito.",
    ]

    def contenido(self) -> ft.Control:
        self.selector = ft.SegmentedButton(segments=[ft.Segment(value=k, label=ft.Text(v.nombre))
                                                     for k, v in CATALOGO.items()],
                                           selected=[next(iter(CATALOGO))], on_change=lambda e: self.mostrar())
        self.texto = ft.TextField(label="Texto a validar", text_style=ft.TextStyle(font_family=MONO, size=16),
                                  on_change=lambda e: self.validar(), expand=True)
        self.veredicto = Veredicto()
        self.ficha = ft.Column(spacing=8)
        self.metricas = ft.Row(wrap=True, spacing=10)
        self.ejemplos = ft.Column(spacing=8)
        self.fuera = ft.Column(spacing=4)
        self.diagrama = Diagrama(760, 360)
        self.mostrar(refrescar=False)
        return ft.Column([
            ft.Row([self.selector], scroll=ft.ScrollMode.AUTO),
            tarjeta(ft.Column([self.texto, self.veredicto, self.ejemplos], spacing=10), "Probar", ft.Icons.KEYBOARD),
            tarjeta(ft.Column([self.ficha, self.metricas], spacing=10), "Expresión", ft.Icons.FUNCTIONS),
            tarjeta(self.diagrama, "AFD mínimo", ft.Icons.ACCOUNT_TREE),
            tarjeta(self.fuera, "Qué queda fuera", ft.Icons.REPORT_GMAILERRORRED)], spacing=16)

    def _actual(self):
        return CATALOGO[next(iter(self.selector.selected))]

    def mostrar(self, refrescar: bool = True) -> None:
        v = self._actual()
        self.ficha.controls = [
            ft.Text(pantalla(v.descripcion), size=13),
            ft.Text("Notación del curso", size=12, color=Paleta.TENUE),
            ft.Text(pantalla(v.expresion), font_family=MONO, size=13, selectable=True),
            ft.Text("Módulo re de Python", size=12, color=Paleta.TENUE),
            ft.Text(v.python, font_family=MONO, size=11, selectable=True, color=Paleta.INFO),
            ft.Text(f"Norma consultada: {v.norma}", size=12, color=Paleta.TENUE)]
        datos = v.estadisticas()
        self.metricas.controls = [metrica(str(n), k) for k, n in datos.items()]
        self.ejemplos.controls = [
            ft.Row([ft.Text("Válidos:", size=12, color=Paleta.EXITO, width=70), self._ejemplos(v.validos)]),
            ft.Row([ft.Text("Inválidos:", size=12, color=Paleta.ERROR, width=70), self._ejemplos(v.invalidos)])]
        self.fuera.controls = [ft.Row([ft.Icon(ft.Icons.REMOVE, size=16, color=Paleta.TENUE),
                                       ft.Text(pantalla(f), size=13, expand=True)]) for f in v.fuera]
        self.diagrama.dibujar(v.afd)
        self.texto.value = v.validos[0]
        self.validar(refrescar=refrescar)

    def _ejemplos(self, lista: list[str]) -> ft.Control:
        return ft.Row([ft.TextButton(w, on_click=lambda e, w=w: self._probar(w),
                                     style=ft.ButtonStyle(text_style=ft.TextStyle(font_family=MONO, size=12)))
                       for w in lista], wrap=True, spacing=2, expand=True)

    def _probar(self, w: str) -> None:
        self.texto.value = w
        self.validar()

    def validar(self, refrescar: bool = True) -> None:
        v = self._actual()
        texto = self.texto.value or ""
        ok, detalle = v.valida(texto)
        coincide = v.coincide_re(texto)
        self.veredicto.mostrar(ok, f"{detalle}  ·  re.fullmatch: {'coincide' if coincide else 'no coincide'}",
                               "VÁLIDO" if ok else "INVÁLIDO")
        if refrescar:
            self.refrescar()
