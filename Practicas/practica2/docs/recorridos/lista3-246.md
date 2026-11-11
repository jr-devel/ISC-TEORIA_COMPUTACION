# Recorridos: Lista 3 · Ejercicio 246

AFN-λ equivalente a la expresión 0*(0 + 1).

Autómata: `lista3-246` (AFN-λ).

## Cadena `1`

- Inicio: {q2}; con cierre λ, {q2, q0, q3, q8, q4, q6}
- Lee `1`: {q2, q0, q3, q8, q4, q6} ⟶ {q7, q9} [q6→q7]; cierre λ añade {q9}
- **Aceptada**: queda {q9} ∈ F.

## Cadena `00`

- Inicio: {q2}; con cierre λ, {q2, q0, q3, q8, q4, q6}
- Lee `0`: {q2, q0, q3, q8, q4, q6} ⟶ {q0, q1, q3, q8, q4, q5, q6, q9} [q0→q1, q4→q5]; cierre λ añade {q0, q3, q8, q4, q6, q9}
- Lee `0`: {q0, q1, q3, q8, q4, q5, q6, q9} ⟶ {q0, q1, q3, q8, q4, q5, q6, q9} [q0→q1, q4→q5]; cierre λ añade {q0, q3, q8, q4, q6, q9}
- **Aceptada**: queda {q9} ∈ F.

## Cadena `0000`

- Inicio: {q2}; con cierre λ, {q2, q0, q3, q8, q4, q6}
- Lee `0`: {q2, q0, q3, q8, q4, q6} ⟶ {q0, q1, q3, q8, q4, q5, q6, q9} [q0→q1, q4→q5]; cierre λ añade {q0, q3, q8, q4, q6, q9}
- Lee `0`: {q0, q1, q3, q8, q4, q5, q6, q9} ⟶ {q0, q1, q3, q8, q4, q5, q6, q9} [q0→q1, q4→q5]; cierre λ añade {q0, q3, q8, q4, q6, q9}
- Lee `0`: {q0, q1, q3, q8, q4, q5, q6, q9} ⟶ {q0, q1, q3, q8, q4, q5, q6, q9} [q0→q1, q4→q5]; cierre λ añade {q0, q3, q8, q4, q6, q9}
- Lee `0`: {q0, q1, q3, q8, q4, q5, q6, q9} ⟶ {q0, q1, q3, q8, q4, q5, q6, q9} [q0→q1, q4→q5]; cierre λ añade {q0, q3, q8, q4, q6, q9}
- **Aceptada**: queda {q9} ∈ F.

## Cadena `000000`

- Inicio: {q2}; con cierre λ, {q2, q0, q3, q8, q4, q6}
- Lee `0`: {q2, q0, q3, q8, q4, q6} ⟶ {q0, q1, q3, q8, q4, q5, q6, q9} [q0→q1, q4→q5]; cierre λ añade {q0, q3, q8, q4, q6, q9}
- Lee `0`: {q0, q1, q3, q8, q4, q5, q6, q9} ⟶ {q0, q1, q3, q8, q4, q5, q6, q9} [q0→q1, q4→q5]; cierre λ añade {q0, q3, q8, q4, q6, q9}
- Lee `0`: {q0, q1, q3, q8, q4, q5, q6, q9} ⟶ {q0, q1, q3, q8, q4, q5, q6, q9} [q0→q1, q4→q5]; cierre λ añade {q0, q3, q8, q4, q6, q9}
- Lee `0`: {q0, q1, q3, q8, q4, q5, q6, q9} ⟶ {q0, q1, q3, q8, q4, q5, q6, q9} [q0→q1, q4→q5]; cierre λ añade {q0, q3, q8, q4, q6, q9}
- Lee `0`: {q0, q1, q3, q8, q4, q5, q6, q9} ⟶ {q0, q1, q3, q8, q4, q5, q6, q9} [q0→q1, q4→q5]; cierre λ añade {q0, q3, q8, q4, q6, q9}
- Lee `0`: {q0, q1, q3, q8, q4, q5, q6, q9} ⟶ {q0, q1, q3, q8, q4, q5, q6, q9} [q0→q1, q4→q5]; cierre λ añade {q0, q3, q8, q4, q6, q9}
- **Aceptada**: queda {q9} ∈ F.

## Cadena `000000000`

