"""Autómatas finitos: AFD, AFN y AFN-λ como una jerarquía de clases.

Jerarquía
---------
``Automata`` (semántica general, con transiciones λ)
    └── ``AFNLambda``  – admite transiciones λ.
          └── ``AFN``  – prohíbe transiciones λ.
                └── ``AFD`` – además, a lo sumo un destino por (estado, símbolo).

Cada subclase *restringe* a la anterior: un AFD es un AFN y un AFN es un
AFN-λ. Por eso basta un solo algoritmo de simulación (conjuntos de estados
activos con cerradura λ) y cada subclase sólo añade validaciones y atajos.
``Automata.crear`` elige la clase más específica que admite la definición.

La simulación sigue todos los caminos a la vez: en cada paso se guarda el
conjunto de estados activos antes de leer el símbolo, después de moverse y
después de aplicar la cerradura λ (clase :class:`Paso`). La función de
transición puede ser parcial: si un par (estado, símbolo) no tiene destino,
ese camino muere.

El módulo no depende de Flet.
"""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass, field
from typing import Iterable, Mapping

from .errores import DefinicionInvalida, PalabraFueraDeAlfabeto

LAMBDA = "λ"
"""Nombre visible de la transición vacía."""

EPSILON = ""
"""Clave interna con la que se guarda la transición λ."""

_SINONIMOS_LAMBDA = {"", LAMBDA, "ε", "lambda", "eps"}


def es_lambda(simbolo: str | None) -> bool:
    return (simbolo or "").strip() in _SINONIMOS_LAMBDA


def conjunto(estados: Iterable[str], orden: Iterable[str] | None = None) -> str:
    """Formatea un conjunto de estados: ``{A, B}``; el vacío es ``∅``."""
    estados = list(estados)
    if not estados:
        return "∅"
    if orden is not None:
        rango = {q: i for i, q in enumerate(orden)}
        estados.sort(key=lambda q: (rango.get(q, len(rango)), q))
    else:
        estados.sort()
    return "{" + ", ".join(estados) + "}"


@dataclass(frozen=True, order=True)
class Arista:
    """Una transición (origen, símbolo, destino); ``simbolo == ""`` es λ."""

    origen: str
    simbolo: str
    destino: str

    @property
    def es_lambda(self) -> bool:
        return self.simbolo == EPSILON

    def __str__(self) -> str:
        return f"δ({self.origen}, {self.simbolo or LAMBDA}) ∋ {self.destino}"


# ==========================================================================
# Recorrido de una palabra
# ==========================================================================
@dataclass(frozen=True)
class Paso:
    """Lectura de un símbolo durante la simulación."""

    numero: int
    simbolo: str
    antes: frozenset[str]
    movidos: frozenset[str]
    despues: frozenset[str]
    aristas: tuple[Arista, ...]

    @property
    def agrego_cierre(self) -> frozenset[str]:
        """Estados que aparecieron sólo por la cerradura λ."""
        return self.despues - self.movidos


@dataclass
class Recorrido:
    """Resultado completo de procesar una palabra."""

    palabra: str
    inicio: frozenset[str]
    inicio_cerrado: frozenset[str]
    pasos: list[Paso] = field(default_factory=list)
    aceptada: bool = False
    finales: frozenset[str] = frozenset()

    @property
    def activos(self) -> frozenset[str]:
        return self.pasos[-1].despues if self.pasos else self.inicio_cerrado

    @property
    def murio_en(self) -> int | None:
        """Número del paso en que se vació el conjunto de activos (o ``None``)."""
        for paso in self.pasos:
            if not paso.despues:
                return paso.numero
        return None

    def lineas(self, orden: Iterable[str] | None = None) -> list[str]:
        """Traza legible, una línea por paso."""
        orden = list(orden) if orden is not None else None
        texto = self.palabra or LAMBDA
        lineas = [f"Palabra: {texto}",
                  f"Inicio: {conjunto(self.inicio, orden)}  cierre λ ⇒ {conjunto(self.inicio_cerrado, orden)}"]
        for p in self.pasos:
            extra = f"  cierre λ ⇒ {conjunto(p.despues, orden)}" if p.agrego_cierre else ""
            lineas.append(f"{p.numero}. lee «{p.simbolo}»: {conjunto(p.antes, orden)} "
                          f"→ {conjunto(p.movidos, orden)}{extra}")
        veredicto = "ACEPTADA" if self.aceptada else "RECHAZADA"
        motivo = (f"contiene el estado final {conjunto(self.activos & self.finales, orden)}" if self.aceptada
                  else "no quedan estados activos" if not self.activos
                  else "ningún estado activo es de aceptación")
        lineas.append(f"Resultado: {veredicto} ({motivo}).")
        return lineas


