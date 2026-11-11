# Recorridos: Lista 3 · AFN del problema 099

AFN para el problema 99: Las palabras de Σ1 que terminan con la cadena 001001.

Autómata: `lista3-afn-099` (AFN).

## Cadena `001001`

- Inicio: {c0}
- Lee `0`: {c0} ⟶ {c0, c1} [c0→c0, c0→c1] (bifurcación)
- Lee `0`: {c0, c1} ⟶ {c0, c1, c2} [c0→c0, c0→c1, c1→c2] (bifurcación)
- Lee `1`: {c0, c1, c2} ⟶ {c0, c3} [c0→c0, c2→c3]
- Lee `0`: {c0, c3} ⟶ {c0, c1, c4} [c0→c0, c0→c1, c3→c4] (bifurcación)
- Lee `0`: {c0, c1, c4} ⟶ {c0, c1, c2, c5} [c0→c0, c0→c1, c1→c2, c4→c5] (bifurcación)
- Lee `1`: {c0, c1, c2, c5} ⟶ {c0, c3, c6} [c0→c0, c2→c3, c5→c6]
- **Aceptada**: queda {c6} ∈ F.

## Cadena `1001001`

- Inicio: {c0}
- Lee `1`: {c0} ⟶ {c0} [c0→c0]
- Lee `0`: {c0} ⟶ {c0, c1} [c0→c0, c0→c1] (bifurcación)
- Lee `0`: {c0, c1} ⟶ {c0, c1, c2} [c0→c0, c0→c1, c1→c2] (bifurcación)
- Lee `1`: {c0, c1, c2} ⟶ {c0, c3} [c0→c0, c2→c3]
- Lee `0`: {c0, c3} ⟶ {c0, c1, c4} [c0→c0, c0→c1, c3→c4] (bifurcación)
- Lee `0`: {c0, c1, c4} ⟶ {c0, c1, c2, c5} [c0→c0, c0→c1, c1→c2, c4→c5] (bifurcación)
- Lee `1`: {c0, c1, c2, c5} ⟶ {c0, c3, c6} [c0→c0, c2→c3, c5→c6]
- **Aceptada**: queda {c6} ∈ F.

## Cadena `121001001`

- Inicio: {c0}
- Lee `1`: {c0} ⟶ {c0} [c0→c0]
- Lee `2`: {c0} ⟶ {c0} [c0→c0]
- Lee `1`: {c0} ⟶ {c0} [c0→c0]
- Lee `0`: {c0} ⟶ {c0, c1} [c0→c0, c0→c1] (bifurcación)
- Lee `0`: {c0, c1} ⟶ {c0, c1, c2} [c0→c0, c0→c1, c1→c2] (bifurcación)
- Lee `1`: {c0, c1, c2} ⟶ {c0, c3} [c0→c0, c2→c3]
- Lee `0`: {c0, c3} ⟶ {c0, c1, c4} [c0→c0, c0→c1, c3→c4] (bifurcación)
- Lee `0`: {c0, c1, c4} ⟶ {c0, c1, c2, c5} [c0→c0, c0→c1, c1→c2, c4→c5] (bifurcación)
- Lee `1`: {c0, c1, c2, c5} ⟶ {c0, c3, c6} [c0→c0, c2→c3, c5→c6]
- **Aceptada**: queda {c6} ∈ F.

## Cadena `10211001001`

- Inicio: {c0}
- Lee `1`: {c0} ⟶ {c0} [c0→c0]
- Lee `0`: {c0} ⟶ {c0, c1} [c0→c0, c0→c1] (bifurcación)
- Lee `2`: {c0, c1} ⟶ {c0} [c0→c0]
- Lee `1`: {c0} ⟶ {c0} [c0→c0]
- Lee `1`: {c0} ⟶ {c0} [c0→c0]
- Lee `0`: {c0} ⟶ {c0, c1} [c0→c0, c0→c1] (bifurcación)
- Lee `0`: {c0, c1} ⟶ {c0, c1, c2} [c0→c0, c0→c1, c1→c2] (bifurcación)
- Lee `1`: {c0, c1, c2} ⟶ {c0, c3} [c0→c0, c2→c3]
- Lee `0`: {c0, c3} ⟶ {c0, c1, c4} [c0→c0, c0→c1, c3→c4] (bifurcación)
- Lee `0`: {c0, c1, c4} ⟶ {c0, c1, c2, c5} [c0→c0, c0→c1, c1→c2, c4→c5] (bifurcación)
- Lee `1`: {c0, c1, c2, c5} ⟶ {c0, c3, c6} [c0→c0, c2→c3, c5→c6]
- **Aceptada**: queda {c6} ∈ F.

