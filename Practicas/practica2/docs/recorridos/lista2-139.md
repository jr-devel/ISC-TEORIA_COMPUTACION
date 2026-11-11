# Recorridos: Lista 2 · Ejercicio 139

Autómata que acepte las cadenas en {0, 1}* con un número par de ceros.

Autómata: `lista2-139` (AFD).

## Cadena λ

- Inicio: {par}
- **Aceptada**: queda {par} ∈ F.

## Cadena `1`

- Inicio: {par}
- Lee `1`: {par} ⟶ {par} [par→par]
- **Aceptada**: queda {par} ∈ F.

## Cadena `010`

- Inicio: {par}
- Lee `0`: {par} ⟶ {impar} [par→impar]
- Lee `1`: {impar} ⟶ {impar} [impar→impar]
- Lee `0`: {impar} ⟶ {par} [impar→par]
- **Aceptada**: queda {par} ∈ F.

## Cadena `10000`

- Inicio: {par}
- Lee `1`: {par} ⟶ {par} [par→par]
- Lee `0`: {par} ⟶ {impar} [par→impar]
- Lee `0`: {impar} ⟶ {par} [impar→par]
- Lee `0`: {par} ⟶ {impar} [par→impar]
- Lee `0`: {impar} ⟶ {par} [impar→par]
- **Aceptada**: queda {par} ∈ F.

## Cadena `11100111`

- Inicio: {par}
- Lee `1`: {par} ⟶ {par} [par→par]
- Lee `1`: {par} ⟶ {par} [par→par]
- Lee `1`: {par} ⟶ {par} [par→par]
- Lee `0`: {par} ⟶ {impar} [par→impar]
- Lee `0`: {impar} ⟶ {par} [impar→par]
- Lee `1`: {par} ⟶ {par} [par→par]
- Lee `1`: {par} ⟶ {par} [par→par]
- Lee `1`: {par} ⟶ {par} [par→par]
- **Aceptada**: queda {par} ∈ F.

## Cadena `0`

- Inicio: {par}
- Lee `0`: {par} ⟶ {impar} [par→impar]
- **Rechazada**: ningún estado de {impar} es de aceptación.

## Cadena `01`

- Inicio: {par}
- Lee `0`: {par} ⟶ {impar} [par→impar]
- Lee `1`: {impar} ⟶ {impar} [impar→impar]
- **Rechazada**: ningún estado de {impar} es de aceptación.

## Cadena `0100`

- Inicio: {par}
- Lee `0`: {par} ⟶ {impar} [par→impar]
- Lee `1`: {impar} ⟶ {impar} [impar→impar]
- Lee `0`: {impar} ⟶ {par} [impar→par]
- Lee `0`: {par} ⟶ {impar} [par→impar]
- **Rechazada**: ningún estado de {impar} es de aceptación.

## Cadena `000100`

- Inicio: {par}
- Lee `0`: {par} ⟶ {impar} [par→impar]
- Lee `0`: {impar} ⟶ {par} [impar→par]
- Lee `0`: {par} ⟶ {impar} [par→impar]
- Lee `1`: {impar} ⟶ {impar} [impar→impar]
- Lee `0`: {impar} ⟶ {par} [impar→par]
- Lee `0`: {par} ⟶ {impar} [par→impar]
- **Rechazada**: ningún estado de {impar} es de aceptación.

## Cadena `011011110`

- Inicio: {par}
- Lee `0`: {par} ⟶ {impar} [par→impar]
- Lee `1`: {impar} ⟶ {impar} [impar→impar]
- Lee `1`: {impar} ⟶ {impar} [impar→impar]
- Lee `0`: {impar} ⟶ {par} [impar→par]
- Lee `1`: {par} ⟶ {par} [par→par]
- Lee `1`: {par} ⟶ {par} [par→par]
- Lee `1`: {par} ⟶ {par} [par→par]
- Lee `1`: {par} ⟶ {par} [par→par]
- Lee `0`: {par} ⟶ {impar} [par→impar]
- **Rechazada**: ningún estado de {impar} es de aceptación.
