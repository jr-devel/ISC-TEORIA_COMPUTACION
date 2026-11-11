# Recorridos: Lista 3 · Ejercicio 241

AFN-λ equivalente a la expresión 0 + 1.

Autómata: `lista3-241` (AFN-λ).

## Cadena `0`

- Inicio: {q4}; con cierre λ, {q4, q0, q2}
- Lee `0`: {q4, q0, q2} ⟶ {q1, q5} [q0→q1]; cierre λ añade {q5}
- **Aceptada**: queda {q5} ∈ F.

## Cadena `1`

- Inicio: {q4}; con cierre λ, {q4, q0, q2}
- Lee `1`: {q4, q0, q2} ⟶ {q3, q5} [q2→q3]; cierre λ añade {q5}
- **Aceptada**: queda {q5} ∈ F.

## Cadena λ

- Inicio: {q4}; con cierre λ, {q4, q0, q2}
- **Rechazada**: ningún estado de {q4, q0, q2} es de aceptación.

## Cadena `100`

- Inicio: {q4}; con cierre λ, {q4, q0, q2}
- Lee `1`: {q4, q0, q2} ⟶ {q3, q5} [q2→q3]; cierre λ añade {q5}
- Lee `0`: {q3, q5} ⟶ ∅ [ninguna transición]
- Lee `0`: ∅ ⟶ ∅ [ninguna transición]
- **Rechazada**: no queda ningún estado activo.

## Cadena `000010`

- Inicio: {q4}; con cierre λ, {q4, q0, q2}
- Lee `0`: {q4, q0, q2} ⟶ {q1, q5} [q0→q1]; cierre λ añade {q5}
- Lee `0`: {q1, q5} ⟶ ∅ [ninguna transición]
- Lee `0`: ∅ ⟶ ∅ [ninguna transición]
- Lee `0`: ∅ ⟶ ∅ [ninguna transición]
- Lee `1`: ∅ ⟶ ∅ [ninguna transición]
- Lee `0`: ∅ ⟶ ∅ [ninguna transición]
- **Rechazada**: no queda ningún estado activo.

## Cadena `001010`

- Inicio: {q4}; con cierre λ, {q4, q0, q2}
- Lee `0`: {q4, q0, q2} ⟶ {q1, q5} [q0→q1]; cierre λ añade {q5}
- Lee `0`: {q1, q5} ⟶ ∅ [ninguna transición]
- Lee `1`: ∅ ⟶ ∅ [ninguna transición]
- Lee `0`: ∅ ⟶ ∅ [ninguna transición]
- Lee `1`: ∅ ⟶ ∅ [ninguna transición]
- Lee `0`: ∅ ⟶ ∅ [ninguna transición]
- **Rechazada**: no queda ningún estado activo.

## Cadena `110110`

- Inicio: {q4}; con cierre λ, {q4, q0, q2}
- Lee `1`: {q4, q0, q2} ⟶ {q3, q5} [q2→q3]; cierre λ añade {q5}
- Lee `1`: {q3, q5} ⟶ ∅ [ninguna transición]
- Lee `0`: ∅ ⟶ ∅ [ninguna transición]
- Lee `1`: ∅ ⟶ ∅ [ninguna transición]
- Lee `1`: ∅ ⟶ ∅ [ninguna transición]
- Lee `0`: ∅ ⟶ ∅ [ninguna transición]
- **Rechazada**: no queda ningún estado activo.
