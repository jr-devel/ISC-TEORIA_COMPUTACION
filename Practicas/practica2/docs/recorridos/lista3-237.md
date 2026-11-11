# Recorridos: Lista 3 · Ejercicio 237

Expresión regular sobre {0, 1} para: L = {x010 : x ∈ Σ*}.

Autómata: `lista3-237` (AFN-λ).

## Cadena `010`

- Inicio: {q6}; con cierre λ, {q6, q4, q0, q2, q7, q8}
- Lee `0`: {q6, q4, q0, q2, q7, q8} ⟶ {q4, q0, q1, q2, q5, q7, q8, q9, q10} [q0→q1, q8→q9]; cierre λ añade {q4, q0, q2, q5, q7, q8, q10}
- Lee `1`: {q4, q0, q1, q2, q5, q7, q8, q9, q10} ⟶ {q4, q0, q2, q3, q5, q7, q8, q11, q12} [q10→q11, q2→q3]; cierre λ añade {q4, q0, q2, q5, q7, q8, q12}
- Lee `0`: {q4, q0, q2, q3, q5, q7, q8, q11, q12} ⟶ {q4, q0, q1, q2, q5, q7, q8, q9, q10, q13} [q0→q1, q12→q13, q8→q9]; cierre λ añade {q4, q0, q2, q5, q7, q8, q10}
- **Aceptada**: queda {q13} ∈ F.

## Cadena `0010`

- Inicio: {q6}; con cierre λ, {q6, q4, q0, q2, q7, q8}
- Lee `0`: {q6, q4, q0, q2, q7, q8} ⟶ {q4, q0, q1, q2, q5, q7, q8, q9, q10} [q0→q1, q8→q9]; cierre λ añade {q4, q0, q2, q5, q7, q8, q10}
- Lee `0`: {q4, q0, q1, q2, q5, q7, q8, q9, q10} ⟶ {q4, q0, q1, q2, q5, q7, q8, q9, q10} [q0→q1, q8→q9]; cierre λ añade {q4, q0, q2, q5, q7, q8, q10}
- Lee `1`: {q4, q0, q1, q2, q5, q7, q8, q9, q10} ⟶ {q4, q0, q2, q3, q5, q7, q8, q11, q12} [q10→q11, q2→q3]; cierre λ añade {q4, q0, q2, q5, q7, q8, q12}
- Lee `0`: {q4, q0, q2, q3, q5, q7, q8, q11, q12} ⟶ {q4, q0, q1, q2, q5, q7, q8, q9, q10, q13} [q0→q1, q12→q13, q8→q9]; cierre λ añade {q4, q0, q2, q5, q7, q8, q10}
- **Aceptada**: queda {q13} ∈ F.

## Cadena `111010`

- Inicio: {q6}; con cierre λ, {q6, q4, q0, q2, q7, q8}
- Lee `1`: {q6, q4, q0, q2, q7, q8} ⟶ {q4, q0, q2, q3, q5, q7, q8} [q2→q3]; cierre λ añade {q4, q0, q2, q5, q7, q8}
- Lee `1`: {q4, q0, q2, q3, q5, q7, q8} ⟶ {q4, q0, q2, q3, q5, q7, q8} [q2→q3]; cierre λ añade {q4, q0, q2, q5, q7, q8}
- Lee `1`: {q4, q0, q2, q3, q5, q7, q8} ⟶ {q4, q0, q2, q3, q5, q7, q8} [q2→q3]; cierre λ añade {q4, q0, q2, q5, q7, q8}
- Lee `0`: {q4, q0, q2, q3, q5, q7, q8} ⟶ {q4, q0, q1, q2, q5, q7, q8, q9, q10} [q0→q1, q8→q9]; cierre λ añade {q4, q0, q2, q5, q7, q8, q10}
- Lee `1`: {q4, q0, q1, q2, q5, q7, q8, q9, q10} ⟶ {q4, q0, q2, q3, q5, q7, q8, q11, q12} [q10→q11, q2→q3]; cierre λ añade {q4, q0, q2, q5, q7, q8, q12}
- Lee `0`: {q4, q0, q2, q3, q5, q7, q8, q11, q12} ⟶ {q4, q0, q1, q2, q5, q7, q8, q9, q10, q13} [q0→q1, q12→q13, q8→q9]; cierre λ añade {q4, q0, q2, q5, q7, q8, q10}
- **Aceptada**: queda {q13} ∈ F.

