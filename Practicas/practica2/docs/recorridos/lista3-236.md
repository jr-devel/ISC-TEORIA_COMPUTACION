# Recorridos: Lista 3 · Ejercicio 236

Expresión regular sobre {0, 1} para: L = {x001y : x, y ∈ Σ*}.

Autómata: `lista3-236` (AFN-λ).

## Cadena `001`

- Inicio: {q6}; con cierre λ, {q6, q4, q0, q2, q7, q8}
- Lee `0`: {q6, q4, q0, q2, q7, q8} ⟶ {q4, q0, q1, q2, q5, q7, q8, q9, q10} [q0→q1, q8→q9]; cierre λ añade {q4, q0, q2, q5, q7, q8, q10}
- Lee `0`: {q4, q0, q1, q2, q5, q7, q8, q9, q10} ⟶ {q4, q0, q1, q2, q5, q7, q8, q9, q10, q11, q12} [q0→q1, q10→q11, q8→q9]; cierre λ añade {q4, q0, q2, q5, q7, q8, q10, q12}
- Lee `1`: {q4, q0, q1, q2, q5, q7, q8, q9, q10, q11, q12} ⟶ {q4, q0, q2, q3, q5, q7, q8, q13, q20, q18, q14, q16, q21} [q12→q13, q2→q3]; cierre λ añade {q4, q0, q2, q5, q7, q8, q20, q18, q14, q16, q21}
- **Aceptada**: queda {q21} ∈ F.

## Cadena `0001`

- Inicio: {q6}; con cierre λ, {q6, q4, q0, q2, q7, q8}
- Lee `0`: {q6, q4, q0, q2, q7, q8} ⟶ {q4, q0, q1, q2, q5, q7, q8, q9, q10} [q0→q1, q8→q9]; cierre λ añade {q4, q0, q2, q5, q7, q8, q10}
- Lee `0`: {q4, q0, q1, q2, q5, q7, q8, q9, q10} ⟶ {q4, q0, q1, q2, q5, q7, q8, q9, q10, q11, q12} [q0→q1, q10→q11, q8→q9]; cierre λ añade {q4, q0, q2, q5, q7, q8, q10, q12}
- Lee `0`: {q4, q0, q1, q2, q5, q7, q8, q9, q10, q11, q12} ⟶ {q4, q0, q1, q2, q5, q7, q8, q9, q10, q11, q12} [q0→q1, q10→q11, q8→q9]; cierre λ añade {q4, q0, q2, q5, q7, q8, q10, q12}
- Lee `1`: {q4, q0, q1, q2, q5, q7, q8, q9, q10, q11, q12} ⟶ {q4, q0, q2, q3, q5, q7, q8, q13, q20, q18, q14, q16, q21} [q12→q13, q2→q3]; cierre λ añade {q4, q0, q2, q5, q7, q8, q20, q18, q14, q16, q21}
- **Aceptada**: queda {q21} ∈ F.

## Cadena `001010`

