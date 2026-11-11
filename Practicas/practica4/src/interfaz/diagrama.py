"""Dibujo de autómatas en un lienzo de Flet.

Los estados se colocan con las coordenadas del autómata (las de JFLAP o las de
:class:`~nucleo.automata.Disposicion`) escaladas al tamaño del lienzo. Las
aristas entre dos estados que se conectan en ambos sentidos se curvan para no
encimarse, los lazos se dibujan sobre el estado y las etiquetas con muchos
símbolos se compactan en rangos (``0–9``, ``a–z``).
"""

from __future__ import annotations

import math
from typing import Iterable

import flet as ft
import flet.canvas as cv

from nucleo.automata import LAMBDA, Arista, Automata

from .tema import FUENTE, RADIO, Paleta, pantalla


def compactar(simbolos: Iterable[str]) -> str:
    """``['0', '1', …, '9', 'x']`` → ``'0–9, x'``; λ va al final."""
    lista = sorted(set(simbolos), key=lambda s: (s == "", s))
    tiene_lambda = "" in lista
    lista = [s for s in lista if s]
    partes, i = [], 0
    while i < len(lista):
        j = i
        while (j + 1 < len(lista) and len(lista[j]) == len(lista[j + 1]) == 1
               and ord(lista[j + 1]) == ord(lista[j]) + 1 and lista[j + 1].isalnum() and lista[i].isalnum()):
            j += 1
        partes.append(f"{lista[i]}–{lista[j]}" if j - i >= 2 else ", ".join(lista[i:j + 1]))
        i = j + 1
    if tiene_lambda:
        partes.append(LAMBDA)
    return ", ".join(partes)


