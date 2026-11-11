# Recorridos: Lista 3 · AFN del problema 105

AFN para el problema 105: Las palabras de Σ3 que terminan con la cadena abaa.

Autómata: `lista3-afn-105` (AFN).

## Cadena `abaa`

- Inicio: {c0}
- Lee `a`: {c0} ⟶ {c0, c1} [c0→c0, c0→c1] (bifurcación)
- Lee `b`: {c0, c1} ⟶ {c0, c2} [c0→c0, c1→c2]
- Lee `a`: {c0, c2} ⟶ {c0, c1, c3} [c0→c0, c0→c1, c2→c3] (bifurcación)
- Lee `a`: {c0, c1, c3} ⟶ {c0, c1, c4} [c0→c0, c0→c1, c3→c4]
- **Aceptada**: queda {c4} ∈ F.

## Cadena `babaa`

- Inicio: {c0}
- Lee `b`: {c0} ⟶ {c0} [c0→c0]
- Lee `a`: {c0} ⟶ {c0, c1} [c0→c0, c0→c1] (bifurcación)
- Lee `b`: {c0, c1} ⟶ {c0, c2} [c0→c0, c1→c2]
- Lee `a`: {c0, c2} ⟶ {c0, c1, c3} [c0→c0, c0→c1, c2→c3] (bifurcación)
- Lee `a`: {c0, c1, c3} ⟶ {c0, c1, c4} [c0→c0, c0→c1, c3→c4]
- **Aceptada**: queda {c4} ∈ F.

## Cadena `bababaa`

- Inicio: {c0}
- Lee `b`: {c0} ⟶ {c0} [c0→c0]
- Lee `a`: {c0} ⟶ {c0, c1} [c0→c0, c0→c1] (bifurcación)
- Lee `b`: {c0, c1} ⟶ {c0, c2} [c0→c0, c1→c2]
- Lee `a`: {c0, c2} ⟶ {c0, c1, c3} [c0→c0, c0→c1, c2→c3] (bifurcación)
- Lee `b`: {c0, c1, c3} ⟶ {c0, c2} [c0→c0, c1→c2]
- Lee `a`: {c0, c2} ⟶ {c0, c1, c3} [c0→c0, c0→c1, c2→c3] (bifurcación)
- Lee `a`: {c0, c1, c3} ⟶ {c0, c1, c4} [c0→c0, c0→c1, c3→c4]
- **Aceptada**: queda {c4} ∈ F.

## Cadena `aaabaabaa`

- Inicio: {c0}
- Lee `a`: {c0} ⟶ {c0, c1} [c0→c0, c0→c1] (bifurcación)
- Lee `a`: {c0, c1} ⟶ {c0, c1} [c0→c0, c0→c1]
- Lee `a`: {c0, c1} ⟶ {c0, c1} [c0→c0, c0→c1]
- Lee `b`: {c0, c1} ⟶ {c0, c2} [c0→c0, c1→c2]
- Lee `a`: {c0, c2} ⟶ {c0, c1, c3} [c0→c0, c0→c1, c2→c3] (bifurcación)
- Lee `a`: {c0, c1, c3} ⟶ {c0, c1, c4} [c0→c0, c0→c1, c3→c4]
- Lee `b`: {c0, c1, c4} ⟶ {c0, c2} [c0→c0, c1→c2]
- Lee `a`: {c0, c2} ⟶ {c0, c1, c3} [c0→c0, c0→c1, c2→c3] (bifurcación)
- Lee `a`: {c0, c1, c3} ⟶ {c0, c1, c4} [c0→c0, c0→c1, c3→c4]
- **Aceptada**: queda {c4} ∈ F.

## Cadena `bababaababaa`

- Inicio: {c0}
- Lee `b`: {c0} ⟶ {c0} [c0→c0]
- Lee `a`: {c0} ⟶ {c0, c1} [c0→c0, c0→c1] (bifurcación)
- Lee `b`: {c0, c1} ⟶ {c0, c2} [c0→c0, c1→c2]
- Lee `a`: {c0, c2} ⟶ {c0, c1, c3} [c0→c0, c0→c1, c2→c3] (bifurcación)
- Lee `b`: {c0, c1, c3} ⟶ {c0, c2} [c0→c0, c1→c2]
- Lee `a`: {c0, c2} ⟶ {c0, c1, c3} [c0→c0, c0→c1, c2→c3] (bifurcación)
- Lee `a`: {c0, c1, c3} ⟶ {c0, c1, c4} [c0→c0, c0→c1, c3→c4]
- Lee `b`: {c0, c1, c4} ⟶ {c0, c2} [c0→c0, c1→c2]
- Lee `a`: {c0, c2} ⟶ {c0, c1, c3} [c0→c0, c0→c1, c2→c3] (bifurcación)
- Lee `b`: {c0, c1, c3} ⟶ {c0, c2} [c0→c0, c1→c2]
- Lee `a`: {c0, c2} ⟶ {c0, c1, c3} [c0→c0, c0→c1, c2→c3] (bifurcación)
- Lee `a`: {c0, c1, c3} ⟶ {c0, c1, c4} [c0→c0, c0→c1, c3→c4]
- **Aceptada**: queda {c4} ∈ F.

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
- Lee `a`: {c0, c1} ⟶ {c0, c1} [c0→c0, c0→c1]
- Lee `a`: {c0, c1} ⟶ {c0, c1} [c0→c0, c0→c1]
- **Rechazada**: ningún estado de {c0, c1} es de aceptación.

## Cadena `bbaab`

- Inicio: {c0}
- Lee `b`: {c0} ⟶ {c0} [c0→c0]
- Lee `b`: {c0} ⟶ {c0} [c0→c0]
- Lee `a`: {c0} ⟶ {c0, c1} [c0→c0, c0→c1] (bifurcación)
- Lee `a`: {c0, c1} ⟶ {c0, c1} [c0→c0, c0→c1]
- Lee `b`: {c0, c1} ⟶ {c0, c2} [c0→c0, c1→c2]
- **Rechazada**: ningún estado de {c0, c2} es de aceptación.

## Cadena `bbbbaaba`

- Inicio: {c0}
- Lee `b`: {c0} ⟶ {c0} [c0→c0]
- Lee `b`: {c0} ⟶ {c0} [c0→c0]
- Lee `b`: {c0} ⟶ {c0} [c0→c0]
- Lee `b`: {c0} ⟶ {c0} [c0→c0]
- Lee `a`: {c0} ⟶ {c0, c1} [c0→c0, c0→c1] (bifurcación)
- Lee `a`: {c0, c1} ⟶ {c0, c1} [c0→c0, c0→c1]
- Lee `b`: {c0, c1} ⟶ {c0, c2} [c0→c0, c1→c2]
- Lee `a`: {c0, c2} ⟶ {c0, c1, c3} [c0→c0, c0→c1, c2→c3] (bifurcación)
- **Rechazada**: ningún estado de {c0, c1, c3} es de aceptación.

## Cadena `aba`

- Inicio: {c0}
- Lee `a`: {c0} ⟶ {c0, c1} [c0→c0, c0→c1] (bifurcación)
- Lee `b`: {c0, c1} ⟶ {c0, c2} [c0→c0, c1→c2]
- Lee `a`: {c0, c2} ⟶ {c0, c1, c3} [c0→c0, c0→c1, c2→c3] (bifurcación)
- **Rechazada**: ningún estado de {c0, c1, c3} es de aceptación.
