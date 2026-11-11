# Ejercicio 3. Documentación de los algoritmos

En las estimaciones, n = \|Q\|, k = \|Σ\| y m es el número de transiciones (m ≤ n²(k + 1) en un AFN-λ).

## Cerradura λ y simulación directa

**Problema.** Dado un AFN-λ y un conjunto de estados S, hallar los estados alcanzables desde S sin consumir símbolos; con ello, decidir si el autómata acepta una palabra sin convertirlo.

**Resultado teórico.** δ̂(q, λ) = λ-cl(q) y δ̂(q, ωa) = λ-cl(⋃\_{p ∈ δ̂(q, ω)} δ(p, a)); ω se acepta si δ̂(q₀, ω) ∩ F ≠ ∅ (Hopcroft et al., 2007, Secciones 2.5.3–2.5.4).

``` text
CIERRE(S)                                  # Automata.cierre
    visitados ← S; pila ← S
    mientras pila ≠ ∅: q ← pop(pila)
        para r ∈ δ(q, λ) − visitados: visitados ← visitados ∪ {r}; push(pila, r)
    devolver visitados

SIMULAR(ω)                                 # Simulacion.avanzar / completar
    S ← CIERRE({q₀})
    para cada símbolo a de ω: S ← CIERRE(⋃_{q∈S} δ(q, a))     # Automata.transitar
    aceptar si S ∩ F ≠ ∅                                       # Automata.es_aceptacion
```

**Ejemplo (196).** A mano: λ-cl(A) = {A, B} porque A →λ B; λ-cl(B) = {B}, λ-cl(C) = {C}. Con ω = `01`: inicio {A, B}; con 0, δ(A, 0) ∪ δ(B, 0) = {A} ∪ {A, B} = {A, B}, cuyo cierre es {A, B}; con 1, δ(B, 1) = {C}; C ∈ F, se acepta. El software da la misma tabla de cerraduras y la misma traza.

**Pasos.** Una cerradura revisa cada estado y cada arista λ una vez: O(n + m_λ). Cada paso de la simulación une hasta n conjuntos de hasta n estados y los cierra: O(n²), y una palabra cuesta O(\|ω\|·n²).

## Eliminación de transiciones λ

**Problema.** Dado un AFN-λ, obtener un AFN sin transiciones λ con el mismo lenguaje y los mismos estados.

**Resultado teórico.** Con Δ’(q, a) = λ-cl(δ(λ-cl(q), a)) y F’ = {q : λ-cl(q) ∩ F ≠ ∅}, el AFN (Q, Σ, Δ’, q₀, F’) reconoce el mismo lenguaje (Hopcroft et al., 2007, Sección 2.5.5; Sipser, 2013, Sección 1.2, demostración del teorema 1.39).

``` text
QUITAR-λ(N)                                # QuitarLambda.resolver
    para q ∈ Q: C[q] ← CIERRE({q})          # etapa 1
    para q ∈ Q, a ∈ Σ: Δ'(q, a) ← CIERRE(⋃_{p∈C[q]} δ(p, a))   # etapa 2
    F' ← {q : C[q] ∩ F ≠ ∅}                 # etapa 3
    devolver (Q, Σ, Δ', q₀, F')             # etapa 4
```

**Ejemplo (196).** A mano: Δ’(A, 0) = λ-cl(δ({A, B}, 0)) = λ-cl({A, B}) = {A, B}, que añade B a δ(A, 0) = {A}; Δ’(A, 1) = λ-cl(δ({A, B}, 1)) = {C}, que no existía. B y C conservan sus transiciones, y como ninguna cerradura distinta de la de C contiene a C, F’ = {C}. El software marca exactamente esos dos destinos añadidos («(+B)» y «(+C)») y reporta que ningún estado nuevo pasa a ser final.

**Pasos.** n cerraduras más, para cada uno de los n·k pares, una unión de hasta n conjuntos y un cierre: O(k·n³) en el peor caso.

## Construcción de subconjuntos

**Problema.** Dado un AFN (o AFN-λ), obtener un AFD equivalente construyendo sólo los subconjuntos alcanzables.

**Resultado teórico.** Para todo AFN existe un AFD equivalente cuyos estados son subconjuntos de Q (Rabin & Scott, 1959, teorema 11; Hopcroft et al., 2007, Sección 2.3.5, teorema 2.11).