- Inicio: {q2}; con cierre λ, {q2, q0, q3, q8, q4, q6}
- Lee `0`: {q2, q0, q3, q8, q4, q6} ⟶ {q0, q1, q3, q8, q4, q5, q6, q9} [q0→q1, q4→q5]; cierre λ añade {q0, q3, q8, q4, q6, q9}
- Lee `0`: {q0, q1, q3, q8, q4, q5, q6, q9} ⟶ {q0, q1, q3, q8, q4, q5, q6, q9} [q0→q1, q4→q5]; cierre λ añade {q0, q3, q8, q4, q6, q9}
- Lee `0`: {q0, q1, q3, q8, q4, q5, q6, q9} ⟶ {q0, q1, q3, q8, q4, q5, q6, q9} [q0→q1, q4→q5]; cierre λ añade {q0, q3, q8, q4, q6, q9}
- Lee `0`: {q0, q1, q3, q8, q4, q5, q6, q9} ⟶ {q0, q1, q3, q8, q4, q5, q6, q9} [q0→q1, q4→q5]; cierre λ añade {q0, q3, q8, q4, q6, q9}
- Lee `0`: {q0, q1, q3, q8, q4, q5, q6, q9} ⟶ {q0, q1, q3, q8, q4, q5, q6, q9} [q0→q1, q4→q5]; cierre λ añade {q0, q3, q8, q4, q6, q9}
- Lee `0`: {q0, q1, q3, q8, q4, q5, q6, q9} ⟶ {q0, q1, q3, q8, q4, q5, q6, q9} [q0→q1, q4→q5]; cierre λ añade {q0, q3, q8, q4, q6, q9}
- Lee `0`: {q0, q1, q3, q8, q4, q5, q6, q9} ⟶ {q0, q1, q3, q8, q4, q5, q6, q9} [q0→q1, q4→q5]; cierre λ añade {q0, q3, q8, q4, q6, q9}
- Lee `0`: {q0, q1, q3, q8, q4, q5, q6, q9} ⟶ {q0, q1, q3, q8, q4, q5, q6, q9} [q0→q1, q4→q5]; cierre λ añade {q0, q3, q8, q4, q6, q9}
- Lee `0`: {q0, q1, q3, q8, q4, q5, q6, q9} ⟶ {q0, q1, q3, q8, q4, q5, q6, q9} [q0→q1, q4→q5]; cierre λ añade {q0, q3, q8, q4, q6, q9}
- **Aceptada**: queda {q9} ∈ F.

## Cadena λ

- Inicio: {q2}; con cierre λ, {q2, q0, q3, q8, q4, q6}
- **Rechazada**: ningún estado de {q2, q0, q3, q8, q4, q6} es de aceptación.

## Cadena `0000011`

- Inicio: {q2}; con cierre λ, {q2, q0, q3, q8, q4, q6}
- Lee `0`: {q2, q0, q3, q8, q4, q6} ⟶ {q0, q1, q3, q8, q4, q5, q6, q9} [q0→q1, q4→q5]; cierre λ añade {q0, q3, q8, q4, q6, q9}
- Lee `0`: {q0, q1, q3, q8, q4, q5, q6, q9} ⟶ {q0, q1, q3, q8, q4, q5, q6, q9} [q0→q1, q4→q5]; cierre λ añade {q0, q3, q8, q4, q6, q9}
- Lee `0`: {q0, q1, q3, q8, q4, q5, q6, q9} ⟶ {q0, q1, q3, q8, q4, q5, q6, q9} [q0→q1, q4→q5]; cierre λ añade {q0, q3, q8, q4, q6, q9}
- Lee `0`: {q0, q1, q3, q8, q4, q5, q6, q9} ⟶ {q0, q1, q3, q8, q4, q5, q6, q9} [q0→q1, q4→q5]; cierre λ añade {q0, q3, q8, q4, q6, q9}
- Lee `0`: {q0, q1, q3, q8, q4, q5, q6, q9} ⟶ {q0, q1, q3, q8, q4, q5, q6, q9} [q0→q1, q4→q5]; cierre λ añade {q0, q3, q8, q4, q6, q9}
- Lee `1`: {q0, q1, q3, q8, q4, q5, q6, q9} ⟶ {q7, q9} [q6→q7]; cierre λ añade {q9}
- Lee `1`: {q7, q9} ⟶ ∅ [ninguna transición]
- **Rechazada**: no queda ningún estado activo.

