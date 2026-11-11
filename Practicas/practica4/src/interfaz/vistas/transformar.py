"""AFN-λ → AFN → AFD → AFD mínimo, con cada algoritmo paso a paso (Práctica 3, 2.2–2.4)."""

from __future__ import annotations

import flet as ft

from nucleo.algoritmos import AFD, Minimizacion, QuitarLambda, Resultado, Subconjuntos
from nucleo.errores import ErrorTC
from nucleo.formatos import Archivos

from ..componentes import VisorEtapas, metrica, tarjeta
from ..diagrama import Diagrama
from ..tema import Paleta, pantalla
from .base import Vista

ETAPAS = [("lambda", "1 · Quitar λ", ft.Icons.REMOVE_CIRCLE_OUTLINE),
          ("subconjuntos", "2 · Subconjuntos", ft.Icons.SCATTER_PLOT),
          ("minimo", "3 · Minimizar", ft.Icons.COMPRESS)]


class Transformar(Vista):
    CLAVE = "transformar"
    TITULO = "Transformaciones"
    ICONO = ft.Icons.AUTO_FIX_HIGH
    DESCRIPCION = "Elimina λ, construye los subconjuntos y minimiza el autómata activo, mostrando cada paso."
    USA_AUTOMATA = True
    PASOS = [
        "Active un autómata en Editor o Biblioteca. Se calculan sólo las etapas que hacen falta para llegar al AFD mínimo.",
        "Elija una etapa en la barra superior. Las etapas que no se necesitan aparecen como «no aplica».",
        "Recorra el algoritmo con «Anterior» y «Siguiente»; cada paso trae su explicación y su tabla.",
        "«Usar resultado» convierte la salida de la etapa en el autómata activo; «Guardar .jff» la escribe en salidas/.",
    ]

    def contenido(self) -> ft.Control:
        self.resumen = ft.Row(wrap=True, spacing=10)
        self.selector = ft.SegmentedButton(segments=[ft.Segment(value=k, label=ft.Text(t), icon=ft.Icon(i))
                                                     for k, t, i in ETAPAS],
                                           selected=["lambda"], on_change=lambda e: self._mostrar_etapa())
        self.estado_etapa = ft.Text("", size=13, color=Paleta.TENUE)
        self.visor = VisorEtapas(lambda m: Diagrama(720, 320).dibujar(m))
        self.acciones = ft.Row([
            ft.FilledButton("Usar resultado", icon=ft.Icons.CHECK, on_click=lambda e: self.ejecutar(self.usar)),
            ft.OutlinedButton("Guardar .jff", icon=ft.Icons.SAVE_ALT, on_click=lambda e: self.ejecutar(self.guardar))])
        self._resultados: dict[str, Resultado | None] = {}
        self._fuente = None
        return ft.Column([
            tarjeta(self.resumen, "Del autómata activo al AFD mínimo", ft.Icons.ROUTE),
            tarjeta(ft.Column([ft.Row([self.selector], scroll=ft.ScrollMode.AUTO), self.estado_etapa, self.visor,
                               self.acciones], spacing=12), "Algoritmo paso a paso", ft.Icons.STAIRS)], spacing=16)

    def al_mostrar(self) -> None:
        m = self.sesion.automata
        if m is None:
            self.resumen.controls = [ft.Text("Active primero un autómata en Editor o Biblioteca.", color=Paleta.TENUE)]
            self.visor.cargar([])
            self.acciones.visible = False
            return
        if m is not self._fuente:
            self.ejecutar(lambda: self._calcular(m))

    def _calcular(self, m) -> None:
        self._fuente = m
        actual = m
        r_lambda = QuitarLambda(actual).resolver() if actual.tiene_lambda else None
        actual = r_lambda.salida if r_lambda else actual
        r_sub = Subconjuntos(actual).resolver() if not isinstance(actual, AFD) else None
        actual = r_sub.salida if r_sub else actual
        r_min = Minimizacion(actual).resolver()
        self._resultados = {"lambda": r_lambda, "subconjuntos": r_sub, "minimo": r_min}
        piezas = [metrica(f"{len(m.estados)}", f"{m.tipo} original")]
        for clave, etiqueta in (("lambda", "AFN sin λ"), ("subconjuntos", "AFD"), ("minimo", "AFD mínimo")):
            r = self._resultados[clave]
            piezas.append(ft.Icon(ft.Icons.ARROW_FORWARD, color=Paleta.BORDE))
            piezas.append(metrica(str(len(r.salida.estados)) if r else "—",
                                  etiqueta if r else f"{etiqueta} (no aplica)",
                                  Paleta.GUINDA if r else Paleta.TENUE))
        self.resumen.controls = piezas
        primera = next(k for k, _, _ in ETAPAS if self._resultados[k] is not None)
        self.selector.selected = [primera]
        self._mostrar_etapa(refrescar=False)

    def _mostrar_etapa(self, refrescar: bool = True) -> None:
        clave = next(iter(self.selector.selected))
        r = self._resultados.get(clave)
        if r is None:
            motivo = {"lambda": "El autómata no tiene transiciones λ.",
                      "subconjuntos": "Después de quitar λ el autómata ya es determinista."}.get(clave, "")
            self.estado_etapa.value = f"No aplica: {motivo}"
            self.visor.cargar([])
            self.acciones.visible = False
        else:
            self.estado_etapa.value = pantalla(f"{r.algoritmo}: {r.resumen}")
            self.visor.cargar(r.etapas)
            self.acciones.visible = True
        if refrescar:
            self.refrescar()

    def _actual(self) -> Resultado:
        r = self._resultados.get(next(iter(self.selector.selected)))
        if r is None:
            raise ErrorTC("Esta etapa no produjo un autómata.")
        return r

    def usar(self) -> None:
        r = self._actual()
        self.sesion.usar(r.salida)
        self._fuente = r.salida
        self.aviso.mostrar(f"El resultado ({r.salida.tipo}, {len(r.salida.estados)} estados) es ahora el autómata activo.",
                           "ok")

    def guardar(self) -> None:
        r = self._actual()
        ruta = Archivos.guardar(r.salida, self.salida(f"{r.salida.nombre}.jff"))
        self.aviso.mostrar(f"Guardado en {ruta}", "ok")
