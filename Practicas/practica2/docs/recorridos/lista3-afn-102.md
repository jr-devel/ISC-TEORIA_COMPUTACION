# Recorridos: Lista 3 · AFN del problema 102

AFN para el problema 102: Las palabras de Σ3 que contienen la cadena abbbab.

Autómata: `lista3-afn-102` (AFN).

## Cadena `abbbab`

- Inicio: {c0}
- Lee `a`: {c0} ⟶ {c0, c1} [c0→c0, c0→c1] (bifurcación)
- Lee `b`: {c0, c1} ⟶ {c0, c2} [c0→c0, c1→c2]
- Lee `b`: {c0, c2} ⟶ {c0, c3} [c0→c0, c2→c3]
- Lee `b`: {c0, c3} ⟶ {c0, c4} [c0→c0, c3→c4]
- Lee `a`: {c0, c4} ⟶ {c0, c1, c5} [c0→c0, c0→c1, c4→c5] (bifurcación)
- Lee `b`: {c0, c1, c5} ⟶ {c0, c2, c6} [c0→c0, c1→c2, c5→c6]
- **Aceptada**: queda {c6} ∈ F.

## Cadena `abbbabb`

- Inicio: {c0}
- Lee `a`: {c0} ⟶ {c0, c1} [c0→c0, c0→c1] (bifurcación)
- Lee `b`: {c0, c1} ⟶ {c0, c2} [c0→c0, c1→c2]
- Lee `b`: {c0, c2} ⟶ {c0, c3} [c0→c0, c2→c3]
- Lee `b`: {c0, c3} ⟶ {c0, c4} [c0→c0, c3→c4]
- Lee `a`: {c0, c4} ⟶ {c0, c1, c5} [c0→c0, c0→c1, c4→c5] (bifurcación)
- Lee `b`: {c0, c1, c5} ⟶ {c0, c2, c6} [c0→c0, c1→c2, c5→c6]
- Lee `b`: {c0, c2, c6} ⟶ {c0, c3, c6} [c0→c0, c2→c3, c6→c6]
- **Aceptada**: queda {c6} ∈ F.

## Cadena `abbbabaaa`

- Inicio: {c0}
- Lee `a`: {c0} ⟶ {c0, c1} [c0→c0, c0→c1] (bifurcación)
- Lee `b`: {c0, c1} ⟶ {c0, c2} [c0→c0, c1→c2]
- Lee `b`: {c0, c2} ⟶ {c0, c3} [c0→c0, c2→c3]
- Lee `b`: {c0, c3} ⟶ {c0, c4} [c0→c0, c3→c4]
- Lee `a`: {c0, c4} ⟶ {c0, c1, c5} [c0→c0, c0→c1, c4→c5] (bifurcación)
- Lee `b`: {c0, c1, c5} ⟶ {c0, c2, c6} [c0→c0, c1→c2, c5→c6]
- Lee `a`: {c0, c2, c6} ⟶ {c0, c1, c6} [c0→c0, c0→c1, c6→c6]
- Lee `a`: {c0, c1, c6} ⟶ {c0, c1, c6} [c0→c0, c0→c1, c6→c6]
- Lee `a`: {c0, c1, c6} ⟶ {c0, c1, c6} [c0→c0, c0→c1, c6→c6]
- **Aceptada**: queda {c6} ∈ F.

## Cadena `abbaabbbaba`

- Inicio: {c0}
- Lee `a`: {c0} ⟶ {c0, c1} [c0→c0, c0→c1] (bifurcación)
- Lee `b`: {c0, c1} ⟶ {c0, c2} [c0→c0, c1→c2]
- Lee `b`: {c0, c2} ⟶ {c0, c3} [c0→c0, c2→c3]
- Lee `a`: {c0, c3} ⟶ {c0, c1} [c0→c0, c0→c1]
- Lee `a`: {c0, c1} ⟶ {c0, c1} [c0→c0, c0→c1]
- Lee `b`: {c0, c1} ⟶ {c0, c2} [c0→c0, c1→c2]
- Lee `b`: {c0, c2} ⟶ {c0, c3} [c0→c0, c2→c3]
- Lee `b`: {c0, c3} ⟶ {c0, c4} [c0→c0, c3→c4]
- Lee `a`: {c0, c4} ⟶ {c0, c1, c5} [c0→c0, c0→c1, c4→c5] (bifurcación)
- Lee `b`: {c0, c1, c5} ⟶ {c0, c2, c6} [c0→c0, c1→c2, c5→c6]
- Lee `a`: {c0, c2, c6} ⟶ {c0, c1, c6} [c0→c0, c0→c1, c6→c6]
- **Aceptada**: queda {c6} ∈ F.

