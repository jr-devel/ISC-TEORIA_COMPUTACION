# Práctica 1. Operaciones Básicas sobre Lenguajes

| | |
|---|---|
| **Alumno** | Rico Espluga Juan Diego |
| **Boleta** | 2025630474 |
| **Grupo** | 4CV4 |
| **Carrera** | Ingeniería en Sistemas Computacionales (Plan 2020) |
| **Unidad de aprendizaje** | Teoría de la Computación |
| **Profesor** | Gabriel Hurtado Avilés |
| **Fecha de entrega** | 22 de septiembre de 2026 |

Instituto Politécnico Nacional · Escuela Superior de Cómputo

Reporte en PDF: [`reporte/main.pdf`](reporte/main.pdf) (fuente LaTeX en `reporte/`).

## Índice

1. [Entorno de trabajo: control de versiones y contenedores](docs/01-entorno.md)
2. [Investigación: qué es la Teoría de la Computación](docs/02-investigacion.md)
3. [Estado del arte: cinco artículos](docs/03-estado-del-arte.md)
4. [Autómatas finitos en JFLAP](docs/04-jflap.md) · [Anexo A: fichas de diseño](docs/anexo-a.md)
5. [Aplicación con interfaz gráfica](docs/05-aplicacion.md)
6. [Conclusiones](docs/conclusiones.md)
7. [Bibliografía](docs/bibliografia.md)

## Estructura

```text
practica1-tc/
├── README.md  .gitignore  requirements.txt  pytest.ini
├── docs/                    # un documento por ejercicio, conclusiones y bibliografía
├── entorno/                 # Dockerfile y compose.yml
├── automatas/lista2/ lista3/  pruebas.json   # AFD de los ejercicios con asterisco
├── src/
│   ├── app.py               # punto de entrada de la interfaz
│   ├── nucleo/              # lenguajes.py y errores.py (sin dependencias de Flet)
│   └── interfaz/            # Flet: ventana, componentes y secciones
├── tests/                   # test_lenguajes.py (34) y test_interfaz.py
├── evidencias/git/ docker/ jflap/ app/
└── reporte/                 # LaTeX y PDF
```

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
| **Palabras** | prefijos, sufijos, subcadenas, reflexión y potencia, calculados al escribir; *Guardar .txt*. |
| **Cerraduras** | Σ*, Σ⁺ y Σⁿ hasta la longitud elegida; el contador avisa antes de pasar de 200 000 cadenas. |
| **Lenguajes** | unión, intersección, diferencia, concatenación, potencia, reflexión y cerraduras de lenguajes finitos. |
