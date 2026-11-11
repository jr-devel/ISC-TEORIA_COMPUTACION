# Ejercicio 3. De autómata a expresión regular

## Verificación del determinismo

La sección **AFD → ER** abre el autómata activo o cualquier `.jff` de la biblioteca y, antes de convertir, llama a `verificar_determinismo`, que devuelve qué pares (estado, símbolo) impiden que sea un AFD: los que tienen dos o más destinos y los estados con transiciones λ. Por ejemplo, para `no-determinista-263.jff` el mensaje es «No es determinista en 1 pares: δ(q0, 0) = {q0, q1}», y el botón de conversión indica que primero hay que pasar por *Transformaciones*.

## Eliminación de estados paso a paso

`AutomataGeneralizado` es un autómata cuyas aristas llevan expresiones: hay una sola arista por par ordenado (las paralelas se unen con +), un inicial nuevo I con I →λ q₀ y un final nuevo T al que llega cada estado de F con λ. `EliminacionDeEstados` quita los estados originales uno a uno; al quitar k, para cada p → k → q:

$$R(p, q) \leftarrow R(p, q) + R(p, k)\,R(k, k)^*\,R(k, q).$$

Las expresiones se combinan con constructores que aplican sólo leyes seguras (∅ absorbente, λ neutro, idempotencia, (r\*)\* = r\*, (λ + r)\* = r\*), para que el resultado no crezca con términos inútiles. El orden puede fijarse escribiéndolo («q1, q2, q0») o dejarse al programa, que elige en cada paso el estado que crea menos aristas nuevas (entrantes × salientes). Cada eliminación es una etapa: la interfaz muestra la tabla «De · A · Expresión» del autómata generalizado que queda y la explicación con cada R(p, q) recalculado, y se avanza con «Siguiente». Como segundo método, `SistemaArden` plantea $X_q = \sum_a a\, X_{\delta(q,a)}$ (más λ si q ∈ F) y despeja con el lema de Arden, X = AX + B ⇒ X = A\*B, mostrando el sistema después de cada sustitución.

![AFD → ER con el AFD 276: autómata generalizado después de eliminar B.](../../evidencias/practica4/app/04-afd-er-pasos.png)

## Comparación con JFLAP

En la Práctica 3 se obtuvieron con JFLAP las expresiones de cinco AFD (119, 122, 138, 140b y 142a). Con el mismo orden de eliminación, el software produce exactamente las mismas expresiones que JFLAP; sólo cambian los espacios. Para comprobar que la comparación sirve cuando la escritura no coincide, en JFLAP se repitió la conversión con otro orden: las expresiones cambian de forma, pero describen el mismo lenguaje. Para decidirlo, ambas expresiones se convierten con el Ejercicio 2 en AFD mínimos y se comparan con la prueba de equivalencia de la Práctica 3: la tarjeta *Comparación* de la sección hace exactamente eso al pegar la expresión de JFLAP.

| AFD  | JFLAP, orden de la Práctica 3                         | JFLAP, otro orden                                                             | Software (orden automático)                           | ¿Equivalentes? |
|------|-------------------------------------------------------|-------------------------------------------------------------------------------|-------------------------------------------------------|:--------------:|
| 119  | (b + a(b + ab))\*(λ + a)                              | (b + ab + aab)\*(λ + a) (q1, q2, q3)                                          | (b + a(b + ab))\*(λ + a)                              |       Sí       |
| 122  | (0 + (1 + 2)(0 + (1 + 2)0))\*(λ + (1 + 2)(λ + 1 + 2)) | (0 + (1 + 2)0 + (1 + 2)(1 + 2)0)\*(λ + 1 + 2 + (1 + 2)(1 + 2)) (q1, q2, q3)   | (0 + (1 + 2)(0 + (1 + 2)0))\*(λ + (1 + 2)(λ + 1 + 2)) |       Sí       |
| 138  | (a + ba\*ba\*b)\*                                     | (a + ba\*ba\*b)\* (q2, q1)                                                    | (a + ba\*ba\*b)\*                                     |       Sí       |
| 140b | (00 + 11 + (01 + 10)(11 + 00)\*(10 + 01))\*           | (1(00)\*1 + (0 + 1(00)\*01)(11 + 10(00)\*01)\*(0 + 10(00)\*1))\* (q3, q2, q1) | (00 + 11 + (01 + 10)(11 + 00)\*(10 + 01))\*           |       Sí       |
| 142a | (ab)\*                                                | (ab)\* (q1, q2)                                                               | (ab)\*                                                |       Sí       |

