# Recorridos: Lista 3 · Ejercicio 245

AFN-λ equivalente a la expresión 0(0 + 1)*.

Autómata: `lista3-245` (AFN-λ).

## Cadena `0`

- Inicio: {q0}
- Lee `0`: {q0} ⟶ {q1, q8, q6, q2, q4, q9} [q0→q1]; cierre λ añade {q8, q6, q2, q4, q9}
- **Aceptada**: queda {q9} ∈ F.

## Cadena `01`

- Inicio: {q0}
- Lee `0`: {q0} ⟶ {q1, q8, q6, q2, q4, q9} [q0→q1]; cierre λ añade {q8, q6, q2, q4, q9}
- Lee `1`: {q1, q8, q6, q2, q4, q9} ⟶ {q6, q2, q4, q5, q7, q9} [q4→q5]; cierre λ añade {q6, q2, q4, q7, q9}
- **Aceptada**: queda {q9} ∈ F.

## Cadena `0000`

- Inicio: {q0}
- Lee `0`: {q0} ⟶ {q1, q8, q6, q2, q4, q9} [q0→q1]; cierre λ añade {q8, q6, q2, q4, q9}
- Lee `0`: {q1, q8, q6, q2, q4, q9} ⟶ {q6, q2, q3, q4, q7, q9} [q2→q3]; cierre λ añade {q6, q2, q4, q7, q9}
- Lee `0`: {q6, q2, q3, q4, q7, q9} ⟶ {q6, q2, q3, q4, q7, q9} [q2→q3]; cierre λ añade {q6, q2, q4, q7, q9}
- Lee `0`: {q6, q2, q3, q4, q7, q9} ⟶ {q6, q2, q3, q4, q7, q9} [q2→q3]; cierre λ añade {q6, q2, q4, q7, q9}
- **Aceptada**: queda {q9} ∈ F.

## Cadena `001110`

- Inicio: {q0}
- Lee `0`: {q0} ⟶ {q1, q8, q6, q2, q4, q9} [q0→q1]; cierre λ añade {q8, q6, q2, q4, q9}
- Lee `0`: {q1, q8, q6, q2, q4, q9} ⟶ {q6, q2, q3, q4, q7, q9} [q2→q3]; cierre λ añade {q6, q2, q4, q7, q9}
- Lee `1`: {q6, q2, q3, q4, q7, q9} ⟶ {q6, q2, q4, q5, q7, q9} [q4→q5]; cierre λ añade {q6, q2, q4, q7, q9}
- Lee `1`: {q6, q2, q4, q5, q7, q9} ⟶ {q6, q2, q4, q5, q7, q9} [q4→q5]; cierre λ añade {q6, q2, q4, q7, q9}
- Lee `1`: {q6, q2, q4, q5, q7, q9} ⟶ {q6, q2, q4, q5, q7, q9} [q4→q5]; cierre λ añade {q6, q2, q4, q7, q9}
- Lee `0`: {q6, q2, q4, q5, q7, q9} ⟶ {q6, q2, q3, q4, q7, q9} [q2→q3]; cierre λ añade {q6, q2, q4, q7, q9}
- **Aceptada**: queda {q9} ∈ F.

## Cadena `011001010`

- Inicio: {q0}
- Lee `0`: {q0} ⟶ {q1, q8, q6, q2, q4, q9} [q0→q1]; cierre λ añade {q8, q6, q2, q4, q9}
- Lee `1`: {q1, q8, q6, q2, q4, q9} ⟶ {q6, q2, q4, q5, q7, q9} [q4→q5]; cierre λ añade {q6, q2, q4, q7, q9}
- Lee `1`: {q6, q2, q4, q5, q7, q9} ⟶ {q6, q2, q4, q5, q7, q9} [q4→q5]; cierre λ añade {q6, q2, q4, q7, q9}
- Lee `0`: {q6, q2, q4, q5, q7, q9} ⟶ {q6, q2, q3, q4, q7, q9} [q2→q3]; cierre λ añade {q6, q2, q4, q7, q9}
- Lee `0`: {q6, q2, q3, q4, q7, q9} ⟶ {q6, q2, q3, q4, q7, q9} [q2→q3]; cierre λ añade {q6, q2, q4, q7, q9}
- Lee `1`: {q6, q2, q3, q4, q7, q9} ⟶ {q6, q2, q4, q5, q7, q9} [q4→q5]; cierre λ añade {q6, q2, q4, q7, q9}
- Lee `0`: {q6, q2, q4, q5, q7, q9} ⟶ {q6, q2, q3, q4, q7, q9} [q2→q3]; cierre λ añade {q6, q2, q4, q7, q9}
- Lee `1`: {q6, q2, q3, q4, q7, q9} ⟶ {q6, q2, q4, q5, q7, q9} [q4→q5]; cierre λ añade {q6, q2, q4, q7, q9}
- Lee `0`: {q6, q2, q4, q5, q7, q9} ⟶ {q6, q2, q3, q4, q7, q9} [q2→q3]; cierre λ añade {q6, q2, q4, q7, q9}
- **Aceptada**: queda {q9} ∈ F.

## Cadena λ

- Inicio: {q0}
- **Rechazada**: ningún estado de {q0} es de aceptación.

## Cadena `1`

- Inicio: {q0}
- Lee `1`: {q0} ⟶ ∅ [ninguna transición]
- **Rechazada**: no queda ningún estado activo.

## Cadena `110`

- Inicio: {q0}
- Lee `1`: {q0} ⟶ ∅ [ninguna transición]
- Lee `1`: ∅ ⟶ ∅ [ninguna transición]
- Lee `0`: ∅ ⟶ ∅ [ninguna transición]
- **Rechazada**: no queda ningún estado activo.

## Cadena `11100`

- Inicio: {q0}
- Lee `1`: {q0} ⟶ ∅ [ninguna transición]
- Lee `1`: ∅ ⟶ ∅ [ninguna transición]
- Lee `1`: ∅ ⟶ ∅ [ninguna transición]
- Lee `0`: ∅ ⟶ ∅ [ninguna transición]
- Lee `0`: ∅ ⟶ ∅ [ninguna transición]
- **Rechazada**: no queda ningún estado activo.

## Cadena `10000111`

- Inicio: {q0}
- Lee `1`: {q0} ⟶ ∅ [ninguna transición]
- Lee `0`: ∅ ⟶ ∅ [ninguna transición]
- Lee `0`: ∅ ⟶ ∅ [ninguna transición]
- Lee `0`: ∅ ⟶ ∅ [ninguna transición]
- Lee `0`: ∅ ⟶ ∅ [ninguna transición]
- Lee `1`: ∅ ⟶ ∅ [ninguna transición]
- Lee `1`: ∅ ⟶ ∅ [ninguna transición]
- Lee `1`: ∅ ⟶ ∅ [ninguna transición]
- **Rechazada**: no queda ningún estado activo.
