# Recorridos: Lista 3 · AFN del problema 106

AFN para el problema 106: Las palabras de Σ1 que incluyen la subcadena 1101001.

Autómata: `lista3-afn-106` (AFN).

## Cadena `1101001`

- Inicio: {c0}
- Lee `1`: {c0} ⟶ {c0, c1} [c0→c0, c0→c1] (bifurcación)
- Lee `1`: {c0, c1} ⟶ {c0, c1, c2} [c0→c0, c0→c1, c1→c2] (bifurcación)
- Lee `0`: {c0, c1, c2} ⟶ {c0, c3} [c0→c0, c2→c3]
- Lee `1`: {c0, c3} ⟶ {c0, c1, c4} [c0→c0, c0→c1, c3→c4] (bifurcación)
- Lee `0`: {c0, c1, c4} ⟶ {c0, c5} [c0→c0, c4→c5]
- Lee `0`: {c0, c5} ⟶ {c0, c6} [c0→c0, c5→c6]
- Lee `1`: {c0, c6} ⟶ {c0, c1, c7} [c0→c0, c0→c1, c6→c7] (bifurcación)
- **Aceptada**: queda {c7} ∈ F.

## Cadena `11010010`

- Inicio: {c0}
- Lee `1`: {c0} ⟶ {c0, c1} [c0→c0, c0→c1] (bifurcación)
- Lee `1`: {c0, c1} ⟶ {c0, c1, c2} [c0→c0, c0→c1, c1→c2] (bifurcación)
- Lee `0`: {c0, c1, c2} ⟶ {c0, c3} [c0→c0, c2→c3]
- Lee `1`: {c0, c3} ⟶ {c0, c1, c4} [c0→c0, c0→c1, c3→c4] (bifurcación)
- Lee `0`: {c0, c1, c4} ⟶ {c0, c5} [c0→c0, c4→c5]
- Lee `0`: {c0, c5} ⟶ {c0, c6} [c0→c0, c5→c6]
- Lee `1`: {c0, c6} ⟶ {c0, c1, c7} [c0→c0, c0→c1, c6→c7] (bifurcación)
- Lee `0`: {c0, c1, c7} ⟶ {c0, c7} [c0→c0, c7→c7]
- **Aceptada**: queda {c7} ∈ F.

## Cadena `1101001110`

- Inicio: {c0}
- Lee `1`: {c0} ⟶ {c0, c1} [c0→c0, c0→c1] (bifurcación)
- Lee `1`: {c0, c1} ⟶ {c0, c1, c2} [c0→c0, c0→c1, c1→c2] (bifurcación)
- Lee `0`: {c0, c1, c2} ⟶ {c0, c3} [c0→c0, c2→c3]
- Lee `1`: {c0, c3} ⟶ {c0, c1, c4} [c0→c0, c0→c1, c3→c4] (bifurcación)
- Lee `0`: {c0, c1, c4} ⟶ {c0, c5} [c0→c0, c4→c5]
- Lee `0`: {c0, c5} ⟶ {c0, c6} [c0→c0, c5→c6]
- Lee `1`: {c0, c6} ⟶ {c0, c1, c7} [c0→c0, c0→c1, c6→c7] (bifurcación)
- Lee `1`: {c0, c1, c7} ⟶ {c0, c1, c2, c7} [c0→c0, c0→c1, c1→c2, c7→c7] (bifurcación)
- Lee `1`: {c0, c1, c2, c7} ⟶ {c0, c1, c2, c7} [c0→c0, c0→c1, c1→c2, c7→c7]
- Lee `0`: {c0, c1, c2, c7} ⟶ {c0, c3, c7} [c0→c0, c2→c3, c7→c7]
- **Aceptada**: queda {c7} ∈ F.

## Cadena `212011010012`

- Inicio: {c0}
- Lee `2`: {c0} ⟶ {c0} [c0→c0]
- Lee `1`: {c0} ⟶ {c0, c1} [c0→c0, c0→c1] (bifurcación)
- Lee `2`: {c0, c1} ⟶ {c0} [c0→c0]
- Lee `0`: {c0} ⟶ {c0} [c0→c0]
- Lee `1`: {c0} ⟶ {c0, c1} [c0→c0, c0→c1] (bifurcación)
- Lee `1`: {c0, c1} ⟶ {c0, c1, c2} [c0→c0, c0→c1, c1→c2] (bifurcación)
- Lee `0`: {c0, c1, c2} ⟶ {c0, c3} [c0→c0, c2→c3]
- Lee `1`: {c0, c3} ⟶ {c0, c1, c4} [c0→c0, c0→c1, c3→c4] (bifurcación)
- Lee `0`: {c0, c1, c4} ⟶ {c0, c5} [c0→c0, c4→c5]
- Lee `0`: {c0, c5} ⟶ {c0, c6} [c0→c0, c5→c6]
- Lee `1`: {c0, c6} ⟶ {c0, c1, c7} [c0→c0, c0→c1, c6→c7] (bifurcación)
- Lee `2`: {c0, c1, c7} ⟶ {c0, c7} [c0→c0, c7→c7]
- **Aceptada**: queda {c7} ∈ F.

