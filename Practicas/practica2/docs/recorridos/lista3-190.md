# Recorridos: Lista 3 · Ejercicio 190

AFN sobre {0, 1} para las palabras que contienen 11010 y 10100; recorrido de 01101010100.

Autómata: `lista3-190` (AFN).

## Cadena `110100`

- Inicio: {c0c0}
- Lee `1`: {c0c0} ⟶ {c0c0, c0c1, c1c0, c1c1} [c0c0→c0c0, c0c0→c0c1, c0c0→c1c0, c0c0→c1c1] (bifurcación)
- Lee `1`: {c0c0, c0c1, c1c0, c1c1} ⟶ {c0c0, c0c1, c1c0, c1c1, c2c0, c2c1} [c0c0→c0c0, c0c0→c0c1, c0c0→c1c0, c0c0→c1c1, c1c0→c2c0, c1c0→c2c1] (bifurcación)
- Lee `0`: {c0c0, c0c1, c1c0, c1c1, c2c0, c2c1} ⟶ {c0c0, c0c2, c3c0, c3c2} [c0c0→c0c0, c0c1→c0c2, c2c0→c3c0, c2c1→c3c2]
- Lee `1`: {c0c0, c0c2, c3c0, c3c2} ⟶ {c0c0, c0c1, c1c0, c1c1, c0c3, c1c3, c4c0, c4c1, c4c3} [c0c0→c0c0, c0c0→c0c1, c0c0→c1c0, c0c0→c1c1, c0c2→c0c3, c0c2→c1c3, c3c0→c4c0, c3c0→c4c1, c3c2→c4c3] (bifurcación)
- Lee `0`: {c0c0, c0c1, c1c0, c1c1, c0c3, c1c3, c4c0, c4c1, c4c3} ⟶ {c0c0, c0c2, c0c4, c5c0, c5c2, c5c4} [c0c0→c0c0, c0c1→c0c2, c0c3→c0c4, c4c0→c5c0, c4c1→c5c2, c4c3→c5c4]
- Lee `0`: {c0c0, c0c2, c0c4, c5c0, c5c2, c5c4} ⟶ {c0c0, c0c5, c5c0, c5c5} [c0c0→c0c0, c0c4→c0c5, c5c0→c5c0, c5c4→c5c5]
- **Aceptada**: queda {c5c5} ∈ F.

## Cadena `1101001`

- Inicio: {c0c0}
- Lee `1`: {c0c0} ⟶ {c0c0, c0c1, c1c0, c1c1} [c0c0→c0c0, c0c0→c0c1, c0c0→c1c0, c0c0→c1c1] (bifurcación)
- Lee `1`: {c0c0, c0c1, c1c0, c1c1} ⟶ {c0c0, c0c1, c1c0, c1c1, c2c0, c2c1} [c0c0→c0c0, c0c0→c0c1, c0c0→c1c0, c0c0→c1c1, c1c0→c2c0, c1c0→c2c1] (bifurcación)
- Lee `0`: {c0c0, c0c1, c1c0, c1c1, c2c0, c2c1} ⟶ {c0c0, c0c2, c3c0, c3c2} [c0c0→c0c0, c0c1→c0c2, c2c0→c3c0, c2c1→c3c2]
- Lee `1`: {c0c0, c0c2, c3c0, c3c2} ⟶ {c0c0, c0c1, c1c0, c1c1, c0c3, c1c3, c4c0, c4c1, c4c3} [c0c0→c0c0, c0c0→c0c1, c0c0→c1c0, c0c0→c1c1, c0c2→c0c3, c0c2→c1c3, c3c0→c4c0, c3c0→c4c1, c3c2→c4c3] (bifurcación)
- Lee `0`: {c0c0, c0c1, c1c0, c1c1, c0c3, c1c3, c4c0, c4c1, c4c3} ⟶ {c0c0, c0c2, c0c4, c5c0, c5c2, c5c4} [c0c0→c0c0, c0c1→c0c2, c0c3→c0c4, c4c0→c5c0, c4c1→c5c2, c4c3→c5c4]
- Lee `0`: {c0c0, c0c2, c0c4, c5c0, c5c2, c5c4} ⟶ {c0c0, c0c5, c5c0, c5c5} [c0c0→c0c0, c0c4→c0c5, c5c0→c5c0, c5c4→c5c5]
- Lee `1`: {c0c0, c0c5, c5c0, c5c5} ⟶ {c0c0, c0c1, c1c0, c1c1, c0c5, c5c0, c1c5, c5c1, c5c5} [c0c0→c0c0, c0c0→c0c1, c0c0→c1c0, c0c0→c1c1, c0c5→c0c5, c0c5→c1c5, c5c0→c5c0, c5c0→c5c1, c5c5→c5c5] (bifurcación)
- **Aceptada**: queda {c5c5} ∈ F.

