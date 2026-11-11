"""Alfabetos, palabras y lenguajes finitos (Unidad Temática I).

Modelo de objetos
-----------------
* :class:`Alfabeto`  – conjunto finito y no vacío de símbolos de un carácter.
* :class:`Palabra`   – cadena finita inmutable; la palabra vacía se muestra como λ.
* :class:`Lenguaje`  – conjunto finito de palabras con las operaciones de conjuntos,
  la concatenación, la potencia, la reflexión y las cerraduras acotadas.
* :class:`Enumerador` – genera Σ⁰ ∪ Σ¹ ∪ … ∪ Σⁿ en orden canónico (longitud y
  luego orden del alfabeto) y vigila el límite de cadenas *antes* de generar.
* :class:`Informe`   – texto exportable con los resultados de una operación.

Todas las operaciones devuelven objetos nuevos y no modifican los existentes,
de modo que pueden probarse de forma aislada. El módulo no depende de Flet.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from itertools import product
from pathlib import Path
from typing import Iterable, Iterator

from .errores import LimiteExcedido, PalabraFueraDeAlfabeto, SimboloInvalido

LAMBDA = "λ"
"""Representación visible de la palabra vacía."""

RESERVADOS = frozenset({LAMBDA, "ε", ",", "{", "}", " ", "\t", "\n"})
"""Caracteres que no pueden ser símbolos porque forman parte de la notación."""

LIMITE_CADENAS = 200_000
"""Máximo de cadenas que una operación puede generar (Práctica 1, Operación 2)."""


def _texto_de(palabra: "Palabra | str") -> str:
    """Normaliza una palabra a ``str``; «λ» y «ε» se leen como la palabra vacía."""
    if isinstance(palabra, Palabra):
        return palabra.texto
    texto = str(palabra).strip()
    return "" if texto in (LAMBDA, "ε") else texto


def separar(texto: str) -> list[str]:
    """Divide un texto escrito por el usuario en elementos.

    Acepta comas o espacios como separadores (``"a, b"``, ``"a b"``) y quita las
    llaves de conjunto si las hay (``"{a, b}"``).
    """
    limpio = (texto or "").strip().removeprefix("{").removesuffix("}")
    partes = limpio.replace(",", " ").split()
    return [p for p in partes if p]


# ==========================================================================
# Alfabeto
# ==========================================================================
class Alfabeto:
    """Conjunto finito y no vacío de símbolos de un solo carácter.

    El orden en que se escriben los símbolos se conserva y define el orden
    canónico con el que se enumeran las cadenas.
    """

    __slots__ = ("_simbolos",)

    def __init__(self, simbolos: Iterable[str]) -> None:
        vistos: list[str] = []
        for s in simbolos:
            if not isinstance(s, str) or len(s) != 1:
                raise SimboloInvalido(f"«{s}» no es un símbolo: cada símbolo debe tener un solo carácter.")
            if s in RESERVADOS:
                raise SimboloInvalido(f"«{s}» está reservado por la notación y no puede ser un símbolo.")
            if s not in vistos:
                vistos.append(s)
        if not vistos:
            raise SimboloInvalido("Un alfabeto debe tener al menos un símbolo.")
        self._simbolos: tuple[str, ...] = tuple(vistos)

    @classmethod
    def leer(cls, texto: str) -> "Alfabeto":
        """Construye el alfabeto a partir de ``"a,b,c"``, ``"a b c"`` o ``"abc"``."""
        partes = separar(texto)
        if len(partes) == 1 and len(partes[0]) > 1:
            partes = list(partes[0])
        return cls(partes)

    # Protocolo de colección -------------------------------------------------
    @property
    def simbolos(self) -> tuple[str, ...]:
        return self._simbolos

    def __len__(self) -> int:
        return len(self._simbolos)

    def __iter__(self) -> Iterator[str]:
        return iter(self._simbolos)

    def __contains__(self, simbolo: object) -> bool:
        return simbolo in self._simbolos

    def __eq__(self, otro: object) -> bool:
        return isinstance(otro, Alfabeto) and set(self._simbolos) == set(otro._simbolos)

    def __hash__(self) -> int:
        return hash(frozenset(self._simbolos))

    def __repr__(self) -> str:
        return f"Alfabeto({list(self._simbolos)!r})"

    def __str__(self) -> str:
        return "{" + ", ".join(self._simbolos) + "}"

    # Pertenencia --------------------------------------------------------------
    def ajenos(self, palabra: "Palabra | str") -> list[str]:
        """Símbolos de ``palabra`` que no pertenecen al alfabeto (sin repetir)."""
        return sorted({c for c in _texto_de(palabra) if c not in self._simbolos})

    def admite(self, palabra: "Palabra | str") -> bool:
        """``True`` si ``palabra`` ∈ Σ*."""
        return not self.ajenos(palabra)

    def exigir(self, palabra: "Palabra | str") -> "Palabra":
        """Devuelve la palabra si está en Σ*; si no, explica qué símbolos sobran."""
        fuera = self.ajenos(palabra)
        if fuera:
            raise PalabraFueraDeAlfabeto(
                f"La palabra «{_texto_de(palabra)}» usa {', '.join(fuera)}, que no está en Σ = {self}.")
        return Palabra(_texto_de(palabra))

    # Conteo y generación --------------------------------------------------
    def cuantas(self, maximo: int, minimo: int = 0) -> int:
        """|Σ^minimo ∪ … ∪ Σ^maximo| = Σ |Σ|^i, sin generar las cadenas."""
        k = len(self)
        return sum(k ** i for i in range(minimo, maximo + 1))

    def potencia(self, n: int) -> "Lenguaje":
        """Σⁿ: todas las palabras de longitud exactamente ``n``."""
        return Lenguaje(Enumerador(self, n, minimo=n))

    def estrella(self, maximo: int) -> "Lenguaje":
        """Σ* acotada: palabras de longitud 0 a ``maximo`` (incluye λ)."""
        return Lenguaje(Enumerador(self, maximo, minimo=0))

    def mas(self, maximo: int) -> "Lenguaje":
        """Σ⁺ acotada: palabras de longitud 1 a ``maximo`` (excluye λ)."""
        if maximo < 1:
            return Lenguaje()
        return Lenguaje(Enumerador(self, maximo, minimo=1))


# ==========================================================================
# Palabra
# ==========================================================================
class Palabra:
    """Cadena finita e inmutable sobre algún alfabeto.

    Las operaciones devuelven palabras nuevas. ``Palabra("")`` y
    ``Palabra("λ")`` representan la palabra vacía.
    """

    __slots__ = ("_texto",)

    def __init__(self, texto: "str | Palabra" = "") -> None:
        self._texto = _texto_de(texto)

    @property
    def texto(self) -> str:
        return self._texto

    @property
    def es_vacia(self) -> bool:
        return not self._texto

    def __len__(self) -> int:
        return len(self._texto)

    def __eq__(self, otra: object) -> bool:
        if isinstance(otra, Palabra):
            return self._texto == otra._texto
        if isinstance(otra, str):
            return self._texto == _texto_de(otra)
        return NotImplemented

    def __hash__(self) -> int:
        return hash(self._texto)

    def __lt__(self, otra: "Palabra") -> bool:
        return (len(self), self._texto) < (len(otra), otra._texto)

    def __repr__(self) -> str:
        return f"Palabra({self._texto!r})"

    def __str__(self) -> str:
        return self._texto or LAMBDA

    # Operaciones ------------------------------------------------------------
    def __add__(self, otra: "Palabra | str") -> "Palabra":
        """Concatenación ω·π."""
        return Palabra(self._texto + _texto_de(otra))

    def potencia(self, n: int) -> "Palabra":
        """ωⁿ, con ω⁰ = λ."""
        if n < 0:
            raise ValueError("El exponente de una palabra debe ser un entero no negativo.")
        return Palabra(self._texto * n)

    def inversa(self) -> "Palabra":
        """Reflexión ωᴿ."""
        return Palabra(self._texto[::-1])

    def prefijos(self, propios: bool = False) -> list["Palabra"]:
        """Prefijos de menor a mayor longitud: λ, ω₁, …, ω.

        Una palabra de longitud n tiene n + 1 prefijos; con ``propios=True`` se
        excluye la propia palabra.
        """
        fin = len(self) if propios else len(self) + 1
        return [Palabra(self._texto[:i]) for i in range(fin)]

    def sufijos(self, propios: bool = False) -> list["Palabra"]:
        """Sufijos de menor a mayor longitud: λ, …, ω (n + 1 en total)."""
        n = len(self)
        fin = n if propios else n + 1
        return [Palabra(self._texto[n - i:]) for i in range(fin)]

    def subcadenas(self) -> list["Palabra"]:
        """Subcadenas distintas (incluida λ), por longitud y orden de aparición.

        Hay a lo sumo n(n + 1)/2 + 1 subcadenas distintas: una por cada par de
        posiciones (i, j) con i < j, más la palabra vacía.
        """
        vistas: dict[str, None] = {"": None}
        n = len(self)
        for largo in range(1, n + 1):
            for i in range(n - largo + 1):
                vistas.setdefault(self._texto[i:i + largo], None)
        return [Palabra(t) for t in vistas]

    def es_prefijo_de(self, otra: "Palabra | str") -> bool:
        return _texto_de(otra).startswith(self._texto)

    def es_sufijo_de(self, otra: "Palabra | str") -> bool:
        return _texto_de(otra).endswith(self._texto)

    def es_subcadena_de(self, otra: "Palabra | str") -> bool:
        return self._texto in _texto_de(otra)

    def cuenta(self, simbolo: str) -> int:
        """|ω|ₐ: número de apariciones del símbolo."""
        return self._texto.count(simbolo)


# ==========================================================================
# Enumerador de Σ^i
# ==========================================================================
class Enumerador:
    """Recorre Σ^minimo ∪ … ∪ Σ^maximo en orden canónico.

    El total se calcula con la fórmula Σ |Σ|^i antes de generar una sola
    cadena; si supera ``limite`` se lanza :class:`LimiteExcedido`.
    """

    def __init__(self, alfabeto: Alfabeto, maximo: int, minimo: int = 0,
                 limite: int = LIMITE_CADENAS) -> None:
        if maximo < 0 or minimo < 0:
            raise ValueError("Las longitudes deben ser enteros no negativos.")
        if minimo > maximo:
            raise ValueError("La longitud mínima no puede ser mayor que la máxima.")
        self.alfabeto, self.maximo, self.minimo, self.limite = alfabeto, maximo, minimo, limite
        self.total = alfabeto.cuantas(maximo, minimo)
        if self.total > limite:
            raise LimiteExcedido(
                f"Σ con {len(alfabeto)} símbolos y longitud hasta {maximo} produce {self.total:,} cadenas; "
                f"el límite es {limite:,}. Reduzca la longitud o el alfabeto.".replace(",", " "))

    def __len__(self) -> int:
        return self.total

    def __iter__(self) -> Iterator[str]:
        for n in range(self.minimo, self.maximo + 1):
            for tupla in product(self.alfabeto.simbolos, repeat=n):
                yield "".join(tupla)

    def por_longitud(self) -> dict[int, list[str]]:
        grupos: dict[int, list[str]] = {}
        for w in self:
            grupos.setdefault(len(w), []).append(w)
        return grupos

    @staticmethod
    def longitud_maxima(simbolos: int, limite: int = LIMITE_CADENAS) -> int:
        """Mayor n tal que |Σ⁰ ∪ … ∪ Σⁿ| no excede el límite."""
        n, total = 0, 1
        while True:
            siguiente = total + simbolos ** (n + 1)
            if siguiente > limite:
                return n
            n, total = n + 1, siguiente


# ==========================================================================
# Lenguaje finito
# ==========================================================================
class Lenguaje:
    """Conjunto finito de palabras.

    Se ordena en forma canónica (por longitud y luego lexicográficamente) al
    mostrarse. Admite ``|`` (unión), ``&`` (intersección), ``-`` (diferencia)
    y ``*`` (concatenación con otro lenguaje).
    """

    __slots__ = ("_palabras",)

    def __init__(self, palabras: Iterable["Palabra | str"] = ()) -> None:
        self._palabras: frozenset[str] = frozenset(_texto_de(p) for p in palabras)

    @classmethod
    def leer(cls, texto: str) -> "Lenguaje":
        """``"{λ, a, ab}"`` → Lenguaje({"", "a", "ab"})."""
        return cls(separar(texto))

    @classmethod
    def vacio(cls) -> "Lenguaje":
        return cls()

    @classmethod
    def unitario_vacio(cls) -> "Lenguaje":
        """{λ}, neutro de la concatenación."""
        return cls([""])

    # Protocolo de colección -------------------------------------------------
    @property
    def textos(self) -> frozenset[str]:
        return self._palabras

    def __len__(self) -> int:
        return len(self._palabras)

    def __iter__(self) -> Iterator[Palabra]:
        return iter(self.ordenadas())

    def __contains__(self, palabra: object) -> bool:
        if isinstance(palabra, (Palabra, str)):
            return _texto_de(palabra) in self._palabras
        return False

    def __eq__(self, otro: object) -> bool:
        return isinstance(otro, Lenguaje) and self._palabras == otro._palabras

    def __hash__(self) -> int:
        return hash(self._palabras)

    def ordenadas(self) -> list[Palabra]:
        return [Palabra(t) for t in sorted(self._palabras, key=lambda t: (len(t), t))]

    def __str__(self) -> str:
        if not self._palabras:
            return "∅"
        return "{" + ", ".join(str(p) for p in self.ordenadas()) + "}"

    def __repr__(self) -> str:
        return f"Lenguaje({sorted(self._palabras, key=lambda t: (len(t), t))!r})"

    # Operaciones de conjuntos ---------------------------------------------------
    def __or__(self, otro: "Lenguaje") -> "Lenguaje":
        return Lenguaje(self._palabras | otro._palabras)

    def __and__(self, otro: "Lenguaje") -> "Lenguaje":
        return Lenguaje(self._palabras & otro._palabras)

    def __sub__(self, otro: "Lenguaje") -> "Lenguaje":
        return Lenguaje(self._palabras - otro._palabras)

    union, interseccion, diferencia = __or__, __and__, __sub__

    # Operaciones de lenguajes ---------------------------------------------------
    def __mul__(self, otro: "Lenguaje") -> "Lenguaje":
        """L₁L₂ = {xy : x ∈ L₁, y ∈ L₂}."""
        if len(self) * len(otro) > LIMITE_CADENAS:
            raise LimiteExcedido(f"La concatenación tendría hasta {len(self) * len(otro)} palabras; "
                                 f"el límite es {LIMITE_CADENAS}.")
        return Lenguaje(x + y for x in self._palabras for y in otro._palabras)

    concatenar = __mul__

    def potencia(self, n: int) -> "Lenguaje":
        """Lⁿ, con L⁰ = {λ}."""
        if n < 0:
            raise ValueError("El exponente de un lenguaje debe ser un entero no negativo.")
        resultado = Lenguaje.unitario_vacio()
        for _ in range(n):
            resultado = resultado * self
        return resultado

    def inverso(self) -> "Lenguaje":
        """Lᴿ = {ωᴿ : ω ∈ L}."""
        return Lenguaje(t[::-1] for t in self._palabras)

    def estrella(self, maximo: int) -> "Lenguaje":
        """L* acotada: palabras de L⁰ ∪ L¹ ∪ … de longitud a lo sumo ``maximo``."""
        return self._cerradura(maximo, incluir_vacia=True)

    def mas(self, maximo: int) -> "Lenguaje":
        """L⁺ acotada: palabras de L¹ ∪ L² ∪ … de longitud a lo sumo ``maximo``."""
        return self._cerradura(maximo, incluir_vacia=False)

    def _cerradura(self, maximo: int, incluir_vacia: bool) -> "Lenguaje":
        resultado: set[str] = {""} if incluir_vacia else set()
        frontera = {t for t in self._palabras if len(t) <= maximo}
        resultado |= frontera
        while frontera:
            nueva = {x + y for x in frontera for y in self._palabras if len(x + y) <= maximo} - resultado
            if len(resultado) + len(nueva) > LIMITE_CADENAS:
                raise LimiteExcedido(f"La cerradura supera {LIMITE_CADENAS} palabras.")
            resultado |= nueva
            frontera = nueva
        return Lenguaje(resultado)


# ==========================================================================
# Informe exportable
# ==========================================================================
@dataclass
class Informe:
    """Resultado de una operación listo para mostrarse o guardarse en .txt."""

    titulo: str
    elementos: list[str]
    datos: dict[str, str] = field(default_factory=dict)

    def texto(self) -> str:
        sello = datetime.now().strftime("%Y-%m-%d %H:%M")
        cabecera = [self.titulo, "=" * len(self.titulo), f"Generado: {sello}"]
        cabecera += [f"{k}: {v}" for k, v in self.datos.items()]
        cabecera += [f"Total: {len(self.elementos)}", ""]
        return "\n".join(cabecera + self.elementos) + "\n"

    def guardar(self, ruta: str | Path) -> Path:
        ruta = Path(ruta)
        ruta.parent.mkdir(parents=True, exist_ok=True)
        ruta.write_text(self.texto(), encoding="utf-8")
        return ruta
