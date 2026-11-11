# Recorridos: Lista 3 · Ejercicio 248

AFN-λ equivalente a la expresión (0* + 1)0.

Autómata: `lista3-248` (AFN-λ).

## Cadena `0`

- Inicio: {q6}; con cierre λ, {q6, q2, q0, q3, q4, q7, q8}
- Lee `0`: {q6, q2, q0, q3, q4, q7, q8} ⟶ {q0, q1, q3, q7, q8, q9} [q0→q1, q8→q9]; cierre λ añade {q0, q3, q7, q8}
- **Aceptada**: queda {q9} ∈ F.

## Cadena `00`

- Inicio: {q6}; con cierre λ, {q6, q2, q0, q3, q4, q7, q8}
- Lee `0`: {q6, q2, q0, q3, q4, q7, q8} ⟶ {q0, q1, q3, q7, q8, q9} [q0→q1, q8→q9]; cierre λ añade {q0, q3, q7, q8}
- Lee `0`: {q0, q1, q3, q7, q8, q9} ⟶ {q0, q1, q3, q7, q8, q9} [q0→q1, q8→q9]; cierre λ añade {q0, q3, q7, q8}
- **Aceptada**: queda {q9} ∈ F.

## Cadena `0000`

- Inicio: {q6}; con cierre λ, {q6, q2, q0, q3, q4, q7, q8}
- Lee `0`: {q6, q2, q0, q3, q4, q7, q8} ⟶ {q0, q1, q3, q7, q8, q9} [q0→q1, q8→q9]; cierre λ añade {q0, q3, q7, q8}
- Lee `0`: {q0, q1, q3, q7, q8, q9} ⟶ {q0, q1, q3, q7, q8, q9} [q0→q1, q8→q9]; cierre λ añade {q0, q3, q7, q8}
- Lee `0`: {q0, q1, q3, q7, q8, q9} ⟶ {q0, q1, q3, q7, q8, q9} [q0→q1, q8→q9]; cierre λ añade {q0, q3, q7, q8}
- Lee `0`: {q0, q1, q3, q7, q8, q9} ⟶ {q0, q1, q3, q7, q8, q9} [q0→q1, q8→q9]; cierre λ añade {q0, q3, q7, q8}
- **Aceptada**: queda {q9} ∈ F.

## Cadena `000000`

- Inicio: {q6}; con cierre λ, {q6, q2, q0, q3, q4, q7, q8}
- Lee `0`: {q6, q2, q0, q3, q4, q7, q8} ⟶ {q0, q1, q3, q7, q8, q9} [q0→q1, q8→q9]; cierre λ añade {q0, q3, q7, q8}
- Lee `0`: {q0, q1, q3, q7, q8, q9} ⟶ {q0, q1, q3, q7, q8, q9} [q0→q1, q8→q9]; cierre λ añade {q0, q3, q7, q8}
- Lee `0`: {q0, q1, q3, q7, q8, q9} ⟶ {q0, q1, q3, q7, q8, q9} [q0→q1, q8→q9]; cierre λ añade {q0, q3, q7, q8}
- Lee `0`: {q0, q1, q3, q7, q8, q9} ⟶ {q0, q1, q3, q7, q8, q9} [q0→q1, q8→q9]; cierre λ añade {q0, q3, q7, q8}
- Lee `0`: {q0, q1, q3, q7, q8, q9} ⟶ {q0, q1, q3, q7, q8, q9} [q0→q1, q8→q9]; cierre λ añade {q0, q3, q7, q8}
- Lee `0`: {q0, q1, q3, q7, q8, q9} ⟶ {q0, q1, q3, q7, q8, q9} [q0→q1, q8→q9]; cierre λ añade {q0, q3, q7, q8}
- **Aceptada**: queda {q9} ∈ F.

## Cadena `000000000`