Comparación con los resultados de JFLAP.

Con el mismo orden las expresiones son idénticas. Con otro orden cambian de forma: en 119 y 122, quitar q1 primero distribuye la concatenación, y en 140b, quitar q3 primero produce una expresión con (00)\* que no se parece a la original. En 138 y 142a el resultado no depende del orden. En los cinco casos los AFD mínimos coinciden salvo el nombre de los estados.

![Comparación de la expresión del software con la que da JFLAP para el AFD 140b eliminando en el orden q3, q2, q1.](../../evidencias/practica4/app/05-comparacion.png)

## Casos de prueba

| Caso   | Orden elegido | Eliminación de estados                   | Lema de Arden                                                  |
|--------|---------------|------------------------------------------|----------------------------------------------------------------|
| L3-254 | A, B          | 0\*1(1 + 00\*1)\*                        | (0 + 11\*0)\*11\*                                              |
| L3-255 | B, A          | ((0 + 1)1\*0)\*                          | ((0 + 1)1\*0)\*                                                |
| L3-256 | A, B          | (1 + 2)\*0(0 + 1 + 2(1 + 2)\*0)\*        | (1 + 2 + 0(0 + 1)\*2)\*0(0 + 1)\*                              |
| L3-257 | B, C, A       | ((1 + 01\*0)(0 + 1))\*(01\* + 1 + 01\*0) | (1(0 + 1) + 01\*0(0 + 1))\*(1 + 01\*(λ + 0))                   |
| L3-258 | B, A, C       | (0 + 1)(01 + (1 + 00)(0 + 1))\*          | ((0 + 1)1 + (0 + 1)0(10)\*(0 + 11))\*(0 + 1 + (0 + 1)0(10)\*1) |
| L4-276 | B, C, A       | (b + ab\*ab\*a)\*                        | (b + ab\*ab\*a)\*                                              |
| L4-277 | A, B          | 0\*1(1 + 00\*1)\*                        | (0 + 11\*0)\*11\*                                              |

Expresiones obtenidas por los dos métodos.

**Lista 4, 276** (número de aes múltiplo de 3). Arden: $X_A = bX_A + aX_B + \lambda$, $X_B = bX_B + aX_C$, $X_C = bX_C + aX_A$. Por Arden, $X_C = b^*aX_A$; sustituyendo, $X_B = bX_B + ab^*aX_A \Rightarrow X_B = b^*ab^*aX_A$; y $X_A = (b + ab^*ab^*a)X_A + \lambda \Rightarrow X_A = (b + ab^*ab^*a)^*$.

**Lista 4, 277** (cadenas que terminan en 1). Las dos expresiones parecen distintas: 0\*1(1 + 00\*1)\* y (0 + 11\*0)\*11\*. Su equivalencia se justifica con leyes: 1 + 00\*1 = (λ + 00\*)1 = 0\*1, así que la primera es 0\*1(0\*1)\* = (0\*1)⁺, las palabras formadas por bloques que terminan en 1; y (0 + 11\*0)\*11\* = (0 + 1⁺0)\*1⁺ es una sucesión de bloques que terminan en 0 seguida de al menos un 1. Ambas describen exactamente las palabras no vacías que terminan en 1, lo que confirma la prueba de equivalencia por autómatas mínimos. Como comprobación adicional, las dos aceptan `1`, `01`, `0011` y `1101`, y rechazan λ, `0`, `10` y `110`; esos ejemplos por sí solos no prueban la equivalencia.

**Pruebas.** `tests/test_kleene.py` (48 pruebas) convierte cada uno de los catorce autómatas (254–258, 276, 277 y los cinco de la Práctica 3) a expresión por eliminación —en orden automático y en el orden de Q— y por Arden, vuelve a construir el autómata de cada expresión y exige que sea equivalente al original. También comprueba el mensaje de no determinismo, la unión de aristas paralelas, que los nombres I y T no choquen con estados existentes, el lenguaje vacío y la comparación de pares de expresiones equivalentes y no equivalentes.
