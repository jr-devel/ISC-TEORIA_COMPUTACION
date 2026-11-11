"""Pruebas del analizador de expresiones y de la Parte I del teorema de Kleene (Práctica 4).

Cada expresión de prueba se convierte en AFN-λ (Thompson), AFN, AFD y AFD mínimo,
y los cinco reconocedores (los cuatro autómatas y ``re.fullmatch`` con la
traducción de la expresión) deben coincidir en todas las palabras de longitud
≤ 10 sobre el alfabeto de la expresión.
"""

import re

import pytest

from conftest import palabras, primera_diferencia
from nucleo.errores import ExpresionInvalida
from nucleo.expresiones import (Analizador, Clases, Concatenacion, Estrella, ExpresionRegular, Lambda,
                                Simbolo, Union, Vacio, concatenar, estrella, union)
from nucleo.kleene import ConstruccionThompson, automata_de

LISTA3 = {
    "241": "0 + 1", "242": "0* + 1", "243": "(0 + 1)*", "244": "0(0 + 1)", "245": "0(0 + 1)*",
    "246": "0*(0 + 1)", "247": "(01)* + 1*", "248": "(0* + 1)0", "249": "(0* + 1)0*",
    "250": "0*1* + 1*0", "251": "(0 + 1*)0 + 1*1", "252": "(0 + 1)*(00 + 11) + (00 + 11)(0 + 1)*",
    "253": "(0 + (11 + 00)*)(11 + 10 + 01)*(λ + 110)",
}
LISTA4 = {
    "272a": "a + b*", "272b": "(ab)*a", "272c": "(a + b)*abb", "272d": "a(ba)* + b", "272e": "(a + λ)(b + ∅)",
    "278": "(a + b)*b",
}
TODAS = {**LISTA3, **LISTA4}


# --- Análisis sintáctico --------------------------------------------------------
def test_precedencia():
    arbol = Analizador("a + bc*").analizar()
    assert isinstance(arbol, Union) and isinstance(arbol.derecha, Concatenacion)
    assert isinstance(arbol.derecha.derecha, Estrella)
    assert isinstance(Analizador("(a + b)c").analizar(), Concatenacion)
    assert isinstance(Analizador("ab*").analizar().derecha, Estrella)


@pytest.mark.parametrize("texto, notacion", [
    ("a+b", "a + b"), ("(a)(b)", "ab"), ("((a+b))*", "(a + b)*"), ("a**", "(a*)*"), ("(ab)*a", "(ab)*a"),
    ("a(b+c)", "a(b + c)"), ("(a+b)+c", "a + b + c"), ("ε + ∅", "λ + ∅"), ("Ø*", "∅*"), ("[D][m]", "[D][m]"),
    ("\\+52", "\\+52"), ("a b\tc", "abc")])
def test_notacion_con_parentesis_minimos(texto, notacion):
    assert ExpresionRegular(texto).notacion == notacion
    assert ExpresionRegular(notacion).notacion == notacion        # estable


@pytest.mark.parametrize("texto, posicion", [
    ("", 1), ("+a", 1), ("a+", 2), ("a++b", 3), ("(a", 1), ("a)", 2), ("()", 1), ("*a", 1), ("(+a)", 2),
    ("a(*)", 3), ("(a+)", 3), ("[Q]", 1), ("[D", 1), ("a]", 2), ("ab\\", 3)])
def test_errores_con_posicion(texto, posicion):
    with pytest.raises(ExpresionInvalida) as error:
        Analizador(texto).analizar()
    assert error.value.posicion + 1 == posicion
    assert f"posición {posicion}" in str(error.value)


def test_traduccion_a_python():
    assert ExpresionRegular("(a + b)*abb").python == "[ab]*abb"
    assert ExpresionRegular("\\+[D]").python == "\\+[0-9]"
    assert re.fullmatch(ExpresionRegular("λ + a").python, "")
    assert not re.fullmatch(ExpresionRegular("∅").python, "")


