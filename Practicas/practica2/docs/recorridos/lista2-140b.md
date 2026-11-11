# Recorridos: Lista 2 · Ejercicio 140b

b) Cadenas sobre {0, 1} con un número par de ceros y un número par de unos.

Autómata: `lista2-140b` (AFD).

## Cadena λ

- Inicio: {0p1p}
- **Aceptada**: queda {0p1p} ∈ F.

## Cadena `11`

- Inicio: {0p1p}
- Lee `1`: {0p1p} ⟶ {0p1i} [0p1p→0p1i]
- Lee `1`: {0p1i} ⟶ {0p1p} [0p1i→0p1p]
- **Aceptada**: queda {0p1p} ∈ F.

## Cadena `0000`

- Inicio: {0p1p}
- Lee `0`: {0p1p} ⟶ {0i1p} [0p1p→0i1p]
- Lee `0`: {0i1p} ⟶ {0p1p} [0i1p→0p1p]
- Lee `0`: {0p1p} ⟶ {0i1p} [0p1p→0i1p]
- Lee `0`: {0i1p} ⟶ {0p1p} [0i1p→0p1p]
- **Aceptada**: queda {0p1p} ∈ F.

## Cadena `01100110`

- Inicio: {0p1p}
- Lee `0`: {0p1p} ⟶ {0i1p} [0p1p→0i1p]
- Lee `1`: {0i1p} ⟶ {0i1i} [0i1p→0i1i]
- Lee `1`: {0i1i} ⟶ {0i1p} [0i1i→0i1p]
- Lee `0`: {0i1p} ⟶ {0p1p} [0i1p→0p1p]
- Lee `0`: {0p1p} ⟶ {0i1p} [0p1p→0i1p]
- Lee `1`: {0i1p} ⟶ {0i1i} [0i1p→0i1i]
- Lee `1`: {0i1i} ⟶ {0i1p} [0i1i→0i1p]
- Lee `0`: {0i1p} ⟶ {0p1p} [0i1p→0p1p]
- **Aceptada**: queda {0p1p} ∈ F.

## Cadena `001110000100`

- Inicio: {0p1p}
- Lee `0`: {0p1p} ⟶ {0i1p} [0p1p→0i1p]
- Lee `0`: {0i1p} ⟶ {0p1p} [0i1p→0p1p]
- Lee `1`: {0p1p} ⟶ {0p1i} [0p1p→0p1i]
- Lee `1`: {0p1i} ⟶ {0p1p} [0p1i→0p1p]
- Lee `1`: {0p1p} ⟶ {0p1i} [0p1p→0p1i]
- Lee `0`: {0p1i} ⟶ {0i1i} [0p1i→0i1i]
- Lee `0`: {0i1i} ⟶ {0p1i} [0i1i→0p1i]
- Lee `0`: {0p1i} ⟶ {0i1i} [0p1i→0i1i]
- Lee `0`: {0i1i} ⟶ {0p1i} [0i1i→0p1i]
- Lee `1`: {0p1i} ⟶ {0p1p} [0p1i→0p1p]
- Lee `0`: {0p1p} ⟶ {0i1p} [0p1p→0i1p]
- Lee `0`: {0i1p} ⟶ {0p1p} [0i1p→0p1p]
- **Aceptada**: queda {0p1p} ∈ F.

## Cadena `1`

- Inicio: {0p1p}
- Lee `1`: {0p1p} ⟶ {0p1i} [0p1p→0p1i]
- **Rechazada**: ningún estado de {0p1i} es de aceptación.

## Cadena `10`

- Inicio: {0p1p}
- Lee `1`: {0p1p} ⟶ {0p1i} [0p1p→0p1i]
- Lee `0`: {0p1i} ⟶ {0i1i} [0p1i→0i1i]
- **Rechazada**: ningún estado de {0i1i} es de aceptación.

## Cadena `0100`

- Inicio: {0p1p}
- Lee `0`: {0p1p} ⟶ {0i1p} [0p1p→0i1p]
- Lee `1`: {0i1p} ⟶ {0i1i} [0i1p→0i1i]
- Lee `0`: {0i1i} ⟶ {0p1i} [0i1i→0p1i]
- Lee `0`: {0p1i} ⟶ {0i1i} [0p1i→0i1i]
- **Rechazada**: ningún estado de {0i1i} es de aceptación.

## Cadena `111000`

- Inicio: {0p1p}
- Lee `1`: {0p1p} ⟶ {0p1i} [0p1p→0p1i]
- Lee `1`: {0p1i} ⟶ {0p1p} [0p1i→0p1p]
- Lee `1`: {0p1p} ⟶ {0p1i} [0p1p→0p1i]
- Lee `0`: {0p1i} ⟶ {0i1i} [0p1i→0i1i]
- Lee `0`: {0i1i} ⟶ {0p1i} [0i1i→0p1i]
- Lee `0`: {0p1i} ⟶ {0i1i} [0p1i→0i1i]
- **Rechazada**: ningún estado de {0i1i} es de aceptación.

## Cadena `111101010`

- Inicio: {0p1p}
- Lee `1`: {0p1p} ⟶ {0p1i} [0p1p→0p1i]
- Lee `1`: {0p1i} ⟶ {0p1p} [0p1i→0p1p]
- Lee `1`: {0p1p} ⟶ {0p1i} [0p1p→0p1i]
- Lee `1`: {0p1i} ⟶ {0p1p} [0p1i→0p1p]
- Lee `0`: {0p1p} ⟶ {0i1p} [0p1p→0i1p]
- Lee `1`: {0i1p} ⟶ {0i1i} [0i1p→0i1i]
- Lee `0`: {0i1i} ⟶ {0p1i} [0i1i→0p1i]
- Lee `1`: {0p1i} ⟶ {0p1p} [0p1i→0p1p]
- Lee `0`: {0p1p} ⟶ {0i1p} [0p1p→0i1p]
- **Rechazada**: ningún estado de {0i1p} es de aceptación.