- Inicio: {q6}; con cierre λ, {q6, q4, q0, q2, q7, q8}
- Lee `0`: {q6, q4, q0, q2, q7, q8} ⟶ {q4, q0, q1, q2, q5, q7, q8, q9, q10} [q0→q1, q8→q9]; cierre λ añade {q4, q0, q2, q5, q7, q8, q10}
- Lee `0`: {q4, q0, q1, q2, q5, q7, q8, q9, q10} ⟶ {q4, q0, q1, q2, q5, q7, q8, q9, q10, q11, q12} [q0→q1, q10→q11, q8→q9]; cierre λ añade {q4, q0, q2, q5, q7, q8, q10, q12}
- Lee `1`: {q4, q0, q1, q2, q5, q7, q8, q9, q10, q11, q12} ⟶ {q4, q0, q2, q3, q5, q7, q8, q13, q20, q18, q14, q16, q21} [q12→q13, q2→q3]; cierre λ añade {q4, q0, q2, q5, q7, q8, q20, q18, q14, q16, q21}
- Lee `0`: {q4, q0, q2, q3, q5, q7, q8, q13, q20, q18, q14, q16, q21} ⟶ {q4, q0, q1, q2, q5, q7, q8, q9, q10, q18, q14, q15, q16, q19, q21} [q0→q1, q14→q15, q8→q9]; cierre λ añade {q4, q0, q2, q5, q7, q8, q10, q18, q14, q16, q19, q21}
- Lee `1`: {q4, q0, q1, q2, q5, q7, q8, q9, q10, q18, q14, q15, q16, q19, q21} ⟶ {q4, q0, q2, q3, q5, q7, q8, q18, q14, q16, q17, q19, q21} [q16→q17, q2→q3]; cierre λ añade {q4, q0, q2, q5, q7, q8, q18, q14, q16, q19, q21}
- Lee `0`: {q4, q0, q2, q3, q5, q7, q8, q18, q14, q16, q17, q19, q21} ⟶ {q4, q0, q1, q2, q5, q7, q8, q9, q10, q18, q14, q15, q16, q19, q21} [q0→q1, q14→q15, q8→q9]; cierre λ añade {q4, q0, q2, q5, q7, q8, q10, q18, q14, q16, q19, q21}
- **Aceptada**: queda {q21} ∈ F.

## Cadena `00100001`

- Inicio: {q6}; con cierre λ, {q6, q4, q0, q2, q7, q8}
- Lee `0`: {q6, q4, q0, q2, q7, q8} ⟶ {q4, q0, q1, q2, q5, q7, q8, q9, q10} [q0→q1, q8→q9]; cierre λ añade {q4, q0, q2, q5, q7, q8, q10}
- Lee `0`: {q4, q0, q1, q2, q5, q7, q8, q9, q10} ⟶ {q4, q0, q1, q2, q5, q7, q8, q9, q10, q11, q12} [q0→q1, q10→q11, q8→q9]; cierre λ añade {q4, q0, q2, q5, q7, q8, q10, q12}
- Lee `1`: {q4, q0, q1, q2, q5, q7, q8, q9, q10, q11, q12} ⟶ {q4, q0, q2, q3, q5, q7, q8, q13, q20, q18, q14, q16, q21} [q12→q13, q2→q3]; cierre λ añade {q4, q0, q2, q5, q7, q8, q20, q18, q14, q16, q21}
- Lee `0`: {q4, q0, q2, q3, q5, q7, q8, q13, q20, q18, q14, q16, q21} ⟶ {q4, q0, q1, q2, q5, q7, q8, q9, q10, q18, q14, q15, q16, q19, q21} [q0→q1, q14→q15, q8→q9]; cierre λ añade {q4, q0, q2, q5, q7, q8, q10, q18, q14, q16, q19, q21}
- Lee `0`: {q4, q0, q1, q2, q5, q7, q8, q9, q10, q18, q14, q15, q16, q19, q21} ⟶ {q4, q0, q1, q2, q5, q7, q8, q9, q10, q11, q12, q18, q14, q15, q16, q19, q21} [q0→q1, q10→q11, q14→q15, q8→q9]; cierre λ añade {q4, q0, q2, q5, q7, q8, q10, q12, q18, q14, q16, q19, q21}
- Lee `0`: {q4, q0, q1, q2, q5, q7, q8, q9, q10, q11, q12, q18, q14, q15, q16, q19, q21} ⟶ {q4, q0, q1, q2, q5, q7, q8, q9, q10, q11, q12, q18, q14, q15, q16, q19, q21} [q0→q1, q10→q11, q14→q15, q8→q9]; cierre λ añade {q4, q0, q2, q5, q7, q8, q10, q12, q18, q14, q16, q19, q21}
- Lee `0`: {q4, q0, q1, q2, q5, q7, q8, q9, q10, q11, q12, q18, q14, q15, q16, q19, q21} ⟶ {q4, q0, q1, q2, q5, q7, q8, q9, q10, q11, q12, q18, q14, q15, q16, q19, q21} [q0→q1, q10→q11, q14→q15, q8→q9]; cierre λ añade {q4, q0, q2, q5, q7, q8, q10, q12, q18, q14, q16, q19, q21}
- Lee `1`: {q4, q0, q1, q2, q5, q7, q8, q9, q10, q11, q12, q18, q14, q15, q16, q19, q21} ⟶ {q4, q0, q2, q3, q5, q7, q8, q13, q20, q18, q14, q16, q17, q19, q21} [q12→q13, q16→q17, q2→q3]; cierre λ añade {q4, q0, q2, q5, q7, q8, q20, q18, q14, q16, q19, q21}
- **Aceptada**: queda {q21} ∈ F.

