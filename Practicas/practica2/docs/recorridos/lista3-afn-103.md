# Recorridos: Lista 3 · AFN del problema 103

AFN para el problema 103: Las palabras de Σ3 que contienen la cadena aabbba.

Autómata: `lista3-afn-103` (AFN).

## Cadena `aabbba`

- Inicio: {c0}
- Lee `a`: {c0} ⟶ {c0, c1} [c0→c0, c0→c1] (bifurcación)
- Lee `a`: {c0, c1} ⟶ {c0, c1, c2} [c0→c0, c0→c1, c1→c2] (bifurcación)
- Lee `b`: {c0, c1, c2} ⟶ {c0, c3} [c0→c0, c2→c3]
- Lee `b`: {c0, c3} ⟶ {c0, c4} [c0→c0, c3→c4]
- Lee `b`: {c0, c4} ⟶ {c0, c5} [c0→c0, c4→c5]
- Lee `a`: {c0, c5} ⟶ {c0, c1, c6} [c0→c0, c0→c1, c5→c6] (bifurcación)
- **Aceptada**: queda {c6} ∈ F.

## Cadena `baabbba`

- Inicio: {c0}
- Lee `b`: {c0} ⟶ {c0} [c0→c0]
- Lee `a`: {c0} ⟶ {c0, c1} [c0→c0, c0→c1] (bifurcación)
- Lee `a`: {c0, c1} ⟶ {c0, c1, c2} [c0→c0, c0→c1, c1→c2] (bifurcación)
- Lee `b`: {c0, c1, c2} ⟶ {c0, c3} [c0→c0, c2→c3]
- Lee `b`: {c0, c3} ⟶ {c0, c4} [c0→c0, c3→c4]
- Lee `b`: {c0, c4} ⟶ {c0, c5} [c0→c0, c4→c5]
- Lee `a`: {c0, c5} ⟶ {c0, c1, c6} [c0→c0, c0→c1, c5→c6] (bifurcación)
- **Aceptada**: queda {c6} ∈ F.

## Cadena `babaabbba`

- Inicio: {c0}
- Lee `b`: {c0} ⟶ {c0} [c0→c0]
- Lee `a`: {c0} ⟶ {c0, c1} [c0→c0, c0→c1] (bifurcación)
- Lee `b`: {c0, c1} ⟶ {c0} [c0→c0]
- Lee `a`: {c0} ⟶ {c0, c1} [c0→c0, c0→c1] (bifurcación)
- Lee `a`: {c0, c1} ⟶ {c0, c1, c2} [c0→c0, c0→c1, c1→c2] (bifurcación)
- Lee `b`: {c0, c1, c2} ⟶ {c0, c3} [c0→c0, c2→c3]
- Lee `b`: {c0, c3} ⟶ {c0, c4} [c0→c0, c3→c4]
- Lee `b`: {c0, c4} ⟶ {c0, c5} [c0→c0, c4→c5]
- Lee `a`: {c0, c5} ⟶ {c0, c1, c6} [c0→c0, c0→c1, c5→c6] (bifurcación)
- **Aceptada**: queda {c6} ∈ F.

## Cadena `ababaabbbaa`

- Inicio: {c0}
- Lee `a`: {c0} ⟶ {c0, c1} [c0→c0, c0→c1] (bifurcación)
- Lee `b`: {c0, c1} ⟶ {c0} [c0→c0]
- Lee `a`: {c0} ⟶ {c0, c1} [c0→c0, c0→c1] (bifurcación)
- Lee `b`: {c0, c1} ⟶ {c0} [c0→c0]
- Lee `a`: {c0} ⟶ {c0, c1} [c0→c0, c0→c1] (bifurcación)
- Lee `a`: {c0, c1} ⟶ {c0, c1, c2} [c0→c0, c0→c1, c1→c2] (bifurcación)
- Lee `b`: {c0, c1, c2} ⟶ {c0, c3} [c0→c0, c2→c3]
- Lee `b`: {c0, c3} ⟶ {c0, c4} [c0→c0, c3→c4]
- Lee `b`: {c0, c4} ⟶ {c0, c5} [c0→c0, c4→c5]
- Lee `a`: {c0, c5} ⟶ {c0, c1, c6} [c0→c0, c0→c1, c5→c6] (bifurcación)
- Lee `a`: {c0, c1, c6} ⟶ {c0, c1, c2, c6} [c0→c0, c0→c1, c1→c2, c6→c6] (bifurcación)
- **Aceptada**: queda {c6} ∈ F.

## Cadena `aaabbbaaaaabbb`

