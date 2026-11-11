# Recorridos: Lista 3 · Ejercicio 249

AFN-λ equivalente a la expresión (0* + 1)0*.

Autómata: `lista3-249` (AFN-λ).

## Cadena λ

- Inicio: {q6}; con cierre λ, {q6, q2, q0, q3, q4, q7, q10, q8, q11}
- **Aceptada**: queda {q11} ∈ F.

## Cadena `1`

- Inicio: {q6}; con cierre λ, {q6, q2, q0, q3, q4, q7, q10, q8, q11}
- Lee `1`: {q6, q2, q0, q3, q4, q7, q10, q8, q11} ⟶ {q5, q7, q10, q8, q11} [q4→q5]; cierre λ añade {q7, q10, q8, q11}
- **Aceptada**: queda {q11} ∈ F.

## Cadena `000`

- Inicio: {q6}; con cierre λ, {q6, q2, q0, q3, q4, q7, q10, q8, q11}
- Lee `0`: {q6, q2, q0, q3, q4, q7, q10, q8, q11} ⟶ {q0, q1, q3, q7, q10, q8, q9, q11} [q0→q1, q8→q9]; cierre λ añade {q0, q3, q7, q10, q8, q11}
- Lee `0`: {q0, q1, q3, q7, q10, q8, q9, q11} ⟶ {q0, q1, q3, q7, q10, q8, q9, q11} [q0→q1, q8→q9]; cierre λ añade {q0, q3, q7, q10, q8, q11}
- Lee `0`: {q0, q1, q3, q7, q10, q8, q9, q11} ⟶ {q0, q1, q3, q7, q10, q8, q9, q11} [q0→q1, q8→q9]; cierre λ añade {q0, q3, q7, q10, q8, q11}
- **Aceptada**: queda {q11} ∈ F.

## Cadena `00000`

- Inicio: {q6}; con cierre λ, {q6, q2, q0, q3, q4, q7, q10, q8, q11}
- Lee `0`: {q6, q2, q0, q3, q4, q7, q10, q8, q11} ⟶ {q0, q1, q3, q7, q10, q8, q9, q11} [q0→q1, q8→q9]; cierre λ añade {q0, q3, q7, q10, q8, q11}
- Lee `0`: {q0, q1, q3, q7, q10, q8, q9, q11} ⟶ {q0, q1, q3, q7, q10, q8, q9, q11} [q0→q1, q8→q9]; cierre λ añade {q0, q3, q7, q10, q8, q11}
- Lee `0`: {q0, q1, q3, q7, q10, q8, q9, q11} ⟶ {q0, q1, q3, q7, q10, q8, q9, q11} [q0→q1, q8→q9]; cierre λ añade {q0, q3, q7, q10, q8, q11}
- Lee `0`: {q0, q1, q3, q7, q10, q8, q9, q11} ⟶ {q0, q1, q3, q7, q10, q8, q9, q11} [q0→q1, q8→q9]; cierre λ añade {q0, q3, q7, q10, q8, q11}
- Lee `0`: {q0, q1, q3, q7, q10, q8, q9, q11} ⟶ {q0, q1, q3, q7, q10, q8, q9, q11} [q0→q1, q8→q9]; cierre λ añade {q0, q3, q7, q10, q8, q11}
- **Aceptada**: queda {q11} ∈ F.

## Cadena `10000000`

- Inicio: {q6}; con cierre λ, {q6, q2, q0, q3, q4, q7, q10, q8, q11}
- Lee `1`: {q6, q2, q0, q3, q4, q7, q10, q8, q11} ⟶ {q5, q7, q10, q8, q11} [q4→q5]; cierre λ añade {q7, q10, q8, q11}
- Lee `0`: {q5, q7, q10, q8, q11} ⟶ {q8, q9, q11} [q8→q9]; cierre λ añade {q8, q11}
- Lee `0`: {q8, q9, q11} ⟶ {q8, q9, q11} [q8→q9]; cierre λ añade {q8, q11}
- Lee `0`: {q8, q9, q11} ⟶ {q8, q9, q11} [q8→q9]; cierre λ añade {q8, q11}
- Lee `0`: {q8, q9, q11} ⟶ {q8, q9, q11} [q8→q9]; cierre λ añade {q8, q11}
- Lee `0`: {q8, q9, q11} ⟶ {q8, q9, q11} [q8→q9]; cierre λ añade {q8, q11}
- Lee `0`: {q8, q9, q11} ⟶ {q8, q9, q11} [q8→q9]; cierre λ añade {q8, q11}
- Lee `0`: {q8, q9, q11} ⟶ {q8, q9, q11} [q8→q9]; cierre λ añade {q8, q11}
- **Aceptada**: queda {q11} ∈ F.

