# Recorridos: Lista 3 · Ejercicio 158

Describa lo que hace el AFN del diagrama 158.

Autómata: `lista3-158` (AFD).

## Cadena `01`

- Inicio: {q1}
- Lee `0`: {q1} ⟶ {q2} [q1→q2]
- Lee `1`: {q2} ⟶ {q3} [q2→q3]
- **Aceptada**: queda {q3} ∈ F.

## Cadena λ

- Inicio: {q1}
- **Rechazada**: ningún estado de {q1} es de aceptación.

## Cadena `1`

- Inicio: {q1}
- Lee `1`: {q1} ⟶ ∅ [ninguna transición]
- **Rechazada**: no queda ningún estado activo.

## Cadena `111`

- Inicio: {q1}
- Lee `1`: {q1} ⟶ ∅ [ninguna transición]
- Lee `1`: ∅ ⟶ ∅ [ninguna transición]
- Lee `1`: ∅ ⟶ ∅ [ninguna transición]
- **Rechazada**: no queda ningún estado activo.

## Cadena `00101`

- Inicio: {q1}
- Lee `0`: {q1} ⟶ {q2} [q1→q2]
- Lee `0`: {q2} ⟶ ∅ [ninguna transición]
- Lee `1`: ∅ ⟶ ∅ [ninguna transición]
- Lee `0`: ∅ ⟶ ∅ [ninguna transición]
- Lee `1`: ∅ ⟶ ∅ [ninguna transición]
- **Rechazada**: no queda ningún estado activo.

## Cadena `11110010`

- Inicio: {q1}
- Lee `1`: {q1} ⟶ ∅ [ninguna transición]
- Lee `1`: ∅ ⟶ ∅ [ninguna transición]
- Lee `1`: ∅ ⟶ ∅ [ninguna transición]
- Lee `1`: ∅ ⟶ ∅ [ninguna transición]
- Lee `0`: ∅ ⟶ ∅ [ninguna transición]
- Lee `0`: ∅ ⟶ ∅ [ninguna transición]
- Lee `1`: ∅ ⟶ ∅ [ninguna transición]
- Lee `0`: ∅ ⟶ ∅ [ninguna transición]
- **Rechazada**: no queda ningún estado activo.
