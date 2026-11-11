# Recorridos: Lista 3 · Ejercicio 189

AFN sobre {0, 1} para las palabras que contienen 00101 o 00110; recorrido de 1001011.

Autómata: `lista3-189` (AFN).

## Cadena `00110`

- Inicio: {i}
- Lee `0`: {i} ⟶ {i, c1} [i→c1, i→i] (bifurcación)
- Lee `0`: {i, c1} ⟶ {i, c1, c2} [c1→c2, i→c1, i→i] (bifurcación)
- Lee `1`: {i, c1, c2} ⟶ {i, c3} [c2→c3, i→i]
- Lee `1`: {i, c3} ⟶ {i, d4} [c3→d4, i→i]
- Lee `0`: {i, d4} ⟶ {i, c1, f} [d4→f, i→c1, i→i] (bifurcación)
- **Aceptada**: queda {f} ∈ F.

## Cadena `100110`

- Inicio: {i}
- Lee `1`: {i} ⟶ {i} [i→i]
- Lee `0`: {i} ⟶ {i, c1} [i→c1, i→i] (bifurcación)
- Lee `0`: {i, c1} ⟶ {i, c1, c2} [c1→c2, i→c1, i→i] (bifurcación)
- Lee `1`: {i, c1, c2} ⟶ {i, c3} [c2→c3, i→i]
- Lee `1`: {i, c3} ⟶ {i, d4} [c3→d4, i→i]
- Lee `0`: {i, d4} ⟶ {i, c1, f} [d4→f, i→c1, i→i] (bifurcación)
- **Aceptada**: queda {f} ∈ F.

## Cadena `00101100`

- Inicio: {i}
- Lee `0`: {i} ⟶ {i, c1} [i→c1, i→i] (bifurcación)
- Lee `0`: {i, c1} ⟶ {i, c1, c2} [c1→c2, i→c1, i→i] (bifurcación)
- Lee `1`: {i, c1, c2} ⟶ {i, c3} [c2→c3, i→i]
- Lee `0`: {i, c3} ⟶ {i, c1, u4} [c3→u4, i→c1, i→i] (bifurcación)
- Lee `1`: {i, c1, u4} ⟶ {i, f} [i→i, u4→f]
- Lee `1`: {i, f} ⟶ {i, f} [f→f, i→i]
- Lee `0`: {i, f} ⟶ {i, c1, f} [f→f, i→c1, i→i] (bifurcación)
- Lee `0`: {i, c1, f} ⟶ {i, c1, c2, f} [c1→c2, f→f, i→c1, i→i] (bifurcación)
- **Aceptada**: queda {f} ∈ F.

## Cadena `0100101101`

- Inicio: {i}
- Lee `0`: {i} ⟶ {i, c1} [i→c1, i→i] (bifurcación)
- Lee `1`: {i, c1} ⟶ {i} [i→i]
- Lee `0`: {i} ⟶ {i, c1} [i→c1, i→i] (bifurcación)
- Lee `0`: {i, c1} ⟶ {i, c1, c2} [c1→c2, i→c1, i→i] (bifurcación)
- Lee `1`: {i, c1, c2} ⟶ {i, c3} [c2→c3, i→i]
- Lee `0`: {i, c3} ⟶ {i, c1, u4} [c3→u4, i→c1, i→i] (bifurcación)
- Lee `1`: {i, c1, u4} ⟶ {i, f} [i→i, u4→f]
- Lee `1`: {i, f} ⟶ {i, f} [f→f, i→i]
- Lee `0`: {i, f} ⟶ {i, c1, f} [f→f, i→c1, i→i] (bifurcación)
- Lee `1`: {i, c1, f} ⟶ {i, f} [f→f, i→i]
- **Aceptada**: queda {f} ∈ F.

## Cadena `1001101110001`

