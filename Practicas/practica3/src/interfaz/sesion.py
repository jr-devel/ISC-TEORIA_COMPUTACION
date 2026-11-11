"""Estado compartido entre las secciones de la aplicación."""

from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING, Callable

if TYPE_CHECKING:                     # la Práctica 1 no incluye el módulo de autómatas
    from nucleo.automata import Automata

RAIZ = Path(__file__).resolve().parents[2]


class Sesion:
    """Autómata activo, carpetas de trabajo y avisos a las secciones interesadas.

    Una sección se suscribe con :meth:`al_cambiar`; cuando otra sección
    establece un autómata nuevo (al definirlo, importarlo o transformarlo),
    todas las suscritas se refrescan.
    """

    def __init__(self, raiz: Path = RAIZ) -> None:
        self.raiz = raiz
        self.biblioteca = raiz / "automatas"
        self.salidas = raiz / "salidas"
        self.automata: "Automata | None" = None
        self.recientes: list["Automata"] = []
        self._oyentes: list[Callable[["Automata"], None]] = []
        self.navegar: Callable[[str], None] = lambda clave: None
        self.secciones: list[tuple[str, str, object, str]] = []   # (clave, título, icono, descripción)

    def al_cambiar(self, oyente: Callable[["Automata"], None]) -> None:
        self._oyentes.append(oyente)

    def usar(self, automata: "Automata") -> None:
        self.automata = automata
        self.recientes = [automata] + [m for m in self.recientes if m is not automata][:7]
        for oyente in list(self._oyentes):
            oyente(automata)
