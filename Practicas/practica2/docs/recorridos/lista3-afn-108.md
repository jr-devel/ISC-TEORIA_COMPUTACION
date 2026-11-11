# Recorridos: Lista 3 · AFN del problema 108

AFN para el problema 108: Las palabras de Σ2 que incluyen abbcb y cbaabb sin traslaparse (abbcbaabb no pertenece).

Autómata: `lista3-afn-108` (AFN).

## Cadena `abbcbcbaabb`

- Inicio: {i}
- Lee `a`: {i} ⟶ {i, x1} [i→i, i→x1] (bifurcación)
- Lee `b`: {i, x1} ⟶ {i, x2} [i→i, x1→x2]
- Lee `b`: {i, x2} ⟶ {i, x3} [i→i, x2→x3]
- Lee `c`: {i, x3} ⟶ {i, x4, y1} [i→i, i→y1, x3→x4] (bifurcación)
- Lee `b`: {i, x4, y1} ⟶ {i, x5, y2} [i→i, x4→x5, y1→y2]
- Lee `c`: {i, x5, y2} ⟶ {i, x5, Y1, y1} [i→i, i→y1, x5→Y1, x5→x5] (bifurcación)
- Lee `b`: {i, x5, Y1, y1} ⟶ {i, x5, Y2, y2} [Y1→Y2, i→i, x5→x5, y1→y2]
- Lee `a`: {i, x5, Y2, y2} ⟶ {i, x1, x5, Y3, y3} [Y2→Y3, i→i, i→x1, x5→x5, y2→y3] (bifurcación)
- Lee `a`: {i, x1, x5, Y3, y3} ⟶ {i, x1, x5, Y4, y4} [Y3→Y4, i→i, i→x1, x5→x5, y3→y4]
- Lee `b`: {i, x1, x5, Y4, y4} ⟶ {i, x2, x5, Y5, y5} [Y4→Y5, i→i, x1→x2, x5→x5, y4→y5]
- Lee `b`: {i, x2, x5, Y5, y5} ⟶ {i, x3, x5, Y6, y6} [Y5→Y6, i→i, x2→x3, x5→x5, y5→y6]
- **Aceptada**: queda {Y6} ∈ F.

## Cadena `cbaabb1abbcb`

- Inicio: {i}
- Lee `c`: {i} ⟶ {i, y1} [i→i, i→y1] (bifurcación)
- Lee `b`: {i, y1} ⟶ {i, y2} [i→i, y1→y2]
- Lee `a`: {i, y2} ⟶ {i, x1, y3} [i→i, i→x1, y2→y3] (bifurcación)
- Lee `a`: {i, x1, y3} ⟶ {i, x1, y4} [i→i, i→x1, y3→y4]
- Lee `b`: {i, x1, y4} ⟶ {i, x2, y5} [i→i, x1→x2, y4→y5]
- Lee `b`: {i, x2, y5} ⟶ {i, x3, y6} [i→i, x2→x3, y5→y6]
- Lee `1`: {i, x3, y6} ⟶ {i, y6} [i→i, y6→y6]
- Lee `a`: {i, y6} ⟶ {i, x1, y6, X1} [i→i, i→x1, y6→X1, y6→y6] (bifurcación)
- Lee `b`: {i, x1, y6, X1} ⟶ {i, x2, y6, X2} [X1→X2, i→i, x1→x2, y6→y6]
- Lee `b`: {i, x2, y6, X2} ⟶ {i, x3, y6, X3} [X2→X3, i→i, x2→x3, y6→y6]
- Lee `c`: {i, x3, y6, X3} ⟶ {i, x4, y1, y6, X4} [X3→X4, i→i, i→y1, x3→x4, y6→y6] (bifurcación)
- Lee `b`: {i, x4, y1, y6, X4} ⟶ {i, x5, y2, y6, X5} [X4→X5, i→i, x4→x5, y1→y2, y6→y6]
- **Aceptada**: queda {X5} ∈ F.

## Cadena `a1abbcbcbaabba`

