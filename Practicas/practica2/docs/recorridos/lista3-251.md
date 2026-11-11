# Recorridos: Lista 3 · Ejercicio 251

AFN-λ equivalente a la expresión (0 + 1*)0 + 1*1.

Autómata: `lista3-251` (AFN-λ).

## Cadena `0`

- Inicio: {q16}; con cierre λ, {q16, q6, q0, q4, q2, q5, q7, q8, q12, q10, q13, q14}
- Lee `0`: {q16, q6, q0, q4, q2, q5, q7, q8, q12, q10, q13, q14} ⟶ {q1, q7, q8, q9, q17} [q0→q1, q8→q9]; cierre λ añade {q7, q8, q17}
- **Aceptada**: queda {q17} ∈ F.

## Cadena `11`

- Inicio: {q16}; con cierre λ, {q16, q6, q0, q4, q2, q5, q7, q8, q12, q10, q13, q14}
- Lee `1`: {q16, q6, q0, q4, q2, q5, q7, q8, q12, q10, q13, q14} ⟶ {q2, q3, q5, q7, q8, q10, q11, q13, q14, q15, q17} [q10→q11, q14→q15, q2→q3]; cierre λ añade {q2, q5, q7, q8, q10, q13, q14, q17}
- Lee `1`: {q2, q3, q5, q7, q8, q10, q11, q13, q14, q15, q17} ⟶ {q2, q3, q5, q7, q8, q10, q11, q13, q14, q15, q17} [q10→q11, q14→q15, q2→q3]; cierre λ añade {q2, q5, q7, q8, q10, q13, q14, q17}
- **Aceptada**: queda {q17} ∈ F.

## Cadena `1111`

- Inicio: {q16}; con cierre λ, {q16, q6, q0, q4, q2, q5, q7, q8, q12, q10, q13, q14}
- Lee `1`: {q16, q6, q0, q4, q2, q5, q7, q8, q12, q10, q13, q14} ⟶ {q2, q3, q5, q7, q8, q10, q11, q13, q14, q15, q17} [q10→q11, q14→q15, q2→q3]; cierre λ añade {q2, q5, q7, q8, q10, q13, q14, q17}
- Lee `1`: {q2, q3, q5, q7, q8, q10, q11, q13, q14, q15, q17} ⟶ {q2, q3, q5, q7, q8, q10, q11, q13, q14, q15, q17} [q10→q11, q14→q15, q2→q3]; cierre λ añade {q2, q5, q7, q8, q10, q13, q14, q17}
- Lee `1`: {q2, q3, q5, q7, q8, q10, q11, q13, q14, q15, q17} ⟶ {q2, q3, q5, q7, q8, q10, q11, q13, q14, q15, q17} [q10→q11, q14→q15, q2→q3]; cierre λ añade {q2, q5, q7, q8, q10, q13, q14, q17}
- Lee `1`: {q2, q3, q5, q7, q8, q10, q11, q13, q14, q15, q17} ⟶ {q2, q3, q5, q7, q8, q10, q11, q13, q14, q15, q17} [q10→q11, q14→q15, q2→q3]; cierre λ añade {q2, q5, q7, q8, q10, q13, q14, q17}
- **Aceptada**: queda {q17} ∈ F.

## Cadena `111111`

- Inicio: {q16}; con cierre λ, {q16, q6, q0, q4, q2, q5, q7, q8, q12, q10, q13, q14}
- Lee `1`: {q16, q6, q0, q4, q2, q5, q7, q8, q12, q10, q13, q14} ⟶ {q2, q3, q5, q7, q8, q10, q11, q13, q14, q15, q17} [q10→q11, q14→q15, q2→q3]; cierre λ añade {q2, q5, q7, q8, q10, q13, q14, q17}
- Lee `1`: {q2, q3, q5, q7, q8, q10, q11, q13, q14, q15, q17} ⟶ {q2, q3, q5, q7, q8, q10, q11, q13, q14, q15, q17} [q10→q11, q14→q15, q2→q3]; cierre λ añade {q2, q5, q7, q8, q10, q13, q14, q17}
- Lee `1`: {q2, q3, q5, q7, q8, q10, q11, q13, q14, q15, q17} ⟶ {q2, q3, q5, q7, q8, q10, q11, q13, q14, q15, q17} [q10→q11, q14→q15, q2→q3]; cierre λ añade {q2, q5, q7, q8, q10, q13, q14, q17}
- Lee `1`: {q2, q3, q5, q7, q8, q10, q11, q13, q14, q15, q17} ⟶ {q2, q3, q5, q7, q8, q10, q11, q13, q14, q15, q17} [q10→q11, q14→q15, q2→q3]; cierre λ añade {q2, q5, q7, q8, q10, q13, q14, q17}
- Lee `1`: {q2, q3, q5, q7, q8, q10, q11, q13, q14, q15, q17} ⟶ {q2, q3, q5, q7, q8, q10, q11, q13, q14, q15, q17} [q10→q11, q14→q15, q2→q3]; cierre λ añade {q2, q5, q7, q8, q10, q13, q14, q17}
- Lee `1`: {q2, q3, q5, q7, q8, q10, q11, q13, q14, q15, q17} ⟶ {q2, q3, q5, q7, q8, q10, q11, q13, q14, q15, q17} [q10→q11, q14→q15, q2→q3]; cierre λ añade {q2, q5, q7, q8, q10, q13, q14, q17}
- **Aceptada**: queda {q17} ∈ F.

