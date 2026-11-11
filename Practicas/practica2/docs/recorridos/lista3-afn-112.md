# Recorridos: Lista 3 · AFN del problema 112

AFN para el problema 112: Las palabras de Σ1 que contienen dos veces 010 sin traslaparse (01010 no pertenece, 010010 sí).

Autómata: `lista3-afn-112` (AFN).

## Cadena `010010`

- Inicio: {i}
- Lee `0`: {i} ⟶ {i, a1} [i→a1, i→i] (bifurcación)
- Lee `1`: {i, a1} ⟶ {i, a2} [a1→a2, i→i]
- Lee `0`: {i, a2} ⟶ {i, a1, a3} [a2→a3, i→a1, i→i] (bifurcación)
- Lee `0`: {i, a1, a3} ⟶ {i, a1, a3, b1} [a3→a3, a3→b1, i→a1, i→i] (bifurcación)
- Lee `1`: {i, a1, a3, b1} ⟶ {i, a2, a3, b2} [a1→a2, a3→a3, b1→b2, i→i]
- Lee `0`: {i, a2, a3, b2} ⟶ {i, a1, a3, b1, b3} [a2→a3, a3→a3, a3→b1, b2→b3, i→a1, i→i] (bifurcación)
- **Aceptada**: queda {b3} ∈ F.

## Cadena `0100010`

- Inicio: {i}
- Lee `0`: {i} ⟶ {i, a1} [i→a1, i→i] (bifurcación)
- Lee `1`: {i, a1} ⟶ {i, a2} [a1→a2, i→i]
- Lee `0`: {i, a2} ⟶ {i, a1, a3} [a2→a3, i→a1, i→i] (bifurcación)
- Lee `0`: {i, a1, a3} ⟶ {i, a1, a3, b1} [a3→a3, a3→b1, i→a1, i→i] (bifurcación)
- Lee `0`: {i, a1, a3, b1} ⟶ {i, a1, a3, b1} [a3→a3, a3→b1, i→a1, i→i]
- Lee `1`: {i, a1, a3, b1} ⟶ {i, a2, a3, b2} [a1→a2, a3→a3, b1→b2, i→i]
- Lee `0`: {i, a2, a3, b2} ⟶ {i, a1, a3, b1, b3} [a2→a3, a3→a3, a3→b1, b2→b3, i→a1, i→i] (bifurcación)
- **Aceptada**: queda {b3} ∈ F.

## Cadena `100100100`

- Inicio: {i}
- Lee `1`: {i} ⟶ {i} [i→i]
- Lee `0`: {i} ⟶ {i, a1} [i→a1, i→i] (bifurcación)
- Lee `0`: {i, a1} ⟶ {i, a1} [i→a1, i→i]
- Lee `1`: {i, a1} ⟶ {i, a2} [a1→a2, i→i]
- Lee `0`: {i, a2} ⟶ {i, a1, a3} [a2→a3, i→a1, i→i] (bifurcación)
- Lee `0`: {i, a1, a3} ⟶ {i, a1, a3, b1} [a3→a3, a3→b1, i→a1, i→i] (bifurcación)
- Lee `1`: {i, a1, a3, b1} ⟶ {i, a2, a3, b2} [a1→a2, a3→a3, b1→b2, i→i]
- Lee `0`: {i, a2, a3, b2} ⟶ {i, a1, a3, b1, b3} [a2→a3, a3→a3, a3→b1, b2→b3, i→a1, i→i] (bifurcación)
- Lee `0`: {i, a1, a3, b1, b3} ⟶ {i, a1, a3, b1, b3} [a3→a3, a3→b1, b3→b3, i→a1, i→i]
- **Aceptada**: queda {b3} ∈ F.

## Cadena `01022010022`

- Inicio: {i}
- Lee `0`: {i} ⟶ {i, a1} [i→a1, i→i] (bifurcación)
- Lee `1`: {i, a1} ⟶ {i, a2} [a1→a2, i→i]
- Lee `0`: {i, a2} ⟶ {i, a1, a3} [a2→a3, i→a1, i→i] (bifurcación)
- Lee `2`: {i, a1, a3} ⟶ {i, a3} [a3→a3, i→i]
- Lee `2`: {i, a3} ⟶ {i, a3} [a3→a3, i→i]
- Lee `0`: {i, a3} ⟶ {i, a1, a3, b1} [a3→a3, a3→b1, i→a1, i→i] (bifurcación)
- Lee `1`: {i, a1, a3, b1} ⟶ {i, a2, a3, b2} [a1→a2, a3→a3, b1→b2, i→i]
- Lee `0`: {i, a2, a3, b2} ⟶ {i, a1, a3, b1, b3} [a2→a3, a3→a3, a3→b1, b2→b3, i→a1, i→i] (bifurcación)
- Lee `0`: {i, a1, a3, b1, b3} ⟶ {i, a1, a3, b1, b3} [a3→a3, a3→b1, b3→b3, i→a1, i→i]
- Lee `2`: {i, a1, a3, b1, b3} ⟶ {i, a3, b3} [a3→a3, b3→b3, i→i]
- Lee `2`: {i, a3, b3} ⟶ {i, a3, b3} [a3→a3, b3→b3, i→i]
- **Aceptada**: queda {b3} ∈ F.

