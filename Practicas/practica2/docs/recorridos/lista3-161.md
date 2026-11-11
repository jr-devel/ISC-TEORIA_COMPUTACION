# Recorridos: Lista 3 · Ejercicio 161

Describa lo que hace el AFN del diagrama 161.

Autómata: `lista3-161` (AFD).

## Cadena λ

- Inicio: {q1}
- **Aceptada**: queda {q1} ∈ F.

## Cadena `010`

- Inicio: {q1}
- Lee `0`: {q1} ⟶ {q2} [q1→q2]
- Lee `1`: {q2} ⟶ {q3} [q2→q3]
- Lee `0`: {q3} ⟶ {q1} [q3→q1]
- **Aceptada**: queda {q1} ∈ F.

## Cadena `010010`

- Inicio: {q1}
- Lee `0`: {q1} ⟶ {q2} [q1→q2]
- Lee `1`: {q2} ⟶ {q3} [q2→q3]
- Lee `0`: {q3} ⟶ {q1} [q3→q1]
- Lee `0`: {q1} ⟶ {q2} [q1→q2]
- Lee `1`: {q2} ⟶ {q3} [q2→q3]
- Lee `0`: {q3} ⟶ {q1} [q3→q1]
- **Aceptada**: queda {q1} ∈ F.

## Cadena `010010010`

- Inicio: {q1}
- Lee `0`: {q1} ⟶ {q2} [q1→q2]
- Lee `1`: {q2} ⟶ {q3} [q2→q3]
- Lee `0`: {q3} ⟶ {q1} [q3→q1]
- Lee `0`: {q1} ⟶ {q2} [q1→q2]
- Lee `1`: {q2} ⟶ {q3} [q2→q3]
- Lee `0`: {q3} ⟶ {q1} [q3→q1]
- Lee `0`: {q1} ⟶ {q2} [q1→q2]
- Lee `1`: {q2} ⟶ {q3} [q2→q3]
- Lee `0`: {q3} ⟶ {q1} [q3→q1]
- **Aceptada**: queda {q1} ∈ F.

## Cadena `010010010010`

- Inicio: {q1}
- Lee `0`: {q1} ⟶ {q2} [q1→q2]
- Lee `1`: {q2} ⟶ {q3} [q2→q3]
- Lee `0`: {q3} ⟶ {q1} [q3→q1]
- Lee `0`: {q1} ⟶ {q2} [q1→q2]
- Lee `1`: {q2} ⟶ {q3} [q2→q3]
- Lee `0`: {q3} ⟶ {q1} [q3→q1]
- Lee `0`: {q1} ⟶ {q2} [q1→q2]
- Lee `1`: {q2} ⟶ {q3} [q2→q3]
- Lee `0`: {q3} ⟶ {q1} [q3→q1]
- Lee `0`: {q1} ⟶ {q2} [q1→q2]
- Lee `1`: {q2} ⟶ {q3} [q2→q3]
- Lee `0`: {q3} ⟶ {q1} [q3→q1]
- **Aceptada**: queda {q1} ∈ F.

## Cadena `0`

- Inicio: {q1}
- Lee `0`: {q1} ⟶ {q2} [q1→q2]
- **Rechazada**: ningún estado de {q2} es de aceptación.

## Cadena `01`

- Inicio: {q1}
- Lee `0`: {q1} ⟶ {q2} [q1→q2]
- Lee `1`: {q2} ⟶ {q3} [q2→q3]
- **Rechazada**: ningún estado de {q3} es de aceptación.

## Cadena `0100`

- Inicio: {q1}
- Lee `0`: {q1} ⟶ {q2} [q1→q2]
- Lee `1`: {q2} ⟶ {q3} [q2→q3]
- Lee `0`: {q3} ⟶ {q1} [q3→q1]
- Lee `0`: {q1} ⟶ {q2} [q1→q2]
- **Rechazada**: ningún estado de {q2} es de aceptación.

## Cadena `110101`

- Inicio: {q1}
- Lee `1`: {q1} ⟶ ∅ [ninguna transición]
- Lee `1`: ∅ ⟶ ∅ [ninguna transición]
- Lee `0`: ∅ ⟶ ∅ [ninguna transición]
- Lee `1`: ∅ ⟶ ∅ [ninguna transición]
- Lee `0`: ∅ ⟶ ∅ [ninguna transición]
- Lee `1`: ∅ ⟶ ∅ [ninguna transición]
- **Rechazada**: no queda ningún estado activo.

## Cadena `000011110`

- Inicio: {q1}
- Lee `0`: {q1} ⟶ {q2} [q1→q2]
- Lee `0`: {q2} ⟶ ∅ [ninguna transición]
- Lee `0`: ∅ ⟶ ∅ [ninguna transición]
- Lee `0`: ∅ ⟶ ∅ [ninguna transición]
- Lee `1`: ∅ ⟶ ∅ [ninguna transición]
- Lee `1`: ∅ ⟶ ∅ [ninguna transición]
- Lee `1`: ∅ ⟶ ∅ [ninguna transición]
- Lee `1`: ∅ ⟶ ∅ [ninguna transición]
- Lee `0`: ∅ ⟶ ∅ [ninguna transición]
- **Rechazada**: no queda ningún estado activo.
