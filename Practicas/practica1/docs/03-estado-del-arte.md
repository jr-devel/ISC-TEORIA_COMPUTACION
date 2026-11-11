# Ejercicio 3. Estado del arte: cinco artículos

Cada texto se resume en una ficha de seis puntos; para los tres asignados se responden además las preguntas del enunciado.

## Texto 1. Gribkoff (2013)

1.  **Cita.** Gribkoff, E. (2013). *Applications of deterministic finite automata* \[Documento de curso, ECS 120\]. University of California, Davis. <https://www.cs.ucdavis.edu/~rogaway/classes/120/spring13/eric-dfa.pdf>
2.  **Problema.** Mostrar a estudiantes de un primer curso de teoría que el AFD no es sólo un objeto abstracto, sino un modelo que aparece en sistemas cotidianos.
3.  **Método.** Tras repasar la definición formal del AFD y la de la máquina de Mealy, analiza cuatro ejemplos: una máquina expendedora, el comportamiento de los fantasmas de Pac-Man, el diagrama de estados de TCP y el autocompletado de Apache Lucene.
4.  **Resultado.** Cada sistema se describe con pocos estados; en Lucene, el transductor comparte prefijos y sufijos entre palabras y así reduce la memoria del índice.
5.  **Tema de la Unidad I.** Autómatas finitos: definición formal del AFD y aplicaciones.
6.  **Aportación.** Ofrece ejemplos de modelado que sirven de punto de partida para diseñar autómatas propios, como el del fantasma de Pac-Man que se amplía en la Práctica 2.

**AFD y máquina de Mealy.** El AFD sólo produce un veredicto al final de la lectura: acepta o rechaza. La máquina de Mealy agrega un alfabeto de salida y una función que emite un símbolo en *cada* transición, de modo que convierte una cadena de entrada en una de salida. El autocompletado de Lucene necesita esa salida: no basta con saber que un prefijo pertenece al diccionario; hay que recuperar información de cada palabra completada (en el ejemplo, un número que se obtiene acumulando las salidas del camino).

**Máquina expendedora con F = ∅.** Si ningún estado es de aceptación, δ̂(q₀, ω) ∉ F para toda ω, así que el lenguaje del autómata es ∅: ninguna cadena se acepta. El modelo sigue siendo útil para describir cómo cambia el estado de la máquina con cada moneda, pero la noción de «cadena aceptada» deja de aportar información; se está usando el autómata como un sistema de transiciones y no como un reconocedor.

**Afirmación por verificar.** El texto afirma que, gracias al transductor, Lucene mantiene en memoria el índice completo del autocompletado y responde mucho más rápido. No da cifras, versiones ni una referencia; antes de citarla debería confirmarse en una publicación arbitrada o en la documentación oficial de Lucene.

## Texto 2. Luna-Benoso et al. (2022)

1.  **Cita.** Luna-Benoso, B., Martínez-Perales, J. C., Cortés-Galicia, J., Flores-Carapia, R., y Silva-García, V. M. (2022). Melanoma detection in dermoscopic images using a cellular automata classifier. *Computers*, *11*(1), 8. <https://doi.org/10.3390/computers11010008>
2.  **Problema.** Distinguir el melanoma de lesiones benignas en imágenes dermatoscópicas como apoyo al diagnóstico temprano.
3.  **Método.** Segmentan la lesión (filtro de mediana, umbral de Otsu y operaciones morfológicas sobre la vecindad de Moore), extraen 11 descriptores estadísticos de textura y clasifican con un autómata celular asociativo de estados binarios.
4.  **Resultado.** Con 190 imágenes de la base PH2 obtienen exactitud de 0.978, sensibilidad de 0.944, especificidad de 0.987 y área bajo la curva ROC de 0.965.
5.  **Tema de la Unidad I.** Modelos de cómputo; diferencia entre autómata finito y autómata celular.
6.  **Aportación.** Un modelo de transiciones locales, barato de calcular, compite con clasificadores mucho más costosos en una aplicación médica.

