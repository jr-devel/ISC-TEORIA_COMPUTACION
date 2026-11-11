# Recorridos: Lista 3 · Ejercicio 244

AFN-λ equivalente a la expresión 0(0 + 1).

Autómata: `lista3-244` (AFN-λ).

## Cadena `00`

- Inicio: {q0}
- Lee `0`: {q0} ⟶ {q1, q6, q2, q4} [q0→q1]; cierre λ añade {q6, q2, q4}
- Lee `0`: {q1, q6, q2, q4} ⟶ {q3, q7} [q2→q3]; cierre λ añade {q7}
- **Aceptada**: queda {q7} ∈ F.

## Cadena `01`

- Inicio: {q0}
- Lee `0`: {q0} ⟶ {q1, q6, q2, q4} [q0→q1]; cierre λ añade {q6, q2, q4}
- Lee `1`: {q1, q6, q2, q4} ⟶ {q5, q7} [q4→q5]; cierre λ añade {q7}
- **Aceptada**: queda {q7} ∈ F.

## Cadena λ

- Inicio: {q0}
- **Rechazada**: ningún estado de {q0} es de aceptación.

## Cadena `1`

- Inicio: {q0}
- Lee `1`: {q0} ⟶ ∅ [ninguna transición]
- **Rechazada**: no queda ningún estado activo.

## Cadena `100`

- Inicio: {q0}
- Lee `1`: {q0} ⟶ ∅ [ninguna transición]
- Lee `0`: ∅ ⟶ ∅ [ninguna transición]
- Lee `0`: ∅ ⟶ ∅ [ninguna transición]
- **Rechazada**: no queda ningún estado activo.

## Cadena `11010`

- Inicio: {q0}
- Lee `1`: {q0} ⟶ ∅ [ninguna transición]
- Lee `1`: ∅ ⟶ ∅ [ninguna transición]
- Lee `0`: ∅ ⟶ ∅ [ninguna transición]
- Lee `1`: ∅ ⟶ ∅ [ninguna transición]
- Lee `0`: ∅ ⟶ ∅ [ninguna transición]
- **Rechazada**: no queda ningún estado activo.

## Cadena `01110100`

- Inicio: {q0}
- Lee `0`: {q0} ⟶ {q1, q6, q2, q4} [q0→q1]; cierre λ añade {q6, q2, q4}
- Lee `1`: {q1, q6, q2, q4} ⟶ {q5, q7} [q4→q5]; cierre λ añade {q7}
- Lee `1`: {q5, q7} ⟶ ∅ [ninguna transición]
- Lee `1`: ∅ ⟶ ∅ [ninguna transición]
- Lee `0`: ∅ ⟶ ∅ [ninguna transición]
- Lee `1`: ∅ ⟶ ∅ [ninguna transición]
- Lee `0`: ∅ ⟶ ∅ [ninguna transición]
- Lee `0`: ∅ ⟶ ∅ [ninguna transición]
- **Rechazada**: no queda ningún estado activo.
