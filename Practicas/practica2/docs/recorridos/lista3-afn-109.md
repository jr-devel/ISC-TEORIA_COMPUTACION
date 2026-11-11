# Recorridos: Lista 3 · AFN del problema 109

AFN para el problema 109: Las palabras de Σ2 que incluyen abbcb y cbaabb, que sí se pueden traslapar.

Autómata: `lista3-afn-109` (AFN).

## Cadena `cbaabbcb`

- Inicio: {c0c0}
- Lee `c`: {c0c0} ⟶ {c0c0, c0c1} [c0c0→c0c0, c0c0→c0c1] (bifurcación)
- Lee `b`: {c0c0, c0c1} ⟶ {c0c0, c0c2} [c0c0→c0c0, c0c1→c0c2]
- Lee `a`: {c0c0, c0c2} ⟶ {c0c0, c1c0, c0c3, c1c3} [c0c0→c0c0, c0c0→c1c0, c0c2→c0c3, c0c2→c1c3] (bifurcación)
- Lee `a`: {c0c0, c1c0, c0c3, c1c3} ⟶ {c0c0, c1c0, c0c4, c1c4} [c0c0→c0c0, c0c0→c1c0, c0c3→c0c4, c0c3→c1c4]
- Lee `b`: {c0c0, c1c0, c0c4, c1c4} ⟶ {c0c0, c2c0, c0c5, c2c5} [c0c0→c0c0, c0c4→c0c5, c1c0→c2c0, c1c4→c2c5]
- Lee `b`: {c0c0, c2c0, c0c5, c2c5} ⟶ {c0c0, c3c0, c0c6, c3c6} [c0c0→c0c0, c0c5→c0c6, c2c0→c3c0, c2c5→c3c6]
- Lee `c`: {c0c0, c3c0, c0c6, c3c6} ⟶ {c0c0, c0c1, c4c0, c4c1, c0c6, c4c6} [c0c0→c0c0, c0c0→c0c1, c0c6→c0c6, c3c0→c4c0, c3c0→c4c1, c3c6→c4c6] (bifurcación)
- Lee `b`: {c0c0, c0c1, c4c0, c4c1, c0c6, c4c6} ⟶ {c0c0, c0c2, c5c0, c5c2, c0c6, c5c6} [c0c0→c0c0, c0c1→c0c2, c0c6→c0c6, c4c0→c5c0, c4c1→c5c2, c4c6→c5c6]
- **Aceptada**: queda {c5c6} ∈ F.

## Cadena `acbaabbcb`

- Inicio: {c0c0}
- Lee `a`: {c0c0} ⟶ {c0c0, c1c0} [c0c0→c0c0, c0c0→c1c0] (bifurcación)
- Lee `c`: {c0c0, c1c0} ⟶ {c0c0, c0c1} [c0c0→c0c0, c0c0→c0c1]
- Lee `b`: {c0c0, c0c1} ⟶ {c0c0, c0c2} [c0c0→c0c0, c0c1→c0c2]
- Lee `a`: {c0c0, c0c2} ⟶ {c0c0, c1c0, c0c3, c1c3} [c0c0→c0c0, c0c0→c1c0, c0c2→c0c3, c0c2→c1c3] (bifurcación)
- Lee `a`: {c0c0, c1c0, c0c3, c1c3} ⟶ {c0c0, c1c0, c0c4, c1c4} [c0c0→c0c0, c0c0→c1c0, c0c3→c0c4, c0c3→c1c4]
- Lee `b`: {c0c0, c1c0, c0c4, c1c4} ⟶ {c0c0, c2c0, c0c5, c2c5} [c0c0→c0c0, c0c4→c0c5, c1c0→c2c0, c1c4→c2c5]
- Lee `b`: {c0c0, c2c0, c0c5, c2c5} ⟶ {c0c0, c3c0, c0c6, c3c6} [c0c0→c0c0, c0c5→c0c6, c2c0→c3c0, c2c5→c3c6]
- Lee `c`: {c0c0, c3c0, c0c6, c3c6} ⟶ {c0c0, c0c1, c4c0, c4c1, c0c6, c4c6} [c0c0→c0c0, c0c0→c0c1, c0c6→c0c6, c3c0→c4c0, c3c0→c4c1, c3c6→c4c6] (bifurcación)
- Lee `b`: {c0c0, c0c1, c4c0, c4c1, c0c6, c4c6} ⟶ {c0c0, c0c2, c5c0, c5c2, c0c6, c5c6} [c0c0→c0c0, c0c1→c0c2, c0c6→c0c6, c4c0→c5c0, c4c1→c5c2, c4c6→c5c6]
- **Aceptada**: queda {c5c6} ∈ F.

