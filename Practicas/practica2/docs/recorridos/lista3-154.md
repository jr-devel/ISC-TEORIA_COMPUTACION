# Recorridos: Lista 3 · Ejercicio 154

Diagrama y simplificación del AFD de la tabla 154.

Autómata: `lista3-154` (AFD).

## Cadena `01`

- Inicio: {A}
- Lee `0`: {A} ⟶ {D} [A→D]
- Lee `1`: {D} ⟶ {G} [D→G]
- **Aceptada**: queda {G} ∈ F.

## Cadena `001`

- Inicio: {A}
- Lee `0`: {A} ⟶ {D} [A→D]
- Lee `0`: {D} ⟶ {C} [D→C]
- Lee `1`: {C} ⟶ {E} [C→E]
- **Aceptada**: queda {E} ∈ F.

## Cadena `10110`

- Inicio: {A}
- Lee `1`: {A} ⟶ {K} [A→K]
- Lee `0`: {K} ⟶ {C} [K→C]
- Lee `1`: {C} ⟶ {E} [C→E]
- Lee `1`: {E} ⟶ {I} [E→I]
- Lee `0`: {I} ⟶ {G} [I→G]
- **Aceptada**: queda {G} ∈ F.

## Cadena `1111001`

- Inicio: {A}
- Lee `1`: {A} ⟶ {K} [A→K]
- Lee `1`: {K} ⟶ {F} [K→F]
- Lee `1`: {F} ⟶ {E} [F→E]
- Lee `1`: {E} ⟶ {I} [E→I]
- Lee `0`: {I} ⟶ {G} [I→G]
- Lee `0`: {G} ⟶ {C} [G→C]
- Lee `1`: {C} ⟶ {E} [C→E]
- **Aceptada**: queda {E} ∈ F.

## Cadena `1001000000`

- Inicio: {A}
- Lee `1`: {A} ⟶ {K} [A→K]
- Lee `0`: {K} ⟶ {C} [K→C]
- Lee `0`: {C} ⟶ {I} [C→I]
- Lee `1`: {I} ⟶ {K} [I→K]
- Lee `0`: {K} ⟶ {C} [K→C]
- Lee `0`: {C} ⟶ {I} [C→I]
- Lee `0`: {I} ⟶ {G} [I→G]
- Lee `0`: {G} ⟶ {C} [G→C]
- Lee `0`: {C} ⟶ {I} [C→I]
- Lee `0`: {I} ⟶ {G} [I→G]
- **Aceptada**: queda {G} ∈ F.

## Cadena λ

- Inicio: {A}
- **Rechazada**: ningún estado de {A} es de aceptación.

## Cadena `1`

- Inicio: {A}
- Lee `1`: {A} ⟶ {K} [A→K]
- **Rechazada**: ningún estado de {K} es de aceptación.

## Cadena `100`

- Inicio: {A}
- Lee `1`: {A} ⟶ {K} [A→K]
- Lee `0`: {K} ⟶ {C} [K→C]
- Lee `0`: {C} ⟶ {I} [C→I]
- **Rechazada**: ningún estado de {I} es de aceptación.

## Cadena `00010`

- Inicio: {A}
- Lee `0`: {A} ⟶ {D} [A→D]
- Lee `0`: {D} ⟶ {C} [D→C]
- Lee `0`: {C} ⟶ {I} [C→I]
- Lee `1`: {I} ⟶ {K} [I→K]
- Lee `0`: {K} ⟶ {C} [K→C]
- **Rechazada**: ningún estado de {C} es de aceptación.

## Cadena `00111110`

- Inicio: {A}
- Lee `0`: {A} ⟶ {D} [A→D]
- Lee `0`: {D} ⟶ {C} [D→C]
- Lee `1`: {C} ⟶ {E} [C→E]
- Lee `1`: {E} ⟶ {I} [E→I]
- Lee `1`: {I} ⟶ {K} [I→K]
- Lee `1`: {K} ⟶ {F} [K→F]
- Lee `1`: {F} ⟶ {E} [F→E]
- Lee `0`: {E} ⟶ {K} [E→K]
- **Rechazada**: ningún estado de {K} es de aceptación.
