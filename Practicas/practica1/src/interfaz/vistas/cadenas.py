"""Operación 1 de la Práctica 1: prefijos, sufijos y subcadenas (y otras operaciones de palabras)."""

from __future__ import annotations

import flet as ft

from nucleo.errores import ErrorTC
from nucleo.lenguajes import Alfabeto, Informe, Palabra

from ..componentes import boton, chips, metrica, tarjeta
from ..tema import MONO, Paleta
from .base import Vista


class Cadenas(Vista):
    CLAVE = "cadenas"
    TITULO = "Palabras"
    ICONO = ft.Icons.TEXT_FIELDS
    DESCRIPCION = "Prefijos, sufijos, subcadenas, reflexión y potencia de una palabra, calculados al escribir."
    PASOS = [
        "Escriba el alfabeto Σ separando los símbolos con comas (a, b, c) o juntos (abc).",
        "Escriba la palabra; si usa un símbolo que no está en Σ, el campo lo señala en rojo.",
        "Elija la operación en la barra de botones; el resultado se actualiza solo.",
        "Pulse «Guardar .txt» para escribir el resultado en la carpeta salidas/.",
    ]
    OPERACIONES = [("prefijos", "Prefijos"), ("sufijos", "Sufijos"), ("subcadenas", "Subcadenas"),
                   ("inversa", "Reflexión"), ("potencia", "Potencia")]

    def contenido(self) -> ft.Control:
        self.sigma = ft.TextField(label="Alfabeto Σ", value="a, b, c", helper="Ejemplo: a, b, c",
                                  on_change=lambda e: self.calcular(), width=260)
        self.palabra = ft.TextField(label="Palabra ω", value="abcb", text_style=ft.TextStyle(font_family=MONO),
                                    on_change=lambda e: self.calcular(), width=300)
        self.exponente = ft.TextField(label="n", value="3", width=90, visible=False,
                                      keyboard_type=ft.KeyboardType.NUMBER, on_change=lambda e: self.calcular())
        self.operacion = ft.SegmentedButton(
            segments=[ft.Segment(value=v, label=ft.Text(t)) for v, t in self.OPERACIONES], selected=["prefijos"],
            on_change=lambda e: self.calcular())
        self.metricas = ft.Row(wrap=True, spacing=10)
        self.resultado = ft.Column()
        self.nota = ft.Text("", size=12, color=Paleta.TENUE)
        self._informe: Informe | None = None
        entrada = tarjeta(ft.Column([
            ft.Row([self.sigma, self.palabra, self.exponente], wrap=True, spacing=14),
            ft.Row([self.operacion], scroll=ft.ScrollMode.AUTO),
            ft.Row([boton("Guardar .txt", ft.Icons.SAVE_ALT, lambda: self.ejecutar(self.guardar), False)])],
            spacing=14), "Entrada", ft.Icons.EDIT_NOTE)
        salida = tarjeta(ft.Column([self.metricas, self.nota, self.resultado], spacing=12), "Resultado",
                         ft.Icons.LIST_ALT)
        self.calcular(primera=True)
        return ft.Column([entrada, salida], spacing=16)

    def calcular(self, primera: bool = False) -> None:
        op = next(iter(self.operacion.selected))
        self.exponente.visible = op == "potencia"
        try:
            sigma = Alfabeto.leer(self.sigma.value)
            self.sigma.error = None
        except ErrorTC as exc:
            self.sigma.error = str(exc)
            self._limpiar()
            return None if primera else self.refrescar()
        fuera = sigma.ajenos(self.palabra.value.strip())
        if fuera:
            self.palabra.error = f"No están en Σ: {', '.join(fuera)}"
            self._limpiar()
            return None if primera else self.refrescar()
        w = Palabra(self.palabra.value.strip())
        self.palabra.error = None
        self.palabra.helper = f"|ω| = {len(w)}"
        n = len(w)
        if op == "prefijos":
            valores, maximo = w.prefijos(), f"n + 1 = {n + 1}"
            self.nota.value = "Se incluyen λ (prefijo vacío) y la propia palabra; ambos son prefijos de toda palabra."
        elif op == "sufijos":
            valores, maximo = w.sufijos(), f"n + 1 = {n + 1}"
            self.nota.value = "Se incluyen λ y la propia palabra, con la misma convención que en los prefijos."
        elif op == "subcadenas":
            valores, maximo = w.subcadenas(), f"n(n+1)/2 + 1 = {n * (n + 1) // 2 + 1}"
            self.nota.value = "Subcadenas distintas; las repetidas se cuentan una vez. La cota se alcanza si no hay símbolos repetidos."
        elif op == "inversa":
            valores, maximo = [w.inversa()], "1"
            self.nota.value = "La reflexión lee la palabra de derecha a izquierda; (ωᴿ)ᴿ = ω."
        else:
            try:
                k = int(self.exponente.value)
                if k < 0 or k * max(n, 1) > 5000:
                    raise ValueError
                self.exponente.error = None
            except ValueError:
                self.exponente.error = "0 ≤ n, |ωⁿ| ≤ 5000"
                self._limpiar()
                return None if primera else self.refrescar()
            valores, maximo = [w.potencia(k)], "1"
            self.nota.value = f"ω^{k} concatena ω consigo misma {k} veces; ω⁰ = λ. |ω^{k}| = {k}·{n} = {k * n}."
        textos = [str(v) for v in valores]
        etiqueta = dict(self.OPERACIONES)[op]
        self._informe = Informe(f"{etiqueta} de {w}", textos, {"Σ": str(sigma), "ω": str(w), "|ω|": str(n)})
        self.metricas.controls = [metrica(str(n), "longitud |ω|"), metrica(str(len(textos)), "resultados"),
                                  metrica(maximo, "máximo teórico", Paleta.DORADO)]
        self.resultado.controls = [chips(textos, destacar=lambda t: t == "λ")]
        if not primera:
            self.refrescar()

    def _limpiar(self) -> None:
        self.metricas.controls, self.resultado.controls, self.nota.value = [], [], ""
        self._informe = None

    def guardar(self) -> None:
        if self._informe is None:
            raise ErrorTC("No hay un resultado que guardar: corrija la entrada.")
        ruta = self._informe.guardar(self.salida(f"palabras-{next(iter(self.operacion.selected))}.txt"))
        self.aviso.mostrar(f"Se guardaron {len(self._informe.elementos)} resultados en {ruta}", "ok")
