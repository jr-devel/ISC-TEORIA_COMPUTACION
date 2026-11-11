# Recorridos: Lista 3 · Ejercicio 257

Expresión regular para el autómata de la tabla 257.

Autómata: `lista3-257` (AFD).

## Cadena `0`

- Inicio: {A}
- Lee `0`: {A} ⟶ {B} [A→B]
- **Aceptada**: queda {B} ∈ F.

## Cadena `00`

- Inicio: {A}
- Lee `0`: {A} ⟶ {B} [A→B]
- Lee `0`: {B} ⟶ {C} [B→C]
- **Aceptada**: queda {C} ∈ F.

## Cadena `1101`

- Inicio: {A}
- Lee `1`: {A} ⟶ {C} [A→C]
- Lee `1`: {C} ⟶ {A} [C→A]
- Lee `0`: {A} ⟶ {B} [A→B]
- Lee `1`: {B} ⟶ {B} [B→B]
- **Aceptada**: queda {B} ∈ F.

## Cadena `010001`

- Inicio: {A}
- Lee `0`: {A} ⟶ {B} [A→B]
- Lee `1`: {B} ⟶ {B} [B→B]
- Lee `0`: {B} ⟶ {C} [B→C]
- Lee `0`: {C} ⟶ {A} [C→A]
- Lee `0`: {A} ⟶ {B} [A→B]
- Lee `1`: {B} ⟶ {B} [B→B]
- **Aceptada**: queda {B} ∈ F.

## Cadena `111100101`

- Inicio: {A}
- Lee `1`: {A} ⟶ {C} [A→C]
- Lee `1`: {C} ⟶ {A} [C→A]
- Lee `1`: {A} ⟶ {C} [A→C]
- Lee `1`: {C} ⟶ {A} [C→A]
- Lee `0`: {A} ⟶ {B} [A→B]
- Lee `0`: {B} ⟶ {C} [B→C]
- Lee `1`: {C} ⟶ {A} [C→A]
- Lee `0`: {A} ⟶ {B} [A→B]
- Lee `1`: {B} ⟶ {B} [B→B]
- **Aceptada**: queda {B} ∈ F.

## Cadena λ

- Inicio: {A}
- **Rechazada**: ningún estado de {A} es de aceptación.

## Cadena `001`

- Inicio: {A}
- Lee `0`: {A} ⟶ {B} [A→B]
- Lee `0`: {B} ⟶ {C} [B→C]
- Lee `1`: {C} ⟶ {A} [C→A]
- **Rechazada**: ningún estado de {A} es de aceptación.

## Cadena `00010001`

- Inicio: {A}
- Lee `0`: {A} ⟶ {B} [A→B]
- Lee `0`: {B} ⟶ {C} [B→C]
- Lee `0`: {C} ⟶ {A} [C→A]
- Lee `1`: {A} ⟶ {C} [A→C]
- Lee `0`: {C} ⟶ {A} [C→A]
- Lee `0`: {A} ⟶ {B} [A→B]
- Lee `0`: {B} ⟶ {C} [B→C]
- Lee `1`: {C} ⟶ {A} [C→A]
- **Rechazada**: ningún estado de {A} es de aceptación.

## Cadena `101101101`

- Inicio: {A}
- Lee `1`: {A} ⟶ {C} [A→C]
- Lee `0`: {C} ⟶ {A} [C→A]
- Lee `1`: {A} ⟶ {C} [A→C]
- Lee `1`: {C} ⟶ {A} [C→A]
- Lee `0`: {A} ⟶ {B} [A→B]
- Lee `1`: {B} ⟶ {B} [B→B]
- Lee `1`: {B} ⟶ {B} [B→B]
- Lee `0`: {B} ⟶ {C} [B→C]
- Lee `1`: {C} ⟶ {A} [C→A]
- **Rechazada**: ningún estado de {A} es de aceptación.

## Cadena `01010011001101`

- Inicio: {A}
- Lee `0`: {A} ⟶ {B} [A→B]
- Lee `1`: {B} ⟶ {B} [B→B]
- Lee `0`: {B} ⟶ {C} [B→C]
- Lee `1`: {C} ⟶ {A} [C→A]
- Lee `0`: {A} ⟶ {B} [A→B]
- Lee `0`: {B} ⟶ {C} [B→C]
- Lee `1`: {C} ⟶ {A} [C→A]
- Lee `1`: {A} ⟶ {C} [A→C]
- Lee `0`: {C} ⟶ {A} [C→A]
- Lee `0`: {A} ⟶ {B} [A→B]
- Lee `1`: {B} ⟶ {B} [B→B]
- Lee `1`: {B} ⟶ {B} [B→B]
- Lee `0`: {B} ⟶ {C} [B→C]
- Lee `1`: {C} ⟶ {A} [C→A]
- **Rechazada**: ningún estado de {A} es de aceptación.
