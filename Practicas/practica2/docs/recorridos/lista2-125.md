# Recorridos: Lista 2 · Ejercicio 125

Sea A = (Q, Σ, δ, A0, F) un AFD. ¿Cuál es el lenguaje de A' = (Q, Σ, δ, A0, Q \ F)?

Autómata: `lista2-125` (AFD).

## Cadena `0`

- Inicio: {par}
- Lee `0`: {par} ⟶ {impar} [par→impar]
- **Aceptada**: queda {impar} ∈ F.

## Cadena `01`

- Inicio: {par}
- Lee `0`: {par} ⟶ {impar} [par→impar]
- Lee `1`: {impar} ⟶ {impar} [impar→impar]
- **Aceptada**: queda {impar} ∈ F.

## Cadena `1101`

- Inicio: {par}
- Lee `1`: {par} ⟶ {par} [par→par]
- Lee `1`: {par} ⟶ {par} [par→par]
- Lee `0`: {par} ⟶ {impar} [par→impar]
- Lee `1`: {impar} ⟶ {impar} [impar→impar]
- **Aceptada**: queda {impar} ∈ F.

## Cadena `111011`

- Inicio: {par}
- Lee `1`: {par} ⟶ {par} [par→par]
- Lee `1`: {par} ⟶ {par} [par→par]
- Lee `1`: {par} ⟶ {par} [par→par]
- Lee `0`: {par} ⟶ {impar} [par→impar]
- Lee `1`: {impar} ⟶ {impar} [impar→impar]
- Lee `1`: {impar} ⟶ {impar} [impar→impar]
- **Aceptada**: queda {impar} ∈ F.

## Cadena `110000000`

- Inicio: {par}
- Lee `1`: {par} ⟶ {par} [par→par]
- Lee `1`: {par} ⟶ {par} [par→par]
- Lee `0`: {par} ⟶ {impar} [par→impar]
- Lee `0`: {impar} ⟶ {par} [impar→par]
- Lee `0`: {par} ⟶ {impar} [par→impar]
- Lee `0`: {impar} ⟶ {par} [impar→par]
- Lee `0`: {par} ⟶ {impar} [par→impar]
- Lee `0`: {impar} ⟶ {par} [impar→par]
- Lee `0`: {par} ⟶ {impar} [par→impar]
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

## Cadena `00010`

- Inicio: {par}
- Lee `0`: {par} ⟶ {impar} [par→impar]
- Lee `0`: {impar} ⟶ {par} [impar→par]
- Lee `0`: {par} ⟶ {impar} [par→impar]
- Lee `1`: {impar} ⟶ {impar} [impar→impar]
- Lee `0`: {impar} ⟶ {par} [impar→par]
- **Rechazada**: ningún estado de {par} es de aceptación.

## Cadena `01101001`

- Inicio: {par}
- Lee `0`: {par} ⟶ {impar} [par→impar]
- Lee `1`: {impar} ⟶ {impar} [impar→impar]
- Lee `1`: {impar} ⟶ {impar} [impar→impar]
- Lee `0`: {impar} ⟶ {par} [impar→par]
- Lee `1`: {par} ⟶ {par} [par→par]
- Lee `0`: {par} ⟶ {impar} [par→impar]
- Lee `0`: {impar} ⟶ {par} [impar→par]
- Lee `1`: {par} ⟶ {par} [par→par]
- **Rechazada**: ningún estado de {par} es de aceptación.
