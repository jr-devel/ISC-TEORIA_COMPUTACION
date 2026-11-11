# Recorridos: Lista 3 · Ejercicio 250

AFN-λ equivalente a la expresión 0*1* + 1*0.

Autómata: `lista3-250` (AFN-λ).

## Cadena λ

- Inicio: {q14}; con cierre λ, {q14, q2, q0, q3, q6, q4, q7, q10, q8, q11, q12, q15}
- **Aceptada**: queda {q15} ∈ F.

## Cadena `0`

- Inicio: {q14}; con cierre λ, {q14, q2, q0, q3, q6, q4, q7, q10, q8, q11, q12, q15}
- Lee `0`: {q14, q2, q0, q3, q6, q4, q7, q10, q8, q11, q12, q15} ⟶ {q0, q1, q3, q6, q4, q7, q13, q15} [q0→q1, q12→q13]; cierre λ añade {q0, q3, q6, q4, q7, q15}
- **Aceptada**: queda {q15} ∈ F.

## Cadena `011`

- Inicio: {q14}; con cierre λ, {q14, q2, q0, q3, q6, q4, q7, q10, q8, q11, q12, q15}
- Lee `0`: {q14, q2, q0, q3, q6, q4, q7, q10, q8, q11, q12, q15} ⟶ {q0, q1, q3, q6, q4, q7, q13, q15} [q0→q1, q12→q13]; cierre λ añade {q0, q3, q6, q4, q7, q15}
- Lee `1`: {q0, q1, q3, q6, q4, q7, q13, q15} ⟶ {q4, q5, q7, q15} [q4→q5]; cierre λ añade {q4, q7, q15}
- Lee `1`: {q4, q5, q7, q15} ⟶ {q4, q5, q7, q15} [q4→q5]; cierre λ añade {q4, q7, q15}
- **Aceptada**: queda {q15} ∈ F.

## Cadena `00011`

- Inicio: {q14}; con cierre λ, {q14, q2, q0, q3, q6, q4, q7, q10, q8, q11, q12, q15}
- Lee `0`: {q14, q2, q0, q3, q6, q4, q7, q10, q8, q11, q12, q15} ⟶ {q0, q1, q3, q6, q4, q7, q13, q15} [q0→q1, q12→q13]; cierre λ añade {q0, q3, q6, q4, q7, q15}
- Lee `0`: {q0, q1, q3, q6, q4, q7, q13, q15} ⟶ {q0, q1, q3, q6, q4, q7, q15} [q0→q1]; cierre λ añade {q0, q3, q6, q4, q7, q15}
- Lee `0`: {q0, q1, q3, q6, q4, q7, q15} ⟶ {q0, q1, q3, q6, q4, q7, q15} [q0→q1]; cierre λ añade {q0, q3, q6, q4, q7, q15}
- Lee `1`: {q0, q1, q3, q6, q4, q7, q15} ⟶ {q4, q5, q7, q15} [q4→q5]; cierre λ añade {q4, q7, q15}
- Lee `1`: {q4, q5, q7, q15} ⟶ {q4, q5, q7, q15} [q4→q5]; cierre λ añade {q4, q7, q15}
- **Aceptada**: queda {q15} ∈ F.

## Cadena `01111111`

- Inicio: {q14}; con cierre λ, {q14, q2, q0, q3, q6, q4, q7, q10, q8, q11, q12, q15}
- Lee `0`: {q14, q2, q0, q3, q6, q4, q7, q10, q8, q11, q12, q15} ⟶ {q0, q1, q3, q6, q4, q7, q13, q15} [q0→q1, q12→q13]; cierre λ añade {q0, q3, q6, q4, q7, q15}
- Lee `1`: {q0, q1, q3, q6, q4, q7, q13, q15} ⟶ {q4, q5, q7, q15} [q4→q5]; cierre λ añade {q4, q7, q15}
- Lee `1`: {q4, q5, q7, q15} ⟶ {q4, q5, q7, q15} [q4→q5]; cierre λ añade {q4, q7, q15}
- Lee `1`: {q4, q5, q7, q15} ⟶ {q4, q5, q7, q15} [q4→q5]; cierre λ añade {q4, q7, q15}
- Lee `1`: {q4, q5, q7, q15} ⟶ {q4, q5, q7, q15} [q4→q5]; cierre λ añade {q4, q7, q15}
- Lee `1`: {q4, q5, q7, q15} ⟶ {q4, q5, q7, q15} [q4→q5]; cierre λ añade {q4, q7, q15}
- Lee `1`: {q4, q5, q7, q15} ⟶ {q4, q5, q7, q15} [q4→q5]; cierre λ añade {q4, q7, q15}
- Lee `1`: {q4, q5, q7, q15} ⟶ {q4, q5, q7, q15} [q4→q5]; cierre λ añade {q4, q7, q15}
- **Aceptada**: queda {q15} ∈ F.

## Cadena `100`