**Autómata celular y autómata finito.** Se parecen en que ambos son discretos y evolucionan con una función de transición sobre un conjunto finito de estados. Difieren en dónde vive el estado y en qué se lee. En el autómata celular el **estado** es de cada celda de una retícula (en el artículo, 0 o 1); el **vecindario** es el conjunto de celdas que influyen en una celda (la vecindad de Moore: sus ocho vecinas); y la **regla local** calcula el nuevo estado de cada celda a partir de su vecindario, para todas las celdas a la vez. Un autómata finito tiene un único estado global que cambia al leer un símbolo de una cadena, uno por paso, y termina aceptando o rechazando.

**Problema y elección del modelo.** El melanoma es el cáncer de piel más agresivo y su pronóstico depende de detectarlo temprano. Los autores eligen autómatas celulares porque se implementan con facilidad y requieren pocos recursos, a diferencia de redes profundas como AlexNet o VGG16.

**Datos y métricas.** Usan la base PH2 del Hospital Pedro Hispano: 200 imágenes RGB de 768 × 560 píxeles, de las que descartan 10 por falta de nitidez. Reportan exactitud, sensibilidad, especificidad y AUC, con los valores del punto 4.

## Texto 3. Turing (1936), trabajo original

1.  **Cita.** Turing, A. M. (1936).[^1] On computable numbers, with an application to the Entscheidungsproblem. *Proceedings of the London Mathematical Society*, *s2-42*(1), 230–265. <https://doi.org/10.1112/plms/s2-42.1.230>
2.  **Problema.** Precisar qué significa que un número sea calculable por un procedimiento mecánico y, con esa definición, responder el *Entscheidungsproblem*.
3.  **Método.** Introduce la *máquina automática*: una cinta dividida en casillas, una cabeza que lee y escribe un símbolo a la vez y un número finito de configuraciones. Un número es computable si una máquina lo escribe cifra por cifra. Construye una máquina *universal* que imita a cualquier otra a partir de su descripción.
4.  **Resultado.** Ninguna máquina decide si una máquina arbitraria escribe infinitas cifras; de ahí se sigue que no existe un procedimiento general de decisión para la lógica de primer orden. En un apéndice muestra que su noción coincide con la λ-definibilidad de Church.
5.  **Tema de la Unidad I.** Orígenes de la teoría, computabilidad y tesis de Church-Turing.
6.  **Aportación.** Es el origen del modelo que ocupa el nivel más alto de la jerarquía de Chomsky estudiada en el curso.

**Resultado y modelo.** Se demuestra la indecidibilidad del *Entscheidungsproblem* y se introduce la máquina de Turing, incluida la universal.

**Tesis de Church-Turing.** Toda función efectivamente calculable, en el sentido intuitivo, es calculable por una máquina de Turing. Es una tesis porque «efectivamente calculable» no es un concepto formal; sólo se puede argumentar a su favor, como hace Turing al analizar lo que una persona hace al calcular con lápiz y papel, y con la equivalencia entre modelos independientes.

**Dificultades de lectura.** La notación es la mayor barrera: letras góticas para las configuraciones, máquinas descritas como tablas de «configuración, símbolo, operaciones, configuración final» y «tablas esqueleto» que funcionan como subrutinas. Se resolvió leyendo en paralelo el capítulo 3 de Sipser (2013) y reescribiendo cada tabla como δ(q, a) = (p, b, D), la notación del curso.

## Texto 4. Mavridou y Laszka (2018)

1.  **Cita.** Mavridou, A., y Laszka, A. (2018). Designing secure Ethereum smart contracts: A finite state machine based approach. En S. Meiklejohn y K. Sako (Eds.), *Financial Cryptography and Data Security* (pp. 523–540). Springer. <https://doi.org/10.1007/978-3-662-58387-6_28>
2.  **Problema.** Los contratos inteligentes de Ethereum administran activos valiosos y no pueden corregirse una vez desplegados, pero muchos se escriben con errores que se han explotado para robar fondos.
3.  **Método.** Proponen FSolidM: el desarrollador describe el contrato como una máquina de estados finitos (estados, transiciones y las acciones de cada transición) en una herramienta gráfica, y el marco genera el código Solidity. La semántica de la máquina se define formalmente y la seguridad se refuerza con patrones de diseño que se agregan como complementos.
4.  **Resultado.** Muestran con casos como una subasta a ciegas que el modelo de estados evita por construcción errores frecuentes (llamadas en un estado indebido, reentrada) y que los complementos añaden protecciones sin reescribir la lógica.
5.  **Tema de la Unidad I.** Autómatas finitos aplicados fuera de la teoría (seguridad y verificación de software).
6.  **Aportación.** Ejemplo de que fijar el conjunto de estados y la función de transición antes de programar es una técnica de ingeniería, no sólo de teoría; es la misma separación entre modelo e implementación que sigue el software de esta práctica.

