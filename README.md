# Teoría de la Computación — Prácticas y tareas

Aquí están las cuatro prácticas y las tareas de las Listas 1 a 4. Las prácticas son un solo programa en Python que crece de una práctica a otra: cada una agrega funciones a la anterior. Las tareas resuelven los ejercicios de las listas en LaTeX, con un archivo de JFLAP para cada autómata, expresión regular y gramática.

## Contenido

```
entrega/
├── practicas/          Las 4 prácticas (código, pruebas, autómatas, reporte y evidencias)
├── tareas/             Listas 1–4 resueltas en LaTeX, con sus .jff y capturas de JFLAP
├── capturas-jflap/     Programas que generaron automáticamente las capturas de JFLAP
├── Practica1..4_Reporte.pdf
└── Tarea1..4_Lista1..4.pdf
```

## Prácticas

| Práctica | Tema | Qué se hizo |
|---|---|---|
| **1. Operaciones básicas sobre lenguajes** | Alfabetos, palabras, lenguajes | Programa con interfaz gráfica que genera Σ*, Σ⁺ y Σⁿ, calcula prefijos, sufijos, subcadenas, inversa y potencia de palabras, y hace operaciones entre lenguajes (unión, intersección, diferencia, concatenación y cerraduras). El anexo diseña 77 AFD de las Listas 2 y 3, cada uno con su `.jff` y su corrida en JFLAP. |
| **2. AFND y simulación de AFD** | Autómatas finitos | Editor y biblioteca de autómatas en 3 formatos (`.jff`, JSON y XML), simulador paso a paso de AFD, AFN y AFN-λ, y clasificación del tipo de autómata. Como aplicación, se modela con un AFD el fantasma de Pac-Man. |
| **3. Conversión de AFD a expresiones regulares** | Teorema de Kleene (Parte II) | En JFLAP, conversión de 5 AFD a expresión regular eliminando estados y comprobación de equivalencia. En el programa se agregan la eliminación de λ, la construcción de subconjuntos, la minimización, la prueba de equivalencia entre autómatas y la validación de cadenas por lotes. |
| **4. Uso de expresiones regulares** | Teorema de Kleene (ambas partes) | Analizador de expresiones regulares, construcción de Thompson (expresión → AFN-λ → AFD mínimo), conversión de AFD a expresión regular (eliminación de estados y lema de Arden) y validadores de correo, teléfono y URL, comparados con el módulo `re` de Python. |

Cada carpeta `practicaN/` contiene:

- `src/`: el código; `nucleo/` tiene los algoritmos y `interfaz/`, la aplicación hecha con Flet.
- `tests/`: las pruebas con pytest. Pasan todas en Python 3.11, 3.12 y 3.13.
- `automatas/`: los `.jff` y los casos de prueba.
- `reporte/`: el reporte en LaTeX y su PDF (`main.pdf`).
- `evidencias/`: las capturas del programa y de JFLAP.
- `docs/`: el reporte también en Markdown.
- `entorno/` (`Dockerfile` y `compose.yml`) y `.github/`: Docker y la integración continua.
- `README.md`: las instrucciones propias de esa práctica.

### Cómo ejecutar

```
cd practicas/practica4
python -m venv venv
venv\Scripts\activate          # en Linux o macOS: source venv/bin/activate
pip install -r requirements.txt
pytest -q                       # pruebas
python src/app.py               # abre la aplicación
```

Con Docker, desde `entorno/`: `docker compose run --rm py312 pytest -q` corre las pruebas, y `docker compose up py312` deja la interfaz en http://localhost:8550.

## Tareas

| Tarea | Ejercicios | Tema | Páginas | `.jff` |
|---|---|---|---|---|
| 1 | Lista 1 (1–93) | Alfabetos, palabras, lenguajes y gramáticas (incluye gramáticas sin restricciones como aⁿbⁿcⁿ) | 27 | 25 |
| 2 | Lista 2 (94–150) | Diseño de AFD | 67 | 62 |
| 3 | Lista 3 (151–263) | AFN y AFN-λ, cerraduras, construcción de subconjuntos y minimización | 121 | 121 |
| 4 | Lista 4 (264–308) | Expresiones regulares, teorema de Kleene, lema de bombeo, autómatas aplicados y gramáticas | 82 | 118 |

Cada ejercicio tiene su enunciado, su procedimiento y su respuesta. Cada autómata y cada gramática traen su captura de JFLAP con Multiple Run de 3 cadenas aceptadas y 3 rechazadas. Junto a cada `.jff` hay un archivo `-entradas.txt` con esas mismas cadenas, para repetir la corrida en JFLAP con *Load Inputs*. Los detalles están en `tareas/LEEME.md`.

## Capturas de JFLAP

Todas las capturas se generaron con JFLAP 7.1 usando sus propias clases, sin hacer capturas de pantalla a mano. En cada una se comparó la respuesta de JFLAP con el resultado esperado, y todas coinciden. Los programas están en `capturas-jflap/` (ver su `LEEME.md`) y necesitan `JFLAP7.1.jar`, que no se incluye.

## Pendiente

Faltan las capturas de Git, de la integración continua (GitHub Actions) y de Docker en los reportes de las prácticas. Se guardan en la carpeta `evidencias/` de cada práctica con el nombre que indica el recuadro «Captura pendiente», y después se vuelve a compilar el reporte.
