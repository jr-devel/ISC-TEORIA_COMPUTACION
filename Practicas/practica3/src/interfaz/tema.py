"""Paleta, tipografía y medidas compartidas por toda la interfaz."""

from __future__ import annotations

import flet as ft


class Paleta:
    GUINDA = "#6C1D45"
    GUINDA_CLARO = "#F4E8EE"
    GUINDA_MEDIO = "#B76E8F"
    DORADO = "#B38E5D"
    FONDO = "#F6F3F4"
    SUPERFICIE = "#FFFFFF"
    BORDE = "#E4DDE0"
    TEXTO = "#1F1A1D"
    TENUE = "#6E6469"
    EXITO = "#2E7D32"
    EXITO_CLARO = "#E8F5E9"
    ERROR = "#B3261E"
    ERROR_CLARO = "#FDECEA"
    INFO = "#1F5F8B"
    INFO_CLARO = "#E7F0F7"
    ARISTA = "#5A5257"
    ETIQUETA = "#1F5F8B"


FUENTE = "DejaVu Sans"
MONO = "DejaVu Sans Mono"
FUENTES = {FUENTE: "/fuentes/DejaVuSans.ttf", "DejaVu Sans Bold": "/fuentes/DejaVuSans-Bold.ttf",
           MONO: "/fuentes/DejaVuSansMono.ttf"}
"""Se incluyen en ``recursos/fuentes`` porque la fuente por omisión de Flet sin
conexión no trae ∅, ∪, →, los subíndices ni otros símbolos de la notación."""
RADIO = 14


def tema() -> ft.Theme:
    return ft.Theme(color_scheme_seed=Paleta.GUINDA, use_material3=True, font_family=FUENTE)


def pantalla(texto: str) -> str:
    """Punto único para adaptar texto a la fuente; con DejaVu sólo falta 𝒫."""
    return texto.replace("𝒫", "P")
