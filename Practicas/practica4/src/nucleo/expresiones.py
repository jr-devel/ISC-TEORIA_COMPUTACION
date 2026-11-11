"""Expresiones regulares en la notación del curso (Práctica 4).

Notación aceptada
-----------------
=============  ==============================================
``a``          cualquier carácter que no sea un operador
``\\x``         el carácter ``x`` literal, aunque sea operador
``λ`` ``ε``    la palabra vacía
``∅`` ``Ø``    el lenguaje vacío
``r + s``      unión (precedencia más baja)
``rs``         concatenación (yuxtaposición)
``r*``         cerradura de Kleene (precedencia más alta)
``( r )``      agrupación
``[D]``        clase de símbolos declarada en :class:`Clases`
=============  ==============================================

Los espacios se ignoran. El análisis usa el algoritmo *shunting-yard*:

1. :class:`Lexico` convierte el texto en fichas con su posición.
2. Se inserta el operador de concatenación implícito (``·``) entre fichas
   adyacentes que lo requieren, y se detectan los errores de forma.
3. Las fichas se pasan a notación posfija respetando la precedencia
   ``*`` > ``·`` > ``+`` y los paréntesis.
4. La posfija se reduce con una pila a un árbol de :class:`Nodo`.

Cualquier error lanza :class:`ExpresionInvalida` con la posición del
carácter que lo provocó.

El módulo no depende de Flet.
"""

from __future__ import annotations

import random
import re
from abc import ABC, abstractmethod
from dataclasses import dataclass

from .errores import ExpresionInvalida

LAMBDA, VACIO = "λ", "∅"
_LAMBDAS, _VACIOS = {"λ", "ε"}, {"∅", "Ø"}
OPERADORES = set("+*()[]\\") | _LAMBDAS | _VACIOS


# ==========================================================================
# Clases de símbolos
# ==========================================================================
class Clases:
    """Abreviaturas para alfabetos grandes, por ejemplo ``[D] = 0 + 1 + … + 9``."""

    _REGISTRO: dict[str, tuple[str, str]] = {
        "D": ("0123456789", "dígitos 0–9"),
        "m": ("abcdefghijklmnopqrstuvwxyz", "minúsculas a–z (sin ñ)"),
        "M": ("ABCDEFGHIJKLMNOPQRSTUVWXYZ", "mayúsculas A–Z"),
        "L": ("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", "letras a–z y A–Z"),
        "X": ("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", "letras y dígitos"),
    }

    @classmethod
    def caracteres(cls, nombre: str) -> str | None:
        entrada = cls._REGISTRO.get(nombre)
        return entrada[0] if entrada else None

    @classmethod
    def registrar(cls, nombre: str, caracteres: str, descripcion: str = "") -> None:
        if not nombre or not caracteres:
            raise ValueError("Una clase necesita nombre y caracteres.")
        cls._REGISTRO[nombre] = ("".join(dict.fromkeys(caracteres)), descripcion or nombre)

    @classmethod
    def catalogo(cls) -> list[tuple[str, str]]:
        return [(f"[{n}]", d) for n, (_, d) in cls._REGISTRO.items()]


def clase_python(caracteres) -> str:
    """Conjunto de caracteres → clase de ``re`` con rangos: ``[0-9a-z_]``."""
    orden = sorted(set(caracteres))
    if len(orden) == 1:
        return re.escape(orden[0])
    partes, i = [], 0
    while i < len(orden):
        j = i
        while j + 1 < len(orden) and ord(orden[j + 1]) == ord(orden[j]) + 1 and orden[j + 1].isalnum() \
                and orden[i].isalnum():
            j += 1
        if j - i >= 2:
            partes.append(f"{orden[i]}-{orden[j]}")
        else:
            partes.extend(("\\" + c) if c in "]\\^-[" else c for c in orden[i:j + 1])
        i = j + 1
    return "[" + "".join(partes) + "]"