- Inicio: {i}
- Lee `a`: {i} ⟶ {i, x1} [i→i, i→x1] (bifurcación)
- Lee `1`: {i, x1} ⟶ {i} [i→i]
- Lee `a`: {i} ⟶ {i, x1} [i→i, i→x1] (bifurcación)
- Lee `b`: {i, x1} ⟶ {i, x2} [i→i, x1→x2]
- Lee `b`: {i, x2} ⟶ {i, x3} [i→i, x2→x3]
- Lee `c`: {i, x3} ⟶ {i, x4, y1} [i→i, i→y1, x3→x4] (bifurcación)
- Lee `b`: {i, x4, y1} ⟶ {i, x5, y2} [i→i, x4→x5, y1→y2]
- Lee `c`: {i, x5, y2} ⟶ {i, x5, Y1, y1} [i→i, i→y1, x5→Y1, x5→x5] (bifurcación)
- Lee `b`: {i, x5, Y1, y1} ⟶ {i, x5, Y2, y2} [Y1→Y2, i→i, x5→x5, y1→y2]
- Lee `a`: {i, x5, Y2, y2} ⟶ {i, x1, x5, Y3, y3} [Y2→Y3, i→i, i→x1, x5→x5, y2→y3] (bifurcación)
- Lee `a`: {i, x1, x5, Y3, y3} ⟶ {i, x1, x5, Y4, y4} [Y3→Y4, i→i, i→x1, x5→x5, y3→y4]
- Lee `b`: {i, x1, x5, Y4, y4} ⟶ {i, x2, x5, Y5, y5} [Y4→Y5, i→i, x1→x2, x5→x5, y4→y5]
- Lee `b`: {i, x2, x5, Y5, y5} ⟶ {i, x3, x5, Y6, y6} [Y5→Y6, i→i, x2→x3, x5→x5, y5→y6]
- Lee `a`: {i, x3, x5, Y6, y6} ⟶ {i, x1, x5, Y6, y6, X1} [Y6→Y6, i→i, i→x1, x5→x5, y6→X1, y6→y6] (bifurcación)
- **Aceptada**: queda {Y6} ∈ F.

## Cadena `cbaabb1abbcb0010`

- Inicio: {i}
- Lee `c`: {i} ⟶ {i, y1} [i→i, i→y1] (bifurcación)
- Lee `b`: {i, y1} ⟶ {i, y2} [i→i, y1→y2]
- Lee `a`: {i, y2} ⟶ {i, x1, y3} [i→i, i→x1, y2→y3] (bifurcación)
- Lee `a`: {i, x1, y3} ⟶ {i, x1, y4} [i→i, i→x1, y3→y4]
- Lee `b`: {i, x1, y4} ⟶ {i, x2, y5} [i→i, x1→x2, y4→y5]
- Lee `b`: {i, x2, y5} ⟶ {i, x3, y6} [i→i, x2→x3, y5→y6]
- Lee `1`: {i, x3, y6} ⟶ {i, y6} [i→i, y6→y6]
- Lee `a`: {i, y6} ⟶ {i, x1, y6, X1} [i→i, i→x1, y6→X1, y6→y6] (bifurcación)
- Lee `b`: {i, x1, y6, X1} ⟶ {i, x2, y6, X2} [X1→X2, i→i, x1→x2, y6→y6]
- Lee `b`: {i, x2, y6, X2} ⟶ {i, x3, y6, X3} [X2→X3, i→i, x2→x3, y6→y6]
- Lee `c`: {i, x3, y6, X3} ⟶ {i, x4, y1, y6, X4} [X3→X4, i→i, i→y1, x3→x4, y6→y6] (bifurcación)
- Lee `b`: {i, x4, y1, y6, X4} ⟶ {i, x5, y2, y6, X5} [X4→X5, i→i, x4→x5, y1→y2, y6→y6]
- Lee `0`: {i, x5, y2, y6, X5} ⟶ {i, x5, y6, X5} [X5→X5, i→i, x5→x5, y6→y6]
- Lee `0`: {i, x5, y6, X5} ⟶ {i, x5, y6, X5} [X5→X5, i→i, x5→x5, y6→y6]
- Lee `1`: {i, x5, y6, X5} ⟶ {i, x5, y6, X5} [X5→X5, i→i, x5→x5, y6→y6]
- Lee `0`: {i, x5, y6, X5} ⟶ {i, x5, y6, X5} [X5→X5, i→i, x5→x5, y6→y6]
- **Aceptada**: queda {X5} ∈ F.

## Cadena `1bbccbaabb0abbcba`

