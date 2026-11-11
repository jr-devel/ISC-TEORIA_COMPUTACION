"""Piezas visuales reutilizables: tarjetas, avisos, tablas, chips y visor de etapas."""

from __future__ import annotations

from typing import TYPE_CHECKING, Callable, Sequence

import flet as ft

if TYPE_CHECKING:                     # sólo para las anotaciones; existe desde la Práctica 3
    from nucleo.algoritmos import Etapa

from .tema import MONO, RADIO, Paleta, pantalla


def texto(valor: str, tamano: int = 14, color: str = Paleta.TEXTO, peso=None, mono: bool = False,
          seleccionable: bool = True) -> ft.Text:
    return ft.Text(pantalla(valor), size=tamano, color=color, weight=peso,
                   font_family=MONO if mono else None, selectable=seleccionable)


def titulo(valor: str, tamano: int = 16) -> ft.Text:
    return ft.Text(pantalla(valor), size=tamano, weight=ft.FontWeight.W_600, color=Paleta.TEXTO)


def tarjeta(contenido: ft.Control, encabezado: str | None = None, icono=None, acciones=None,
            col=None, expand=False, relleno: int = 18) -> ft.Container:
    """Contenedor blanco con borde suave; ``col`` sirve dentro de un ResponsiveRow."""
    partes: list[ft.Control] = []
    if encabezado:
        fila = [ft.Icon(icono, color=Paleta.GUINDA, size=20)] if icono else []
        fila.append(titulo(encabezado, 15))
        if acciones:
            fila += [ft.Container(expand=True)] + list(acciones)
        partes.append(ft.Row(fila, vertical_alignment=ft.CrossAxisAlignment.CENTER))
    partes.append(contenido)
    return ft.Container(
        ft.Column(partes, spacing=12, tight=True), bgcolor=Paleta.SUPERFICIE, border_radius=RADIO,
        border=ft.Border.all(1, Paleta.BORDE), padding=relleno, col=col if col is not None else 12,
        expand=expand)


class Aviso(ft.Container):
    """Franja de estado: éxito, error o información."""

    ESTILOS = {
        "ok": (Paleta.EXITO, Paleta.EXITO_CLARO, ft.Icons.CHECK_CIRCLE),
        "error": (Paleta.ERROR, Paleta.ERROR_CLARO, ft.Icons.ERROR_OUTLINE),
        "info": (Paleta.INFO, Paleta.INFO_CLARO, ft.Icons.INFO_OUTLINE),
    }

    def __init__(self) -> None:
        self._icono = ft.Icon(ft.Icons.INFO_OUTLINE, size=20)
        self._texto = ft.Text("", size=14, selectable=True, expand=True)
        super().__init__(ft.Row([self._icono, self._texto], spacing=10), padding=12, border_radius=10,
                         visible=False)

    def mostrar(self, mensaje: str, tipo: str = "info") -> None:
        color, fondo, icono = self.ESTILOS[tipo]
        self._icono.icon, self._icono.color = icono, color
        self._texto.value, self._texto.color = pantalla(mensaje), color
        self.bgcolor, self.visible = fondo, True
        self.border = ft.Border.all(1, color)

    def ocultar(self) -> None:
        self.visible = False


class Veredicto(ft.Container):
    """Resultado grande de aceptación o rechazo."""

    def __init__(self) -> None:
        self._icono = ft.Icon(ft.Icons.HELP_OUTLINE, size=34)
        self._titulo = ft.Text("", size=22, weight=ft.FontWeight.BOLD)
        self._detalle = ft.Text("", size=13, selectable=True)
        super().__init__(ft.Row([self._icono, ft.Column([self._titulo, self._detalle], spacing=2, expand=True)]),
                         padding=16, border_radius=RADIO, visible=False)

    def mostrar(self, aceptada: bool, detalle: str, titulo: str | None = None) -> None:
        color = Paleta.EXITO if aceptada else Paleta.ERROR
        self.bgcolor = Paleta.EXITO_CLARO if aceptada else Paleta.ERROR_CLARO
        self.border = ft.Border.all(1.5, color)
        self._icono.icon = ft.Icons.CHECK_CIRCLE if aceptada else ft.Icons.CANCEL
        self._icono.color = self._titulo.color = color
        self._titulo.value = titulo or ("ACEPTADA" if aceptada else "RECHAZADA")
        self._detalle.value = pantalla(detalle)
        self.visible = True

    def ocultar(self) -> None:
        self.visible = False