## Cadena `0000100`

- Inicio: {q2}; con cierre λ, {q2, q0, q3, q8, q4, q6}
- Lee `0`: {q2, q0, q3, q8, q4, q6} ⟶ {q0, q1, q3, q8, q4, q5, q6, q9} [q0→q1, q4→q5]; cierre λ añade {q0, q3, q8, q4, q6, q9}
- Lee `0`: {q0, q1, q3, q8, q4, q5, q6, q9} ⟶ {q0, q1, q3, q8, q4, q5, q6, q9} [q0→q1, q4→q5]; cierre λ añade {q0, q3, q8, q4, q6, q9}
- Lee `0`: {q0, q1, q3, q8, q4, q5, q6, q9} ⟶ {q0, q1, q3, q8, q4, q5, q6, q9} [q0→q1, q4→q5]; cierre λ añade {q0, q3, q8, q4, q6, q9}
- Lee `0`: {q0, q1, q3, q8, q4, q5, q6, q9} ⟶ {q0, q1, q3, q8, q4, q5, q6, q9} [q0→q1, q4→q5]; cierre λ añade {q0, q3, q8, q4, q6, q9}
- Lee `1`: {q0, q1, q3, q8, q4, q5, q6, q9} ⟶ {q7, q9} [q6→q7]; cierre λ añade {q9}
- Lee `0`: {q7, q9} ⟶ ∅ [ninguna transición]
- Lee `0`: ∅ ⟶ ∅ [ninguna transición]
- **Rechazada**: no queda ningún estado activo.

## Cadena `1110010101`

- Inicio: {q2}; con cierre λ, {q2, q0, q3, q8, q4, q6}
- Lee `1`: {q2, q0, q3, q8, q4, q6} ⟶ {q7, q9} [q6→q7]; cierre λ añade {q9}
- Lee `1`: {q7, q9} ⟶ ∅ [ninguna transición]
- Lee `1`: ∅ ⟶ ∅ [ninguna transición]
- Lee `0`: ∅ ⟶ ∅ [ninguna transición]
- Lee `0`: ∅ ⟶ ∅ [ninguna transición]
- Lee `1`: ∅ ⟶ ∅ [ninguna transición]
- Lee `0`: ∅ ⟶ ∅ [ninguna transición]
- Lee `1`: ∅ ⟶ ∅ [ninguna transición]
- Lee `0`: ∅ ⟶ ∅ [ninguna transición]
- Lee `1`: ∅ ⟶ ∅ [ninguna transición]
- **Rechazada**: no queda ningún estado activo.

## Cadena `01010111101`

- Inicio: {q2}; con cierre λ, {q2, q0, q3, q8, q4, q6}
- Lee `0`: {q2, q0, q3, q8, q4, q6} ⟶ {q0, q1, q3, q8, q4, q5, q6, q9} [q0→q1, q4→q5]; cierre λ añade {q0, q3, q8, q4, q6, q9}
- Lee `1`: {q0, q1, q3, q8, q4, q5, q6, q9} ⟶ {q7, q9} [q6→q7]; cierre λ añade {q9}
- Lee `0`: {q7, q9} ⟶ ∅ [ninguna transición]
- Lee `1`: ∅ ⟶ ∅ [ninguna transición]
- Lee `0`: ∅ ⟶ ∅ [ninguna transición]
- Lee `1`: ∅ ⟶ ∅ [ninguna transición]
- Lee `1`: ∅ ⟶ ∅ [ninguna transición]
- Lee `1`: ∅ ⟶ ∅ [ninguna transición]
- Lee `1`: ∅ ⟶ ∅ [ninguna transición]
- Lee `0`: ∅ ⟶ ∅ [ninguna transición]
- Lee `1`: ∅ ⟶ ∅ [ninguna transición]
- **Rechazada**: no queda ningún estado activo.

## Cadena `0`

- Inicio: {q2}; con cierre λ, {q2, q0, q3, q8, q4, q6}
- Lee `0`: {q2, q0, q3, q8, q4, q6} ⟶ {q0, q1, q3, q8, q4, q5, q6, q9} [q0→q1, q4→q5]; cierre λ añade {q0, q3, q8, q4, q6, q9}
- **Aceptada**: queda {q9} ∈ F.
