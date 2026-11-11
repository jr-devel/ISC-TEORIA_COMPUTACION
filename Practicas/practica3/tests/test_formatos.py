"""Pruebas de importación y exportación (.jff, .json y .xml)."""

import json

import pytest

from nucleo.automata import Automata
from nucleo.errores import ArchivoInvalido
from nucleo.formatos import Archivos, SerializadorJFF, SerializadorJSON, SerializadorXML

SERIALIZADORES = [SerializadorJFF(), SerializadorJSON(), SerializadorXML()]


def ejemplos():
    return [
        Automata.crear(["P", "I"], "ab", "P", ["P"], [("P", "a", "I"), ("I", "a", "P"), ("P", "b", "P"),
                                                      ("I", "b", "I")], "afd"),
        Automata.crear(["0", "1", "2"], "ab", "0", ["2"], [("0", "a", "0"), ("0", "b", "0"), ("0", "a", "1"),
                                                           ("1", "b", "2")], "afn"),
        Automata.crear(["q0", "q1"], "ab", "q0", ["q1"], [("q0", "a", "q1"), ("q0", "b", "q0"),
                                                          ("q0", "", "q1")], "anexo3"),
        Automata.crear(["{A,B}", "∅"], "01", "{A,B}", ["{A,B}"], [("{A,B}", "0", "∅"), ("∅", "0", "∅")], "raros"),
    ]


def mismo(a, b):
    return (a.estados == b.estados and a.inicial == b.inicial and a.finales == b.finales
            and a.aristas == b.aristas and a.tipo == b.tipo)


@pytest.mark.parametrize("serializador", SERIALIZADORES, ids=lambda s: s.EXTENSION)
@pytest.mark.parametrize("automata", ejemplos(), ids=lambda m: m.nombre)
def test_ida_y_vuelta(serializador, automata):
    leido = serializador.leer(serializador.escribir(automata))
    assert mismo(leido, automata)
    if serializador.EXTENSION != ".jff":            # .jff no guarda Σ: se infiere
        assert leido.alfabeto == automata.alfabeto
    assert serializador.escribir(leido) == serializador.escribir(automata)   # punto fijo


@pytest.mark.parametrize("automata", ejemplos(), ids=lambda m: m.nombre)
def test_archivos_en_los_tres_formatos(tmp_path, automata):
    rutas = Archivos.guardar_en_todos(automata, tmp_path / automata.nombre)
    assert [r.suffix for r in rutas] == [".jff", ".json", ".xml"]
    for ruta in rutas:
        assert mismo(Archivos.abrir(ruta), automata)


def test_lambda_en_jff_es_read_vacio():
    texto = SerializadorJFF().escribir(ejemplos()[2])
    assert "<read />" in texto or "<read/>" in texto
    assert "<type>fa</type>" in texto and "<initial />" in texto


def test_lectura_del_esquema_del_anexo_3():
    anexo = {"tipo": "AFND-lambda", "alfabeto": ["a", "b"], "estados": ["q0", "q1"], "inicial": "q0",
             "aceptacion": ["q1"], "transiciones": [{"desde": "q0", "lee": "a", "hacia": ["q1"]},
                                                    {"desde": "q0", "lee": "b", "hacia": ["q0"]},
                                                    {"desde": "q0", "lee": "", "hacia": ["q1"]}]}
    m = SerializadorJSON().leer(json.dumps(anexo))
    assert mismo(m, ejemplos()[2])
    xml = """<?xml version="1.0" encoding="UTF-8"?>
<automata tipo="AFND-lambda"><alfabeto><simbolo>a</simbolo><simbolo>b</simbolo></alfabeto>
<estados><estado nombre="q0" inicial="true"/><estado nombre="q1" aceptacion="true"/></estados>
<transiciones><transicion desde="q0" lee="a" hacia="q1"/><transicion desde="q0" lee="b" hacia="q0"/>
<transicion desde="q0" lee="" hacia="q1"/></transiciones></automata>"""
    assert mismo(SerializadorXML().leer(xml), ejemplos()[2])


def test_jff_de_jflap_con_lambda_y_nombres_por_omision():
    texto = """<structure><type>fa</type><automaton>
    <state id="0" name="q0"><x>1</x><y>2</y><initial/></state><state id="1"><x>3</x><y>4</y><final/></state>
    <transition><from>0</from><to>1</to><read>λ</read></transition>
    <transition><from>1</from><to>1</to><read>x</read></transition></automaton></structure>"""
    m = SerializadorJFF().leer(texto)
    assert m.estados == ("q0", "q1") and m.tiene_lambda and m.alfabeto == ("x",) and m.acepta("xx")
    assert m.posicion("q1") == (3.0, 4.0)


@pytest.mark.parametrize("texto", [
    "<structure><type>pda</type></structure>",
    "<structure><type>fa</type><automaton><state id='0' name='a'/></automaton></structure>",
    "<structure><type>fa</type><automaton><state id='0' name='a'><initial/></state>"
    "<transition><from>0</from><to>9</to><read>a</read></transition></automaton></structure>",
])
def test_jff_invalido(texto):
    with pytest.raises(ArchivoInvalido):
        SerializadorJFF().leer(texto)


def test_declarado_afd_sin_serlo():
    datos = json.loads(SerializadorJSON().escribir(ejemplos()[1]))
    datos["tipo"] = "AFD"
    with pytest.raises(ArchivoInvalido, match="no es determinista"):
        SerializadorJSON().leer(json.dumps(datos))


def test_errores_de_archivo(tmp_path):
    with pytest.raises(ArchivoInvalido):
        Archivos.abrir(tmp_path / "no-existe.jff")
    with pytest.raises(ArchivoInvalido):
        Archivos.serializador("automata.txt")
    roto = tmp_path / "roto.json"
    roto.write_text("{", encoding="utf-8")
    with pytest.raises(ArchivoInvalido):
        Archivos.abrir(roto)
    sin_clave = tmp_path / "sin.json"
    sin_clave.write_text('{"estados": ["a"]}', encoding="utf-8")
    with pytest.raises(ArchivoInvalido, match="Falta la clave"):
        Archivos.abrir(sin_clave)
