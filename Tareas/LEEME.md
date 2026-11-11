# Tareas de Teoría de la Computación (Listas 1–4)

Rico Espluga Juan Diego · Boleta 2025630474 · Grupo 4CV4 · Docente: Gabriel Hurtado Avilés

| Carpeta | Ejercicios | Páginas | Archivos .jff |
|---|---|---|---|
| `tarea1/` | Lista 1 (1–93): alfabetos, palabras, lenguajes, gramáticas | 27 | 25 |
| `tarea2/` | Lista 2 (94–150): AFD | 67 | 62 |
| `tarea3/` | Lista 3 (151–263): AFN, AFN-λ, subconjuntos, minimización | 121 | 121 |
| `tarea4/` | Lista 4 (264–308): expresiones regulares, Kleene, bombeo, aplicaciones, gramáticas | 82 | 118 |

Cada carpeta contiene:

- `tareaN.pdf`: la tarea compilada (enunciado, procedimiento y respuesta de cada ejercicio).
- `tareaN.tex` y `preambulo.tex`: el código LaTeX.
- `jff/`: un archivo de JFLAP por cada autómata (*Finite Automaton*), expresión regular (*Regular Expression*; λ se escribe `!`) y gramática (*Grammar*).
- `img/`: las capturas de JFLAP (y los logos de la portada).

## Capturas de JFLAP

Todas las capturas ya están en `img/` y dentro del PDF. Se generaron con JFLAP 7.1:

- **Autómatas:** *Input → Multiple Run* con 3 cadenas aceptadas y 3 rechazadas. Debajo de cada captura, el PDF lista esas cadenas.
- **Gramáticas:** *Input → Multiple Brute Force Parse*. Cuando la fuerza bruta no termina con las cadenas rechazadas (por ejemplo, con S → SS | λ), se usa *Multiple CYK Parse*.
- **Expresiones regulares:** la ventana de la expresión. Su AFD tiene su propio archivo y su propio Multiple Run.

Algunos lenguajes no tienen 3 cadenas de cada lado: el lenguaje vacío, Σ* o lenguajes finitos pequeños. En esos casos se usan todas las que hay, y el PDF dice «ninguna» cuando no hay.

Junto a cada `.jff` hay un archivo `<nombre>-entradas.txt` con las mismas cadenas. En JFLAP, *Multiple Run → Load Inputs* lo carga para repetir la corrida en vivo.

## Cómo reemplazar una captura

1. Guarde la nueva imagen en `img/` con el mismo nombre que el `.jff` y extensión `.png`.
2. Vuelva a compilar dentro de la carpeta de la tarea:

   ```
   xelatex tareaN.tex
   xelatex tareaN.tex
   ```
