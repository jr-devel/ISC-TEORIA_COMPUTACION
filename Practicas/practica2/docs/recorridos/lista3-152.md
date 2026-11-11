# Recorridos: Lista 3 · Ejercicio 152

Diagrama y simplificación del AFD de la tabla 152.

Autómata: `lista3-152` (AFD).

## Cadena `1`

- Inicio: {A}
- Lee `1`: {A} ⟶ {E} [A→E]
- **Aceptada**: queda {E} ∈ F.

## Cadena `02`

- Inicio: {A}
- Lee `0`: {A} ⟶ {C} [A→C]
- Lee `2`: {C} ⟶ {F} [C→F]
- **Aceptada**: queda {F} ∈ F.

## Cadena `2021`

- Inicio: {A}
- Lee `2`: {A} ⟶ {B} [A→B]
- Lee `0`: {B} ⟶ {D} [B→D]
- Lee `2`: {D} ⟶ {C} [D→C]
- Lee `1`: {C} ⟶ {D} [C→D]
- **Aceptada**: queda {D} ∈ F.

## Cadena `210201`

- Inicio: {A}
- Lee `2`: {A} ⟶ {B} [A→B]
- Lee `1`: {B} ⟶ {E} [B→E]
- Lee `0`: {E} ⟶ {F} [E→F]
- Lee `2`: {F} ⟶ {C} [F→C]
- Lee `0`: {C} ⟶ {A} [C→A]
- Lee `1`: {A} ⟶ {E} [A→E]
- **Aceptada**: queda {E} ∈ F.

## Cadena `000111100`

- Inicio: {A}
- Lee `0`: {A} ⟶ {C} [A→C]
- Lee `0`: {C} ⟶ {A} [C→A]
- Lee `0`: {A} ⟶ {C} [A→C]
- Lee `1`: {C} ⟶ {D} [C→D]
- Lee `1`: {D} ⟶ {B} [D→B]
- Lee `1`: {B} ⟶ {E} [B→E]
- Lee `1`: {E} ⟶ {B} [E→B]
- Lee `0`: {B} ⟶ {D} [B→D]
- Lee `0`: {D} ⟶ {F} [D→F]
- **Aceptada**: queda {F} ∈ F.

## Cadena λ

- Inicio: {A}
- **Rechazada**: ningún estado de {A} es de aceptación.

## Cadena `0`

- Inicio: {A}
- Lee `0`: {A} ⟶ {C} [A→C]
- **Rechazada**: ningún estado de {C} es de aceptación.

## Cadena `211`

- Inicio: {A}
- Lee `2`: {A} ⟶ {B} [A→B]
- Lee `1`: {B} ⟶ {E} [B→E]
- Lee `1`: {E} ⟶ {B} [E→B]
- **Rechazada**: ningún estado de {B} es de aceptación.

## Cadena `02002`

- Inicio: {A}
- Lee `0`: {A} ⟶ {C} [A→C]
- Lee `2`: {C} ⟶ {F} [C→F]
- Lee `0`: {F} ⟶ {D} [F→D]
- Lee `0`: {D} ⟶ {F} [D→F]
- Lee `2`: {F} ⟶ {C} [F→C]
- **Rechazada**: ningún estado de {C} es de aceptación.

## Cadena `12111020`

- Inicio: {A}
- Lee `1`: {A} ⟶ {E} [A→E]
- Lee `2`: {E} ⟶ {A} [E→A]
- Lee `1`: {A} ⟶ {E} [A→E]
- Lee `1`: {E} ⟶ {B} [E→B]
- Lee `1`: {B} ⟶ {E} [B→E]
- Lee `0`: {E} ⟶ {F} [E→F]
- Lee `2`: {F} ⟶ {C} [F→C]
- Lee `0`: {C} ⟶ {A} [C→A]
- **Rechazada**: ningún estado de {A} es de aceptación.
