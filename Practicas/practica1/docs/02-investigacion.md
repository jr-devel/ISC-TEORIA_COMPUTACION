# Ejercicio 2. Investigación: qué es la Teoría de la Computación

## Objeto de estudio y preguntas centrales

La Teoría de la Computación estudia, con modelos matemáticos, qué pueden calcular las máquinas y con qué recursos. Sipser (2013, 0) la organiza alrededor de una sola pregunta: *cuáles son las capacidades y las limitaciones fundamentales de las computadoras*, y la descompone en tres áreas que responden a versiones cada vez más finas de esa pregunta. Hopcroft et al. (2007, 1) parten de un punto distinto: definen la teoría de autómatas como el estudio de dispositivos de cómputo abstractos, y llegan a la computabilidad y a la complejidad como consecuencias de preguntar qué lenguajes reconoce cada dispositivo. Linz (2017, 1) adopta un enfoque todavía más concreto: los lenguajes formales, las gramáticas y los autómatas son el lenguaje común con el que se describen y comparan los modelos.

Las definiciones coinciden en el objeto (modelos abstractos de cómputo) y en el método (definición formal y demostración), pero difieren en el orden y en el énfasis. Sipser parte de la pregunta filosófica y presenta los modelos como herramientas para contestarla; Hopcroft, Motwani y Ullman, y Linz, parten de los modelos y dejan que las preguntas surjan de sus límites. Para un curso que empieza por los autómatas, la segunda forma es la más práctica; la primera explica por qué vale la pena el esfuerzo.

Las preguntas que plantea la teoría pueden resumirse en tres: ¿qué problemas se pueden resolver con un algoritmo?, ¿cuáles se pueden resolver eficientemente? y ¿qué modelo mínimo basta para un problema dado?

## Orígenes

A principios del siglo XX la lógica matemática atravesaba una crisis: la paradoja de Russell (el conjunto de los conjuntos que no se contienen a sí mismos) mostró que la teoría intuitiva de conjuntos era contradictoria, y otras paradojas de autorreferencia, como la del mentiroso, apuntaban al mismo problema (Kleene, 1952, 3). David Hilbert propuso entonces un programa para dar a la matemática una base segura: formalizarla por completo en sistemas axiomáticos y demostrar, con medios finitos, que esos sistemas son consistentes y completos.

Una pieza del programa era el *Entscheidungsproblem*, planteado por Hilbert y Ackermann en 1928: encontrar un procedimiento mecánico que, dada una fórmula de la lógica de primer orden, decida en un número finito de pasos si es válida. Para responder negativamente había que decir con precisión qué es un «procedimiento mecánico», y esa necesidad dio origen a la teoría. Gödel demostró en 1931 que todo sistema consistente suficientemente expresivo contiene enunciados verdaderos que no puede demostrar, y en 1936 Church (1936) y Turing (1936), de manera independiente, mostraron que el *Entscheidungsproblem* no tiene solución: Church con el cálculo λ y Turing con sus máquinas.

## Las tres ramas

| Rama                                     | Pregunta                                                                       | Ejemplo de resultado                                                                       |
|------------------------------------------|--------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|
| Teoría de autómatas y lenguajes formales | ¿Qué puede reconocer o generar cada modelo de cómputo restringido?             | Los autómatas finitos reconocen exactamente los lenguajes regulares; {aⁿbⁿ} no es regular. |
| Computabilidad                           | ¿Qué problemas se pueden resolver con un algoritmo?                            | El problema de la parada es indecidible.                                                   |
| Complejidad                              | ¿Qué problemas se pueden resolver con recursos razonables de tiempo y memoria? | La pregunta P = NP sigue abierta.                                                          |

Las tres ramas de la teoría (Sipser, 2013, 0).

## La tesis de Church-Turing

La tesis afirma que **toda función que puede calcularse mediante un procedimiento efectivo, en el sentido intuitivo, puede calcularse con una máquina de Turing**. En la década de 1930 se propusieron varios modelos independientes: las funciones recursivas generales de Herbrand y Gödel, el cálculo λ de Church, las máquinas de Turing y los sistemas de Post; todos resultaron equivalentes, en el sentido de que calculan exactamente las mismas funciones (Kleene, 1952, 13; Sipser, 2013, Sección 3.3). Turing lo demostró para su modelo y el de Church en el apéndice de su artículo.

Se llama *tesis* y no teorema porque uno de sus dos lados, «procedimiento efectivo», es una noción intuitiva y no un objeto matemático; no puede demostrarse una equivalencia entre algo definido y algo que no lo está. Lo que sí está demostrado es la equivalencia entre los modelos formales, y esa coincidencia es la mejor evidencia a favor de la tesis.

## Alfabetos, cadenas y lenguajes

Un **alfabeto** Σ es un conjunto finito y no vacío de símbolos. Una **cadena** (o palabra) sobre Σ es una sucesión finita de símbolos de Σ; su longitud \|ω\| es el número de símbolos, y la **cadena vacía** λ es la única de longitud 0. Σⁿ es el conjunto de las cadenas de longitud n, Σ\* = ⋃ₙ≥₀ Σⁿ el de todas las cadenas y Σ⁺ = ⋃ₙ≥₁ Σⁿ el de las no vacías. Un **lenguaje** sobre Σ es cualquier subconjunto de Σ\* (Hopcroft et al., 2007, Sección 1.5).

