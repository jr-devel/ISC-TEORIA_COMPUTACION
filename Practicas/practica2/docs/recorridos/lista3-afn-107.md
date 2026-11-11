# Recorridos: Lista 3 · AFN del problema 107

AFN para el problema 107: Las palabras de Σ1 que incluyen al menos una vez 0101 y al menos una vez 021.

Autómata: `lista3-afn-107` (AFN).

## Cadena `0101021`

- Inicio: {c0c0}
- Lee `0`: {c0c0} ⟶ {c0c0, c0c1, c1c0, c1c1} [c0c0→c0c0, c0c0→c0c1, c0c0→c1c0, c0c0→c1c1] (bifurcación)
- Lee `1`: {c0c0, c0c1, c1c0, c1c1} ⟶ {c0c0, c2c0} [c0c0→c0c0, c1c0→c2c0]
- Lee `0`: {c0c0, c2c0} ⟶ {c0c0, c0c1, c1c0, c1c1, c3c0, c3c1} [c0c0→c0c0, c0c0→c0c1, c0c0→c1c0, c0c0→c1c1, c2c0→c3c0, c2c0→c3c1] (bifurcación)
- Lee `1`: {c0c0, c0c1, c1c0, c1c1, c3c0, c3c1} ⟶ {c0c0, c2c0, c4c0} [c0c0→c0c0, c1c0→c2c0, c3c0→c4c0]
- Lee `0`: {c0c0, c2c0, c4c0} ⟶ {c0c0, c0c1, c1c0, c1c1, c3c0, c3c1, c4c0, c4c1} [c0c0→c0c0, c0c0→c0c1, c0c0→c1c0, c0c0→c1c1, c2c0→c3c0, c2c0→c3c1, c4c0→c4c0, c4c0→c4c1] (bifurcación)
- Lee `2`: {c0c0, c0c1, c1c0, c1c1, c3c0, c3c1, c4c0, c4c1} ⟶ {c0c0, c0c2, c4c0, c4c2} [c0c0→c0c0, c0c1→c0c2, c4c0→c4c0, c4c1→c4c2]
- Lee `1`: {c0c0, c0c2, c4c0, c4c2} ⟶ {c0c0, c0c3, c4c0, c4c3} [c0c0→c0c0, c0c2→c0c3, c4c0→c4c0, c4c2→c4c3]
- **Aceptada**: queda {c4c3} ∈ F.

## Cadena `20210101`

- Inicio: {c0c0}
- Lee `2`: {c0c0} ⟶ {c0c0} [c0c0→c0c0]
- Lee `0`: {c0c0} ⟶ {c0c0, c0c1, c1c0, c1c1} [c0c0→c0c0, c0c0→c0c1, c0c0→c1c0, c0c0→c1c1] (bifurcación)
- Lee `2`: {c0c0, c0c1, c1c0, c1c1} ⟶ {c0c0, c0c2} [c0c0→c0c0, c0c1→c0c2]
- Lee `1`: {c0c0, c0c2} ⟶ {c0c0, c0c3} [c0c0→c0c0, c0c2→c0c3]
- Lee `0`: {c0c0, c0c3} ⟶ {c0c0, c0c1, c1c0, c1c1, c0c3, c1c3} [c0c0→c0c0, c0c0→c0c1, c0c0→c1c0, c0c0→c1c1, c0c3→c0c3, c0c3→c1c3] (bifurcación)
- Lee `1`: {c0c0, c0c1, c1c0, c1c1, c0c3, c1c3} ⟶ {c0c0, c2c0, c0c3, c2c3} [c0c0→c0c0, c0c3→c0c3, c1c0→c2c0, c1c3→c2c3]
- Lee `0`: {c0c0, c2c0, c0c3, c2c3} ⟶ {c0c0, c0c1, c1c0, c1c1, c0c3, c3c0, c3c1, c1c3, c3c3} [c0c0→c0c0, c0c0→c0c1, c0c0→c1c0, c0c0→c1c1, c0c3→c0c3, c0c3→c1c3, c2c0→c3c0, c2c0→c3c1, c2c3→c3c3] (bifurcación)
- Lee `1`: {c0c0, c0c1, c1c0, c1c1, c0c3, c3c0, c3c1, c1c3, c3c3} ⟶ {c0c0, c2c0, c0c3, c4c0, c2c3, c4c3} [c0c0→c0c0, c0c3→c0c3, c1c0→c2c0, c1c3→c2c3, c3c0→c4c0, c3c3→c4c3]
- **Aceptada**: queda {c4c3} ∈ F.

