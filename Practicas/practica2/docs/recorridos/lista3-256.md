# Recorridos: Lista 3 · Ejercicio 256

Expresión regular para el autómata de la tabla 256.

Autómata: `lista3-256` (AFD).

## Cadena `0`

- Inicio: {A}
- Lee `0`: {A} ⟶ {B} [A→B]
- **Aceptada**: queda {B} ∈ F.

## Cadena `01`

- Inicio: {A}
- Lee `0`: {A} ⟶ {B} [A→B]
- Lee `1`: {B} ⟶ {B} [B→B]
- **Aceptada**: queda {B} ∈ F.

## Cadena `0000`

- Inicio: {A}
- Lee `0`: {A} ⟶ {B} [A→B]
- Lee `0`: {B} ⟶ {B} [B→B]
- Lee `0`: {B} ⟶ {B} [B→B]
- Lee `0`: {B} ⟶ {B} [B→B]
- **Aceptada**: queda {B} ∈ F.

## Cadena `201210`

- Inicio: {A}
- Lee `2`: {A} ⟶ {A} [A→A]
- Lee `0`: {A} ⟶ {B} [A→B]
- Lee `1`: {B} ⟶ {B} [B→B]
- Lee `2`: {B} ⟶ {A} [B→A]
- Lee `1`: {A} ⟶ {A} [A→A]
- Lee `0`: {A} ⟶ {B} [A→B]
- **Aceptada**: queda {B} ∈ F.

## Cadena `121101000`

- Inicio: {A}
- Lee `1`: {A} ⟶ {A} [A→A]
- Lee `2`: {A} ⟶ {A} [A→A]
- Lee `1`: {A} ⟶ {A} [A→A]
- Lee `1`: {A} ⟶ {A} [A→A]
- Lee `0`: {A} ⟶ {B} [A→B]
- Lee `1`: {B} ⟶ {B} [B→B]
- Lee `0`: {B} ⟶ {B} [B→B]
- Lee `0`: {B} ⟶ {B} [B→B]
- Lee `0`: {B} ⟶ {B} [B→B]
- **Aceptada**: queda {B} ∈ F.

## Cadena λ

- Inicio: {A}
- **Rechazada**: ningún estado de {A} es de aceptación.

## Cadena `2`

- Inicio: {A}
- Lee `2`: {A} ⟶ {A} [A→A]
- **Rechazada**: ningún estado de {A} es de aceptación.

## Cadena `202`

- Inicio: {A}
- Lee `2`: {A} ⟶ {A} [A→A]
- Lee `0`: {A} ⟶ {B} [A→B]
- Lee `2`: {B} ⟶ {A} [B→A]
- **Rechazada**: ningún estado de {A} es de aceptación.

## Cadena `21112`

- Inicio: {A}
- Lee `2`: {A} ⟶ {A} [A→A]
- Lee `1`: {A} ⟶ {A} [A→A]
- Lee `1`: {A} ⟶ {A} [A→A]
- Lee `1`: {A} ⟶ {A} [A→A]
- Lee `2`: {A} ⟶ {A} [A→A]
- **Rechazada**: ningún estado de {A} es de aceptación.

## Cadena `01211211`

- Inicio: {A}
- Lee `0`: {A} ⟶ {B} [A→B]
- Lee `1`: {B} ⟶ {B} [B→B]
- Lee `2`: {B} ⟶ {A} [B→A]
- Lee `1`: {A} ⟶ {A} [A→A]
- Lee `1`: {A} ⟶ {A} [A→A]
- Lee `2`: {A} ⟶ {A} [A→A]
- Lee `1`: {A} ⟶ {A} [A→A]
- Lee `1`: {A} ⟶ {A} [A→A]
- **Rechazada**: ningún estado de {A} es de aceptación.
