# Recorridos: Lista 3 · Ejercicio 262

Diseñe un AFN que acepte {ab, ba} y obtenga un AFD.

Autómata: `lista3-262` (AFD).

## Cadena `ab`

- Inicio: {q0}
- Lee `a`: {q0} ⟶ {q1} [q0→q1]
- Lee `b`: {q1} ⟶ {q2} [q1→q2]
- **Aceptada**: queda {q2} ∈ F.

## Cadena `ba`

- Inicio: {q0}
- Lee `b`: {q0} ⟶ {q3} [q0→q3]
- Lee `a`: {q3} ⟶ {q4} [q3→q4]
- **Aceptada**: queda {q4} ∈ F.

## Cadena λ

- Inicio: {q0}
- **Rechazada**: ningún estado de {q0} es de aceptación.

## Cadena `a`

- Inicio: {q0}
- Lee `a`: {q0} ⟶ {q1} [q0→q1]
- **Rechazada**: ningún estado de {q1} es de aceptación.

## Cadena `bba`

- Inicio: {q0}
- Lee `b`: {q0} ⟶ {q3} [q0→q3]
- Lee `b`: {q3} ⟶ ∅ [ninguna transición]
- Lee `a`: ∅ ⟶ ∅ [ninguna transición]
- **Rechazada**: no queda ningún estado activo.

## Cadena `aaaba`

- Inicio: {q0}
- Lee `a`: {q0} ⟶ {q1} [q0→q1]
- Lee `a`: {q1} ⟶ ∅ [ninguna transición]
- Lee `a`: ∅ ⟶ ∅ [ninguna transición]
- Lee `b`: ∅ ⟶ ∅ [ninguna transición]
- Lee `a`: ∅ ⟶ ∅ [ninguna transición]
- **Rechazada**: no queda ningún estado activo.

## Cadena `babbaaaa`

- Inicio: {q0}
- Lee `b`: {q0} ⟶ {q3} [q0→q3]
- Lee `a`: {q3} ⟶ {q4} [q3→q4]
- Lee `b`: {q4} ⟶ ∅ [ninguna transición]
- Lee `b`: ∅ ⟶ ∅ [ninguna transición]
- Lee `a`: ∅ ⟶ ∅ [ninguna transición]
- Lee `a`: ∅ ⟶ ∅ [ninguna transición]
- Lee `a`: ∅ ⟶ ∅ [ninguna transición]
- Lee `a`: ∅ ⟶ ∅ [ninguna transición]
- **Rechazada**: no queda ningún estado activo.

## Cadena `b`

- Inicio: {q0}
- Lee `b`: {q0} ⟶ {q3} [q0→q3]
- **Rechazada**: ningún estado de {q3} es de aceptación.
