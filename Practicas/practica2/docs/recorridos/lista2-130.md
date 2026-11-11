# Recorridos: Lista 2 · Ejercicio 130

AFD dado M = ({q1, q2, q3}, {0, 1}, δ, q1, {q2}).

Autómata: `lista2-130` (AFD).

## Cadena `1`

- Inicio: {q1}
- Lee `1`: {q1} ⟶ {q2} [q1→q2]
- **Aceptada**: queda {q2} ∈ F.

## Cadena `01`

- Inicio: {q1}
- Lee `0`: {q1} ⟶ {q1} [q1→q1]
- Lee `1`: {q1} ⟶ {q2} [q1→q2]
- **Aceptada**: queda {q2} ∈ F.

## Cadena `1001`

- Inicio: {q1}
- Lee `1`: {q1} ⟶ {q2} [q1→q2]
- Lee `0`: {q2} ⟶ {q3} [q2→q3]
- Lee `0`: {q3} ⟶ {q2} [q3→q2]
- Lee `1`: {q2} ⟶ {q2} [q2→q2]
- **Aceptada**: queda {q2} ∈ F.

## Cadena `011100`

- Inicio: {q1}
- Lee `0`: {q1} ⟶ {q1} [q1→q1]
- Lee `1`: {q1} ⟶ {q2} [q1→q2]
- Lee `1`: {q2} ⟶ {q2} [q2→q2]
- Lee `1`: {q2} ⟶ {q2} [q2→q2]
- Lee `0`: {q2} ⟶ {q3} [q2→q3]
- Lee `0`: {q3} ⟶ {q2} [q3→q2]
- **Aceptada**: queda {q2} ∈ F.

## Cadena `101001100`

- Inicio: {q1}
- Lee `1`: {q1} ⟶ {q2} [q1→q2]
- Lee `0`: {q2} ⟶ {q3} [q2→q3]
- Lee `1`: {q3} ⟶ {q2} [q3→q2]
- Lee `0`: {q2} ⟶ {q3} [q2→q3]
- Lee `0`: {q3} ⟶ {q2} [q3→q2]
- Lee `1`: {q2} ⟶ {q2} [q2→q2]
- Lee `1`: {q2} ⟶ {q2} [q2→q2]
- Lee `0`: {q2} ⟶ {q3} [q2→q3]
- Lee `0`: {q3} ⟶ {q2} [q3→q2]
- **Aceptada**: queda {q2} ∈ F.

## Cadena λ

- Inicio: {q1}
- **Rechazada**: ningún estado de {q1} es de aceptación.

## Cadena `0`

- Inicio: {q1}
- Lee `0`: {q1} ⟶ {q1} [q1→q1]
- **Rechazada**: ningún estado de {q1} es de aceptación.

## Cadena `000`

- Inicio: {q1}
- Lee `0`: {q1} ⟶ {q1} [q1→q1]
- Lee `0`: {q1} ⟶ {q1} [q1→q1]
- Lee `0`: {q1} ⟶ {q1} [q1→q1]
- **Rechazada**: ningún estado de {q1} es de aceptación.

## Cadena `00110`

- Inicio: {q1}
- Lee `0`: {q1} ⟶ {q1} [q1→q1]
- Lee `0`: {q1} ⟶ {q1} [q1→q1]
- Lee `1`: {q1} ⟶ {q2} [q1→q2]
- Lee `1`: {q2} ⟶ {q2} [q2→q2]
- Lee `0`: {q2} ⟶ {q3} [q2→q3]
- **Rechazada**: ningún estado de {q3} es de aceptación.

## Cadena `11100110`

- Inicio: {q1}
- Lee `1`: {q1} ⟶ {q2} [q1→q2]
- Lee `1`: {q2} ⟶ {q2} [q2→q2]
- Lee `1`: {q2} ⟶ {q2} [q2→q2]
- Lee `0`: {q2} ⟶ {q3} [q2→q3]
- Lee `0`: {q3} ⟶ {q2} [q3→q2]
- Lee `1`: {q2} ⟶ {q2} [q2→q2]
- Lee `1`: {q2} ⟶ {q2} [q2→q2]
- Lee `0`: {q2} ⟶ {q3} [q2→q3]
- **Rechazada**: ningún estado de {q3} es de aceptación.