## Cadena `1acbaabbcba`

- Inicio: {c0c0}
- Lee `1`: {c0c0} ⟶ {c0c0} [c0c0→c0c0]
- Lee `a`: {c0c0} ⟶ {c0c0, c1c0} [c0c0→c0c0, c0c0→c1c0] (bifurcación)
- Lee `c`: {c0c0, c1c0} ⟶ {c0c0, c0c1} [c0c0→c0c0, c0c0→c0c1]
- Lee `b`: {c0c0, c0c1} ⟶ {c0c0, c0c2} [c0c0→c0c0, c0c1→c0c2]
- Lee `a`: {c0c0, c0c2} ⟶ {c0c0, c1c0, c0c3, c1c3} [c0c0→c0c0, c0c0→c1c0, c0c2→c0c3, c0c2→c1c3] (bifurcación)
- Lee `a`: {c0c0, c1c0, c0c3, c1c3} ⟶ {c0c0, c1c0, c0c4, c1c4} [c0c0→c0c0, c0c0→c1c0, c0c3→c0c4, c0c3→c1c4]
- Lee `b`: {c0c0, c1c0, c0c4, c1c4} ⟶ {c0c0, c2c0, c0c5, c2c5} [c0c0→c0c0, c0c4→c0c5, c1c0→c2c0, c1c4→c2c5]
- Lee `b`: {c0c0, c2c0, c0c5, c2c5} ⟶ {c0c0, c3c0, c0c6, c3c6} [c0c0→c0c0, c0c5→c0c6, c2c0→c3c0, c2c5→c3c6]
- Lee `c`: {c0c0, c3c0, c0c6, c3c6} ⟶ {c0c0, c0c1, c4c0, c4c1, c0c6, c4c6} [c0c0→c0c0, c0c0→c0c1, c0c6→c0c6, c3c0→c4c0, c3c0→c4c1, c3c6→c4c6] (bifurcación)
- Lee `b`: {c0c0, c0c1, c4c0, c4c1, c0c6, c4c6} ⟶ {c0c0, c0c2, c5c0, c5c2, c0c6, c5c6} [c0c0→c0c0, c0c1→c0c2, c0c6→c0c6, c4c0→c5c0, c4c1→c5c2, c4c6→c5c6]
- Lee `a`: {c0c0, c0c2, c5c0, c5c2, c0c6, c5c6} ⟶ {c0c0, c1c0, c0c3, c1c3, c5c0, c5c3, c0c6, c1c6, c5c6} [c0c0→c0c0, c0c0→c1c0, c0c2→c0c3, c0c2→c1c3, c0c6→c0c6, c0c6→c1c6, c5c0→c5c0, c5c2→c5c3, c5c6→c5c6] (bifurcación)
- **Aceptada**: queda {c5c6} ∈ F.

## Cadena `011cbaabbcbbb`