class Simulacion:
    """Simulación interactiva: avanza un símbolo por llamada a :meth:`avanzar`."""

    def __init__(self, automata: "Automata", palabra: str) -> None:
        automata.validar_palabra(palabra)
        self.automata = automata
        self.palabra = palabra
        self.indice = 0
        inicio = frozenset({automata.inicial})
        self.recorrido = Recorrido(palabra, inicio, automata.cierre(inicio), finales=automata.finales)
        self.recorrido.aceptada = automata.es_aceptacion(self.recorrido.inicio_cerrado)

    @property
    def activos(self) -> frozenset[str]:
        return self.recorrido.activos

    @property
    def terminada(self) -> bool:
        return self.indice >= len(self.palabra)

    @property
    def leido(self) -> str:
        return self.palabra[:self.indice]

    @property
    def pendiente(self) -> str:
        return self.palabra[self.indice:]

    def avanzar(self) -> Paso:
        if self.terminada:
            raise DefinicionInvalida("La palabra ya se leyó completa.")
        simbolo = self.palabra[self.indice]
        antes = self.activos
        aristas = tuple(Arista(q, simbolo, d) for q in sorted(antes)
                        for d in sorted(self.automata.destinos(q, simbolo)))
        movidos = frozenset(a.destino for a in aristas)
        paso = Paso(self.indice + 1, simbolo, antes, movidos, self.automata.cierre(movidos), aristas)
        self.recorrido.pasos.append(paso)
        self.indice += 1
        self.recorrido.aceptada = self.automata.es_aceptacion(paso.despues)
        return paso

    def completar(self) -> Recorrido:
        while not self.terminada:
            self.avanzar()
        return self.recorrido


