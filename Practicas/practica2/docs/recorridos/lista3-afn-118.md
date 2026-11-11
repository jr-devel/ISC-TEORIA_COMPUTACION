# Recorridos: Lista 3 · AFN del problema 118

AFN para el problema 118: L = {w ∈ Σ3* : w = axabya, x, y ∈ Σ3*}.

Autómata: `lista3-afn-118` (AFN).

## Cadena `aaba`

- Inicio: {q0}
- Lee `a`: {q0} ⟶ {q1} [q0→q1]
- Lee `a`: {q1} ⟶ {q1, q2} [q1→q1, q1→q2] (bifurcación)
- Lee `b`: {q1, q2} ⟶ {q1, q3} [q1→q1, q2→q3]
- Lee `a`: {q1, q3} ⟶ {q1, q2, q3, q4} [q1→q1, q1→q2, q3→q3, q3→q4] (bifurcación)
- **Aceptada**: queda {q4} ∈ F.

## Cadena `aabba`

- Inicio: {q0}
- Lee `a`: {q0} ⟶ {q1} [q0→q1]
- Lee `a`: {q1} ⟶ {q1, q2} [q1→q1, q1→q2] (bifurcación)
- Lee `b`: {q1, q2} ⟶ {q1, q3} [q1→q1, q2→q3]
- Lee `b`: {q1, q3} ⟶ {q1, q3} [q1→q1, q3→q3]
- Lee `a`: {q1, q3} ⟶ {q1, q2, q3, q4} [q1→q1, q1→q2, q3→q3, q3→q4] (bifurcación)
- **Aceptada**: queda {q4} ∈ F.

## Cadena `ababaaa`

- Inicio: {q0}
- Lee `a`: {q0} ⟶ {q1} [q0→q1]
- Lee `b`: {q1} ⟶ {q1} [q1→q1]
- Lee `a`: {q1} ⟶ {q1, q2} [q1→q1, q1→q2] (bifurcación)
- Lee `b`: {q1, q2} ⟶ {q1, q3} [q1→q1, q2→q3]
- Lee `a`: {q1, q3} ⟶ {q1, q2, q3, q4} [q1→q1, q1→q2, q3→q3, q3→q4] (bifurcación)
- Lee `a`: {q1, q2, q3, q4} ⟶ {q1, q2, q3, q4} [q1→q1, q1→q2, q3→q3, q3→q4]
- Lee `a`: {q1, q2, q3, q4} ⟶ {q1, q2, q3, q4} [q1→q1, q1→q2, q3→q3, q3→q4]
- **Aceptada**: queda {q4} ∈ F.

## Cadena `ababbbbaa`

- Inicio: {q0}
- Lee `a`: {q0} ⟶ {q1} [q0→q1]
- Lee `b`: {q1} ⟶ {q1} [q1→q1]
- Lee `a`: {q1} ⟶ {q1, q2} [q1→q1, q1→q2] (bifurcación)
- Lee `b`: {q1, q2} ⟶ {q1, q3} [q1→q1, q2→q3]
- Lee `b`: {q1, q3} ⟶ {q1, q3} [q1→q1, q3→q3]
- Lee `b`: {q1, q3} ⟶ {q1, q3} [q1→q1, q3→q3]
- Lee `b`: {q1, q3} ⟶ {q1, q3} [q1→q1, q3→q3]
- Lee `a`: {q1, q3} ⟶ {q1, q2, q3, q4} [q1→q1, q1→q2, q3→q3, q3→q4] (bifurcación)
- Lee `a`: {q1, q2, q3, q4} ⟶ {q1, q2, q3, q4} [q1→q1, q1→q2, q3→q3, q3→q4]
- **Aceptada**: queda {q4} ∈ F.

## Cadena `aababaaabaaa`

