# Recorridos: Lista 3 · Ejercicio 151

Diagrama y simplificación del AFD de la tabla 151.

Autómata: `lista3-151` (AFD).

## Cadena `1`

- Inicio: {A}
- Lee `1`: {A} ⟶ {E} [A→E]
- **Aceptada**: queda {E} ∈ F.

## Cadena `0111`

- Inicio: {A}
- Lee `0`: {A} ⟶ {C} [A→C]
- Lee `1`: {C} ⟶ {G} [C→G]
- Lee `1`: {G} ⟶ {I} [G→I]
- Lee `1`: {I} ⟶ {E} [I→E]
- **Aceptada**: queda {E} ∈ F.

## Cadena `1001`

- Inicio: {A}
- Lee `1`: {A} ⟶ {E} [A→E]
- Lee `0`: {E} ⟶ {I} [E→I]
- Lee `0`: {I} ⟶ {J} [I→J]
- Lee `1`: {J} ⟶ {E} [J→E]
- **Aceptada**: queda {E} ∈ F.

## Cadena `0100111`

- Inicio: {A}
- Lee `0`: {A} ⟶ {C} [A→C]
- Lee `1`: {C} ⟶ {G} [C→G]
- Lee `0`: {G} ⟶ {F} [G→F]
- Lee `0`: {F} ⟶ {D} [F→D]
- Lee `1`: {D} ⟶ {E} [D→E]
- Lee `1`: {E} ⟶ {B} [E→B]
- Lee `1`: {B} ⟶ {E} [B→E]
- **Aceptada**: queda {E} ∈ F.

## Cadena `0010111011001`

- Inicio: {A}
- Lee `0`: {A} ⟶ {C} [A→C]
- Lee `0`: {C} ⟶ {A} [C→A]
- Lee `1`: {A} ⟶ {E} [A→E]
- Lee `0`: {E} ⟶ {I} [E→I]
- Lee `1`: {I} ⟶ {E} [I→E]
- Lee `1`: {E} ⟶ {B} [E→B]
- Lee `1`: {B} ⟶ {E} [B→E]
- Lee `0`: {E} ⟶ {I} [E→I]
- Lee `1`: {I} ⟶ {E} [I→E]
- Lee `1`: {E} ⟶ {B} [E→B]
- Lee `0`: {B} ⟶ {F} [B→F]
- Lee `0`: {F} ⟶ {D} [F→D]
- Lee `1`: {D} ⟶ {E} [D→E]
- **Aceptada**: queda {E} ∈ F.

## Cadena λ

- Inicio: {A}
- **Rechazada**: ningún estado de {A} es de aceptación.

## Cadena `001001000`

- Inicio: {A}
- Lee `0`: {A} ⟶ {C} [A→C]
- Lee `0`: {C} ⟶ {A} [C→A]
- Lee `1`: {A} ⟶ {E} [A→E]
- Lee `0`: {E} ⟶ {I} [E→I]
- Lee `0`: {I} ⟶ {J} [I→J]
- Lee `1`: {J} ⟶ {E} [J→E]
- Lee `0`: {E} ⟶ {I} [E→I]
- Lee `0`: {I} ⟶ {J} [I→J]
- Lee `0`: {J} ⟶ {I} [J→I]
- **Rechazada**: ningún estado de {I} es de aceptación.

## Cadena `100100000`

- Inicio: {A}
- Lee `1`: {A} ⟶ {E} [A→E]
- Lee `0`: {E} ⟶ {I} [E→I]
- Lee `0`: {I} ⟶ {J} [I→J]
- Lee `1`: {J} ⟶ {E} [J→E]
- Lee `0`: {E} ⟶ {I} [E→I]
- Lee `0`: {I} ⟶ {J} [I→J]
- Lee `0`: {J} ⟶ {I} [J→I]
- Lee `0`: {I} ⟶ {J} [I→J]
- Lee `0`: {J} ⟶ {I} [J→I]
- **Rechazada**: ningún estado de {I} es de aceptación.

## Cadena `1101000000`

- Inicio: {A}
- Lee `1`: {A} ⟶ {E} [A→E]
- Lee `1`: {E} ⟶ {B} [E→B]
- Lee `0`: {B} ⟶ {F} [B→F]
- Lee `1`: {F} ⟶ {H} [F→H]
- Lee `0`: {H} ⟶ {C} [H→C]
- Lee `0`: {C} ⟶ {A} [C→A]
- Lee `0`: {A} ⟶ {C} [A→C]
- Lee `0`: {C} ⟶ {A} [C→A]
- Lee `0`: {A} ⟶ {C} [A→C]
- Lee `0`: {C} ⟶ {A} [C→A]
- **Rechazada**: ningún estado de {A} es de aceptación.

## Cadena `01000100000101`

- Inicio: {A}
- Lee `0`: {A} ⟶ {C} [A→C]
- Lee `1`: {C} ⟶ {G} [C→G]
- Lee `0`: {G} ⟶ {F} [G→F]
- Lee `0`: {F} ⟶ {D} [F→D]
- Lee `0`: {D} ⟶ {C} [D→C]
- Lee `1`: {C} ⟶ {G} [C→G]
- Lee `0`: {G} ⟶ {F} [G→F]
- Lee `0`: {F} ⟶ {D} [F→D]
- Lee `0`: {D} ⟶ {C} [D→C]
- Lee `0`: {C} ⟶ {A} [C→A]
- Lee `0`: {A} ⟶ {C} [A→C]
- Lee `1`: {C} ⟶ {G} [C→G]
- Lee `0`: {G} ⟶ {F} [G→F]
- Lee `1`: {F} ⟶ {H} [F→H]
- **Rechazada**: ningún estado de {H} es de aceptación.
