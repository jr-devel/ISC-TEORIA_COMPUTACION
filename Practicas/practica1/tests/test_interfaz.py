"""Pruebas de humo de la interfaz: cada sección se construye y responde sin abrir una ventana.

Las secciones se crean con una sesión real (carpeta automatas/ del proyecto) y se
ejercitan sus acciones principales llamando a los mismos métodos que los botones.
Como no hay página, ``refrescar`` no hace nada; lo que se comprueba es que la
lógica de la interfaz no lanza excepciones y deja el estado esperado.
"""

import pytest

flet = pytest.importorskip("flet")

from conftest import AUTOMATAS, RAIZ  # noqa: E402
from interfaz.sesion import Sesion  # noqa: E402
from interfaz.vistas import base  # noqa: E402

VISTAS = []
for modulo, clase in [("inicio", "Inicio"), ("cadenas", "Cadenas"), ("cerraduras", "Cerraduras"),
                      ("lenguajes", "Lenguajes"), ("editor", "Editor"), ("biblioteca", "Biblioteca"),
                      ("simulador", "Simulador"), ("transformar", "Transformar"), ("equivalencia", "Equivalencia"),
                      ("lote", "Lote"), ("expresion", "Expresion"), ("automata_a_er", "AutomataAER"),
                      ("validadores", "Validadores")]:
    try:
        VISTAS.append(getattr(__import__(f"interfaz.vistas.{modulo}", fromlist=[clase]), clase))
    except ImportError:          # la sección no forma parte de esta práctica
        pass


@pytest.fixture
def sesion(tmp_path):
    s = Sesion(RAIZ)
    s.salidas = tmp_path
    s.secciones = [(v.CLAVE, v.TITULO, v.ICONO, v.DESCRIPCION) for v in VISTAS]
    return s


def montar(clase, sesion):
    vista = clase(sesion)
    vista.control()
    vista.al_mostrar()
    return vista


@pytest.mark.parametrize("clase", VISTAS, ids=lambda c: c.CLAVE)
def test_cada_seccion_se_construye(clase, sesion):
    vista = montar(clase, sesion)
    assert isinstance(vista, base.Vista) and vista.TITULO and vista.DESCRIPCION
    assert vista.CLAVE == "inicio" or len(vista.PASOS) >= 3


def test_errores_se_muestran_como_aviso(sesion):
    vista = montar(VISTAS[0], sesion)
    vista.ejecutar(lambda: (_ for _ in ()).throw(base.ErrorTC("mensaje de prueba")))
    assert vista.aviso.visible and "mensaje de prueba" in vista.aviso._texto.value


def buscar(nombre):
    return next(c for c in VISTAS if c.__name__ == nombre)


def test_palabras_y_cerraduras(sesion):
    cadenas = montar(buscar("Cadenas"), sesion)
    cadenas.palabra.value = "abc"
    cadenas.operacion.selected = ["subcadenas"]
    cadenas.calcular()
    assert len(cadenas._informe.elementos) == 7
    cadenas.ejecutar(cadenas.guardar)
    assert (sesion.salidas / "palabras-subcadenas.txt").is_file()
    cadenas.palabra.value = "abz"
    cadenas.calcular()
    assert "z" in cadenas.palabra.error

    cerraduras = montar(buscar("Cerraduras"), sesion)
    cerraduras.longitud.value = 17
    cerraduras.prever()
    assert cerraduras.generar_btn.disabled
    cerraduras.longitud.value = 3
    cerraduras.prever()
    cerraduras.ejecutar(cerraduras.generar)
    assert len(cerraduras._informe.elementos) == 15


def test_lenguajes(sesion):
    vista = montar(buscar("Lenguajes"), sesion)
    vista.operacion.value = "concatenacion"
    vista.calcular()
    assert len(vista._informe.elementos) == 5


