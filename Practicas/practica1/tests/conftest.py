"""Utilidades compartidas por las pruebas."""

from itertools import product
from pathlib import Path

import pytest

RAIZ = Path(__file__).resolve().parent.parent
AUTOMATAS = RAIZ / "automatas"


def palabras(alfabeto, maximo):
    """Todas las palabras de Σ⁰ ∪ … ∪ Σ^maximo."""
    for n in range(maximo + 1):
        for t in product(alfabeto, repeat=n):
            yield "".join(t)


def longitud_exhaustiva(simbolos: int, presupuesto: int = 20_000) -> int:
    """Mayor L tal que |Σ⁰ ∪ … ∪ Σᴸ| ≤ presupuesto (12 con |Σ| = 2, 8 con |Σ| = 3)."""
    L, total = 0, 1
    while total + simbolos ** (L + 1) <= presupuesto:
        L, total = L + 1, total + simbolos ** (L + 1)
    return L


@pytest.fixture
def raiz() -> Path:
    return RAIZ


def primera_diferencia(automatas, alfabeto, maximo):
    """Primera palabra (orden canónico por profundidad) en la que los autómatas no coinciden.

    Recorre el árbol de Σ⁰ ∪ … ∪ Σ^maximo actualizando el conjunto de estados
    activos de cada autómata símbolo a símbolo, de modo que el costo es el número
    de nodos del árbol y no la suma de las longitudes de las palabras.
    Devuelve ``None`` si coinciden en todas.
    """
    inicio = [m.cierre({m.inicial}) for m in automatas]
    pila = [("", inicio)]
    while pila:
        palabra, activos = pila.pop()
        veredictos = {m.es_aceptacion(s) for m, s in zip(automatas, activos)}
        if len(veredictos) > 1:
            return palabra
        if len(palabra) < maximo:
            for a in reversed(alfabeto):
                pila.append((palabra + a, [m.transitar(s, a) for m, s in zip(automatas, activos)]))
    return None
