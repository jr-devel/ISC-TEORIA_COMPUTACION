# Recorridos: Lista 3 · Ejercicio 258

Expresión regular para el autómata de la tabla 258.

Autómata: `lista3-258` (AFD).

## Cadena `1`

- Inicio: {A}
- Lee `1`: {A} ⟶ {C} [A→C]
- **Aceptada**: queda {C} ∈ F.

## Cadena `01100011`

- Inicio: {A}
- Lee `0`: {A} ⟶ {C} [A→C]
- Lee `1`: {C} ⟶ {A} [C→A]
- Lee `1`: {A} ⟶ {C} [A→C]
- Lee `0`: {C} ⟶ {B} [C→B]
- Lee `0`: {B} ⟶ {A} [B→A]
- Lee `0`: {A} ⟶ {C} [A→C]
- Lee `1`: {C} ⟶ {A} [C→A]
- Lee `1`: {A} ⟶ {C} [A→C]
- **Aceptada**: queda {C} ∈ F.

## Cadena `1110100010`

- Inicio: {A}
- Lee `1`: {A} ⟶ {C} [A→C]
- Lee `1`: {C} ⟶ {A} [C→A]
- Lee `1`: {A} ⟶ {C} [A→C]
- Lee `0`: {C} ⟶ {B} [C→B]
- Lee `1`: {B} ⟶ {C} [B→C]
- Lee `0`: {C} ⟶ {B} [C→B]
- Lee `0`: {B} ⟶ {A} [B→A]
- Lee `0`: {A} ⟶ {C} [A→C]
- Lee `1`: {C} ⟶ {A} [C→A]
- Lee `0`: {A} ⟶ {C} [A→C]
- **Aceptada**: queda {C} ∈ F.

## Cadena `011001000001`

- Inicio: {A}
- Lee `0`: {A} ⟶ {C} [A→C]
- Lee `1`: {C} ⟶ {A} [C→A]
- Lee `1`: {A} ⟶ {C} [A→C]
- Lee `0`: {C} ⟶ {B} [C→B]
- Lee `0`: {B} ⟶ {A} [B→A]
- Lee `1`: {A} ⟶ {C} [A→C]
- Lee `0`: {C} ⟶ {B} [C→B]
- Lee `0`: {B} ⟶ {A} [B→A]
- Lee `0`: {A} ⟶ {C} [A→C]
- Lee `0`: {C} ⟶ {B} [C→B]
- Lee `0`: {B} ⟶ {A} [B→A]
- Lee `1`: {A} ⟶ {C} [A→C]
- **Aceptada**: queda {C} ∈ F.

## Cadena `11100000100110`

- Inicio: {A}
- Lee `1`: {A} ⟶ {C} [A→C]
- Lee `1`: {C} ⟶ {A} [C→A]
- Lee `1`: {A} ⟶ {C} [A→C]
- Lee `0`: {C} ⟶ {B} [C→B]
- Lee `0`: {B} ⟶ {A} [B→A]
- Lee `0`: {A} ⟶ {C} [A→C]
- Lee `0`: {C} ⟶ {B} [C→B]
- Lee `0`: {B} ⟶ {A} [B→A]
- Lee `1`: {A} ⟶ {C} [A→C]
- Lee `0`: {C} ⟶ {B} [C→B]
- Lee `0`: {B} ⟶ {A} [B→A]
- Lee `1`: {A} ⟶ {C} [A→C]
- Lee `1`: {C} ⟶ {A} [C→A]
- Lee `0`: {A} ⟶ {C} [A→C]
- **Aceptada**: queda {C} ∈ F.

## Cadena λ

- Inicio: {A}
- **Rechazada**: ningún estado de {A} es de aceptación.

## Cadena `0000101`

- Inicio: {A}
- Lee `0`: {A} ⟶ {C} [A→C]
- Lee `0`: {C} ⟶ {B} [C→B]
- Lee `0`: {B} ⟶ {A} [B→A]
- Lee `0`: {A} ⟶ {C} [A→C]
- Lee `1`: {C} ⟶ {A} [C→A]
- Lee `0`: {A} ⟶ {C} [A→C]
- Lee `1`: {C} ⟶ {A} [C→A]
- **Rechazada**: ningún estado de {A} es de aceptación.

## Cadena `00000100`

- Inicio: {A}
- Lee `0`: {A} ⟶ {C} [A→C]
- Lee `0`: {C} ⟶ {B} [C→B]
- Lee `0`: {B} ⟶ {A} [B→A]
- Lee `0`: {A} ⟶ {C} [A→C]
- Lee `0`: {C} ⟶ {B} [C→B]
- Lee `1`: {B} ⟶ {C} [B→C]
- Lee `0`: {C} ⟶ {B} [C→B]
- Lee `0`: {B} ⟶ {A} [B→A]
- **Rechazada**: ningún estado de {A} es de aceptación.

## Cadena `100011011`

- Inicio: {A}
- Lee `1`: {A} ⟶ {C} [A→C]
- Lee `0`: {C} ⟶ {B} [C→B]
- Lee `0`: {B} ⟶ {A} [B→A]
- Lee `0`: {A} ⟶ {C} [A→C]
- Lee `1`: {C} ⟶ {A} [C→A]
- Lee `1`: {A} ⟶ {C} [A→C]
- Lee `0`: {C} ⟶ {B} [C→B]
- Lee `1`: {B} ⟶ {C} [B→C]
- Lee `1`: {C} ⟶ {A} [C→A]
- **Rechazada**: ningún estado de {A} es de aceptación.

## Cadena `011000000101`

- Inicio: {A}
- Lee `0`: {A} ⟶ {C} [A→C]
- Lee `1`: {C} ⟶ {A} [C→A]
- Lee `1`: {A} ⟶ {C} [A→C]
- Lee `0`: {C} ⟶ {B} [C→B]
- Lee `0`: {B} ⟶ {A} [B→A]
- Lee `0`: {A} ⟶ {C} [A→C]
- Lee `0`: {C} ⟶ {B} [C→B]
- Lee `0`: {B} ⟶ {A} [B→A]
- Lee `0`: {A} ⟶ {C} [A→C]
- Lee `1`: {C} ⟶ {A} [C→A]
- Lee `0`: {A} ⟶ {C} [A→C]
- Lee `1`: {C} ⟶ {A} [C→A]
- **Rechazada**: ningún estado de {A} es de aceptación.