- Inicio: {c0c0}
- Lee `0`: {c0c0} ⟶ {c0c0} [c0c0→c0c0]
- Lee `1`: {c0c0} ⟶ {c0c0} [c0c0→c0c0]
- Lee `1`: {c0c0} ⟶ {c0c0} [c0c0→c0c0]
- Lee `c`: {c0c0} ⟶ {c0c0, c0c1} [c0c0→c0c0, c0c0→c0c1] (bifurcación)
- Lee `b`: {c0c0, c0c1} ⟶ {c0c0, c0c2} [c0c0→c0c0, c0c1→c0c2]
- Lee `a`: {c0c0, c0c2} ⟶ {c0c0, c1c0, c0c3, c1c3} [c0c0→c0c0, c0c0→c1c0, c0c2→c0c3, c0c2→c1c3] (bifurcación)
- Lee `a`: {c0c0, c1c0, c0c3, c1c3} ⟶ {c0c0, c1c0, c0c4, c1c4} [c0c0→c0c0, c0c0→c1c0, c0c3→c0c4, c0c3→c1c4]
- Lee `b`: {c0c0, c1c0, c0c4, c1c4} ⟶ {c0c0, c2c0, c0c5, c2c5} [c0c0→c0c0, c0c4→c0c5, c1c0→c2c0, c1c4→c2c5]
- Lee `b`: {c0c0, c2c0, c0c5, c2c5} ⟶ {c0c0, c3c0, c0c6, c3c6} [c0c0→c0c0, c0c5→c0c6, c2c0→c3c0, c2c5→c3c6]
- Lee `c`: {c0c0, c3c0, c0c6, c3c6} ⟶ {c0c0, c0c1, c4c0, c4c1, c0c6, c4c6} [c0c0→c0c0, c0c0→c0c1, c0c6→c0c6, c3c0→c4c0, c3c0→c4c1, c3c6→c4c6] (bifurcación)
- Lee `b`: {c0c0, c0c1, c4c0, c4c1, c0c6, c4c6} ⟶ {c0c0, c0c2, c5c0, c5c2, c0c6, c5c6} [c0c0→c0c0, c0c1→c0c2, c0c6→c0c6, c4c0→c5c0, c4c1→c5c2, c4c6→c5c6]
- Lee `b`: {c0c0, c0c2, c5c0, c5c2, c0c6, c5c6} ⟶ {c0c0, c5c0, c0c6, c5c6} [c0c0→c0c0, c0c6→c0c6, c5c0→c5c0, c5c6→c5c6]
- Lee `b`: {c0c0, c5c0, c0c6, c5c6} ⟶ {c0c0, c5c0, c0c6, c5c6} [c0c0→c0c0, c0c6→c0c6, c5c0→c5c0, c5c6→c5c6]
- **Aceptada**: queda {c5c6} ∈ F.

## Cadena `1a0c0cbaabbcba`

- Inicio: {c0c0}
- Lee `1`: {c0c0} ⟶ {c0c0} [c0c0→c0c0]
- Lee `a`: {c0c0} ⟶ {c0c0, c1c0} [c0c0→c0c0, c0c0→c1c0] (bifurcación)
- Lee `0`: {c0c0, c1c0} ⟶ {c0c0} [c0c0→c0c0]
- Lee `c`: {c0c0} ⟶ {c0c0, c0c1} [c0c0→c0c0, c0c0→c0c1] (bifurcación)
- Lee `0`: {c0c0, c0c1} ⟶ {c0c0} [c0c0→c0c0]
- Lee `c`: {c0c0} ⟶ {c0c0, c0c1} [c0c0→c0c0, c0c0→c0c1] (bifurcación)
- Lee `b`: {c0c0, c0c1} ⟶ {c0c0, c0c2} [c0c0→c0c0, c0c1→c0c2]
- Lee `a`: {c0c0, c0c2} ⟶ {c0c0, c1c0, c0c3, c1c3} [c0c0→c0c0, c0c0→c1c0, c0c2→c0c3, c0c2→c1c3] (bifurcación)
- Lee `a`: {c0c0, c1c0, c0c3, c1c3} ⟶ {c0c0, c1c0, c0c4, c1c4} [c0c0→c0c0, c0c0→c1c0, c0c3→c0c4, c0c3→c1c4]
- Lee `b`: {c0c0, c1c0, c0c4, c1c4} ⟶ {c0c0, c2c0, c0c5, c2c5} [c0c0→c0c0, c0c4→c0c5, c1c0→c2c0, c1c4→c2c5]
- Lee `b`: {c0c0, c2c0, c0c5, c2c5} ⟶ {c0c0, c3c0, c0c6, c3c6} [c0c0→c0c0, c0c5→c0c6, c2c0→c3c0, c2c5→c3c6]
- Lee `c`: {c0c0, c3c0, c0c6, c3c6} ⟶ {c0c0, c0c1, c4c0, c4c1, c0c6, c4c6} [c0c0→c0c0, c0c0→c0c1, c0c6→c0c6, c3c0→c4c0, c3c0→c4c1, c3c6→c4c6] (bifurcación)
- Lee `b`: {c0c0, c0c1, c4c0, c4c1, c0c6, c4c6} ⟶ {c0c0, c0c2, c5c0, c5c2, c0c6, c5c6} [c0c0→c0c0, c0c1→c0c2, c0c6→c0c6, c4c0→c5c0, c4c1→c5c2, c4c6→c5c6]
- Lee `a`: {c0c0, c0c2, c5c0, c5c2, c0c6, c5c6} ⟶ {c0c0, c1c0, c0c3, c1c3, c5c0, c5c3, c0c6, c1c6, c5c6} [c0c0→c0c0, c0c0→c1c0, c0c2→c0c3, c0c2→c1c3, c0c6→c0c6, c0c6→c1c6, c5c0→c5c0, c5c2→c5c3, c5c6→c5c6] (bifurcación)
- **Aceptada**: queda {c5c6} ∈ F.