``` text
SUBCONJUNTOS(N)                            # Subconjuntos.resolver
    S₀ ← CIERRE({q₀}); descubiertos ← [S₀]; cola ← [S₀]
    mientras cola ≠ ∅:
        S ← desencolar(cola)                # una etapa por fila
        para a ∈ Σ:
            T ← CIERRE(⋃_{q∈S} δ(q, a))     # Automata.transitar
            si T ∉ descubiertos: agregar T a descubiertos y a cola
            δ_D(S, a) ← T
    F_D ← {S ∈ descubiertos : S ∩ F ≠ ∅}
```

**Ejemplo (192).** A mano: A = {A}; con 0 va a {B} = B y con 1 a {B, C} = C. B: con 0 a {A, B} = D, con 1 a ∅. C: con 0 a δ(B, 0) ∪ δ(C, 0) = {A, B, C} = E. D: con 0 a {A, B} (D), con 1 a {B, C} (C). E: con 0 a E y con 1 a C. Son finales C y E porque contienen al estado final C. El software genera las cinco filas en el mismo orden y con los mismos nombres; JFLAP (*Convert to DFA*) da un AFD de cinco estados equivalente.

**Pasos.** A lo sumo 2ⁿ subconjuntos, y por cada uno k transiciones de costo O(n²): O(k·n²·2ⁿ) en el peor caso; en los casos de prueba se generaron entre 2 y 12 subconjuntos.

## Minimización

**Problema.** Dado un AFD, obtener el AFD con el menor número de estados que reconoce el mismo lenguaje.

**Resultado teórico.** El AFD mínimo es único salvo el nombre de los estados y sus estados corresponden a las clases de la relación de Myhill-Nerode (Nerode, 1958); dos estados son equivalentes si ninguna palabra los distingue, y el algoritmo de llenado de tabla encuentra exactamente los pares distinguibles (Hopcroft et al., 2007, Secciones 4.4.1–4.4.3).

``` text
MINIMIZAR(D)                               # Minimizacion.resolver
    eliminar estados inaccesibles           # Automata.alcanzables
    si δ es parcial: completar con un sumidero      # AFD.completar
    marcar {p, q} si exactamente uno está en F       # ronda 0
    repetir (ronda r = 1, 2, …):
        para cada par {p, q} sin marcar y a ∈ Σ:
            si {δ(p, a), δ(q, a)} está marcado: marcar {p, q} en la ronda r
    hasta que una ronda no marque nada
    clases ← pares sin marcar                        # Minimizacion._clases
    construir el AFD de clases (y retirar la del sumidero si se agregó)
```

**Ejemplo (156).** A mano: el único final es E, así que la ronda 0 marca los cuatro pares con E. En la ronda 1, con el símbolo 1, A y C van a C mientras que B y D van a E; como {C, E} está marcado, se marcan {A, B}, {A, D}, {B, C} y {C, D}. La ronda 2 no marca nada. Quedan {A, C} y {B, D} sin marcar: el mínimo tiene tres estados, {A, C}, {B, D} y E. El software muestra la tabla triangular de las tres rondas con las mismas marcas y el mismo resultado.

**Equivalencia.** Dos AFD son equivalentes si sus mínimos coinciden salvo el nombre; `Equivalencia` lo decide recorriendo ambos mínimos en paralelo, y si no lo son, una búsqueda en anchura sobre el producto da la palabra más corta que los distingue (Hopcroft et al., 2007, Sección 4.4.2).

**Pasos.** Hay n(n − 1)/2 pares y a lo sumo n − 2 rondas útiles, cada una de costo O(k·n²): O(k·n³) en total. El algoritmo de Hopcroft baja el costo a O(k·n log n) (Hopcroft, 1971). La prueba de isomorfismo cuesta O(k·n) y la del contraejemplo O(k·n₁·n₂).

## Validación por lotes

**Problema.** Validar muchas palabras con un mismo autómata y conservar el resultado. No requiere teoría nueva: es SIMULAR(ω) para cada línea.

``` text
LOTE(N, texto)                              # Lote.validar_texto
    para cada línea no vacía que no empiece con #:
        ω ← (λ si la línea es «λ»; si no, la línea)
        registrar (número, ω, ACEPTADA/RECHAZADA/ERROR, estados finales)
    escribir informe                         # Lote.informe → Informe.guardar
```

**Ejemplo.** Con el AFN 263 (palabras que terminan en 01) y `cadenas-ejemplo.txt`: `01`, `1101`, `001` y `0101010101` se aceptan; `0110`, λ y `10` se rechazan, y `012` produce un error porque 2 ∉ Σ. Es lo que se obtiene a mano al revisar el sufijo de cada palabra.

**Pasos.** La suma, sobre las palabras, de O(\|ω\|·n²).
