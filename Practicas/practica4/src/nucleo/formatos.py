"""Persistencia de autómatas: JFLAP (.jff), JSON (.json) y XML (.xml).

Cada formato es un *serializador* con dos operaciones inversas:
``escribir(automata) -> str`` y ``leer(texto) -> Automata``. La clase
:class:`Archivos` elige el serializador por la extensión y trabaja con rutas.

Convención para λ
-----------------
La transición λ se guarda con el símbolo vacío: ``<read/>`` en .jff,
``""`` en .json y ``simbolo=""`` en .xml. Al leer se aceptan además «λ»,
«ε», «lambda» y «eps».

Esquemas propios
----------------
JSON::

    {"formato": "automata-tc", "version": 1, "nombre": "...", "tipo": "AFD",
     "alfabeto": ["a", "b"], "estados": ["q0", "q1"], "inicial": "q0",
     "aceptacion": ["q1"],
     "delta": {"q0": {"a": ["q1"], "": ["q0"]}, "q1": {}},
     "posiciones": {"q0": [80, 120], "q1": [240, 120]}}

XML::

    <automata formato="automata-tc" version="1" nombre="..." tipo="AFD">
      <alfabeto><simbolo>a</simbolo>...</alfabeto>
      <estados><estado id="q0" inicial="si" aceptacion="no" x="80" y="120"/>...</estados>
      <delta><desde estado="q0"><con simbolo="a"><hacia>q1</hacia></con></desde>...</delta>
    </automata>

Para leer archivos de otros compañeros, el lector JSON y el XML aceptan
también el esquema de ejemplo del Anexo 3 de la Práctica 2 (lista de
transiciones con ``desde``/``lee``/``hacia``).

El módulo no depende de Flet.
"""

from __future__ import annotations

import json
import xml.etree.ElementTree as ET
from abc import ABC, abstractmethod
from pathlib import Path

from .automata import EPSILON, Arista, Automata, Clasificador, es_lambda
from .errores import ArchivoInvalido, ErrorTC


def _simbolo(valor: str | None) -> str:
    return EPSILON if es_lambda(valor) else (valor or "").strip()


def _sangrar(raiz: ET.Element) -> str:
    ET.indent(raiz, space="  ")
    return '<?xml version="1.0" encoding="UTF-8" standalone="no"?>\n' + ET.tostring(raiz, encoding="unicode") + "\n"


class Serializador(ABC):
    """Interfaz común de los formatos."""

    EXTENSION = ""
    DESCRIPCION = ""

    @abstractmethod
    def escribir(self, automata: Automata) -> str: ...

    @abstractmethod
    def leer(self, texto: str, nombre: str = "") -> Automata: ...

    @staticmethod
    def _tipo_declarado(declarado: str | None, automata: Automata) -> None:
        """Rechaza archivos que se declaran AFD pero no lo son."""
        if declarado and declarado.upper() == "AFD" and Clasificador.clase_de(automata).TIPO != "AFD":
            pares = ", ".join(f"({q}, {a})" for q, a in Clasificador.no_determinismo(automata))
            raise ArchivoInvalido(f"El archivo se declara AFD pero no es determinista en {pares}.")