def _caracteres(nodo: "Nodo") -> set[str] | None:
    """Si el nodo es una unión de símbolos sueltos, devuelve ese conjunto."""
    if isinstance(nodo, (Simbolo, Clase)):
        return nodo.simbolos()
    if isinstance(nodo, Union):
        izq, der = _caracteres(nodo.izquierda), _caracteres(nodo.derecha)
        if izq is not None and der is not None:
            return izq | der
    return None


# ==========================================================================
# Árbol sintáctico
# ==========================================================================
class Nodo(ABC):
    """Nodo del árbol de una expresión regular."""

    PRECEDENCIA = 4          # 1 unión, 2 concatenación, 3 estrella, 4 átomo

    @abstractmethod
    def notacion(self) -> str:
        """Texto en la notación del curso con los paréntesis mínimos."""

    @abstractmethod
    def python(self) -> str:
        """Patrón equivalente para el módulo ``re`` de Python."""

    @abstractmethod
    def simbolos(self) -> set[str]: ...

    @abstractmethod
    def anulable(self) -> bool:
        """``True`` si λ pertenece al lenguaje."""

    @abstractmethod
    def es_vacio(self) -> bool:
        """``True`` si el lenguaje es ∅."""

    def hijos(self) -> tuple["Nodo", ...]:
        return ()

    def _envolver(self, hijo: "Nodo", minimo: int) -> str:
        texto = hijo.notacion()
        return f"({texto})" if hijo.PRECEDENCIA < minimo else texto

    def __str__(self) -> str:
        return self.notacion()

    def __eq__(self, otro: object) -> bool:
        return type(self) is type(otro) and self.notacion() == otro.notacion()  # type: ignore[union-attr]

    def __hash__(self) -> int:
        return hash((type(self).__name__, self.notacion()))

    def tamano(self) -> int:
        return 1 + sum(h.tamano() for h in self.hijos())


class Vacio(Nodo):
    def notacion(self) -> str: return VACIO
    def python(self) -> str: return "(?!)"
    def simbolos(self) -> set[str]: return set()
    def anulable(self) -> bool: return False
    def es_vacio(self) -> bool: return True


class Lambda(Nodo):
    def notacion(self) -> str: return LAMBDA
    def python(self) -> str: return ""
    def simbolos(self) -> set[str]: return set()
    def anulable(self) -> bool: return True
    def es_vacio(self) -> bool: return False


class Simbolo(Nodo):
    def __init__(self, caracter: str) -> None:
        self.caracter = caracter

    def notacion(self) -> str:
        return "\\" + self.caracter if self.caracter in OPERADORES else self.caracter

    def python(self) -> str: return re.escape(self.caracter)
    def simbolos(self) -> set[str]: return {self.caracter}
    def anulable(self) -> bool: return False
    def es_vacio(self) -> bool: return False


class Clase(Nodo):
    """Abreviatura de la unión de varios símbolos."""

    def __init__(self, nombre: str, caracteres: str) -> None:
        self.nombre, self.caracteres = nombre, caracteres

    def notacion(self) -> str: return f"[{self.nombre}]"

    def python(self) -> str:
        return clase_python(self.caracteres)

    def simbolos(self) -> set[str]: return set(self.caracteres)
    def anulable(self) -> bool: return False
    def es_vacio(self) -> bool: return False


class Union(Nodo):
    PRECEDENCIA = 1

    def __init__(self, izquierda: Nodo, derecha: Nodo) -> None:
        self.izquierda, self.derecha = izquierda, derecha

    def hijos(self): return (self.izquierda, self.derecha)
    def notacion(self) -> str: return f"{self._envolver(self.izquierda, 1)} + {self._envolver(self.derecha, 1)}"
    def python(self) -> str:
        conjunto = _caracteres(self)
        if conjunto is not None:
            return clase_python(conjunto)
        return f"(?:{self.izquierda.python()}|{self.derecha.python()})"
    def simbolos(self) -> set[str]: return self.izquierda.simbolos() | self.derecha.simbolos()
    def anulable(self) -> bool: return self.izquierda.anulable() or self.derecha.anulable()
    def es_vacio(self) -> bool: return self.izquierda.es_vacio() and self.derecha.es_vacio()


