# Recorridos: Lista 3 · Ejercicio 195

AFN de la tabla 195: AFD equivalente y δ̂(Z, ω).

Autómata: `lista3-195` (AFN).

## Cadena `01`

- Inicio: {A}
- Lee `0`: {A} ⟶ {A, B} [A→A, A→B] (bifurcación)
- Lee `1`: {A, B} ⟶ {A, C} [A→A, B→C]
- **Aceptada**: queda {C} ∈ F.

## Cadena `101`

- Inicio: {A}
- Lee `1`: {A} ⟶ {A} [A→A]
- Lee `0`: {A} ⟶ {A, B} [A→A, A→B] (bifurcación)
- Lee `1`: {A, B} ⟶ {A, C} [A→A, B→C]
- **Aceptada**: queda {C} ∈ F.

## Cadena `01110`

- Inicio: {A}
- Lee `0`: {A} ⟶ {A, B} [A→A, A→B] (bifurcación)
- Lee `1`: {A, B} ⟶ {A, C} [A→A, B→C]
- Lee `1`: {A, C} ⟶ {A, D} [A→A, C→D]
- Lee `1`: {A, D} ⟶ {A, E} [A→A, D→E]
- Lee `0`: {A, E} ⟶ {A, B, E} [A→A, A→B, E→E] (bifurcación)
- **Aceptada**: queda {E} ∈ F.

## Cadena `0100111`

- Inicio: {A}
- Lee `0`: {A} ⟶ {A, B} [A→A, A→B] (bifurcación)
- Lee `1`: {A, B} ⟶ {A, C} [A→A, B→C]
- Lee `0`: {A, C} ⟶ {A, B} [A→A, A→B, C→A]
- Lee `0`: {A, B} ⟶ {A, B} [A→A, A→B, B→A]
- Lee `1`: {A, B} ⟶ {A, C} [A→A, B→C]
- Lee `1`: {A, C} ⟶ {A, D} [A→A, C→D]
- Lee `1`: {A, D} ⟶ {A, E} [A→A, D→E]
- **Aceptada**: queda {E} ∈ F.

## Cadena `1001110111`

- Inicio: {A}
- Lee `1`: {A} ⟶ {A} [A→A]
- Lee `0`: {A} ⟶ {A, B} [A→A, A→B] (bifurcación)
- Lee `0`: {A, B} ⟶ {A, B} [A→A, A→B, B→A]
- Lee `1`: {A, B} ⟶ {A, C} [A→A, B→C]
- Lee `1`: {A, C} ⟶ {A, D} [A→A, C→D]
- Lee `1`: {A, D} ⟶ {A, E} [A→A, D→E]
- Lee `0`: {A, E} ⟶ {A, B, E} [A→A, A→B, E→E] (bifurcación)
- Lee `1`: {A, B, E} ⟶ {A, C, D} [A→A, B→C, E→C, E→D]
- Lee `1`: {A, C, D} ⟶ {A, D, E} [A→A, C→D, D→E]
- Lee `1`: {A, D, E} ⟶ {A, C, D, E} [A→A, D→E, E→C, E→D] (bifurcación)
- **Aceptada**: queda {C, E} ∈ F.

## Cadena λ

- Inicio: {A}
- **Rechazada**: ningún estado de {A} es de aceptación.

## Cadena `1`

- Inicio: {A}
- Lee `1`: {A} ⟶ {A} [A→A]
- **Rechazada**: ningún estado de {A} es de aceptación.

## Cadena `011`

- Inicio: {A}
- Lee `0`: {A} ⟶ {A, B} [A→A, A→B] (bifurcación)
- Lee `1`: {A, B} ⟶ {A, C} [A→A, B→C]
- Lee `1`: {A, C} ⟶ {A, D} [A→A, C→D]
- **Rechazada**: ningún estado de {A, D} es de aceptación.

## Cadena `00010`

- Inicio: {A}
- Lee `0`: {A} ⟶ {A, B} [A→A, A→B] (bifurcación)
- Lee `0`: {A, B} ⟶ {A, B} [A→A, A→B, B→A]
- Lee `0`: {A, B} ⟶ {A, B} [A→A, A→B, B→A]
- Lee `1`: {A, B} ⟶ {A, C} [A→A, B→C]
- Lee `0`: {A, C} ⟶ {A, B} [A→A, A→B, C→A]
- **Rechazada**: ningún estado de {A, B} es de aceptación.

## Cadena `11100110`

- Inicio: {A}
- Lee `1`: {A} ⟶ {A} [A→A]
- Lee `1`: {A} ⟶ {A} [A→A]
- Lee `1`: {A} ⟶ {A} [A→A]
- Lee `0`: {A} ⟶ {A, B} [A→A, A→B] (bifurcación)
- Lee `0`: {A, B} ⟶ {A, B} [A→A, A→B, B→A]
- Lee `1`: {A, B} ⟶ {A, C} [A→A, B→C]
- Lee `1`: {A, C} ⟶ {A, D} [A→A, C→D]
- Lee `0`: {A, D} ⟶ {A, B, D} [A→A, A→B, D→D] (bifurcación)
- **Rechazada**: ningún estado de {A, B, D} es de aceptación.
