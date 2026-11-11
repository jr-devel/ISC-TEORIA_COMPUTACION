"""Jerarquía de excepciones del núcleo.

Todas derivan de :class:`ErrorTC`, de modo que la interfaz puede atrapar una
sola clase y mostrar el mensaje al usuario sin conocer el detalle.
"""

from __future__ import annotations


class ErrorTC(Exception):
    """Error de dominio con un mensaje pensado para el usuario final."""


class SimboloInvalido(ErrorTC):
    """Un símbolo no puede formar parte de un alfabeto."""


class PalabraFueraDeAlfabeto(ErrorTC):
    """La palabra usa símbolos que no pertenecen al alfabeto."""


class LimiteExcedido(ErrorTC):
    """La operación generaría más cadenas de las permitidas."""


class DefinicionInvalida(ErrorTC):
    """La quíntupla de un autómata no es coherente."""


class ArchivoInvalido(ErrorTC):
    """Un archivo no tiene el formato esperado."""


class ExpresionInvalida(ErrorTC):
    """Una expresión regular está mal formada.

    ``posicion`` es el índice (desde 0) del carácter donde se detectó el
    problema; la interfaz lo usa para señalarlo con un acento circunflejo.
    """

    def __init__(self, mensaje: str, posicion: int) -> None:
        super().__init__(f"{mensaje} (posición {posicion + 1})")
        self.posicion = posicion
        self.detalle = mensaje
