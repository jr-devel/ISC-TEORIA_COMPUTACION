# Recorridos: Lista 3 · AFN del problema 120

AFN para el problema 120: Las palabras de Σ1 tales que el primer carácter y el último son distintos.

Autómata: `lista3-afn-120` (AFN).

## Cadena `12`

- Inicio: {q0}
- Lee `1`: {q0} ⟶ {s1} [q0→s1]
- Lee `2`: {s1} ⟶ {s1, f} [s1→f, s1→s1] (bifurcación)
- **Aceptada**: queda {f} ∈ F.

## Cadena `211`

- Inicio: {q0}
- Lee `2`: {q0} ⟶ {s2} [q0→s2]
- Lee `1`: {s2} ⟶ {s2, f} [s2→f, s2→s2] (bifurcación)
- Lee `1`: {s2, f} ⟶ {s2, f} [s2→f, s2→s2]
- **Aceptada**: queda {f} ∈ F.

## Cadena `12002`

- Inicio: {q0}
- Lee `1`: {q0} ⟶ {s1} [q0→s1]
- Lee `2`: {s1} ⟶ {s1, f} [s1→f, s1→s1] (bifurcación)
- Lee `0`: {s1, f} ⟶ {s1, f} [s1→f, s1→s1]
- Lee `0`: {s1, f} ⟶ {s1, f} [s1→f, s1→s1]
- Lee `2`: {s1, f} ⟶ {s1, f} [s1→f, s1→s1]
- **Aceptada**: queda {f} ∈ F.

## Cadena `1202000`

- Inicio: {q0}
- Lee `1`: {q0} ⟶ {s1} [q0→s1]
- Lee `2`: {s1} ⟶ {s1, f} [s1→f, s1→s1] (bifurcación)
- Lee `0`: {s1, f} ⟶ {s1, f} [s1→f, s1→s1]
- Lee `2`: {s1, f} ⟶ {s1, f} [s1→f, s1→s1]
- Lee `0`: {s1, f} ⟶ {s1, f} [s1→f, s1→s1]
- Lee `0`: {s1, f} ⟶ {s1, f} [s1→f, s1→s1]
- Lee `0`: {s1, f} ⟶ {s1, f} [s1→f, s1→s1]
- **Aceptada**: queda {f} ∈ F.

## Cadena `0121120211`

- Inicio: {q0}
- Lee `0`: {q0} ⟶ {s0} [q0→s0]
- Lee `1`: {s0} ⟶ {s0, f} [s0→f, s0→s0] (bifurcación)
- Lee `2`: {s0, f} ⟶ {s0, f} [s0→f, s0→s0]
- Lee `1`: {s0, f} ⟶ {s0, f} [s0→f, s0→s0]
- Lee `1`: {s0, f} ⟶ {s0, f} [s0→f, s0→s0]
- Lee `2`: {s0, f} ⟶ {s0, f} [s0→f, s0→s0]
- Lee `0`: {s0, f} ⟶ {s0} [s0→s0]
- Lee `2`: {s0} ⟶ {s0, f} [s0→f, s0→s0] (bifurcación)
- Lee `1`: {s0, f} ⟶ {s0, f} [s0→f, s0→s0]
- Lee `1`: {s0, f} ⟶ {s0, f} [s0→f, s0→s0]
- **Aceptada**: queda {f} ∈ F.

## Cadena λ

- Inicio: {q0}
- **Rechazada**: ningún estado de {q0} es de aceptación.

## Cadena `1`

- Inicio: {q0}
- Lee `1`: {q0} ⟶ {s1} [q0→s1]
- **Rechazada**: ningún estado de {s1} es de aceptación.

## Cadena `222`

- Inicio: {q0}
- Lee `2`: {q0} ⟶ {s2} [q0→s2]
- Lee `2`: {s2} ⟶ {s2} [s2→s2]
- Lee `2`: {s2} ⟶ {s2} [s2→s2]
- **Rechazada**: ningún estado de {s2} es de aceptación.

## Cadena `21012`

- Inicio: {q0}
- Lee `2`: {q0} ⟶ {s2} [q0→s2]
- Lee `1`: {s2} ⟶ {s2, f} [s2→f, s2→s2] (bifurcación)
- Lee `0`: {s2, f} ⟶ {s2, f} [s2→f, s2→s2]
- Lee `1`: {s2, f} ⟶ {s2, f} [s2→f, s2→s2]
- Lee `2`: {s2, f} ⟶ {s2} [s2→s2]
- **Rechazada**: ningún estado de {s2} es de aceptación.

## Cadena `02120120`

- Inicio: {q0}
- Lee `0`: {q0} ⟶ {s0} [q0→s0]
- Lee `2`: {s0} ⟶ {s0, f} [s0→f, s0→s0] (bifurcación)
- Lee `1`: {s0, f} ⟶ {s0, f} [s0→f, s0→s0]
- Lee `2`: {s0, f} ⟶ {s0, f} [s0→f, s0→s0]
- Lee `0`: {s0, f} ⟶ {s0} [s0→s0]
- Lee `1`: {s0} ⟶ {s0, f} [s0→f, s0→s0] (bifurcación)
- Lee `2`: {s0, f} ⟶ {s0, f} [s0→f, s0→s0]
- Lee `0`: {s0, f} ⟶ {s0} [s0→s0]
- **Rechazada**: ningún estado de {s0} es de aceptación.

## Cadena `02`

- Inicio: {q0}
- Lee `0`: {q0} ⟶ {s0} [q0→s0]
- Lee `2`: {s0} ⟶ {s0, f} [s0→f, s0→s0] (bifurcación)
- **Aceptada**: queda {f} ∈ F.

## Cadena `2`

- Inicio: {q0}
- Lee `2`: {q0} ⟶ {s2} [q0→s2]
- **Rechazada**: ningún estado de {s2} es de aceptación.