## Cadena `0212100101`

- Inicio: {c0c0}
- Lee `0`: {c0c0} ⟶ {c0c0, c0c1, c1c0, c1c1} [c0c0→c0c0, c0c0→c0c1, c0c0→c1c0, c0c0→c1c1] (bifurcación)
- Lee `2`: {c0c0, c0c1, c1c0, c1c1} ⟶ {c0c0, c0c2} [c0c0→c0c0, c0c1→c0c2]
- Lee `1`: {c0c0, c0c2} ⟶ {c0c0, c0c3} [c0c0→c0c0, c0c2→c0c3]
- Lee `2`: {c0c0, c0c3} ⟶ {c0c0, c0c3} [c0c0→c0c0, c0c3→c0c3]
- Lee `1`: {c0c0, c0c3} ⟶ {c0c0, c0c3} [c0c0→c0c0, c0c3→c0c3]
- Lee `0`: {c0c0, c0c3} ⟶ {c0c0, c0c1, c1c0, c1c1, c0c3, c1c3} [c0c0→c0c0, c0c0→c0c1, c0c0→c1c0, c0c0→c1c1, c0c3→c0c3, c0c3→c1c3] (bifurcación)
- Lee `0`: {c0c0, c0c1, c1c0, c1c1, c0c3, c1c3} ⟶ {c0c0, c0c1, c1c0, c1c1, c0c3, c1c3} [c0c0→c0c0, c0c0→c0c1, c0c0→c1c0, c0c0→c1c1, c0c3→c0c3, c0c3→c1c3]
- Lee `1`: {c0c0, c0c1, c1c0, c1c1, c0c3, c1c3} ⟶ {c0c0, c2c0, c0c3, c2c3} [c0c0→c0c0, c0c3→c0c3, c1c0→c2c0, c1c3→c2c3]
- Lee `0`: {c0c0, c2c0, c0c3, c2c3} ⟶ {c0c0, c0c1, c1c0, c1c1, c0c3, c3c0, c3c1, c1c3, c3c3} [c0c0→c0c0, c0c0→c0c1, c0c0→c1c0, c0c0→c1c1, c0c3→c0c3, c0c3→c1c3, c2c0→c3c0, c2c0→c3c1, c2c3→c3c3] (bifurcación)
- Lee `1`: {c0c0, c0c1, c1c0, c1c1, c0c3, c3c0, c3c1, c1c3, c3c3} ⟶ {c0c0, c2c0, c0c3, c4c0, c2c3, c4c3} [c0c0→c0c0, c0c3→c0c3, c1c0→c2c0, c1c3→c2c3, c3c0→c4c0, c3c3→c4c3]
- **Aceptada**: queda {c4c3} ∈ F.

## Cadena `021112010101`

