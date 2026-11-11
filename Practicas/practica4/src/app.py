"""Práctica 4: punto de entrada de la interfaz gráfica.

Se ejecuta con ``python src/app.py``. Sin escritorio (por ejemplo, en el
contenedor) Flet se sirve como página web en el puerto de ``FLET_SERVER_PORT``.
La lógica está en ``nucleo/``; la interfaz en ``interfaz/`` sólo la invoca.
"""

from interfaz.aplicacion import iniciar
from interfaz.vistas.automata_a_er import AutomataAER
from interfaz.vistas.biblioteca import Biblioteca
from interfaz.vistas.cadenas import Cadenas
from interfaz.vistas.cerraduras import Cerraduras
from interfaz.vistas.editor import Editor
from interfaz.vistas.equivalencia import Equivalencia
from interfaz.vistas.expresion import Expresion
from interfaz.vistas.inicio import Inicio
from interfaz.vistas.lenguajes import Lenguajes
from interfaz.vistas.lote import Lote
from interfaz.vistas.simulador import Simulador
from interfaz.vistas.transformar import Transformar
from interfaz.vistas.validadores import Validadores

SECCIONES = [Inicio, Editor, Biblioteca, Simulador, Transformar, Equivalencia, Lote, Expresion, AutomataAER, Validadores, Cadenas, Cerraduras, Lenguajes]

if __name__ == "__main__":
    iniciar("Teoría de la Computación · Práctica 4: Expresiones Regulares y Teorema de Kleene", "Práctica 4", SECCIONES)
