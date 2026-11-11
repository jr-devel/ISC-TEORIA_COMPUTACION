# Práctica 2. Autómatas Finitos No Deterministas (AFND) y Simulación de AFD con Interfaz Gráfica

| | |
|---|---|
| **Alumno** | Rico Espluga Juan Diego |
| **Boleta** | 2025630474 |
| **Grupo** | 4CV4 |
| **Carrera** | Ingeniería en Sistemas Computacionales (Plan 2020) |
| **Unidad de aprendizaje** | Teoría de la Computación |
| **Profesor** | Gabriel Hurtado Avilés |
| **Fecha de entrega** | 6 de octubre de 2026 |

Instituto Politécnico Nacional · Escuela Superior de Cómputo

Reporte en PDF: [`reporte/main.pdf`](reporte/main.pdf) (fuente LaTeX en `reporte/`).

## Índice

1. [Entorno de trabajo y flujo de ramas](docs/01-entorno.md)
2. [AFND y AFND-λ en JFLAP](docs/02-jflap.md)
3. [Simulador de autómatas con interfaz gráfica](docs/03-simulador.md)
4. [Investigación y estado del arte](docs/04-investigacion.md)
5. [Del artículo al autómata](docs/05-del-articulo-al-automata.md)
6. [Propuesta de trabajo](docs/propuesta.md)
7. [Conclusiones](docs/conclusiones.md) · [Bibliografía](docs/bibliografia.md)
8. Anexos: [clasificación, cerraduras λ y conversiones](docs/anexos.md) · [fichas de los 140 autómatas](docs/fichas.md) · [recorridos de cada cadena](docs/recorridos/)

## Procedencia del código

`src/nucleo/lenguajes.py`, `src/nucleo/errores.py` y `tests/test_lenguajes.py` proceden de la **Práctica 1** (repositorio `practica1-tc`) y se reutilizan sin cambios; también `entorno/`, `requirements.txt` y `pytest.ini`.

## Estructura

```text
practica2-tc/
├── README.md  .gitignore  requirements.txt  pytest.ini
├── .github/workflows/pruebas.yml        # pruebas con Python 3.11, 3.12 y 3.13
├── docs/
├── entorno/
├── automatas/
│   ├── afd/  afnd/  afnd-lambda/        # .jff, .json y .xml de cada ejercicio, por clase
│   ├── conversiones/                    # AFN sin λ, AFD y AFD mínimos
│   ├── aplicacion/                      # Ejercicio 5: fantasma de Pac-Man y sus cadenas
│   └── pruebas.json                     # cadenas de prueba de cada autómata
├── src/nucleo/   lenguajes.py  automata.py  formatos.py  errores.py
├── src/interfaz/ y src/app.py
├── tests/                               # 404 pruebas
├── evidencias/git/ ci/ jflap/ app/
└── reporte/
```

## Convención para λ y formatos

En los tres formatos la **transición λ se escribe con el símbolo vacío**: `<read/>` en `.jff`, `""` en `.json` y `simbolo=""` en `.xml`; al leer se aceptan también `λ`, `ε`, `lambda` y `eps`. El `.json` y el `.xml` usan un esquema propio (`automata-tc`, descrito en `docs/03-simulador.md`) que agrupa δ por estado y símbolo; los lectores aceptan además el esquema de ejemplo del Anexo 3. El `.jff` no guarda Σ: se infiere de las transiciones.

## Entorno y pruebas

```bash
cd entorno
docker compose build                              # construye las tres imágenes
docker compose run --rm py311 python --version    # 3.11.x (igual con py312 y py313)
docker compose run --rm py311 pytest -q
docker compose run --rm py312 pytest -q
docker compose run --rm py313 pytest -q
docker compose up py312                           # interfaz en http://localhost:8550
docker compose down
```

Sin contenedores: `python -m venv venv`, activar el entorno, `pip install -r requirements.txt`, `pytest -q` y `python src/app.py` (abre la ventana de escritorio).
Versiones: Python 3.11, 3.12 y 3.13 · Flet 0.86.5 · FastAPI 0.115.12 (fijada porque `flet-web` 0.86.5 no funciona con versiones posteriores) · pytest 8.3.4.
Si usa Podman, sustituya `docker` por `podman` en todas las órdenes.

Variables opcionales al abrir la interfaz: `TC_SECCION=<clave>` abre directamente una sección y `TC_AUTOMATA=<ruta>` carga un autómata al iniciar (por ejemplo `TC_AUTOMATA=automatas/... python src/app.py`).

## Uso de la interfaz

La ventana tiene un menú lateral con las secciones; cada una explica sus pasos con el botón **¿Cómo se usa?**. Arriba a la derecha se ve el autómata activo, con el que trabajan las secciones que lo necesitan.

| Sección | Qué hace |
|---|---|
| **Inicio** | accesos directos y el flujo de trabajo sugerido. |
| **Editor** | Σ, Q, q₀ y F; tabla de transiciones con destinos separados por comas (vacío = sin transición); interruptor de columna λ; vista previa con diagrama, tabla y tipo deducido. |
| **Biblioteca** | busca y abre `.jff`, `.json` o `.xml`; guarda el autómata activo en uno o en los tres formatos (carpeta `salidas/`). |
| **Simulador** | *Validar* procesa la palabra completa; *Paso a paso* y *Siguiente* leen un símbolo a la vez, con cinta, estados activos, transiciones usadas, traza y cerraduras λ. |
| **Palabras** | prefijos, sufijos, subcadenas, reflexión y potencia, calculados al escribir; *Guardar .txt*. |
| **Cerraduras** | Σ*, Σ⁺ y Σⁿ hasta la longitud elegida; el contador avisa antes de pasar de 200 000 cadenas. |
| **Lenguajes** | unión, intersección, diferencia, concatenación, potencia, reflexión y cerraduras de lenguajes finitos. |