- Inicio: {c0c0}
- Lee `0`: {c0c0} ⟶ {c0c0, c0c1, c1c0, c1c1} [c0c0→c0c0, c0c0→c0c1, c0c0→c1c0, c0c0→c1c1] (bifurcación)
- Lee `2`: {c0c0, c0c1, c1c0, c1c1} ⟶ {c0c0, c0c2} [c0c0→c0c0, c0c1→c0c2]
- Lee `1`: {c0c0, c0c2} ⟶ {c0c0, c0c3} [c0c0→c0c0, c0c2→c0c3]
- Lee `1`: {c0c0, c0c3} ⟶ {c0c0, c0c3} [c0c0→c0c0, c0c3→c0c3]
- Lee `1`: {c0c0, c0c3} ⟶ {c0c0, c0c3} [c0c0→c0c0, c0c3→c0c3]
- Lee `2`: {c0c0, c0c3} ⟶ {c0c0, c0c3} [c0c0→c0c0, c0c3→c0c3]
- Lee `0`: {c0c0, c0c3} ⟶ {c0c0, c0c1, c1c0, c1c1, c0c3, c1c3} [c0c0→c0c0, c0c0→c0c1, c0c0→c1c0, c0c0→c1c1, c0c3→c0c3, c0c3→c1c3] (bifurcación)
- Lee `1`: {c0c0, c0c1, c1c0, c1c1, c0c3, c1c3} ⟶ {c0c0, c2c0, c0c3, c2c3} [c0c0→c0c0, c0c3→c0c3, c1c0→c2c0, c1c3→c2c3]
- Lee `0`: {c0c0, c2c0, c0c3, c2c3} ⟶ {c0c0, c0c1, c1c0, c1c1, c0c3, c3c0, c3c1, c1c3, c3c3} [c0c0→c0c0, c0c0→c0c1, c0c0→c1c0, c0c0→c1c1, c0c3→c0c3, c0c3→c1c3, c2c0→c3c0, c2c0→c3c1, c2c3→c3c3] (bifurcación)
- Lee `1`: {c0c0, c0c1, c1c0, c1c1, c0c3, c3c0, c3c1, c1c3, c3c3} ⟶ {c0c0, c2c0, c0c3, c4c0, c2c3, c4c3} [c0c0→c0c0, c0c3→c0c3, c1c0→c2c0, c1c3→c2c3, c3c0→c4c0, c3c3→c4c3]
- Lee `0`: {c0c0, c2c0, c0c3, c4c0, c2c3, c4c3} ⟶ {c0c0, c0c1, c1c0, c1c1, c0c3, c3c0, c3c1, c1c3, c4c0, c4c1, c3c3, c4c3} [c0c0→c0c0, c0c0→c0c1, c0c0→c1c0, c0c0→c1c1, c0c3→c0c3, c0c3→c1c3, c2c0→c3c0, c2c0→c3c1, c2c3→c3c3, c4c0→c4c0, c4c0→c4c1, c4c3→c4c3] (bifurcación)
- Lee `1`: {c0c0, c0c1, c1c0, c1c1, c0c3, c3c0, c3c1, c1c3, c4c0, c4c1, c3c3, c4c3} ⟶ {c0c0, c2c0, c0c3, c4c0, c2c3, c4c3} [c0c0→c0c0, c0c3→c0c3, c1c0→c2c0, c1c3→c2c3, c3c0→c4c0, c3c3→c4c3, c4c0→c4c0, c4c3→c4c3]
- **Aceptada**: queda {c4c3} ∈ F.

## Cadena `10202021010111`

- Inicio: {c0c0}
- Lee `1`: {c0c0} ⟶ {c0c0} [c0c0→c0c0]
- Lee `0`: {c0c0} ⟶ {c0c0, c0c1, c1c0, c1c1} [c0c0→c0c0, c0c0→c0c1, c0c0→c1c0, c0c0→c1c1] (bifurcación)
- Lee `2`: {c0c0, c0c1, c1c0, c1c1} ⟶ {c0c0, c0c2} [c0c0→c0c0, c0c1→c0c2]
- Lee `0`: {c0c0, c0c2} ⟶ {c0c0, c0c1, c1c0, c1c1} [c0c0→c0c0, c0c0→c0c1, c0c0→c1c0, c0c0→c1c1] (bifurcación)
- Lee `2`: {c0c0, c0c1, c1c0, c1c1} ⟶ {c0c0, c0c2} [c0c0→c0c0, c0c1→c0c2]
- Lee `0`: {c0c0, c0c2} ⟶ {c0c0, c0c1, c1c0, c1c1} [c0c0→c0c0, c0c0→c0c1, c0c0→c1c0, c0c0→c1c1] (bifurcación)
- Lee `2`: {c0c0, c0c1, c1c0, c1c1} ⟶ {c0c0, c0c2} [c0c0→c0c0, c0c1→c0c2]
- Lee `1`: {c0c0, c0c2} ⟶ {c0c0, c0c3} [c0c0→c0c0, c0c2→c0c3]
- Lee `0`: {c0c0, c0c3} ⟶ {c0c0, c0c1, c1c0, c1c1, c0c3, c1c3} [c0c0→c0c0, c0c0→c0c1, c0c0→c1c0, c0c0→c1c1, c0c3→c0c3, c0c3→c1c3] (bifurcación)
- Lee `1`: {c0c0, c0c1, c1c0, c1c1, c0c3, c1c3} ⟶ {c0c0, c2c0, c0c3, c2c3} [c0c0→c0c0, c0c3→c0c3, c1c0→c2c0, c1c3→c2c3]
- Lee `0`: {c0c0, c2c0, c0c3, c2c3} ⟶ {c0c0, c0c1, c1c0, c1c1, c0c3, c3c0, c3c1, c1c3, c3c3} [c0c0→c0c0, c0c0→c0c1, c0c0→c1c0, c0c0→c1c1, c0c3→c0c3, c0c3→c1c3, c2c0→c3c0, c2c0→c3c1, c2c3→c3c3] (bifurcación)
- Lee `1`: {c0c0, c0c1, c1c0, c1c1, c0c3, c3c0, c3c1, c1c3, c3c3} ⟶ {c0c0, c2c0, c0c3, c4c0, c2c3, c4c3} [c0c0→c0c0, c0c3→c0c3, c1c0→c2c0, c1c3→c2c3, c3c0→c4c0, c3c3→c4c3]
- Lee `1`: {c0c0, c2c0, c0c3, c4c0, c2c3, c4c3} ⟶ {c0c0, c0c3, c4c0, c4c3} [c0c0→c0c0, c0c3→c0c3, c4c0→c4c0, c4c3→c4c3]
- Lee `1`: {c0c0, c0c3, c4c0, c4c3} ⟶ {c0c0, c0c3, c4c0, c4c3} [c0c0→c0c0, c0c3→c0c3, c4c0→c4c0, c4c3→c4c3]
- **Aceptada**: queda {c4c3} ∈ F.

