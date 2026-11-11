# Recorridos: Lista 3 · Ejercicio 159

Describa lo que hace el AFN del diagrama 159.

Autómata: `lista3-159` (AFD).

## Cadena `01`

- Inicio: {q1}
- Lee `0`: {q1} ⟶ {q2} [q1→q2]
- Lee `1`: {q2} ⟶ {q3} [q2→q3]
- **Aceptada**: queda {q3} ∈ F.

## Cadena `101`

- Inicio: {q1}
- Lee `1`: {q1} ⟶ {q1} [q1→q1]
- Lee `0`: {q1} ⟶ {q2} [q1→q2]
- Lee `1`: {q2} ⟶ {q3} [q2→q3]
- **Aceptada**: queda {q3} ∈ F.

## Cadena `11101`

- Inicio: {q1}
- Lee `1`: {q1} ⟶ {q1} [q1→q1]
- Lee `1`: {q1} ⟶ {q1} [q1→q1]
- Lee `1`: {q1} ⟶ {q1} [q1→q1]
- Lee `0`: {q1} ⟶ {q2} [q1→q2]
- Lee `1`: {q2} ⟶ {q3} [q2→q3]
- **Aceptada**: queda {q3} ∈ F.

## Cadena `1111101`

- Inicio: {q1}
- Lee `1`: {q1} ⟶ {q1} [q1→q1]
- Lee `1`: {q1} ⟶ {q1} [q1→q1]
- Lee `1`: {q1} ⟶ {q1} [q1→q1]
- Lee `1`: {q1} ⟶ {q1} [q1→q1]
- Lee `1`: {q1} ⟶ {q1} [q1→q1]
- Lee `0`: {q1} ⟶ {q2} [q1→q2]
- Lee `1`: {q2} ⟶ {q3} [q2→q3]
- **Aceptada**: queda {q3} ∈ F.

## Cadena `1111111101`

- Inicio: {q1}
- Lee `1`: {q1} ⟶ {q1} [q1→q1]
- Lee `1`: {q1} ⟶ {q1} [q1→q1]
- Lee `1`: {q1} ⟶ {q1} [q1→q1]
- Lee `1`: {q1} ⟶ {q1} [q1→q1]
- Lee `1`: {q1} ⟶ {q1} [q1→q1]
- Lee `1`: {q1} ⟶ {q1} [q1→q1]
- Lee `1`: {q1} ⟶ {q1} [q1→q1]
- Lee `1`: {q1} ⟶ {q1} [q1→q1]
- Lee `0`: {q1} ⟶ {q2} [q1→q2]
- Lee `1`: {q2} ⟶ {q3} [q2→q3]
- **Aceptada**: queda {q3} ∈ F.

## Cadena λ

- Inicio: {q1}
- **Rechazada**: ningún estado de {q1} es de aceptación.

## Cadena `0`

- Inicio: {q1}
- Lee `0`: {q1} ⟶ {q2} [q1→q2]
- **Rechazada**: ningún estado de {q2} es de aceptación.

## Cadena `001`

- Inicio: {q1}
- Lee `0`: {q1} ⟶ {q2} [q1→q2]
- Lee `0`: {q2} ⟶ ∅ [ninguna transición]
- Lee `1`: ∅ ⟶ ∅ [ninguna transición]
- **Rechazada**: no queda ningún estado activo.

## Cadena `01010`

- Inicio: {q1}
- Lee `0`: {q1} ⟶ {q2} [q1→q2]
- Lee `1`: {q2} ⟶ {q3} [q2→q3]
- Lee `0`: {q3} ⟶ ∅ [ninguna transición]
- Lee `1`: ∅ ⟶ ∅ [ninguna transición]
- Lee `0`: ∅ ⟶ ∅ [ninguna transición]
- **Rechazada**: no queda ningún estado activo.

## Cadena `11101100`

- Inicio: {q1}
- Lee `1`: {q1} ⟶ {q1} [q1→q1]
- Lee `1`: {q1} ⟶ {q1} [q1→q1]
- Lee `1`: {q1} ⟶ {q1} [q1→q1]
- Lee `0`: {q1} ⟶ {q2} [q1→q2]
- Lee `1`: {q2} ⟶ {q3} [q2→q3]
- Lee `1`: {q3} ⟶ ∅ [ninguna transición]
- Lee `0`: ∅ ⟶ ∅ [ninguna transición]
- Lee `0`: ∅ ⟶ ∅ [ninguna transición]
- **Rechazada**: no queda ningún estado activo.

## Cadena `1`

- Inicio: {q1}
- Lee `1`: {q1} ⟶ {q1} [q1→q1]
- **Rechazada**: ningún estado de {q1} es de aceptación.