## Cadena `01001010`

- Inicio: {q6}; con cierre λ, {q6, q4, q0, q2, q7, q8}
- Lee `0`: {q6, q4, q0, q2, q7, q8} ⟶ {q4, q0, q1, q2, q5, q7, q8, q9, q10} [q0→q1, q8→q9]; cierre λ añade {q4, q0, q2, q5, q7, q8, q10}
- Lee `1`: {q4, q0, q1, q2, q5, q7, q8, q9, q10} ⟶ {q4, q0, q2, q3, q5, q7, q8, q11, q12} [q10→q11, q2→q3]; cierre λ añade {q4, q0, q2, q5, q7, q8, q12}
- Lee `0`: {q4, q0, q2, q3, q5, q7, q8, q11, q12} ⟶ {q4, q0, q1, q2, q5, q7, q8, q9, q10, q13} [q0→q1, q12→q13, q8→q9]; cierre λ añade {q4, q0, q2, q5, q7, q8, q10}
- Lee `0`: {q4, q0, q1, q2, q5, q7, q8, q9, q10, q13} ⟶ {q4, q0, q1, q2, q5, q7, q8, q9, q10} [q0→q1, q8→q9]; cierre λ añade {q4, q0, q2, q5, q7, q8, q10}
- Lee `1`: {q4, q0, q1, q2, q5, q7, q8, q9, q10} ⟶ {q4, q0, q2, q3, q5, q7, q8, q11, q12} [q10→q11, q2→q3]; cierre λ añade {q4, q0, q2, q5, q7, q8, q12}
- Lee `0`: {q4, q0, q2, q3, q5, q7, q8, q11, q12} ⟶ {q4, q0, q1, q2, q5, q7, q8, q9, q10, q13} [q0→q1, q12→q13, q8→q9]; cierre λ añade {q4, q0, q2, q5, q7, q8, q10}
- Lee `1`: {q4, q0, q1, q2, q5, q7, q8, q9, q10, q13} ⟶ {q4, q0, q2, q3, q5, q7, q8, q11, q12} [q10→q11, q2→q3]; cierre λ añade {q4, q0, q2, q5, q7, q8, q12}
- Lee `0`: {q4, q0, q2, q3, q5, q7, q8, q11, q12} ⟶ {q4, q0, q1, q2, q5, q7, q8, q9, q10, q13} [q0→q1, q12→q13, q8→q9]; cierre λ añade {q4, q0, q2, q5, q7, q8, q10}
- **Aceptada**: queda {q13} ∈ F.

## Cadena `01110100010`

