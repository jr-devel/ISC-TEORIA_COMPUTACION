# Ejercicio 4. Autómatas finitos en JFLAP

## Método de diseño

Todos los autómatas se diseñaron con la misma pregunta: *¿qué es lo mínimo que hay que recordar del prefijo leído para decidir el resto?* La respuesta define los estados; la función de transición dice cómo cambia ese recuerdo al leer un símbolo, y los estados de aceptación son aquellos cuyo recuerdo ya garantiza que la cadena pertenece al lenguaje. Cuatro familias de enunciados cubren casi todas las listas:

| Familia               | Qué guarda cada estado                                                                   | Ejemplos           |
|-----------------------|------------------------------------------------------------------------------------------|--------------------|
| Conteo módulo k       | El residuo de una longitud, de un número de apariciones o del valor numérico leído       | 097, 139, 145, 147 |
| Búsqueda de patrones  | El sufijo más largo leído que es prefijo del patrón (construcción de Knuth-Morris-Pratt) | 099, 102, 103, 106 |
| Producto de autómatas | Un par de recuerdos, uno por condición, cuando el enunciado pide «y» o «o»               | 107, 109, 133      |
| Prefijos y extremos   | Cuánto del prefijo exigido se ha leído, o el primer símbolo y el último                  | 120, 135, 137      |

Familias de diseño.

Cuando una condición ya no puede cumplirse (por ejemplo, la cadena no empieza como se exige) se usa un estado **sumidero**: no es de aceptación y todas sus transiciones vuelven a él. En los enunciados de la Lista 3 que piden un AFN, el AFD se obtuvo convirtiendo ese AFN y minimizando el resultado; su ficha indica qué estados del AFN representa cada estado del AFD.

## Implementación y validación

Cada autómata se capturó en JFLAP 7.1 y se exportó a `automatas/lista2/` y `automatas/lista3/`; los archivos `.jff` se leen también con el software del Ejercicio 5 de la Práctica 2. Se resolvieron los 77 ejercicios con asterisco que piden un autómata; los ejercicios 116 (lenguaje no regular), 143 (figuras ausentes en la lista), 191 y 201–235 no piden un AFD y se resuelven en las tareas.

Cada ficha del Anexo A tiene el diagrama en JFLAP, la tabla de transiciones —en todos los autómatas, no sólo en los cinco que pide el enunciado—, tres cadenas válidas, tres inválidas y los casos frontera: la cadena vacía, la aceptada más corta y, cuando existe, una cadena justo por debajo de esa longitud. Las cadenas se eligieron de longitudes crecientes y se comprobaron dos veces: con *Input → Multiple Run* en JFLAP y con un programa que compara cada autómata contra la definición del lenguaje sobre todas las cadenas de longitud ≤ 14 (≤ 9 con tres símbolos). El archivo `automatas/pruebas.json` reúne las cadenas de todas las fichas.

## Simulación paso a paso

La simulación paso a paso (*Input → Step with Closure*) se usó en los cinco autómatas de la tabla; cada captura muestra la configuración (estado y resto de la entrada) después de algunos pasos y el resultado final.

| Ejercicio | Lenguaje                                    | Cadena simulada | Resultado           |
|-----------|---------------------------------------------|-----------------|---------------------|
| 097       | Longitud múltiplo de 3                      | `102211`        | aceptada en r0      |
| 113       | Dos apariciones de 010, con traslape        | `01010`         | aceptada            |
| 120       | Primer y último símbolo distintos           | `2101`          | aceptada            |
| 135       | bᵐabⁿ con m, n \> 0                         | `bbab`          | aceptada            |
| 147       | Binario (izquierda a derecha) múltiplo de 6 | `1100`          | aceptada (12 = 2·6) |

Autómatas simulados paso a paso.

![JFLAP, simulación paso a paso de `102211` en lista2-097.](../evidencias/jflap/lista2-097-paso-a-paso.png)

![JFLAP, simulación paso a paso de `01010` en lista2-113.](../evidencias/jflap/lista2-113-paso-a-paso.png)

![JFLAP, simulación paso a paso de `2101` en lista2-120.](../evidencias/jflap/lista2-120-paso-a-paso.png)

