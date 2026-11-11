# Recorridos: Lista 3 · AFN del problema 094

AFN para el problema 94: Las palabras de Σ1 que comienzan con 1 y terminan con 2.

Autómata: `lista3-afn-094` (AFN).

## Cadena `12`

- Inicio: {q0}
- Lee `1`: {q0} ⟶ {q1} [q0→q1]
- Lee `2`: {q1} ⟶ {q1, q2} [q1→q1, q1→q2] (bifurcación)
- **Aceptada**: queda {q2} ∈ F.

## Cadena `102`

- Inicio: {q0}
- Lee `1`: {q0} ⟶ {q1} [q0→q1]
- Lee `0`: {q1} ⟶ {q1} [q1→q1]
- Lee `2`: {q1} ⟶ {q1, q2} [q1→q1, q1→q2] (bifurcación)
- **Aceptada**: queda {q2} ∈ F.

## Cadena `11012`

- Inicio: {q0}
- Lee `1`: {q0} ⟶ {q1} [q0→q1]
- Lee `1`: {q1} ⟶ {q1} [q1→q1]
- Lee `0`: {q1} ⟶ {q1} [q1→q1]
- Lee `1`: {q1} ⟶ {q1} [q1→q1]
- Lee `2`: {q1} ⟶ {q1, q2} [q1→q1, q1→q2] (bifurcación)
- **Aceptada**: queda {q2} ∈ F.

## Cadena `1022012`

- Inicio: {q0}
- Lee `1`: {q0} ⟶ {q1} [q0→q1]
- Lee `0`: {q1} ⟶ {q1} [q1→q1]
- Lee `2`: {q1} ⟶ {q1, q2} [q1→q1, q1→q2] (bifurcación)
- Lee `2`: {q1, q2} ⟶ {q1, q2} [q1→q1, q1→q2]
- Lee `0`: {q1, q2} ⟶ {q1} [q1→q1]
- Lee `1`: {q1} ⟶ {q1} [q1→q1]
- Lee `2`: {q1} ⟶ {q1, q2} [q1→q1, q1→q2] (bifurcación)
- **Aceptada**: queda {q2} ∈ F.

## Cadena `1021101222`

- Inicio: {q0}
- Lee `1`: {q0} ⟶ {q1} [q0→q1]
- Lee `0`: {q1} ⟶ {q1} [q1→q1]
- Lee `2`: {q1} ⟶ {q1, q2} [q1→q1, q1→q2] (bifurcación)
- Lee `1`: {q1, q2} ⟶ {q1} [q1→q1]
- Lee `1`: {q1} ⟶ {q1} [q1→q1]
- Lee `0`: {q1} ⟶ {q1} [q1→q1]
- Lee `1`: {q1} ⟶ {q1} [q1→q1]
- Lee `2`: {q1} ⟶ {q1, q2} [q1→q1, q1→q2] (bifurcación)
- Lee `2`: {q1, q2} ⟶ {q1, q2} [q1→q1, q1→q2]
- Lee `2`: {q1, q2} ⟶ {q1, q2} [q1→q1, q1→q2]
- **Aceptada**: queda {q2} ∈ F.

## Cadena λ

- Inicio: {q0}
- **Rechazada**: ningún estado de {q0} es de aceptación.

## Cadena `2`

- Inicio: {q0}
- Lee `2`: {q0} ⟶ ∅ [ninguna transición]
- **Rechazada**: no queda ningún estado activo.

## Cadena `212`

- Inicio: {q0}
- Lee `2`: {q0} ⟶ ∅ [ninguna transición]
- Lee `1`: ∅ ⟶ ∅ [ninguna transición]
- Lee `2`: ∅ ⟶ ∅ [ninguna transición]
- **Rechazada**: no queda ningún estado activo.

## Cadena `00012`

- Inicio: {q0}
- Lee `0`: {q0} ⟶ ∅ [ninguna transición]
- Lee `0`: ∅ ⟶ ∅ [ninguna transición]
- Lee `0`: ∅ ⟶ ∅ [ninguna transición]
- Lee `1`: ∅ ⟶ ∅ [ninguna transición]
- Lee `2`: ∅ ⟶ ∅ [ninguna transición]
- **Rechazada**: no queda ningún estado activo.

## Cadena `20021021`

- Inicio: {q0}
- Lee `2`: {q0} ⟶ ∅ [ninguna transición]
- Lee `0`: ∅ ⟶ ∅ [ninguna transición]
- Lee `0`: ∅ ⟶ ∅ [ninguna transición]
- Lee `2`: ∅ ⟶ ∅ [ninguna transición]
- Lee `1`: ∅ ⟶ ∅ [ninguna transición]
- Lee `0`: ∅ ⟶ ∅ [ninguna transición]
- Lee `2`: ∅ ⟶ ∅ [ninguna transición]
- Lee `1`: ∅ ⟶ ∅ [ninguna transición]
- **Rechazada**: no queda ningún estado activo.

## Cadena `0`

- Inicio: {q0}
- Lee `0`: {q0} ⟶ ∅ [ninguna transición]
- **Rechazada**: no queda ningún estado activo.
