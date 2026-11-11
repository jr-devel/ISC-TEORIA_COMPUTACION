"""Operaciones entre lenguajes finitos: unión, intersección, diferencia, concatenación, potencia y cerraduras."""

from __future__ import annotations

import flet as ft

from nucleo.errores import ErrorTC
from nucleo.lenguajes import Informe, Lenguaje

from ..componentes import boton, chips, metrica, tarjeta
from ..tema import MONO, Paleta
from .base import Vista


class Lenguajes(Vista):
    CLAVE = "lenguajes"
    TITULO = "Lenguajes"
    ICONO = ft.Icons.JOIN_INNER
    DESCRIPCION = "Operaciones entre lenguajes finitos escritos como conjuntos de palabras."
    PASOS = [
        "Escriba L₁ y L₂ como listas de palabras separadas por comas; use λ para la palabra vacía.",
        "Elija la operación. Para la potencia y las cerraduras indique n.",
        "En las cerraduras L* y L⁺, n es la longitud máxima de las palabras que se muestran.",
    ]
    OPERACIONES = [("union", "L₁ ∪ L₂"), ("interseccion", "L₁ ∩ L₂"), ("diferencia", "L₁ − L₂"),
                   ("concatenacion", "L₁L₂"), ("potencia", "L₁ⁿ"), ("inverso", "L₁ᴿ"), ("estrella", "L₁*"),
                   ("mas", "L₁⁺")]

    def contenido(self) -> ft.Control:
        estilo = ft.TextStyle(font_family=MONO)
        self.l1 = ft.TextField(label="L₁", value="a, ab, λ", text_style=estilo, expand=True,
                               on_change=lambda e: self.calcular())
        self.l2 = ft.TextField(label="L₂", value="ab, b", text_style=estilo, expand=True,
                               on_change=lambda e: self.calcular())
        self.n = ft.TextField(label="n", value="2", width=90, on_change=lambda e: self.calcular())
        self.operacion = ft.Dropdown(label="Operación", value="union", width=200,
                                     options=[ft.DropdownOption(key=k, text=t) for k, t in self.OPERACIONES],
                                     on_select=lambda e: self.calcular())
        self.metricas = ft.Row(spacing=10)
        self.resultado = ft.Column()
        self._informe: Informe | None = None
        entrada = tarjeta(ft.Column([ft.Row([self.l1, self.l2]), ft.Row([self.operacion, self.n,
                                     boton("Guardar .txt", ft.Icons.SAVE_ALT, lambda: self.ejecutar(self.guardar),
                                           False)])], spacing=14), "Lenguajes", ft.Icons.EDIT_NOTE)
        salida = tarjeta(ft.Column([self.metricas, self.resultado]), "Resultado", ft.Icons.LIST_ALT)
        self.calcular(primera=True)
        return ft.Column([entrada, salida], spacing=16)

    def calcular(self, primera: bool = False) -> None:
        try:
            l1, l2 = Lenguaje.leer(self.l1.value), Lenguaje.leer(self.l2.value)
            op = self.operacion.value
            n = int(self.n.value or 0)
            if n < 0 or n > 12:
                raise ValueError("n debe estar entre 0 y 12")
            r = {"union": lambda: l1 | l2, "interseccion": lambda: l1 & l2, "diferencia": lambda: l1 - l2,
                 "concatenacion": lambda: l1 * l2, "potencia": lambda: l1.potencia(n),
                 "inverso": l1.inverso, "estrella": lambda: l1.estrella(n), "mas": lambda: l1.mas(n)}[op]()
            textos = [str(p) for p in r]
            self._informe = Informe(f"{dict(self.OPERACIONES)[op]}", textos, {"L₁": str(l1), "L₂": str(l2)})
            self.metricas.controls = [metrica(str(len(l1)), "|L₁|"), metrica(str(len(l2)), "|L₂|"),
                                      metrica(str(len(r)), "|resultado|", Paleta.DORADO)]
            self.resultado.controls = [chips(textos, destacar=lambda t: t == "λ") if textos
                                       else ft.Text("∅  (lenguaje vacío)", color=Paleta.TENUE)]
            self.n.error = None
        except (ErrorTC, ValueError) as exc:
            self.n.error = str(exc) if isinstance(exc, ValueError) else None
            if isinstance(exc, ErrorTC):
                self.aviso.mostrar(str(exc), "error")
        if not primera:
            self.refrescar()

    def guardar(self) -> None:
        if self._informe is None:
            raise ErrorTC("No hay un resultado que guardar.")
        ruta = self._informe.guardar(self.salida(f"lenguajes-{self.operacion.value}.txt"))
        self.aviso.mostrar(f"Resultado guardado en {ruta}", "ok")
