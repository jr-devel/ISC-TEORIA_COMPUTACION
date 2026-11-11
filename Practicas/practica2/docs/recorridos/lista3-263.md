# Recorridos: Lista 3 · Ejercicio 263

AFD equivalente al AFN de la figura 263 (transcrito).

Autómata: `lista3-263` (AFN).

## Cadena `01`

- Inicio: {q0}
- Lee `0`: {q0} ⟶ {q0, q1} [q0→q0, q0→q1] (bifurcación)
- Lee `1`: {q0, q1} ⟶ {q0, q2} [q0→q0, q1→q2]
- **Aceptada**: queda {q2} ∈ F.

## Cadena `001`

- Inicio: {q0}
- Lee `0`: {q0} ⟶ {q0, q1} [q0→q0, q0→q1] (bifurcación)
- Lee `0`: {q0, q1} ⟶ {q0, q1} [q0→q0, q0→q1]
- Lee `1`: {q0, q1} ⟶ {q0, q2} [q0→q0, q1→q2]
- **Aceptada**: queda {q2} ∈ F.

## Cadena `00001`

- Inicio: {q0}
- Lee `0`: {q0} ⟶ {q0, q1} [q0→q0, q0→q1] (bifurcación)
- Lee `0`: {q0, q1} ⟶ {q0, q1} [q0→q0, q0→q1]
- Lee `0`: {q0, q1} ⟶ {q0, q1} [q0→q0, q0→q1]
- Lee `0`: {q0, q1} ⟶ {q0, q1} [q0→q0, q0→q1]
- Lee `1`: {q0, q1} ⟶ {q0, q2} [q0→q0, q1→q2]
- **Aceptada**: queda {q2} ∈ F.

## Cadena `1000001`

- Inicio: {q0}
- Lee `1`: {q0} ⟶ {q0} [q0→q0]
- Lee `0`: {q0} ⟶ {q0, q1} [q0→q0, q0→q1] (bifurcación)
- Lee `0`: {q0, q1} ⟶ {q0, q1} [q0→q0, q0→q1]
- Lee `0`: {q0, q1} ⟶ {q0, q1} [q0→q0, q0→q1]
- Lee `0`: {q0, q1} ⟶ {q0, q1} [q0→q0, q0→q1]
- Lee `0`: {q0, q1} ⟶ {q0, q1} [q0→q0, q0→q1]
- Lee `1`: {q0, q1} ⟶ {q0, q2} [q0→q0, q1→q2]
- **Aceptada**: queda {q2} ∈ F.

## Cadena `0100011001`

- Inicio: {q0}
- Lee `0`: {q0} ⟶ {q0, q1} [q0→q0, q0→q1] (bifurcación)
- Lee `1`: {q0, q1} ⟶ {q0, q2} [q0→q0, q1→q2]
- Lee `0`: {q0, q2} ⟶ {q0, q1} [q0→q0, q0→q1]
- Lee `0`: {q0, q1} ⟶ {q0, q1} [q0→q0, q0→q1]
- Lee `0`: {q0, q1} ⟶ {q0, q1} [q0→q0, q0→q1]
- Lee `1`: {q0, q1} ⟶ {q0, q2} [q0→q0, q1→q2]
- Lee `1`: {q0, q2} ⟶ {q0} [q0→q0]
- Lee `0`: {q0} ⟶ {q0, q1} [q0→q0, q0→q1] (bifurcación)
- Lee `0`: {q0, q1} ⟶ {q0, q1} [q0→q0, q0→q1]
- Lee `1`: {q0, q1} ⟶ {q0, q2} [q0→q0, q1→q2]
- **Aceptada**: queda {q2} ∈ F.

## Cadena λ

- Inicio: {q0}
- **Rechazada**: ningún estado de {q0} es de aceptación.

## Cadena `0`

- Inicio: {q0}
- Lee `0`: {q0} ⟶ {q0, q1} [q0→q0, q0→q1] (bifurcación)
- **Rechazada**: ningún estado de {q0, q1} es de aceptación.

## Cadena `100`

- Inicio: {q0}
- Lee `1`: {q0} ⟶ {q0} [q0→q0]
- Lee `0`: {q0} ⟶ {q0, q1} [q0→q0, q0→q1] (bifurcación)
- Lee `0`: {q0, q1} ⟶ {q0, q1} [q0→q0, q0→q1]
- **Rechazada**: ningún estado de {q0, q1} es de aceptación.

## Cadena `00011`

- Inicio: {q0}
- Lee `0`: {q0} ⟶ {q0, q1} [q0→q0, q0→q1] (bifurcación)
- Lee `0`: {q0, q1} ⟶ {q0, q1} [q0→q0, q0→q1]
- Lee `0`: {q0, q1} ⟶ {q0, q1} [q0→q0, q0→q1]
- Lee `1`: {q0, q1} ⟶ {q0, q2} [q0→q0, q1→q2]
- Lee `1`: {q0, q2} ⟶ {q0} [q0→q0]
- **Rechazada**: ningún estado de {q0} es de aceptación.

## Cadena `01010010`

- Inicio: {q0}
- Lee `0`: {q0} ⟶ {q0, q1} [q0→q0, q0→q1] (bifurcación)
- Lee `1`: {q0, q1} ⟶ {q0, q2} [q0→q0, q1→q2]
- Lee `0`: {q0, q2} ⟶ {q0, q1} [q0→q0, q0→q1]
- Lee `1`: {q0, q1} ⟶ {q0, q2} [q0→q0, q1→q2]
- Lee `0`: {q0, q2} ⟶ {q0, q1} [q0→q0, q0→q1]
- Lee `0`: {q0, q1} ⟶ {q0, q1} [q0→q0, q0→q1]
- Lee `1`: {q0, q1} ⟶ {q0, q2} [q0→q0, q1→q2]
- Lee `0`: {q0, q2} ⟶ {q0, q1} [q0→q0, q0→q1]
- **Rechazada**: ningún estado de {q0, q1} es de aceptación.