# ==========================================================================
# Autómata general
# ==========================================================================
class Automata:
    """Quíntupla (Q, Σ, δ, q₀, F) con δ: Q × (Σ ∪ {λ}) → 𝒫(Q).

    Los estados y el alfabeto conservan el orden en que se dieron; ese orden
    se usa en tablas, diagramas y archivos exportados.
    """

    TIPO = "AFN-λ"
    DESCRIPCION = "autómata finito no determinista con transiciones λ"

    def __init__(self, estados: Iterable[str], alfabeto: Iterable[str], inicial: str,
                 finales: Iterable[str], aristas: Iterable[Arista | tuple[str, str, str]],
                 nombre: str = "", posiciones: Mapping[str, tuple[float, float]] | None = None) -> None:
        self._estados = self._normalizar_estados(estados)
        self._alfabeto = self._normalizar_alfabeto(alfabeto)
        self._inicial = str(inicial).strip()
        self._finales = frozenset(str(q).strip() for q in finales)
        self.nombre = nombre
        self._delta: dict[str, dict[str, set[str]]] = {q: {} for q in self._estados}
        for arista in aristas:
            self._agregar(arista if isinstance(arista, Arista) else Arista(*arista))
        self._validar()
        self._cierres: dict[str, frozenset[str]] | None = None
        conocidas = {q: p for q, p in (posiciones or {}).items() if q in self._delta}
        self.posiciones: dict[str, tuple[float, float]] = (
            conocidas if len(conocidas) == len(self._estados) else Disposicion.por_niveles(self))

    # ------------------------------------------------------------------
    # Construcción y validación
    # ------------------------------------------------------------------
    @staticmethod
    def _normalizar_estados(estados: Iterable[str]) -> tuple[str, ...]:
        vistos: list[str] = []
        for q in estados:
            q = str(q).strip()
            if not q:
                raise DefinicionInvalida("Hay un estado sin nombre.")
            if q in vistos:
                raise DefinicionInvalida(f"El estado «{q}» está repetido.")
            vistos.append(q)
        if not vistos:
            raise DefinicionInvalida("El conjunto de estados Q no puede ser vacío.")
        return tuple(vistos)

    @staticmethod
    def _normalizar_alfabeto(alfabeto: Iterable[str]) -> tuple[str, ...]:
        vistos: list[str] = []
        for a in alfabeto:
            a = str(a)
            if es_lambda(a):
                raise DefinicionInvalida("λ no es un símbolo del alfabeto: se usa para las transiciones vacías.")
            if any(c in a for c in ", \t\n"):
                raise DefinicionInvalida(f"El símbolo «{a}» contiene espacios o comas.")
            if a not in vistos:
                vistos.append(a)
        if not vistos:
            raise DefinicionInvalida("El alfabeto Σ no puede ser vacío.")
        return tuple(vistos)

    def _agregar(self, arista: Arista) -> None:
        simbolo = EPSILON if es_lambda(arista.simbolo) else arista.simbolo
        origen, destino = arista.origen.strip(), arista.destino.strip()
        for q in (origen, destino):
            if q not in self._delta:
                raise DefinicionInvalida(f"La transición δ({origen}, {simbolo or LAMBDA}) = {destino} "
                                         f"usa el estado «{q}», que no está en Q.")
        if simbolo != EPSILON and simbolo not in self._alfabeto:
            raise DefinicionInvalida(f"La transición δ({origen}, {simbolo}) usa «{simbolo}», que no está en Σ.")
        self._delta[origen].setdefault(simbolo, set()).add(destino)

    def _validar(self) -> None:
        if self._inicial not in self._delta:
            raise DefinicionInvalida(f"El estado inicial «{self._inicial}» no está en Q.")
        ajenos = sorted(self._finales - set(self._estados))
        if ajenos:
            raise DefinicionInvalida(f"Los estados de aceptación {', '.join(ajenos)} no están en Q.")

    @classmethod
    def crear(cls, estados, alfabeto, inicial, finales, aristas, nombre: str = "",
              posiciones=None) -> "Automata":
        """Construye el autómata con la clase más específica que lo admite."""
        general = AFNLambda(estados, alfabeto, inicial, finales, aristas, nombre, posiciones)
        clase = Clasificador.clase_de(general)
        if clase is AFNLambda:
            return general
        return clase(general.estados, general.alfabeto, general.inicial, general.finales,
                     general.aristas, nombre, general.posiciones)

    @classmethod
    def desde_tabla(cls, estados, alfabeto, inicial, finales,
                    tabla: Mapping[tuple[str, str], Iterable[str]], nombre: str = "") -> "Automata":
        """Construye desde una tabla {(estado, símbolo): destinos}; símbolo ``""`` = λ."""
        aristas = [Arista(q, a, d) for (q, a), destinos in tabla.items() for d in destinos]
        return cls.crear(estados, alfabeto, inicial, finales, aristas, nombre)

    # ------------------------------------------------------------------
    # Consulta
    # ------------------------------------------------------------------
    @property
    def estados(self) -> tuple[str, ...]:
        return self._estados

    @property
    def alfabeto(self) -> tuple[str, ...]:
        return self._alfabeto

    @property
    def inicial(self) -> str:
        return self._inicial

    @property
    def finales(self) -> frozenset[str]:
        return self._finales

    @property
    def aristas(self) -> list[Arista]:
        rango = {q: i for i, q in enumerate(self._estados)}
        orden_simbolo = {a: i for i, a in enumerate(self._alfabeto + (EPSILON,))}
        lista = [Arista(q, a, d) for q, fila in self._delta.items() for a, ds in fila.items() for d in ds]
        return sorted(lista, key=lambda t: (rango[t.origen], orden_simbolo[t.simbolo], rango[t.destino]))

    @property
    def tiene_lambda(self) -> bool:
        return any(EPSILON in fila for fila in self._delta.values())

    @property
    def tipo(self) -> str:
        return self.TIPO

    def columnas(self) -> tuple[str, ...]:
        """Símbolos de la tabla de transiciones; λ va al final si se usa."""
        return self._alfabeto + ((EPSILON,) if self.tiene_lambda else ())

    def destinos(self, estado: str, simbolo: str) -> frozenset[str]:
        return frozenset(self._delta.get(estado, {}).get(EPSILON if es_lambda(simbolo) else simbolo, ()))

    def es_aceptacion(self, activos: Iterable[str]) -> bool:
        return not self._finales.isdisjoint(activos)

    def orden(self, estados: Iterable[str]) -> list[str]:
        rango = {q: i for i, q in enumerate(self._estados)}
        return sorted(estados, key=lambda q: rango.get(q, len(rango)))

    def posicion(self, estado: str) -> tuple[float, float]:
        return self.posiciones[estado]

    # ------------------------------------------------------------------
    # Cerradura λ y función de transición extendida
    # ------------------------------------------------------------------
    def cierre(self, estados: Iterable[str]) -> frozenset[str]:
        """λ-cl(S): estados alcanzables desde S usando sólo transiciones λ."""
        visitados = set(estados)
        pila = list(visitados)
        while pila:
            q = pila.pop()
            for r in self._delta[q].get(EPSILON, ()):
                if r not in visitados:
                    visitados.add(r)
                    pila.append(r)
        return frozenset(visitados)

    def cierres(self) -> dict[str, frozenset[str]]:
        """λ-cl(q) de cada estado (se calcula una sola vez)."""
        if self._cierres is None:
            self._cierres = {q: self.cierre({q}) for q in self._estados}
        return dict(self._cierres)

    def mover(self, estados: Iterable[str], simbolo: str) -> frozenset[str]:
        """δ(S, a) = ⋃ δ(q, a) para q ∈ S, sin cerradura."""
        return frozenset(d for q in estados for d in self._delta[q].get(simbolo, ()))

    def transitar(self, estados: Iterable[str], simbolo: str) -> frozenset[str]:
        """λ-cl(δ(S, a)): un paso completo de la simulación."""
        return self.cierre(self.mover(estados, simbolo))

    def delta_extendida(self, estado: str, palabra: str) -> frozenset[str]:
        """δ̂(q, ω) definida recursivamente sobre la palabra."""
        self.validar_palabra(palabra)
        activos = self.cierre({estado})
        for simbolo in palabra:
            activos = self.transitar(activos, simbolo)
        return activos

    # ------------------------------------------------------------------
    # Reconocimiento
    # ------------------------------------------------------------------
    def validar_palabra(self, palabra: str) -> None:
        if len(max(self._alfabeto, key=len)) > 1:
            raise DefinicionInvalida("El reconocimiento de palabras requiere símbolos de un carácter.")
        fuera = sorted({c for c in palabra if c not in self._alfabeto})
        if fuera:
            raise PalabraFueraDeAlfabeto(f"«{palabra}» contiene {', '.join(fuera)}, que no está en "
                                         f"Σ = {{{', '.join(self._alfabeto)}}}.")

    def acepta(self, palabra: str) -> bool:
        return self.es_aceptacion(self.delta_extendida(self._inicial, palabra))

    def simulacion(self, palabra: str) -> Simulacion:
        return Simulacion(self, palabra)

    def recorrer(self, palabra: str) -> Recorrido:
        return Simulacion(self, palabra).completar()

    # ------------------------------------------------------------------
    # Estructura
    # ------------------------------------------------------------------
    def alcanzables(self) -> list[str]:
        """Estados accesibles desde q₀ (por cualquier símbolo o λ), en orden BFS."""
        vistos, cola = [self._inicial], deque([self._inicial])
        while cola:
            q = cola.popleft()
            for destinos in self._delta[q].values():
                for r in sorted(destinos, key=self._estados.index):
                    if r not in vistos:
                        vistos.append(r)
                        cola.append(r)
        return vistos

    def tabla(self) -> tuple[list[str], list[list[str]]]:
        """Encabezados y filas de la tabla de transiciones (→ inicial, * final)."""
        columnas = self.columnas()
        encabezados = ["", "δ"] + [a or LAMBDA for a in columnas]
        filas = []
        for q in self._estados:
            marca = ("→" if q == self._inicial else "") + ("*" if q in self._finales else "")
            celdas = [self._celda(self.destinos(q, a)) for a in columnas]
            filas.append([marca, q] + celdas)
        return encabezados, filas

    def _celda(self, destinos: frozenset[str]) -> str:
        return conjunto(destinos, self._estados)

    def tabla_texto(self) -> str:
        encabezados, filas = self.tabla()
        anchos = [max(len(str(f[i])) for f in [encabezados] + filas) for i in range(len(encabezados))]
        lineas = ["  ".join(str(c).ljust(w) for c, w in zip(f, anchos)).rstrip() for f in [encabezados] + filas]
        return "\n".join(lineas)

    def quintupla(self) -> list[str]:
        """Los cinco componentes en notación de conjuntos."""
        return [
            f"Q  = {conjunto(self._estados, self._estados)}  (|Q| = {len(self._estados)})",
            f"Σ  = {{{', '.join(self._alfabeto)}}}",
            f"q₀ = {self._inicial}",
            f"F  = {conjunto(self._finales, self._estados)}",
            f"δ  = {len(self.aristas)} transiciones" + (" (incluye λ)" if self.tiene_lambda else ""),
        ]

    def renombrar(self, mapa: Mapping[str, str], nombre: str | None = None) -> "Automata":
        """Copia con los estados renombrados según ``mapa`` (los ausentes se conservan)."""
        f = lambda q: mapa.get(q, q)  # noqa: E731
        return type(self)([f(q) for q in self._estados], self._alfabeto, f(self._inicial),
                          [f(q) for q in self._finales],
                          [Arista(f(t.origen), t.simbolo, f(t.destino)) for t in self.aristas],
                          self.nombre if nombre is None else nombre,
                          {f(q): p for q, p in self.posiciones.items()})

    def renumerar(self, prefijo: str = "q", nombre: str | None = None) -> "Automata":
        """Copia con estados q0, q1, … en orden BFS desde el inicial (los inaccesibles al final)."""
        orden = self.alcanzables() + [q for q in self._estados if q not in self.alcanzables()]
        copia = self.renombrar({q: f"{prefijo}{i}" for i, q in enumerate(orden)}, nombre)
        copia._estados = tuple(f"{prefijo}{i}" for i in range(len(orden)))
        copia._delta = {q: copia._delta[q] for q in copia._estados}
        copia.posiciones = Disposicion.por_niveles(copia)
        return copia

    def con_alfabeto(self, alfabeto: Iterable[str]) -> "Automata":
        """Copia con un alfabeto ampliado (útil al comparar dos autómatas)."""
        nuevo = list(self._alfabeto) + [a for a in alfabeto if a not in self._alfabeto]
        return type(self)(self._estados, nuevo, self._inicial, self._finales, self.aristas,
                          self.nombre, self.posiciones)

    def __repr__(self) -> str:
        return (f"{type(self).__name__}(nombre={self.nombre!r}, |Q|={len(self._estados)}, "
                f"Σ={list(self._alfabeto)}, q0={self._inicial!r}, F={sorted(self._finales)})")