**Operaciones sobre cadenas.** La *concatenación* ωπ escribe π a continuación de ω, es asociativa y tiene a λ como neutro; \|ωπ\| = \|ω\| + \|π\|. La *potencia* se define por recursión: ω⁰ = λ y ωⁿ⁺¹ = ωⁿω. La *reflexión* ωᴿ invierte el orden: λᴿ = λ y (aω)ᴿ = ωᴿa, con (ωπ)ᴿ = πᴿωᴿ.

**Operaciones sobre lenguajes.** Como conjuntos, los lenguajes admiten *unión*, *intersección* y *diferencia*. La *concatenación* es L₁L₂ = {xy : x ∈ L₁, y ∈ L₂}; la *potencia*, L⁰ = {λ} y Lⁿ⁺¹ = LⁿL; la *reflexión*, Lᴿ = {ωᴿ : ω ∈ L}. La **cerradura de Kleene** es L\* = ⋃ₙ≥₀ Lⁿ y la **cerradura positiva**, L⁺ = ⋃ₙ≥₁ Lⁿ (Linz, 2017, Sección 1.2).

**Por qué Σ⁰ = {λ}.** Σ⁰ es el conjunto de las cadenas de longitud 0, y hay exactamente una: λ. Además, {λ} es el neutro de la concatenación de lenguajes (L{λ} = L), igual que λ lo es de la de cadenas; si Σ⁰ fuera ∅, la identidad Σᵐ⁺ⁿ = ΣᵐΣⁿ fallaría para m = 0, porque ∅L = ∅. **Σ\* frente a Σ⁺.** La única diferencia es λ: Σ\* = Σ⁺ ∪ {λ} y Σ⁺ = ΣΣ*. En general L⁺ = L* sólo si λ ∈ L.

## La jerarquía de Chomsky

Chomsky (1956) clasificó las gramáticas según la forma de sus producciones; cada tipo genera una clase de lenguajes que contiene a la siguiente, y a cada clase corresponde una máquina que la reconoce.

| Tipo | Lenguajes                   | Forma de las producciones               | Máquina reconocedora               |
|------|-----------------------------|-----------------------------------------|------------------------------------|
| 0    | Recursivamente enumerables  | α → β, con α no vacía (sin restricción) | Máquina de Turing                  |
| 1    | Sensibles al contexto       | αAβ → αγβ, con γ no vacía               | Autómata linealmente acotado       |
| 2    | Independientes del contexto | A → γ                                   | Autómata de pila (no determinista) |
| 3    | Regulares                   | A → aB o A → a (lineal por la derecha)  | Autómata finito                    |

Jerarquía de Chomsky (Hopcroft et al., 2007; Lewis & Papadimitriou, 1998; Sipser, 2013).

Las inclusiones son estrictas: {aⁿbⁿ : n ≥ 0} es independiente del contexto pero no regular, {aⁿbⁿcⁿ : n ≥ 0} es sensible al contexto pero no independiente del contexto, y el lenguaje de la parada es recursivamente enumerable pero no recursivo.

## Autómatas finitos y expresiones regulares

Un **autómata finito determinista** es una quíntupla M = (Q, Σ, δ, q₀, F), con Q un conjunto finito de estados, Σ el alfabeto, δ: Q × Σ → Q la función de transición, q₀ ∈ Q el estado inicial y F ⊆ Q los de aceptación. δ se extiende a cadenas con δ̂(q, λ) = q y δ̂(q, ωa) = δ(δ̂(q, ω), a); M acepta ω si δ̂(q₀, ω) ∈ F, y L(M) es el conjunto de las cadenas aceptadas (Hopcroft et al., 2007, Sección 2.2). Un **autómata finito no determinista** sólo cambia la función de transición: δ: Q × Σ → 𝒫(Q) devuelve un conjunto de estados, posiblemente vacío, y la cadena se acepta si *alguna* de las sucesiones posibles de estados termina en F.

Los dos modelos son **equivalentes**: para todo AFN existe un AFD que reconoce el mismo lenguaje (Kozen, 1997). Rabin & Scott (1959) lo demostraron con la *construcción de subconjuntos*, en la que cada estado del AFD es un conjunto de estados del AFN; el precio es que el AFD puede tener hasta 2ⁿ estados. Kleene (1956) probó además que los lenguajes que reconocen los autómatas finitos son exactamente los que describen las **expresiones regulares**, construidas a partir de ∅, λ y los símbolos con unión, concatenación y estrella.

Tres problemas reales en los que se aplican expresiones regulares:

1.  **Análisis léxico.** El primer paso de un compilador divide el código en fichas (identificadores, números, palabras reservadas); cada clase de ficha se describe con una expresión, como `[A-Za-z_][A-Za-z0-9_]*` para los identificadores, y el analizador se construye como un AFD.
2.  **Validación de datos.** Un formulario rechaza un correo o un código postal mal escritos comparando el texto con una expresión antes de enviarlo.
3.  **Búsqueda en texto y registros.** Herramientas como `grep` encuentran todas las líneas de un archivo de bitácora que contienen, por ejemplo, una dirección IP o un código de error, sin recorrer el archivo más de una vez.

Las expresiones de los lenguajes de programación añaden operadores que no son regulares, como las referencias hacia atrás, y sus motores pueden tardar un tiempo exponencial; el artículo de Davis et al. (2019) del Ejercicio 3 estudia esas diferencias.
