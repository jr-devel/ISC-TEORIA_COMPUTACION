# Recorridos: Lista 3 · Ejercicio 243

AFN-λ equivalente a la expresión (0 + 1)*.

Autómata: `lista3-243` (AFN-λ).

## Cadena λ

- Inicio: {q6}; con cierre λ, {q6, q4, q0, q2, q7}
- **Aceptada**: queda {q7} ∈ F.

## Cadena `0`

- Inicio: {q6}; con cierre λ, {q6, q4, q0, q2, q7}
- Lee `0`: {q6, q4, q0, q2, q7} ⟶ {q4, q0, q1, q2, q5, q7} [q0→q1]; cierre λ añade {q4, q0, q2, q5, q7}
- **Aceptada**: queda {q7} ∈ F.

## Cadena `001`

- Inicio: {q6}; con cierre λ, {q6, q4, q0, q2, q7}
- Lee `0`: {q6, q4, q0, q2, q7} ⟶ {q4, q0, q1, q2, q5, q7} [q0→q1]; cierre λ añade {q4, q0, q2, q5, q7}
- Lee `0`: {q4, q0, q1, q2, q5, q7} ⟶ {q4, q0, q1, q2, q5, q7} [q0→q1]; cierre λ añade {q4, q0, q2, q5, q7}
- Lee `1`: {q4, q0, q1, q2, q5, q7} ⟶ {q4, q0, q2, q3, q5, q7} [q2→q3]; cierre λ añade {q4, q0, q2, q5, q7}
- **Aceptada**: queda {q7} ∈ F.

## Cadena `11011`

- Inicio: {q6}; con cierre λ, {q6, q4, q0, q2, q7}
- Lee `1`: {q6, q4, q0, q2, q7} ⟶ {q4, q0, q2, q3, q5, q7} [q2→q3]; cierre λ añade {q4, q0, q2, q5, q7}
- Lee `1`: {q4, q0, q2, q3, q5, q7} ⟶ {q4, q0, q2, q3, q5, q7} [q2→q3]; cierre λ añade {q4, q0, q2, q5, q7}
- Lee `0`: {q4, q0, q2, q3, q5, q7} ⟶ {q4, q0, q1, q2, q5, q7} [q0→q1]; cierre λ añade {q4, q0, q2, q5, q7}
- Lee `1`: {q4, q0, q1, q2, q5, q7} ⟶ {q4, q0, q2, q3, q5, q7} [q2→q3]; cierre λ añade {q4, q0, q2, q5, q7}
- Lee `1`: {q4, q0, q2, q3, q5, q7} ⟶ {q4, q0, q2, q3, q5, q7} [q2→q3]; cierre λ añade {q4, q0, q2, q5, q7}
- **Aceptada**: queda {q7} ∈ F.

## Cadena `10010111`

- Inicio: {q6}; con cierre λ, {q6, q4, q0, q2, q7}
- Lee `1`: {q6, q4, q0, q2, q7} ⟶ {q4, q0, q2, q3, q5, q7} [q2→q3]; cierre λ añade {q4, q0, q2, q5, q7}
- Lee `0`: {q4, q0, q2, q3, q5, q7} ⟶ {q4, q0, q1, q2, q5, q7} [q0→q1]; cierre λ añade {q4, q0, q2, q5, q7}
- Lee `0`: {q4, q0, q1, q2, q5, q7} ⟶ {q4, q0, q1, q2, q5, q7} [q0→q1]; cierre λ añade {q4, q0, q2, q5, q7}
- Lee `1`: {q4, q0, q1, q2, q5, q7} ⟶ {q4, q0, q2, q3, q5, q7} [q2→q3]; cierre λ añade {q4, q0, q2, q5, q7}
- Lee `0`: {q4, q0, q2, q3, q5, q7} ⟶ {q4, q0, q1, q2, q5, q7} [q0→q1]; cierre λ añade {q4, q0, q2, q5, q7}
- Lee `1`: {q4, q0, q1, q2, q5, q7} ⟶ {q4, q0, q2, q3, q5, q7} [q2→q3]; cierre λ añade {q4, q0, q2, q5, q7}
- Lee `1`: {q4, q0, q2, q3, q5, q7} ⟶ {q4, q0, q2, q3, q5, q7} [q2→q3]; cierre λ añade {q4, q0, q2, q5, q7}
- Lee `1`: {q4, q0, q2, q3, q5, q7} ⟶ {q4, q0, q2, q3, q5, q7} [q2→q3]; cierre λ añade {q4, q0, q2, q5, q7}
- **Aceptada**: queda {q7} ∈ F.