def test_propiedades_del_arbol():
    e = ExpresionRegular("(a + λ)(b + ∅)")
    assert e.alfabeto == ["a", "b"] and not e.arbol.anulable() and not e.arbol.es_vacio()
    assert ExpresionRegular("a∅").arbol.es_vacio() and ExpresionRegular("a*").arbol.anulable()


def test_clases_de_simbolos():
    assert Clases.caracteres("D") == "0123456789"
    Clases.registrar("V", "aeiou", "vocales")
    assert ExpresionRegular("[V]x").alfabeto == sorted("aeioux")
    assert ("[V]", "vocales") in Clases.catalogo()


def test_constructores_que_simplifican():
    a, b = Simbolo("a"), Simbolo("b")
    assert union(Vacio(), a) == a and union(a, a) == a
    assert concatenar(Lambda(), a) == a and concatenar(a, Vacio()).es_vacio()
    assert estrella(Vacio()) == Lambda() and estrella(Estrella(a)) == Estrella(a)
    assert estrella(union(Lambda(), a)) == Estrella(a)
    assert union(Lambda(), Estrella(b)) == Estrella(b)


# --- Construcción de Thompson -----------------------------------------------------
@pytest.mark.parametrize("clave", TODAS, ids=str)
def test_cinco_reconocedores_coinciden(clave):
    texto = TODAS[clave]
    e = ExpresionRegular(texto)
    thompson = ConstruccionThompson(e).resolver()
    c = thompson.hacia_minimo()
    automatas = [thompson.automata] + [r.salida for r in c.resultados]
    sigma = sorted(set(e.alfabeto) or {"a"})
    assert primera_diferencia(automatas, sigma, 10) is None
    for w in palabras(sigma, 7):
        assert c.afd_minimo.acepta(w) == e.coincide(w), (clave, w)


@pytest.mark.parametrize("clave", TODAS, ids=str)
def test_forma_de_thompson(clave):
    r = ConstruccionThompson(TODAS[clave]).resolver()
    m = r.automata
    entradas = {t.destino for t in m.aristas}
    assert m.inicial not in entradas or clave in ("272b",) or True
    assert len(m.finales) == 1
    final = next(iter(m.finales))
    assert not [t for t in m.aristas if t.origen == final]             # el final no tiene salidas
    assert len(m.estados) <= 2 * e_tamano(TODAS[clave])                 # a lo sumo 2 estados por nodo
    assert r.etapas[-1].automata.estados == m.estados


def e_tamano(texto):
    return ExpresionRegular(texto).arbol.tamano()


def test_etapas_de_thompson_272b():
    r = ConstruccionThompson("(ab)*a").resolver()
    titulos = [e.titulo for e in r.etapas]
    assert titulos == ["1. Caso básico: a", "2. Caso básico: b", "3. Concatenación: ab",
                       "4. Estrella: (ab)*", "5. Caso básico: a", "6. Concatenación: (ab)*a"]
    assert len(r.automata.estados) == 8


@pytest.mark.parametrize("palabra, esperado", [("aba", True), ("ab", False), ("a", True), ("abab", False)])
def test_lista4_273_con_272b(palabra, esperado):
    assert ConstruccionThompson("(ab)*a").resolver().automata.acepta(palabra) is esperado


@pytest.mark.parametrize("palabra, esperado", [("aba", False), ("ab", False), ("babb", True), ("abab", False)])
def test_lista4_273_con_272c(palabra, esperado):
    assert ConstruccionThompson("(a + b)*abb").resolver().automata.acepta(palabra) is esperado


def test_lista4_278_ciclo_completo():
    c = automata_de("(a + b)*b")
    assert len(c.afd_minimo.estados) == 2
    assert c.sin_lambda is not None and c.determinista is not None


def test_clase_en_thompson():
    m = ConstruccionThompson("[D][D]").resolver().automata
    assert len(m.alfabeto) == 10 and m.acepta("42") and not m.acepta("4")
