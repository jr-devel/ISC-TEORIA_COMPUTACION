"""Práctica 2: punto de entrada de la interfaz gráfica.

Se ejecuta con ``python src/app.py``. Sin escritorio (por ejemplo, en el
contenedor) Flet se sirve como página web en el puerto de ``FLET_SERVER_PORT``.
La lógica está en ``nucleo/``; la interfaz en ``interfaz/`` sólo la invoca.
"""

from interfaz.aplicacion import iniciar
from interfaz.vistas.biblioteca import Biblioteca
from interfaz.vistas.cadenas import Cadenas
from interfaz.vistas.cerraduras import Cerraduras
from interfaz.vistas.editor import Editor
from interfaz.vistas.inicio import Inicio
from interfaz.vistas.lenguajes import Lenguajes
from interfaz.vistas.simulador import Simulador

SECCIONES = [Inicio, Editor, Biblioteca, Simulador, Cadenas, Cerraduras, Lenguajes]

if __name__ == "__main__":
    iniciar("Teoría de la Computación · Práctica 2: AFND y Simulación de AFD con Interfaz Gráfica", "Práctica 2", SECCIONES)