## Cadena `10010011110`

- Inicio: {q6}; con cierre λ, {q6, q4, q0, q2, q7, q8}
- Lee `1`: {q6, q4, q0, q2, q7, q8} ⟶ {q4, q0, q2, q3, q5, q7, q8} [q2→q3]; cierre λ añade {q4, q0, q2, q5, q7, q8}
- Lee `0`: {q4, q0, q2, q3, q5, q7, q8} ⟶ {q4, q0, q1, q2, q5, q7, q8, q9, q10} [q0→q1, q8→q9]; cierre λ añade {q4, q0, q2, q5, q7, q8, q10}
- Lee `0`: {q4, q0, q1, q2, q5, q7, q8, q9, q10} ⟶ {q4, q0, q1, q2, q5, q7, q8, q9, q10, q11, q12} [q0→q1, q10→q11, q8→q9]; cierre λ añade {q4, q0, q2, q5, q7, q8, q10, q12}
- Lee `1`: {q4, q0, q1, q2, q5, q7, q8, q9, q10, q11, q12} ⟶ {q4, q0, q2, q3, q5, q7, q8, q13, q20, q18, q14, q16, q21} [q12→q13, q2→q3]; cierre λ añade {q4, q0, q2, q5, q7, q8, q20, q18, q14, q16, q21}
- Lee `0`: {q4, q0, q2, q3, q5, q7, q8, q13, q20, q18, q14, q16, q21} ⟶ {q4, q0, q1, q2, q5, q7, q8, q9, q10, q18, q14, q15, q16, q19, q21} [q0→q1, q14→q15, q8→q9]; cierre λ añade {q4, q0, q2, q5, q7, q8, q10, q18, q14, q16, q19, q21}
- Lee `0`: {q4, q0, q1, q2, q5, q7, q8, q9, q10, q18, q14, q15, q16, q19, q21} ⟶ {q4, q0, q1, q2, q5, q7, q8, q9, q10, q11, q12, q18, q14, q15, q16, q19, q21} [q0→q1, q10→q11, q14→q15, q8→q9]; cierre λ añade {q4, q0, q2, q5, q7, q8, q10, q12, q18, q14, q16, q19, q21}
- Lee `1`: {q4, q0, q1, q2, q5, q7, q8, q9, q10, q11, q12, q18, q14, q15, q16, q19, q21} ⟶ {q4, q0, q2, q3, q5, q7, q8, q13, q20, q18, q14, q16, q17, q19, q21} [q12→q13, q16→q17, q2→q3]; cierre λ añade {q4, q0, q2, q5, q7, q8, q20, q18, q14, q16, q19, q21}
- Lee `1`: {q4, q0, q2, q3, q5, q7, q8, q13, q20, q18, q14, q16, q17, q19, q21} ⟶ {q4, q0, q2, q3, q5, q7, q8, q18, q14, q16, q17, q19, q21} [q16→q17, q2→q3]; cierre λ añade {q4, q0, q2, q5, q7, q8, q18, q14, q16, q19, q21}
- Lee `1`: {q4, q0, q2, q3, q5, q7, q8, q18, q14, q16, q17, q19, q21} ⟶ {q4, q0, q2, q3, q5, q7, q8, q18, q14, q16, q17, q19, q21} [q16→q17, q2→q3]; cierre λ añade {q4, q0, q2, q5, q7, q8, q18, q14, q16, q19, q21}
- Lee `1`: {q4, q0, q2, q3, q5, q7, q8, q18, q14, q16, q17, q19, q21} ⟶ {q4, q0, q2, q3, q5, q7, q8, q18, q14, q16, q17, q19, q21} [q16→q17, q2→q3]; cierre λ añade {q4, q0, q2, q5, q7, q8, q18, q14, q16, q19, q21}
- Lee `0`: {q4, q0, q2, q3, q5, q7, q8, q18, q14, q16, q17, q19, q21} ⟶ {q4, q0, q1, q2, q5, q7, q8, q9, q10, q18, q14, q15, q16, q19, q21} [q0→q1, q14→q15, q8→q9]; cierre λ añade {q4, q0, q2, q5, q7, q8, q10, q18, q14, q16, q19, q21}
- **Aceptada**: queda {q21} ∈ F.

