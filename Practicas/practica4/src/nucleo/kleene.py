"""Las dos direcciones del teorema de Kleene (Práctica 4).

Parte I – de expresión regular a AFN-λ
    :class:`ConstruccionThompson` recorre el árbol en posorden y aplica los
    casos básicos (∅, λ, símbolo, clase) y las construcciones de unión,
    concatenación y estrella. Cada construcción queda registrada como una
    :class:`~nucleo.algoritmos.Etapa` con el autómata parcial.

Parte II – de autómata a expresión regular
    :class:`EliminacionDeEstados` trabaja sobre un :class:`AutomataGeneralizado`
    (aristas etiquetadas con expresiones) con un estado inicial ``I`` y uno
    final ``T`` nuevos, y elimina los estados originales uno a uno:
    R(p, q) ← R(p, q) + R(p, k) R(k, k)* R(k, q).

    :class:`SistemaArden` resuelve el sistema de ecuaciones Xq = Σ a·Xδ(q,a)
    (+ λ si q ∈ F) con el lema de Arden: X = AX + B ⇒ X = A*B.

:func:`comparar` decide si dos expresiones describen el mismo lenguaje
convirtiéndolas en AFD mínimos.

El módulo no depende de Flet.
"""

from __future__ import annotations

from dataclasses import dataclass, field

from .algoritmos import Cadena, Equivalencia, Etapa, HaciaMinimo, Veredicto
from .automata import AFNLambda, Arista, Automata, Clasificador, conjunto
from .errores import DefinicionInvalida
from .expresiones import (Clase, Concatenacion, Estrella, ExpresionRegular, Lambda, Nodo, Simbolo,
                          Union, Vacio, concatenar, estrella, union)


# ==========================================================================
# Parte I: construcción de Thompson
# ==========================================================================
@dataclass
class Fragmento:
    """Autómata parcial con un único estado inicial y un único estado final."""

    inicio: str
    fin: str
    estados: list[str]
    aristas: list[Arista]
    expresion: str

    def automata(self, alfabeto: list[str], nombre: str = "") -> AFNLambda:
        sigma = alfabeto or ["a"]
        estados = sorted(self.estados, key=lambda q: int(q[1:]))
        return AFNLambda(estados, sigma, self.inicio, [self.fin], self.aristas, nombre)


@dataclass
class ResultadoThompson:
    expresion: ExpresionRegular
    automata: AFNLambda
    etapas: list[Etapa]

    def hacia_minimo(self) -> Cadena:
        return HaciaMinimo(self.automata).resolver()