## Cadena λ

- Inicio: {c0c0}
- **Rechazada**: ningún estado de {c0c0} es de aceptación.

## Cadena `0`

- Inicio: {c0c0}
- Lee `0`: {c0c0} ⟶ {c0c0, c0c1, c1c0, c1c1} [c0c0→c0c0, c0c0→c0c1, c0c0→c1c0, c0c0→c1c1] (bifurcación)
- **Rechazada**: ningún estado de {c0c0, c0c1, c1c0, c1c1} es de aceptación.

## Cadena `201`

- Inicio: {c0c0}
- Lee `2`: {c0c0} ⟶ {c0c0} [c0c0→c0c0]
- Lee `0`: {c0c0} ⟶ {c0c0, c0c1, c1c0, c1c1} [c0c0→c0c0, c0c0→c0c1, c0c0→c1c0, c0c0→c1c1] (bifurcación)
- Lee `1`: {c0c0, c0c1, c1c0, c1c1} ⟶ {c0c0, c2c0} [c0c0→c0c0, c1c0→c2c0]
- **Rechazada**: ningún estado de {c0c0, c2c0} es de aceptación.

## Cadena `21202`

- Inicio: {c0c0}
- Lee `2`: {c0c0} ⟶ {c0c0} [c0c0→c0c0]
- Lee `1`: {c0c0} ⟶ {c0c0} [c0c0→c0c0]
- Lee `2`: {c0c0} ⟶ {c0c0} [c0c0→c0c0]
- Lee `0`: {c0c0} ⟶ {c0c0, c0c1, c1c0, c1c1} [c0c0→c0c0, c0c0→c0c1, c0c0→c1c0, c0c0→c1c1] (bifurcación)
- Lee `2`: {c0c0, c0c1, c1c0, c1c1} ⟶ {c0c0, c0c2} [c0c0→c0c0, c0c1→c0c2]
- **Rechazada**: ningún estado de {c0c0, c0c2} es de aceptación.

## Cadena `20001211`