## Cadena `22120010010201`

- Inicio: {i}
- Lee `2`: {i} ⟶ {i} [i→i]
- Lee `2`: {i} ⟶ {i} [i→i]
- Lee `1`: {i} ⟶ {i} [i→i]
- Lee `2`: {i} ⟶ {i} [i→i]
- Lee `0`: {i} ⟶ {i, a1} [i→a1, i→i] (bifurcación)
- Lee `0`: {i, a1} ⟶ {i, a1} [i→a1, i→i]
- Lee `1`: {i, a1} ⟶ {i, a2} [a1→a2, i→i]
- Lee `0`: {i, a2} ⟶ {i, a1, a3} [a2→a3, i→a1, i→i] (bifurcación)
- Lee `0`: {i, a1, a3} ⟶ {i, a1, a3, b1} [a3→a3, a3→b1, i→a1, i→i] (bifurcación)
- Lee `1`: {i, a1, a3, b1} ⟶ {i, a2, a3, b2} [a1→a2, a3→a3, b1→b2, i→i]
- Lee `0`: {i, a2, a3, b2} ⟶ {i, a1, a3, b1, b3} [a2→a3, a3→a3, a3→b1, b2→b3, i→a1, i→i] (bifurcación)
- Lee `2`: {i, a1, a3, b1, b3} ⟶ {i, a3, b3} [a3→a3, b3→b3, i→i]
- Lee `0`: {i, a3, b3} ⟶ {i, a1, a3, b1, b3} [a3→a3, a3→b1, b3→b3, i→a1, i→i] (bifurcación)
- Lee `1`: {i, a1, a3, b1, b3} ⟶ {i, a2, a3, b2, b3} [a1→a2, a3→a3, b1→b2, b3→b3, i→i]
- **Aceptada**: queda {b3} ∈ F.

## Cadena λ

- Inicio: {i}
- **Rechazada**: ningún estado de {i} es de aceptación.

## Cadena `1`

- Inicio: {i}
- Lee `1`: {i} ⟶ {i} [i→i]
- **Rechazada**: ningún estado de {i} es de aceptación.

## Cadena `122`

- Inicio: {i}
- Lee `1`: {i} ⟶ {i} [i→i]
- Lee `2`: {i} ⟶ {i} [i→i]
- Lee `2`: {i} ⟶ {i} [i→i]
- **Rechazada**: ningún estado de {i} es de aceptación.

## Cadena `02122`

- Inicio: {i}
- Lee `0`: {i} ⟶ {i, a1} [i→a1, i→i] (bifurcación)
- Lee `2`: {i, a1} ⟶ {i} [i→i]
- Lee `1`: {i} ⟶ {i} [i→i]
- Lee `2`: {i} ⟶ {i} [i→i]
- Lee `2`: {i} ⟶ {i} [i→i]
- **Rechazada**: ningún estado de {i} es de aceptación.

## Cadena `22210211`

- Inicio: {i}
- Lee `2`: {i} ⟶ {i} [i→i]
- Lee `2`: {i} ⟶ {i} [i→i]
- Lee `2`: {i} ⟶ {i} [i→i]
- Lee `1`: {i} ⟶ {i} [i→i]
- Lee `0`: {i} ⟶ {i, a1} [i→a1, i→i] (bifurcación)
- Lee `2`: {i, a1} ⟶ {i} [i→i]
- Lee `1`: {i} ⟶ {i} [i→i]
- Lee `1`: {i} ⟶ {i} [i→i]
- **Rechazada**: ningún estado de {i} es de aceptación.

## Cadena `10002`

- Inicio: {i}
- Lee `1`: {i} ⟶ {i} [i→i]
- Lee `0`: {i} ⟶ {i, a1} [i→a1, i→i] (bifurcación)
- Lee `0`: {i, a1} ⟶ {i, a1} [i→a1, i→i]
- Lee `0`: {i, a1} ⟶ {i, a1} [i→a1, i→i]
- Lee `2`: {i, a1} ⟶ {i} [i→i]
- **Rechazada**: ningún estado de {i} es de aceptación.