- Inicio: {i}
- Lee `1`: {i} ⟶ {i} [i→i]
- Lee `b`: {i} ⟶ {i} [i→i]
- Lee `b`: {i} ⟶ {i} [i→i]
- Lee `c`: {i} ⟶ {i, y1} [i→i, i→y1] (bifurcación)
- Lee `c`: {i, y1} ⟶ {i, y1} [i→i, i→y1]
- Lee `b`: {i, y1} ⟶ {i, y2} [i→i, y1→y2]
- Lee `a`: {i, y2} ⟶ {i, x1, y3} [i→i, i→x1, y2→y3] (bifurcación)
- Lee `a`: {i, x1, y3} ⟶ {i, x1, y4} [i→i, i→x1, y3→y4]
- Lee `b`: {i, x1, y4} ⟶ {i, x2, y5} [i→i, x1→x2, y4→y5]
- Lee `b`: {i, x2, y5} ⟶ {i, x3, y6} [i→i, x2→x3, y5→y6]
- Lee `0`: {i, x3, y6} ⟶ {i, y6} [i→i, y6→y6]
- Lee `a`: {i, y6} ⟶ {i, x1, y6, X1} [i→i, i→x1, y6→X1, y6→y6] (bifurcación)
- Lee `b`: {i, x1, y6, X1} ⟶ {i, x2, y6, X2} [X1→X2, i→i, x1→x2, y6→y6]
- Lee `b`: {i, x2, y6, X2} ⟶ {i, x3, y6, X3} [X2→X3, i→i, x2→x3, y6→y6]
- Lee `c`: {i, x3, y6, X3} ⟶ {i, x4, y1, y6, X4} [X3→X4, i→i, i→y1, x3→x4, y6→y6] (bifurcación)
- Lee `b`: {i, x4, y1, y6, X4} ⟶ {i, x5, y2, y6, X5} [X4→X5, i→i, x4→x5, y1→y2, y6→y6]
- Lee `a`: {i, x5, y2, y6, X5} ⟶ {i, x1, x5, y3, y6, X1, X5} [X5→X5, i→i, i→x1, x5→x5, y2→y3, y6→X1, y6→y6] (bifurcación)
- **Aceptada**: queda {X5} ∈ F.

## Cadena λ

- Inicio: {i}
- **Rechazada**: ningún estado de {i} es de aceptación.

## Cadena `c`

- Inicio: {i}
- Lee `c`: {i} ⟶ {i, y1} [i→i, i→y1] (bifurcación)
- **Rechazada**: ningún estado de {i, y1} es de aceptación.

## Cadena `1b0`

- Inicio: {i}
- Lee `1`: {i} ⟶ {i} [i→i]
- Lee `b`: {i} ⟶ {i} [i→i]
- Lee `0`: {i} ⟶ {i} [i→i]
- **Rechazada**: ningún estado de {i} es de aceptación.

## Cadena `cac1b`

- Inicio: {i}
- Lee `c`: {i} ⟶ {i, y1} [i→i, i→y1] (bifurcación)
- Lee `a`: {i, y1} ⟶ {i, x1} [i→i, i→x1]
- Lee `c`: {i, x1} ⟶ {i, y1} [i→i, i→y1]
- Lee `1`: {i, y1} ⟶ {i} [i→i]
- Lee `b`: {i} ⟶ {i} [i→i]
- **Rechazada**: ningún estado de {i} es de aceptación.

## Cadena `baa1a0aa`

- Inicio: {i}
- Lee `b`: {i} ⟶ {i} [i→i]
- Lee `a`: {i} ⟶ {i, x1} [i→i, i→x1] (bifurcación)
- Lee `a`: {i, x1} ⟶ {i, x1} [i→i, i→x1]
- Lee `1`: {i, x1} ⟶ {i} [i→i]
- Lee `a`: {i} ⟶ {i, x1} [i→i, i→x1] (bifurcación)
- Lee `0`: {i, x1} ⟶ {i} [i→i]
- Lee `a`: {i} ⟶ {i, x1} [i→i, i→x1] (bifurcación)
- Lee `a`: {i, x1} ⟶ {i, x1} [i→i, i→x1]
- **Rechazada**: ningún estado de {i, x1} es de aceptación.

## Cadena `0b0ac0b0ab`

- Inicio: {i}
- Lee `0`: {i} ⟶ {i} [i→i]
- Lee `b`: {i} ⟶ {i} [i→i]
- Lee `0`: {i} ⟶ {i} [i→i]
- Lee `a`: {i} ⟶ {i, x1} [i→i, i→x1] (bifurcación)
- Lee `c`: {i, x1} ⟶ {i, y1} [i→i, i→y1]
- Lee `0`: {i, y1} ⟶ {i} [i→i]
- Lee `b`: {i} ⟶ {i} [i→i]
- Lee `0`: {i} ⟶ {i} [i→i]
- Lee `a`: {i} ⟶ {i, x1} [i→i, i→x1] (bifurcación)
- Lee `b`: {i, x1} ⟶ {i, x2} [i→i, x1→x2]
- **Rechazada**: ningún estado de {i, x2} es de aceptación.
