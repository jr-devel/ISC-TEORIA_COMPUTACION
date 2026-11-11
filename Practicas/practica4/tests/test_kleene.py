"""Pruebas de la Parte II del teorema de Kleene: eliminación de estados y lema de Arden.

Para cada autómata se obtiene la expresión, se vuelve a convertir en AFD mínimo
con la Parte I y se exige que sea equivalente al autómata original.
"""

import pytest

from conftest import AUTOMATAS
from nucleo.algoritmos import Equivalencia
from nucleo.automata import Automata
from nucleo.errores import DefinicionInvalida
from nucleo.expresiones import ExpresionRegular
from nucleo.formatos import Archivos
from nucleo.kleene import (AutomataGeneralizado, ConstruccionThompson, EliminacionDeEstados, SistemaArden,
                           comparar, verificar_determinismo)

CASOS = (sorted((AUTOMATAS / "practica4" / "casos-de-prueba").glob("lista*.jff"))
         + sorted((AUTOMATAS / "practica3" / "afd-a-er").glob("*.jff")))


def equivale(automata, expresion):
    regreso = ConstruccionThompson(ExpresionRegular(expresion.notacion()), list(automata.alfabeto)).resolver()
    return Equivalencia(automata, regreso.automata).resolver().equivalentes


@pytest.mark.parametrize("ruta", CASOS, ids=lambda p: p.stem)
def test_eliminacion_de_estados(ruta):
    m = Archivos.abrir(ruta)
    assert verificar_determinismo(m)[0]
    r = EliminacionDeEstados(m).resolver()
    assert equivale(m, r.expresion)
    assert len(r.etapas) == len(m.estados) + 2 and sorted(r.orden) == sorted(m.estados)


@pytest.mark.parametrize("ruta", CASOS, ids=lambda p: p.stem)
def test_eliminacion_en_el_orden_de_q(ruta):
    m = Archivos.abrir(ruta)
    r = EliminacionDeEstados(m, list(m.estados)).resolver()
    assert r.orden == list(m.estados) and equivale(m, r.expresion)


@pytest.mark.parametrize("ruta", CASOS, ids=lambda p: p.stem)
def test_lema_de_arden(ruta):
    m = Archivos.abrir(ruta)
    assert equivale(m, SistemaArden(m).resolver().expresion)


def test_lista4_276_multiplos_de_tres():
    m = Archivos.abrir(AUTOMATAS / "practica4" / "casos-de-prueba" / "lista4-276.jff")
    e = ExpresionRegular(EliminacionDeEstados(m).resolver().notacion)
    for w in ["", "aaa", "babaab", "bbb", "aaaaaa"]:
        assert e.coincide(w)
    for w in ["a", "aab", "aaaa"]:
        assert not e.coincide(w)


def test_dos_metodos_dan_expresiones_equivalentes():
    m = Archivos.abrir(AUTOMATAS / "practica4" / "casos-de-prueba" / "lista4-277.jff")
    r1 = EliminacionDeEstados(m).resolver().notacion
    r2 = SistemaArden(m).resolver().notacion
    assert comparar(r1, r2).equivalentes


def test_determinismo():
    m = Archivos.abrir(AUTOMATAS / "practica4" / "casos-de-prueba" / "no-determinista-263.jff")
    ok, mensaje = verificar_determinismo(m)
    assert not ok and "δ(" in mensaje
    con_lambda = Automata.crear(["A", "B"], "a", "A", ["B"], [("A", "", "B")])
    assert "λ" in verificar_determinismo(con_lambda)[1]


def test_generalizado_une_paralelas():
    m = Automata.crear(["A"], "ab", "A", ["A"], [("A", "a", "A"), ("A", "b", "A")])
    g = AutomataGeneralizado(m)
    assert g.etiqueta("A", "A").notacion() == "a + b"
    assert g.inicio == "I" and g.fin == "T"
    assert EliminacionDeEstados(m).resolver().notacion == "(a + b)*"


def test_nombres_de_i_y_t_no_chocan():
    m = Automata.crear(["I", "T"], "a", "I", ["T"], [("I", "a", "T")])
    g = AutomataGeneralizado(m)
    assert g.inicio == "I'" and g.fin == "T'"
    assert EliminacionDeEstados(m).resolver().notacion == "a"


def test_orden_invalido():
    m = Automata.crear(["A", "B"], "a", "A", ["B"], [("A", "a", "B")])
    with pytest.raises(DefinicionInvalida):
        EliminacionDeEstados(m, ["A"])


def test_lenguaje_vacio():
    m = Automata.crear(["A"], "a", "A", [], [("A", "a", "A")])
    assert EliminacionDeEstados(m).resolver().notacion == "∅"


@pytest.mark.parametrize("r1, r2, iguales", [
    ("(a + b)*", "(a*b*)*", True), ("a(ba)*", "(ab)*a", True), ("(a + λ)*", "a*", True),
    ("a*b", "a*", False), ("(0 + 1)*00", "(0 + 1)*0", False)])
def test_comparar(r1, r2, iguales):
    assert comparar(r1, r2).equivalentes is iguales