def chips(valores: Sequence[str], maximo: int = 400, destacar: Callable[[str], bool] | None = None) -> ft.Control:
    """Muestra palabras como pastillas; si son demasiadas indica cuántas se omiten."""
    piezas = []
    for v in list(valores)[:maximo]:
        marcado = destacar(v) if destacar else False
        piezas.append(ft.Container(
            ft.Text(pantalla(v), size=13, font_family=MONO, color=Paleta.GUINDA if marcado else Paleta.TEXTO),
            padding=ft.Padding.symmetric(horizontal=10, vertical=5), border_radius=20,
            bgcolor=Paleta.GUINDA_CLARO if marcado else "#F1EEF0", border=ft.Border.all(1, Paleta.BORDE)))
    if len(valores) > maximo:
        piezas.append(texto(f"… y {len(valores) - maximo} más (todas se incluyen al guardar)", 13, Paleta.TENUE))
    return ft.Row(piezas, wrap=True, spacing=6, run_spacing=6)


def tabla(encabezados: Sequence[str], filas: Sequence[Sequence[str]], resaltar: set[int] | None = None,
          mono: bool = True) -> ft.Control:
    """Tabla con encabezado guinda; ``resaltar`` indica filas a sombrear."""
    resaltar = resaltar or set()
    if len(encabezados) > 1 and encabezados[0] == "" and encabezados[1] == "δ":
        # La marca (→ inicial, * final) se escribe junto al estado para que no ocupe una columna angosta.
        encabezados = ["δ"] + list(encabezados[2:])
        filas = [[f"{f[0]} {f[1]}".strip()] + list(f[2:]) for f in filas]
    columnas = [ft.DataColumn(ft.Text(pantalla(h) or " ", weight=ft.FontWeight.W_600, color=Paleta.SUPERFICIE,
                                      size=13)) for h in encabezados]
    renglones = []
    for i, fila in enumerate(filas):
        celdas = [ft.DataCell(ft.Text(pantalla(str(c)), size=13, font_family=MONO if mono else None,
                                      no_wrap=True)) for c in fila]
        renglones.append(ft.DataRow(cells=celdas, color=Paleta.GUINDA_CLARO if i in resaltar else None))
    return ft.Row([ft.DataTable(
        columns=columnas, rows=renglones, heading_row_color=Paleta.GUINDA, heading_row_height=36,
        data_row_min_height=30, data_row_max_height=40, column_spacing=22, horizontal_lines=ft.BorderSide(1, Paleta.BORDE),
        border=ft.Border.all(1, Paleta.BORDE), border_radius=10)], scroll=ft.ScrollMode.AUTO)


def ayuda(pasos: Sequence[str]) -> ft.Container:
    """Instrucciones numeradas que se muestran con el botón «¿Cómo se usa?»."""
    filas = []
    for i, paso in enumerate(pasos, start=1):
        filas.append(ft.Row([
            ft.Container(ft.Text(str(i), size=12, color=Paleta.SUPERFICIE, weight=ft.FontWeight.BOLD),
                         width=24, height=24, border_radius=12, bgcolor=Paleta.DORADO,
                         alignment=ft.Alignment.CENTER),
            ft.Text(pantalla(paso), size=13, expand=True)], vertical_alignment=ft.CrossAxisAlignment.START))
    return ft.Container(ft.Column(filas, spacing=8), bgcolor="#FBF7F0", border=ft.Border.all(1, "#E8DCC8"),
                        border_radius=RADIO, padding=14, visible=False)


