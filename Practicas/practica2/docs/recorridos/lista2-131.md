# Recorridos: Lista 2 · Ejercicio 131

AFD dado M = ({q1, q2}, {0, 1}, δ, q1, {q2}).

Autómata: `lista2-131` (AFD).

## Cadena `1`

- Inicio: {q1}
- Lee `1`: {q1} ⟶ {q2} [q1→q2]
- **Aceptada**: queda {q2} ∈ F.

## Cadena `11`

- Inicio: {q1}
- Lee `1`: {q1} ⟶ {q2} [q1→q2]
- Lee `1`: {q2} ⟶ {q2} [q2→q2]
- **Aceptada**: queda {q2} ∈ F.

## Cadena `0111`

- Inicio: {q1}
- Lee `0`: {q1} ⟶ {q1} [q1→q1]
- Lee `1`: {q1} ⟶ {q2} [q1→q2]
- Lee `1`: {q2} ⟶ {q2} [q2→q2]
- Lee `1`: {q2} ⟶ {q2} [q2→q2]
- **Aceptada**: queda {q2} ∈ F.

## Cadena `100111`

- Inicio: {q1}
- Lee `1`: {q1} ⟶ {q2} [q1→q2]
- Lee `0`: {q2} ⟶ {q1} [q2→q1]
- Lee `0`: {q1} ⟶ {q1} [q1→q1]
- Lee `1`: {q1} ⟶ {q2} [q1→q2]
- Lee `1`: {q2} ⟶ {q2} [q2→q2]
- Lee `1`: {q2} ⟶ {q2} [q2→q2]
- **Aceptada**: queda {q2} ∈ F.

## Cadena `000010011`

- Inicio: {q1}
- Lee `0`: {q1} ⟶ {q1} [q1→q1]
- Lee `0`: {q1} ⟶ {q1} [q1→q1]
- Lee `0`: {q1} ⟶ {q1} [q1→q1]
- Lee `0`: {q1} ⟶ {q1} [q1→q1]
- Lee `1`: {q1} ⟶ {q2} [q1→q2]
- Lee `0`: {q2} ⟶ {q1} [q2→q1]
- Lee `0`: {q1} ⟶ {q1} [q1→q1]
- Lee `1`: {q1} ⟶ {q2} [q1→q2]
- Lee `1`: {q2} ⟶ {q2} [q2→q2]
- **Aceptada**: queda {q2} ∈ F.

## Cadena λ

- Inicio: {q1}
- **Rechazada**: ningún estado de {q1} es de aceptación.

## Cadena `0`

- Inicio: {q1}
- Lee `0`: {q1} ⟶ {q1} [q1→q1]
- **Rechazada**: ningún estado de {q1} es de aceptación.

## Cadena `010`

- Inicio: {q1}
- Lee `0`: {q1} ⟶ {q1} [q1→q1]
- Lee `1`: {q1} ⟶ {q2} [q1→q2]
- Lee `0`: {q2} ⟶ {q1} [q2→q1]
- **Rechazada**: ningún estado de {q1} es de aceptación.

## Cadena `01100`

- Inicio: {q1}
- Lee `0`: {q1} ⟶ {q1} [q1→q1]
- Lee `1`: {q1} ⟶ {q2} [q1→q2]
- Lee `1`: {q2} ⟶ {q2} [q2→q2]
- Lee `0`: {q2} ⟶ {q1} [q2→q1]
- Lee `0`: {q1} ⟶ {q1} [q1→q1]
- **Rechazada**: ningún estado de {q1} es de aceptación.

## Cadena `01110010`

- Inicio: {q1}
- Lee `0`: {q1} ⟶ {q1} [q1→q1]
- Lee `1`: {q1} ⟶ {q2} [q1→q2]
- Lee `1`: {q2} ⟶ {q2} [q2→q2]
- Lee `1`: {q2} ⟶ {q2} [q2→q2]
- Lee `0`: {q2} ⟶ {q1} [q2→q1]
- Lee `0`: {q1} ⟶ {q1} [q1→q1]
- Lee `1`: {q1} ⟶ {q2} [q1→q2]
- Lee `0`: {q2} ⟶ {q1} [q2→q1]
- **Rechazada**: ningún estado de {q1} es de aceptación.
