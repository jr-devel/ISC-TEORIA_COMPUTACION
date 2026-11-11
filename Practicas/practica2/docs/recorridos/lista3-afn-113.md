# Recorridos: Lista 3 · AFN del problema 113

AFN para el problema 113: Las palabras de Σ1 que contienen dos veces 010, que sí se pueden traslapar.

Autómata: `lista3-afn-113` (AFN).

## Cadena `01010`

- Inicio: {i}
- Lee `0`: {i} ⟶ {i, a1, o1} [i→a1, i→i, i→o1] (bifurcación)
- Lee `1`: {i, a1, o1} ⟶ {i, a2, o2} [a1→a2, i→i, o1→o2]
- Lee `0`: {i, a2, o2} ⟶ {i, a1, a3, o1, o3} [a2→a3, i→a1, i→i, i→o1, o2→o3] (bifurcación)
- Lee `1`: {i, a1, a3, o1, o3} ⟶ {i, a2, a3, o2, o4} [a1→a2, a3→a3, i→i, o1→o2, o3→o4]
- Lee `0`: {i, a2, a3, o2, o4} ⟶ {i, a1, a3, b1, b3, o1, o3} [a2→a3, a3→a3, a3→b1, i→a1, i→i, i→o1, o2→o3, o4→b3] (bifurcación)
- **Aceptada**: queda {b3} ∈ F.

## Cadena `010101`

- Inicio: {i}
- Lee `0`: {i} ⟶ {i, a1, o1} [i→a1, i→i, i→o1] (bifurcación)
- Lee `1`: {i, a1, o1} ⟶ {i, a2, o2} [a1→a2, i→i, o1→o2]
- Lee `0`: {i, a2, o2} ⟶ {i, a1, a3, o1, o3} [a2→a3, i→a1, i→i, i→o1, o2→o3] (bifurcación)
- Lee `1`: {i, a1, a3, o1, o3} ⟶ {i, a2, a3, o2, o4} [a1→a2, a3→a3, i→i, o1→o2, o3→o4]
- Lee `0`: {i, a2, a3, o2, o4} ⟶ {i, a1, a3, b1, b3, o1, o3} [a2→a3, a3→a3, a3→b1, i→a1, i→i, i→o1, o2→o3, o4→b3] (bifurcación)
- Lee `1`: {i, a1, a3, b1, b3, o1, o3} ⟶ {i, a2, a3, b2, b3, o2, o4} [a1→a2, a3→a3, b1→b2, b3→b3, i→i, o1→o2, o3→o4]
- **Aceptada**: queda {b3} ∈ F.

## Cadena `20101001`

- Inicio: {i}
- Lee `2`: {i} ⟶ {i} [i→i]
- Lee `0`: {i} ⟶ {i, a1, o1} [i→a1, i→i, i→o1] (bifurcación)
- Lee `1`: {i, a1, o1} ⟶ {i, a2, o2} [a1→a2, i→i, o1→o2]
- Lee `0`: {i, a2, o2} ⟶ {i, a1, a3, o1, o3} [a2→a3, i→a1, i→i, i→o1, o2→o3] (bifurcación)
- Lee `1`: {i, a1, a3, o1, o3} ⟶ {i, a2, a3, o2, o4} [a1→a2, a3→a3, i→i, o1→o2, o3→o4]
- Lee `0`: {i, a2, a3, o2, o4} ⟶ {i, a1, a3, b1, b3, o1, o3} [a2→a3, a3→a3, a3→b1, i→a1, i→i, i→o1, o2→o3, o4→b3] (bifurcación)
- Lee `0`: {i, a1, a3, b1, b3, o1, o3} ⟶ {i, a1, a3, b1, b3, o1} [a3→a3, a3→b1, b3→b3, i→a1, i→i, i→o1]
- Lee `1`: {i, a1, a3, b1, b3, o1} ⟶ {i, a2, a3, b2, b3, o2} [a1→a2, a3→a3, b1→b2, b3→b3, i→i, o1→o2]
- **Aceptada**: queda {b3} ∈ F.

## Cadena `0101020211`

- Inicio: {i}
- Lee `0`: {i} ⟶ {i, a1, o1} [i→a1, i→i, i→o1] (bifurcación)
- Lee `1`: {i, a1, o1} ⟶ {i, a2, o2} [a1→a2, i→i, o1→o2]
- Lee `0`: {i, a2, o2} ⟶ {i, a1, a3, o1, o3} [a2→a3, i→a1, i→i, i→o1, o2→o3] (bifurcación)
- Lee `1`: {i, a1, a3, o1, o3} ⟶ {i, a2, a3, o2, o4} [a1→a2, a3→a3, i→i, o1→o2, o3→o4]
- Lee `0`: {i, a2, a3, o2, o4} ⟶ {i, a1, a3, b1, b3, o1, o3} [a2→a3, a3→a3, a3→b1, i→a1, i→i, i→o1, o2→o3, o4→b3] (bifurcación)
- Lee `2`: {i, a1, a3, b1, b3, o1, o3} ⟶ {i, a3, b3} [a3→a3, b3→b3, i→i]
- Lee `0`: {i, a3, b3} ⟶ {i, a1, a3, b1, b3, o1} [a3→a3, a3→b1, b3→b3, i→a1, i→i, i→o1] (bifurcación)
- Lee `2`: {i, a1, a3, b1, b3, o1} ⟶ {i, a3, b3} [a3→a3, b3→b3, i→i]
- Lee `1`: {i, a3, b3} ⟶ {i, a3, b3} [a3→a3, b3→b3, i→i]
- Lee `1`: {i, a3, b3} ⟶ {i, a3, b3} [a3→a3, b3→b3, i→i]
- **Aceptada**: queda {b3} ∈ F.

