"""Validación de muchas palabras a la vez con informe (Práctica 3, 2.5)."""

from __future__ import annotations

from pathlib import Path

import flet as ft

from nucleo.algoritmos import Lote as Validador
from nucleo.errores import ErrorTC

from ..componentes import metrica, tabla, tarjeta
from ..tema import MONO, Paleta
from .base import Vista


class Lote(Vista):
    CLAVE = "lote"
    TITULO = "Validación por lotes"
    ICONO = ft.Icons.PLAYLIST_ADD_CHECK
    DESCRIPCION = "Valida un archivo de texto con una palabra por línea y guarda un informe."
    USA_AUTOMATA = True
    PASOS = [
        "Active el autómata con el que se validará.",
        "Escriba las palabras (una por línea) o cargue un archivo .txt con «Cargar archivo».",
        "Las líneas vacías y las que empiezan con # se ignoran; escriba λ para la palabra vacía.",
        "Pulse «Validar todo» y después «Guardar informe» para escribirlo en salidas/.",
    ]

    def contenido(self) -> ft.Control:
        self.ruta = ft.TextField(label="Archivo .txt", value="automatas/practica3/cadenas-ejemplo.txt", expand=True)
        self.texto = ft.TextField(multiline=True, min_lines=8, max_lines=14, text_style=ft.TextStyle(font_family=MONO),
                                  hint_text="una palabra por línea", width=720)
        self.metricas = ft.Row(spacing=10)
        self.resultado = ft.Column()
        self._filas = []
        return ft.Column([
            tarjeta(ft.Column([ft.Row([self.ruta, ft.OutlinedButton("Cargar archivo", icon=ft.Icons.UPLOAD_FILE,
                                                                     on_click=lambda e: self.ejecutar(self.cargar))]),
                               ft.Row([ft.FilledButton("Validar todo", icon=ft.Icons.PLAYLIST_ADD_CHECK,
                                                       on_click=lambda e: self.ejecutar(self.validar)),
                                       ft.OutlinedButton("Guardar informe", icon=ft.Icons.SAVE_ALT,
                                                         on_click=lambda e: self.ejecutar(self.guardar))]),
                               self.texto],
                              spacing=12), "Palabras", ft.Icons.NOTES),
            tarjeta(ft.Column([self.metricas, self.resultado], spacing=12), "Resultados", ft.Icons.FACT_CHECK)],
            spacing=16)

    def cargar(self) -> None:
        ruta = Path(self.ruta.value.strip())
        ruta = ruta if ruta.is_absolute() else self.sesion.raiz / ruta
        if not ruta.is_file():
            raise ErrorTC(f"No existe el archivo {ruta}.")
        self.texto.value = ruta.read_text(encoding="utf-8")
        self.aviso.mostrar(f"Se cargaron {len(self.texto.value.splitlines())} líneas de {ruta.name}.", "info")

    def validar(self) -> None:
        validador = Validador(self.exigir_automata())
        self._filas = validador.validar_texto(self.texto.value or "")
        if not self._filas:
            raise ErrorTC("No hay palabras que validar.")
        cuenta = {v: sum(f.veredicto == v for f in self._filas) for v in ("ACEPTADA", "RECHAZADA", "ERROR")}
        self.metricas.controls = [metrica(str(len(self._filas)), "palabras"),
                                  metrica(str(cuenta["ACEPTADA"]), "aceptadas", Paleta.EXITO),
                                  metrica(str(cuenta["RECHAZADA"]), "rechazadas", Paleta.ERROR),
                                  metrica(str(cuenta["ERROR"]), "con error", Paleta.DORADO)]
        self.resultado.controls = [tabla(["#", "Palabra", "Resultado", "Estados finales / detalle"],
                                         [[f.numero, f.palabra, f.veredicto, f.detalle] for f in self._filas],
                                         {i for i, f in enumerate(self._filas) if f.veredicto == "ACEPTADA"})]

    def guardar(self) -> None:
        if not self._filas:
            raise ErrorTC("Valide primero las palabras.")
        m = self.exigir_automata()
        ruta = Validador(m).informe(self._filas).guardar(self.salida(f"informe-{m.nombre or 'lote'}.txt"))
        self.aviso.mostrar(f"Informe guardado en {ruta}", "ok")