## Cadena `110100010`

- Inicio: {c0c0}
- Lee `1`: {c0c0} ⟶ {c0c0, c0c1, c1c0, c1c1} [c0c0→c0c0, c0c0→c0c1, c0c0→c1c0, c0c0→c1c1] (bifurcación)
- Lee `1`: {c0c0, c0c1, c1c0, c1c1} ⟶ {c0c0, c0c1, c1c0, c1c1, c2c0, c2c1} [c0c0→c0c0, c0c0→c0c1, c0c0→c1c0, c0c0→c1c1, c1c0→c2c0, c1c0→c2c1] (bifurcación)
- Lee `0`: {c0c0, c0c1, c1c0, c1c1, c2c0, c2c1} ⟶ {c0c0, c0c2, c3c0, c3c2} [c0c0→c0c0, c0c1→c0c2, c2c0→c3c0, c2c1→c3c2]
- Lee `1`: {c0c0, c0c2, c3c0, c3c2} ⟶ {c0c0, c0c1, c1c0, c1c1, c0c3, c1c3, c4c0, c4c1, c4c3} [c0c0→c0c0, c0c0→c0c1, c0c0→c1c0, c0c0→c1c1, c0c2→c0c3, c0c2→c1c3, c3c0→c4c0, c3c0→c4c1, c3c2→c4c3] (bifurcación)
- Lee `0`: {c0c0, c0c1, c1c0, c1c1, c0c3, c1c3, c4c0, c4c1, c4c3} ⟶ {c0c0, c0c2, c0c4, c5c0, c5c2, c5c4} [c0c0→c0c0, c0c1→c0c2, c0c3→c0c4, c4c0→c5c0, c4c1→c5c2, c4c3→c5c4]
- Lee `0`: {c0c0, c0c2, c0c4, c5c0, c5c2, c5c4} ⟶ {c0c0, c0c5, c5c0, c5c5} [c0c0→c0c0, c0c4→c0c5, c5c0→c5c0, c5c4→c5c5]
- Lee `0`: {c0c0, c0c5, c5c0, c5c5} ⟶ {c0c0, c0c5, c5c0, c5c5} [c0c0→c0c0, c0c5→c0c5, c5c0→c5c0, c5c5→c5c5]
- Lee `1`: {c0c0, c0c5, c5c0, c5c5} ⟶ {c0c0, c0c1, c1c0, c1c1, c0c5, c5c0, c1c5, c5c1, c5c5} [c0c0→c0c0, c0c0→c0c1, c0c0→c1c0, c0c0→c1c1, c0c5→c0c5, c0c5→c1c5, c5c0→c5c0, c5c0→c5c1, c5c5→c5c5] (bifurcación)
- Lee `0`: {c0c0, c0c1, c1c0, c1c1, c0c5, c5c0, c1c5, c5c1, c5c5} ⟶ {c0c0, c0c2, c0c5, c5c0, c5c2, c5c5} [c0c0→c0c0, c0c1→c0c2, c0c5→c0c5, c5c0→c5c0, c5c1→c5c2, c5c5→c5c5]
- **Aceptada**: queda {c5c5} ∈ F.

## Cadena `01110100001`