## Cadena `2101022220102`

- Inicio: {i}
- Lee `2`: {i} ⟶ {i} [i→i]
- Lee `1`: {i} ⟶ {i} [i→i]
- Lee `0`: {i} ⟶ {i, a1, o1} [i→a1, i→i, i→o1] (bifurcación)
- Lee `1`: {i, a1, o1} ⟶ {i, a2, o2} [a1→a2, i→i, o1→o2]
- Lee `0`: {i, a2, o2} ⟶ {i, a1, a3, o1, o3} [a2→a3, i→a1, i→i, i→o1, o2→o3] (bifurcación)
- Lee `2`: {i, a1, a3, o1, o3} ⟶ {i, a3} [a3→a3, i→i]
- Lee `2`: {i, a3} ⟶ {i, a3} [a3→a3, i→i]
- Lee `2`: {i, a3} ⟶ {i, a3} [a3→a3, i→i]
- Lee `2`: {i, a3} ⟶ {i, a3} [a3→a3, i→i]
- Lee `0`: {i, a3} ⟶ {i, a1, a3, b1, o1} [a3→a3, a3→b1, i→a1, i→i, i→o1] (bifurcación)
- Lee `1`: {i, a1, a3, b1, o1} ⟶ {i, a2, a3, b2, o2} [a1→a2, a3→a3, b1→b2, i→i, o1→o2]
- Lee `0`: {i, a2, a3, b2, o2} ⟶ {i, a1, a3, b1, b3, o1, o3} [a2→a3, a3→a3, a3→b1, b2→b3, i→a1, i→i, i→o1, o2→o3] (bifurcación)
- Lee `2`: {i, a1, a3, b1, b3, o1, o3} ⟶ {i, a3, b3} [a3→a3, b3→b3, i→i]
- **Aceptada**: queda {b3} ∈ F.

## Cadena λ

- Inicio: {i}
- **Rechazada**: ningún estado de {i} es de aceptación.

## Cadena `0`

- Inicio: {i}
- Lee `0`: {i} ⟶ {i, a1, o1} [i→a1, i→i, i→o1] (bifurcación)
- **Rechazada**: ningún estado de {i, a1, o1} es de aceptación.

## Cadena `222`

- Inicio: {i}
- Lee `2`: {i} ⟶ {i} [i→i]
- Lee `2`: {i} ⟶ {i} [i→i]
- Lee `2`: {i} ⟶ {i} [i→i]
- **Rechazada**: ningún estado de {i} es de aceptación.

## Cadena `22201`

- Inicio: {i}
- Lee `2`: {i} ⟶ {i} [i→i]
- Lee `2`: {i} ⟶ {i} [i→i]
- Lee `2`: {i} ⟶ {i} [i→i]
- Lee `0`: {i} ⟶ {i, a1, o1} [i→a1, i→i, i→o1] (bifurcación)
- Lee `1`: {i, a1, o1} ⟶ {i, a2, o2} [a1→a2, i→i, o1→o2]
- **Rechazada**: ningún estado de {i, a2, o2} es de aceptación.

## Cadena `11210000`

- Inicio: {i}
- Lee `1`: {i} ⟶ {i} [i→i]
- Lee `1`: {i} ⟶ {i} [i→i]
- Lee `2`: {i} ⟶ {i} [i→i]
- Lee `1`: {i} ⟶ {i} [i→i]
- Lee `0`: {i} ⟶ {i, a1, o1} [i→a1, i→i, i→o1] (bifurcación)
- Lee `0`: {i, a1, o1} ⟶ {i, a1, o1} [i→a1, i→i, i→o1]
- Lee `0`: {i, a1, o1} ⟶ {i, a1, o1} [i→a1, i→i, i→o1]
- Lee `0`: {i, a1, o1} ⟶ {i, a1, o1} [i→a1, i→i, i→o1]
- **Rechazada**: ningún estado de {i, a1, o1} es de aceptación.

## Cadena `0111`

- Inicio: {i}
- Lee `0`: {i} ⟶ {i, a1, o1} [i→a1, i→i, i→o1] (bifurcación)
- Lee `1`: {i, a1, o1} ⟶ {i, a2, o2} [a1→a2, i→i, o1→o2]
- Lee `1`: {i, a2, o2} ⟶ {i} [i→i]
- Lee `1`: {i} ⟶ {i} [i→i]
- **Rechazada**: ningún estado de {i} es de aceptación.
