# Recorridos: Lista 3 · AFN del problema 098

AFN para el problema 98: Las palabras de Σ1 que terminan con la cadena 00102.

Autómata: `lista3-afn-098` (AFN).

## Cadena `00102`

- Inicio: {c0}
- Lee `0`: {c0} ⟶ {c0, c1} [c0→c0, c0→c1] (bifurcación)
- Lee `0`: {c0, c1} ⟶ {c0, c1, c2} [c0→c0, c0→c1, c1→c2] (bifurcación)
- Lee `1`: {c0, c1, c2} ⟶ {c0, c3} [c0→c0, c2→c3]
- Lee `0`: {c0, c3} ⟶ {c0, c1, c4} [c0→c0, c0→c1, c3→c4] (bifurcación)
- Lee `2`: {c0, c1, c4} ⟶ {c0, c5} [c0→c0, c4→c5]
- **Aceptada**: queda {c5} ∈ F.

## Cadena `100102`

- Inicio: {c0}
- Lee `1`: {c0} ⟶ {c0} [c0→c0]
- Lee `0`: {c0} ⟶ {c0, c1} [c0→c0, c0→c1] (bifurcación)
- Lee `0`: {c0, c1} ⟶ {c0, c1, c2} [c0→c0, c0→c1, c1→c2] (bifurcación)
- Lee `1`: {c0, c1, c2} ⟶ {c0, c3} [c0→c0, c2→c3]
- Lee `0`: {c0, c3} ⟶ {c0, c1, c4} [c0→c0, c0→c1, c3→c4] (bifurcación)
- Lee `2`: {c0, c1, c4} ⟶ {c0, c5} [c0→c0, c4→c5]
- **Aceptada**: queda {c5} ∈ F.

## Cadena `20000102`

- Inicio: {c0}
- Lee `2`: {c0} ⟶ {c0} [c0→c0]
- Lee `0`: {c0} ⟶ {c0, c1} [c0→c0, c0→c1] (bifurcación)
- Lee `0`: {c0, c1} ⟶ {c0, c1, c2} [c0→c0, c0→c1, c1→c2] (bifurcación)
- Lee `0`: {c0, c1, c2} ⟶ {c0, c1, c2} [c0→c0, c0→c1, c1→c2]
- Lee `0`: {c0, c1, c2} ⟶ {c0, c1, c2} [c0→c0, c0→c1, c1→c2]
- Lee `1`: {c0, c1, c2} ⟶ {c0, c3} [c0→c0, c2→c3]
- Lee `0`: {c0, c3} ⟶ {c0, c1, c4} [c0→c0, c0→c1, c3→c4] (bifurcación)
- Lee `2`: {c0, c1, c4} ⟶ {c0, c5} [c0→c0, c4→c5]
- **Aceptada**: queda {c5} ∈ F.

## Cadena `2100200102`

- Inicio: {c0}
- Lee `2`: {c0} ⟶ {c0} [c0→c0]
- Lee `1`: {c0} ⟶ {c0} [c0→c0]
- Lee `0`: {c0} ⟶ {c0, c1} [c0→c0, c0→c1] (bifurcación)
- Lee `0`: {c0, c1} ⟶ {c0, c1, c2} [c0→c0, c0→c1, c1→c2] (bifurcación)
- Lee `2`: {c0, c1, c2} ⟶ {c0} [c0→c0]
- Lee `0`: {c0} ⟶ {c0, c1} [c0→c0, c0→c1] (bifurcación)
- Lee `0`: {c0, c1} ⟶ {c0, c1, c2} [c0→c0, c0→c1, c1→c2] (bifurcación)
- Lee `1`: {c0, c1, c2} ⟶ {c0, c3} [c0→c0, c2→c3]
- Lee `0`: {c0, c3} ⟶ {c0, c1, c4} [c0→c0, c0→c1, c3→c4] (bifurcación)
- Lee `2`: {c0, c1, c4} ⟶ {c0, c5} [c0→c0, c4→c5]
- **Aceptada**: queda {c5} ∈ F.

## Cadena `0221101000102`