@pytest.mark.skipif(not any(c.__name__ == "Editor" for c in VISTAS), reason="sin autómatas en esta práctica")
def test_editor_simulador_y_biblioteca(sesion):
    editor = montar(buscar("Editor"), sesion)
    editor.cargar_ejemplo("lambda")
    editor.ejecutar(editor.usar)
    assert sesion.automata.tipo == "AFN-λ" and sesion.automata.nombre == "ejemplo-lambda"

    simulador = montar(buscar("Simulador"), sesion)
    simulador.palabra.value = "aab"
    simulador.ejecutar(simulador.validar)
    assert simulador.veredicto.visible and simulador._sim.recorrido.aceptada
    simulador.ejecutar(simulador.preparar)
    simulador.ejecutar(simulador.avanzar)
    assert simulador._sim.indice == 1

    biblioteca = montar(buscar("Biblioteca"), sesion)
    biblioteca.nombre.value = "copia"
    biblioteca.ejecutar(lambda: biblioteca.guardar(None))
    assert sorted(p.suffix for p in sesion.salidas.glob("copia.*")) == [".jff", ".json", ".xml"]
    biblioteca.ejecutar(lambda: biblioteca.previsualizar(sesion.salidas / "copia.json"))
    biblioteca.ejecutar(biblioteca.usar)
    assert sesion.automata.nombre == "ejemplo-lambda"


@pytest.mark.skipif(not any(c.__name__ == "Transformar" for c in VISTAS), reason="sección de la Práctica 3")
def test_transformaciones_equivalencia_y_lote(sesion):
    from nucleo.formatos import Archivos
    m = Archivos.abrir(AUTOMATAS / "practica3" / "casos-de-prueba" / "lista3-199.jff")
    sesion.usar(m)
    vista = montar(buscar("Transformar"), sesion)
    assert all(vista._resultados[k] is not None for k in ("lambda", "subconjuntos", "minimo"))
    vista.selector.selected = ["minimo"]
    vista._mostrar_etapa(refrescar=False)
    vista.visor.mover(1)
    assert vista.visor.indice == 1
    vista.ejecutar(vista.guardar)
    assert list(sesion.salidas.glob("*.jff"))

    equivalencia = montar(buscar("Equivalencia"), sesion)
    equivalencia.segundo.value = str(AUTOMATAS / "practica3" / "casos-de-prueba" / "lista3-199.jff")
    equivalencia.ejecutar(equivalencia.comparar)
    assert "EQUIVALENTES" in equivalencia.veredicto._titulo.value

    lote = montar(buscar("Lote"), sesion)
    lote.texto.value = "01\n0\nλ\n"
    lote.ejecutar(lote.validar)
    assert len(lote._filas) == 3
    lote.ejecutar(lote.guardar)


@pytest.mark.skipif(not any(c.__name__ == "Expresion" for c in VISTAS), reason="sección de la Práctica 4")
def test_expresiones_y_validadores(sesion):
    vista = montar(buscar("Expresion"), sesion)
    vista.entrada.value = "(a + b"
    assert vista.revisar(refrescar=False) is None and vista.marca.visible
    vista.entrada.value = "(ab)*a"
    vista.ejecutar(vista.construir)
    assert len(vista._thompson.etapas) == 6
    vista.palabra.value = "aba"
    vista.ejecutar(vista.probar)
    assert vista.veredicto._titulo.value == "ACEPTADA"
    vista.ejecutar(vista.guardar_todas)

    a_er = montar(buscar("AutomataAER"), sesion)
    a_er.fuente.value = str(AUTOMATAS / "practica4" / "casos-de-prueba" / "lista4-276.jff")
    a_er.ejecutar(a_er.revisar)
    a_er.ejecutar(a_er.convertir)
    assert a_er._expresion is not None
    a_er.otra.value = "(b + ab*ab*a)*"
    a_er.ejecutar(a_er.comparar)
    assert a_er.veredicto._titulo.value == "EQUIVALENTES"

    validadores = montar(buscar("Validadores"), sesion)
    validadores.texto.value = "no es correo"
    validadores.validar(refrescar=False)
    assert validadores.veredicto._titulo.value == "INVÁLIDO"