## Cadena `bbbabbbabbbbaa`

- Inicio: {c0}
- Lee `b`: {c0} ⟶ {c0} [c0→c0]
- Lee `b`: {c0} ⟶ {c0} [c0→c0]
- Lee `b`: {c0} ⟶ {c0} [c0→c0]
- Lee `a`: {c0} ⟶ {c0, c1} [c0→c0, c0→c1] (bifurcación)
- Lee `b`: {c0, c1} ⟶ {c0, c2} [c0→c0, c1→c2]
- Lee `b`: {c0, c2} ⟶ {c0, c3} [c0→c0, c2→c3]
- Lee `b`: {c0, c3} ⟶ {c0, c4} [c0→c0, c3→c4]
- Lee `a`: {c0, c4} ⟶ {c0, c1, c5} [c0→c0, c0→c1, c4→c5] (bifurcación)
- Lee `b`: {c0, c1, c5} ⟶ {c0, c2, c6} [c0→c0, c1→c2, c5→c6]
- Lee `b`: {c0, c2, c6} ⟶ {c0, c3, c6} [c0→c0, c2→c3, c6→c6]
- Lee `b`: {c0, c3, c6} ⟶ {c0, c4, c6} [c0→c0, c3→c4, c6→c6]
- Lee `b`: {c0, c4, c6} ⟶ {c0, c6} [c0→c0, c6→c6]
- Lee `a`: {c0, c6} ⟶ {c0, c1, c6} [c0→c0, c0→c1, c6→c6] (bifurcación)
- Lee `a`: {c0, c1, c6} ⟶ {c0, c1, c6} [c0→c0, c0→c1, c6→c6]
- **Aceptada**: queda {c6} ∈ F.

## Cadena λ

- Inicio: {c0}
- **Rechazada**: ningún estado de {c0} es de aceptación.

## Cadena `a`

- Inicio: {c0}
- Lee `a`: {c0} ⟶ {c0, c1} [c0→c0, c0→c1] (bifurcación)
- **Rechazada**: ningún estado de {c0, c1} es de aceptación.

## Cadena `baa`

- Inicio: {c0}
- Lee `b`: {c0} ⟶ {c0} [c0→c0]
- Lee `a`: {c0} ⟶ {c0, c1} [c0→c0, c0→c1] (bifurcación)
- Lee `a`: {c0, c1} ⟶ {c0, c1} [c0→c0, c0→c1]
- **Rechazada**: ningún estado de {c0, c1} es de aceptación.

## Cadena `bbbaa`

- Inicio: {c0}
- Lee `b`: {c0} ⟶ {c0} [c0→c0]
- Lee `b`: {c0} ⟶ {c0} [c0→c0]
- Lee `b`: {c0} ⟶ {c0} [c0→c0]
- Lee `a`: {c0} ⟶ {c0, c1} [c0→c0, c0→c1] (bifurcación)
- Lee `a`: {c0, c1} ⟶ {c0, c1} [c0→c0, c0→c1]
- **Rechazada**: ningún estado de {c0, c1} es de aceptación.

## Cadena `bbbbbaba`

- Inicio: {c0}
- Lee `b`: {c0} ⟶ {c0} [c0→c0]
- Lee `b`: {c0} ⟶ {c0} [c0→c0]
- Lee `b`: {c0} ⟶ {c0} [c0→c0]
- Lee `b`: {c0} ⟶ {c0} [c0→c0]
- Lee `b`: {c0} ⟶ {c0} [c0→c0]
- Lee `a`: {c0} ⟶ {c0, c1} [c0→c0, c0→c1] (bifurcación)
- Lee `b`: {c0, c1} ⟶ {c0, c2} [c0→c0, c1→c2]
- Lee `a`: {c0, c2} ⟶ {c0, c1} [c0→c0, c0→c1]
- **Rechazada**: ningún estado de {c0, c1} es de aceptación.

## Cadena `aabab`

- Inicio: {c0}
- Lee `a`: {c0} ⟶ {c0, c1} [c0→c0, c0→c1] (bifurcación)
- Lee `a`: {c0, c1} ⟶ {c0, c1} [c0→c0, c0→c1]
- Lee `b`: {c0, c1} ⟶ {c0, c2} [c0→c0, c1→c2]
- Lee `a`: {c0, c2} ⟶ {c0, c1} [c0→c0, c0→c1]
- Lee `b`: {c0, c1} ⟶ {c0, c2} [c0→c0, c1→c2]
- **Rechazada**: ningún estado de {c0, c2} es de aceptación.
