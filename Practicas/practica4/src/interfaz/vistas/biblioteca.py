"""Importar y exportar autómatas en .jff, .json y .xml (Práctica 2, 3.2 y 3.4)."""

from __future__ import annotations

from pathlib import Path

import flet as ft

from nucleo.automata import Automata, Clasificador
from nucleo.errores import ErrorTC
from nucleo.formatos import Archivos

from ..componentes import boton, tabla, tarjeta
from ..diagrama import Diagrama
from ..tema import MONO, Paleta, pantalla
from .base import Vista

ICONOS = {".jff": ft.Icons.ACCOUNT_TREE_OUTLINED, ".json": ft.Icons.DATA_OBJECT, ".xml": ft.Icons.CODE}


class Biblioteca(Vista):
    CLAVE = "biblioteca"
    TITULO = "Biblioteca"
    ICONO = ft.Icons.FOLDER_OPEN
    DESCRIPCION = "Abra autómatas de la carpeta automatas/ (o de cualquier ruta) y guárdelos en los tres formatos."
    USA_AUTOMATA = True
    PASOS = [
        "Escriba parte del nombre en el buscador para filtrar (por ejemplo «196» o «afd»).",
        "Toque un archivo para ver su quíntupla, su diagrama y su tabla; nada cambia hasta pulsar «Usar».",
        "Para un archivo fuera de la carpeta, escriba su ruta y pulse «Abrir ruta».",
        "En «Guardar» elija el nombre y el formato; los archivos se escriben en salidas/.",
    ]

    def contenido(self) -> ft.Control:
        self.buscar = ft.TextField(label="Buscar", prefix_icon=ft.Icons.SEARCH, dense=True,
                                   on_change=lambda e: self._listar())
        self.lista = ft.ListView(spacing=2, height=430)
        self.ruta = ft.TextField(label="Otra ruta", hint_text="archivo .jff, .json o .xml", expand=True)
        self.quintupla = ft.Column(spacing=2)
        self.diagrama = Diagrama(640, 320)
        self.tabla = ft.Column()
        self.nombre = ft.TextField(label="Nombre del archivo", value="automata", width=240, dense=True)
        self.guardados = ft.Column(spacing=2)
        self._previo: Automata | None = None
        izquierda = tarjeta(ft.Column([self.buscar, self.lista,
                                       ft.Row([self.ruta, boton("Abrir ruta", ft.Icons.FILE_OPEN,
                                                                lambda: self.ejecutar(self.abrir_ruta), False)])],
                                      spacing=10), "Archivos", ft.Icons.FOLDER, col={"xs": 12, "lg": 4})
        derecha = tarjeta(ft.Column([self.quintupla, self.diagrama, self.tabla,
                                     ft.Row([boton("Usar", ft.Icons.CHECK, lambda: self.ejecutar(self.usar)),
                                             boton("Simular", ft.Icons.PLAY_CIRCLE_OUTLINE,
                                                   lambda: self.ejecutar(self.usar_y_simular), False)])],
                                    spacing=10), "Vista previa", ft.Icons.VISIBILITY, col={"xs": 12, "lg": 8})
        exportar = tarjeta(ft.Column([
            ft.Text("Guarda el autómata activo. λ se escribe con el símbolo vacío en los tres formatos.",
                    size=13, color=Paleta.TENUE),
            ft.Row([self.nombre] + [boton(ext, ICONOS[ext], lambda ext=ext: self.ejecutar(lambda: self.guardar(ext)),
                                          False) for ext in Archivos.extensiones()]
                   + [boton("Los tres", ft.Icons.SAVE, lambda: self.ejecutar(lambda: self.guardar(None)))], wrap=True),
            self.guardados]), "Guardar", ft.Icons.SAVE_ALT)
        self._listar()
        return ft.Column([ft.ResponsiveRow([izquierda, derecha], spacing=16), exportar], spacing=16)

    def al_mostrar(self) -> None:
        m = self.sesion.automata
        if m is not None:
            self.nombre.value = m.nombre or "automata"
            if self._previo is None:
                self._previo = m
                self.quintupla.controls = [ft.Text("Autómata activo", weight=ft.FontWeight.W_600)] + [
                    ft.Text(pantalla(linea), font_family=MONO, size=13, selectable=True) for linea in m.quintupla()]
                self.diagrama.dibujar(m)
                self.tabla.controls = [tabla(*m.tabla())]

    # ------------------------------------------------------------------
    def _archivos(self) -> list[Path]:
        if not self.sesion.biblioteca.is_dir():
            return []
        return sorted(p for p in self.sesion.biblioteca.rglob("*") if p.suffix in Archivos.extensiones())

    def _listar(self) -> None:
        filtro = (self.buscar.value or "").lower()
        elementos = []
        for p in self._archivos():
            relativo = p.relative_to(self.sesion.biblioteca)
            if filtro and filtro not in str(relativo).lower():
                continue
            elementos.append(ft.ListTile(
                leading=ft.Icon(ICONOS[p.suffix], color=Paleta.GUINDA), dense=True,
                title=ft.Text(p.name, font_family=MONO, size=13),
                subtitle=ft.Text(str(relativo.parent), size=11, color=Paleta.TENUE),
                on_click=lambda e, p=p: self.ejecutar(lambda: self.previsualizar(p))))
        self.lista.controls = elementos or [ft.Text("No hay archivos que coincidan.", color=Paleta.TENUE)]
        self.refrescar()

    def previsualizar(self, ruta: Path) -> None:
        m = Archivos.abrir(ruta)
        self._previo = m
        self.quintupla.controls = [ft.Row([
            ft.Container(ft.Text(m.tipo, color=Paleta.SUPERFICIE, weight=ft.FontWeight.BOLD), bgcolor=Paleta.GUINDA,
                         border_radius=20, padding=ft.Padding.symmetric(horizontal=12, vertical=4)),
            ft.Text(ruta.name, weight=ft.FontWeight.W_600), ft.Text(pantalla(Clasificador.motivo(m)), size=12,
                                                                     color=Paleta.TENUE, expand=True)])]
        self.quintupla.controls += [ft.Text(pantalla(linea), font_family=MONO, size=13, selectable=True)
                                    for linea in m.quintupla()]
        self.diagrama.dibujar(m)
        self.tabla.controls = [tabla(*m.tabla())]
        self.nombre.value = m.nombre

    def abrir_ruta(self) -> None:
        texto = (self.ruta.value or "").strip()
        if not texto:
            raise ErrorTC("Escriba la ruta del archivo.")
        ruta = Path(texto).expanduser()
        if not ruta.is_absolute() and not ruta.exists():
            ruta = self.sesion.raiz / ruta
        self.previsualizar(ruta)

    def usar(self) -> None:
        if self._previo is None:
            raise ErrorTC("Elija primero un archivo de la lista.")
        self.sesion.usar(self._previo)
        self.aviso.mostrar(f"«{self._previo.nombre}» es ahora el autómata activo.", "ok")

    def usar_y_simular(self) -> None:
        self.usar()
        self.sesion.navegar("simulador")

    def guardar(self, extension: str | None) -> None:
        m = self.exigir_automata()
        base = self.salida(self.nombre.value.strip() or "automata")
        rutas = Archivos.guardar_en_todos(m, base) if extension is None else [
            Archivos.guardar(m, base.with_suffix(extension))]
        self.guardados.controls = [ft.Row([ft.Icon(ft.Icons.CHECK, color=Paleta.EXITO, size=16),
                                           ft.Text(str(r), font_family=MONO, size=12, selectable=True)])
                                   for r in rutas]
        self.aviso.mostrar(f"Se guardaron {len(rutas)} archivo(s) en {base.parent}", "ok")
