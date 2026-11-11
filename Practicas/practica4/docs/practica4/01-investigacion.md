# Ejercicio 1. Investigación sobre expresiones regulares

## Lenguajes regulares y expresiones regulares

Sobre un alfabeto Σ, las **expresiones regulares** se definen por inducción (Hopcroft et al., 2007, Sección 3.1.2): ∅, λ y cada símbolo a ∈ Σ son expresiones, con L(∅) = ∅, L(λ) = {λ} y L(a) = {a}; y si r y s son expresiones, también lo son r + s, rs, r\* y (r), con

- **unión**: L(r + s) = L(r) ∪ L(s);
- **concatenación**: L(rs) = L(r)L(s) = {xy : x ∈ L(r), y ∈ L(s)};
- **cerradura de Kleene**: L(r\*) = ⋃\_{n≥0} L(r)ⁿ, con L(r)⁰ = {λ}.

Un lenguaje es **regular** si lo describe alguna expresión regular; equivalentemente, si lo reconoce algún autómata finito. La distinción importa: la expresión es un objeto sintáctico (una cadena de símbolos con operadores) y el lenguaje es un conjunto, posiblemente infinito. Muchas expresiones distintas describen el mismo lenguaje, como (a + b)\* y (a\*b\*)\*, y decidir si dos lo hacen es justamente lo que permiten los autómatas mínimos. La precedencia es estrella, después concatenación y al final unión, de modo que ab\* + c significa (a(b\*)) + c.

## Lugar en la jerarquía de Chomsky

Los lenguajes regulares son el **tipo 3**, el nivel más bajo de la jerarquía (Chomsky, 1956): los generan las gramáticas lineales por la derecha (producciones A → aB o A → a, y S → λ) y los reconocen los autómatas finitos. Están contenidos estrictamente en los independientes del contexto (tipo 2): {aⁿbⁿ : n ≥ 0} lo genera S → aSb \| λ, pero ningún autómata finito lo reconoce. La razón es la memoria: un autómata finito sólo distingue un número fijo de situaciones, y contar n aes no acotadas exige una pila.

## Teorema de Kleene

**Teorema** (Hopcroft et al., 2007, Sección 3.2, teoremas 3.4 y 3.7; Kleene, 1956; Sipser, 2013, Sección 1.3, teorema 1.54). Un lenguaje es regular si y sólo si es reconocido por un autómata finito.

- **De expresión a autómata** (Parte I en la notación del curso): por inducción sobre la expresión se construye un AFN-λ con un único estado inicial y un único final; hay un caso básico para ∅, λ y cada símbolo, y una construcción para cada operador. El Ejercicio 2 la implementa.
- **De autómata a expresión** (Parte II): se obtiene la expresión de un AFD con las expresiones $R_{ij}^{(k)}$, eliminando estados o resolviendo el sistema de ecuaciones con el lema de Arden. El Ejercicio 3 implementa la eliminación de estados y el lema de Arden.

## Leyes algebraicas usadas en la Práctica 3

Para simplificar las expresiones del Ejercicio 1 de la Práctica 3 se usaron estas leyes (Hopcroft et al., 2007, Sección 3.4):

| Ley                                        | Forma                                        |
|--------------------------------------------|----------------------------------------------|
| Conmutatividad y asociatividad de la unión | r + s = s + r; (r + s) + t = r + (s + t)     |
| Asociatividad de la concatenación          | (rs)t = r(st)                                |
| Idempotencia                               | r + r = r                                    |
| Neutros y absorbente                       | ∅ + r = r; λr = rλ = r; ∅r = r∅ = ∅          |
| Distributividad                            | r(s + t) = rs + rt; (s + t)r = sr + tr       |
| Estrella                                   | (r\*)\* = r\*; ∅\* = λ\* = λ; λ + rr\* = r\* |
| Desplazamiento                             | r(sr)\* = (rs)\*r                            |
| Unión bajo estrella                        | (r + s)\* = r\*(sr\*)\*                      |