- Inicio: {q0}
- Lee `a`: {q0} ⟶ {q1} [q0→q1]
- Lee `a`: {q1} ⟶ {q1, q2} [q1→q1, q1→q2] (bifurcación)
- Lee `b`: {q1, q2} ⟶ {q1, q3} [q1→q1, q2→q3]
- Lee `a`: {q1, q3} ⟶ {q1, q2, q3, q4} [q1→q1, q1→q2, q3→q3, q3→q4] (bifurcación)
- Lee `b`: {q1, q2, q3, q4} ⟶ {q1, q3} [q1→q1, q2→q3, q3→q3]
- Lee `a`: {q1, q3} ⟶ {q1, q2, q3, q4} [q1→q1, q1→q2, q3→q3, q3→q4] (bifurcación)
- Lee `a`: {q1, q2, q3, q4} ⟶ {q1, q2, q3, q4} [q1→q1, q1→q2, q3→q3, q3→q4]
- Lee `a`: {q1, q2, q3, q4} ⟶ {q1, q2, q3, q4} [q1→q1, q1→q2, q3→q3, q3→q4]
- Lee `b`: {q1, q2, q3, q4} ⟶ {q1, q3} [q1→q1, q2→q3, q3→q3]
- Lee `a`: {q1, q3} ⟶ {q1, q2, q3, q4} [q1→q1, q1→q2, q3→q3, q3→q4] (bifurcación)
- Lee `a`: {q1, q2, q3, q4} ⟶ {q1, q2, q3, q4} [q1→q1, q1→q2, q3→q3, q3→q4]
- Lee `a`: {q1, q2, q3, q4} ⟶ {q1, q2, q3, q4} [q1→q1, q1→q2, q3→q3, q3→q4]
- **Aceptada**: queda {q4} ∈ F.

## Cadena λ

- Inicio: {q0}
- **Rechazada**: ningún estado de {q0} es de aceptación.

## Cadena `a`

- Inicio: {q0}
- Lee `a`: {q0} ⟶ {q1} [q0→q1]
- **Rechazada**: ningún estado de {q1} es de aceptación.

## Cadena `baa`

- Inicio: {q0}
- Lee `b`: {q0} ⟶ ∅ [ninguna transición]
- Lee `a`: ∅ ⟶ ∅ [ninguna transición]
- Lee `a`: ∅ ⟶ ∅ [ninguna transición]
- **Rechazada**: no queda ningún estado activo.

## Cadena `abbaa`

- Inicio: {q0}
- Lee `a`: {q0} ⟶ {q1} [q0→q1]
- Lee `b`: {q1} ⟶ {q1} [q1→q1]
- Lee `b`: {q1} ⟶ {q1} [q1→q1]
- Lee `a`: {q1} ⟶ {q1, q2} [q1→q1, q1→q2] (bifurcación)
- Lee `a`: {q1, q2} ⟶ {q1, q2} [q1→q1, q1→q2]
- **Rechazada**: ningún estado de {q1, q2} es de aceptación.

## Cadena `abaabbab`

- Inicio: {q0}
- Lee `a`: {q0} ⟶ {q1} [q0→q1]
- Lee `b`: {q1} ⟶ {q1} [q1→q1]
- Lee `a`: {q1} ⟶ {q1, q2} [q1→q1, q1→q2] (bifurcación)
- Lee `a`: {q1, q2} ⟶ {q1, q2} [q1→q1, q1→q2]
- Lee `b`: {q1, q2} ⟶ {q1, q3} [q1→q1, q2→q3]
- Lee `b`: {q1, q3} ⟶ {q1, q3} [q1→q1, q3→q3]
- Lee `a`: {q1, q3} ⟶ {q1, q2, q3, q4} [q1→q1, q1→q2, q3→q3, q3→q4] (bifurcación)
- Lee `b`: {q1, q2, q3, q4} ⟶ {q1, q3} [q1→q1, q2→q3, q3→q3]
- **Rechazada**: ningún estado de {q1, q3} es de aceptación.