class ConstruccionThompson:
    """Expresión regular → AFN-λ con un estado inicial y uno final."""

    def __init__(self, expresion: ExpresionRegular | str, alfabeto: list[str] | None = None) -> None:
        self.expresion = expresion if isinstance(expresion, ExpresionRegular) else ExpresionRegular(expresion)
        self.alfabeto = sorted(set(alfabeto or []) | set(self.expresion.alfabeto))
        self._contador = 0
        self.etapas: list[Etapa] = []

    def _nuevo(self) -> str:
        nombre = f"q{self._contador}"
        self._contador += 1
        return nombre

    def resolver(self) -> ResultadoThompson:
        fragmento = self._construir(self.expresion.arbol)
        automata = fragmento.automata(self.alfabeto, "thompson")
        return ResultadoThompson(self.expresion, automata, self.etapas)

    def _registrar(self, titulo: str, explicacion: str, f: Fragmento) -> Fragmento:
        m = f.automata(self.alfabeto)
        self.etapas.append(Etapa(f"{len(self.etapas) + 1}. {titulo}", explicacion, *m.tabla(), automata=m))
        return f

    def _construir(self, nodo: Nodo) -> Fragmento:
        texto = nodo.notacion()
        if isinstance(nodo, (Vacio, Lambda, Simbolo, Clase)):
            i, f = self._nuevo(), self._nuevo()
            if isinstance(nodo, Vacio):
                aristas, caso = [], "Caso básico ∅: dos estados sin transiciones."
            elif isinstance(nodo, Lambda):
                aristas, caso = [Arista(i, "", f)], f"Caso básico λ: {i} →λ {f}."
            elif isinstance(nodo, Simbolo):
                aristas, caso = [Arista(i, nodo.caracter, f)], f"Caso básico «{nodo.caracter}»: {i} →{nodo.caracter} {f}."
            else:
                aristas = [Arista(i, c, f) for c in nodo.caracteres]
                caso = (f"Clase {texto}: abreviatura de la unión de {len(nodo.caracteres)} símbolos; "
                        f"una transición {i} → {f} por cada uno.")
            return self._registrar(f"Caso básico: {texto}", caso, Fragmento(i, f, [i, f], aristas, texto))

        if isinstance(nodo, Union):
            a, b = self._construir(nodo.izquierda), self._construir(nodo.derecha)
            i, f = self._nuevo(), self._nuevo()
            aristas = a.aristas + b.aristas + [Arista(i, "", a.inicio), Arista(i, "", b.inicio),
                                               Arista(a.fin, "", f), Arista(b.fin, "", f)]
            return self._registrar(
                f"Unión: {texto}",
                f"Nuevo inicial {i} con λ hacia {a.inicio} y {b.inicio}; nuevo final {f} "
                f"al que llegan {a.fin} y {b.fin} con λ.",
                Fragmento(i, f, [i] + a.estados + b.estados + [f], aristas, texto))

        if isinstance(nodo, Concatenacion):
            a, b = self._construir(nodo.izquierda), self._construir(nodo.derecha)
            aristas = a.aristas + b.aristas + [Arista(a.fin, "", b.inicio)]
            return self._registrar(
                f"Concatenación: {texto}",
                f"El final {a.fin} de ({a.expresion}) se une con λ al inicial {b.inicio} de ({b.expresion}).",
                Fragmento(a.inicio, b.fin, a.estados + b.estados, aristas, texto))

        if isinstance(nodo, Estrella):
            a = self._construir(nodo.hijo)
            i, f = self._nuevo(), self._nuevo()
            aristas = a.aristas + [Arista(i, "", a.inicio), Arista(i, "", f),
                                   Arista(a.fin, "", a.inicio), Arista(a.fin, "", f)]
            return self._registrar(
                f"Estrella: {texto}",
                f"Nuevo inicial {i} y nuevo final {f}; {i} →λ {f} acepta λ y {a.fin} →λ {a.inicio} "
                "permite repetir.",
                Fragmento(i, f, [i] + a.estados + [f], aristas, texto))
        raise TypeError(nodo)


# ==========================================================================
# Parte II: eliminación de estados
# ==========================================================================
class AutomataGeneralizado:
    """Autómata cuyas aristas llevan expresiones regulares.

    Sólo hay una arista por par ordenado (p, q): las transiciones paralelas se
    unen. ``I`` y ``T`` son el inicial y el final nuevos.
    """

    def __init__(self, automata: Automata, inicio: str = "I", fin: str = "T") -> None:
        while inicio in automata.estados:
            inicio += "'"
        while fin in automata.estados:
            fin += "'"
        self.inicio, self.fin = inicio, fin
        self.estados: list[str] = list(automata.estados)
        self.etiquetas: dict[tuple[str, str], Nodo] = {}
        self._agregar(inicio, automata.inicial, Lambda())
        for q in automata.orden(automata.finales):
            self._agregar(q, fin, Lambda())
        for t in automata.aristas:
            self._agregar(t.origen, t.destino, Lambda() if t.es_lambda else Simbolo(t.simbolo))

    def _agregar(self, p: str, q: str, r: Nodo) -> None:
        actual = self.etiquetas.get((p, q))
        self.etiquetas[(p, q)] = r if actual is None else union(actual, r)

    def etiqueta(self, p: str, q: str) -> Nodo:
        return self.etiquetas.get((p, q), Vacio())

    def eliminar(self, k: str) -> list[str]:
        """Quita ``k`` y devuelve la descripción de cada arista modificada."""
        lazo = self.etiqueta(k, k)
        entrantes = [p for (p, q) in self.etiquetas if q == k and p != k]
        salientes = [q for (p, q) in self.etiquetas if p == k and q != k]
        cambios = []
        for p in entrantes:
            for q in salientes:
                camino = concatenar(concatenar(self.etiqueta(p, k), estrella(lazo)), self.etiqueta(k, q))
                anterior = self.etiqueta(p, q)
                self.etiquetas[(p, q)] = union(anterior, camino)
                cambios.append(f"R({p},{q}) = {anterior} + ({self.etiqueta(p, k)})({lazo})*"
                               f"({self.etiqueta(k, q)}) = {self.etiquetas[(p, q)]}")
        self.etiquetas = {(p, q): r for (p, q), r in self.etiquetas.items() if k not in (p, q)}
        self.estados.remove(k)
        return cambios

    def filas(self) -> list[list[str]]:
        orden = [self.inicio] + self.estados + [self.fin]
        rango = {q: i for i, q in enumerate(orden)}
        pares = sorted(self.etiquetas, key=lambda par: (rango[par[0]], rango[par[1]]))
        return [[p, q, self.etiquetas[(p, q)].notacion()] for p, q in pares]