Leyes algebraicas.

## Expresiones de la teoría y de los lenguajes de programación

Las expresiones de los lenguajes de programación (PCRE, el módulo `re` de Python, JavaScript) parten de las de la teoría pero añaden sintaxis cómoda que no cambia la potencia —clases `[0-9]`, cuantificadores `+`, `?`, `{m,n}`, anclas `^` y `$`— y operadores que **sí** la cambian, como las referencias hacia atrás `\1`, que obligan a repetir exactamente el texto que capturó un grupo y con las que se describen lenguajes que no son regulares (Câmpeanu et al., 2003). Además, su significado práctico no es «¿pertenece la cadena al lenguaje?», sino «¿dónde está la primera coincidencia?», y muchos motores la buscan con retroceso, lo que puede tardar un tiempo exponencial (Davis et al., 2018).

**El patrón (a\*)b\1 no es regular.** El grupo captura una sucesión de aes, después debe venir una b y al final la *misma* sucesión. Con coincidencia completa describe L = {aⁿbaⁿ : n ≥ 0}.

*Demostración con el lema de bombeo* (Hopcroft et al., 2007, Sección 4.1). Supongamos que L es regular y sea p su constante de bombeo. Tomamos ω = aᵖbaᵖ ∈ L, con \|ω\| ≥ p. El lema garantiza una descomposición ω = xyz con \|xy\| ≤ p, \|y\| ≥ 1 y xyⁱz ∈ L para todo i ≥ 0. Como \|xy\| ≤ p, x y y están dentro del primer bloque de aes: y = aᵏ con k ≥ 1. Con i = 2, xy²z = aᵖ⁺ᵏbaᵖ, que tiene más aes antes de la b que después, así que no pertenece a L. Esto contradice el lema; por lo tanto L no es regular y ningún autómata finito, ni ninguna expresión regular de la teoría, lo describe.

## Cinco aplicaciones

| Aplicación                                 | Expresión concreta                                                              | Cómo funciona                                                                                                                                                                                                    |
|--------------------------------------------|---------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Análisis léxico** en compiladores        | `[A-Za-z_][A-Za-z0-9_]*` para identificadores; `[0-9]+(\.[0-9]+)?` para números | Un generador como `lex` convierte cada patrón en un AFN, los une, determiniza y produce un AFD que lee el código una sola vez y devuelve la ficha más larga que coincide (Hopcroft et al., 2007, Sección 3.3.2). |
| **Búsqueda de patrones en texto**          | `grep -E 'colou?r'`                                                             | `u?` equivale a (u + λ): encuentra «color» y «colour» en todas las líneas de un archivo.                                                                                                                         |
| **Validación de datos**                    | `^[0-9]{5}$` para un código postal mexicano                                     | Exige exactamente cinco dígitos y nada más; un formulario rechaza la entrada antes de enviarla.                                                                                                                  |
| **Filtrado de registros**                  | `^\S+ \S+ \S+ \[[^]]+\] "GET [^"]*" 404`                                        | Sobre una bitácora de un servidor web en formato común, selecciona las peticiones GET que respondieron 404 (recurso no encontrado).                                                                              |
| **Automatización en el sistema operativo** | `sed -E 's/([0-9]{4})-([0-9]{2})-([0-9]{2})/\3\/\2\/\1/'`                       | Reescribe fechas ISO 8601 (2026-11-06) al formato 06/11/2026 en todos los archivos de un lote; los grupos capturan año, mes y día.                                                                               |

Aplicaciones de las expresiones regulares.

En los cinco casos la parte que decide si un texto coincide es regular; la sustitución con `\3/\2/\1` del último usa los grupos para *escribir* la salida, no para reconocer, así que no sale de la clase regular. Los validadores del Ejercicio 4 aplican esta idea con autómatas propios.
