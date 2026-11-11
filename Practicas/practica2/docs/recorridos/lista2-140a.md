# Recorridos: Lista 2 · Ejercicio 140a

a) Cadenas sobre {0, 1} con un número impar de ceros.

Autómata: `lista2-140a` (AFD).

## Cadena `0`

- Inicio: {par}
- Lee `0`: {par} ⟶ {impar} [par→impar]
- **Aceptada**: queda {impar} ∈ F.

## Cadena `10`

- Inicio: {par}
- Lee `1`: {par} ⟶ {par} [par→par]
- Lee `0`: {par} ⟶ {impar} [par→impar]
- **Aceptada**: queda {impar} ∈ F.

## Cadena `1110`

- Inicio: {par}
- Lee `1`: {par} ⟶ {par} [par→par]
- Lee `1`: {par} ⟶ {par} [par→par]
- Lee `1`: {par} ⟶ {par} [par→par]
- Lee `0`: {par} ⟶ {impar} [par→impar]
- **Aceptada**: queda {impar} ∈ F.

## Cadena `001011`

- Inicio: {par}
- Lee `0`: {par} ⟶ {impar} [par→impar]
- Lee `0`: {impar} ⟶ {par} [impar→par]
- Lee `1`: {par} ⟶ {par} [par→par]
- Lee `0`: {par} ⟶ {impar} [par→impar]
- Lee `1`: {impar} ⟶ {impar} [impar→impar]
- Lee `1`: {impar} ⟶ {impar} [impar→impar]
- **Aceptada**: queda {impar} ∈ F.

## Cadena `011010001`

- Inicio: {par}
- Lee `0`: {par} ⟶ {impar} [par→impar]
- Lee `1`: {impar} ⟶ {impar} [impar→impar]
- Lee `1`: {impar} ⟶ {impar} [impar→impar]
- Lee `0`: {impar} ⟶ {par} [impar→par]
- Lee `1`: {par} ⟶ {par} [par→par]
- Lee `0`: {par} ⟶ {impar} [par→impar]
- Lee `0`: {impar} ⟶ {par} [impar→par]
- Lee `0`: {par} ⟶ {impar} [par→impar]
- Lee `1`: {impar} ⟶ {impar} [impar→impar]
- **Aceptada**: queda {impar} ∈ F.

## Cadena λ

- Inicio: {par}
- **Rechazada**: ningún estado de {par} es de aceptación.

## Cadena `1`

- Inicio: {par}
- Lee `1`: {par} ⟶ {par} [par→par]
- **Rechazada**: ningún estado de {par} es de aceptación.

## Cadena `100`

- Inicio: {par}
- Lee `1`: {par} ⟶ {par} [par→par]
- Lee `0`: {par} ⟶ {impar} [par→impar]
- Lee `0`: {impar} ⟶ {par} [impar→par]
- **Rechazada**: ningún estado de {par} es de aceptación.

## Cadena `00001`

- Inicio: {par}
- Lee `0`: {par} ⟶ {impar} [par→impar]
- Lee `0`: {impar} ⟶ {par} [impar→par]
- Lee `0`: {par} ⟶ {impar} [par→impar]
- Lee `0`: {impar} ⟶ {par} [impar→par]
- Lee `1`: {par} ⟶ {par} [par→par]
- **Rechazada**: ningún estado de {par} es de aceptación.

## Cadena `10010011`

- Inicio: {par}
- Lee `1`: {par} ⟶ {par} [par→par]
- Lee `0`: {par} ⟶ {impar} [par→impar]
- Lee `0`: {impar} ⟶ {par} [impar→par]
- Lee `1`: {par} ⟶ {par} [par→par]
- Lee `0`: {par} ⟶ {impar} [par→impar]
- Lee `0`: {impar} ⟶ {par} [impar→par]
- Lee `1`: {par} ⟶ {par} [par→par]
- Lee `1`: {par} ⟶ {par} [par→par]
- **Rechazada**: ningún estado de {par} es de aceptación.
