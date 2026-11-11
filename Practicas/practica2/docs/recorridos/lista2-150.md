# Recorridos: Lista 2 · Ejercicio 150

AFD de la tabla (→A; B, C, D finales). Halle δ̂(B, 10a11), δ̂(B, aa1100), δ̂(A, a01a01), δ̂(C, a11a00).

Autómata: `lista2-150` (AFD).

## Cadena `1`

- Inicio: {A}
- Lee `1`: {A} ⟶ {C} [A→C]
- **Aceptada**: queda {C} ∈ F.

## Cadena `aa`

- Inicio: {A}
- Lee `a`: {A} ⟶ {D} [A→D]
- Lee `a`: {D} ⟶ {B} [D→B]
- **Aceptada**: queda {B} ∈ F.

## Cadena `1a01`

- Inicio: {A}
- Lee `1`: {A} ⟶ {C} [A→C]
- Lee `a`: {C} ⟶ {D} [C→D]
- Lee `0`: {D} ⟶ {B} [D→B]
- Lee `1`: {B} ⟶ {C} [B→C]
- **Aceptada**: queda {C} ∈ F.

## Cadena `1a001a`

- Inicio: {A}
- Lee `1`: {A} ⟶ {C} [A→C]
- Lee `a`: {C} ⟶ {D} [C→D]
- Lee `0`: {D} ⟶ {B} [D→B]
- Lee `0`: {B} ⟶ {B} [B→B]
- Lee `1`: {B} ⟶ {C} [B→C]
- Lee `a`: {C} ⟶ {D} [C→D]
- **Aceptada**: queda {D} ∈ F.

## Cadena `0a01a1001`

- Inicio: {A}
- Lee `0`: {A} ⟶ {B} [A→B]
- Lee `a`: {B} ⟶ {C} [B→C]
- Lee `0`: {C} ⟶ {A} [C→A]
- Lee `1`: {A} ⟶ {C} [A→C]
- Lee `a`: {C} ⟶ {D} [C→D]
- Lee `1`: {D} ⟶ {B} [D→B]
- Lee `0`: {B} ⟶ {B} [B→B]
- Lee `0`: {B} ⟶ {B} [B→B]
- Lee `1`: {B} ⟶ {C} [B→C]
- **Aceptada**: queda {C} ∈ F.

## Cadena λ

- Inicio: {A}
- **Rechazada**: ningún estado de {A} es de aceptación.

## Cadena `01011`

- Inicio: {A}
- Lee `0`: {A} ⟶ {B} [A→B]
- Lee `1`: {B} ⟶ {C} [B→C]
- Lee `0`: {C} ⟶ {A} [C→A]
- Lee `1`: {A} ⟶ {C} [A→C]
- Lee `1`: {C} ⟶ {A} [C→A]
- **Rechazada**: ningún estado de {A} es de aceptación.

## Cadena `0aa10a0`

- Inicio: {A}
- Lee `0`: {A} ⟶ {B} [A→B]
- Lee `a`: {B} ⟶ {C} [B→C]
- Lee `a`: {C} ⟶ {D} [C→D]
- Lee `1`: {D} ⟶ {B} [D→B]
- Lee `0`: {B} ⟶ {B} [B→B]
- Lee `a`: {B} ⟶ {C} [B→C]
- Lee `0`: {C} ⟶ {A} [C→A]
- **Rechazada**: ningún estado de {A} es de aceptación.

## Cadena `001a01011`

- Inicio: {A}
- Lee `0`: {A} ⟶ {B} [A→B]
- Lee `0`: {B} ⟶ {B} [B→B]
- Lee `1`: {B} ⟶ {C} [B→C]
- Lee `a`: {C} ⟶ {D} [C→D]
- Lee `0`: {D} ⟶ {B} [D→B]
- Lee `1`: {B} ⟶ {C} [B→C]
- Lee `0`: {C} ⟶ {A} [C→A]
- Lee `1`: {A} ⟶ {C} [A→C]
- Lee `1`: {C} ⟶ {A} [C→A]
- **Rechazada**: ningún estado de {A} es de aceptación.

## Cadena `0a001a0100a0`

- Inicio: {A}
- Lee `0`: {A} ⟶ {B} [A→B]
- Lee `a`: {B} ⟶ {C} [B→C]
- Lee `0`: {C} ⟶ {A} [C→A]
- Lee `0`: {A} ⟶ {B} [A→B]
- Lee `1`: {B} ⟶ {C} [B→C]
- Lee `a`: {C} ⟶ {D} [C→D]
- Lee `0`: {D} ⟶ {B} [D→B]
- Lee `1`: {B} ⟶ {C} [B→C]
- Lee `0`: {C} ⟶ {A} [C→A]
- Lee `0`: {A} ⟶ {B} [A→B]
- Lee `a`: {B} ⟶ {C} [B→C]
- Lee `0`: {C} ⟶ {A} [C→A]
- **Rechazada**: ningún estado de {A} es de aceptación.