- Inicio: {c0c0}
- Lee `2`: {c0c0} ⟶ {c0c0} [c0c0→c0c0]
- Lee `0`: {c0c0} ⟶ {c0c0, c0c1, c1c0, c1c1} [c0c0→c0c0, c0c0→c0c1, c0c0→c1c0, c0c0→c1c1] (bifurcación)
- Lee `0`: {c0c0, c0c1, c1c0, c1c1} ⟶ {c0c0, c0c1, c1c0, c1c1} [c0c0→c0c0, c0c0→c0c1, c0c0→c1c0, c0c0→c1c1]
- Lee `0`: {c0c0, c0c1, c1c0, c1c1} ⟶ {c0c0, c0c1, c1c0, c1c1} [c0c0→c0c0, c0c0→c0c1, c0c0→c1c0, c0c0→c1c1]
- Lee `1`: {c0c0, c0c1, c1c0, c1c1} ⟶ {c0c0, c2c0} [c0c0→c0c0, c1c0→c2c0]
- Lee `2`: {c0c0, c2c0} ⟶ {c0c0} [c0c0→c0c0]
- Lee `1`: {c0c0} ⟶ {c0c0} [c0c0→c0c0]
- Lee `1`: {c0c0} ⟶ {c0c0} [c0c0→c0c0]
- **Rechazada**: ningún estado de {c0c0} es de aceptación.

## Cadena `0210101`

- Inicio: {c0c0}
- Lee `0`: {c0c0} ⟶ {c0c0, c0c1, c1c0, c1c1} [c0c0→c0c0, c0c0→c0c1, c0c0→c1c0, c0c0→c1c1] (bifurcación)
- Lee `2`: {c0c0, c0c1, c1c0, c1c1} ⟶ {c0c0, c0c2} [c0c0→c0c0, c0c1→c0c2]
- Lee `1`: {c0c0, c0c2} ⟶ {c0c0, c0c3} [c0c0→c0c0, c0c2→c0c3]
- Lee `0`: {c0c0, c0c3} ⟶ {c0c0, c0c1, c1c0, c1c1, c0c3, c1c3} [c0c0→c0c0, c0c0→c0c1, c0c0→c1c0, c0c0→c1c1, c0c3→c0c3, c0c3→c1c3] (bifurcación)
- Lee `1`: {c0c0, c0c1, c1c0, c1c1, c0c3, c1c3} ⟶ {c0c0, c2c0, c0c3, c2c3} [c0c0→c0c0, c0c3→c0c3, c1c0→c2c0, c1c3→c2c3]
- Lee `0`: {c0c0, c2c0, c0c3, c2c3} ⟶ {c0c0, c0c1, c1c0, c1c1, c0c3, c3c0, c3c1, c1c3, c3c3} [c0c0→c0c0, c0c0→c0c1, c0c0→c1c0, c0c0→c1c1, c0c3→c0c3, c0c3→c1c3, c2c0→c3c0, c2c0→c3c1, c2c3→c3c3] (bifurcación)
- Lee `1`: {c0c0, c0c1, c1c0, c1c1, c0c3, c3c0, c3c1, c1c3, c3c3} ⟶ {c0c0, c2c0, c0c3, c4c0, c2c3, c4c3} [c0c0→c0c0, c0c3→c0c3, c1c0→c2c0, c1c3→c2c3, c3c0→c4c0, c3c3→c4c3]
- **Aceptada**: queda {c4c3} ∈ F.

## Cadena `101002`

- Inicio: {c0c0}
- Lee `1`: {c0c0} ⟶ {c0c0} [c0c0→c0c0]
- Lee `0`: {c0c0} ⟶ {c0c0, c0c1, c1c0, c1c1} [c0c0→c0c0, c0c0→c0c1, c0c0→c1c0, c0c0→c1c1] (bifurcación)
- Lee `1`: {c0c0, c0c1, c1c0, c1c1} ⟶ {c0c0, c2c0} [c0c0→c0c0, c1c0→c2c0]
- Lee `0`: {c0c0, c2c0} ⟶ {c0c0, c0c1, c1c0, c1c1, c3c0, c3c1} [c0c0→c0c0, c0c0→c0c1, c0c0→c1c0, c0c0→c1c1, c2c0→c3c0, c2c0→c3c1] (bifurcación)
- Lee `0`: {c0c0, c0c1, c1c0, c1c1, c3c0, c3c1} ⟶ {c0c0, c0c1, c1c0, c1c1} [c0c0→c0c0, c0c0→c0c1, c0c0→c1c0, c0c0→c1c1]
- Lee `2`: {c0c0, c0c1, c1c0, c1c1} ⟶ {c0c0, c0c2} [c0c0→c0c0, c0c1→c0c2]
- **Rechazada**: ningún estado de {c0c0, c0c2} es de aceptación.
