"""Validadores construidos con expresiones regulares (Práctica 4, Ejercicio 4).

Cada :class:`Validador` guarda su expresión en la notación del curso; la
traducción a ``re`` se obtiene del árbol, y el reconocimiento se hace con el
AFD mínimo que produce la Parte I del teorema de Kleene seguida de la
eliminación de λ, la construcción de subconjuntos y la minimización.

:class:`GeneradorDePruebas` produce el conjunto de palabras con el que las
pruebas comparan el autómata con ``re.fullmatch``:

* palabras válidas obtenidas recorriendo el árbol al azar;
* mutaciones de las válidas: una o dos operaciones al azar entre insertar,
  borrar, sustituir o duplicar un carácter, o intercambiar dos vecinos; la
  mitad de los caracteres nuevos vienen del alfabeto y la otra mitad de un
  ruido fijo con espacio, ñ y signos;
* casos frontera escritos a mano.

El módulo no depende de Flet.
"""

from __future__ import annotations

import random
import re
from dataclasses import dataclass, field
from functools import cached_property

from .algoritmos import Cadena
from .automata import AFD
from .expresiones import ExpresionRegular, Muestreo
from .kleene import ConstruccionThompson


@dataclass
class Validador:
    clave: str
    nombre: str
    expresion: str
    norma: str
    descripcion: str
    validos: list[str] = field(default_factory=list)
    invalidos: list[str] = field(default_factory=list)
    fuera: list[str] = field(default_factory=list)

    @cached_property
    def er(self) -> ExpresionRegular:
        return ExpresionRegular(self.expresion)

    @property
    def python(self) -> str:
        return self.er.python

    @cached_property
    def construccion(self) -> tuple[int, Cadena]:
        thompson = ConstruccionThompson(self.er).resolver()
        return len(thompson.automata.estados), thompson.hacia_minimo()

    @cached_property
    def afd(self) -> AFD:
        """AFD mínimo con los estados renumerados q0, q1, … para que el diagrama sea legible."""
        return self.construccion[1].afd_minimo.renumerar(nombre=self.clave)

    def estadisticas(self) -> dict[str, int]:
        estados_thompson, cadena = self.construccion
        return {
            "AFN-λ (Thompson)": estados_thompson,
            "AFD (subconjuntos)": len(cadena.determinista.salida.estados) if cadena.determinista else 0,
            "AFD mínimo": len(cadena.afd_minimo.estados),
            "|Σ|": len(cadena.afd_minimo.alfabeto),
        }

    def valida(self, texto: str) -> tuple[bool, str]:
        """Reconoce ``texto`` con el AFD mínimo y explica el resultado."""
        ajenos = sorted({c for c in texto if c not in self.afd.alfabeto})
        if ajenos:
            return False, f"Contiene caracteres que la expresión no admite: {' '.join(ajenos)}"
        recorrido = self.afd.recorrer(texto)
        if recorrido.aceptada:
            return True, f"Aceptada: el AFD termina en el estado final {', '.join(recorrido.activos)}."
        if recorrido.murio_en is not None:
            n = recorrido.murio_en
            return False, f"Rechazada: el carácter {n} («{texto[n - 1]}») no puede aparecer ahí."
        return False, "Rechazada: la entrada termina antes de completar un valor válido."

    def coincide_re(self, texto: str) -> bool:
        return re.fullmatch(self.python, texto) is not None


class GeneradorDePruebas:
    """Conjunto reproducible de palabras válidas e inválidas para un validador."""

    RUIDO = "@.-_/:+()# aZ09ñ"

    def __init__(self, validador: Validador, semilla: int = 2027) -> None:
        self.validador = validador
        self.azar = random.Random(semilla)

    def generar(self, validas: int = 300, mutaciones: int = 300) -> list[str]:
        muestreo = Muestreo(self.azar, repeticiones=4)
        base = [muestreo.palabra(self.validador.er.arbol) for _ in range(validas)]
        alfabeto = "".join(self.validador.afd.alfabeto) + self.RUIDO
        mutadas = []
        for _ in range(mutaciones):
            palabra = self.azar.choice(base)
            for _ in range(self.azar.randint(1, 2)):
                palabra = self._mutar(palabra, alfabeto if self.azar.random() < 0.5 else self.RUIDO)
            mutadas.append(palabra)
        frontera = ["", " "] + self.validador.validos + self.validador.invalidos
        return list(dict.fromkeys(base + mutadas + frontera))

    def _mutar(self, palabra: str, alfabeto: str) -> str:
        i = self.azar.randrange(len(palabra) + 1)
        operacion = self.azar.choice(("insertar", "borrar", "sustituir", "duplicar", "intercambiar"))
        c = self.azar.choice(alfabeto)
        if operacion == "insertar" or not palabra:
            return palabra[:i] + c + palabra[i:]
        i = min(i, len(palabra) - 1)
        if operacion == "borrar":
            return palabra[:i] + palabra[i + 1:]
        if operacion == "sustituir":
            return palabra[:i] + c + palabra[i + 1:]
        if operacion == "duplicar":
            return palabra[:i] + palabra[i] + palabra[i:]
        if i + 1 < len(palabra):
            return palabra[:i] + palabra[i + 1] + palabra[i] + palabra[i + 2:]
        return palabra[:-1]


