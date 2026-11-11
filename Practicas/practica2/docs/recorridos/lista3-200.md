# Recorridos: Lista 3 · Ejercicio 200

AFN-λ de la tabla 200: diagrama, AFD equivalente e incisos.

Autómata: `lista3-200` (AFN-λ).

## Cadena `1`

- Inicio: {A}; con cierre λ, {A, B}
- Lee `1`: {A, B} ⟶ {A, B, C, E, F} [A→A, A→C, A→F, B→B, B→E] (bifurcación)
- **Aceptada**: queda {E} ∈ F.

## Cadena `01`

- Inicio: {A}; con cierre λ, {A, B}
- Lee `0`: {A, B} ⟶ {C, D, E, F} [A→F, B→C, B→D] (bifurcación); cierre λ añade {E}
- Lee `1`: {C, D, E, F} ⟶ {A, B, C, D, E, F} [C→A, C→C, D→B, D→E, E→D] (bifurcación); cierre λ añade {F}
- **Aceptada**: queda {D, E} ∈ F.

## Cadena `1000`

- Inicio: {A}; con cierre λ, {A, B}
- Lee `1`: {A, B} ⟶ {A, B, C, E, F} [A→A, A→C, A→F, B→B, B→E] (bifurcación)
- Lee `0`: {A, B, C, E, F} ⟶ {B, C, D, E, F} [A→F, B→C, B→D, F→B, F→E]
- Lee `0`: {B, C, D, E, F} ⟶ {A, B, C, D, E, F} [B→C, B→D, D→A, D→C, F→B, F→E]; cierre λ añade {F}
- Lee `0`: {A, B, C, D, E, F} ⟶ {A, B, C, D, E, F} [A→F, B→C, B→D, D→A, D→C, F→B, F→E]
- **Aceptada**: queda {D, E} ∈ F.

## Cadena `100100`

- Inicio: {A}; con cierre λ, {A, B}
- Lee `1`: {A, B} ⟶ {A, B, C, E, F} [A→A, A→C, A→F, B→B, B→E] (bifurcación)
- Lee `0`: {A, B, C, E, F} ⟶ {B, C, D, E, F} [A→F, B→C, B→D, F→B, F→E]
- Lee `0`: {B, C, D, E, F} ⟶ {A, B, C, D, E, F} [B→C, B→D, D→A, D→C, F→B, F→E]; cierre λ añade {F}
- Lee `1`: {A, B, C, D, E, F} ⟶ {A, B, C, D, E, F} [A→A, A→C, A→F, B→B, B→E, C→A, C→C, D→B, D→E, E→D]
- Lee `0`: {A, B, C, D, E, F} ⟶ {A, B, C, D, E, F} [A→F, B→C, B→D, D→A, D→C, F→B, F→E]
- Lee `0`: {A, B, C, D, E, F} ⟶ {A, B, C, D, E, F} [A→F, B→C, B→D, D→A, D→C, F→B, F→E]
- **Aceptada**: queda {D, E} ∈ F.

## Cadena `101010101`

- Inicio: {A}; con cierre λ, {A, B}
- Lee `1`: {A, B} ⟶ {A, B, C, E, F} [A→A, A→C, A→F, B→B, B→E] (bifurcación)
- Lee `0`: {A, B, C, E, F} ⟶ {B, C, D, E, F} [A→F, B→C, B→D, F→B, F→E]
- Lee `1`: {B, C, D, E, F} ⟶ {A, B, C, D, E, F} [B→B, B→E, C→A, C→C, D→B, D→E, E→D]; cierre λ añade {F}
- Lee `0`: {A, B, C, D, E, F} ⟶ {A, B, C, D, E, F} [A→F, B→C, B→D, D→A, D→C, F→B, F→E]
- Lee `1`: {A, B, C, D, E, F} ⟶ {A, B, C, D, E, F} [A→A, A→C, A→F, B→B, B→E, C→A, C→C, D→B, D→E, E→D]
- Lee `0`: {A, B, C, D, E, F} ⟶ {A, B, C, D, E, F} [A→F, B→C, B→D, D→A, D→C, F→B, F→E]
- Lee `1`: {A, B, C, D, E, F} ⟶ {A, B, C, D, E, F} [A→A, A→C, A→F, B→B, B→E, C→A, C→C, D→B, D→E, E→D]
- Lee `0`: {A, B, C, D, E, F} ⟶ {A, B, C, D, E, F} [A→F, B→C, B→D, D→A, D→C, F→B, F→E]
- Lee `1`: {A, B, C, D, E, F} ⟶ {A, B, C, D, E, F} [A→A, A→C, A→F, B→B, B→E, C→A, C→C, D→B, D→E, E→D]
- **Aceptada**: queda {D, E} ∈ F.

## Cadena λ

- Inicio: {A}; con cierre λ, {A, B}
- **Rechazada**: ningún estado de {A, B} es de aceptación.

## Cadena `0`

- Inicio: {A}; con cierre λ, {A, B}
- Lee `0`: {A, B} ⟶ {C, D, E, F} [A→F, B→C, B→D] (bifurcación); cierre λ añade {E}
- **Aceptada**: queda {D, E} ∈ F.
