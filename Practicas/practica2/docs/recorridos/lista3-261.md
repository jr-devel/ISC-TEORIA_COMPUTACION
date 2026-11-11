# Recorridos: Lista 3 · Ejercicio 261

AFD equivalente al AFN de la figura 261 (transcrito).

Autómata: `lista3-261` (AFN).

## Cadena `00`

- Inicio: {q0}
- Lee `0`: {q0} ⟶ {q0, q1} [q0→q0, q0→q1] (bifurcación)
- Lee `0`: {q0, q1} ⟶ {q0, q1, q2} [q0→q0, q0→q1, q1→q2] (bifurcación)
- **Aceptada**: queda {q2} ∈ F.

## Cadena `000`

- Inicio: {q0}
- Lee `0`: {q0} ⟶ {q0, q1} [q0→q0, q0→q1] (bifurcación)
- Lee `0`: {q0, q1} ⟶ {q0, q1, q2} [q0→q0, q0→q1, q1→q2] (bifurcación)
- Lee `0`: {q0, q1, q2} ⟶ {q0, q1, q2} [q0→q0, q0→q1, q1→q2]
- **Aceptada**: queda {q2} ∈ F.

## Cadena `01000`

- Inicio: {q0}
- Lee `0`: {q0} ⟶ {q0, q1} [q0→q0, q0→q1] (bifurcación)
- Lee `1`: {q0, q1} ⟶ {q0, q3} [q0→q0, q0→q3]
- Lee `0`: {q0, q3} ⟶ {q0, q1} [q0→q0, q0→q1]
- Lee `0`: {q0, q1} ⟶ {q0, q1, q2} [q0→q0, q0→q1, q1→q2] (bifurcación)
- Lee `0`: {q0, q1, q2} ⟶ {q0, q1, q2} [q0→q0, q0→q1, q1→q2]
- **Aceptada**: queda {q2} ∈ F.

## Cadena `1010000`

- Inicio: {q0}
- Lee `1`: {q0} ⟶ {q0, q3} [q0→q0, q0→q3] (bifurcación)
- Lee `0`: {q0, q3} ⟶ {q0, q1} [q0→q0, q0→q1]
- Lee `1`: {q0, q1} ⟶ {q0, q3} [q0→q0, q0→q3]
- Lee `0`: {q0, q3} ⟶ {q0, q1} [q0→q0, q0→q1]
- Lee `0`: {q0, q1} ⟶ {q0, q1, q2} [q0→q0, q0→q1, q1→q2] (bifurcación)
- Lee `0`: {q0, q1, q2} ⟶ {q0, q1, q2} [q0→q0, q0→q1, q1→q2]
- Lee `0`: {q0, q1, q2} ⟶ {q0, q1, q2} [q0→q0, q0→q1, q1→q2]
- **Aceptada**: queda {q2} ∈ F.

## Cadena `0010100100`

- Inicio: {q0}
- Lee `0`: {q0} ⟶ {q0, q1} [q0→q0, q0→q1] (bifurcación)
- Lee `0`: {q0, q1} ⟶ {q0, q1, q2} [q0→q0, q0→q1, q1→q2] (bifurcación)
- Lee `1`: {q0, q1, q2} ⟶ {q0, q3} [q0→q0, q0→q3]
- Lee `0`: {q0, q3} ⟶ {q0, q1} [q0→q0, q0→q1]
- Lee `1`: {q0, q1} ⟶ {q0, q3} [q0→q0, q0→q3]
- Lee `0`: {q0, q3} ⟶ {q0, q1} [q0→q0, q0→q1]
- Lee `0`: {q0, q1} ⟶ {q0, q1, q2} [q0→q0, q0→q1, q1→q2] (bifurcación)
- Lee `1`: {q0, q1, q2} ⟶ {q0, q3} [q0→q0, q0→q3]
- Lee `0`: {q0, q3} ⟶ {q0, q1} [q0→q0, q0→q1]
- Lee `0`: {q0, q1} ⟶ {q0, q1, q2} [q0→q0, q0→q1, q1→q2] (bifurcación)
- **Aceptada**: queda {q2} ∈ F.

## Cadena λ

- Inicio: {q0}
- **Rechazada**: ningún estado de {q0} es de aceptación.

## Cadena `0`

- Inicio: {q0}
- Lee `0`: {q0} ⟶ {q0, q1} [q0→q0, q0→q1] (bifurcación)
- **Rechazada**: ningún estado de {q0, q1} es de aceptación.

## Cadena `010`

- Inicio: {q0}
- Lee `0`: {q0} ⟶ {q0, q1} [q0→q0, q0→q1] (bifurcación)
- Lee `1`: {q0, q1} ⟶ {q0, q3} [q0→q0, q0→q3]
- Lee `0`: {q0, q3} ⟶ {q0, q1} [q0→q0, q0→q1]
- **Rechazada**: ningún estado de {q0, q1} es de aceptación.

## Cadena `01111`

- Inicio: {q0}
- Lee `0`: {q0} ⟶ {q0, q1} [q0→q0, q0→q1] (bifurcación)
- Lee `1`: {q0, q1} ⟶ {q0, q3} [q0→q0, q0→q3]
- Lee `1`: {q0, q3} ⟶ {q0, q3, q4} [q0→q0, q0→q3, q3→q4] (bifurcación)
- Lee `1`: {q0, q3, q4} ⟶ {q0, q3, q4} [q0→q0, q0→q3, q3→q4]
- Lee `1`: {q0, q3, q4} ⟶ {q0, q3, q4} [q0→q0, q0→q3, q3→q4]
- **Rechazada**: ningún estado de {q0, q3, q4} es de aceptación.

## Cadena `01101001`

- Inicio: {q0}
- Lee `0`: {q0} ⟶ {q0, q1} [q0→q0, q0→q1] (bifurcación)
- Lee `1`: {q0, q1} ⟶ {q0, q3} [q0→q0, q0→q3]
- Lee `1`: {q0, q3} ⟶ {q0, q3, q4} [q0→q0, q0→q3, q3→q4] (bifurcación)
- Lee `0`: {q0, q3, q4} ⟶ {q0, q1} [q0→q0, q0→q1]
- Lee `1`: {q0, q1} ⟶ {q0, q3} [q0→q0, q0→q3]
- Lee `0`: {q0, q3} ⟶ {q0, q1} [q0→q0, q0→q1]
- Lee `0`: {q0, q1} ⟶ {q0, q1, q2} [q0→q0, q0→q1, q1→q2] (bifurcación)
- Lee `1`: {q0, q1, q2} ⟶ {q0, q3} [q0→q0, q0→q3]
- **Rechazada**: ningún estado de {q0, q3} es de aceptación.