class AFNLambda(Automata):
    """AFN con transiciones λ: la clase más general."""


class AFN(AFNLambda):
    """AFN sin transiciones λ."""

    TIPO = "AFN"
    DESCRIPCION = "autómata finito no determinista"

    def _validar(self) -> None:
        super()._validar()
        for q, fila in self._delta.items():
            if EPSILON in fila:
                raise DefinicionInvalida(f"Un AFN no admite transiciones λ y {q} tiene una.")

    def cierre(self, estados: Iterable[str]) -> frozenset[str]:
        return frozenset(estados)


class AFD(AFN):
    """AFN en el que cada par (estado, símbolo) tiene a lo sumo un destino.

    Se admite δ parcial: un par sin destino equivale a ir a un estado sumidero
    implícito. :meth:`completar` lo hace explícito.
    """

    TIPO = "AFD"
    DESCRIPCION = "autómata finito determinista"

    def _validar(self) -> None:
        super()._validar()
        for q, fila in self._delta.items():
            for a, destinos in fila.items():
                if len(destinos) > 1:
                    raise DefinicionInvalida(f"No es determinista: δ({q}, {a}) = {conjunto(destinos)}.")

    def siguiente(self, estado: str, simbolo: str) -> str | None:
        destinos = self._delta.get(estado, {}).get(simbolo)
        return next(iter(destinos)) if destinos else None

    @property
    def es_completo(self) -> bool:
        return all(self.siguiente(q, a) is not None for q in self._estados for a in self._alfabeto)

    def faltantes(self) -> list[tuple[str, str]]:
        return [(q, a) for q in self._estados for a in self._alfabeto if self.siguiente(q, a) is None]

    def _celda(self, destinos: frozenset[str]) -> str:
        return next(iter(destinos)) if destinos else "—"

    def completar(self, sumidero: str = "∅") -> "AFD":
        """AFD equivalente con δ total, añadiendo un sumidero si hace falta."""
        if self.es_completo:
            return self
        nombre = sumidero
        while nombre in self._estados:
            nombre += "'"
        aristas = self.aristas + [Arista(q, a, nombre) for q, a in self.faltantes()]
        aristas += [Arista(nombre, a, nombre) for a in self._alfabeto]
        return AFD(self._estados + (nombre,), self._alfabeto, self._inicial, self._finales, aristas,
                   self.nombre)