## Texto 5. Davis et al. (2019)

1.  **Cita.** Davis, J. C., Michael IV, L. G., Coghlan, C. A., Servant, F., y Lee, D. (2019). Why aren’t regular expressions a lingua franca? An empirical study on the re-use and portability of regular expressions. En *Proceedings of the 27th ACM Joint European Software Engineering Conference and Symposium on the Foundations of Software Engineering* (pp. 443–454). ACM. <https://doi.org/10.1145/3338906.3338909>
2.  **Problema.** Los programadores copian expresiones regulares de un lenguaje a otro suponiendo que significan lo mismo; nadie había medido si esa suposición es cierta.
3.  **Método.** Encuesta a 158 desarrolladores y análisis de 537 806 expresiones únicas extraídas de 193 524 proyectos en ocho lenguajes; cada expresión se ejecuta en todos los motores con unas 10 000 entradas generadas y se buscan diferencias de resultado y de tiempo.
4.  **Resultado.** El 94 % de los encuestados reutiliza expresiones; alrededor del 15 % de las expresiones produce resultados distintos en algún lenguaje y alrededor del 10 % tiene un costo en tiempo distinto. Go y Rust no presentaron expresiones de tiempo exponencial; Java, JavaScript, Python y Ruby, más de mil cada uno.
5.  **Tema de la Unidad I.** Expresiones regulares y su relación con los autómatas finitos.
6.  **Aportación.** Explica por qué el curso distingue la expresión regular teórica de la de los lenguajes de programación y por qué conviene validar con un autómata cuyo tiempo es lineal.

## Comparación

| Texto                  | Arbitrado | Año  | Modelo que usa                      | Campo de aplicación                         |
|------------------------|:---------:|:----:|-------------------------------------|---------------------------------------------|
| 1\. Gribkoff           |    No     | 2013 | AFD y máquina de Mealy              | Docencia: máquinas, juegos, redes, búsqueda |
| 2\. Luna-Benoso et al. |    Sí     | 2022 | Autómata celular                    | Diagnóstico médico por imagen               |
| 3\. Turing (original)  |    Sí     | 1936 | Máquina de Turing                   | Fundamentos de la matemática                |
| 4\. Mavridou y Laszka  |    Sí     | 2018 | Máquina de estados finitos          | Seguridad de contratos inteligentes         |
| 5\. Davis et al.       |    Sí     | 2019 | Expresiones regulares y sus motores | Ingeniería de software                      |

Resumen de los cinco textos.

Los cinco describen un sistema mediante estados y reglas que dicen cómo cambiar de uno a otro; la diferencia está en el rigor y en el propósito. Turing demuestra un teorema de fundamentos con una definición nueva; Gribkoff, sin revisión ni bibliografía, divulga; Luna-Benoso et al. y Mavridou y Laszka construyen un sistema y lo evalúan; Davis et al. miden cómo se usa la teoría en la práctica. Los textos 4 y 5 se complementan: uno muestra el beneficio de fijar el modelo de estados antes de programar y el otro, el costo de no hacerlo, pues las expresiones de los lenguajes de programación ya no corresponden a un autómata finito. De ahí surge un problema abierto: cómo garantizar que una especificación escrita como autómata o expresión regular conserve su significado y su costo lineal cuando se traduce a la implementación concreta de cada lenguaje.

[^1]: El artículo se publicó en las partes 3 y 4 del volumen 42 (serie 2), aparecidas a finales de 1936, pero el volumen se cerró en 1937. El registro del DOI usa la fecha del volumen y la literatura, la de las partes.
