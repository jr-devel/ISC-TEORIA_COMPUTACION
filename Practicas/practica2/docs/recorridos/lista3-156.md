# Recorridos: Lista 3 · Ejercicio 156

Diagrama y simplificación del AFD de la tabla 156 (tabla transcrita del diagrama).

Autómata: `lista3-156` (AFD).

## Cadena `01`

- Inicio: {A}
- Lee `0`: {A} ⟶ {B} [A→B]
- Lee `1`: {B} ⟶ {E} [B→E]
- **Aceptada**: queda {E} ∈ F.

## Cadena `011`

- Inicio: {A}
- Lee `0`: {A} ⟶ {B} [A→B]
- Lee `1`: {B} ⟶ {E} [B→E]
- Lee `1`: {E} ⟶ {E} [E→E]
- **Aceptada**: queda {E} ∈ F.

## Cadena `10001`

- Inicio: {A}
- Lee `1`: {A} ⟶ {C} [A→C]
- Lee `0`: {C} ⟶ {D} [C→D]
- Lee `0`: {D} ⟶ {C} [D→C]
- Lee `0`: {C} ⟶ {D} [C→D]
- Lee `1`: {D} ⟶ {E} [D→E]
- **Aceptada**: queda {E} ∈ F.

## Cadena `1100011`

- Inicio: {A}
- Lee `1`: {A} ⟶ {C} [A→C]
- Lee `1`: {C} ⟶ {C} [C→C]
- Lee `0`: {C} ⟶ {D} [C→D]
- Lee `0`: {D} ⟶ {C} [D→C]
- Lee `0`: {C} ⟶ {D} [C→D]
- Lee `1`: {D} ⟶ {E} [D→E]
- Lee `1`: {E} ⟶ {E} [E→E]
- **Aceptada**: queda {E} ∈ F.

## Cadena `1100000001`

- Inicio: {A}
- Lee `1`: {A} ⟶ {C} [A→C]
- Lee `1`: {C} ⟶ {C} [C→C]
- Lee `0`: {C} ⟶ {D} [C→D]
- Lee `0`: {D} ⟶ {C} [D→C]
- Lee `0`: {C} ⟶ {D} [C→D]
- Lee `0`: {D} ⟶ {C} [D→C]
- Lee `0`: {C} ⟶ {D} [C→D]
- Lee `0`: {D} ⟶ {C} [D→C]
- Lee `0`: {C} ⟶ {D} [C→D]
- Lee `1`: {D} ⟶ {E} [D→E]
- **Aceptada**: queda {E} ∈ F.

## Cadena λ

- Inicio: {A}
- **Rechazada**: ningún estado de {A} es de aceptación.

## Cadena `1`

- Inicio: {A}
- Lee `1`: {A} ⟶ {C} [A→C]
- **Rechazada**: ningún estado de {C} es de aceptación.

## Cadena `010`

- Inicio: {A}
- Lee `0`: {A} ⟶ {B} [A→B]
- Lee `1`: {B} ⟶ {E} [B→E]
- Lee `0`: {E} ⟶ {B} [E→B]
- **Rechazada**: ningún estado de {B} es de aceptación.

## Cadena `10000`

- Inicio: {A}
- Lee `1`: {A} ⟶ {C} [A→C]
- Lee `0`: {C} ⟶ {D} [C→D]
- Lee `0`: {D} ⟶ {C} [D→C]
- Lee `0`: {C} ⟶ {D} [C→D]
- Lee `0`: {D} ⟶ {C} [D→C]
- **Rechazada**: ningún estado de {C} es de aceptación.

## Cadena `10000001`

- Inicio: {A}
- Lee `1`: {A} ⟶ {C} [A→C]
- Lee `0`: {C} ⟶ {D} [C→D]
- Lee `0`: {D} ⟶ {C} [D→C]
- Lee `0`: {C} ⟶ {D} [C→D]
- Lee `0`: {D} ⟶ {C} [D→C]
- Lee `0`: {C} ⟶ {D} [C→D]
- Lee `0`: {D} ⟶ {C} [D→C]
- Lee `1`: {C} ⟶ {C} [C→C]
- **Rechazada**: ningún estado de {C} es de aceptación.
