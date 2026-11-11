# Ejercicio 4. Investigación y estado del arte

## 4.1 Investigación

### El no determinismo

Un **AFN** es una quíntupla N = (Q, Σ, δ, q₀, F) igual a la de un AFD salvo por la función de transición, que ahora devuelve un conjunto: δ: Q × Σ → 𝒫(Q). Un mismo par puede llevar a varios estados o a ninguno. La extensión a cadenas es δ̂(q, λ) = {q} y δ̂(q, ωa) = ⋃\_{p ∈ δ̂(q, ω)} δ(p, a), y N **acepta** ω si δ̂(q₀, ω) ∩ F ≠ ∅: basta con que *alguna* de las sucesiones de elecciones termine en un estado final (Hopcroft et al., 2007, Sección 2.3.2). Una manera útil de pensarlo es que el autómata adivina siempre bien, o que explora todas las elecciones en paralelo y gana si alguna gana.

Un **AFN-λ** permite además transiciones que no consumen símbolo: δ: Q × (Σ ∪ {λ}) → 𝒫(Q). Para él, aceptar significa que existe un camino desde q₀ hasta un estado de F cuyas etiquetas, al concatenarse, forman ω (las λ no aportan nada a la concatenación) (Sipser, 2013, Sección 1.2).

### La λ-clausura

λ-cl(q) es el menor conjunto que contiene a q y que es cerrado bajo transiciones λ: si p ∈ λ-cl(q) y r ∈ δ(p, λ), entonces r ∈ λ-cl(q). Para un conjunto, λ-cl(S) = ⋃\_{q∈S} λ-cl(q). Se calcula con un recorrido de grafo restringido a las aristas λ:

``` text
λ-cl(S):
    visitados ← S;  pila ← elementos de S
    mientras pila no esté vacía:
        q ← sacar(pila)
        para cada r en δ(q, λ) que no esté en visitados:
            agregar r a visitados y a pila
    devolver visitados
```

Cada estado entra a la pila una vez y cada arista λ se revisa una vez, así que el costo es O(\|Q\| + \|δ_λ\|). Con ella, δ̂(q, λ) = λ-cl(q) y δ̂(q, ωa) = λ-cl(⋃\_{p ∈ δ̂(q, ω)} δ(p, a)) (Hopcroft et al., 2007, Sección 2.5.3).

### Construcción de subconjuntos y equivalencia AFD–AFN

**Teorema** (Hopcroft et al., 2007, Sección 2.3.5; Rabin & Scott, 1959). Para todo AFN N existe un AFD D tal que L(D) = L(N).

*Esbozo de la demostración.* Se define D = (𝒫(Q), Σ, δ_D, {q₀}, F_D) con δ_D(S, a) = ⋃\_{q∈S} δ(q, a) y F_D = {S : S ∩ F ≠ ∅}. Por inducción sobre \|ω\| se prueba que δ̂\_D({q₀}, ω) = δ̂\_N(q₀, ω): para λ ambos son {q₀}, y el paso inductivo es la definición de δ_D. Entonces D acepta ω ⇔ δ̂\_D({q₀}, ω) ∩ F ≠ ∅ ⇔ N acepta ω. Para un AFN-λ basta usar λ-cl({q₀}) como inicial y λ-cl(⋃ δ(q, a)) como transición.

### El costo de la conversión

D puede tener hasta 2^\|Q\| estados, y la cota es justa: el lenguaje de las cadenas cuyo n-ésimo símbolo desde el final es 1 tiene un AFN de n + 1 estados y ningún AFD de menos de 2ⁿ (Hopcroft et al., 2007, Sección 2.3.6). En la práctica se construyen sólo los subconjuntos alcanzables desde el inicial, y suelen ser muchos menos (Ejercicio 2).

### Teorema de Kleene

**Teorema** (Kleene, 1956). Un lenguaje es reconocido por un autómata finito si y sólo si lo describe una expresión regular. En una dirección se construye, por inducción sobre la expresión, un AFN-λ para ∅, λ y cada símbolo, y para la unión, la concatenación y la estrella; en la otra, se obtiene una expresión del autómata eliminando estados o con las expresiones $R_{ij}^{(k)}$ (Hopcroft et al., 2007, Sección 3.2). Junto con la equivalencia anterior, AFD, AFN, AFN-λ y expresiones regulares describen la misma clase: los lenguajes regulares.

### Minimización: Myhill-Nerode y Hopcroft

Dos cadenas x, y son *indistinguibles* respecto de L (x ≡\_L y) si para toda z, xz ∈ L ⇔ yz ∈ L. **Teorema de Myhill-Nerode** (Nerode, 1958): L es regular si y sólo si ≡\_L tiene un número finito de clases, y ese número es el de estados del AFD mínimo, que es único salvo el nombre de los estados. El **algoritmo de Hopcroft** (Hopcroft, 1971) encuentra esas clases refinando particiones: empieza con {F, Q − F}, mantiene una lista de bloques «separadores» y, para cada separador B y símbolo a, parte todo bloque cuyos estados van con a unos a B y otros fuera de B. Su truco es agregar a la lista sólo la mitad *más pequeña* de cada bloque partido; así cada estado se procesa O(log \|Q\|) veces y el algoritmo cuesta O(\|Σ\|·\|Q\| log \|Q\|), frente a O(\|Σ\|·\|Q\|²) del refinamiento ingenuo de Moore (Moore, 1971).

### Qué significa que el no determinismo no aumente el poder

Que AFN y AFD reconozcan la misma clase significa que el no determinismo es una herramienta de **descripción**, no de **cómputo**: permite escribir autómatas más pequeños y más fáciles de entender («adivina dónde empieza el patrón»), pero cualquier cosa que haga un AFN puede hacerla un AFD, a costa de quizá exponencialmente más estados. En ingeniería eso se traduce en una elección: se diseña y se razona con el AFN (o con la expresión regular), y se ejecuta con un AFD cuando el tiempo por símbolo importa más que la memoria.