![JFLAP, simulación paso a paso de `bbab` en lista2-135.](../evidencias/jflap/lista2-135-paso-a-paso.png)

![JFLAP, simulación paso a paso de `1100` en lista2-147.](../evidencias/jflap/lista2-147-paso-a-paso.png)

## Resumen de los autómatas

| Ejercicio        | Σ               | Diseño original | Estados del AFD | Archivo              |
|------------------|-----------------|-----------------|:---------------:|----------------------|
| L2 · 097         | {0, 1, 2}       | AFD             |        3        | `lista2-097.jff`     |
| L2 · 099         | {0, 1, 2}       | AFD             |        7        | `lista2-099.jff`     |
| L2 · 102         | {a, b}          | AFD             |        7        | `lista2-102.jff`     |
| L2 · 103         | {a, b}          | AFD             |        7        | `lista2-103.jff`     |
| L2 · 106         | {0, 1, 2}       | AFD             |        8        | `lista2-106.jff`     |
| L2 · 107         | {0, 1, 2}       | AFD             |       13        | `lista2-107.jff`     |
| L2 · 109         | {0, 1, a, b, c} | AFD             |       22        | `lista2-109.jff`     |
| L2 · 111         | {0, 1, 2}       | AFD             |       21        | `lista2-111.jff`     |
| L2 · 112         | {0, 1, 2}       | AFD             |        7        | `lista2-112.jff`     |
| L2 · 113         | {0, 1, 2}       | AFD             |        7        | `lista2-113.jff`     |
| L2 · 118         | {a, b}          | AFD             |        6        | `lista2-118.jff`     |
| L2 · 120         | {0, 1, 2}       | AFD             |        7        | `lista2-120.jff`     |
| L2 · 121         | {0, 1, 2}       | AFD             |        6        | `lista2-121.jff`     |
| L2 · 122         | {0, 1, 2}       | AFD             |        4        | `lista2-122.jff`     |
| L2 · 123         | {a, b}          | AFD             |       15        | `lista2-123.jff`     |
| L2 · 124         | {0, 1}          | AFD             |       13        | `lista2-124.jff`     |
| L2 · 125         | {0, 1}          | AFD             |        2        | `lista2-125.jff`     |
| L2 · 126         | {0, 1}          | AFD             |        2        | `lista2-126.jff`     |
| L2 · 127         | {0, 1}          | AFD             |        2        | `lista2-127.jff`     |
| L2 · 128         | {0, 1}          | AFD             |        6        | `lista2-128.jff`     |
| L2 · 131         | {0, 1}          | AFD             |        2        | `lista2-131.jff`     |
| L2 · 133         | {a, b}          | AFD             |        4        | `lista2-133.jff`     |
| L2 · 135         | {a, b}          | AFD             |        5        | `lista2-135.jff`     |
| L2 · 137         | {a, b}          | AFD             |        4        | `lista2-137.jff`     |
| L2 · 139         | {0, 1}          | AFD             |        2        | `lista2-139.jff`     |
| L2 · 141         | {0, 1}          | AFD             |        3        | `lista2-141.jff`     |
| L2 · 145         | {0, 1}          | AFD             |        6        | `lista2-145.jff`     |
| L2 · 147         | {0, 1}          | AFD             |        7        | `lista2-147.jff`     |
| L2 · 148         | {A, N, P, S}    | AFD             |       13        | `lista2-148.jff`     |
| L2 · 149         | {0, 1}          | AFD             |        3        | `lista2-149.jff`     |
| L2 · 150         | {0, 1, a}       | AFD             |        4        | `lista2-150.jff`     |
| L3 · 151         | {0, 1}          | AFD             |       10        | `lista3-151.jff`     |
| L3 · 152         | {0, 1, 2}       | AFD             |        6        | `lista3-152.jff`     |
| L3 · 153         | {0, 1}          | AFD             |        7        | `lista3-153.jff`     |
| L3 · 154         | {0, 1}          | AFD             |       11        | `lista3-154.jff`     |
| L3 · 155         | {0, 1}          | AFD             |       12        | `lista3-155.jff`     |
| L3 · 156         | {0, 1}          | AFD             |        5        | `lista3-156.jff`     |
| L3 · 157         | {0, 1}          | AFD             |        6        | `lista3-157.jff`     |
| L3 · 158         | {0, 1}          | AFD             |        3        | `lista3-158.jff`     |
| L3 · 159         | {0, 1}          | AFD             |        3        | `lista3-159.jff`     |
| L3 · 160         | {0, 1}          | AFD             |        3        | `lista3-160.jff`     |
| L3 · 161         | {0, 1}          | AFD             |        3        | `lista3-161.jff`     |
| L3 · AFN del 097 | {0, 1, 2}       | AFD             |        3        | `lista3-afn-097.jff` |
| L3 · AFN del 099 | {0, 1, 2}       | AFN             |        7        | `lista3-afn-099.jff` |
| L3 · AFN del 102 | {a, b}          | AFN             |        7        | `lista3-afn-102.jff` |
| L3 · AFN del 103 | {a, b}          | AFN             |        7        | `lista3-afn-103.jff` |
| L3 · AFN del 106 | {0, 1, 2}       | AFN             |        8        | `lista3-afn-106.jff` |
| L3 · AFN del 107 | {0, 1, 2}       | AFN             |       13        | `lista3-afn-107.jff` |
| L3 · AFN del 109 | {0, 1, a, b, c} | AFN             |       22        | `lista3-afn-109.jff` |
| L3 · AFN del 111 | {0, 1, 2}       | AFD             |       20        | `lista3-afn-111.jff` |
| L3 · AFN del 112 | {0, 1, 2}       | AFN             |        7        | `lista3-afn-112.jff` |
| L3 · AFN del 113 | {0, 1, 2}       | AFN             |        7        | `lista3-afn-113.jff` |
| L3 · AFN del 118 | {a, b}          | AFN             |        5        | `lista3-afn-118.jff` |
| L3 · AFN del 120 | {0, 1, 2}       | AFN             |        7        | `lista3-afn-120.jff` |
| L3 · AFN del 121 | {0, 1, 2}       | AFD             |        5        | `lista3-afn-121.jff` |
| L3 · AFN del 122 | {0, 1, 2}       | AFD             |        3        | `lista3-afn-122.jff` |
| L3 · AFN del 123 | {a, b}          | AFN             |       15        | `lista3-afn-123.jff` |
| L3 · 189         | {0, 1}          | AFN             |        7        | `lista3-189.jff`     |
| L3 · 190         | {0, 1}          | AFN             |       19        | `lista3-190.jff`     |
| L3 · 192         | {0, 1}          | AFN             |        5        | `lista3-192.jff`     |
| L3 · 193         | {0, 1}          | AFN             |        6        | `lista3-193.jff`     |
| L3 · 194         | {0, 1, 2}       | AFN             |        2        | `lista3-194.jff`     |
| L3 · 195         | {0, 1}          | AFN             |        7        | `lista3-195.jff`     |
| L3 · 236         | {0, 1}          | AFN-λ           |        4        | `lista3-236.jff`     |
| L3 · 237         | {0, 1}          | AFN-λ           |        4        | `lista3-237.jff`     |
| L3 · 238         | {0, 1}          | AFN-λ           |        6        | `lista3-238.jff`     |
| L3 · 239         | {0, 1}          | AFN-λ           |        6        | `lista3-239.jff`     |
| L3 · 240         | {0, 1}          | AFN-λ           |        6        | `lista3-240.jff`     |
| L3 · 254         | {0, 1}          | AFD             |        2        | `lista3-254.jff`     |
| L3 · 255         | {0, 1}          | AFD             |        2        | `lista3-255.jff`     |
| L3 · 256         | {0, 1, 2}       | AFD             |        2        | `lista3-256.jff`     |
| L3 · 257         | {0, 1}          | AFD             |        3        | `lista3-257.jff`     |
| L3 · 258         | {0, 1}          | AFD             |        3        | `lista3-258.jff`     |
| L3 · 260         | {0, 1}          | AFN             |        6        | `lista3-260.jff`     |
| L3 · 261         | {0, 1}          | AFN             |        3        | `lista3-261.jff`     |
| L3 · 262         | {a, b}          | AFD             |        5        | `lista3-262.jff`     |
| L3 · 263         | {0, 1}          | AFN             |        3        | `lista3-263.jff`     |

Autómatas de los ejercicios con asterisco.