- Inicio: {q6}; con cierre λ, {q6, q4, q0, q2, q7, q8}
- Lee `0`: {q6, q4, q0, q2, q7, q8} ⟶ {q4, q0, q1, q2, q5, q7, q8, q9, q10} [q0→q1, q8→q9]; cierre λ añade {q4, q0, q2, q5, q7, q8, q10}
- Lee `1`: {q4, q0, q1, q2, q5, q7, q8, q9, q10} ⟶ {q4, q0, q2, q3, q5, q7, q8, q11, q12} [q10→q11, q2→q3]; cierre λ añade {q4, q0, q2, q5, q7, q8, q12}
- Lee `1`: {q4, q0, q2, q3, q5, q7, q8, q11, q12} ⟶ {q4, q0, q2, q3, q5, q7, q8} [q2→q3]; cierre λ añade {q4, q0, q2, q5, q7, q8}
- Lee `1`: {q4, q0, q2, q3, q5, q7, q8} ⟶ {q4, q0, q2, q3, q5, q7, q8} [q2→q3]; cierre λ añade {q4, q0, q2, q5, q7, q8}
- Lee `0`: {q4, q0, q2, q3, q5, q7, q8} ⟶ {q4, q0, q1, q2, q5, q7, q8, q9, q10} [q0→q1, q8→q9]; cierre λ añade {q4, q0, q2, q5, q7, q8, q10}
- Lee `1`: {q4, q0, q1, q2, q5, q7, q8, q9, q10} ⟶ {q4, q0, q2, q3, q5, q7, q8, q11, q12} [q10→q11, q2→q3]; cierre λ añade {q4, q0, q2, q5, q7, q8, q12}
- Lee `0`: {q4, q0, q2, q3, q5, q7, q8, q11, q12} ⟶ {q4, q0, q1, q2, q5, q7, q8, q9, q10, q13} [q0→q1, q12→q13, q8→q9]; cierre λ añade {q4, q0, q2, q5, q7, q8, q10}
- Lee `0`: {q4, q0, q1, q2, q5, q7, q8, q9, q10, q13} ⟶ {q4, q0, q1, q2, q5, q7, q8, q9, q10} [q0→q1, q8→q9]; cierre λ añade {q4, q0, q2, q5, q7, q8, q10}
- Lee `0`: {q4, q0, q1, q2, q5, q7, q8, q9, q10} ⟶ {q4, q0, q1, q2, q5, q7, q8, q9, q10} [q0→q1, q8→q9]; cierre λ añade {q4, q0, q2, q5, q7, q8, q10}
- Lee `1`: {q4, q0, q1, q2, q5, q7, q8, q9, q10} ⟶ {q4, q0, q2, q3, q5, q7, q8, q11, q12} [q10→q11, q2→q3]; cierre λ añade {q4, q0, q2, q5, q7, q8, q12}
- Lee `0`: {q4, q0, q2, q3, q5, q7, q8, q11, q12} ⟶ {q4, q0, q1, q2, q5, q7, q8, q9, q10, q13} [q0→q1, q12→q13, q8→q9]; cierre λ añade {q4, q0, q2, q5, q7, q8, q10}
- **Aceptada**: queda {q13} ∈ F.

## Cadena λ

- Inicio: {q6}; con cierre λ, {q6, q4, q0, q2, q7, q8}
- **Rechazada**: ningún estado de {q6, q4, q0, q2, q7, q8} es de aceptación.

## Cadena `0`

- Inicio: {q6}; con cierre λ, {q6, q4, q0, q2, q7, q8}
- Lee `0`: {q6, q4, q0, q2, q7, q8} ⟶ {q4, q0, q1, q2, q5, q7, q8, q9, q10} [q0→q1, q8→q9]; cierre λ añade {q4, q0, q2, q5, q7, q8, q10}
- **Rechazada**: ningún estado de {q4, q0, q1, q2, q5, q7, q8, q9, q10} es de aceptación.

## Cadena `110`

- Inicio: {q6}; con cierre λ, {q6, q4, q0, q2, q7, q8}
- Lee `1`: {q6, q4, q0, q2, q7, q8} ⟶ {q4, q0, q2, q3, q5, q7, q8} [q2→q3]; cierre λ añade {q4, q0, q2, q5, q7, q8}
- Lee `1`: {q4, q0, q2, q3, q5, q7, q8} ⟶ {q4, q0, q2, q3, q5, q7, q8} [q2→q3]; cierre λ añade {q4, q0, q2, q5, q7, q8}
- Lee `0`: {q4, q0, q2, q3, q5, q7, q8} ⟶ {q4, q0, q1, q2, q5, q7, q8, q9, q10} [q0→q1, q8→q9]; cierre λ añade {q4, q0, q2, q5, q7, q8, q10}
- **Rechazada**: ningún estado de {q4, q0, q1, q2, q5, q7, q8, q9, q10} es de aceptación.

## Cadena `00110`

