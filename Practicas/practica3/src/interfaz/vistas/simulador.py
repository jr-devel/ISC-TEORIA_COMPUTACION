"""Validación de palabras y ejecución paso a paso (Práctica 2, 3.3; Práctica 3, 2.1)."""

from __future__ import annotations

import flet as ft

from nucleo.automata import LAMBDA, Simulacion, conjunto
from nucleo.errores import ErrorTC

from ..componentes import Veredicto, tabla, tarjeta
from ..diagrama import Diagrama
from ..tema import MONO, Paleta, pantalla
from .base import Vista


class Simulador(Vista):
    CLAVE = "simulador"
    TITULO = "Simulador"
    ICONO = ft.Icons.PLAY_CIRCLE_OUTLINE
    DESCRIPCION = "Pruebe palabras en el autómata activo: completas o símbolo por símbolo, con la traza."
    USA_AUTOMATA = True
    PASOS = [
        "Asegúrese de tener un autómata activo (Editor o Biblioteca); su nombre aparece arriba a la derecha.",
        "Escriba la palabra (vacía o «λ» para la palabra vacía).",
        "«Validar» recorre toda la palabra. «Paso a paso» prepara la cinta y «Siguiente» lee un símbolo.",
        "Los estados activos se resaltan en el diagrama y en la tabla; las transiciones usadas, en guinda.",
        "En un AFN o AFN-λ se siguen todos los caminos a la vez: se muestra el conjunto de estados activos.",
    ]

    def contenido(self) -> ft.Control:
        self.palabra = ft.TextField(label="Palabra", hint_text="vacío = λ", text_style=ft.TextStyle(font_family=MONO),
                                    width=320, on_submit=lambda e: self.ejecutar(self.validar))
        self.cinta = ft.Row(spacing=4, wrap=True)
        self.activos = ft.Text("", font_family=MONO, size=14, selectable=True)
        self.diagrama = Diagrama(640, 340)
        self.tabla = ft.Column()
        self.veredicto = Veredicto()
        self.traza = ft.Column(spacing=4)
        self.cierres = ft.Column(spacing=6)
        self.siguiente = ft.FilledButton("Siguiente", icon=ft.Icons.SKIP_NEXT, disabled=True,
                                         on_click=lambda e: self.ejecutar(self.avanzar))
        self._sim: Simulacion | None = None
        controles = tarjeta(ft.Column([
            ft.Row([self.palabra,
                    ft.FilledButton("Validar", icon=ft.Icons.FACT_CHECK, on_click=lambda e: self.ejecutar(self.validar)),
                    ft.OutlinedButton("Paso a paso", icon=ft.Icons.DIRECTIONS_WALK,
                                      on_click=lambda e: self.ejecutar(self.preparar)),
                    self.siguiente,
                    ft.TextButton("Reiniciar", icon=ft.Icons.RESTART_ALT, on_click=lambda e: self.ejecutar(self.reiniciar))],
                   wrap=True, spacing=10),
            ft.Row([ft.Text("Cinta:", size=13, color=Paleta.TENUE), self.cinta]),
            ft.Row([ft.Text("Activos:", size=13, color=Paleta.TENUE), self.activos]),
            self.veredicto], spacing=12), "Palabra", ft.Icons.KEYBOARD)
        dibujo = tarjeta(ft.Column([self.diagrama, self.tabla], spacing=12), "Autómata", ft.Icons.ACCOUNT_TREE,
                         col={"xs": 12, "xl": 8})
        lateral = ft.Column([tarjeta(self.traza, "Traza", ft.Icons.TIMELINE),
                             tarjeta(self.cierres, "Cerradura λ", ft.Icons.BUBBLE_CHART)],
                            col={"xs": 12, "xl": 4}, spacing=16)
        return ft.Column([controles, ft.ResponsiveRow([dibujo, lateral], spacing=16)], spacing=16)

    def al_mostrar(self) -> None:
        self.reiniciar()

    # ------------------------------------------------------------------
    def _texto(self) -> str:
        t = (self.palabra.value or "").strip()
        return "" if t in (LAMBDA, "ε") else t

    def _pintar(self, usadas=()) -> None:
        m = self.sesion.automata
        sim = self._sim
        activos = sim.activos if sim else (m.cierre({m.inicial}) if m else frozenset())
        self.diagrama.dibujar(m, activos, usadas)
        if m is None:
            self.tabla.controls, self.cierres.controls = [], [ft.Text("Sin autómata activo.", color=Paleta.TENUE)]
            return
        encabezados, filas = m.tabla()
        resaltar = {i for i, q in enumerate(m.estados) if q in activos}
        self.tabla.controls = [tabla(encabezados, filas, resaltar)]
        self.activos.value = pantalla(conjunto(activos, m.estados))
        texto = sim.palabra if sim else self._texto()
        indice = sim.indice if sim else 0
        celdas = []
        for i, c in enumerate(texto):
            leido, actual = i < indice, i == indice and sim is not None and not sim.terminada
            celdas.append(ft.Container(
                ft.Text(c, font_family=MONO, size=16, weight=ft.FontWeight.BOLD,
                        color=Paleta.SUPERFICIE if actual else (Paleta.TENUE if leido else Paleta.TEXTO)),
                width=32, height=36, alignment=ft.Alignment.CENTER, border_radius=6,
                bgcolor=Paleta.GUINDA if actual else ("#ECE7EA" if leido else Paleta.SUPERFICIE),
                border=ft.Border.all(1, Paleta.BORDE)))
        self.cinta.controls = celdas or [ft.Text("λ (palabra vacía)", color=Paleta.TENUE, font_family=MONO)]
        cierres = m.cierres()
        if m.tiene_lambda:
            self.cierres.controls = [tabla(["q", "λ-cl(q)"], [[q, conjunto(cierres[q], m.estados)] for q in m.estados])]
        else:
            self.cierres.controls = [ft.Text("Este autómata no tiene transiciones λ: λ-cl(q) = {q}.",
                                             color=Paleta.TENUE, size=13)]

    def _linea(self, numero: str, texto: str, color: str = Paleta.TEXTO) -> ft.Control:
        return ft.Row([ft.Container(ft.Text(numero, size=11, color=Paleta.SUPERFICIE), width=24, height=24,
                                    border_radius=12, bgcolor=Paleta.DORADO, alignment=ft.Alignment.CENTER),
                       ft.Text(pantalla(texto), font_family=MONO, size=12, color=color, expand=True, selectable=True)],
                      vertical_alignment=ft.CrossAxisAlignment.START)

    def _traza_de(self, sim: Simulacion) -> None:
        m = sim.automata
        r = sim.recorrido
        lineas = [self._linea("0", f"inicio {conjunto(r.inicio, m.estados)} → λ-cl = "
                                   f"{conjunto(r.inicio_cerrado, m.estados)}")]
        for p in r.pasos:
            extra = f"; λ-cl = {conjunto(p.despues, m.estados)}" if p.agrego_cierre else ""
            lineas.append(self._linea(str(p.numero), f"«{p.simbolo}»: {conjunto(p.antes, m.estados)} → "
                                                     f"{conjunto(p.movidos, m.estados)}{extra}"))
        self.traza.controls = lineas

    def _cerrar(self) -> None:
        sim = self._sim
        self.siguiente.disabled = True
        ultima = sim.recorrido.lineas(sim.automata.estados)[-1]
        self.veredicto.mostrar(sim.recorrido.aceptada, ultima.replace("Resultado: ", ""))

    # -- acciones -------------------------------------------------------------------
    def validar(self) -> None:
        m = self.exigir_automata()
        self._sim = Simulacion(m, self._texto())
        self._sim.completar()
        self._traza_de(self._sim)
        usadas = self._sim.recorrido.pasos[-1].aristas if self._sim.recorrido.pasos else ()
        self._pintar(usadas)
        self._cerrar()

    def preparar(self) -> None:
        m = self.exigir_automata()
        self._sim = Simulacion(m, self._texto())
        self.veredicto.ocultar()
        self._traza_de(self._sim)
        self._pintar()
        self.siguiente.disabled = self._sim.terminada
        if self._sim.terminada:
            self._cerrar()
        else:
            self.aviso.mostrar("Pulse «Siguiente» para leer cada símbolo.", "info")

    def avanzar(self) -> None:
        if self._sim is None:
            raise ErrorTC("Pulse primero «Paso a paso».")
        paso = self._sim.avanzar()
        self._traza_de(self._sim)
        self._pintar(paso.aristas)
        if self._sim.terminada:
            self._cerrar()

    def reiniciar(self) -> None:
        self._sim = None
        self.veredicto.ocultar()
        self.siguiente.disabled = True
        self.traza.controls = [ft.Text("La traza aparecerá aquí.", color=Paleta.TENUE, size=13)]
        self._pintar()