_NOMBRE = "([X] + _)([X] + _ + -)*"
_ETIQUETA = "[X]([X] + -)*"

CATALOGO: dict[str, Validador] = {v.clave: v for v in (
    Validador(
        "correo", "Correo electrónico",
        f"{_NOMBRE}(.{_NOMBRE})*@{_ETIQUETA}(.{_ETIQUETA})*.[L][L][L]*",
        "RFC 5321, sec. 4.1.2 (Mailbox, Dot-string) y RFC 1035, sec. 2.3.1 (etiquetas de dominio)",
        "Parte local de palabras separadas por puntos, @, uno o más subdominios y un dominio de "
        "primer nivel de al menos dos letras.",
        ["juan.rico@ipn.mx", "j_diego-2025@alumno.ipn.mx", "a@b.co"],
        ["juan..rico@ipn.mx", "@ipn.mx", "juan@ipn", "juan@ipn.m", ".juan@ipn.mx"],
        ["Partes locales entre comillas y caracteres como ! # $ % & ' * + / = ? ^ ` { | } ~ que el RFC 5322 "
         "sí admite.", "Dominios internacionalizados (ñ, acentos) y direcciones IP entre corchetes.",
         "Etiquetas de dominio que terminan en guion o exceden 63 caracteres: la expresión las acepta."]),
    Validador(
        "telefono", "Teléfono nacional (México)",
        "(\\+52 + λ)([D][D](-[D][D][D][D]-[D][D][D][D] + .[D][D][D][D].[D][D][D][D] + "
        "[D][D][D][D][D][D][D][D]) + [D][D][D]-[D][D][D]-[D][D][D][D] + \\([D][D]\\)[D][D][D][D]-[D][D][D][D])",
        "Plan Técnico Fundamental de Numeración del IFT (números nacionales de 10 dígitos)",
        "Diez dígitos, con prefijo +52 opcional, agrupados 2-4-4 o 3-3-4 con guiones, 2-4-4 con puntos, "
        "sin separadores o con la clave entre paréntesis.",
        ["5512345678", "55-1234-5678", "+52222-123-4567", "(55)1234-5678", "55.1234.5678"],
        ["55-1234.5678", "551234567", "55 1234 5678", "+5255-1234-567", "(55)12345678"],
        ["Espacios como separador: el alfabeto del autómata no incluye el espacio.",
         "No verifica que la clave de larga distancia exista; acepta cualquier combinación de dígitos.",
         "Formatos con prefijos antiguos (01, 044, 045) que se eliminaron en 2019."]),
    Validador(
        "url", "Dirección web (URL http/https)",
        "http(s + λ)://([m] + [D])([m] + [D] + -)*(.([m] + [D])([m] + [D] + -)*)*.[m][m][m]*"
        "(:[D][D]* + λ)(/([X] + - + _ + . + ~)*)*",
        "RFC 3986, secs. 3.1–3.3 (scheme, authority, path)",
        "Esquema http o https, nombre de host en minúsculas con dominio de primer nivel, puerto opcional "
        "y una ruta de segmentos con caracteres no reservados.",
        ["https://www.ipn.mx", "http://escom.ipn.mx:8080/tc/practica4", "https://a.io/", "http://x1.com/a/b~c"],
        ["ftp://ipn.mx", "https//ipn.mx", "https://ipn", "https://IPN.mx", "https://ipn.mx:/x"],
        ["Consultas (?a=1) y fragmentos (#sec), y los caracteres codificados con %.",
         "Hosts en mayúsculas, direcciones IP y usuarios (user@host).",
         "Otros esquemas (ftp, mailto, file)."]),
)}