- Inicio: {q6}; con cierre λ, {q6, q2, q0, q3, q4, q7, q8}
- Lee `0`: {q6, q2, q0, q3, q4, q7, q8} ⟶ {q0, q1, q3, q7, q8, q9} [q0→q1, q8→q9]; cierre λ añade {q0, q3, q7, q8}
- Lee `0`: {q0, q1, q3, q7, q8, q9} ⟶ {q0, q1, q3, q7, q8, q9} [q0→q1, q8→q9]; cierre λ añade {q0, q3, q7, q8}
- Lee `0`: {q0, q1, q3, q7, q8, q9} ⟶ {q0, q1, q3, q7, q8, q9} [q0→q1, q8→q9]; cierre λ añade {q0, q3, q7, q8}
- Lee `0`: {q0, q1, q3, q7, q8, q9} ⟶ {q0, q1, q3, q7, q8, q9} [q0→q1, q8→q9]; cierre λ añade {q0, q3, q7, q8}
- Lee `0`: {q0, q1, q3, q7, q8, q9} ⟶ {q0, q1, q3, q7, q8, q9} [q0→q1, q8→q9]; cierre λ añade {q0, q3, q7, q8}
- Lee `0`: {q0, q1, q3, q7, q8, q9} ⟶ {q0, q1, q3, q7, q8, q9} [q0→q1, q8→q9]; cierre λ añade {q0, q3, q7, q8}
- Lee `0`: {q0, q1, q3, q7, q8, q9} ⟶ {q0, q1, q3, q7, q8, q9} [q0→q1, q8→q9]; cierre λ añade {q0, q3, q7, q8}
- Lee `0`: {q0, q1, q3, q7, q8, q9} ⟶ {q0, q1, q3, q7, q8, q9} [q0→q1, q8→q9]; cierre λ añade {q0, q3, q7, q8}
- Lee `0`: {q0, q1, q3, q7, q8, q9} ⟶ {q0, q1, q3, q7, q8, q9} [q0→q1, q8→q9]; cierre λ añade {q0, q3, q7, q8}
- **Aceptada**: queda {q9} ∈ F.

## Cadena λ

- Inicio: {q6}; con cierre λ, {q6, q2, q0, q3, q4, q7, q8}
- **Rechazada**: ningún estado de {q6, q2, q0, q3, q4, q7, q8} es de aceptación.

## Cadena `1`

- Inicio: {q6}; con cierre λ, {q6, q2, q0, q3, q4, q7, q8}
- Lee `1`: {q6, q2, q0, q3, q4, q7, q8} ⟶ {q5, q7, q8} [q4→q5]; cierre λ añade {q7, q8}
- **Rechazada**: ningún estado de {q5, q7, q8} es de aceptación.

## Cadena `110`

- Inicio: {q6}; con cierre λ, {q6, q2, q0, q3, q4, q7, q8}
- Lee `1`: {q6, q2, q0, q3, q4, q7, q8} ⟶ {q5, q7, q8} [q4→q5]; cierre λ añade {q7, q8}
- Lee `1`: {q5, q7, q8} ⟶ ∅ [ninguna transición]
- Lee `0`: ∅ ⟶ ∅ [ninguna transición]
- **Rechazada**: no queda ningún estado activo.

## Cadena `01011`

- Inicio: {q6}; con cierre λ, {q6, q2, q0, q3, q4, q7, q8}
- Lee `0`: {q6, q2, q0, q3, q4, q7, q8} ⟶ {q0, q1, q3, q7, q8, q9} [q0→q1, q8→q9]; cierre λ añade {q0, q3, q7, q8}
- Lee `1`: {q0, q1, q3, q7, q8, q9} ⟶ ∅ [ninguna transición]
- Lee `0`: ∅ ⟶ ∅ [ninguna transición]
- Lee `1`: ∅ ⟶ ∅ [ninguna transición]
- Lee `1`: ∅ ⟶ ∅ [ninguna transición]
- **Rechazada**: no queda ningún estado activo.

## Cadena `10010000`

- Inicio: {q6}; con cierre λ, {q6, q2, q0, q3, q4, q7, q8}
- Lee `1`: {q6, q2, q0, q3, q4, q7, q8} ⟶ {q5, q7, q8} [q4→q5]; cierre λ añade {q7, q8}
- Lee `0`: {q5, q7, q8} ⟶ {q9} [q8→q9]
- Lee `0`: {q9} ⟶ ∅ [ninguna transición]
- Lee `1`: ∅ ⟶ ∅ [ninguna transición]
- Lee `0`: ∅ ⟶ ∅ [ninguna transición]
- Lee `0`: ∅ ⟶ ∅ [ninguna transición]
- Lee `0`: ∅ ⟶ ∅ [ninguna transición]
- Lee `0`: ∅ ⟶ ∅ [ninguna transición]
- **Rechazada**: no queda ningún estado activo.
