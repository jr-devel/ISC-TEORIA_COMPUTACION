"""Ejercicio 5: modelo del fantasma de Pac-Man ampliado (Gribkoff, 2013, fig. 3).

Las cadenas son secuencias de eventos; el autómata acepta las que dejan al
fantasma en un estado peligroso para Pac-Man (Vagar o Perseguir). Una secuencia
físicamente imposible deja el conjunto de estados activos vacío.
"""

import pytest

from conftest import AUTOMATAS
from nucleo.formatos import Archivos

APLICACION = AUTOMATAS / "aplicacion"

CASOS = [
    ("", "rechaza"), ("l", "acepta"), ("lv", "acepta"), ("lvp", "acepta"), ("lve", "rechaza"),
    ("lveax", "acepta"), ("lvec", "rechaza"), ("lvecb", "rechaza"), ("lvecbl", "acepta"), ("lveae", "rechaza"),
    ("lveaeax", "acepta"), ("lp", "imposible"), ("lc", "imposible"), ("lvex", "imposible"), ("v", "imposible"),
]


@pytest.fixture(scope="module")
def fantasma():
    return Archivos.abrir(APLICACION / "fantasma-pacman.jff")


def test_quintupla(fantasma):
    assert fantasma.tipo == "AFD"
    assert fantasma.estados == ("Casa", "Vagar", "Perseguir", "Huir", "Titilar", "Regresar")
    assert set(fantasma.alfabeto) == set("lvpeaxcb")
    assert fantasma.inicial == "Casa" and fantasma.finales == {"Vagar", "Perseguir"}


@pytest.mark.parametrize("palabra, esperado", CASOS)
def test_resultado_esperado(fantasma, palabra, esperado):
    r = fantasma.recorrer(palabra)
    obtenido = "imposible" if not r.activos else ("acepta" if r.aceptada else "rechaza")
    assert obtenido == esperado


def test_estados_nuevos_y_eventos_nuevos(fantasma):
    assert fantasma.delta_extendida("Casa", "lvea") == {"Titilar"}
    assert fantasma.delta_extendida("Casa", "lvecb") == {"Casa"}


@pytest.mark.parametrize("extension", [".json", ".xml"])
def test_mismo_modelo_en_los_tres_formatos(fantasma, extension):
    otro = Archivos.abrir(APLICACION / f"fantasma-pacman{extension}")
    assert set(otro.aristas) == set(fantasma.aristas) and otro.finales == fantasma.finales


def test_archivo_de_pruebas(fantasma):
    lineas = [x.strip() for x in (APLICACION / "pruebas.txt").read_text(encoding="utf-8").splitlines()
              if x.strip() and not x.startswith("#")]
    palabras = ["" if x == "λ" else x for x in lineas]
    assert palabras == [w for w, _ in CASOS] and len(palabras) >= 10