@dataclass
class ResultadoER:
    expresion: Nodo
    etapas: list[Etapa]
    orden: list[str]

    @property
    def notacion(self) -> str:
        return self.expresion.notacion()


class EliminacionDeEstados:
    """Autómata → expresión regular eliminando estados.

    ``orden`` fija qué estados se eliminan primero. Si se omite se usa una
    heurística: primero el estado que crea menos aristas nuevas
    (entrantes × salientes), con desempate por el orden de Q.
    """

    def __init__(self, automata: Automata, orden: list[str] | None = None) -> None:
        if orden is not None and sorted(orden) != sorted(automata.estados):
            raise DefinicionInvalida("El orden de eliminación debe mencionar cada estado exactamente una vez.")
        self.automata, self.orden = automata, orden

    def resolver(self) -> ResultadoER:
        g = AutomataGeneralizado(self.automata)
        etapas = [Etapa("0. Autómata generalizado",
                        f"Se agregan {g.inicio} →λ {self.automata.inicial} y λ desde cada final hacia {g.fin}; "
                        "las transiciones paralelas se unen con +.",
                        ["De", "A", "Expresión"], g.filas())]
        orden = list(self.orden) if self.orden else []
        paso = 0
        while g.estados:
            k = orden[paso] if self.orden else self._siguiente(g)
            if not self.orden:
                orden.append(k)
            paso += 1
            lazo = g.etiqueta(k, k)
            cambios = g.eliminar(k)
            explicacion = f"Se elimina {k} (lazo: {lazo.notacion()}). " + (
                "; ".join(cambios) if cambios else "No tenía caminos que lo atravesaran.")
            etapas.append(Etapa(f"{paso}. Eliminar {k}", explicacion, ["De", "A", "Expresión"], g.filas()))
        resultado = g.etiqueta(g.inicio, g.fin)
        etapas.append(Etapa("Resultado", f"La expresión es la etiqueta de {g.inicio} a {g.fin}: "
                            f"{resultado.notacion()}", [], []))
        return ResultadoER(resultado, etapas, orden)

    @staticmethod
    def _siguiente(g: AutomataGeneralizado) -> str:
        def costo(k: str) -> int:
            entra = sum(1 for (p, q) in g.etiquetas if q == k and p != k)
            sale = sum(1 for (p, q) in g.etiquetas if p == k and q != k)
            return entra * sale
        return min(g.estados, key=lambda k: (costo(k), g.estados.index(k)))


# ==========================================================================
# Lema de Arden
# ==========================================================================
@dataclass
class Ecuacion:
    """X = Σ coeficiente·Y + constante, con coeficientes a la izquierda."""

    variable: str
    terminos: dict[str, Nodo] = field(default_factory=dict)
    constante: Nodo = field(default_factory=Vacio)

    def texto(self) -> str:
        partes = [f"{c.notacion() if c.PRECEDENCIA >= 2 else '(' + c.notacion() + ')'}·X{y}"
                  for y, c in self.terminos.items()]
        if not self.constante.es_vacio() or not partes:
            partes.append(self.constante.notacion())
        return f"X{self.variable} = " + " + ".join(partes)


