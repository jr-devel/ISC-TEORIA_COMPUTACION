# Recorridos: Lista 3 · Ejercicio 153

Diagrama y simplificación del AFD de la tabla 153.

Autómata: `lista3-153` (AFD).

## Cadena `10`

- Inicio: {A}
- Lee `1`: {A} ⟶ {C} [A→C]
- Lee `0`: {C} ⟶ {F} [C→F]
- **Aceptada**: queda {F} ∈ F.

## Cadena `101`

- Inicio: {A}
- Lee `1`: {A} ⟶ {C} [A→C]
- Lee `0`: {C} ⟶ {F} [C→F]
- Lee `1`: {F} ⟶ {D} [F→D]
- **Aceptada**: queda {D} ∈ F.

## Cadena `01101`

- Inicio: {A}
- Lee `0`: {A} ⟶ {B} [A→B]
- Lee `1`: {B} ⟶ {E} [B→E]
- Lee `1`: {E} ⟶ {G} [E→G]
- Lee `0`: {G} ⟶ {F} [G→F]
- Lee `1`: {F} ⟶ {D} [F→D]
- **Aceptada**: queda {D} ∈ F.

## Cadena `0011000`

- Inicio: {A}
- Lee `0`: {A} ⟶ {B} [A→B]
- Lee `0`: {B} ⟶ {D} [B→D]
- Lee `1`: {D} ⟶ {E} [D→E]
- Lee `1`: {E} ⟶ {G} [E→G]
- Lee `0`: {G} ⟶ {F} [G→F]
- Lee `0`: {F} ⟶ {E} [F→E]
- Lee `0`: {E} ⟶ {F} [E→F]
- **Aceptada**: queda {F} ∈ F.

## Cadena `1000000010`

- Inicio: {A}
- Lee `1`: {A} ⟶ {C} [A→C]
- Lee `0`: {C} ⟶ {F} [C→F]
- Lee `0`: {F} ⟶ {E} [F→E]
- Lee `0`: {E} ⟶ {F} [E→F]
- Lee `0`: {F} ⟶ {E} [F→E]
- Lee `0`: {E} ⟶ {F} [E→F]
- Lee `0`: {F} ⟶ {E} [F→E]
- Lee `0`: {E} ⟶ {F} [E→F]
- Lee `1`: {F} ⟶ {D} [F→D]
- Lee `0`: {D} ⟶ {D} [D→D]
- **Aceptada**: queda {D} ∈ F.

## Cadena λ

- Inicio: {A}
- **Rechazada**: ningún estado de {A} es de aceptación.

## Cadena `1`

- Inicio: {A}
- Lee `1`: {A} ⟶ {C} [A→C]
- **Rechazada**: ningún estado de {C} es de aceptación.

## Cadena `100`

- Inicio: {A}
- Lee `1`: {A} ⟶ {C} [A→C]
- Lee `0`: {C} ⟶ {F} [C→F]
- Lee `0`: {F} ⟶ {E} [F→E]
- **Rechazada**: ningún estado de {E} es de aceptación.

## Cadena `10101`

- Inicio: {A}
- Lee `1`: {A} ⟶ {C} [A→C]
- Lee `0`: {C} ⟶ {F} [C→F]
- Lee `1`: {F} ⟶ {D} [F→D]
- Lee `0`: {D} ⟶ {D} [D→D]
- Lee `1`: {D} ⟶ {E} [D→E]
- **Rechazada**: ningún estado de {E} es de aceptación.

## Cadena `00101001`

- Inicio: {A}
- Lee `0`: {A} ⟶ {B} [A→B]
- Lee `0`: {B} ⟶ {D} [B→D]
- Lee `1`: {D} ⟶ {E} [D→E]
- Lee `0`: {E} ⟶ {F} [E→F]
- Lee `1`: {F} ⟶ {D} [F→D]
- Lee `0`: {D} ⟶ {D} [D→D]
- Lee `0`: {D} ⟶ {D} [D→D]
- Lee `1`: {D} ⟶ {E} [D→E]
- **Rechazada**: ningún estado de {E} es de aceptación.

## Cadena `0`

- Inicio: {A}
- Lee `0`: {A} ⟶ {B} [A→B]
- **Rechazada**: ningún estado de {B} es de aceptación.
