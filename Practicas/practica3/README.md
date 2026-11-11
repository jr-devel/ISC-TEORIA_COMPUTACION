# Práctica 3. Conversión de AFD a Expresiones Regulares y Algoritmos sobre Autómatas

| | |
|---|---|
| **Alumno** | Rico Espluga Juan Diego |
| **Boleta** | 2025630474 |
| **Grupo** | 4CV4 |
| **Carrera** | Ingeniería en Sistemas Computacionales (Plan 2020) |
| **Unidad de aprendizaje** | Teoría de la Computación |
| **Profesor** | Gabriel Hurtado Avilés |
| **Fecha de entrega** | 4 de noviembre de 2026 |

Instituto Politécnico Nacional · Escuela Superior de Cómputo

Reporte en PDF: [`reporte/main.pdf`](reporte/main.pdf) (fuente LaTeX en `reporte/`).

## Práctica 3 (etiqueta `practica3`)

1. [Conversión de AFD a expresiones regulares (JFLAP y a mano)](docs/practica3/01-afd-a-er-jflap.md)
2. [Extensión del software](docs/practica3/02-software.md)
3. [Documentación de los algoritmos](docs/practica3/03-algoritmos.md)
4. [Conclusiones](docs/practica3/conclusiones.md) · [Bibliografía](docs/practica3/bibliografia.md)

### Funciones nuevas

- **Transformaciones**: active un autómata (Editor o Biblioteca), elija la etapa y recórrala con *Anterior/Siguiente*.
- **Equivalencia**: elija dos autómatas y pulse *Comparar*.
- **Validación por lotes**: cargue `automatas/practica3/cadenas-ejemplo.txt` o escriba palabras, *Validar todo* y *Guardar informe*.
- **Simulador**: ahora muestra la tabla de cerraduras λ y, en cada paso, el conjunto antes y después de cerrar.

Todos los algoritmos están en `src/nucleo/algoritmos.py` y se ejecutan sin abrir la interfaz:

```python
from nucleo.formatos import Archivos
from nucleo.algoritmos import HaciaMinimo
cadena = HaciaMinimo(Archivos.abrir("automatas/practica3/casos-de-prueba/lista3-199.jff")).resolver()
print(cadena.afd_minimo.tabla_texto())
```

```text
automatas/practica3/afd-a-er/          # los cinco AFD del Ejercicio 1
automatas/practica3/casos-de-prueba/   # Lista 3: 151–157, 192–200, 260–263
docs/practica3/  src/  tests/  evidencias/practica3/  reporte/
```

**Fecha de entrega:** 4 de noviembre de 2026.

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
| **Transformaciones** | quitar λ, construcción de subconjuntos y minimización (tabla de pares), cada una paso a paso; *Usar resultado* y *Guardar .jff*. |
| **Equivalencia** | compara dos autómatas por sus AFD mínimos; muestra la correspondencia o el contraejemplo más corto. |
| **Validación por lotes** | una palabra por línea (`#` comenta, `λ` es la palabra vacía); tabla de resultados e informe en `salidas/`. |
| **Palabras** | prefijos, sufijos, subcadenas, reflexión y potencia, calculados al escribir; *Guardar .txt*. |
| **Cerraduras** | Σ*, Σ⁺ y Σⁿ hasta la longitud elegida; el contador avisa antes de pasar de 200 000 cadenas. |
| **Lenguajes** | unión, intersección, diferencia, concatenación, potencia, reflexión y cerraduras de lenguajes finitos. |