class SistemaArden:
    """Resuelve Xq = Σ a·Xδ(q,a) + [λ si q ∈ F] por sustitución y lema de Arden."""

    def __init__(self, automata: Automata, orden: list[str] | None = None) -> None:
        if automata.tiene_lambda:
            raise DefinicionInvalida("El sistema de Arden se plantea sobre un autómata sin transiciones λ.")
        self.automata = automata
        self.orden = orden or [q for q in reversed(automata.estados) if q != automata.inicial] + [automata.inicial]

    def resolver(self) -> ResultadoER:
        m = self.automata
        ecuaciones: dict[str, Ecuacion] = {}
        for q in m.estados:
            e = Ecuacion(q, constante=Lambda() if q in m.finales else Vacio())
            for t in m.aristas:
                if t.origen == q:
                    previo = e.terminos.get(t.destino)
                    e.terminos[t.destino] = Simbolo(t.simbolo) if previo is None else union(previo, Simbolo(t.simbolo))
            ecuaciones[q] = e
        etapas = [Etapa("Sistema de ecuaciones", "Una ecuación por estado; λ se suma en los finales.",
                        ["Ecuación"], [[e.texto()] for e in ecuaciones.values()])]
        for k in self.orden:
            e = ecuaciones.pop(k)
            pasos = []
            if k in e.terminos:
                a = e.terminos.pop(k)
                e.terminos = {y: concatenar(estrella(a), c) for y, c in e.terminos.items()}
                e.constante = concatenar(estrella(a), e.constante)
                pasos.append(f"Arden en X{k}: X{k} = ({a})*·(resto)")
            for otra in ecuaciones.values():
                if k in otra.terminos:
                    c = otra.terminos.pop(k)
                    for y, d in e.terminos.items():
                        nuevo = concatenar(c, d)
                        otra.terminos[y] = union(otra.terminos[y], nuevo) if y in otra.terminos else nuevo
                    otra.constante = union(otra.constante, concatenar(c, e.constante))
            pasos.append(f"se sustituye X{k} = {e.texto().split(' = ', 1)[1]} en las demás")
            ecuaciones_vista = list(ecuaciones.values()) or [e]
            etapas.append(Etapa(f"Despejar X{k}", "; ".join(pasos) + ".", ["Ecuación"],
                                [[x.texto()] for x in ecuaciones_vista]))
            if not ecuaciones:
                return ResultadoER(e.constante, etapas, list(self.orden))
        raise DefinicionInvalida("El orden no termina en el estado inicial.")


# ==========================================================================
# Utilidades
# ==========================================================================
def automata_de(expresion: str | ExpresionRegular, alfabeto: list[str] | None = None) -> Cadena:
    """Expresión → (Thompson) → AFN → AFD → AFD mínimo."""
    return ConstruccionThompson(expresion, alfabeto).resolver().hacia_minimo()


def comparar(primera: str | ExpresionRegular, segunda: str | ExpresionRegular) -> Veredicto:
    """Decide si dos expresiones describen el mismo lenguaje."""
    e1 = primera if isinstance(primera, ExpresionRegular) else ExpresionRegular(primera)
    e2 = segunda if isinstance(segunda, ExpresionRegular) else ExpresionRegular(segunda)
    sigma = sorted(set(e1.alfabeto) | set(e2.alfabeto))
    m1 = ConstruccionThompson(e1, sigma).resolver().automata
    m2 = ConstruccionThompson(e2, sigma).resolver().automata
    return Equivalencia(m1, m2).resolver()


def verificar_determinismo(automata: Automata) -> tuple[bool, str]:
    """(es_afd, mensaje) indicando qué estado y símbolo impiden el determinismo."""
    pares = Clasificador.no_determinismo(automata)
    if not pares:
        return True, f"Es un AFD: {Clasificador.motivo(automata)}"
    detalle = "; ".join(f"δ({q}, {a}) = {conjunto(automata.destinos(q, a), automata.estados)}"
                        for q, a in pares[:6])
    return False, f"No es determinista en {len(pares)} pares: {detalle}."
