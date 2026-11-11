"""Transformaciones de autómatas con registro de cada paso (Práctica 3).

Cada algoritmo es una clase con un único método público, ``resolver()``,
que devuelve un :class:`Resultado`: el autómata de entrada, el de salida y
la lista de :class:`Etapa` que la interfaz recorre con «Anterior/Siguiente».
Una etapa es una explicación en texto más una tabla (encabezados y filas) y,
cuando tiene sentido, el autómata parcial para dibujarlo.

* :class:`QuitarLambda`   – AFN-λ → AFN con Δ'(q,a) = λ-cl(δ(λ-cl(q), a)).
* :class:`Subconjuntos`   – AFN (o AFN-λ) → AFD, sólo subconjuntos alcanzables.
* :class:`Minimizacion`   – AFD → AFD mínimo por la tabla de pares distinguibles.
* :class:`HaciaMinimo`    – encadena las tres anteriores.
* :class:`Equivalencia`   – decide si dos autómatas son equivalentes comparando
  sus AFD mínimos salvo el nombre de los estados, y da un contraejemplo.
* :class:`Lote`           – valida muchas palabras y produce un informe.

El módulo no depende de Flet.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from collections import deque
from dataclasses import dataclass, field
from itertools import combinations
from pathlib import Path

from .automata import AFD, LAMBDA, Arista, Automata, Disposicion, conjunto
from .errores import DefinicionInvalida, ErrorTC
from .lenguajes import Informe


@dataclass
class Etapa:
    """Un paso documentado de un algoritmo."""

    titulo: str
    explicacion: str
    encabezados: list[str] = field(default_factory=list)
    filas: list[list[str]] = field(default_factory=list)
    automata: Automata | None = None

    def texto(self) -> str:
        partes = [self.titulo, self.explicacion]
        if self.encabezados:
            anchos = [max(len(str(f[i])) for f in [self.encabezados] + self.filas)
                      for i in range(len(self.encabezados))]
            for fila in [self.encabezados] + self.filas:
                partes.append("  ".join(str(c).ljust(w) for c, w in zip(fila, anchos)).rstrip())
        return "\n".join(partes)


@dataclass
class Resultado:
    """Entrada, salida y pasos intermedios de un algoritmo."""

    algoritmo: str
    entrada: Automata
    salida: Automata
    etapas: list[Etapa]
    resumen: str

    def texto(self) -> str:
        bloques = [f"{self.algoritmo}: {self.resumen}"] + [e.texto() for e in self.etapas]
        return "\n\n".join(bloques)


class Algoritmo(ABC):
    """Interfaz común: se construye con la entrada y se ejecuta con ``resolver``."""

    NOMBRE = ""

    def __init__(self, automata: Automata) -> None:
        self.automata = automata

    @abstractmethod
    def resolver(self) -> Resultado: ...


def etiqueta_de_indice(i: int) -> str:
    """0 → A, 1 → B, …, 25 → Z, 26 → A1, …"""
    letra, vuelta = chr(ord("A") + i % 26), i // 26
    return letra if vuelta == 0 else f"{letra}{vuelta}"


def nombre_de_conjunto(estados, orden) -> str:
    """Nombre de un estado del AFD de subconjuntos: ``{q0,q1}`` o ``∅``."""
    return conjunto(estados, orden).replace(", ", ",")


# ==========================================================================
# Eliminación de transiciones λ
# ==========================================================================
class QuitarLambda(Algoritmo):
    """AFN-λ → AFN equivalente sin transiciones λ.

    Δ'(q, a) = λ-cl(δ(λ-cl(q), a))   y   F' = {q : λ-cl(q) ∩ F ≠ ∅}.
    Los estados no cambian; cambian las transiciones y, quizá, F.
    """

    NOMBRE = "Eliminación de transiciones λ"

    def resolver(self) -> Resultado:
        m = self.automata
        orden = m.estados
        cierres = m.cierres()
        etapas = [Etapa(
            "1. Cerradura λ de cada estado",
            "λ-cl(q) reúne los estados a los que se llega desde q sin leer símbolos (q incluido).",
            ["q", "λ-cl(q)"], [[q, conjunto(cierres[q], orden)] for q in orden])]

        aristas: list[Arista] = []
        filas = []
        for q in orden:
            fila = [q]
            for a in m.alfabeto:
                directos = m.destinos(q, a)
                nuevos = m.transitar(cierres[q], a)
                aristas += [Arista(q, a, d) for d in m.orden(nuevos)]
                agregados = nuevos - directos
                celda = conjunto(nuevos, orden)
                if agregados:
                    celda += f"  (+{', '.join(m.orden(agregados))})"
                fila.append(celda)
            filas.append(fila)
        etapas.append(Etapa(
            "2. Nuevas transiciones Δ'(q, a) = λ-cl(δ(λ-cl(q), a))",
            "Entre paréntesis, los destinos que no estaban en δ(q, a) y que se añaden.",
            ["q"] + [f"Δ'(q, {a})" for a in m.alfabeto], filas))

        finales = [q for q in orden if m.es_aceptacion(cierres[q])]
        nuevos_finales = [q for q in finales if q not in m.finales]
        motivo = [[q, conjunto(cierres[q] & m.finales, orden),
                   "nuevo" if q in nuevos_finales else "ya era final"] for q in finales]
        etapas.append(Etapa(
            "3. Estados de aceptación F' = {q : λ-cl(q) ∩ F ≠ ∅}",
            ("Pasan a ser de aceptación: " + ", ".join(nuevos_finales) + ".") if nuevos_finales
            else "Ningún estado nuevo pasa a ser de aceptación.",
            ["q", "λ-cl(q) ∩ F", ""], motivo))

        salida = Automata.crear(orden, m.alfabeto, m.inicial, finales, aristas,
                                f"{m.nombre}-sin-lambda" if m.nombre else "sin-lambda", m.posiciones)
        etapas.append(Etapa("4. AFN resultante", f"Resultado: {salida.tipo} con {len(salida.aristas)} "
                            "transiciones y sin transiciones λ.", *salida.tabla(), automata=salida))
        quitadas = sum(1 for t in m.aristas if t.es_lambda)
        return Resultado(self.NOMBRE, m, salida, etapas,
                         f"se quitaron {quitadas} transiciones λ; |F| pasó de {len(m.finales)} a {len(finales)}.")


# ==========================================================================
# Construcción de subconjuntos
# ==========================================================================
class Subconjuntos(Algoritmo):
    """AFN → AFD por la construcción de subconjuntos (Rabin y Scott, 1959).

    Sólo se generan los subconjuntos alcanzables desde λ-cl({q₀}). Si
    ``incluir_vacio`` es falso, el subconjunto ∅ no se agrega y el AFD queda
    parcial (como en JFLAP).
    """

    NOMBRE = "Construcción de subconjuntos"

    def __init__(self, automata: Automata, incluir_vacio: bool = False, con_letras: bool = True) -> None:
        super().__init__(automata)
        self.incluir_vacio = incluir_vacio
        self.con_letras = con_letras

    def resolver(self) -> Resultado:
        m = self.automata
        orden = m.estados
        inicio = m.cierre({m.inicial})
        descubiertos = [inicio]

        def nombre(s: frozenset[str]) -> str:
            if not self.con_letras:
                return nombre_de_conjunto(s, orden)
            return etiqueta_de_indice(descubiertos.index(s))

        def con_contenido(s: frozenset[str]) -> str:
            texto = nombre_de_conjunto(s, orden)
            return f"{nombre(s)} = {texto}" if self.con_letras else texto

        cola = deque([inicio])
        filas: list[list[str]] = []
        etapas: list[Etapa] = []
        aristas: list[Arista] = []
        encabezados = ["", "Subconjunto"] + list(m.alfabeto)
        while cola:
            actual = cola.popleft()
            fila = ["→" if actual == inicio else "", con_contenido(actual)]
            aparecen = []
            for a in m.alfabeto:
                destino = m.transitar(actual, a)
                if not destino and not self.incluir_vacio:
                    fila.append("—")
                    continue
                if destino not in descubiertos:
                    descubiertos.append(destino)
                    cola.append(destino)
                    aparecen.append(con_contenido(destino))
                aristas.append(Arista(nombre(actual), a, nombre(destino)))
                fila.append(nombre(destino))
            if m.es_aceptacion(actual):
                fila[0] += "*"
            filas.append(fila)
            explicacion = f"Se procesa {con_contenido(actual)}: para cada símbolo a se calcula λ-cl(δ(S, a))."
            explicacion += (f" Subconjuntos nuevos: {', '.join(aparecen)}." if aparecen
                            else " No aparecen subconjuntos nuevos.")
            etapas.append(Etapa(f"Fila {len(filas)}: {con_contenido(actual)}", explicacion,
                                encabezados, [list(f) for f in filas]))

        finales = [nombre(s) for s in descubiertos if m.es_aceptacion(s)]
        etapas.append(Etapa(
            "Subconjuntos de aceptación",
            "Un subconjunto es de aceptación si contiene algún estado de F = "
            f"{conjunto(m.finales, orden)}.",
            ["Subconjunto", "Estados de F que contiene"],
            [[con_contenido(s), conjunto(s & m.finales, orden)] for s in descubiertos if m.es_aceptacion(s)]))
        estados = [nombre(s) for s in descubiertos]
        salida = AFD(estados, m.alfabeto, nombre(inicio), finales, aristas,
                     f"{m.nombre}-afd" if m.nombre else "afd")
        etapas.append(Etapa("AFD resultante", f"{len(estados)} estados de 2^{len(orden)} = "
                            f"{2 ** len(orden)} posibles.", *salida.tabla(), automata=salida))
        return Resultado(self.NOMBRE, m, salida, etapas,
                         f"{len(orden)} estados → {len(estados)} subconjuntos alcanzables "
                         f"(cota 2^{len(orden)} = {2 ** len(orden)}).")


# ==========================================================================
# Minimización por la tabla de pares distinguibles
# ==========================================================================
class Minimizacion(Algoritmo):
    """AFD → AFD mínimo.

    1. Se eliminan los estados inaccesibles.
    2. Si δ es parcial se agrega un sumidero para que la tabla esté definida.
    3. Ronda 0: se marcan los pares {p, q} con exactamente un estado final.
       Ronda k: se marca {p, q} si para algún símbolo a el par
       {δ(p, a), δ(q, a)} quedó marcado en una ronda anterior.
    4. Los pares sin marcar son equivalentes; sus clases son los estados del
       AFD mínimo. Si el sumidero se agregó en el paso 2, su clase se retira al
       final para que el resultado sea comparable con la entrada.
    """

    NOMBRE = "Minimización (tabla de pares distinguibles)"

    def __init__(self, automata: Automata) -> None:
        if not isinstance(automata, AFD):
            raise DefinicionInvalida("La minimización requiere un AFD; convierta primero el autómata.")
        super().__init__(automata)

    def resolver(self) -> Resultado:
        original = self.automata
        etapas: list[Etapa] = []

        accesibles = original.alcanzables()
        inaccesibles = [q for q in original.estados if q not in accesibles]
        etapas.append(Etapa(
            "1. Estados inaccesibles",
            (f"Se eliminan {', '.join(inaccesibles)}: no se alcanzan desde {original.inicial}."
             if inaccesibles else "Todos los estados son accesibles desde el inicial."),
            ["Accesibles (orden BFS)"], [[", ".join(accesibles)]]))
        m = AFD([q for q in original.estados if q in accesibles], original.alfabeto, original.inicial,
                [q for q in original.finales if q in accesibles],
                [t for t in original.aristas if t.origen in accesibles], original.nombre)

        sumidero = None
        if not m.es_completo:
            completo = m.completar()
            sumidero = completo.estados[-1]
            etapas.append(Etapa(
                "2. Completar δ",
                f"δ es parcial en {len(m.faltantes())} pares; se agrega el sumidero {sumidero} "
                "para que todo par tenga sucesor.", *completo.tabla()))
            m = completo

        estados = list(m.estados)
        marca: dict[frozenset[str], int] = {}
        motivo: dict[frozenset[str], str] = {}
        for p, q in combinations(estados, 2):
            if (p in m.finales) != (q in m.finales):
                marca[frozenset((p, q))] = 0
                motivo[frozenset((p, q))] = "uno es final y el otro no"
        etapas.append(self._etapa_tabla(estados, marca, 0, "3. Ronda 0",
                                        "Se marcan los pares con exactamente un estado de aceptación."))
        ronda = 0
        while True:
            ronda += 1
            nuevas = {}
            for p, q in combinations(estados, 2):
                par = frozenset((p, q))
                if par in marca:
                    continue
                for a in m.alfabeto:
                    r, s = m.siguiente(p, a), m.siguiente(q, a)
                    if r != s and frozenset((r, s)) in marca:
                        nuevas[par] = f"con «{a}» van a {r} y {s}, ya distinguibles"
                        break
            if not nuevas:
                etapas.append(self._etapa_tabla(estados, marca, ronda, f"Ronda {ronda}",
                                                "No se marca ningún par nuevo: la tabla se estabilizó."))
                break
            for par, razon in nuevas.items():
                marca[par] = ronda
                motivo[par] = razon
            detalle = "; ".join(f"{{{', '.join(m.orden(par))}}}: {razon}" for par, razon in nuevas.items())
            etapas.append(self._etapa_tabla(estados, marca, ronda, f"Ronda {ronda}",
                                            f"Se marcan {len(nuevas)} pares. {detalle}."))

        clases = self._clases(estados, marca)
        nombre_clase = {}
        for clase in clases:
            texto = clase[0] if len(clase) == 1 else "{" + ",".join(clase) + "}"
            for q in clase:
                nombre_clase[q] = texto
        muertos = set()
        if sumidero is not None and nombre_clase[sumidero] != nombre_clase[m.inicial]:
            muertos = {nombre_clase[sumidero]}
        estados_min = [nombre_clase[c[0]] for c in clases if nombre_clase[c[0]] not in muertos]
        aristas = [Arista(nombre_clase[c[0]], a, nombre_clase[m.siguiente(c[0], a)])
                   for c in clases for a in m.alfabeto
                   if nombre_clase[c[0]] not in muertos and nombre_clase[m.siguiente(c[0], a)] not in muertos]
        finales = [nombre_clase[c[0]] for c in clases if c[0] in m.finales]
        salida = AFD(estados_min, m.alfabeto, nombre_clase[m.inicial], finales, aristas,
                     f"{original.nombre}-min" if original.nombre else "minimo")
        nota = (f" La clase del sumidero {sumidero} se retira porque no estaba en la entrada."
                if muertos else "")
        etapas.append(Etapa(
            "4. Clases de equivalencia",
            "Los pares que nunca se marcaron son indistinguibles y se fusionan." + nota,
            ["Clase", "Estados", "Final"],
            [[nombre_clase[c[0]], ", ".join(c), "sí" if c[0] in m.finales else "no"] for c in clases]))
        etapas.append(Etapa("5. AFD mínimo", f"{len(original.estados)} → {len(estados_min)} estados.",
                            *salida.tabla(), automata=salida))
        return Resultado(self.NOMBRE, original, salida, etapas,
                         f"{len(original.estados)} estados → {len(estados_min)} en {ronda} rondas.")

    @staticmethod
    def _clases(estados: list[str], marca: dict[frozenset[str], int]) -> list[list[str]]:
        clases: list[list[str]] = []
        asignado: set[str] = set()
        for p in estados:
            if p in asignado:
                continue
            clase = [p] + [q for q in estados if q != p and q not in asignado and frozenset((p, q)) not in marca]
            asignado.update(clase)
            clases.append(clase)
        return clases

    @staticmethod
    def _etapa_tabla(estados, marca, ronda, titulo, explicacion) -> Etapa:
        """Tabla triangular: × k indica el par marcado en la ronda k."""
        encabezados = [""] + estados[:-1]
        filas = []
        for i, p in enumerate(estados[1:], start=1):
            fila = [p]
            for j, q in enumerate(estados[:-1]):
                if j >= i:
                    fila.append("")
                else:
                    k = marca.get(frozenset((p, q)))
                    fila.append("·" if k is None else f"×{k}")
            filas.append(fila)
        return Etapa(titulo, explicacion, encabezados, filas)


# ==========================================================================
# Canalización completa
# ==========================================================================
@dataclass
class Cadena:
    """Resultados encadenados AFN-λ → AFN → AFD → AFD mínimo."""

    sin_lambda: Resultado | None
    determinista: Resultado | None
    minimo: Resultado

    @property
    def resultados(self) -> list[Resultado]:
        return [r for r in (self.sin_lambda, self.determinista, self.minimo) if r is not None]

    @property
    def afd_minimo(self) -> AFD:
        return self.minimo.salida  # type: ignore[return-value]


class HaciaMinimo:
    """Aplica sólo los pasos necesarios para llegar al AFD mínimo."""

    def __init__(self, automata: Automata) -> None:
        self.automata = automata

    def resolver(self) -> Cadena:
        actual = self.automata
        sin_lambda = determinista = None
        if actual.tiene_lambda:
            sin_lambda = QuitarLambda(actual).resolver()
            actual = sin_lambda.salida
        if not isinstance(actual, AFD):
            determinista = Subconjuntos(actual).resolver()
            actual = determinista.salida
        minimo = Minimizacion(actual).resolver()
        return Cadena(sin_lambda, determinista, minimo)


# ==========================================================================
# Equivalencia
# ==========================================================================
@dataclass
class Veredicto:
    equivalentes: bool
    minimo_1: AFD
    minimo_2: AFD
    correspondencia: dict[str, str]
    contraejemplo: str | None
    etapas: list[Etapa]

    @property
    def explicacion(self) -> str:
        if self.equivalentes:
            return ("Equivalentes: sus AFD mínimos coinciden salvo el nombre de los estados "
                    f"({len(self.minimo_1.estados)} estados).")
        w = self.contraejemplo if self.contraejemplo else LAMBDA
        return f"No equivalentes: la palabra «{w}» es aceptada por uno y rechazada por el otro."


class Equivalencia:
    """Compara dos autómatas por medio de sus AFD mínimos completos."""

    def __init__(self, primero: Automata, segundo: Automata) -> None:
        sigma = list(primero.alfabeto) + [a for a in segundo.alfabeto if a not in primero.alfabeto]
        self.primero = primero.con_alfabeto(sigma)
        self.segundo = segundo.con_alfabeto(sigma)

    def resolver(self) -> Veredicto:
        m1 = HaciaMinimo(self.primero).resolver().afd_minimo.completar()
        m2 = HaciaMinimo(self.segundo).resolver().afd_minimo.completar()
        etapas = [Etapa("AFD mínimo del primero", f"{len(m1.estados)} estados.", *m1.tabla()),
                  Etapa("AFD mínimo del segundo", f"{len(m2.estados)} estados.", *m2.tabla())]
        correspondencia = self._isomorfismo(m1, m2)
        contraejemplo = None if correspondencia else self._contraejemplo(m1, m2)
        if correspondencia:
            etapas.append(Etapa("Correspondencia de estados",
                                "Recorriendo ambos en anchura con los mismos símbolos se llega a pares "
                                "con el mismo carácter de aceptación.",
                                ["Primero", "Segundo"], [[p, q] for p, q in correspondencia.items()]))
        else:
            etapas.append(Etapa("Contraejemplo", "Palabra más corta en la que difieren: «"
                                f"{contraejemplo or LAMBDA}».", [], []))
        return Veredicto(bool(correspondencia), m1, m2, correspondencia or {}, contraejemplo, etapas)

    @staticmethod
    def _isomorfismo(m1: AFD, m2: AFD) -> dict[str, str] | None:
        if len(m1.estados) != len(m2.estados):
            return None
        mapa = {m1.inicial: m2.inicial}
        cola = deque([m1.inicial])
        while cola:
            p = cola.popleft()
            q = mapa[p]
            if (p in m1.finales) != (q in m2.finales):
                return None
            for a in m1.alfabeto:
                r, s = m1.siguiente(p, a), m2.siguiente(q, a)
                if r in mapa:
                    if mapa[r] != s:
                        return None
                else:
                    if s in mapa.values():
                        return None
                    mapa[r] = s
                    cola.append(r)
        return mapa

    @staticmethod
    def _contraejemplo(m1: AFD, m2: AFD) -> str | None:
        inicio = (m1.inicial, m2.inicial)
        previo: dict[tuple[str, str], tuple[tuple[str, str], str] | None] = {inicio: None}
        cola = deque([inicio])
        while cola:
            par = cola.popleft()
            p, q = par
            if (p in m1.finales) != (q in m2.finales):
                letras = []
                while previo[par] is not None:
                    par, a = previo[par]
                    letras.append(a)
                return "".join(reversed(letras))
            for a in m1.alfabeto:
                sig = (m1.siguiente(p, a), m2.siguiente(q, a))
                if sig not in previo:
                    previo[sig] = (par, a)
                    cola.append(sig)
        return None


# ==========================================================================
# Validación por lotes
# ==========================================================================
@dataclass
class Fila:
    numero: int
    palabra: str
    veredicto: str
    detalle: str


class Lote:
    """Valida un texto con una palabra por línea.

    Las líneas en blanco y las que empiezan con ``#`` se ignoran; «λ» o «ε»
    representan la palabra vacía.
    """

    def __init__(self, automata: Automata) -> None:
        self.automata = automata

    def validar_texto(self, texto: str) -> list[Fila]:
        filas = []
        for linea in texto.splitlines():
            bruta = linea.strip()
            if not bruta or bruta.startswith("#"):
                continue
            palabra = "" if bruta in (LAMBDA, "ε") else bruta
            try:
                recorrido = self.automata.recorrer(palabra)
                filas.append(Fila(len(filas) + 1, palabra or LAMBDA,
                                  "ACEPTADA" if recorrido.aceptada else "RECHAZADA",
                                  conjunto(recorrido.activos, self.automata.estados)))
            except ErrorTC as exc:
                filas.append(Fila(len(filas) + 1, palabra or LAMBDA, "ERROR", str(exc)))
        return filas

    def validar_archivo(self, ruta: str | Path) -> list[Fila]:
        ruta = Path(ruta)
        if not ruta.is_file():
            raise DefinicionInvalida(f"No existe el archivo {ruta}.")
        return self.validar_texto(ruta.read_text(encoding="utf-8"))

    def informe(self, filas: list[Fila]) -> Informe:
        aceptadas = sum(f.veredicto == "ACEPTADA" for f in filas)
        return Informe(
            f"Validación por lotes – {self.automata.nombre or 'autómata'}",
            [f"{f.numero:>4}  {f.palabra:<30} {f.veredicto:<10} {f.detalle}" for f in filas],
            {"Tipo": self.automata.tipo, "Aceptadas": str(aceptadas),
             "Rechazadas": str(sum(f.veredicto == "RECHAZADA" for f in filas)),
             "Errores": str(sum(f.veredicto == "ERROR" for f in filas))})


def redisponer(automata: Automata) -> Automata:
    """Recalcula las coordenadas del autómata (tras renombrar o transformar)."""
    automata.posiciones = Disposicion.por_niveles(automata)
    return automata