# ==========================================================================
# JFLAP
# ==========================================================================
class SerializadorJFF(Serializador):
    """Formato de JFLAP 7.1: ``<structure><type>fa</type><automaton>…``.

    JFLAP no guarda el alfabeto: al leer se infiere de las transiciones. Al
    escribir se conservan las coordenadas del autómata.
    """

    EXTENSION = ".jff"
    DESCRIPCION = "JFLAP 7.1"

    def escribir(self, automata: Automata) -> str:
        raiz = ET.Element("structure")
        ET.SubElement(raiz, "type").text = "fa"
        nodo = ET.SubElement(raiz, "automaton")
        ids = {q: str(i) for i, q in enumerate(automata.estados)}
        for q in automata.estados:
            x, y = automata.posicion(q)
            estado = ET.SubElement(nodo, "state", id=ids[q], name=q)
            ET.SubElement(estado, "x").text = f"{x:.1f}"
            ET.SubElement(estado, "y").text = f"{y:.1f}"
            if q == automata.inicial:
                ET.SubElement(estado, "initial")
            if q in automata.finales:
                ET.SubElement(estado, "final")
        for t in automata.aristas:
            tr = ET.SubElement(nodo, "transition")
            ET.SubElement(tr, "from").text = ids[t.origen]
            ET.SubElement(tr, "to").text = ids[t.destino]
            ET.SubElement(tr, "read").text = t.simbolo or None
        return _sangrar(raiz)

    def leer(self, texto: str, nombre: str = "") -> Automata:
        raiz = ET.fromstring(texto)
        tipo = (raiz.findtext("type") or "").strip()
        if raiz.tag != "structure" or tipo != "fa":
            raise ArchivoInvalido(f"No es un autómata finito de JFLAP (type = «{tipo or '?'}»).")
        nodo = raiz.find("automaton")
        nodo = raiz if nodo is None else nodo
        nombres: dict[str, str] = {}
        posiciones: dict[str, tuple[float, float]] = {}
        inicial, finales = None, []
        for e in nodo.iter("state"):
            ident = e.get("id")
            q = (e.get("name") or f"q{ident}").strip()
            nombres[ident] = q
            posiciones[q] = (float(e.findtext("x") or 0), float(e.findtext("y") or 0))
            if e.find("initial") is not None:
                if inicial is not None:
                    raise ArchivoInvalido("El archivo marca más de un estado inicial.")
                inicial = q
            if e.find("final") is not None:
                finales.append(q)
        if inicial is None:
            raise ArchivoInvalido("El archivo no marca un estado inicial.")
        aristas, alfabeto = [], []
        for t in nodo.iter("transition"):
            try:
                origen, destino = nombres[t.findtext("from")], nombres[t.findtext("to")]
            except KeyError as exc:
                raise ArchivoInvalido(f"Una transición usa el estado inexistente {exc}.") from exc
            simbolo = _simbolo(t.findtext("read"))
            if simbolo and simbolo not in alfabeto:
                alfabeto.append(simbolo)
            aristas.append(Arista(origen, simbolo, destino))
        if not alfabeto:
            raise ArchivoInvalido("No se puede inferir el alfabeto: no hay transiciones con símbolo.")
        return Automata.crear(list(nombres.values()), sorted(alfabeto), inicial, finales, aristas,
                              nombre, posiciones)


# ==========================================================================
# JSON
# ==========================================================================
class SerializadorJSON(Serializador):
    EXTENSION = ".json"
    DESCRIPCION = "JSON (esquema automata-tc)"

    def escribir(self, automata: Automata) -> str:
        delta: dict[str, dict[str, list[str]]] = {q: {} for q in automata.estados}
        for t in automata.aristas:
            delta[t.origen].setdefault(t.simbolo, []).append(t.destino)
        datos = {
            "formato": "automata-tc", "version": 1,
            "nombre": automata.nombre, "tipo": automata.tipo,
            "alfabeto": list(automata.alfabeto),
            "estados": list(automata.estados),
            "inicial": automata.inicial,
            "aceptacion": automata.orden(automata.finales),
            "delta": delta,
            "posiciones": {q: [round(x, 1), round(y, 1)] for q, (x, y) in automata.posiciones.items()},
        }
        return json.dumps(datos, ensure_ascii=False, indent=2) + "\n"

    def leer(self, texto: str, nombre: str = "") -> Automata:
        datos = json.loads(texto)
        if not isinstance(datos, dict):
            raise ArchivoInvalido("El JSON debe ser un objeto.")
        try:
            aristas = []
            if "delta" in datos:
                for q, fila in datos["delta"].items():
                    for a, destinos in fila.items():
                        aristas += [Arista(q, _simbolo(a), d) for d in destinos]
            else:                              # esquema del Anexo 3
                for t in datos["transiciones"]:
                    hacia = t["hacia"] if isinstance(t["hacia"], list) else [t["hacia"]]
                    aristas += [Arista(t["desde"], _simbolo(t["lee"]), d) for d in hacia]
            posiciones = {q: tuple(p) for q, p in datos.get("posiciones", {}).items()}
            automata = Automata.crear(datos["estados"], datos["alfabeto"], datos["inicial"],
                                      datos.get("aceptacion", []), aristas,
                                      datos.get("nombre") or nombre, posiciones)
        except KeyError as exc:
            raise ArchivoInvalido(f"Falta la clave {exc} en el JSON.") from exc
        self._tipo_declarado(datos.get("tipo"), automata)
        return automata


