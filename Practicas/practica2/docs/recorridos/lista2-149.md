# Recorridos: Lista 2 · Ejercicio 149

AFD de la tabla (→A, C final). Halle δ(B, 0), δ(C, 1), δ̂(A, 1101), δ̂(A, 01001).

Autómata: `lista2-149` (AFD).

## Cadena `1`

- Inicio: {A}
- Lee `1`: {A} ⟶ {C} [A→C]
- **Aceptada**: queda {C} ∈ F.

## Cadena `10`

- Inicio: {A}
- Lee `1`: {A} ⟶ {C} [A→C]
- Lee `0`: {C} ⟶ {C} [C→C]
- **Aceptada**: queda {C} ∈ F.

## Cadena `1110`

- Inicio: {A}
- Lee `1`: {A} ⟶ {C} [A→C]
- Lee `1`: {C} ⟶ {A} [C→A]
- Lee `1`: {A} ⟶ {C} [A→C]
- Lee `0`: {C} ⟶ {C} [C→C]
- **Aceptada**: queda {C} ∈ F.

## Cadena `111110`

- Inicio: {A}
- Lee `1`: {A} ⟶ {C} [A→C]
- Lee `1`: {C} ⟶ {A} [C→A]
- Lee `1`: {A} ⟶ {C} [A→C]
- Lee `1`: {C} ⟶ {A} [C→A]
- Lee `1`: {A} ⟶ {C} [A→C]
- Lee `0`: {C} ⟶ {C} [C→C]
- **Aceptada**: queda {C} ∈ F.

## Cadena `110001000`

- Inicio: {A}
- Lee `1`: {A} ⟶ {C} [A→C]
- Lee `1`: {C} ⟶ {A} [C→A]
- Lee `0`: {A} ⟶ {B} [A→B]
- Lee `0`: {B} ⟶ {A} [B→A]
- Lee `0`: {A} ⟶ {B} [A→B]
- Lee `1`: {B} ⟶ {C} [B→C]
- Lee `0`: {C} ⟶ {C} [C→C]
- Lee `0`: {C} ⟶ {C} [C→C]
- Lee `0`: {C} ⟶ {C} [C→C]
- **Aceptada**: queda {C} ∈ F.

## Cadena λ

- Inicio: {A}
- **Rechazada**: ningún estado de {A} es de aceptación.

## Cadena `0`

- Inicio: {A}
- Lee `0`: {A} ⟶ {B} [A→B]
- **Rechazada**: ningún estado de {B} es de aceptación.

## Cadena `011`

- Inicio: {A}
- Lee `0`: {A} ⟶ {B} [A→B]
- Lee `1`: {B} ⟶ {C} [B→C]
- Lee `1`: {C} ⟶ {A} [C→A]
- **Rechazada**: ningún estado de {A} es de aceptación.

## Cadena `10010`

- Inicio: {A}
- Lee `1`: {A} ⟶ {C} [A→C]
- Lee `0`: {C} ⟶ {C} [C→C]
- Lee `0`: {C} ⟶ {C} [C→C]
- Lee `1`: {C} ⟶ {A} [C→A]
- Lee `0`: {A} ⟶ {B} [A→B]
- **Rechazada**: ningún estado de {B} es de aceptación.

## Cadena `00110000`

- Inicio: {A}
- Lee `0`: {A} ⟶ {B} [A→B]
- Lee `0`: {B} ⟶ {A} [B→A]
- Lee `1`: {A} ⟶ {C} [A→C]
- Lee `1`: {C} ⟶ {A} [C→A]
- Lee `0`: {A} ⟶ {B} [A→B]
- Lee `0`: {B} ⟶ {A} [B→A]
- Lee `0`: {A} ⟶ {B} [A→B]
- Lee `0`: {B} ⟶ {A} [B→A]
- **Rechazada**: ningún estado de {A} es de aceptación.