## Cadena `11`

- Inicio: {q6}; con cierre λ, {q6, q2, q0, q3, q4, q7, q10, q8, q11}
- Lee `1`: {q6, q2, q0, q3, q4, q7, q10, q8, q11} ⟶ {q5, q7, q10, q8, q11} [q4→q5]; cierre λ añade {q7, q10, q8, q11}
- Lee `1`: {q5, q7, q10, q8, q11} ⟶ ∅ [ninguna transición]
- **Rechazada**: no queda ningún estado activo.

## Cadena `110`

- Inicio: {q6}; con cierre λ, {q6, q2, q0, q3, q4, q7, q10, q8, q11}
- Lee `1`: {q6, q2, q0, q3, q4, q7, q10, q8, q11} ⟶ {q5, q7, q10, q8, q11} [q4→q5]; cierre λ añade {q7, q10, q8, q11}
- Lee `1`: {q5, q7, q10, q8, q11} ⟶ ∅ [ninguna transición]
- Lee `0`: ∅ ⟶ ∅ [ninguna transición]
- **Rechazada**: no queda ningún estado activo.

## Cadena `11110`

- Inicio: {q6}; con cierre λ, {q6, q2, q0, q3, q4, q7, q10, q8, q11}
- Lee `1`: {q6, q2, q0, q3, q4, q7, q10, q8, q11} ⟶ {q5, q7, q10, q8, q11} [q4→q5]; cierre λ añade {q7, q10, q8, q11}
- Lee `1`: {q5, q7, q10, q8, q11} ⟶ ∅ [ninguna transición]
- Lee `1`: ∅ ⟶ ∅ [ninguna transición]
- Lee `1`: ∅ ⟶ ∅ [ninguna transición]
- Lee `0`: ∅ ⟶ ∅ [ninguna transición]
- **Rechazada**: no queda ningún estado activo.

## Cadena `1100101`

- Inicio: {q6}; con cierre λ, {q6, q2, q0, q3, q4, q7, q10, q8, q11}
- Lee `1`: {q6, q2, q0, q3, q4, q7, q10, q8, q11} ⟶ {q5, q7, q10, q8, q11} [q4→q5]; cierre λ añade {q7, q10, q8, q11}
- Lee `1`: {q5, q7, q10, q8, q11} ⟶ ∅ [ninguna transición]
- Lee `0`: ∅ ⟶ ∅ [ninguna transición]
- Lee `0`: ∅ ⟶ ∅ [ninguna transición]
- Lee `1`: ∅ ⟶ ∅ [ninguna transición]
- Lee `0`: ∅ ⟶ ∅ [ninguna transición]
- Lee `1`: ∅ ⟶ ∅ [ninguna transición]
- **Rechazada**: no queda ningún estado activo.

## Cadena `0100110101`

- Inicio: {q6}; con cierre λ, {q6, q2, q0, q3, q4, q7, q10, q8, q11}
- Lee `0`: {q6, q2, q0, q3, q4, q7, q10, q8, q11} ⟶ {q0, q1, q3, q7, q10, q8, q9, q11} [q0→q1, q8→q9]; cierre λ añade {q0, q3, q7, q10, q8, q11}
- Lee `1`: {q0, q1, q3, q7, q10, q8, q9, q11} ⟶ ∅ [ninguna transición]
- Lee `0`: ∅ ⟶ ∅ [ninguna transición]
- Lee `0`: ∅ ⟶ ∅ [ninguna transición]
- Lee `1`: ∅ ⟶ ∅ [ninguna transición]
- Lee `1`: ∅ ⟶ ∅ [ninguna transición]
- Lee `0`: ∅ ⟶ ∅ [ninguna transición]
- Lee `1`: ∅ ⟶ ∅ [ninguna transición]
- Lee `0`: ∅ ⟶ ∅ [ninguna transición]
- Lee `1`: ∅ ⟶ ∅ [ninguna transición]
- **Rechazada**: no queda ningún estado activo.
