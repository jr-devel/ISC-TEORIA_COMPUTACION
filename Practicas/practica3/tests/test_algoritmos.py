"""Pruebas de la Práctica 3: eliminación de λ, subconjuntos, minimización, equivalencia y lotes.

Longitud de comparación. Para cada caso se comparan el autómata original, el AFN
sin λ, el AFD de subconjuntos y el AFD mínimo sobre *todas* las palabras de
longitud ≤ L, con L = n₁ + n₂ − 2, donde n₁ y n₂ son los estados del AFD de
subconjuntos y del AFD mínimo una vez completados. Por el teorema de Moore, dos
AFD completos con n₁ y n₂ estados que coinciden en todas las palabras de esa
longitud son equivalentes, así que la comprobación exhaustiva es también una
demostración. Se usa además L ≥ 8 para que los casos pequeños no queden triviales.
"""

from pathlib import Path

import pytest

from conftest import AUTOMATAS, primera_diferencia
from nucleo.algoritmos import (AFD, Equivalencia, HaciaMinimo, Lote, Minimizacion, QuitarLambda,
                               Subconjuntos, etiqueta_de_indice)
from nucleo.automata import Automata
from nucleo.errores import DefinicionInvalida
from nucleo.formatos import Archivos

CASOS = sorted((AUTOMATAS / "practica3" / "casos-de-prueba").glob("*.jff"))
POR_NUMERO = {p.stem.split("-")[-1]: p for p in CASOS}


def cadena_completa(m):
    c = HaciaMinimo(m).resolver()
    sin_lambda = c.sin_lambda.salida if c.sin_lambda else m
    afd = c.determinista.salida if c.determinista else sin_lambda
    return sin_lambda, afd, c.afd_minimo


@pytest.mark.parametrize("ruta", CASOS, ids=lambda p: p.stem)
def test_las_cuatro_versiones_reconocen_lo_mismo(ruta):
    original = Archivos.abrir(ruta)
    sin_lambda, afd, minimo = cadena_completa(original)
    assert not sin_lambda.tiene_lambda and isinstance(afd, AFD) and isinstance(minimo, AFD)
    n1, n2 = len(afd.completar().estados), len(minimo.completar().estados)
    L = max(8, n1 + n2 - 2)
    assert primera_diferencia([original, sin_lambda, afd, minimo], list(original.alfabeto), L) is None
    assert len(minimo.estados) <= len(afd.estados)


@pytest.mark.parametrize("ruta", CASOS, ids=lambda p: p.stem)
def test_el_minimo_es_minimo(ruta):
    """Ningún par de estados del mínimo es equivalente: minimizarlo otra vez no lo reduce."""
    _, _, minimo = cadena_completa(Archivos.abrir(ruta))
    assert len(Minimizacion(minimo).resolver().salida.estados) == len(minimo.estados)


# --- Casos con resultado conocido (Lista 3) --------------------------------------
@pytest.mark.parametrize("numero, estados", [("151", 5), ("152", 5), ("153", 6), ("154", 7), ("155", 5),
                                             ("156", 3), ("157", 4)])
def test_minimizacion_lista3(numero, estados):
    m = Archivos.abrir(POR_NUMERO[numero])
    assert len(Minimizacion(m).resolver().salida.estados) == estados


def test_inaccesibles_se_eliminan():
    m = Archivos.abrir(POR_NUMERO["154"])
    etapa = Minimizacion(m).resolver().etapas[0]
    assert "Se eliminan" in etapa.explicacion


def test_rondas_de_la_tabla():
    m = Automata.crear(list("ABCDE"), "01", "A", ["E"], [
        ("A", "0", "B"), ("A", "1", "C"), ("B", "0", "B"), ("B", "1", "D"), ("C", "0", "B"), ("C", "1", "C"),
        ("D", "0", "B"), ("D", "1", "E"), ("E", "0", "B"), ("E", "1", "C")])
    r = Minimizacion(m).resolver()
    rondas = [e for e in r.etapas if e.titulo.startswith(("3. Ronda", "Ronda"))]
    assert len(rondas) == 4                          # rondas 0, 1, 2 y la que ya no marca
    assert sorted(r.salida.estados) == ["B", "D", "E", "{A,C}"]


