"""Clase base de las secciones."""

from __future__ import annotations

from pathlib import Path
from typing import Callable

import flet as ft

from nucleo.errores import ErrorTC

from ..componentes import Aviso, ayuda
from ..sesion import Sesion
from ..tema import Paleta, pantalla


class Vista:
    """Una sección de la aplicación: encabezado, ayuda plegable y contenido.

    Las subclases definen ``CLAVE``, ``TITULO``, ``ICONO``, ``DESCRIPCION`` y
    ``PASOS`` (instrucciones) e implementan :meth:`contenido`. Las acciones del
    usuario se envuelven en :meth:`ejecutar`, que convierte los errores del
    núcleo en un aviso rojo en lugar de un fallo.
    """

    CLAVE = ""
    TITULO = ""
    ICONO = ft.Icons.CIRCLE
    DESCRIPCION = ""
    PASOS: list[str] = []
    USA_AUTOMATA = False

    def __init__(self, sesion: Sesion) -> None:
        self.sesion = sesion
        self.page: ft.Page | None = None
        self.aviso = Aviso()
        self._ayuda = ayuda(self.PASOS)
        self._raiz: ft.Control | None = None

    # -- ciclo de vida ----------------------------------------------------------
    def control(self) -> ft.Control:
        if self._raiz is None:
            boton_ayuda = ft.TextButton("¿Cómo se usa?", icon=ft.Icons.HELP_OUTLINE,
                                        on_click=lambda e: self._alternar_ayuda())
            encabezado = ft.Row([
                ft.Container(ft.Icon(self.ICONO, color=Paleta.SUPERFICIE, size=26), bgcolor=Paleta.GUINDA,
                             border_radius=12, padding=10),
                ft.Column([ft.Text(self.TITULO, size=24, weight=ft.FontWeight.BOLD, color=Paleta.TEXTO),
                           ft.Text(pantalla(self.DESCRIPCION), size=14, color=Paleta.TENUE)],
                          spacing=2, expand=True),
                boton_ayuda if self.PASOS else ft.Container()],
                vertical_alignment=ft.CrossAxisAlignment.CENTER, spacing=14)
            self._raiz = ft.Column([encabezado, self._ayuda, self.aviso, self.contenido()],
                                   spacing=16, scroll=ft.ScrollMode.AUTO, expand=True)
        return self._raiz

    def contenido(self) -> ft.Control:  # pragma: no cover - lo implementan las subclases
        raise NotImplementedError

    def al_mostrar(self) -> None:
        """Se llama cada vez que el usuario entra a la sección."""

    # -- utilidades -----------------------------------------------------------------
    def _alternar_ayuda(self) -> None:
        self._ayuda.visible = not self._ayuda.visible
        self.refrescar()

    def refrescar(self) -> None:
        if self.page is not None:
            self.page.update()

    def ejecutar(self, accion: Callable[[], None]) -> None:
        """Ejecuta una acción y muestra cualquier error del núcleo como aviso."""
        self.aviso.ocultar()
        try:
            accion()
        except ErrorTC as exc:
            self.aviso.mostrar(str(exc), "error")
        except (ValueError, OSError) as exc:
            self.aviso.mostrar(f"No se pudo completar la acción: {exc}", "error")
        self.refrescar()

    def salida(self, nombre: str) -> Path:
        self.sesion.salidas.mkdir(parents=True, exist_ok=True)
        return self.sesion.salidas / nombre

    def exigir_automata(self):
        if self.sesion.automata is None:
            raise ErrorTC("Primero defina un autómata en «Editor» o ábralo en «Biblioteca».")
        return self.sesion.automata