def boton(etiqueta: str, icono, accion, principal: bool = True, tooltip: str | None = None) -> ft.Control:
    clase = ft.FilledButton if principal else ft.OutlinedButton
    return clase(etiqueta, icon=icono, on_click=lambda e: accion(), tooltip=tooltip)


def metrica(valor: str, etiqueta: str, color: str = Paleta.GUINDA) -> ft.Container:
    return ft.Container(ft.Column([ft.Text(pantalla(valor), size=24, weight=ft.FontWeight.BOLD, color=color),
                                   ft.Text(pantalla(etiqueta), size=12, color=Paleta.TENUE)], spacing=0,
                                  horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                        padding=ft.Padding.symmetric(horizontal=18, vertical=10), border_radius=12,
                        bgcolor="#FAF7F8", border=ft.Border.all(1, Paleta.BORDE))


class VisorEtapas(ft.Column):
    """Recorre una lista de :class:`Etapa` con «Anterior» y «Siguiente».

    Muestra el número de paso, una barra de avance, la explicación, la tabla
    y, si la etapa trae un autómata, su diagrama.
    """

    def __init__(self, dibujar: Callable[[object], ft.Control] | None = None) -> None:
        self.etapas: list["Etapa"] = []
        self.indice = 0
        self._dibujar = dibujar
        self._contador = ft.Text("", size=12, color=Paleta.TENUE)
        self._barra = ft.ProgressBar(value=0, color=Paleta.GUINDA, bgcolor=Paleta.BORDE, bar_height=6,
                                     border_radius=3)
        self._titulo = titulo("", 15)
        self._explicacion = ft.Text("", size=13, selectable=True)
        self._cuerpo = ft.Column(spacing=10)
        self._anterior = ft.OutlinedButton("Anterior", icon=ft.Icons.CHEVRON_LEFT, on_click=lambda e: self.mover(-1))
        self._siguiente = ft.FilledButton("Siguiente", icon=ft.Icons.CHEVRON_RIGHT, on_click=lambda e: self.mover(1))
        self._todo = ft.TextButton("Ir al resultado", icon=ft.Icons.LAST_PAGE, on_click=lambda e: self.ir(-1))
        super().__init__([
            ft.Row([self._contador, ft.Container(expand=True), self._anterior, self._siguiente, self._todo]),
            self._barra, self._titulo, self._explicacion, self._cuerpo], spacing=10, visible=False)

    def cargar(self, etapas: list["Etapa"]) -> None:
        self.etapas, self.indice = etapas, 0
        self.visible = bool(etapas)
        self._pintar()

    def mover(self, delta: int) -> None:
        self.ir(max(0, min(len(self.etapas) - 1, self.indice + delta)))

    def ir(self, indice: int) -> None:
        self.indice = indice % len(self.etapas) if self.etapas else 0
        self._pintar()
        try:
            self.update()
        except RuntimeError:        # todavía no está en la página (por ejemplo, en las pruebas)
            pass

    def _pintar(self) -> None:
        if not self.etapas:
            return
        e = self.etapas[self.indice]
        n = len(self.etapas)
        self._contador.value = f"Paso {self.indice + 1} de {n}"
        self._barra.value = (self.indice + 1) / n
        self._titulo.value = pantalla(e.titulo)
        self._explicacion.value = pantalla(e.explicacion)
        self._anterior.disabled = self.indice == 0
        self._siguiente.disabled = self.indice == n - 1
        cuerpo: list[ft.Control] = []
        if e.encabezados:
            cuerpo.append(tabla(e.encabezados, e.filas))
        if e.automata is not None and self._dibujar is not None:
            cuerpo.append(self._dibujar(e.automata))
        self._cuerpo.controls = cuerpo