- Inicio: {c0c0}
- Lee `0`: {c0c0} ⟶ {c0c0} [c0c0→c0c0]
- Lee `1`: {c0c0} ⟶ {c0c0, c0c1, c1c0, c1c1} [c0c0→c0c0, c0c0→c0c1, c0c0→c1c0, c0c0→c1c1] (bifurcación)
- Lee `1`: {c0c0, c0c1, c1c0, c1c1} ⟶ {c0c0, c0c1, c1c0, c1c1, c2c0, c2c1} [c0c0→c0c0, c0c0→c0c1, c0c0→c1c0, c0c0→c1c1, c1c0→c2c0, c1c0→c2c1] (bifurcación)
- Lee `1`: {c0c0, c0c1, c1c0, c1c1, c2c0, c2c1} ⟶ {c0c0, c0c1, c1c0, c1c1, c2c0, c2c1} [c0c0→c0c0, c0c0→c0c1, c0c0→c1c0, c0c0→c1c1, c1c0→c2c0, c1c0→c2c1]
- Lee `0`: {c0c0, c0c1, c1c0, c1c1, c2c0, c2c1} ⟶ {c0c0, c0c2, c3c0, c3c2} [c0c0→c0c0, c0c1→c0c2, c2c0→c3c0, c2c1→c3c2]
- Lee `1`: {c0c0, c0c2, c3c0, c3c2} ⟶ {c0c0, c0c1, c1c0, c1c1, c0c3, c1c3, c4c0, c4c1, c4c3} [c0c0→c0c0, c0c0→c0c1, c0c0→c1c0, c0c0→c1c1, c0c2→c0c3, c0c2→c1c3, c3c0→c4c0, c3c0→c4c1, c3c2→c4c3] (bifurcación)
- Lee `0`: {c0c0, c0c1, c1c0, c1c1, c0c3, c1c3, c4c0, c4c1, c4c3} ⟶ {c0c0, c0c2, c0c4, c5c0, c5c2, c5c4} [c0c0→c0c0, c0c1→c0c2, c0c3→c0c4, c4c0→c5c0, c4c1→c5c2, c4c3→c5c4]
- Lee `0`: {c0c0, c0c2, c0c4, c5c0, c5c2, c5c4} ⟶ {c0c0, c0c5, c5c0, c5c5} [c0c0→c0c0, c0c4→c0c5, c5c0→c5c0, c5c4→c5c5]
- Lee `0`: {c0c0, c0c5, c5c0, c5c5} ⟶ {c0c0, c0c5, c5c0, c5c5} [c0c0→c0c0, c0c5→c0c5, c5c0→c5c0, c5c5→c5c5]
- Lee `0`: {c0c0, c0c5, c5c0, c5c5} ⟶ {c0c0, c0c5, c5c0, c5c5} [c0c0→c0c0, c0c5→c0c5, c5c0→c5c0, c5c5→c5c5]
- Lee `1`: {c0c0, c0c5, c5c0, c5c5} ⟶ {c0c0, c0c1, c1c0, c1c1, c0c5, c5c0, c1c5, c5c1, c5c5} [c0c0→c0c0, c0c0→c0c1, c0c0→c1c0, c0c0→c1c1, c0c5→c0c5, c0c5→c1c5, c5c0→c5c0, c5c0→c5c1, c5c5→c5c5] (bifurcación)
- **Aceptada**: queda {c5c5} ∈ F.

## Cadena `01100001110100`