# ==========================================================================
# XML
# ==========================================================================
class SerializadorXML(Serializador):
    EXTENSION = ".xml"
    DESCRIPCION = "XML (esquema automata-tc)"

    def escribir(self, automata: Automata) -> str:
        raiz = ET.Element("automata", formato="automata-tc", version="1",
                          nombre=automata.nombre, tipo=automata.tipo)
        sigma = ET.SubElement(raiz, "alfabeto")
        for a in automata.alfabeto:
            ET.SubElement(sigma, "simbolo").text = a
        estados = ET.SubElement(raiz, "estados")
        for q in automata.estados:
            x, y = automata.posicion(q)
            ET.SubElement(estados, "estado", id=q,
                          inicial="si" if q == automata.inicial else "no",
                          aceptacion="si" if q in automata.finales else "no",
                          x=f"{x:.1f}", y=f"{y:.1f}")
        delta = ET.SubElement(raiz, "delta")
        nodos: dict[tuple[str, str], ET.Element] = {}
        desde: dict[str, ET.Element] = {}
        for t in automata.aristas:
            if t.origen not in desde:
                desde[t.origen] = ET.SubElement(delta, "desde", estado=t.origen)
            if (t.origen, t.simbolo) not in nodos:
                nodos[(t.origen, t.simbolo)] = ET.SubElement(desde[t.origen], "con", simbolo=t.simbolo)
            ET.SubElement(nodos[(t.origen, t.simbolo)], "hacia").text = t.destino
        return _sangrar(raiz)

    @staticmethod
    def _si(valor: str | None) -> bool:
        return (valor or "").strip().lower() in ("si", "sí", "true", "1", "yes")

    def leer(self, texto: str, nombre: str = "") -> Automata:
        raiz = ET.fromstring(texto)
        if raiz.tag != "automata":
            raise ArchivoInvalido(f"La raíz del XML debe ser <automata>, no <{raiz.tag}>.")
        alfabeto = [(s.text or "").strip() for s in raiz.iter("simbolo")]
        estados, finales, posiciones, inicial = [], [], {}, None
        for e in raiz.iter("estado"):
            q = (e.get("id") or e.get("nombre") or "").strip()
            estados.append(q)
            if self._si(e.get("inicial")):
                inicial = q
            if self._si(e.get("aceptacion")):
                finales.append(q)
            if e.get("x") is not None:
                posiciones[q] = (float(e.get("x")), float(e.get("y") or 0))
        if inicial is None:
            raise ArchivoInvalido("Ningún <estado> está marcado como inicial.")
        aristas = []
        for d in raiz.iter("desde"):
            for con in d.iter("con"):
                aristas += [Arista(d.get("estado"), _simbolo(con.get("simbolo")), (h.text or "").strip())
                            for h in con.iter("hacia")]
        for t in raiz.iter("transicion"):           # esquema del Anexo 3
            aristas.append(Arista(t.get("desde"), _simbolo(t.get("lee")), t.get("hacia")))
        automata = Automata.crear(estados, alfabeto, inicial, finales, aristas,
                                  raiz.get("nombre") or nombre, posiciones)
        self._tipo_declarado(raiz.get("tipo"), automata)
        return automata


# ==========================================================================
# Fachada por extensión
# ==========================================================================
class Archivos:
    """Abre y guarda autómatas eligiendo el formato por la extensión."""

    SERIALIZADORES: dict[str, Serializador] = {
        s.EXTENSION: s for s in (SerializadorJFF(), SerializadorJSON(), SerializadorXML())}

    @classmethod
    def extensiones(cls) -> tuple[str, ...]:
        return tuple(cls.SERIALIZADORES)

    @classmethod
    def serializador(cls, ruta: str | Path) -> Serializador:
        extension = Path(ruta).suffix.lower()
        if extension not in cls.SERIALIZADORES:
            raise ArchivoInvalido(f"Extensión «{extension or '(ninguna)'}» no admitida; "
                                  f"use {', '.join(cls.SERIALIZADORES)}.")
        return cls.SERIALIZADORES[extension]

    @classmethod
    def abrir(cls, ruta: str | Path) -> Automata:
        ruta = Path(ruta)
        serializador = cls.serializador(ruta)
        if not ruta.is_file():
            raise ArchivoInvalido(f"No existe el archivo {ruta}.")
        try:
            return serializador.leer(ruta.read_text(encoding="utf-8"), nombre=ruta.stem)
        except (ET.ParseError, json.JSONDecodeError) as exc:
            raise ArchivoInvalido(f"{ruta.name} está mal formado: {exc}.") from exc
        except ErrorTC as exc:
            raise ArchivoInvalido(f"{ruta.name}: {exc}") from exc

    @classmethod
    def guardar(cls, automata: Automata, ruta: str | Path) -> Path:
        ruta = Path(ruta)
        texto = cls.serializador(ruta).escribir(automata)
        ruta.parent.mkdir(parents=True, exist_ok=True)
        ruta.write_text(texto, encoding="utf-8")
        return ruta

    @classmethod
    def guardar_en_todos(cls, automata: Automata, base: str | Path) -> list[Path]:
        base = Path(base)
        return [cls.guardar(automata, base.with_suffix(ext)) for ext in cls.SERIALIZADORES]
