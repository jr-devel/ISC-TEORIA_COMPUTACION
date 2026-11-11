# Recorridos: Lista 3 · Ejercicio 255

Expresión regular para el autómata de la tabla 255.

Autómata: `lista3-255` (AFD).

## Cadena λ

- Inicio: {A}
- **Aceptada**: queda {A} ∈ F.

## Cadena `00`

- Inicio: {A}
- Lee `0`: {A} ⟶ {B} [A→B]
- Lee `0`: {B} ⟶ {A} [B→A]
- **Aceptada**: queda {A} ∈ F.

## Cadena `1111010`

- Inicio: {A}
- Lee `1`: {A} ⟶ {B} [A→B]
- Lee `1`: {B} ⟶ {B} [B→B]
- Lee `1`: {B} ⟶ {B} [B→B]
- Lee `1`: {B} ⟶ {B} [B→B]
- Lee `0`: {B} ⟶ {A} [B→A]
- Lee `1`: {A} ⟶ {B} [A→B]
- Lee `0`: {B} ⟶ {A} [B→A]
- **Aceptada**: queda {A} ∈ F.

## Cadena `0100001010`

- Inicio: {A}
- Lee `0`: {A} ⟶ {B} [A→B]
- Lee `1`: {B} ⟶ {B} [B→B]
- Lee `0`: {B} ⟶ {A} [B→A]
- Lee `0`: {A} ⟶ {B} [A→B]
- Lee `0`: {B} ⟶ {A} [B→A]
- Lee `0`: {A} ⟶ {B} [A→B]
- Lee `1`: {B} ⟶ {B} [B→B]
- Lee `0`: {B} ⟶ {A} [B→A]
- Lee `1`: {A} ⟶ {B} [A→B]
- Lee `0`: {B} ⟶ {A} [B→A]
- **Aceptada**: queda {A} ∈ F.

## Cadena `0010111110110`

- Inicio: {A}
- Lee `0`: {A} ⟶ {B} [A→B]
- Lee `0`: {B} ⟶ {A} [B→A]
- Lee `1`: {A} ⟶ {B} [A→B]
- Lee `0`: {B} ⟶ {A} [B→A]
- Lee `1`: {A} ⟶ {B} [A→B]
- Lee `1`: {B} ⟶ {B} [B→B]
- Lee `1`: {B} ⟶ {B} [B→B]
- Lee `1`: {B} ⟶ {B} [B→B]
- Lee `1`: {B} ⟶ {B} [B→B]
- Lee `0`: {B} ⟶ {A} [B→A]
- Lee `1`: {A} ⟶ {B} [A→B]
- Lee `1`: {B} ⟶ {B} [B→B]
- Lee `0`: {B} ⟶ {A} [B→A]
- **Aceptada**: queda {A} ∈ F.

## Cadena `1`

- Inicio: {A}
- Lee `1`: {A} ⟶ {B} [A→B]
- **Rechazada**: ningún estado de {B} es de aceptación.

## Cadena `01`

- Inicio: {A}
- Lee `0`: {A} ⟶ {B} [A→B]
- Lee `1`: {B} ⟶ {B} [B→B]
- **Rechazada**: ningún estado de {B} es de aceptación.

## Cadena `1101`

- Inicio: {A}
- Lee `1`: {A} ⟶ {B} [A→B]
- Lee `1`: {B} ⟶ {B} [B→B]
- Lee `0`: {B} ⟶ {A} [B→A]
- Lee `1`: {A} ⟶ {B} [A→B]
- **Rechazada**: ningún estado de {B} es de aceptación.

## Cadena `101111`

- Inicio: {A}
- Lee `1`: {A} ⟶ {B} [A→B]
- Lee `0`: {B} ⟶ {A} [B→A]
- Lee `1`: {A} ⟶ {B} [A→B]
- Lee `1`: {B} ⟶ {B} [B→B]
- Lee `1`: {B} ⟶ {B} [B→B]
- Lee `1`: {B} ⟶ {B} [B→B]
- **Rechazada**: ningún estado de {B} es de aceptación.

## Cadena `111101101`

- Inicio: {A}
- Lee `1`: {A} ⟶ {B} [A→B]
- Lee `1`: {B} ⟶ {B} [B→B]
- Lee `1`: {B} ⟶ {B} [B→B]
- Lee `1`: {B} ⟶ {B} [B→B]
- Lee `0`: {B} ⟶ {A} [B→A]
- Lee `1`: {A} ⟶ {B} [A→B]
- Lee `1`: {B} ⟶ {B} [B→B]
- Lee `0`: {B} ⟶ {A} [B→A]
- Lee `1`: {A} ⟶ {B} [A→B]
- **Rechazada**: ningún estado de {B} es de aceptación.