# ==========================================================================
# Clasificación y disposición
# ==========================================================================
class Clasificador:
    """Decide el tipo de un autómata a partir de su función de transición."""

    @staticmethod
    def clase_de(automata: Automata) -> type[Automata]:
        if automata.tiene_lambda:
            return AFNLambda
        if all(len(automata.destinos(q, a)) <= 1 for q in automata.estados for a in automata.alfabeto):
            return AFD
        return AFN

    @staticmethod
    def motivo(automata: Automata) -> str:
        """Explica en una línea por qué el autómata tiene el tipo que tiene."""
        lambdas = [t for t in automata.aristas if t.es_lambda]
        if lambdas:
            t = lambdas[0]
            return f"Tiene transiciones λ, por ejemplo δ({t.origen}, λ) ∋ {t.destino}."
        for q in automata.estados:
            for a in automata.alfabeto:
                ds = automata.destinos(q, a)
                if len(ds) > 1:
                    return f"Hay elección: δ({q}, {a}) = {conjunto(ds, automata.estados)}."
        return "Cada par (estado, símbolo) tiene a lo sumo un destino y no hay transiciones λ."

    @staticmethod
    def no_determinismo(automata: Automata) -> list[tuple[str, str]]:
        """Pares (estado, símbolo) que impiden que el autómata sea un AFD."""
        pares = [(t.origen, LAMBDA) for t in automata.aristas if t.es_lambda]
        pares += [(q, a) for q in automata.estados for a in automata.alfabeto
                  if len(automata.destinos(q, a)) > 1]
        return list(dict.fromkeys(pares))


class Disposicion:
    """Coordenadas para dibujar un autómata (y para el .jff de JFLAP)."""

    SEPARACION_X = 170.0
    SEPARACION_Y = 130.0

    @classmethod
    def por_niveles(cls, automata: Automata) -> dict[str, tuple[float, float]]:
        """Columnas por distancia BFS desde q₀; los inaccesibles van al final."""
        nivel = {automata.inicial: 0}
        cola = deque([automata.inicial])
        while cola:
            q = cola.popleft()
            for t in automata.aristas:
                if t.origen == q and t.destino not in nivel:
                    nivel[t.destino] = nivel[q] + 1
                    cola.append(t.destino)
        ultimo = max(nivel.values()) + 1
        columnas: dict[int, list[str]] = {}
        for q in automata.estados:
            columnas.setdefault(nivel.get(q, ultimo), []).append(q)
        alto = max(len(c) for c in columnas.values())
        posiciones = {}
        for c, estados in columnas.items():
            desfase = (alto - len(estados)) * cls.SEPARACION_Y / 2
            for i, q in enumerate(estados):
                posiciones[q] = (100.0 + c * cls.SEPARACION_X, 100.0 + desfase + i * cls.SEPARACION_Y)
        return posiciones
