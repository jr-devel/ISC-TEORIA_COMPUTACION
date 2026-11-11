# Recorridos: Lista 3 · Ejercicio 194

AFN de la tabla 194: AFD equivalente y δ̂(Z, ω).

Autómata: `lista3-194` (AFN).

## Cadena `1`

- Inicio: {A}
- Lee `1`: {A} ⟶ {A, C} [A→A, A→C] (bifurcación)
- **Aceptada**: queda {C} ∈ F.

## Cadena `11`

- Inicio: {A}
- Lee `1`: {A} ⟶ {A, C} [A→A, A→C] (bifurcación)
- Lee `1`: {A, C} ⟶ {A, B, C, D} [A→A, A→C, C→A, C→B, C→C, C→D] (bifurcación)
- **Aceptada**: queda {C, D} ∈ F.

## Cadena `0011`

- Inicio: {A}
- Lee `0`: {A} ⟶ {A, B} [A→A, A→B] (bifurcación)
- Lee `0`: {A, B} ⟶ {A, B} [A→A, A→B]
- Lee `1`: {A, B} ⟶ {A, C} [A→A, A→C]
- Lee `1`: {A, C} ⟶ {A, B, C, D} [A→A, A→C, C→A, C→B, C→C, C→D] (bifurcación)
- **Aceptada**: queda {C, D} ∈ F.

## Cadena `102211`

- Inicio: {A}
- Lee `1`: {A} ⟶ {A, C} [A→A, A→C] (bifurcación)
- Lee `0`: {A, C} ⟶ {A, B} [A→A, A→B, C→A, C→B]
- Lee `2`: {A, B} ⟶ {A} [A→A]
- Lee `2`: {A} ⟶ {A} [A→A]
- Lee `1`: {A} ⟶ {A, C} [A→A, A→C] (bifurcación)
- Lee `1`: {A, C} ⟶ {A, B, C, D} [A→A, A→C, C→A, C→B, C→C, C→D] (bifurcación)
- **Aceptada**: queda {C, D} ∈ F.

## Cadena `111212021`

- Inicio: {A}
- Lee `1`: {A} ⟶ {A, C} [A→A, A→C] (bifurcación)
- Lee `1`: {A, C} ⟶ {A, B, C, D} [A→A, A→C, C→A, C→B, C→C, C→D] (bifurcación)
- Lee `1`: {A, B, C, D} ⟶ {A, B, C, D} [A→A, A→C, C→A, C→B, C→C, C→D, D→A]
- Lee `2`: {A, B, C, D} ⟶ {A} [A→A]
- Lee `1`: {A} ⟶ {A, C} [A→A, A→C] (bifurcación)
- Lee `2`: {A, C} ⟶ {A} [A→A]
- Lee `0`: {A} ⟶ {A, B} [A→A, A→B] (bifurcación)
- Lee `2`: {A, B} ⟶ {A} [A→A]
- Lee `1`: {A} ⟶ {A, C} [A→A, A→C] (bifurcación)
- **Aceptada**: queda {C} ∈ F.

## Cadena λ

- Inicio: {A}
- **Rechazada**: ningún estado de {A} es de aceptación.

## Cadena `2`

- Inicio: {A}
- Lee `2`: {A} ⟶ {A} [A→A]
- **Rechazada**: ningún estado de {A} es de aceptación.

## Cadena `220`

- Inicio: {A}
- Lee `2`: {A} ⟶ {A} [A→A]
- Lee `2`: {A} ⟶ {A} [A→A]
- Lee `0`: {A} ⟶ {A, B} [A→A, A→B] (bifurcación)
- **Rechazada**: ningún estado de {A, B} es de aceptación.

## Cadena `11222`

- Inicio: {A}
- Lee `1`: {A} ⟶ {A, C} [A→A, A→C] (bifurcación)
- Lee `1`: {A, C} ⟶ {A, B, C, D} [A→A, A→C, C→A, C→B, C→C, C→D] (bifurcación)
- Lee `2`: {A, B, C, D} ⟶ {A} [A→A]
- Lee `2`: {A} ⟶ {A} [A→A]
- Lee `2`: {A} ⟶ {A} [A→A]
- **Rechazada**: ningún estado de {A} es de aceptación.

## Cadena `02122220`

- Inicio: {A}
- Lee `0`: {A} ⟶ {A, B} [A→A, A→B] (bifurcación)
- Lee `2`: {A, B} ⟶ {A} [A→A]
- Lee `1`: {A} ⟶ {A, C} [A→A, A→C] (bifurcación)
- Lee `2`: {A, C} ⟶ {A} [A→A]
- Lee `2`: {A} ⟶ {A} [A→A]
- Lee `2`: {A} ⟶ {A} [A→A]
- Lee `2`: {A} ⟶ {A} [A→A]
- Lee `0`: {A} ⟶ {A, B} [A→A, A→B] (bifurcación)
- **Rechazada**: ningún estado de {A, B} es de aceptación.