@pytest.mark.parametrize("numero", ["196", "197", "198", "199", "200"])
def test_quitar_lambda(numero):
    m = Archivos.abrir(POR_NUMERO[numero])
    r = QuitarLambda(m).resolver()
    assert not r.salida.tiene_lambda and r.salida.estados == m.estados
    cierres = m.cierres()
    for q in m.estados:
        for a in m.alfabeto:
            assert r.salida.destinos(q, a) == m.transitar(cierres[q], a)
        assert (q in r.salida.finales) == bool(cierres[q] & m.finales)


@pytest.mark.parametrize("numero", ["192", "193", "194", "260", "261", "263"])
def test_subconjuntos_solo_alcanzables(numero):
    m = Archivos.abrir(POR_NUMERO[numero])
    r = Subconjuntos(m).resolver()
    assert len(r.salida.estados) <= 2 ** len(m.estados)
    assert r.salida.alcanzables() == list(r.salida.estados)
    assert r.etapas[0].filas[0][1].startswith("A = {")


def test_subconjuntos_con_vacio():
    m = Automata.crear(["0", "1", "2"], "ab", "0", ["2"], [("0", "a", "1"), ("0", "a", "2")])
    sin = Subconjuntos(m).resolver().salida
    con = Subconjuntos(m, incluir_vacio=True).resolver().salida
    assert len(con.estados) == len(sin.estados) + 1 and con.es_completo and not sin.es_completo


def test_minimizacion_requiere_afd():
    with pytest.raises(DefinicionInvalida):
        Minimizacion(Archivos.abrir(POR_NUMERO["192"]))


def test_lenguaje_vacio_se_minimiza_a_un_estado():
    m = Automata.crear(["A", "B"], "a", "A", [], [("A", "a", "B")])
    r = Minimizacion(m).resolver()
    assert len(r.salida.estados) == 1 and not r.salida.finales


def test_etiquetas():
    assert [etiqueta_de_indice(i) for i in (0, 25, 26, 27)] == ["A", "Z", "A1", "B1"]


# --- Equivalencia -------------------------------------------------------------------
def test_equivalencia_de_un_automata_con_su_minimo():
    for ruta in CASOS:
        m = Archivos.abrir(ruta)
        veredicto = Equivalencia(m, cadena_completa(m)[2]).resolver()
        assert veredicto.equivalentes, ruta.stem


def test_no_equivalentes_con_contraejemplo_minimo():
    pares = Automata.crear(["P", "I"], "ab", "P", ["P"], [("P", "a", "I"), ("I", "a", "P"), ("P", "b", "P"),
                                                          ("I", "b", "I")])
    todo = Automata.crear(["T"], "ab", "T", ["T"], [("T", "a", "T"), ("T", "b", "T")])
    v = Equivalencia(pares, todo).resolver()
    assert not v.equivalentes and v.contraejemplo == "a" and "«a»" in v.explicacion


def test_alfabetos_distintos():
    solo_a = Automata.crear(["X"], "a", "X", ["X"], [("X", "a", "X")])
    a_y_b = Automata.crear(["X"], "ab", "X", ["X"], [("X", "a", "X")])
    assert Equivalencia(solo_a, a_y_b).resolver().equivalentes


# --- Lotes ---------------------------------------------------------------------------
def test_lote(tmp_path):
    m = Archivos.abrir(POR_NUMERO["263"])
    entrada = tmp_path / "cadenas.txt"
    entrada.write_text("# comentario\n01\n\n1101\nλ\n012\n", encoding="utf-8")
    lote = Lote(m)
    filas = lote.validar_archivo(entrada)
    assert [f.palabra for f in filas] == ["01", "1101", "λ", "012"]
    assert [f.veredicto for f in filas] == ["ACEPTADA", "ACEPTADA", "RECHAZADA", "ERROR"]
    salida = lote.informe(filas).guardar(tmp_path / "informe.txt")
    assert "Aceptadas: 2" in salida.read_text(encoding="utf-8")
    with pytest.raises(DefinicionInvalida):
        lote.validar_archivo(tmp_path / "no.txt")


def test_cada_resultado_tiene_etapas_y_texto():
    m = Archivos.abrir(POR_NUMERO["199"])
    for r in HaciaMinimo(m).resolver().resultados:
        assert r.etapas and r.texto().startswith(r.algoritmo)
        assert r.etapas[-1].automata is r.salida