## Cadena λ

- Inicio: {q6}; con cierre λ, {q6, q4, q0, q2, q7, q8}
- **Rechazada**: ningún estado de {q6, q4, q0, q2, q7, q8} es de aceptación.

## Cadena `0`

- Inicio: {q6}; con cierre λ, {q6, q4, q0, q2, q7, q8}
- Lee `0`: {q6, q4, q0, q2, q7, q8} ⟶ {q4, q0, q1, q2, q5, q7, q8, q9, q10} [q0→q1, q8→q9]; cierre λ añade {q4, q0, q2, q5, q7, q8, q10}
- **Rechazada**: ningún estado de {q4, q0, q1, q2, q5, q7, q8, q9, q10} es de aceptación.

## Cadena `100`

- Inicio: {q6}; con cierre λ, {q6, q4, q0, q2, q7, q8}
- Lee `1`: {q6, q4, q0, q2, q7, q8} ⟶ {q4, q0, q2, q3, q5, q7, q8} [q2→q3]; cierre λ añade {q4, q0, q2, q5, q7, q8}
- Lee `0`: {q4, q0, q2, q3, q5, q7, q8} ⟶ {q4, q0, q1, q2, q5, q7, q8, q9, q10} [q0→q1, q8→q9]; cierre λ añade {q4, q0, q2, q5, q7, q8, q10}
- Lee `0`: {q4, q0, q1, q2, q5, q7, q8, q9, q10} ⟶ {q4, q0, q1, q2, q5, q7, q8, q9, q10, q11, q12} [q0→q1, q10→q11, q8→q9]; cierre λ añade {q4, q0, q2, q5, q7, q8, q10, q12}
- **Rechazada**: ningún estado de {q4, q0, q1, q2, q5, q7, q8, q9, q10, q11, q12} es de aceptación.

## Cadena `01010`

- Inicio: {q6}; con cierre λ, {q6, q4, q0, q2, q7, q8}
- Lee `0`: {q6, q4, q0, q2, q7, q8} ⟶ {q4, q0, q1, q2, q5, q7, q8, q9, q10} [q0→q1, q8→q9]; cierre λ añade {q4, q0, q2, q5, q7, q8, q10}
- Lee `1`: {q4, q0, q1, q2, q5, q7, q8, q9, q10} ⟶ {q4, q0, q2, q3, q5, q7, q8} [q2→q3]; cierre λ añade {q4, q0, q2, q5, q7, q8}
- Lee `0`: {q4, q0, q2, q3, q5, q7, q8} ⟶ {q4, q0, q1, q2, q5, q7, q8, q9, q10} [q0→q1, q8→q9]; cierre λ añade {q4, q0, q2, q5, q7, q8, q10}
- Lee `1`: {q4, q0, q1, q2, q5, q7, q8, q9, q10} ⟶ {q4, q0, q2, q3, q5, q7, q8} [q2→q3]; cierre λ añade {q4, q0, q2, q5, q7, q8}
- Lee `0`: {q4, q0, q2, q3, q5, q7, q8} ⟶ {q4, q0, q1, q2, q5, q7, q8, q9, q10} [q0→q1, q8→q9]; cierre λ añade {q4, q0, q2, q5, q7, q8, q10}
- **Rechazada**: ningún estado de {q4, q0, q1, q2, q5, q7, q8, q9, q10} es de aceptación.

