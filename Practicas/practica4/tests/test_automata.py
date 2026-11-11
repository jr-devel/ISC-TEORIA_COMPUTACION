"""Pruebas de la jerarquía de autómatas y de la simulación (Práctica 2)."""

import pytest

from nucleo.automata import AFD, AFN, AFNLambda, Arista, Automata, Clasificador, Disposicion
from nucleo.errores import DefinicionInvalida, PalabraFueraDeAlfabeto


@pytest.fixture
def pares_de_a():
    """AFD: número par de aes sobre {a, b}."""
    return Automata.crear(["P", "I"], ["a", "b"], "P", ["P"],
                          [("P", "a", "I"), ("I", "a", "P"), ("P", "b", "P"), ("I", "b", "I")], "pares")


@pytest.fixture
def termina_en_ab():
    """AFN: palabras que terminan en ab (adivina dónde empieza el sufijo)."""
    return Automata.crear(["0", "1", "2"], "ab", "0", ["2"],
                          [("0", "a", "0"), ("0", "b", "0"), ("0", "a", "1"), ("1", "b", "2")])


@pytest.fixture
def con_lambda():
    """AFN-λ para a*b*: sólo acepta «b» pasando por la cerradura λ de q0."""
    return Automata.crear(["q0", "q1"], "ab", "q0", ["q1"],
                          [("q0", "a", "q0"), ("q0", "", "q1"), ("q1", "b", "q1")])


# --- Clasificación -----------------------------------------------------------
def test_el_tipo_se_deduce_de_delta(pares_de_a, termina_en_ab, con_lambda):
    assert isinstance(pares_de_a, AFD) and pares_de_a.tipo == "AFD"
    assert type(termina_en_ab) is AFN and termina_en_ab.tipo == "AFN"
    assert type(con_lambda) is AFNLambda and con_lambda.tipo == "AFN-λ"
    assert isinstance(pares_de_a, AFN) and isinstance(termina_en_ab, AFNLambda)   # jerarquía


def test_motivo_de_la_clasificacion(pares_de_a, termina_en_ab, con_lambda):
    assert "a lo sumo un destino" in Clasificador.motivo(pares_de_a)
    assert "δ(0, a)" in Clasificador.motivo(termina_en_ab)
    assert "λ" in Clasificador.motivo(con_lambda)
    assert Clasificador.no_determinismo(termina_en_ab) == [("0", "a")]
    assert Clasificador.no_determinismo(pares_de_a) == []


# --- AFD -----------------------------------------------------------------------
@pytest.mark.parametrize("palabra", ["", "b", "aa", "abab", "bbaab", "aaaa"])
def test_afd_acepta(pares_de_a, palabra):
    assert pares_de_a.acepta(palabra)


@pytest.mark.parametrize("palabra", ["a", "ab", "aaa", "babbb", "abbbb"])
def test_afd_rechaza(pares_de_a, palabra):
    assert not pares_de_a.acepta(palabra)


def test_afd_parcial_y_completado():
    m = Automata.crear(["A", "B"], "ab", "A", ["B"], [("A", "a", "B")])
    assert isinstance(m, AFD) and not m.es_completo and m.faltantes() == [("A", "b"), ("B", "a"), ("B", "b")]
    assert m.acepta("a") and not m.acepta("ab") and not m.acepta("b")
    completo = m.completar()
    assert completo.es_completo and len(completo.estados) == 3 and completo.estados[-1] == "∅"
    assert all(completo.acepta(w) == m.acepta(w) for w in ["", "a", "b", "ab", "aa", "ba"])


def test_afd_rechaza_no_determinismo():
    with pytest.raises(DefinicionInvalida):
        AFD(["A", "B"], "a", "A", [], [("A", "a", "A"), ("A", "a", "B")])
    with pytest.raises(DefinicionInvalida):
        AFN(["A"], "a", "A", [], [("A", "", "A")])


# --- AFN y AFN-λ ----------------------------------------------------------------
def test_afn_sigue_todos_los_caminos(termina_en_ab):
    r = termina_en_ab.recorrer("aab")
    assert [sorted(p.despues) for p in r.pasos] == [["0", "1"], ["0", "1"], ["0", "2"]]
    assert r.aceptada
    assert not termina_en_ab.acepta("aba")