class Diagrama(ft.Container):
    """Lienzo con el diagrama de transiciones de un autómata."""

    def __init__(self, ancho: int = 760, alto: int = 380) -> None:
        self.ancho, self.alto = ancho, alto
        self.lienzo = cv.Canvas(width=ancho, height=alto)
        self._vacio = ft.Column([ft.Icon(ft.Icons.ACCOUNT_TREE_OUTLINED, size=40, color=Paleta.BORDE),
                                 ft.Text("Aún no hay un autómata que dibujar.", color=Paleta.TENUE)],
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                alignment=ft.MainAxisAlignment.CENTER, width=ancho, height=alto)
        super().__init__(ft.Stack([self.lienzo, self._vacio], width=ancho, height=alto), width=ancho, height=alto,
                         bgcolor="#FCFBFB", border=ft.Border.all(1, Paleta.BORDE), border_radius=RADIO)

    # ------------------------------------------------------------------
    def dibujar(self, automata: Automata | None, activos: Iterable[str] = (),
                usadas: Iterable[Arista] = ()) -> "Diagrama":
        self._vacio.visible = automata is None
        self.lienzo.shapes = [] if automata is None else self._figuras(automata, set(activos), set(usadas))
        return self

    def _escala(self, automata: Automata) -> dict[str, tuple[float, float]]:
        puntos = {q: automata.posicion(q) for q in automata.estados}
        xs, ys = [p[0] for p in puntos.values()], [p[1] for p in puntos.values()]
        margen_x, margen_arriba, margen_abajo = 70, 80, 45
        util_x, util_y = self.ancho - 2 * margen_x, self.alto - margen_arriba - margen_abajo
        dx, dy = (max(xs) - min(xs)) or 1, (max(ys) - min(ys)) or 1
        k = min(util_x / dx, util_y / dy, 1.5)
        ox = margen_x + (util_x - dx * k) / 2
        oy = margen_arriba + (util_y - dy * k) / 2
        return {q: (ox + (x - min(xs)) * k, oy + (y - min(ys)) * k) for q, (x, y) in puntos.items()}

    @staticmethod
    def _radio(nombre: str) -> float:
        return min(36.0, max(23.0, 8 + 4.2 * len(pantalla(nombre))))

    def _figuras(self, m: Automata, activos: set[str], usadas: set[Arista]) -> list:
        pos = self._escala(m)
        radios = {q: self._radio(q) for q in m.estados}
        grupos: dict[tuple[str, str], list[str]] = {}
        resaltadas: set[tuple[str, str]] = {(t.origen, t.destino) for t in usadas}
        for t in m.aristas:
            grupos.setdefault((t.origen, t.destino), []).append(t.simbolo)
        figuras: list = []
        for (p, q), simbolos in grupos.items():
            color = Paleta.GUINDA if (p, q) in resaltadas else Paleta.ARISTA
            grosor = 2.6 if (p, q) in resaltadas else 1.5
            etiqueta = pantalla(compactar(simbolos))
            if p == q:
                figuras += self._lazo(pos[p], radios[p], etiqueta, color, grosor)
            else:
                curva = self._curvatura(pos, radios, p, q, (q, p) in grupos)
                figuras += self._arista(pos[p], pos[q], radios[p], radios[q], etiqueta, color, grosor, curva)
        x0, y0 = pos[m.inicial]
        r0 = radios[m.inicial]
        figuras += self._flecha(x0 - r0 - 34, y0, x0 - r0 - 1, y0, Paleta.TEXTO, 1.8)
        for q, (x, y) in pos.items():
            r = radios[q]
            activo = q in activos
            borde = Paleta.GUINDA if activo else "#3B3438"
            figuras.append(cv.Circle(x, y, r, ft.Paint(color=Paleta.GUINDA_CLARO if activo else Paleta.SUPERFICIE,
                                                       style=ft.PaintingStyle.FILL)))
            figuras.append(cv.Circle(x, y, r, ft.Paint(color=borde, stroke_width=3 if activo else 1.6,
                                                       style=ft.PaintingStyle.STROKE)))
            if q in m.finales:
                figuras.append(cv.Circle(x, y, r - 4.5, ft.Paint(color=borde, stroke_width=1.4,
                                                                 style=ft.PaintingStyle.STROKE)))
            visible = pantalla(q) if len(q) <= 12 else pantalla(q)[:10] + "…"
            figuras.append(cv.Text(x, y, visible, alignment=ft.Alignment.CENTER,
                                   style=ft.TextStyle(size=13 if len(q) < 6 else (11 if len(q) < 9 else 9), color=Paleta.TEXTO, font_family=FUENTE,
                                                      weight=ft.FontWeight.W_600 if activo else None)))
        return figuras

    @staticmethod
    def _curvatura(pos, radios, p, q, doble: bool) -> float:
        """Curva la arista si es de ida y vuelta o si su recta atraviesa otro estado."""
        (x1, y1), (x2, y2) = pos[p], pos[q]
        d = math.hypot(x2 - x1, y2 - y1) or 1
        curva = 26.0 if doble else 0.0
        for r, (x, y) in pos.items():
            if r in (p, q):
                continue
            t = ((x - x1) * (x2 - x1) + (y - y1) * (y2 - y1)) / (d * d)
            if 0 < t < 1:
                distancia = abs((x2 - x1) * (y1 - y) - (x1 - x) * (y2 - y1)) / d
                if distancia < radios[r] + 10:
                    curva = max(curva, 0.28 * d + 20)
        return curva

    def _arista(self, a, b, ra, rb, etiqueta, color, grosor, curva) -> list:
        (x1, y1), (x2, y2) = a, b
        d = math.hypot(x2 - x1, y2 - y1) or 1
        ux, uy = (x2 - x1) / d, (y2 - y1) / d
        nx, ny = uy, -ux                                   # normal a la izquierda del sentido de avance
        cx, cy = (x1 + x2) / 2 + nx * curva, (y1 + y2) / 2 + ny * curva
        # puntos sobre los círculos en dirección del punto de control
        sx, sy = self._borde(x1, y1, cx, cy, ra)
        ex, ey = self._borde(x2, y2, cx, cy, rb)
        trazo = ft.Paint(color=color, stroke_width=grosor, style=ft.PaintingStyle.STROKE)
        figuras = [cv.Path([cv.Path.MoveTo(sx, sy), cv.Path.QuadraticTo(cx, cy, ex, ey)], trazo)]
        figuras += self._punta(cx, cy, ex, ey, color, grosor)
        mx, my = 0.25 * sx + 0.5 * cx + 0.25 * ex, 0.25 * sy + 0.5 * cy + 0.25 * ey
        figuras.append(self._etiqueta(mx + nx * 11, my + ny * 11, etiqueta, color))
        return figuras

    def _lazo(self, centro, radio, etiqueta, color, grosor) -> list:
        x, y = centro
        trazo = ft.Paint(color=color, stroke_width=grosor, style=ft.PaintingStyle.STROKE)
        izq, der = (x - radio * 0.55, y - radio * 0.83), (x + radio * 0.55, y - radio * 0.83)
        arriba = y - radio - 34
        figuras = [cv.Path([cv.Path.MoveTo(*izq), cv.Path.CubicTo(x - radio, arriba, x + radio, arriba, *der)], trazo)]
        figuras += self._punta(x + radio * 0.9, arriba + 10, der[0], der[1], color, grosor)
        figuras.append(self._etiqueta(x, arriba - 2, etiqueta, color))
        return figuras

    @staticmethod
    def _borde(x, y, hacia_x, hacia_y, r):
        d = math.hypot(hacia_x - x, hacia_y - y) or 1
        return x + (hacia_x - x) / d * r, y + (hacia_y - y) / d * r

    def _flecha(self, x1, y1, x2, y2, color, grosor) -> list:
        trazo = ft.Paint(color=color, stroke_width=grosor, style=ft.PaintingStyle.STROKE)
        return [cv.Line(x1, y1, x2, y2, trazo)] + self._punta(x1, y1, x2, y2, color, grosor)

    @staticmethod
    def _punta(x1, y1, x2, y2, color, grosor) -> list:
        ang = math.atan2(y2 - y1, x2 - x1)
        largo = 10
        p1 = (x2 - largo * math.cos(ang - 0.42), y2 - largo * math.sin(ang - 0.42))
        p2 = (x2 - largo * math.cos(ang + 0.42), y2 - largo * math.sin(ang + 0.42))
        return [cv.Path([cv.Path.MoveTo(x2, y2), cv.Path.LineTo(*p1), cv.Path.LineTo(*p2), cv.Path.Close()],
                        ft.Paint(color=color, style=ft.PaintingStyle.FILL))]

    @staticmethod
    def _etiqueta(x, y, texto, color):
        return cv.Text(x, y, texto, alignment=ft.Alignment.CENTER,
                       style=ft.TextStyle(size=13, color=Paleta.ETIQUETA if color == Paleta.ARISTA else color, font_family=FUENTE,
                                          weight=ft.FontWeight.BOLD,
                                          bgcolor="#FCFBFB"))