## Cadena `01000000`

- Inicio: {q6}; con cierre λ, {q6, q4, q0, q2, q7, q8}
- Lee `0`: {q6, q4, q0, q2, q7, q8} ⟶ {q4, q0, q1, q2, q5, q7, q8, q9, q10} [q0→q1, q8→q9]; cierre λ añade {q4, q0, q2, q5, q7, q8, q10}
- Lee `1`: {q4, q0, q1, q2, q5, q7, q8, q9, q10} ⟶ {q4, q0, q2, q3, q5, q7, q8} [q2→q3]; cierre λ añade {q4, q0, q2, q5, q7, q8}
- Lee `0`: {q4, q0, q2, q3, q5, q7, q8} ⟶ {q4, q0, q1, q2, q5, q7, q8, q9, q10} [q0→q1, q8→q9]; cierre λ añade {q4, q0, q2, q5, q7, q8, q10}
- Lee `0`: {q4, q0, q1, q2, q5, q7, q8, q9, q10} ⟶ {q4, q0, q1, q2, q5, q7, q8, q9, q10, q11, q12} [q0→q1, q10→q11, q8→q9]; cierre λ añade {q4, q0, q2, q5, q7, q8, q10, q12}
- Lee `0`: {q4, q0, q1, q2, q5, q7, q8, q9, q10, q11, q12} ⟶ {q4, q0, q1, q2, q5, q7, q8, q9, q10, q11, q12} [q0→q1, q10→q11, q8→q9]; cierre λ añade {q4, q0, q2, q5, q7, q8, q10, q12}
- Lee `0`: {q4, q0, q1, q2, q5, q7, q8, q9, q10, q11, q12} ⟶ {q4, q0, q1, q2, q5, q7, q8, q9, q10, q11, q12} [q0→q1, q10→q11, q8→q9]; cierre λ añade {q4, q0, q2, q5, q7, q8, q10, q12}
- Lee `0`: {q4, q0, q1, q2, q5, q7, q8, q9, q10, q11, q12} ⟶ {q4, q0, q1, q2, q5, q7, q8, q9, q10, q11, q12} [q0→q1, q10→q11, q8→q9]; cierre λ añade {q4, q0, q2, q5, q7, q8, q10, q12}
- Lee `0`: {q4, q0, q1, q2, q5, q7, q8, q9, q10, q11, q12} ⟶ {q4, q0, q1, q2, q5, q7, q8, q9, q10, q11, q12} [q0→q1, q10→q11, q8→q9]; cierre λ añade {q4, q0, q2, q5, q7, q8, q10, q12}
- **Rechazada**: ningún estado de {q4, q0, q1, q2, q5, q7, q8, q9, q10, q11, q12} es de aceptación.

## Cadena `00`

- Inicio: {q6}; con cierre λ, {q6, q4, q0, q2, q7, q8}
- Lee `0`: {q6, q4, q0, q2, q7, q8} ⟶ {q4, q0, q1, q2, q5, q7, q8, q9, q10} [q0→q1, q8→q9]; cierre λ añade {q4, q0, q2, q5, q7, q8, q10}
- Lee `0`: {q4, q0, q1, q2, q5, q7, q8, q9, q10} ⟶ {q4, q0, q1, q2, q5, q7, q8, q9, q10, q11, q12} [q0→q1, q10→q11, q8→q9]; cierre λ añade {q4, q0, q2, q5, q7, q8, q10, q12}
- **Rechazada**: ningún estado de {q4, q0, q1, q2, q5, q7, q8, q9, q10, q11, q12} es de aceptación.