def test_afn_lambda_requiere_la_cerradura(con_lambda):
    assert con_lambda.cierres() == {"q0": frozenset({"q0", "q1"}), "q1": frozenset({"q1"})}
    assert con_lambda.acepta("")            # q1 ∈ λ-cl(q0)
    assert con_lambda.acepta("b")           # sólo por la cerradura λ
    assert con_lambda.acepta("aabb") and not con_lambda.acepta("ba")
    r = con_lambda.recorrer("b")
    assert r.inicio == {"q0"} and r.inicio_cerrado == {"q0", "q1"}
    assert r.pasos[0].movidos == {"q1"}


def test_cierre_transitivo():
    m = Automata.crear(list("ABCD"), "a", "A", ["D"], [("A", "", "B"), ("B", "", "C"), ("C", "", "A"),
                                                     ("C", "a", "D")])
    assert m.cierre({"A"}) == {"A", "B", "C"}
    assert m.acepta("a") and not m.acepta("")


def test_delta_extendida(termina_en_ab):
    assert termina_en_ab.delta_extendida("0", "ab") == {"0", "2"}
    assert termina_en_ab.delta_extendida("1", "a") == frozenset()


# --- Simulación paso a paso --------------------------------------------------------
def test_simulacion_interactiva(con_lambda):
    sim = con_lambda.simulacion("ab")
    assert sim.activos == {"q0", "q1"} and sim.leido == "" and sim.pendiente == "ab"
    paso = sim.avanzar()
    assert paso.simbolo == "a" and paso.movidos == {"q0"} and paso.despues == {"q0", "q1"}
    assert paso.agrego_cierre == {"q1"}
    sim.avanzar()
    assert sim.terminada and sim.recorrido.aceptada
    with pytest.raises(DefinicionInvalida):
        sim.avanzar()


def test_traza_legible(termina_en_ab):
    lineas = termina_en_ab.recorrer("ba").lineas(termina_en_ab.estados)
    assert lineas[0] == "Palabra: ba" and "RECHAZADA" in lineas[-1]


def test_muerte_del_recorrido():
    m = Automata.crear(["A", "B"], "ab", "A", ["B"], [("A", "a", "B")])
    r = m.recorrer("ba")
    assert r.murio_en == 1 and not r.aceptada and "no quedan estados activos" in r.lineas()[-1]


def test_palabra_fuera_del_alfabeto(pares_de_a):
    with pytest.raises(PalabraFueraDeAlfabeto):
        pares_de_a.acepta("abc")


# --- Validación de la quíntupla ------------------------------------------------------
@pytest.mark.parametrize("args", [
    ([], "a", "A", [], []),                                  # Q vacío
    (["A", "A"], "a", "A", [], []),                          # estado repetido
    (["A"], "", "A", [], []),                                # Σ vacío
    (["A"], "a", "Z", [], []),                               # inicial fuera de Q
    (["A"], "a", "A", ["Z"], []),                            # F ⊄ Q
    (["A"], "a", "A", [], [("A", "b", "A")]),                # símbolo fuera de Σ
    (["A"], "a", "A", [], [("A", "a", "Z")]),                # destino fuera de Q
    (["A"], ["λ"], "A", [], []),                             # λ en Σ
])
def test_quintupla_invalida(args):
    with pytest.raises(DefinicionInvalida):
        Automata.crear(*args)


def test_tabla_y_quintupla(pares_de_a, con_lambda):
    encabezados, filas = pares_de_a.tabla()
    assert encabezados == ["", "δ", "a", "b"] and filas[0] == ["→*", "P", "I", "P"]
    assert con_lambda.tabla()[0][-1] == "λ"
    assert con_lambda.quintupla()[0].startswith("Q  = {q0, q1}")
    assert "→*" in pares_de_a.tabla_texto()


def test_renombrar_y_alcanzables():
    m = Automata.crear(list("ABC"), "a", "A", ["B"], [("A", "a", "B"), ("C", "a", "A")])
    assert m.alcanzables() == ["A", "B"]
    r = m.renombrar({"A": "q0", "B": "q1"})
    assert r.estados == ("q0", "q1", "C") and r.inicial == "q0" and r.finales == {"q1"}
    assert type(r) is type(m)


def test_desde_tabla_y_disposicion():
    m = Automata.desde_tabla(["p", "q"], ["0"], "p", ["q"], {("p", "0"): ["q"], ("q", ""): ["p"]})
    assert m.tipo == "AFN-λ" and m.aristas == [Arista("p", "0", "q"), Arista("q", "", "p")]
    pos = Disposicion.por_niveles(m)
    assert pos["p"][0] < pos["q"][0]
