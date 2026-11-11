# Recorridos: Lista 3 · Ejercicio 247

AFN-λ equivalente a la expresión (01)* + 1*.

Autómata: `lista3-247` (AFN-λ).

## Cadena λ

- Inicio: {q10}; con cierre λ, {q10, q4, q0, q5, q8, q6, q9, q11}
- **Aceptada**: queda {q11} ∈ F.

## Cadena `1`

- Inicio: {q10}; con cierre λ, {q10, q4, q0, q5, q8, q6, q9, q11}
- Lee `1`: {q10, q4, q0, q5, q8, q6, q9, q11} ⟶ {q6, q7, q9, q11} [q6→q7]; cierre λ añade {q6, q9, q11}
- **Aceptada**: queda {q11} ∈ F.

## Cadena `111`

- Inicio: {q10}; con cierre λ, {q10, q4, q0, q5, q8, q6, q9, q11}
- Lee `1`: {q10, q4, q0, q5, q8, q6, q9, q11} ⟶ {q6, q7, q9, q11} [q6→q7]; cierre λ añade {q6, q9, q11}
- Lee `1`: {q6, q7, q9, q11} ⟶ {q6, q7, q9, q11} [q6→q7]; cierre λ añade {q6, q9, q11}
- Lee `1`: {q6, q7, q9, q11} ⟶ {q6, q7, q9, q11} [q6→q7]; cierre λ añade {q6, q9, q11}
- **Aceptada**: queda {q11} ∈ F.

## Cadena `11111`

- Inicio: {q10}; con cierre λ, {q10, q4, q0, q5, q8, q6, q9, q11}
- Lee `1`: {q10, q4, q0, q5, q8, q6, q9, q11} ⟶ {q6, q7, q9, q11} [q6→q7]; cierre λ añade {q6, q9, q11}
- Lee `1`: {q6, q7, q9, q11} ⟶ {q6, q7, q9, q11} [q6→q7]; cierre λ añade {q6, q9, q11}
- Lee `1`: {q6, q7, q9, q11} ⟶ {q6, q7, q9, q11} [q6→q7]; cierre λ añade {q6, q9, q11}
- Lee `1`: {q6, q7, q9, q11} ⟶ {q6, q7, q9, q11} [q6→q7]; cierre λ añade {q6, q9, q11}
- Lee `1`: {q6, q7, q9, q11} ⟶ {q6, q7, q9, q11} [q6→q7]; cierre λ añade {q6, q9, q11}
- **Aceptada**: queda {q11} ∈ F.

## Cadena `01010101`

- Inicio: {q10}; con cierre λ, {q10, q4, q0, q5, q8, q6, q9, q11}
- Lee `0`: {q10, q4, q0, q5, q8, q6, q9, q11} ⟶ {q1, q2} [q0→q1]; cierre λ añade {q2}
- Lee `1`: {q1, q2} ⟶ {q0, q3, q5, q11} [q2→q3]; cierre λ añade {q0, q5, q11}
- Lee `0`: {q0, q3, q5, q11} ⟶ {q1, q2} [q0→q1]; cierre λ añade {q2}
- Lee `1`: {q1, q2} ⟶ {q0, q3, q5, q11} [q2→q3]; cierre λ añade {q0, q5, q11}
- Lee `0`: {q0, q3, q5, q11} ⟶ {q1, q2} [q0→q1]; cierre λ añade {q2}
- Lee `1`: {q1, q2} ⟶ {q0, q3, q5, q11} [q2→q3]; cierre λ añade {q0, q5, q11}
- Lee `0`: {q0, q3, q5, q11} ⟶ {q1, q2} [q0→q1]; cierre λ añade {q2}
- Lee `1`: {q1, q2} ⟶ {q0, q3, q5, q11} [q2→q3]; cierre λ añade {q0, q5, q11}
- **Aceptada**: queda {q11} ∈ F.

## Cadena `0`

- Inicio: {q10}; con cierre λ, {q10, q4, q0, q5, q8, q6, q9, q11}
- Lee `0`: {q10, q4, q0, q5, q8, q6, q9, q11} ⟶ {q1, q2} [q0→q1]; cierre λ añade {q2}
- **Rechazada**: ningún estado de {q1, q2} es de aceptación.

## Cadena `00`

- Inicio: {q10}; con cierre λ, {q10, q4, q0, q5, q8, q6, q9, q11}
- Lee `0`: {q10, q4, q0, q5, q8, q6, q9, q11} ⟶ {q1, q2} [q0→q1]; cierre λ añade {q2}
- Lee `0`: {q1, q2} ⟶ ∅ [ninguna transición]
- **Rechazada**: no queda ningún estado activo.

## Cadena `0000`

- Inicio: {q10}; con cierre λ, {q10, q4, q0, q5, q8, q6, q9, q11}
- Lee `0`: {q10, q4, q0, q5, q8, q6, q9, q11} ⟶ {q1, q2} [q0→q1]; cierre λ añade {q2}
- Lee `0`: {q1, q2} ⟶ ∅ [ninguna transición]
- Lee `0`: ∅ ⟶ ∅ [ninguna transición]
- Lee `0`: ∅ ⟶ ∅ [ninguna transición]
- **Rechazada**: no queda ningún estado activo.

## Cadena `101001`

- Inicio: {q10}; con cierre λ, {q10, q4, q0, q5, q8, q6, q9, q11}
- Lee `1`: {q10, q4, q0, q5, q8, q6, q9, q11} ⟶ {q6, q7, q9, q11} [q6→q7]; cierre λ añade {q6, q9, q11}
- Lee `0`: {q6, q7, q9, q11} ⟶ ∅ [ninguna transición]
- Lee `1`: ∅ ⟶ ∅ [ninguna transición]
- Lee `0`: ∅ ⟶ ∅ [ninguna transición]
- Lee `0`: ∅ ⟶ ∅ [ninguna transición]
- Lee `1`: ∅ ⟶ ∅ [ninguna transición]
- **Rechazada**: no queda ningún estado activo.

## Cadena `110001011`

- Inicio: {q10}; con cierre λ, {q10, q4, q0, q5, q8, q6, q9, q11}
- Lee `1`: {q10, q4, q0, q5, q8, q6, q9, q11} ⟶ {q6, q7, q9, q11} [q6→q7]; cierre λ añade {q6, q9, q11}
- Lee `1`: {q6, q7, q9, q11} ⟶ {q6, q7, q9, q11} [q6→q7]; cierre λ añade {q6, q9, q11}
- Lee `0`: {q6, q7, q9, q11} ⟶ ∅ [ninguna transición]
- Lee `0`: ∅ ⟶ ∅ [ninguna transición]
- Lee `0`: ∅ ⟶ ∅ [ninguna transición]
- Lee `1`: ∅ ⟶ ∅ [ninguna transición]
- Lee `0`: ∅ ⟶ ∅ [ninguna transición]
- Lee `1`: ∅ ⟶ ∅ [ninguna transición]
- Lee `1`: ∅ ⟶ ∅ [ninguna transición]
- **Rechazada**: no queda ningún estado activo.
