# Ejercicio 1. Entorno de trabajo y flujo de ramas

## Lo que se reutiliza

El repositorio `practica2-tc` parte de la Práctica 1: la carpeta `entorno/` (el `Dockerfile` parametrizado y el `compose.yml` con los servicios `py311`, `py312` y `py313`), `requirements.txt` y `pytest.ini`. Sólo cambian los nombres de los contenedores (`tc_p2_py311`, …) para que puedan convivir con los de la práctica anterior.

El módulo `src/nucleo/lenguajes.py`, junto con `errores.py` y sus pruebas (`tests/test_lenguajes.py`), se copió **sin modificaciones** de la Práctica 1, como pide el enunciado; el `README` lo indica y enlaza el repositorio `practica1-tc`. La interfaz conserva las secciones *Palabras*, *Cerraduras* y *Lenguajes* y agrega las de esta práctica.

## Una rama por funcionalidad

Ninguna confirmación se hizo directamente sobre `main`: cada funcionalidad se desarrolló en su rama y se integró con un Pull Request que describe el cambio y muestra el resultado de las pruebas. La rama `main` se protegió en *Settings → Branches* para que GitHub rechace los `push` directos.

| Rama                           | Qué integra                                                                                        |
|--------------------------------|----------------------------------------------------------------------------------------------------|
| `feature/entorno-ci`           | Entorno copiado de la Práctica 1 y flujo de GitHub Actions.                                        |
| `feature/nucleo-automatas`     | `automata.py`: `Automata`, `AFNLambda`, `AFN`, `AFD`, `Simulacion` y `Recorrido`, con sus pruebas. |
| `feature/formatos`             | `formatos.py`: serializadores `.jff`, `.json` y `.xml` y pruebas de ida y vuelta.                  |
| `feature/editor`               | Sección *Editor*: quíntupla, tabla de transiciones y vista previa.                                 |
| `feature/biblioteca-simulador` | Secciones *Biblioteca* y *Simulador*, con la ejecución paso a paso.                                |
| `feature/fantasma-pacman`      | Ejercicio 5: el modelo del fantasma, sus archivos y sus pruebas.                                   |
| `feature/automatas-listas`     | Los 140 autómatas de las Listas 2 y 3 en tres formatos y su prueba.                                |

Ramas fusionadas.

## Integración continua

`.github/workflows/pruebas.yml` es el flujo del Anexo 2: en cada `push` y en cada Pull Request, la matriz crea tres trabajos independientes, uno por versión de Python, y `fail-fast: false` evita que el fallo de una versión cancele las otras (GitHub Inc., 2026). La suite tiene 404 pruebas aprobadas y 2 omitidas (las de secciones de prácticas posteriores):

| Archivo              | Pruebas | Qué comprueba                                                                                              |
|----------------------|:-------:|------------------------------------------------------------------------------------------------------------|
| `test_lenguajes.py`  |   34    | Operaciones de la Práctica 1 (sin cambios).                                                                |
| `test_automata.py`   |   34    | Clasificación, AFD, AFN, cerradura λ, simulación paso a paso y validación de la quíntupla.                 |
| `test_formatos.py`   |   24    | Ida y vuelta en los tres formatos, lectura del esquema del Anexo 3 y archivos dañados.                     |
| `test_listas.py`     |   281   | Cada autómata de las listas acepta sus válidas, rechaza sus inválidas y se lee igual en los tres formatos. |
| `test_aplicacion.py` |   20    | Modelo del Ejercicio 5 y sus quince cadenas.                                                               |
| `test_interfaz.py`   |   13    | Cada sección se construye y responde sin abrir una ventana.                                                |

Composición de la suite.

![`git log --oneline --graph --all` con las fusiones de las ramas.](../evidencias/git/git-log-graph.png)

![Pull Requests cerrados.](../evidencias/git/pull-requests.png)

![GitHub Actions: los tres trabajos de la matriz aprobados.](../evidencias/ci/actions.png)