## Cadena λ

- Inicio: {c0c0}
- **Rechazada**: ningún estado de {c0c0} es de aceptación.

## Cadena `a`

- Inicio: {c0c0}
- Lee `a`: {c0c0} ⟶ {c0c0, c1c0} [c0c0→c0c0, c0c0→c1c0] (bifurcación)
- **Rechazada**: ningún estado de {c0c0, c1c0} es de aceptación.

## Cadena `1ac`

- Inicio: {c0c0}
- Lee `1`: {c0c0} ⟶ {c0c0} [c0c0→c0c0]
- Lee `a`: {c0c0} ⟶ {c0c0, c1c0} [c0c0→c0c0, c0c0→c1c0] (bifurcación)
- Lee `c`: {c0c0, c1c0} ⟶ {c0c0, c0c1} [c0c0→c0c0, c0c0→c0c1]
- **Rechazada**: ningún estado de {c0c0, c0c1} es de aceptación.

## Cadena `1ab00`

- Inicio: {c0c0}
- Lee `1`: {c0c0} ⟶ {c0c0} [c0c0→c0c0]
- Lee `a`: {c0c0} ⟶ {c0c0, c1c0} [c0c0→c0c0, c0c0→c1c0] (bifurcación)
- Lee `b`: {c0c0, c1c0} ⟶ {c0c0, c2c0} [c0c0→c0c0, c1c0→c2c0]
- Lee `0`: {c0c0, c2c0} ⟶ {c0c0} [c0c0→c0c0]
- Lee `0`: {c0c0} ⟶ {c0c0} [c0c0→c0c0]
- **Rechazada**: ningún estado de {c0c0} es de aceptación.

## Cadena `cbaaac01`

- Inicio: {c0c0}
- Lee `c`: {c0c0} ⟶ {c0c0, c0c1} [c0c0→c0c0, c0c0→c0c1] (bifurcación)
- Lee `b`: {c0c0, c0c1} ⟶ {c0c0, c0c2} [c0c0→c0c0, c0c1→c0c2]
- Lee `a`: {c0c0, c0c2} ⟶ {c0c0, c1c0, c0c3, c1c3} [c0c0→c0c0, c0c0→c1c0, c0c2→c0c3, c0c2→c1c3] (bifurcación)
- Lee `a`: {c0c0, c1c0, c0c3, c1c3} ⟶ {c0c0, c1c0, c0c4, c1c4} [c0c0→c0c0, c0c0→c1c0, c0c3→c0c4, c0c3→c1c4]
- Lee `a`: {c0c0, c1c0, c0c4, c1c4} ⟶ {c0c0, c1c0} [c0c0→c0c0, c0c0→c1c0]
- Lee `c`: {c0c0, c1c0} ⟶ {c0c0, c0c1} [c0c0→c0c0, c0c0→c0c1]
- Lee `0`: {c0c0, c0c1} ⟶ {c0c0} [c0c0→c0c0]
- Lee `1`: {c0c0} ⟶ {c0c0} [c0c0→c0c0]
- **Rechazada**: ningún estado de {c0c0} es de aceptación.

## Cadena `abc0bca`

- Inicio: {c0c0}
- Lee `a`: {c0c0} ⟶ {c0c0, c1c0} [c0c0→c0c0, c0c0→c1c0] (bifurcación)
- Lee `b`: {c0c0, c1c0} ⟶ {c0c0, c2c0} [c0c0→c0c0, c1c0→c2c0]
- Lee `c`: {c0c0, c2c0} ⟶ {c0c0, c0c1} [c0c0→c0c0, c0c0→c0c1]
- Lee `0`: {c0c0, c0c1} ⟶ {c0c0} [c0c0→c0c0]
- Lee `b`: {c0c0} ⟶ {c0c0} [c0c0→c0c0]
- Lee `c`: {c0c0} ⟶ {c0c0, c0c1} [c0c0→c0c0, c0c0→c0c1] (bifurcación)
- Lee `a`: {c0c0, c0c1} ⟶ {c0c0, c1c0} [c0c0→c0c0, c0c0→c1c0]
- **Rechazada**: ningún estado de {c0c0, c1c0} es de aceptación.
