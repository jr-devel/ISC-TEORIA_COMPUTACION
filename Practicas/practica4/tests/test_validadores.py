"""Congruencia entre modelos: cada validador frente a ``re.fullmatch``.

Procedimiento de generación (``GeneradorDePruebas``): 300 palabras válidas
recorriendo el árbol de la expresión al azar con semilla fija, 300 mutaciones
de esas palabras (una o dos operaciones entre insertar, borrar, sustituir,
duplicar o intercambiar un carácter, con caracteres del alfabeto o de un ruido
fijo que incluye espacio, ñ y signos) y los casos frontera escritos a mano. Tras quitar repetidas quedan
más de 500 palabras por validador, con al menos 100 válidas y 100 inválidas.
"""

import pytest

from nucleo.validadores import CATALOGO, GeneradorDePruebas

VALIDADORES = list(CATALOGO.values())


@pytest.mark.parametrize("validador", VALIDADORES, ids=lambda v: v.clave)
def test_automata_y_re_coinciden(validador):
    palabras = GeneradorDePruebas(validador).generar()
    assert len(palabras) >= 500
    validas = [w for w in palabras if validador.coincide_re(w)]
    assert len(validas) >= 100 and len(palabras) - len(validas) >= 100
    for w in palabras:
        assert validador.valida(w)[0] == validador.coincide_re(w), w


@pytest.mark.parametrize("validador", VALIDADORES, ids=lambda v: v.clave)
def test_ejemplos_documentados(validador):
    for w in validador.validos:
        assert validador.valida(w)[0], w
    for w in validador.invalidos:
        assert not validador.valida(w)[0], w


@pytest.mark.parametrize("validador", VALIDADORES, ids=lambda v: v.clave)
def test_minimizacion_reduce(validador):
    e = validador.estadisticas()
    assert e["AFD mínimo"] <= e["AFD (subconjuntos)"] < e["AFN-λ (Thompson)"]


def test_mensajes():
    correo = CATALOGO["correo"]
    assert "ñ" in correo.valida("niño@ipn.mx")[1]
    assert "carácter 6" in correo.valida("juan..rico@ipn.mx")[1]
    assert "termina antes" in correo.valida("juan@ipn")[1]


def test_al_menos_tres_validadores():
    assert len(CATALOGO) >= 3 and all(v.norma and v.fuera for v in VALIDADORES)
