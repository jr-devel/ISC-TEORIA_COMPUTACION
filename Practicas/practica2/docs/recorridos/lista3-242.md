# Recorridos: Lista 3 · Ejercicio 242

AFN-λ equivalente a la expresión 0* + 1.

Autómata: `lista3-242` (AFN-λ).

## Cadena λ

- Inicio: {q6}; con cierre λ, {q6, q2, q0, q3, q4, q7}
- **Aceptada**: queda {q7} ∈ F.

## Cadena `1`

- Inicio: {q6}; con cierre λ, {q6, q2, q0, q3, q4, q7}
- Lee `1`: {q6, q2, q0, q3, q4, q7} ⟶ {q5, q7} [q4→q5]; cierre λ añade {q7}
- **Aceptada**: queda {q7} ∈ F.

## Cadena `000`

- Inicio: {q6}; con cierre λ, {q6, q2, q0, q3, q4, q7}
- Lee `0`: {q6, q2, q0, q3, q4, q7} ⟶ {q0, q1, q3, q7} [q0→q1]; cierre λ añade {q0, q3, q7}
- Lee `0`: {q0, q1, q3, q7} ⟶ {q0, q1, q3, q7} [q0→q1]; cierre λ añade {q0, q3, q7}
- Lee `0`: {q0, q1, q3, q7} ⟶ {q0, q1, q3, q7} [q0→q1]; cierre λ añade {q0, q3, q7}
- **Aceptada**: queda {q7} ∈ F.

## Cadena `00000`

- Inicio: {q6}; con cierre λ, {q6, q2, q0, q3, q4, q7}
- Lee `0`: {q6, q2, q0, q3, q4, q7} ⟶ {q0, q1, q3, q7} [q0→q1]; cierre λ añade {q0, q3, q7}
- Lee `0`: {q0, q1, q3, q7} ⟶ {q0, q1, q3, q7} [q0→q1]; cierre λ añade {q0, q3, q7}
- Lee `0`: {q0, q1, q3, q7} ⟶ {q0, q1, q3, q7} [q0→q1]; cierre λ añade {q0, q3, q7}
- Lee `0`: {q0, q1, q3, q7} ⟶ {q0, q1, q3, q7} [q0→q1]; cierre λ añade {q0, q3, q7}
- Lee `0`: {q0, q1, q3, q7} ⟶ {q0, q1, q3, q7} [q0→q1]; cierre λ añade {q0, q3, q7}
- **Aceptada**: queda {q7} ∈ F.

## Cadena `00000000`

- Inicio: {q6}; con cierre λ, {q6, q2, q0, q3, q4, q7}
- Lee `0`: {q6, q2, q0, q3, q4, q7} ⟶ {q0, q1, q3, q7} [q0→q1]; cierre λ añade {q0, q3, q7}
- Lee `0`: {q0, q1, q3, q7} ⟶ {q0, q1, q3, q7} [q0→q1]; cierre λ añade {q0, q3, q7}
- Lee `0`: {q0, q1, q3, q7} ⟶ {q0, q1, q3, q7} [q0→q1]; cierre λ añade {q0, q3, q7}
- Lee `0`: {q0, q1, q3, q7} ⟶ {q0, q1, q3, q7} [q0→q1]; cierre λ añade {q0, q3, q7}
- Lee `0`: {q0, q1, q3, q7} ⟶ {q0, q1, q3, q7} [q0→q1]; cierre λ añade {q0, q3, q7}
- Lee `0`: {q0, q1, q3, q7} ⟶ {q0, q1, q3, q7} [q0→q1]; cierre λ añade {q0, q3, q7}
- Lee `0`: {q0, q1, q3, q7} ⟶ {q0, q1, q3, q7} [q0→q1]; cierre λ añade {q0, q3, q7}
- Lee `0`: {q0, q1, q3, q7} ⟶ {q0, q1, q3, q7} [q0→q1]; cierre λ añade {q0, q3, q7}
- **Aceptada**: queda {q7} ∈ F.

## Cadena `10`

- Inicio: {q6}; con cierre λ, {q6, q2, q0, q3, q4, q7}
- Lee `1`: {q6, q2, q0, q3, q4, q7} ⟶ {q5, q7} [q4→q5]; cierre λ añade {q7}
- Lee `0`: {q5, q7} ⟶ ∅ [ninguna transición]
- **Rechazada**: no queda ningún estado activo.

## Cadena `011`

- Inicio: {q6}; con cierre λ, {q6, q2, q0, q3, q4, q7}
- Lee `0`: {q6, q2, q0, q3, q4, q7} ⟶ {q0, q1, q3, q7} [q0→q1]; cierre λ añade {q0, q3, q7}
- Lee `1`: {q0, q1, q3, q7} ⟶ ∅ [ninguna transición]
- Lee `1`: ∅ ⟶ ∅ [ninguna transición]
- **Rechazada**: no queda ningún estado activo.

## Cadena `10001`

- Inicio: {q6}; con cierre λ, {q6, q2, q0, q3, q4, q7}
- Lee `1`: {q6, q2, q0, q3, q4, q7} ⟶ {q5, q7} [q4→q5]; cierre λ añade {q7}
- Lee `0`: {q5, q7} ⟶ ∅ [ninguna transición]
- Lee `0`: ∅ ⟶ ∅ [ninguna transición]
- Lee `0`: ∅ ⟶ ∅ [ninguna transición]
- Lee `1`: ∅ ⟶ ∅ [ninguna transición]
- **Rechazada**: no queda ningún estado activo.

## Cadena `1011100`

- Inicio: {q6}; con cierre λ, {q6, q2, q0, q3, q4, q7}
- Lee `1`: {q6, q2, q0, q3, q4, q7} ⟶ {q5, q7} [q4→q5]; cierre λ añade {q7}
- Lee `0`: {q5, q7} ⟶ ∅ [ninguna transición]
- Lee `1`: ∅ ⟶ ∅ [ninguna transición]
- Lee `1`: ∅ ⟶ ∅ [ninguna transición]
- Lee `1`: ∅ ⟶ ∅ [ninguna transición]
- Lee `0`: ∅ ⟶ ∅ [ninguna transición]
- Lee `0`: ∅ ⟶ ∅ [ninguna transición]
- **Rechazada**: no queda ningún estado activo.

## Cadena `0110011100`

- Inicio: {q6}; con cierre λ, {q6, q2, q0, q3, q4, q7}
- Lee `0`: {q6, q2, q0, q3, q4, q7} ⟶ {q0, q1, q3, q7} [q0→q1]; cierre λ añade {q0, q3, q7}
- Lee `1`: {q0, q1, q3, q7} ⟶ ∅ [ninguna transición]
- Lee `1`: ∅ ⟶ ∅ [ninguna transición]
- Lee `0`: ∅ ⟶ ∅ [ninguna transición]
- Lee `0`: ∅ ⟶ ∅ [ninguna transición]
- Lee `1`: ∅ ⟶ ∅ [ninguna transición]
- Lee `1`: ∅ ⟶ ∅ [ninguna transición]
- Lee `1`: ∅ ⟶ ∅ [ninguna transición]
- Lee `0`: ∅ ⟶ ∅ [ninguna transición]
- Lee `0`: ∅ ⟶ ∅ [ninguna transición]
- **Rechazada**: no queda ningún estado activo.