class Concatenacion(Nodo):
    PRECEDENCIA = 2

    def __init__(self, izquierda: Nodo, derecha: Nodo) -> None:
        self.izquierda, self.derecha = izquierda, derecha

    def hijos(self): return (self.izquierda, self.derecha)
    def notacion(self) -> str: return self._envolver(self.izquierda, 2) + self._envolver(self.derecha, 2)
    def python(self) -> str: return self.izquierda.python() + self.derecha.python()
    def simbolos(self) -> set[str]: return self.izquierda.simbolos() | self.derecha.simbolos()
    def anulable(self) -> bool: return self.izquierda.anulable() and self.derecha.anulable()
    def es_vacio(self) -> bool: return self.izquierda.es_vacio() or self.derecha.es_vacio()


class Estrella(Nodo):
    PRECEDENCIA = 3

    def __init__(self, hijo: Nodo) -> None:
        self.hijo = hijo

    def hijos(self): return (self.hijo,)
    def notacion(self) -> str: return self._envolver(self.hijo, 4) + "*"
    def python(self) -> str:
        interno = self.hijo.python()
        simple = _caracteres(self.hijo) is not None or (isinstance(self.hijo, Simbolo))
        return f"{interno}*" if simple else f"(?:{interno})*"
    def simbolos(self) -> set[str]: return self.hijo.simbolos()
    def anulable(self) -> bool: return True
    def es_vacio(self) -> bool: return False


# --------------------------------------------------------------------------
# Constructores con simplificación (los usa la Parte II del teorema de Kleene)
# --------------------------------------------------------------------------
def _terminos(nodo: Nodo) -> list[Nodo]:
    return _terminos(nodo.izquierda) + _terminos(nodo.derecha) if isinstance(nodo, Union) else [nodo]


def union(r: Nodo, s: Nodo) -> Nodo:
    """r + s con ∅ + r = r, r + r = r y λ + r* = r*."""
    if r.es_vacio():
        return s
    if s.es_vacio():
        return r
    terminos = _terminos(r)
    for t in _terminos(s):
        if t not in terminos:
            terminos.append(t)
    if any(isinstance(t, Lambda) for t in terminos) and any(isinstance(t, Estrella) or
                                                          (t.anulable() and not isinstance(t, Lambda))
                                                          for t in terminos):
        terminos = [t for t in terminos if not isinstance(t, Lambda)]
    resultado = terminos[0]
    for t in terminos[1:]:
        resultado = Union(resultado, t)
    return resultado


def concatenar(r: Nodo, s: Nodo) -> Nodo:
    """rs con ∅r = r∅ = ∅ y λr = rλ = r."""
    if r.es_vacio() or s.es_vacio():
        return Vacio()
    if isinstance(r, Lambda):
        return s
    if isinstance(s, Lambda):
        return r
    return Concatenacion(r, s)


def estrella(r: Nodo) -> Nodo:
    """r* con ∅* = λ* = λ, (r*)* = r* y (λ + r)* = r*."""
    if r.es_vacio() or isinstance(r, Lambda):
        return Lambda()
    if isinstance(r, Estrella):
        return r
    if isinstance(r, Union):
        sin_lambda = [t for t in _terminos(r) if not isinstance(t, Lambda)]
        if len(sin_lambda) < len(_terminos(r)):
            base = sin_lambda[0]
            for t in sin_lambda[1:]:
                base = Union(base, t)
            return estrella(base)
    return Estrella(r)


# ==========================================================================
# Análisis léxico
# ==========================================================================
@dataclass(frozen=True)
class Ficha:
    clase: str          # SIMBOLO, CLASE, LAMBDA, VACIO, UNION, ESTRELLA, ABRE, CIERRA, CONCAT
    valor: str
    posicion: int

    @property
    def es_operando(self) -> bool:
        return self.clase in ("SIMBOLO", "CLASE", "LAMBDA", "VACIO")