## Cadena `111111110`

- Inicio: {q16}; con cierre λ, {q16, q6, q0, q4, q2, q5, q7, q8, q12, q10, q13, q14}
- Lee `1`: {q16, q6, q0, q4, q2, q5, q7, q8, q12, q10, q13, q14} ⟶ {q2, q3, q5, q7, q8, q10, q11, q13, q14, q15, q17} [q10→q11, q14→q15, q2→q3]; cierre λ añade {q2, q5, q7, q8, q10, q13, q14, q17}
- Lee `1`: {q2, q3, q5, q7, q8, q10, q11, q13, q14, q15, q17} ⟶ {q2, q3, q5, q7, q8, q10, q11, q13, q14, q15, q17} [q10→q11, q14→q15, q2→q3]; cierre λ añade {q2, q5, q7, q8, q10, q13, q14, q17}
- Lee `1`: {q2, q3, q5, q7, q8, q10, q11, q13, q14, q15, q17} ⟶ {q2, q3, q5, q7, q8, q10, q11, q13, q14, q15, q17} [q10→q11, q14→q15, q2→q3]; cierre λ añade {q2, q5, q7, q8, q10, q13, q14, q17}
- Lee `1`: {q2, q3, q5, q7, q8, q10, q11, q13, q14, q15, q17} ⟶ {q2, q3, q5, q7, q8, q10, q11, q13, q14, q15, q17} [q10→q11, q14→q15, q2→q3]; cierre λ añade {q2, q5, q7, q8, q10, q13, q14, q17}
- Lee `1`: {q2, q3, q5, q7, q8, q10, q11, q13, q14, q15, q17} ⟶ {q2, q3, q5, q7, q8, q10, q11, q13, q14, q15, q17} [q10→q11, q14→q15, q2→q3]; cierre λ añade {q2, q5, q7, q8, q10, q13, q14, q17}
- Lee `1`: {q2, q3, q5, q7, q8, q10, q11, q13, q14, q15, q17} ⟶ {q2, q3, q5, q7, q8, q10, q11, q13, q14, q15, q17} [q10→q11, q14→q15, q2→q3]; cierre λ añade {q2, q5, q7, q8, q10, q13, q14, q17}
- Lee `1`: {q2, q3, q5, q7, q8, q10, q11, q13, q14, q15, q17} ⟶ {q2, q3, q5, q7, q8, q10, q11, q13, q14, q15, q17} [q10→q11, q14→q15, q2→q3]; cierre λ añade {q2, q5, q7, q8, q10, q13, q14, q17}
- Lee `1`: {q2, q3, q5, q7, q8, q10, q11, q13, q14, q15, q17} ⟶ {q2, q3, q5, q7, q8, q10, q11, q13, q14, q15, q17} [q10→q11, q14→q15, q2→q3]; cierre λ añade {q2, q5, q7, q8, q10, q13, q14, q17}
- Lee `0`: {q2, q3, q5, q7, q8, q10, q11, q13, q14, q15, q17} ⟶ {q9, q17} [q8→q9]; cierre λ añade {q17}
- **Aceptada**: queda {q17} ∈ F.

## Cadena λ

- Inicio: {q16}; con cierre λ, {q16, q6, q0, q4, q2, q5, q7, q8, q12, q10, q13, q14}
- **Rechazada**: ningún estado de {q16, q6, q0, q4, q2, q5, q7, q8, q12, q10, q13, q14} es de aceptación.

## Cadena `01`