- Inicio: {c0c0}
- Lee `0`: {c0c0} ⟶ {c0c0} [c0c0→c0c0]
- Lee `1`: {c0c0} ⟶ {c0c0, c0c1, c1c0, c1c1} [c0c0→c0c0, c0c0→c0c1, c0c0→c1c0, c0c0→c1c1] (bifurcación)
- Lee `1`: {c0c0, c0c1, c1c0, c1c1} ⟶ {c0c0, c0c1, c1c0, c1c1, c2c0, c2c1} [c0c0→c0c0, c0c0→c0c1, c0c0→c1c0, c0c0→c1c1, c1c0→c2c0, c1c0→c2c1] (bifurcación)
- Lee `0`: {c0c0, c0c1, c1c0, c1c1, c2c0, c2c1} ⟶ {c0c0, c0c2, c3c0, c3c2} [c0c0→c0c0, c0c1→c0c2, c2c0→c3c0, c2c1→c3c2]
- Lee `0`: {c0c0, c0c2, c3c0, c3c2} ⟶ {c0c0} [c0c0→c0c0]
- Lee `0`: {c0c0} ⟶ {c0c0} [c0c0→c0c0]
- Lee `0`: {c0c0} ⟶ {c0c0} [c0c0→c0c0]
- Lee `1`: {c0c0} ⟶ {c0c0, c0c1, c1c0, c1c1} [c0c0→c0c0, c0c0→c0c1, c0c0→c1c0, c0c0→c1c1] (bifurcación)
- Lee `1`: {c0c0, c0c1, c1c0, c1c1} ⟶ {c0c0, c0c1, c1c0, c1c1, c2c0, c2c1} [c0c0→c0c0, c0c0→c0c1, c0c0→c1c0, c0c0→c1c1, c1c0→c2c0, c1c0→c2c1] (bifurcación)
- Lee `1`: {c0c0, c0c1, c1c0, c1c1, c2c0, c2c1} ⟶ {c0c0, c0c1, c1c0, c1c1, c2c0, c2c1} [c0c0→c0c0, c0c0→c0c1, c0c0→c1c0, c0c0→c1c1, c1c0→c2c0, c1c0→c2c1]
- Lee `0`: {c0c0, c0c1, c1c0, c1c1, c2c0, c2c1} ⟶ {c0c0, c0c2, c3c0, c3c2} [c0c0→c0c0, c0c1→c0c2, c2c0→c3c0, c2c1→c3c2]
- Lee `1`: {c0c0, c0c2, c3c0, c3c2} ⟶ {c0c0, c0c1, c1c0, c1c1, c0c3, c1c3, c4c0, c4c1, c4c3} [c0c0→c0c0, c0c0→c0c1, c0c0→c1c0, c0c0→c1c1, c0c2→c0c3, c0c2→c1c3, c3c0→c4c0, c3c0→c4c1, c3c2→c4c3] (bifurcación)
- Lee `0`: {c0c0, c0c1, c1c0, c1c1, c0c3, c1c3, c4c0, c4c1, c4c3} ⟶ {c0c0, c0c2, c0c4, c5c0, c5c2, c5c4} [c0c0→c0c0, c0c1→c0c2, c0c3→c0c4, c4c0→c5c0, c4c1→c5c2, c4c3→c5c4]
- Lee `0`: {c0c0, c0c2, c0c4, c5c0, c5c2, c5c4} ⟶ {c0c0, c0c5, c5c0, c5c5} [c0c0→c0c0, c0c4→c0c5, c5c0→c5c0, c5c4→c5c5]
- **Aceptada**: queda {c5c5} ∈ F.

## Cadena λ

- Inicio: {c0c0}
- **Rechazada**: ningún estado de {c0c0} es de aceptación.

## Cadena `0`

- Inicio: {c0c0}
- Lee `0`: {c0c0} ⟶ {c0c0} [c0c0→c0c0]
- **Rechazada**: ningún estado de {c0c0} es de aceptación.

## Cadena `001`

- Inicio: {c0c0}
- Lee `0`: {c0c0} ⟶ {c0c0} [c0c0→c0c0]
- Lee `0`: {c0c0} ⟶ {c0c0} [c0c0→c0c0]
- Lee `1`: {c0c0} ⟶ {c0c0, c0c1, c1c0, c1c1} [c0c0→c0c0, c0c0→c0c1, c0c0→c1c0, c0c0→c1c1] (bifurcación)
- **Rechazada**: ningún estado de {c0c0, c0c1, c1c0, c1c1} es de aceptación.

## Cadena `01011`