- Inicio: {q6}; con cierre λ, {q6, q4, q0, q2, q7, q8}
- Lee `0`: {q6, q4, q0, q2, q7, q8} ⟶ {q4, q0, q1, q2, q5, q7, q8, q9, q10} [q0→q1, q8→q9]; cierre λ añade {q4, q0, q2, q5, q7, q8, q10}
- Lee `0`: {q4, q0, q1, q2, q5, q7, q8, q9, q10} ⟶ {q4, q0, q1, q2, q5, q7, q8, q9, q10} [q0→q1, q8→q9]; cierre λ añade {q4, q0, q2, q5, q7, q8, q10}
- Lee `1`: {q4, q0, q1, q2, q5, q7, q8, q9, q10} ⟶ {q4, q0, q2, q3, q5, q7, q8, q11, q12} [q10→q11, q2→q3]; cierre λ añade {q4, q0, q2, q5, q7, q8, q12}
- Lee `1`: {q4, q0, q2, q3, q5, q7, q8, q11, q12} ⟶ {q4, q0, q2, q3, q5, q7, q8} [q2→q3]; cierre λ añade {q4, q0, q2, q5, q7, q8}
- Lee `0`: {q4, q0, q2, q3, q5, q7, q8} ⟶ {q4, q0, q1, q2, q5, q7, q8, q9, q10} [q0→q1, q8→q9]; cierre λ añade {q4, q0, q2, q5, q7, q8, q10}
- **Rechazada**: ningún estado de {q4, q0, q1, q2, q5, q7, q8, q9, q10} es de aceptación.

## Cadena `00001011`

- Inicio: {q6}; con cierre λ, {q6, q4, q0, q2, q7, q8}
- Lee `0`: {q6, q4, q0, q2, q7, q8} ⟶ {q4, q0, q1, q2, q5, q7, q8, q9, q10} [q0→q1, q8→q9]; cierre λ añade {q4, q0, q2, q5, q7, q8, q10}
- Lee `0`: {q4, q0, q1, q2, q5, q7, q8, q9, q10} ⟶ {q4, q0, q1, q2, q5, q7, q8, q9, q10} [q0→q1, q8→q9]; cierre λ añade {q4, q0, q2, q5, q7, q8, q10}
- Lee `0`: {q4, q0, q1, q2, q5, q7, q8, q9, q10} ⟶ {q4, q0, q1, q2, q5, q7, q8, q9, q10} [q0→q1, q8→q9]; cierre λ añade {q4, q0, q2, q5, q7, q8, q10}
- Lee `0`: {q4, q0, q1, q2, q5, q7, q8, q9, q10} ⟶ {q4, q0, q1, q2, q5, q7, q8, q9, q10} [q0→q1, q8→q9]; cierre λ añade {q4, q0, q2, q5, q7, q8, q10}
- Lee `1`: {q4, q0, q1, q2, q5, q7, q8, q9, q10} ⟶ {q4, q0, q2, q3, q5, q7, q8, q11, q12} [q10→q11, q2→q3]; cierre λ añade {q4, q0, q2, q5, q7, q8, q12}
- Lee `0`: {q4, q0, q2, q3, q5, q7, q8, q11, q12} ⟶ {q4, q0, q1, q2, q5, q7, q8, q9, q10, q13} [q0→q1, q12→q13, q8→q9]; cierre λ añade {q4, q0, q2, q5, q7, q8, q10}
- Lee `1`: {q4, q0, q1, q2, q5, q7, q8, q9, q10, q13} ⟶ {q4, q0, q2, q3, q5, q7, q8, q11, q12} [q10→q11, q2→q3]; cierre λ añade {q4, q0, q2, q5, q7, q8, q12}
- Lee `1`: {q4, q0, q2, q3, q5, q7, q8, q11, q12} ⟶ {q4, q0, q2, q3, q5, q7, q8} [q2→q3]; cierre λ añade {q4, q0, q2, q5, q7, q8}
- **Rechazada**: ningún estado de {q4, q0, q2, q3, q5, q7, q8} es de aceptación.

## Cadena `11`

- Inicio: {q6}; con cierre λ, {q6, q4, q0, q2, q7, q8}
- Lee `1`: {q6, q4, q0, q2, q7, q8} ⟶ {q4, q0, q2, q3, q5, q7, q8} [q2→q3]; cierre λ añade {q4, q0, q2, q5, q7, q8}
- Lee `1`: {q4, q0, q2, q3, q5, q7, q8} ⟶ {q4, q0, q2, q3, q5, q7, q8} [q2→q3]; cierre λ añade {q4, q0, q2, q5, q7, q8}
- **Rechazada**: ningún estado de {q4, q0, q2, q3, q5, q7, q8} es de aceptación.