## Cadena `00200202001001`

- Inicio: {c0}
- Lee `0`: {c0} ⟶ {c0, c1} [c0→c0, c0→c1] (bifurcación)
- Lee `0`: {c0, c1} ⟶ {c0, c1, c2} [c0→c0, c0→c1, c1→c2] (bifurcación)
- Lee `2`: {c0, c1, c2} ⟶ {c0} [c0→c0]
- Lee `0`: {c0} ⟶ {c0, c1} [c0→c0, c0→c1] (bifurcación)
- Lee `0`: {c0, c1} ⟶ {c0, c1, c2} [c0→c0, c0→c1, c1→c2] (bifurcación)
- Lee `2`: {c0, c1, c2} ⟶ {c0} [c0→c0]
- Lee `0`: {c0} ⟶ {c0, c1} [c0→c0, c0→c1] (bifurcación)
- Lee `2`: {c0, c1} ⟶ {c0} [c0→c0]
- Lee `0`: {c0} ⟶ {c0, c1} [c0→c0, c0→c1] (bifurcación)
- Lee `0`: {c0, c1} ⟶ {c0, c1, c2} [c0→c0, c0→c1, c1→c2] (bifurcación)
- Lee `1`: {c0, c1, c2} ⟶ {c0, c3} [c0→c0, c2→c3]
- Lee `0`: {c0, c3} ⟶ {c0, c1, c4} [c0→c0, c0→c1, c3→c4] (bifurcación)
- Lee `0`: {c0, c1, c4} ⟶ {c0, c1, c2, c5} [c0→c0, c0→c1, c1→c2, c4→c5] (bifurcación)
- Lee `1`: {c0, c1, c2, c5} ⟶ {c0, c3, c6} [c0→c0, c2→c3, c5→c6]
- **Aceptada**: queda {c6} ∈ F.

## Cadena λ

- Inicio: {c0}
- **Rechazada**: ningún estado de {c0} es de aceptación.

## Cadena `2`

- Inicio: {c0}
- Lee `2`: {c0} ⟶ {c0} [c0→c0]
- **Rechazada**: ningún estado de {c0} es de aceptación.

## Cadena `120`

- Inicio: {c0}
- Lee `1`: {c0} ⟶ {c0} [c0→c0]
- Lee `2`: {c0} ⟶ {c0} [c0→c0]
- Lee `0`: {c0} ⟶ {c0, c1} [c0→c0, c0→c1] (bifurcación)
- **Rechazada**: ningún estado de {c0, c1} es de aceptación.

## Cadena `22202`

- Inicio: {c0}
- Lee `2`: {c0} ⟶ {c0} [c0→c0]
- Lee `2`: {c0} ⟶ {c0} [c0→c0]
- Lee `2`: {c0} ⟶ {c0} [c0→c0]
- Lee `0`: {c0} ⟶ {c0, c1} [c0→c0, c0→c1] (bifurcación)
- Lee `2`: {c0, c1} ⟶ {c0} [c0→c0]
- **Rechazada**: ningún estado de {c0} es de aceptación.

## Cadena `02211011`

- Inicio: {c0}
- Lee `0`: {c0} ⟶ {c0, c1} [c0→c0, c0→c1] (bifurcación)
- Lee `2`: {c0, c1} ⟶ {c0} [c0→c0]
- Lee `2`: {c0} ⟶ {c0} [c0→c0]
- Lee `1`: {c0} ⟶ {c0} [c0→c0]
- Lee `1`: {c0} ⟶ {c0} [c0→c0]
- Lee `0`: {c0} ⟶ {c0, c1} [c0→c0, c0→c1] (bifurcación)
- Lee `1`: {c0, c1} ⟶ {c0} [c0→c0]
- Lee `1`: {c0} ⟶ {c0} [c0→c0]
- **Rechazada**: ningún estado de {c0} es de aceptación.

## Cadena `02210`

- Inicio: {c0}
- Lee `0`: {c0} ⟶ {c0, c1} [c0→c0, c0→c1] (bifurcación)
- Lee `2`: {c0, c1} ⟶ {c0} [c0→c0]
- Lee `2`: {c0} ⟶ {c0} [c0→c0]
- Lee `1`: {c0} ⟶ {c0} [c0→c0]
- Lee `0`: {c0} ⟶ {c0, c1} [c0→c0, c0→c1] (bifurcación)
- **Rechazada**: ningún estado de {c0, c1} es de aceptación.