## 4.2 Artículo asignado: Rabin y Scott (1959)

**Dónde se prueba.** En la sección 5, «Nondeterministic operation». El artículo define el autómata no determinista como un sistema (S, M, S₀, F) cuya tabla M asigna a cada par (estado, símbolo) un *conjunto* de estados y que admite un *conjunto* de iniciales S₀; una cinta se acepta si alguna sucesión de elecciones termina en F. Después construye el autómata determinista cuyos estados son los subconjuntos de S y, en el **teorema 11**, prueba que ambos aceptan las mismas cintas (Rabin & Scott, 1959).

**La construcción en la notación del curso.** Dado N = (Q, Σ, δ, q₀, F), D = (𝒫(Q), Σ, δ_D, {q₀}, F_D) con δ_D(S, a) = ⋃\_{q∈S} δ(q, a) y F_D = {S ⊆ Q : S ∩ F ≠ ∅}. Con varios iniciales, como en el artículo, el inicial de D es S₀ completo.

**Diferencias de notación.** El artículo llama *tapes* a las cadenas, escribe M en lugar de δ, no incluye el alfabeto en la tupla y admite varios iniciales; el libro de texto usa la quíntupla con Σ explícito y un solo q₀. La notación del libro resulta más clara: el mismo símbolo δ sirve para todos los modelos del curso y la extensión δ̂ se define aparte, mientras que el artículo, escrito para lectores de lógica, define la aceptación con sucesiones de estados.

**El Premio Turing.** La mención oficial de la ACM otorga el premio de 1976 a Rabin y Scott por este artículo y destaca que introdujo la idea de las máquinas no deterministas, un concepto que resultó de enorme valor y que siguió inspirando trabajos posteriores (Association for Computing Machinery, 2026). El reconocimiento no se debe a que los AFN reconozcan más lenguajes —el propio artículo prueba que no—, sino al concepto: el no determinismo es hoy central en la complejidad (la clase NP), en la verificación y en el procesamiento de expresiones regulares.

## 4.3 Dos artículos localizados

### Saarikivi, Veanes, Wan y Xu (2019)

1.  **Cita.** Saarikivi, O., Veanes, M., Wan, T., y Xu, E. (2019). Symbolic regex matcher. En T. Vojnar y L. Zhang (Eds.), *Tools and Algorithms for the Construction and Analysis of Systems (TACAS 2019)* (Lecture Notes in Computer Science, Vol. 11427, pp. 372–378). Springer. <https://doi.org/10.1007/978-3-030-17462-0_24>
2.  **Problema.** El motor de expresiones regulares de .NET usa retroceso (*backtracking*) y algunos patrones tardan un tiempo exponencial; una herramienta de Microsoft que revisa código en la nube en busca de credenciales necesitaba buscar con tiempo lineal.
3.  **Método.** SRM construye el autómata sobre la marcha con *derivadas simbólicas de Brzozowski*: el estado es una expresión regular y leer un carácter la transforma en otra. Las clases de caracteres se representan como predicados sobre *minterms* (una partición del alfabeto en clases que se comportan igual) y los estados de AFD ya calculados se guardan en caché.
4.  **Resultado.** En dos colecciones de prueba, SRM y RE2 de Google fueron en general más rápidos que el motor de .NET; el tiempo medio de SRM fue comparable al de RE2 con menos casos extremos, aunque su compilación es más lenta. Se adoptó internamente y eliminó el retroceso catastrófico en archivos con líneas largas.
5.  **Relación con el temario.** Construcción de subconjuntos perezosa y equivalencia entre expresiones regulares y autómatas.
6.  **Aportación.** Es una implementación medida, como pide el enunciado, y muestra la misma decisión que el Ejercicio 3: no construir de antemano el AFD completo, sino sólo los estados que la entrada visita.

### Moseley et al. (2023)

1.  **Cita.** Moseley, D., Nishio, M., Perez Rodriguez, J., Saarikivi, O., Toub, S., Veanes, M., Wan, T., y Xu, E. (2023). Derivative based nonbacktracking real-world regex matching with backtracking semantics. *Proceedings of the ACM on Programming Languages*, *7*(PLDI), Artículo 148. <https://doi.org/10.1145/3591262>
2.  **Problema.** Los motores sin retroceso eran inmunes a los ataques de denegación de servicio por expresiones regulares, pero no podían reemplazar a los de retroceso porque no soportaban anclas, contadores ni el mismo resultado de coincidencia.
3.  **Método.** Extienden las derivadas de Brzozowski a *derivadas por posición* que manejan anclas, simulan la prioridad de las alternativas del retroceso sin retroceder y buscan en dos pasadas (una hacia adelante para el final de la coincidencia y otra sobre la expresión invertida para el inicio). Demuestran la corrección formalmente e implementan el resultado como la opción `RegexOptions.NonBacktracking` de .NET 7.
4.  **Resultado.** En un conjunto industrial de 184 patrones obtienen una aceleración media geométrica de 4.7× sobre el motor compilado de .NET, y en la búsqueda de credenciales sobre 15 GB de código, mejoras de 9 % a 26 %; el beneficio principal es eliminar los casos extremos.
5.  **Relación con el temario.** Autómatas finitos deterministas construidos desde expresiones regulares; reflexión (la expresión invertida reconoce Lᴿ).
6.  **Aportación.** Prueba que la teoría del curso llega a un producto de uso masivo y explica por qué un validador debe reconocer con un autómata y no con un motor de retroceso, idea que se retoma en la Práctica 4.