- Inicio: {c0}
- Lee `a`: {c0} ⟶ {c0, c1} [c0→c0, c0→c1] (bifurcación)
- Lee `a`: {c0, c1} ⟶ {c0, c1, c2} [c0→c0, c0→c1, c1→c2] (bifurcación)
- Lee `a`: {c0, c1, c2} ⟶ {c0, c1, c2} [c0→c0, c0→c1, c1→c2]
- Lee `b`: {c0, c1, c2} ⟶ {c0, c3} [c0→c0, c2→c3]
- Lee `b`: {c0, c3} ⟶ {c0, c4} [c0→c0, c3→c4]
- Lee `b`: {c0, c4} ⟶ {c0, c5} [c0→c0, c4→c5]
- Lee `a`: {c0, c5} ⟶ {c0, c1, c6} [c0→c0, c0→c1, c5→c6] (bifurcación)
- Lee `a`: {c0, c1, c6} ⟶ {c0, c1, c2, c6} [c0→c0, c0→c1, c1→c2, c6→c6] (bifurcación)
- Lee `a`: {c0, c1, c2, c6} ⟶ {c0, c1, c2, c6} [c0→c0, c0→c1, c1→c2, c6→c6]
- Lee `a`: {c0, c1, c2, c6} ⟶ {c0, c1, c2, c6} [c0→c0, c0→c1, c1→c2, c6→c6]
- Lee `a`: {c0, c1, c2, c6} ⟶ {c0, c1, c2, c6} [c0→c0, c0→c1, c1→c2, c6→c6]
- Lee `b`: {c0, c1, c2, c6} ⟶ {c0, c3, c6} [c0→c0, c2→c3, c6→c6]
- Lee `b`: {c0, c3, c6} ⟶ {c0, c4, c6} [c0→c0, c3→c4, c6→c6]
- Lee `b`: {c0, c4, c6} ⟶ {c0, c5, c6} [c0→c0, c4→c5, c6→c6]
- **Aceptada**: queda {c6} ∈ F.

## Cadena λ

- Inicio: {c0}
- **Rechazada**: ningún estado de {c0} es de aceptación.

## Cadena `a`

- Inicio: {c0}
- Lee `a`: {c0} ⟶ {c0, c1} [c0→c0, c0→c1] (bifurcación)
- **Rechazada**: ningún estado de {c0, c1} es de aceptación.

## Cadena `aaa`

- Inicio: {c0}
- Lee `a`: {c0} ⟶ {c0, c1} [c0→c0, c0→c1] (bifurcación)
- Lee `a`: {c0, c1} ⟶ {c0, c1, c2} [c0→c0, c0→c1, c1→c2] (bifurcación)
- Lee `a`: {c0, c1, c2} ⟶ {c0, c1, c2} [c0→c0, c0→c1, c1→c2]
- **Rechazada**: ningún estado de {c0, c1, c2} es de aceptación.

## Cadena `bbabb`

- Inicio: {c0}
- Lee `b`: {c0} ⟶ {c0} [c0→c0]
- Lee `b`: {c0} ⟶ {c0} [c0→c0]
- Lee `a`: {c0} ⟶ {c0, c1} [c0→c0, c0→c1] (bifurcación)
- Lee `b`: {c0, c1} ⟶ {c0} [c0→c0]
- Lee `b`: {c0} ⟶ {c0} [c0→c0]
- **Rechazada**: ningún estado de {c0} es de aceptación.

## Cadena `baabbaaa`

- Inicio: {c0}
- Lee `b`: {c0} ⟶ {c0} [c0→c0]
- Lee `a`: {c0} ⟶ {c0, c1} [c0→c0, c0→c1] (bifurcación)
- Lee `a`: {c0, c1} ⟶ {c0, c1, c2} [c0→c0, c0→c1, c1→c2] (bifurcación)
- Lee `b`: {c0, c1, c2} ⟶ {c0, c3} [c0→c0, c2→c3]
- Lee `b`: {c0, c3} ⟶ {c0, c4} [c0→c0, c3→c4]
- Lee `a`: {c0, c4} ⟶ {c0, c1} [c0→c0, c0→c1]
- Lee `a`: {c0, c1} ⟶ {c0, c1, c2} [c0→c0, c0→c1, c1→c2] (bifurcación)
- Lee `a`: {c0, c1, c2} ⟶ {c0, c1, c2} [c0→c0, c0→c1, c1→c2]
- **Rechazada**: ningún estado de {c0, c1, c2} es de aceptación.

## Cadena `ababb`

- Inicio: {c0}
- Lee `a`: {c0} ⟶ {c0, c1} [c0→c0, c0→c1] (bifurcación)
- Lee `b`: {c0, c1} ⟶ {c0} [c0→c0]
- Lee `a`: {c0} ⟶ {c0, c1} [c0→c0, c0→c1] (bifurcación)
- Lee `b`: {c0, c1} ⟶ {c0} [c0→c0]
- Lee `b`: {c0} ⟶ {c0} [c0→c0]
- **Rechazada**: ningún estado de {c0} es de aceptación.
