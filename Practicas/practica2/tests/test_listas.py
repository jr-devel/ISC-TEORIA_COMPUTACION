"""Los autómatas de las Listas 2 y 3 (Ejercicio 2) se cargan y reconocen sus cadenas de prueba.

``automatas/pruebas.json`` guarda, para cada ejercicio, el tipo con el que se
clasificó y las cadenas válidas, inválidas y frontera documentadas. Cada
autómata se prueba en sus tres formatos para confirmar que el simulador lee
lo mismo del .jff, del .json y del .xml.
"""

import json

import pytest

from conftest import AUTOMATAS
from nucleo.errores import PalabraFueraDeAlfabeto
from nucleo.formatos import Archivos

PRUEBAS = json.loads((AUTOMATAS / "pruebas.json").read_text(encoding="utf-8"))
CARPETA = {"AFD": "afd", "AFN": "afnd", "AFN-λ": "afnd-lambda"}


def acepta(m, w):
    """El .jff no guarda Σ (se infiere de las transiciones): un símbolo ajeno equivale a rechazo."""
    try:
        return m.acepta(w)
    except PalabraFueraDeAlfabeto:
        return False


def ruta(clave, extension):
    return AUTOMATAS / CARPETA[PRUEBAS[clave]["tipo"]] / f"{clave}{extension}"


@pytest.mark.parametrize("clave", sorted(PRUEBAS))
def test_cadenas_de_prueba(clave):
    datos = PRUEBAS[clave]
    m = Archivos.abrir(ruta(clave, ".jff"))
    assert m.tipo == datos["tipo"]
    # Cinco de cada clase, salvo cuando el lenguaje (o su complemento) tiene menos palabras.
    assert len(datos["validas"]) + len(datos["invalidas"]) >= 5
    for w in datos["validas"]:
        assert acepta(m, w), w
    for w in datos["invalidas"]:
        assert not acepta(m, w), w


@pytest.mark.parametrize("clave", sorted(PRUEBAS))
def test_los_tres_formatos_coinciden(clave):
    jff, json_, xml = (Archivos.abrir(ruta(clave, e)) for e in (".jff", ".json", ".xml"))
    assert set(jff.aristas) == set(json_.aristas) == set(xml.aristas)
    assert jff.finales == json_.finales == xml.finales and jff.inicial == json_.inicial == xml.inicial


def test_clasificacion_completa():
    tipos = [d["tipo"] for d in PRUEBAS.values()]
    assert {"AFD", "AFN", "AFN-λ"} <= set(tipos)
    for tipo, carpeta in CARPETA.items():
        assert len(list((AUTOMATAS / carpeta).glob("*.jff"))) == tipos.count(tipo)
