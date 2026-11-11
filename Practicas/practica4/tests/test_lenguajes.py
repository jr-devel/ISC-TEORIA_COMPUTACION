"""Pruebas del núcleo de cadenas y lenguajes (Práctica 1, Ejercicio 5)."""

import pytest

from nucleo.errores import LimiteExcedido, PalabraFueraDeAlfabeto, SimboloInvalido
from nucleo.lenguajes import LIMITE_CADENAS, Alfabeto, Enumerador, Informe, Lenguaje, Palabra


# --- Alfabeto ---------------------------------------------------------------
@pytest.mark.parametrize("texto, esperado", [("a,b", ("a", "b")), ("a b c", ("a", "b", "c")),
                                             ("01", ("0", "1")), ("{x, y}", ("x", "y")), ("a,a,b", ("a", "b"))])
def test_alfabeto_se_lee_de_varias_formas(texto, esperado):
    assert Alfabeto.leer(texto).simbolos == esperado


@pytest.mark.parametrize("texto", ["", "λ", "a,λ", "ab,c", "a,{"])
def test_alfabeto_invalido(texto):
    with pytest.raises(SimboloInvalido):
        Alfabeto.leer(texto) if texto != "ab,c" else Alfabeto(["ab", "c"])


def test_pertenencia_a_sigma_estrella():
    sigma = Alfabeto.leer("a,b")
    assert sigma.admite("abba") and sigma.admite("")
    assert sigma.ajenos("abcz") == ["c", "z"]
    with pytest.raises(PalabraFueraDeAlfabeto):
        sigma.exigir("abc")


# --- Palabra vacía y casos frontera ------------------------------------------
def test_palabra_vacia():
    vacia = Palabra("")
    assert vacia == Palabra("λ") == Palabra("ε")
    assert len(vacia) == 0 and str(vacia) == "λ" and vacia.es_vacia
    assert vacia.prefijos() == [vacia] and vacia.sufijos() == [vacia] and vacia.subcadenas() == [vacia]
    assert vacia.inversa() == vacia and vacia.potencia(5) == vacia


def test_prefijos_y_sufijos_de_longitud_uno():
    a = Palabra("a")
    assert [str(p) for p in a.prefijos()] == ["λ", "a"]
    assert [str(s) for s in a.sufijos()] == ["λ", "a"]
    assert a.prefijos(propios=True) == [Palabra("")]


def test_prefijos_sufijos_y_subcadenas():
    w = Palabra("abcb")
    assert [str(p) for p in w.prefijos()] == ["λ", "a", "ab", "abc", "abcb"]
    assert [str(s) for s in w.sufijos()] == ["λ", "b", "cb", "bcb", "abcb"]
    assert [str(s) for s in w.subcadenas()] == ["λ", "a", "b", "c", "ab", "bc", "cb", "abc", "bcb", "abcb"]


@pytest.mark.parametrize("texto", ["a", "ab", "abc", "abcd", "aaaa", "abab"])
def test_conteos(texto):
    w, n = Palabra(texto), len(texto)
    assert len(w.prefijos()) == n + 1 == len(w.sufijos())
    assert len(w.subcadenas()) <= n * (n + 1) // 2 + 1
    if len(set(texto)) == n:                      # símbolos distintos: se alcanza la cota
        assert len(w.subcadenas()) == n * (n + 1) // 2 + 1


def test_operaciones_de_palabras():
    w, p = Palabra("abbbaa"), Palabra("aaabb")
    assert w + p == Palabra("abbbaaaaabb") and len(w + p) == len(w) + len(p)
    assert w.inversa() == Palabra("aabbba") and w.potencia(0) == Palabra("")
    assert Palabra("ab").potencia(3) == Palabra("ababab")
    assert Palabra("ab").es_prefijo_de("abc") and Palabra("bc").es_sufijo_de("abc")
    assert w.cuenta("b") == 3
    with pytest.raises(ValueError):
        w.potencia(-1)


