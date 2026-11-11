# Recorridos: Lista 2 · Ejercicio 126

Sea A un AFD. ¿Cuál es el lenguaje del autómata si F = ∅?

Autómata: `lista2-126` (AFD).

## Cadena λ

- Inicio: {par}
- **Rechazada**: ningún estado de {par} es de aceptación.

## Cadena `1`

- Inicio: {par}
- Lee `1`: {par} ⟶ {par} [par→par]
- **Rechazada**: ningún estado de {par} es de aceptación.

## Cadena `001`

- Inicio: {par}
- Lee `0`: {par} ⟶ {impar} [par→impar]
- Lee `0`: {impar} ⟶ {par} [impar→par]
- Lee `1`: {par} ⟶ {par} [par→par]
- **Rechazada**: ningún estado de {par} es de aceptación.

## Cadena `10111`

- Inicio: {par}
- Lee `1`: {par} ⟶ {par} [par→par]
- Lee `0`: {par} ⟶ {impar} [par→impar]
- Lee `1`: {impar} ⟶ {impar} [impar→impar]
- Lee `1`: {impar} ⟶ {impar} [impar→impar]
- Lee `1`: {impar} ⟶ {impar} [impar→impar]
- **Rechazada**: ningún estado de {impar} es de aceptación.

## Cadena `10001101`

- Inicio: {par}
- Lee `1`: {par} ⟶ {par} [par→par]
- Lee `0`: {par} ⟶ {impar} [par→impar]
- Lee `0`: {impar} ⟶ {par} [impar→par]
- Lee `0`: {par} ⟶ {impar} [par→impar]
- Lee `1`: {impar} ⟶ {impar} [impar→impar]
- Lee `1`: {impar} ⟶ {impar} [impar→impar]
- Lee `0`: {impar} ⟶ {par} [impar→par]
- Lee `1`: {par} ⟶ {par} [par→par]
- **Rechazada**: ningún estado de {par} es de aceptación.