class Lexico:
    """Convierte el texto en fichas y conserva la posición de cada una."""

    def __init__(self, texto: str) -> None:
        self.texto = texto

    def fichas(self) -> list[Ficha]:
        t, i, salida = self.texto, 0, []
        while i < len(t):
            c = t[i]
            if c.isspace():
                i += 1
                continue
            if c == "\\":
                if i + 1 >= len(t):
                    raise ExpresionInvalida("La barra invertida debe ir seguida del carácter que escapa", i)
                salida.append(Ficha("SIMBOLO", t[i + 1], i))
                i += 2
                continue
            if c == "[":
                fin = t.find("]", i)
                if fin < 0:
                    raise ExpresionInvalida("Falta el «]» que cierra la clase de símbolos", i)
                nombre = t[i + 1:fin].strip()
                caracteres = Clases.caracteres(nombre)
                if caracteres is None:
                    raise ExpresionInvalida(f"La clase «[{nombre}]» no está declarada", i)
                salida.append(Ficha("CLASE", nombre, i))
                i = fin + 1
                continue
            if c == "]":
                raise ExpresionInvalida("«]» sin un «[» que lo abra", i)
            clase = {"+": "UNION", "*": "ESTRELLA", "(": "ABRE", ")": "CIERRA"}.get(c)
            if clase is None:
                clase = "LAMBDA" if c in _LAMBDAS else "VACIO" if c in _VACIOS else "SIMBOLO"
            salida.append(Ficha(clase, c, i))
            i += 1
        return salida


# ==========================================================================
# Análisis sintáctico (shunting-yard)
# ==========================================================================
class Analizador:
    """Texto → árbol sintáctico, con mensajes de error que indican la posición."""

    PRECEDENCIA = {"UNION": 1, "CONCAT": 2}

    def __init__(self, texto: str) -> None:
        self.texto = texto

    def analizar(self) -> Nodo:
        fichas = Lexico(self.texto).fichas()
        if not fichas:
            raise ExpresionInvalida("La expresión está vacía; use λ para la palabra vacía", 0)
        fichas = self._con_concatenacion(fichas)
        return self._reducir(self._posfija(fichas))

    # -- paso 2: concatenación implícita y errores de forma ------------------
    def _con_concatenacion(self, fichas: list[Ficha]) -> list[Ficha]:
        salida: list[Ficha] = []
        previa: Ficha | None = None
        for f in fichas:
            if f.clase == "UNION" and (previa is None or previa.clase in ("UNION", "ABRE")):
                raise ExpresionInvalida("Al «+» le falta el operando izquierdo", f.posicion)
            if f.clase == "ESTRELLA" and (previa is None or previa.clase in ("UNION", "ABRE")):
                raise ExpresionInvalida("La «*» no se aplica a nada", f.posicion)
            if f.clase == "CIERRA" and previa is not None and previa.clase == "UNION":
                raise ExpresionInvalida("Al «+» le falta el operando derecho", previa.posicion)
            if f.clase == "CIERRA" and previa is not None and previa.clase == "ABRE":
                raise ExpresionInvalida("Paréntesis vacíos; use λ para la palabra vacía", previa.posicion)
            empieza = f.es_operando or f.clase == "ABRE"
            termina = previa is not None and (previa.es_operando or previa.clase in ("CIERRA", "ESTRELLA"))
            if empieza and termina:
                salida.append(Ficha("CONCAT", "·", f.posicion))
            salida.append(f)
            previa = f
        if previa is not None and previa.clase == "UNION":
            raise ExpresionInvalida("Al «+» le falta el operando derecho", previa.posicion)
        return salida

    # -- paso 3: posfija -------------------------------------------------------
    def _posfija(self, fichas: list[Ficha]) -> list[Ficha]:
        salida: list[Ficha] = []
        pila: list[Ficha] = []
        for f in fichas:
            if f.es_operando or f.clase == "ESTRELLA":
                salida.append(f)          # la estrella es posfija y de máxima precedencia
            elif f.clase in self.PRECEDENCIA:
                while pila and pila[-1].clase in self.PRECEDENCIA and \
                        self.PRECEDENCIA[pila[-1].clase] >= self.PRECEDENCIA[f.clase]:
                    salida.append(pila.pop())
                pila.append(f)
            elif f.clase == "ABRE":
                pila.append(f)
            elif f.clase == "CIERRA":
                while pila and pila[-1].clase != "ABRE":
                    salida.append(pila.pop())
                if not pila:
                    raise ExpresionInvalida("«)» sin un «(» que lo abra", f.posicion)
                pila.pop()
        while pila:
            f = pila.pop()
            if f.clase == "ABRE":
                raise ExpresionInvalida("Falta el «)» que cierra este paréntesis", f.posicion)
            salida.append(f)
        return salida

    # -- paso 4: árbol -------------------------------------------------------
    @staticmethod
    def _reducir(posfija: list[Ficha]) -> Nodo:
        pila: list[Nodo] = []
        for f in posfija:
            if f.clase == "SIMBOLO":
                pila.append(Simbolo(f.valor))
            elif f.clase == "CLASE":
                pila.append(Clase(f.valor, Clases.caracteres(f.valor) or ""))
            elif f.clase == "LAMBDA":
                pila.append(Lambda())
            elif f.clase == "VACIO":
                pila.append(Vacio())
            elif f.clase == "ESTRELLA":
                pila.append(Estrella(pila.pop()))
            else:
                if len(pila) < 2:
                    raise ExpresionInvalida("Falta un operando", f.posicion)
                derecha, izquierda = pila.pop(), pila.pop()
                pila.append(Union(izquierda, derecha) if f.clase == "UNION" else Concatenacion(izquierda, derecha))
        if len(pila) != 1:
            raise ExpresionInvalida("La expresión no está bien formada", 0)
        return pila[0]