- Inicio: {i}
- Lee `1`: {i} ⟶ {i} [i→i]
- Lee `0`: {i} ⟶ {i, c1} [i→c1, i→i] (bifurcación)
- Lee `0`: {i, c1} ⟶ {i, c1, c2} [c1→c2, i→c1, i→i] (bifurcación)
- Lee `1`: {i, c1, c2} ⟶ {i, c3} [c2→c3, i→i]
- Lee `1`: {i, c3} ⟶ {i, d4} [c3→d4, i→i]
- Lee `0`: {i, d4} ⟶ {i, c1, f} [d4→f, i→c1, i→i] (bifurcación)
- Lee `1`: {i, c1, f} ⟶ {i, f} [f→f, i→i]
- Lee `1`: {i, f} ⟶ {i, f} [f→f, i→i]
- Lee `1`: {i, f} ⟶ {i, f} [f→f, i→i]
- Lee `0`: {i, f} ⟶ {i, c1, f} [f→f, i→c1, i→i] (bifurcación)
- Lee `0`: {i, c1, f} ⟶ {i, c1, c2, f} [c1→c2, f→f, i→c1, i→i] (bifurcación)
- Lee `0`: {i, c1, c2, f} ⟶ {i, c1, c2, f} [c1→c2, f→f, i→c1, i→i]
- Lee `1`: {i, c1, c2, f} ⟶ {i, c3, f} [c2→c3, f→f, i→i]
- **Aceptada**: queda {f} ∈ F.

## Cadena λ

- Inicio: {i}
- **Rechazada**: ningún estado de {i} es de aceptación.

## Cadena `0`

- Inicio: {i}
- Lee `0`: {i} ⟶ {i, c1} [i→c1, i→i] (bifurcación)
- **Rechazada**: ningún estado de {i, c1} es de aceptación.

## Cadena `101`

- Inicio: {i}
- Lee `1`: {i} ⟶ {i} [i→i]
- Lee `0`: {i} ⟶ {i, c1} [i→c1, i→i] (bifurcación)
- Lee `1`: {i, c1} ⟶ {i} [i→i]
- **Rechazada**: ningún estado de {i} es de aceptación.

## Cadena `01101`

- Inicio: {i}
- Lee `0`: {i} ⟶ {i, c1} [i→c1, i→i] (bifurcación)
- Lee `1`: {i, c1} ⟶ {i} [i→i]
- Lee `1`: {i} ⟶ {i} [i→i]
- Lee `0`: {i} ⟶ {i, c1} [i→c1, i→i] (bifurcación)
- Lee `1`: {i, c1} ⟶ {i} [i→i]
- **Rechazada**: ningún estado de {i} es de aceptación.

## Cadena `01100000`

- Inicio: {i}
- Lee `0`: {i} ⟶ {i, c1} [i→c1, i→i] (bifurcación)
- Lee `1`: {i, c1} ⟶ {i} [i→i]
- Lee `1`: {i} ⟶ {i} [i→i]
- Lee `0`: {i} ⟶ {i, c1} [i→c1, i→i] (bifurcación)
- Lee `0`: {i, c1} ⟶ {i, c1, c2} [c1→c2, i→c1, i→i] (bifurcación)
- Lee `0`: {i, c1, c2} ⟶ {i, c1, c2} [c1→c2, i→c1, i→i]
- Lee `0`: {i, c1, c2} ⟶ {i, c1, c2} [c1→c2, i→c1, i→i]
- Lee `0`: {i, c1, c2} ⟶ {i, c1, c2} [c1→c2, i→c1, i→i]
- **Rechazada**: ningún estado de {i, c1, c2} es de aceptación.

## Cadena `00101`

- Inicio: {i}
- Lee `0`: {i} ⟶ {i, c1} [i→c1, i→i] (bifurcación)
- Lee `0`: {i, c1} ⟶ {i, c1, c2} [c1→c2, i→c1, i→i] (bifurcación)
- Lee `1`: {i, c1, c2} ⟶ {i, c3} [c2→c3, i→i]
- Lee `0`: {i, c3} ⟶ {i, c1, u4} [c3→u4, i→c1, i→i] (bifurcación)
- Lee `1`: {i, c1, u4} ⟶ {i, f} [i→i, u4→f]
- **Aceptada**: queda {f} ∈ F.

## Cadena `0110`

- Inicio: {i}
- Lee `0`: {i} ⟶ {i, c1} [i→c1, i→i] (bifurcación)
- Lee `1`: {i, c1} ⟶ {i} [i→i]
- Lee `1`: {i} ⟶ {i} [i→i]
- Lee `0`: {i} ⟶ {i, c1} [i→c1, i→i] (bifurcación)
- **Rechazada**: ningún estado de {i, c1} es de aceptación.