- Inicio: {q16}; con cierre λ, {q16, q6, q0, q4, q2, q5, q7, q8, q12, q10, q13, q14}
- Lee `0`: {q16, q6, q0, q4, q2, q5, q7, q8, q12, q10, q13, q14} ⟶ {q1, q7, q8, q9, q17} [q0→q1, q8→q9]; cierre λ añade {q7, q8, q17}
- Lee `1`: {q1, q7, q8, q9, q17} ⟶ ∅ [ninguna transición]
- **Rechazada**: no queda ningún estado activo.

## Cadena `010111`

- Inicio: {q16}; con cierre λ, {q16, q6, q0, q4, q2, q5, q7, q8, q12, q10, q13, q14}
- Lee `0`: {q16, q6, q0, q4, q2, q5, q7, q8, q12, q10, q13, q14} ⟶ {q1, q7, q8, q9, q17} [q0→q1, q8→q9]; cierre λ añade {q7, q8, q17}
- Lee `1`: {q1, q7, q8, q9, q17} ⟶ ∅ [ninguna transición]
- Lee `0`: ∅ ⟶ ∅ [ninguna transición]
- Lee `1`: ∅ ⟶ ∅ [ninguna transición]
- Lee `1`: ∅ ⟶ ∅ [ninguna transición]
- Lee `1`: ∅ ⟶ ∅ [ninguna transición]
- **Rechazada**: no queda ningún estado activo.

## Cadena `11001100100`

- Inicio: {q16}; con cierre λ, {q16, q6, q0, q4, q2, q5, q7, q8, q12, q10, q13, q14}
- Lee `1`: {q16, q6, q0, q4, q2, q5, q7, q8, q12, q10, q13, q14} ⟶ {q2, q3, q5, q7, q8, q10, q11, q13, q14, q15, q17} [q10→q11, q14→q15, q2→q3]; cierre λ añade {q2, q5, q7, q8, q10, q13, q14, q17}
- Lee `1`: {q2, q3, q5, q7, q8, q10, q11, q13, q14, q15, q17} ⟶ {q2, q3, q5, q7, q8, q10, q11, q13, q14, q15, q17} [q10→q11, q14→q15, q2→q3]; cierre λ añade {q2, q5, q7, q8, q10, q13, q14, q17}
- Lee `0`: {q2, q3, q5, q7, q8, q10, q11, q13, q14, q15, q17} ⟶ {q9, q17} [q8→q9]; cierre λ añade {q17}
- Lee `0`: {q9, q17} ⟶ ∅ [ninguna transición]
- Lee `1`: ∅ ⟶ ∅ [ninguna transición]
- Lee `1`: ∅ ⟶ ∅ [ninguna transición]
- Lee `0`: ∅ ⟶ ∅ [ninguna transición]
- Lee `0`: ∅ ⟶ ∅ [ninguna transición]
- Lee `1`: ∅ ⟶ ∅ [ninguna transición]
- Lee `0`: ∅ ⟶ ∅ [ninguna transición]
- Lee `0`: ∅ ⟶ ∅ [ninguna transición]
- **Rechazada**: no queda ningún estado activo.

## Cadena `10110011110010`

- Inicio: {q16}; con cierre λ, {q16, q6, q0, q4, q2, q5, q7, q8, q12, q10, q13, q14}
- Lee `1`: {q16, q6, q0, q4, q2, q5, q7, q8, q12, q10, q13, q14} ⟶ {q2, q3, q5, q7, q8, q10, q11, q13, q14, q15, q17} [q10→q11, q14→q15, q2→q3]; cierre λ añade {q2, q5, q7, q8, q10, q13, q14, q17}
- Lee `0`: {q2, q3, q5, q7, q8, q10, q11, q13, q14, q15, q17} ⟶ {q9, q17} [q8→q9]; cierre λ añade {q17}
- Lee `1`: {q9, q17} ⟶ ∅ [ninguna transición]
- Lee `1`: ∅ ⟶ ∅ [ninguna transición]
- Lee `0`: ∅ ⟶ ∅ [ninguna transición]
- Lee `0`: ∅ ⟶ ∅ [ninguna transición]
- Lee `1`: ∅ ⟶ ∅ [ninguna transición]
- Lee `1`: ∅ ⟶ ∅ [ninguna transición]
- Lee `1`: ∅ ⟶ ∅ [ninguna transición]
- Lee `1`: ∅ ⟶ ∅ [ninguna transición]
- Lee `0`: ∅ ⟶ ∅ [ninguna transición]
- Lee `0`: ∅ ⟶ ∅ [ninguna transición]
- Lee `1`: ∅ ⟶ ∅ [ninguna transición]
- Lee `0`: ∅ ⟶ ∅ [ninguna transición]
- **Rechazada**: no queda ningún estado activo.
