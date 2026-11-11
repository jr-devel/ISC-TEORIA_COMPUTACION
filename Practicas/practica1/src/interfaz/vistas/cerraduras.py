"""Operación 2 de la Práctica 1: Σ*, Σ⁺ y Σⁿ con el límite de 200 000 cadenas."""

from __future__ import annotations

import flet as ft

from nucleo.errores import ErrorTC
from nucleo.lenguajes import LIMITE_CADENAS, Alfabeto, Enumerador, Informe

from ..componentes import boton, chips, metrica, tarjeta
from ..tema import Paleta
from .base import Vista


class Cerraduras(Vista):
    CLAVE = "cerraduras"
    TITULO = "Cerraduras"
    ICONO = ft.Icons.ALL_INCLUSIVE
    DESCRIPCION = "Cerradura de Kleene Σ*, cerradura positiva Σ⁺ y potencia Σⁿ hasta una longitud dada."
    PASOS = [
        "Escriba el alfabeto Σ.",
        "Mueva el control de longitud máxima n; el contador indica cuántas cadenas se generarían.",
        "Elija Σ*, Σ⁺ o Σⁿ y pulse «Generar». Si el total supera 200 000 el botón se desactiva.",
        "Las cadenas aparecen agrupadas por longitud; «Guardar .txt» escribe la lista completa.",
    ]

    def contenido(self) -> ft.Control:
        self.sigma = ft.TextField(label="Alfabeto Σ", value="a, b", width=260, on_change=lambda e: self.prever())
        self.longitud = ft.Slider(min=0, max=20, divisions=20, value=3, label="n = {value}",
                                  on_change=lambda e: self.prever(), expand=True)
        self.tipo = ft.SegmentedButton(segments=[ft.Segment(value="estrella", label=ft.Text("Σ*")),
                                                 ft.Segment(value="mas", label=ft.Text("Σ⁺")),
                                                 ft.Segment(value="potencia", label=ft.Text("Σⁿ"))],
                                       selected=["estrella"], on_change=lambda e: self.prever())
        self.valor_n = ft.Text("n = 3", size=15, weight=ft.FontWeight.BOLD, color=Paleta.GUINDA, width=70)
        self.contador = ft.Text("", size=14, weight=ft.FontWeight.W_600)
        self.medidor = ft.ProgressBar(value=0, bar_height=8, border_radius=4, bgcolor=Paleta.BORDE)
        self.generar_btn = ft.FilledButton("Generar", icon=ft.Icons.PLAY_ARROW,
                                           on_click=lambda e: self.ejecutar(self.generar))
        self.metricas = ft.Row(wrap=True, spacing=10)
        self.grupos = ft.Column(spacing=12)
        self._informe: Informe | None = None
        entrada = tarjeta(ft.Column([
            ft.Row([self.sigma], wrap=True),
            ft.Row([ft.Text("Longitud máxima", size=13, color=Paleta.TENUE), self.longitud, self.valor_n]),
            ft.Row([self.tipo, ft.Text("Σ* incluye λ; Σ⁺ la excluye; Σⁿ sólo genera la longitud n.", size=12,
                                       color=Paleta.TENUE)], wrap=True, spacing=14),
            ft.Column([self.contador, self.medidor], spacing=6),
            ft.Row([self.generar_btn, boton("Guardar .txt", ft.Icons.SAVE_ALT, lambda: self.ejecutar(self.guardar),
                                            False)])], spacing=14), "Entrada", ft.Icons.TUNE)
        salida = tarjeta(ft.Column([self.metricas, self.grupos], spacing=12), "Cadenas generadas",
                         ft.Icons.FORMAT_LIST_NUMBERED)
        self.prever(primera=True)
        return ft.Column([entrada, salida], spacing=16)

    def _rango(self) -> tuple[int, int]:
        n = int(self.longitud.value)
        tipo = next(iter(self.tipo.selected))
        return {"estrella": (0, n), "mas": (1, n), "potencia": (n, n)}[tipo]

    def prever(self, primera: bool = False) -> None:
        """Calcula Σ|Σ|^i con la fórmula, sin generar, y avisa si excede el límite."""
        self.valor_n.value = f"n = {int(self.longitud.value)}"
        try:
            sigma = Alfabeto.leer(self.sigma.value)
            self.sigma.error = None
            minimo, maximo = self._rango()
            total = sigma.cuantas(maximo, minimo) if maximo >= minimo else 0
            excede = total > LIMITE_CADENAS
            self.contador.value = (f"Se generarían {total:,} cadenas (|Σ| = {len(sigma)}; límite "
                                   f"{LIMITE_CADENAS:,}).").replace(",", " ")
            self.contador.color = Paleta.ERROR if excede else Paleta.TEXTO
            self.medidor.value = min(1.0, total / LIMITE_CADENAS)
            self.medidor.color = Paleta.ERROR if excede else Paleta.GUINDA
            self.generar_btn.disabled = excede
            if excede:
                self.contador.value += (f" Reduzca n: con |Σ| = {len(sigma)} el máximo es n = "
                                        f"{Enumerador.longitud_maxima(len(sigma))}.")
        except ErrorTC as exc:
            self.sigma.error = str(exc)
            self.generar_btn.disabled = True
        if not primera:
            self.refrescar()

    def generar(self) -> None:
        sigma = Alfabeto.leer(self.sigma.value)
        minimo, maximo = self._rango()
        enumerador = Enumerador(sigma, maximo, minimo) if maximo >= minimo else None
        cadenas = list(enumerador) if enumerador else []
        tipo = next(iter(self.tipo.selected))
        nombre = {"estrella": "Σ*", "mas": "Σ⁺", "potencia": f"Σ^{maximo}"}[tipo]
        self._informe = Informe(f"{nombre} con Σ = {sigma}, longitud ≤ {maximo}", [c or "λ" for c in cadenas],
                                {"Σ": str(sigma), "n": str(maximo)})
        self.metricas.controls = [metrica(str(len(sigma)), "|Σ|"), metrica(str(maximo), "longitud máxima"),
                                  metrica(f"{len(cadenas):,}".replace(",", " "), "cadenas")]
        grupos: dict[int, list[str]] = {}
        for c in cadenas:
            grupos.setdefault(len(c), []).append(c or "λ")
        mostradas, controles = 0, []
        for largo, lista in grupos.items():
            if mostradas > 600:
                controles.append(ft.Text(f"Longitudes {largo} a {maximo}: se omiten en pantalla; "
                                         "«Guardar .txt» las incluye.", color=Paleta.TENUE, size=13))
                break
            controles.append(ft.Text(f"Longitud {largo}  ·  |Σ^{largo}| = {len(lista)}", size=13,
                                     weight=ft.FontWeight.W_600, color=Paleta.GUINDA))
            controles.append(chips(lista, maximo=300, destacar=lambda t: t == "λ"))
            mostradas += min(len(lista), 300)
        if not cadenas:
            controles = [ft.Text("Σ⁺ con longitud 0 es vacío: la única palabra de longitud 0 es λ y Σ⁺ la excluye.",
                                 color=Paleta.TENUE)]
        self.grupos.controls = controles
        self.aviso.mostrar(f"{nombre}: {len(cadenas)} cadenas generadas.", "ok")

    def guardar(self) -> None:
        if self._informe is None:
            raise ErrorTC("Genere primero las cadenas.")
        ruta = self._informe.guardar(self.salida(f"cerradura-{next(iter(self.tipo.selected))}.txt"))
        self.aviso.mostrar(f"Se guardaron {len(self._informe.elementos)} cadenas en {ruta}", "ok")
