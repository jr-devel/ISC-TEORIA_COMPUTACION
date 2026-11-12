# Teoría de la Computación — Prácticas y tareas

| | |
|---|---|
| **Alumno** | Rico Espluga Juan Diego |
| **Boleta** | 2025630474 |
| **Grupo** | 4CV4 |
| **Profesor** | Gabriel Hurtado Avilés |
| **Escuela** | ESCOM-IPN |

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

## Uso paso a paso

Al abrir la aplicación (`python src/app.py`), el menú de la izquierda muestra las secciones de esa práctica. Cada sección tiene el botón **«¿Cómo se usa?»** con sus pasos. Los resultados que se guardan van a la carpeta `salidas/`.

Varias secciones trabajan sobre el **autómata activo**, cuyo nombre aparece arriba a la derecha. Se activa desde el **Editor** («Usar este autómata») o desde la **Biblioteca** («Usar»).

### Práctica 1. Operaciones sobre palabras y lenguajes

**Palabras**
1. Escriba el alfabeto, por ejemplo `a, b` o `ab`.
2. Escriba una palabra, como `abba`. Si usa un símbolo que no está en Σ, el campo se marca en rojo.
3. Elija la operación en la barra: prefijos, sufijos, subcadenas, reflexión o potencia. El resultado aparece solo.
4. Pulse «Guardar .txt» para guardar el resultado.

**Cerraduras**
1. Escriba el alfabeto.
2. Mueva el control de longitud máxima n. El contador indica cuántas cadenas se generarían.
3. Elija Σ*, Σ⁺ o Σⁿ y pulse «Generar». Si el total pasa de 200 000 cadenas, el botón se desactiva.
4. «Guardar .txt» escribe la lista completa.

**Lenguajes**
1. Escriba L₁ y L₂ separando las palabras con comas, por ejemplo `a, ab, λ`.
2. Elija la operación: unión, intersección, diferencia, concatenación, potencia, inverso, L* o L⁺.
3. Para la potencia y las cerraduras, indique n.

Los 77 AFD del anexo están en `automatas/lista2/` y `automatas/lista3/` y se abren con JFLAP (*File → Open*).

### Práctica 2. Autómatas y simulación

Incluye todo lo de la Práctica 1, más estas secciones:

**Editor** (crear un autómata)
1. Escriba Σ y Q separados por comas, por ejemplo `0, 1` y `q0, q1, q2`.
2. Elija el estado inicial y toque las pastillas de los estados de aceptación.
3. Llene la tabla: en cada celda van los destinos separados por comas; una celda vacía significa que no hay transición.
4. Active «Transiciones λ» si las necesita. El tipo (AFD, AFN o AFN-λ) se deduce solo.
5. Pulse «Usar este autómata».

**Biblioteca** (abrir un autómata)
1. Escriba en el buscador parte del nombre, por ejemplo `196`.
2. Toque el archivo para ver su quíntupla, su diagrama y su tabla, y pulse «Usar».
3. Para guardarlo, elija un nombre y un formato (`.jff`, JSON o XML) en «Guardar».

**Simulador**
1. Con un autómata activo, escriba la palabra (`λ` o nada para la palabra vacía).
2. «Validar» la recorre completa. «Paso a paso» y luego «Siguiente» leen un símbolo a la vez.
3. Los estados activos se resaltan en el diagrama y en la tabla. En un AFN o AFN-λ se ve el conjunto de estados activos.

Ejemplo: abra `aplicacion/fantasma-pacman` en la Biblioteca, pulse «Usar» y simule `lveax` (aceptada) o `lve` (rechazada).

### Práctica 3. Transformaciones, equivalencia y lotes

Incluye todo lo de la Práctica 2, más:

**Transformaciones** (AFN-λ → AFN → AFD → AFD mínimo)
1. Active un autómata, por ejemplo `lista3-196` (un AFN-λ).
2. Elija la etapa en la barra superior: quitar λ, subconjuntos o minimización. Las que no hacen falta aparecen como «no aplica».
3. Avance con «Anterior» y «Siguiente»; cada paso trae su explicación y su tabla.
4. «Usar resultado» vuelve activo el autómata obtenido y «Guardar .jff» lo guarda.

**Equivalencia**
1. Elija el primer autómata (puede ser el activo) y el segundo de la biblioteca.
2. Pulse «Comparar». Si son equivalentes, se muestra la correspondencia entre estados. Si no, aparece la palabra más corta que uno acepta y el otro no.

**Validación por lotes**
1. Active `lista3-263` (las palabras que terminan en 01).
2. En «Archivo .txt» ya viene escrita la ruta `automatas/practica3/cadenas-ejemplo.txt`; pulse «Cargar archivo». También puede escribir las palabras directamente, una por línea.
3. Pulse «Validar todo» y después «Guardar informe».

La parte de JFLAP (convertir los AFD de `automatas/practica3/afd-a-er/` a expresión regular) se hace en JFLAP con *Convert → Convert FA to RE*.

### Práctica 4. Expresiones regulares

Incluye todo lo de la Práctica 3, más:

**ER → AFD**
1. Escriba la expresión: `+` es unión, escribir seguido concatena, `*` es la estrella, y `λ` y `∅` son la palabra vacía y el lenguaje vacío. Ejemplo: `(a + b)*abb`.
2. Si hay un error de sintaxis, se señala con `^` bajo el carácter que lo provoca.
3. Pulse «Construir» y recorra las etapas: los casos básicos, uniones, concatenaciones y estrellas de Thompson, y después el AFD mínimo.
4. Pruebe palabras abajo. Cada una se valida con el AFD y se compara con `re.fullmatch` de Python.
5. «Guardar .jff» exporta el autómata de la etapa elegida y «Usar» lo vuelve el autómata activo.

**AFD → ER**
1. Elija el AFD, por ejemplo `lista4-276` de `automatas/practica4/casos-de-prueba/`.
2. Elija el método: eliminación de estados o lema de Arden. En la eliminación puede fijar el orden (por ejemplo `B, C, A`) o dejarlo vacío para que el programa lo elija.
3. Recorra los pasos. Después de cada eliminación se muestra el autómata generalizado como tabla.
4. Para comparar con JFLAP, pegue la expresión de JFLAP en «Comparar con» y pulse el botón. Ambas expresiones se convierten en AFD mínimos y se prueban por equivalencia.

**Validadores**
1. Elija correo, teléfono o URL en la barra.
2. Escriba un texto. Se valida mientras escribe y se indica dónde falla.
3. Toque un ejemplo para probarlo. Abajo se listan los casos que la expresión deja fuera a propósito.

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