# --- Cerraduras --------------------------------------------------------------
def test_estrella_y_mas_en_longitud_cero():
    sigma = Alfabeto.leer("a,b")
    assert sigma.estrella(0) == Lenguaje([""])
    assert len(sigma.mas(0)) == 0
    assert sigma.estrella(3) - sigma.mas(3) == Lenguaje([""])


def test_alfabeto_de_un_simbolo():
    sigma = Alfabeto.leer("a")
    assert [str(p) for p in sigma.estrella(3)] == ["λ", "a", "aa", "aaa"]
    assert [str(p) for p in sigma.mas(3)] == ["a", "aa", "aaa"]
    assert sigma.potencia(2) == Lenguaje(["aa"])


@pytest.mark.parametrize("k, n", [(2, 3), (3, 4), (5, 2), (1, 7)])
def test_numero_de_cadenas(k, n):
    sigma = Alfabeto("abcde"[:k])
    assert len(sigma.estrella(n)) == sum(k ** i for i in range(n + 1)) == sigma.cuantas(n)
    assert len(sigma.mas(n)) == sum(k ** i for i in range(1, n + 1))


def test_orden_canonico():
    assert [str(p) for p in Alfabeto.leer("b,a").estrella(2)] == ["λ", "a", "b", "aa", "ab", "ba", "bb"]
    assert list(Enumerador(Alfabeto.leer("b,a"), 2)) == ["", "b", "a", "bb", "ba", "ab", "aa"]


def test_limite_de_doscientas_mil():
    sigma = Alfabeto.leer("0,1")
    assert sigma.cuantas(16) <= LIMITE_CADENAS < sigma.cuantas(17)
    assert len(Enumerador(sigma, 16)) == 131_071
    with pytest.raises(LimiteExcedido):
        Enumerador(sigma, 17)
    assert Enumerador.longitud_maxima(2) == 16 and Enumerador.longitud_maxima(10) == 5


def test_longitudes_invalidas():
    with pytest.raises(ValueError):
        Enumerador(Alfabeto("a"), -1)
    with pytest.raises(ValueError):
        Enumerador(Alfabeto("a"), 1, minimo=3)


# --- Lenguajes finitos -----------------------------------------------------------
def test_operaciones_de_conjuntos():
    l1, l2 = Lenguaje.leer("{a, ab, λ}"), Lenguaje.leer("ab, b")
    assert l1 | l2 == Lenguaje(["", "a", "ab", "b"])
    assert l1 & l2 == Lenguaje(["ab"])
    assert l1 - l2 == Lenguaje(["", "a"])
    assert str(l1) == "{λ, a, ab}" and str(Lenguaje()) == "∅"


def test_concatenacion_y_potencia():
    l1, l2 = Lenguaje(["a", "ab", "aa"]), Lenguaje(["bb", "aba"])
    assert l1 * l2 == Lenguaje(["abb", "aaba", "abbb", "ababa", "aabb", "aaaba"])
    assert Lenguaje(["ab", "c"]).potencia(0) == Lenguaje([""])
    assert len(Lenguaje(["ab", "c"]).potencia(3)) == 8
    assert l1 * Lenguaje() == Lenguaje() and l1 * Lenguaje([""]) == l1


def test_inverso_y_cerraduras_de_lenguajes():
    l = Lenguaje(["ab", "aa", "baa"])
    assert l.inverso() == Lenguaje(["ba", "aa", "aab"])
    estrella = l.estrella(6)
    assert "" in estrella and "abaab" not in estrella and "abaa" in estrella and "aabaa" in estrella
    assert "" not in l.mas(6) and l.mas(6) == estrella - Lenguaje([""])


def test_informe(tmp_path):
    informe = Informe("Prefijos de abc", ["λ", "a", "ab", "abc"], {"Palabra": "abc"})
    ruta = informe.guardar(tmp_path / "salida" / "prefijos.txt")
    texto = ruta.read_text(encoding="utf-8")
    assert "Prefijos de abc" in texto and "Total: 4" in texto and texto.rstrip().endswith("abc")