- Inicio: {c0c0}
- Lee `0`: {c0c0} ⟶ {c0c0} [c0c0→c0c0]
- Lee `1`: {c0c0} ⟶ {c0c0, c0c1, c1c0, c1c1} [c0c0→c0c0, c0c0→c0c1, c0c0→c1c0, c0c0→c1c1] (bifurcación)
- Lee `0`: {c0c0, c0c1, c1c0, c1c1} ⟶ {c0c0, c0c2} [c0c0→c0c0, c0c1→c0c2]
- Lee `1`: {c0c0, c0c2} ⟶ {c0c0, c0c1, c1c0, c1c1, c0c3, c1c3} [c0c0→c0c0, c0c0→c0c1, c0c0→c1c0, c0c0→c1c1, c0c2→c0c3, c0c2→c1c3] (bifurcación)
- Lee `1`: {c0c0, c0c1, c1c0, c1c1, c0c3, c1c3} ⟶ {c0c0, c0c1, c1c0, c1c1, c2c0, c2c1} [c0c0→c0c0, c0c0→c0c1, c0c0→c1c0, c0c0→c1c1, c1c0→c2c0, c1c0→c2c1]
- **Rechazada**: ningún estado de {c0c0, c0c1, c1c0, c1c1, c2c0, c2c1} es de aceptación.

## Cadena `01011001`

- Inicio: {c0c0}
- Lee `0`: {c0c0} ⟶ {c0c0} [c0c0→c0c0]
- Lee `1`: {c0c0} ⟶ {c0c0, c0c1, c1c0, c1c1} [c0c0→c0c0, c0c0→c0c1, c0c0→c1c0, c0c0→c1c1] (bifurcación)
- Lee `0`: {c0c0, c0c1, c1c0, c1c1} ⟶ {c0c0, c0c2} [c0c0→c0c0, c0c1→c0c2]
- Lee `1`: {c0c0, c0c2} ⟶ {c0c0, c0c1, c1c0, c1c1, c0c3, c1c3} [c0c0→c0c0, c0c0→c0c1, c0c0→c1c0, c0c0→c1c1, c0c2→c0c3, c0c2→c1c3] (bifurcación)
- Lee `1`: {c0c0, c0c1, c1c0, c1c1, c0c3, c1c3} ⟶ {c0c0, c0c1, c1c0, c1c1, c2c0, c2c1} [c0c0→c0c0, c0c0→c0c1, c0c0→c1c0, c0c0→c1c1, c1c0→c2c0, c1c0→c2c1]
- Lee `0`: {c0c0, c0c1, c1c0, c1c1, c2c0, c2c1} ⟶ {c0c0, c0c2, c3c0, c3c2} [c0c0→c0c0, c0c1→c0c2, c2c0→c3c0, c2c1→c3c2]
- Lee `0`: {c0c0, c0c2, c3c0, c3c2} ⟶ {c0c0} [c0c0→c0c0]
- Lee `1`: {c0c0} ⟶ {c0c0, c0c1, c1c0, c1c1} [c0c0→c0c0, c0c0→c0c1, c0c0→c1c0, c0c0→c1c1] (bifurcación)
- **Rechazada**: ningún estado de {c0c0, c0c1, c1c0, c1c1} es de aceptación.

## Cadena `00010`

- Inicio: {c0c0}
- Lee `0`: {c0c0} ⟶ {c0c0} [c0c0→c0c0]
- Lee `0`: {c0c0} ⟶ {c0c0} [c0c0→c0c0]
- Lee `0`: {c0c0} ⟶ {c0c0} [c0c0→c0c0]
- Lee `1`: {c0c0} ⟶ {c0c0, c0c1, c1c0, c1c1} [c0c0→c0c0, c0c0→c0c1, c0c0→c1c0, c0c0→c1c1] (bifurcación)
- Lee `0`: {c0c0, c0c1, c1c0, c1c1} ⟶ {c0c0, c0c2} [c0c0→c0c0, c0c1→c0c2]
- **Rechazada**: ningún estado de {c0c0, c0c2} es de aceptación.