- Inicio: {c0}
- Lee `0`: {c0} ⟶ {c0, c1} [c0→c0, c0→c1] (bifurcación)
- Lee `2`: {c0, c1} ⟶ {c0} [c0→c0]
- Lee `2`: {c0} ⟶ {c0} [c0→c0]
- Lee `1`: {c0} ⟶ {c0} [c0→c0]
- Lee `1`: {c0} ⟶ {c0} [c0→c0]
- Lee `0`: {c0} ⟶ {c0, c1} [c0→c0, c0→c1] (bifurcación)
- Lee `1`: {c0, c1} ⟶ {c0} [c0→c0]
- Lee `0`: {c0} ⟶ {c0, c1} [c0→c0, c0→c1] (bifurcación)
- Lee `0`: {c0, c1} ⟶ {c0, c1, c2} [c0→c0, c0→c1, c1→c2] (bifurcación)
- Lee `0`: {c0, c1, c2} ⟶ {c0, c1, c2} [c0→c0, c0→c1, c1→c2]
- Lee `1`: {c0, c1, c2} ⟶ {c0, c3} [c0→c0, c2→c3]
- Lee `0`: {c0, c3} ⟶ {c0, c1, c4} [c0→c0, c0→c1, c3→c4] (bifurcación)
- Lee `2`: {c0, c1, c4} ⟶ {c0, c5} [c0→c0, c4→c5]
- **Aceptada**: queda {c5} ∈ F.

## Cadena λ

- Inicio: {c0}
- **Rechazada**: ningún estado de {c0} es de aceptación.

## Cadena `2`

- Inicio: {c0}
- Lee `2`: {c0} ⟶ {c0} [c0→c0]
- **Rechazada**: ningún estado de {c0} es de aceptación.

## Cadena `122`

- Inicio: {c0}
- Lee `1`: {c0} ⟶ {c0} [c0→c0]
- Lee `2`: {c0} ⟶ {c0} [c0→c0]
- Lee `2`: {c0} ⟶ {c0} [c0→c0]
- **Rechazada**: ningún estado de {c0} es de aceptación.

## Cadena `11100`

- Inicio: {c0}
- Lee `1`: {c0} ⟶ {c0} [c0→c0]
- Lee `1`: {c0} ⟶ {c0} [c0→c0]
- Lee `1`: {c0} ⟶ {c0} [c0→c0]
- Lee `0`: {c0} ⟶ {c0, c1} [c0→c0, c0→c1] (bifurcación)
- Lee `0`: {c0, c1} ⟶ {c0, c1, c2} [c0→c0, c0→c1, c1→c2] (bifurcación)
- **Rechazada**: ningún estado de {c0, c1, c2} es de aceptación.

## Cadena `22220002`

- Inicio: {c0}
- Lee `2`: {c0} ⟶ {c0} [c0→c0]
- Lee `2`: {c0} ⟶ {c0} [c0→c0]
- Lee `2`: {c0} ⟶ {c0} [c0→c0]
- Lee `2`: {c0} ⟶ {c0} [c0→c0]
- Lee `0`: {c0} ⟶ {c0, c1} [c0→c0, c0→c1] (bifurcación)
- Lee `0`: {c0, c1} ⟶ {c0, c1, c2} [c0→c0, c0→c1, c1→c2] (bifurcación)
- Lee `0`: {c0, c1, c2} ⟶ {c0, c1, c2} [c0→c0, c0→c1, c1→c2]
- Lee `2`: {c0, c1, c2} ⟶ {c0} [c0→c0]
- **Rechazada**: ningún estado de {c0} es de aceptación.

## Cadena `0222`

- Inicio: {c0}
- Lee `0`: {c0} ⟶ {c0, c1} [c0→c0, c0→c1] (bifurcación)
- Lee `2`: {c0, c1} ⟶ {c0} [c0→c0]
- Lee `2`: {c0} ⟶ {c0} [c0→c0]
- Lee `2`: {c0} ⟶ {c0} [c0→c0]
- **Rechazada**: ningún estado de {c0} es de aceptación.