# ==========================================================================
# Fachada
# ==========================================================================
class ExpresionRegular:
    """Expresión ya analizada, con sus traducciones y su muestreo."""

    def __init__(self, texto: str) -> None:
        self.texto = texto
        self.arbol = Analizador(texto).analizar()

    @property
    def notacion(self) -> str:
        return self.arbol.notacion()

    @property
    def python(self) -> str:
        return self.arbol.python()

    @property
    def alfabeto(self) -> list[str]:
        return sorted(self.arbol.simbolos())

    def coincide(self, palabra: str) -> bool:
        """Referencia independiente: ``re.fullmatch`` con el patrón traducido."""
        return re.fullmatch(self.python, palabra) is not None

    def muestra(self, generador: random.Random, profundidad: int = 3) -> str:
        """Palabra al azar del lenguaje (o ``None`` si el lenguaje es vacío)."""
        return Muestreo(generador, profundidad).palabra(self.arbol)

    def __str__(self) -> str:
        return self.notacion


class Muestreo:
    """Genera palabras de L(r) recorriendo el árbol al azar."""

    def __init__(self, generador: random.Random, repeticiones: int = 3) -> None:
        self.azar, self.repeticiones = generador, repeticiones

    def palabra(self, nodo: Nodo) -> str:
        if isinstance(nodo, (Lambda, Vacio)):
            return ""
        if isinstance(nodo, Simbolo):
            return nodo.caracter
        if isinstance(nodo, Clase):
            return self.azar.choice(nodo.caracteres)
        if isinstance(nodo, Union):
            opciones = [h for h in nodo.hijos() if not h.es_vacio()]
            return self.palabra(self.azar.choice(opciones))
        if isinstance(nodo, Concatenacion):
            return self.palabra(nodo.izquierda) + self.palabra(nodo.derecha)
        if isinstance(nodo, Estrella):
            return "".join(self.palabra(nodo.hijo) for _ in range(self.azar.randint(0, self.repeticiones)))
        raise TypeError(nodo)