- Inicio: {q14}; con cierre λ, {q14, q2, q0, q3, q6, q4, q7, q10, q8, q11, q12, q15}
- Lee `1`: {q14, q2, q0, q3, q6, q4, q7, q10, q8, q11, q12, q15} ⟶ {q4, q5, q7, q8, q9, q11, q12, q15} [q4→q5, q8→q9]; cierre λ añade {q4, q7, q8, q11, q12, q15}
- Lee `0`: {q4, q5, q7, q8, q9, q11, q12, q15} ⟶ {q13, q15} [q12→q13]; cierre λ añade {q15}
- Lee `0`: {q13, q15} ⟶ ∅ [ninguna transición]
- **Rechazada**: no queda ningún estado activo.

## Cadena `1010`

- Inicio: {q14}; con cierre λ, {q14, q2, q0, q3, q6, q4, q7, q10, q8, q11, q12, q15}
- Lee `1`: {q14, q2, q0, q3, q6, q4, q7, q10, q8, q11, q12, q15} ⟶ {q4, q5, q7, q8, q9, q11, q12, q15} [q4→q5, q8→q9]; cierre λ añade {q4, q7, q8, q11, q12, q15}
- Lee `0`: {q4, q5, q7, q8, q9, q11, q12, q15} ⟶ {q13, q15} [q12→q13]; cierre λ añade {q15}
- Lee `1`: {q13, q15} ⟶ ∅ [ninguna transición]
- Lee `0`: ∅ ⟶ ∅ [ninguna transición]
- **Rechazada**: no queda ningún estado activo.

## Cadena `100000`

- Inicio: {q14}; con cierre λ, {q14, q2, q0, q3, q6, q4, q7, q10, q8, q11, q12, q15}
- Lee `1`: {q14, q2, q0, q3, q6, q4, q7, q10, q8, q11, q12, q15} ⟶ {q4, q5, q7, q8, q9, q11, q12, q15} [q4→q5, q8→q9]; cierre λ añade {q4, q7, q8, q11, q12, q15}
- Lee `0`: {q4, q5, q7, q8, q9, q11, q12, q15} ⟶ {q13, q15} [q12→q13]; cierre λ añade {q15}
- Lee `0`: {q13, q15} ⟶ ∅ [ninguna transición]
- Lee `0`: ∅ ⟶ ∅ [ninguna transición]
- Lee `0`: ∅ ⟶ ∅ [ninguna transición]
- Lee `0`: ∅ ⟶ ∅ [ninguna transición]
- **Rechazada**: no queda ningún estado activo.

## Cadena `11001110`

- Inicio: {q14}; con cierre λ, {q14, q2, q0, q3, q6, q4, q7, q10, q8, q11, q12, q15}
- Lee `1`: {q14, q2, q0, q3, q6, q4, q7, q10, q8, q11, q12, q15} ⟶ {q4, q5, q7, q8, q9, q11, q12, q15} [q4→q5, q8→q9]; cierre λ añade {q4, q7, q8, q11, q12, q15}
- Lee `1`: {q4, q5, q7, q8, q9, q11, q12, q15} ⟶ {q4, q5, q7, q8, q9, q11, q12, q15} [q4→q5, q8→q9]; cierre λ añade {q4, q7, q8, q11, q12, q15}
- Lee `0`: {q4, q5, q7, q8, q9, q11, q12, q15} ⟶ {q13, q15} [q12→q13]; cierre λ añade {q15}
- Lee `0`: {q13, q15} ⟶ ∅ [ninguna transición]
- Lee `1`: ∅ ⟶ ∅ [ninguna transición]
- Lee `1`: ∅ ⟶ ∅ [ninguna transición]
- Lee `1`: ∅ ⟶ ∅ [ninguna transición]
- Lee `0`: ∅ ⟶ ∅ [ninguna transición]
- **Rechazada**: no queda ningún estado activo.

## Cadena `10111100000`

- Inicio: {q14}; con cierre λ, {q14, q2, q0, q3, q6, q4, q7, q10, q8, q11, q12, q15}
- Lee `1`: {q14, q2, q0, q3, q6, q4, q7, q10, q8, q11, q12, q15} ⟶ {q4, q5, q7, q8, q9, q11, q12, q15} [q4→q5, q8→q9]; cierre λ añade {q4, q7, q8, q11, q12, q15}
- Lee `0`: {q4, q5, q7, q8, q9, q11, q12, q15} ⟶ {q13, q15} [q12→q13]; cierre λ añade {q15}
- Lee `1`: {q13, q15} ⟶ ∅ [ninguna transición]
- Lee `1`: ∅ ⟶ ∅ [ninguna transición]
- Lee `1`: ∅ ⟶ ∅ [ninguna transición]
- Lee `1`: ∅ ⟶ ∅ [ninguna transición]
- Lee `0`: ∅ ⟶ ∅ [ninguna transición]
- Lee `0`: ∅ ⟶ ∅ [ninguna transición]
- Lee `0`: ∅ ⟶ ∅ [ninguna transición]
- Lee `0`: ∅ ⟶ ∅ [ninguna transición]
- Lee `0`: ∅ ⟶ ∅ [ninguna transición]
- **Rechazada**: no queda ningún estado activo.
