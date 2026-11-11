# Práctica 4. Uso de las Expresiones Regulares y Extensión de Software para Convertir Expresiones Regulares

| | |
|---|---|
| **Alumno** | Rico Espluga Juan Diego |
| **Boleta** | 2025630474 |
| **Grupo** | 4CV4 |
| **Carrera** | Ingeniería en Sistemas Computacionales (Plan 2020) |
| **Unidad de aprendizaje** | Teoría de la Computación |
| **Profesor** | Gabriel Hurtado Avilés |
| **Fecha de entrega** | 6 de noviembre de 2026 |

Instituto Politécnico Nacional · Escuela Superior de Cómputo

Reporte en PDF: [`reporte/main.pdf`](reporte/main.pdf) (fuente LaTeX en `reporte/`).

## Práctica 4 (etiqueta `practica4`)

1. [Investigación sobre expresiones regulares](docs/practica4/01-investigacion.md)
2. [De expresión regular a autómata](docs/practica4/02-er-a-afd.md)
3. [De autómata a expresión regular](docs/practica4/03-afd-a-er.md)
4. [Validadores](docs/practica4/04-validadores.md)
5. [Conclusiones](docs/practica4/conclusiones.md) · [Bibliografía](docs/practica4/bibliografia.md)

### Notación aceptada por el analizador

| Escritura | Significado |
|---|---|
| `a`, `0`, `@`… | símbolo (cualquier carácter que no sea operador) |
| `\x` | el carácter `x` literal aunque sea operador (`\+`, `\(`) |
| `λ` o `ε` · `∅` o `Ø` | palabra vacía · lenguaje vacío |
| `r + s` · `rs` · `r*` · `( r )` | unión · concatenación · estrella · agrupación |
| `[D]` `[m]` `[M]` `[L]` `[X]` | dígitos · minúsculas · mayúsculas · letras · letras y dígitos |

Precedencia: `*` > concatenación > `+`. Los espacios se ignoran. Un error se informa con la posición del carácter (desde 1).

### Funciones nuevas

- **ER → AFD**: escriba la expresión (o elija un caso de prueba), *Construir*, recorra las etapas y exporte con *Guardar .jff* / *Guardar las cuatro*. Abajo, pruebe palabras.
- **AFD → ER**: elija un AFD, el método y, si quiere, el orden; *Obtener la expresión*; pegue otra expresión en *Comparar con* para decidir si son equivalentes.
- **Validadores**: elija correo, teléfono o URL y escriba el texto.

```text
automatas/practica4/casos-de-prueba/   # Lista 3: 254–258; Lista 4: 276, 277; un AFN para el aviso de no determinismo
automatas/practica4/expresiones.txt    # expresiones de Lista 3 (241–253) y Lista 4 (272, 278)
automatas/practica3/afd-a-er/          # los cinco AFD del Ejercicio 1 de la Práctica 3
```

**Fecha de entrega:** 6 de noviembre de 2026.

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
| **ER → AFD** | analiza la expresión mientras se escribe (errores con posición), construye el AFN-λ por partes y lo lleva al AFD mínimo; exporta cada etapa a `.jff` y prueba palabras contra el AFD y `re.fullmatch`. |
| **AFD → ER** | verifica el determinismo, elimina estados paso a paso (orden propio o automático) o aplica el lema de Arden, y compara con otra expresión (por ejemplo, la de JFLAP). |
| **Validadores** | correo, teléfono y URL: expresión del curso, traducción a `re`, AFD mínimo y validación en vivo. |
| **Palabras** | prefijos, sufijos, subcadenas, reflexión y potencia, calculados al escribir; *Guardar .txt*. |
| **Cerraduras** | Σ*, Σ⁺ y Σⁿ hasta la longitud elegida; el contador avisa antes de pasar de 200 000 cadenas. |
| **Lenguajes** | unión, intersección, diferencia, concatenación, potencia, reflexión y cerraduras de lenguajes finitos. |