## Cadena `20000110100120`

- Inicio: {c0}
- Lee `2`: {c0} ⟶ {c0} [c0→c0]
- Lee `0`: {c0} ⟶ {c0} [c0→c0]
- Lee `0`: {c0} ⟶ {c0} [c0→c0]
- Lee `0`: {c0} ⟶ {c0} [c0→c0]
- Lee `0`: {c0} ⟶ {c0} [c0→c0]
- Lee `1`: {c0} ⟶ {c0, c1} [c0→c0, c0→c1] (bifurcación)
- Lee `1`: {c0, c1} ⟶ {c0, c1, c2} [c0→c0, c0→c1, c1→c2] (bifurcación)
- Lee `0`: {c0, c1, c2} ⟶ {c0, c3} [c0→c0, c2→c3]
- Lee `1`: {c0, c3} ⟶ {c0, c1, c4} [c0→c0, c0→c1, c3→c4] (bifurcación)
- Lee `0`: {c0, c1, c4} ⟶ {c0, c5} [c0→c0, c4→c5]
- Lee `0`: {c0, c5} ⟶ {c0, c6} [c0→c0, c5→c6]
- Lee `1`: {c0, c6} ⟶ {c0, c1, c7} [c0→c0, c0→c1, c6→c7] (bifurcación)
- Lee `2`: {c0, c1, c7} ⟶ {c0, c7} [c0→c0, c7→c7]
- Lee `0`: {c0, c7} ⟶ {c0, c7} [c0→c0, c7→c7]
- **Aceptada**: queda {c7} ∈ F.

## Cadena λ

- Inicio: {c0}
- **Rechazada**: ningún estado de {c0} es de aceptación.

## Cadena `2`

- Inicio: {c0}
- Lee `2`: {c0} ⟶ {c0} [c0→c0]
- **Rechazada**: ningún estado de {c0} es de aceptación.

## Cadena `210`

- Inicio: {c0}
- Lee `2`: {c0} ⟶ {c0} [c0→c0]
- Lee `1`: {c0} ⟶ {c0, c1} [c0→c0, c0→c1] (bifurcación)
- Lee `0`: {c0, c1} ⟶ {c0} [c0→c0]
- **Rechazada**: ningún estado de {c0} es de aceptación.

## Cadena `21220`

- Inicio: {c0}
- Lee `2`: {c0} ⟶ {c0} [c0→c0]
- Lee `1`: {c0} ⟶ {c0, c1} [c0→c0, c0→c1] (bifurcación)
- Lee `2`: {c0, c1} ⟶ {c0} [c0→c0]
- Lee `2`: {c0} ⟶ {c0} [c0→c0]
- Lee `0`: {c0} ⟶ {c0} [c0→c0]
- **Rechazada**: ningún estado de {c0} es de aceptación.

## Cadena `22110022`

- Inicio: {c0}
- Lee `2`: {c0} ⟶ {c0} [c0→c0]
- Lee `2`: {c0} ⟶ {c0} [c0→c0]
- Lee `1`: {c0} ⟶ {c0, c1} [c0→c0, c0→c1] (bifurcación)
- Lee `1`: {c0, c1} ⟶ {c0, c1, c2} [c0→c0, c0→c1, c1→c2] (bifurcación)
- Lee `0`: {c0, c1, c2} ⟶ {c0, c3} [c0→c0, c2→c3]
- Lee `0`: {c0, c3} ⟶ {c0} [c0→c0]
- Lee `2`: {c0} ⟶ {c0} [c0→c0]
- Lee `2`: {c0} ⟶ {c0} [c0→c0]
- **Rechazada**: ningún estado de {c0} es de aceptación.

## Cadena `221200`

- Inicio: {c0}
- Lee `2`: {c0} ⟶ {c0} [c0→c0]
- Lee `2`: {c0} ⟶ {c0} [c0→c0]
- Lee `1`: {c0} ⟶ {c0, c1} [c0→c0, c0→c1] (bifurcación)
- Lee `2`: {c0, c1} ⟶ {c0} [c0→c0]
- Lee `0`: {c0} ⟶ {c0} [c0→c0]
- Lee `0`: {c0} ⟶ {c0} [c0→c0]
- **Rechazada**: ningún estado de {c0} es de aceptación.
