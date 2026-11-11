# Recorridos: Lista 3 · Ejercicio 254

Expresión regular para el autómata de la tabla 254.

Autómata: `lista3-254` (AFD).

## Cadena `1`

- Inicio: {A}
- Lee `1`: {A} ⟶ {B} [A→B]
- **Aceptada**: queda {B} ∈ F.

## Cadena `01`

- Inicio: {A}
- Lee `0`: {A} ⟶ {A} [A→A]
- Lee `1`: {A} ⟶ {B} [A→B]
- **Aceptada**: queda {B} ∈ F.

## Cadena `0001`

- Inicio: {A}
- Lee `0`: {A} ⟶ {A} [A→A]
- Lee `0`: {A} ⟶ {A} [A→A]
- Lee `0`: {A} ⟶ {A} [A→A]
- Lee `1`: {A} ⟶ {B} [A→B]
- **Aceptada**: queda {B} ∈ F.

## Cadena `101001`

- Inicio: {A}
- Lee `1`: {A} ⟶ {B} [A→B]
- Lee `0`: {B} ⟶ {A} [B→A]
- Lee `1`: {A} ⟶ {B} [A→B]
- Lee `0`: {B} ⟶ {A} [B→A]
- Lee `0`: {A} ⟶ {A} [A→A]
- Lee `1`: {A} ⟶ {B} [A→B]
- **Aceptada**: queda {B} ∈ F.

## Cadena `001101101`

- Inicio: {A}
- Lee `0`: {A} ⟶ {A} [A→A]
- Lee `0`: {A} ⟶ {A} [A→A]
- Lee `1`: {A} ⟶ {B} [A→B]
- Lee `1`: {B} ⟶ {B} [B→B]
- Lee `0`: {B} ⟶ {A} [B→A]
- Lee `1`: {A} ⟶ {B} [A→B]
- Lee `1`: {B} ⟶ {B} [B→B]
- Lee `0`: {B} ⟶ {A} [B→A]
- Lee `1`: {A} ⟶ {B} [A→B]
- **Aceptada**: queda {B} ∈ F.

## Cadena λ

- Inicio: {A}
- **Rechazada**: ningún estado de {A} es de aceptación.

## Cadena `0`

- Inicio: {A}
- Lee `0`: {A} ⟶ {A} [A→A]
- **Rechazada**: ningún estado de {A} es de aceptación.

## Cadena `010`

- Inicio: {A}
- Lee `0`: {A} ⟶ {A} [A→A]
- Lee `1`: {A} ⟶ {B} [A→B]
- Lee `0`: {B} ⟶ {A} [B→A]
- **Rechazada**: ningún estado de {A} es de aceptación.

## Cadena `10000`

- Inicio: {A}
- Lee `1`: {A} ⟶ {B} [A→B]
- Lee `0`: {B} ⟶ {A} [B→A]
- Lee `0`: {A} ⟶ {A} [A→A]
- Lee `0`: {A} ⟶ {A} [A→A]
- Lee `0`: {A} ⟶ {A} [A→A]
- **Rechazada**: ningún estado de {A} es de aceptación.

## Cadena `10101000`

- Inicio: {A}
- Lee `1`: {A} ⟶ {B} [A→B]
- Lee `0`: {B} ⟶ {A} [B→A]
- Lee `1`: {A} ⟶ {B} [A→B]
- Lee `0`: {B} ⟶ {A} [B→A]
- Lee `1`: {A} ⟶ {B} [A→B]
- Lee `0`: {B} ⟶ {A} [B→A]
- Lee `0`: {A} ⟶ {A} [A→A]
- Lee `0`: {A} ⟶ {A} [A→A]
- **Rechazada**: ningún estado de {A} es de aceptación.
