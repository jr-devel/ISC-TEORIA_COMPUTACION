# Recorridos: Lista 3 · AFN del problema 101

AFN para el problema 101: Las palabras de Σ3 que contienen la cadena aba.

Autómata: `lista3-afn-101` (AFN).

## Cadena `aba`

- Inicio: {c0}
- Lee `a`: {c0} ⟶ {c0, c1} [c0→c0, c0→c1] (bifurcación)
- Lee `b`: {c0, c1} ⟶ {c0, c2} [c0→c0, c1→c2]
- Lee `a`: {c0, c2} ⟶ {c0, c1, c3} [c0→c0, c0→c1, c2→c3] (bifurcación)
- **Aceptada**: queda {c3} ∈ F.

## Cadena `abab`

- Inicio: {c0}
- Lee `a`: {c0} ⟶ {c0, c1} [c0→c0, c0→c1] (bifurcación)
- Lee `b`: {c0, c1} ⟶ {c0, c2} [c0→c0, c1→c2]
- Lee `a`: {c0, c2} ⟶ {c0, c1, c3} [c0→c0, c0→c1, c2→c3] (bifurcación)
- Lee `b`: {c0, c1, c3} ⟶ {c0, c2, c3} [c0→c0, c1→c2, c3→c3]
- **Aceptada**: queda {c3} ∈ F.

## Cadena `abaaab`

- Inicio: {c0}
- Lee `a`: {c0} ⟶ {c0, c1} [c0→c0, c0→c1] (bifurcación)
- Lee `b`: {c0, c1} ⟶ {c0, c2} [c0→c0, c1→c2]
- Lee `a`: {c0, c2} ⟶ {c0, c1, c3} [c0→c0, c0→c1, c2→c3] (bifurcación)
- Lee `a`: {c0, c1, c3} ⟶ {c0, c1, c3} [c0→c0, c0→c1, c3→c3]
- Lee `a`: {c0, c1, c3} ⟶ {c0, c1, c3} [c0→c0, c0→c1, c3→c3]
- Lee `b`: {c0, c1, c3} ⟶ {c0, c2, c3} [c0→c0, c1→c2, c3→c3]
- **Aceptada**: queda {c3} ∈ F.

## Cadena `abbbabab`

- Inicio: {c0}
- Lee `a`: {c0} ⟶ {c0, c1} [c0→c0, c0→c1] (bifurcación)
- Lee `b`: {c0, c1} ⟶ {c0, c2} [c0→c0, c1→c2]
- Lee `b`: {c0, c2} ⟶ {c0} [c0→c0]
- Lee `b`: {c0} ⟶ {c0} [c0→c0]
- Lee `a`: {c0} ⟶ {c0, c1} [c0→c0, c0→c1] (bifurcación)
- Lee `b`: {c0, c1} ⟶ {c0, c2} [c0→c0, c1→c2]
- Lee `a`: {c0, c2} ⟶ {c0, c1, c3} [c0→c0, c0→c1, c2→c3] (bifurcación)
- Lee `b`: {c0, c1, c3} ⟶ {c0, c2, c3} [c0→c0, c1→c2, c3→c3]
- **Aceptada**: queda {c3} ∈ F.

## Cadena `baababbbaba`

- Inicio: {c0}
- Lee `b`: {c0} ⟶ {c0} [c0→c0]
- Lee `a`: {c0} ⟶ {c0, c1} [c0→c0, c0→c1] (bifurcación)
- Lee `a`: {c0, c1} ⟶ {c0, c1} [c0→c0, c0→c1]
- Lee `b`: {c0, c1} ⟶ {c0, c2} [c0→c0, c1→c2]
- Lee `a`: {c0, c2} ⟶ {c0, c1, c3} [c0→c0, c0→c1, c2→c3] (bifurcación)
- Lee `b`: {c0, c1, c3} ⟶ {c0, c2, c3} [c0→c0, c1→c2, c3→c3]
- Lee `b`: {c0, c2, c3} ⟶ {c0, c3} [c0→c0, c3→c3]
- Lee `b`: {c0, c3} ⟶ {c0, c3} [c0→c0, c3→c3]
- Lee `a`: {c0, c3} ⟶ {c0, c1, c3} [c0→c0, c0→c1, c3→c3] (bifurcación)
- Lee `b`: {c0, c1, c3} ⟶ {c0, c2, c3} [c0→c0, c1→c2, c3→c3]
- Lee `a`: {c0, c2, c3} ⟶ {c0, c1, c3} [c0→c0, c0→c1, c2→c3, c3→c3]
- **Aceptada**: queda {c3} ∈ F.

## Cadena λ

- Inicio: {c0}
- **Rechazada**: ningún estado de {c0} es de aceptación.

## Cadena `b`

- Inicio: {c0}
- Lee `b`: {c0} ⟶ {c0} [c0→c0]
- **Rechazada**: ningún estado de {c0} es de aceptación.

## Cadena `aaa`

- Inicio: {c0}
- Lee `a`: {c0} ⟶ {c0, c1} [c0→c0, c0→c1] (bifurcación)
- Lee `a`: {c0, c1} ⟶ {c0, c1} [c0→c0, c0→c1]
- Lee `a`: {c0, c1} ⟶ {c0, c1} [c0→c0, c0→c1]
- **Rechazada**: ningún estado de {c0, c1} es de aceptación.

## Cadena `babba`

- Inicio: {c0}
- Lee `b`: {c0} ⟶ {c0} [c0→c0]
- Lee `a`: {c0} ⟶ {c0, c1} [c0→c0, c0→c1] (bifurcación)
- Lee `b`: {c0, c1} ⟶ {c0, c2} [c0→c0, c1→c2]
- Lee `b`: {c0, c2} ⟶ {c0} [c0→c0]
- Lee `a`: {c0} ⟶ {c0, c1} [c0→c0, c0→c1] (bifurcación)
- **Rechazada**: ningún estado de {c0, c1} es de aceptación.

## Cadena `aaaaabbb`

- Inicio: {c0}
- Lee `a`: {c0} ⟶ {c0, c1} [c0→c0, c0→c1] (bifurcación)
- Lee `a`: {c0, c1} ⟶ {c0, c1} [c0→c0, c0→c1]
- Lee `a`: {c0, c1} ⟶ {c0, c1} [c0→c0, c0→c1]
- Lee `a`: {c0, c1} ⟶ {c0, c1} [c0→c0, c0→c1]
- Lee `a`: {c0, c1} ⟶ {c0, c1} [c0→c0, c0→c1]
- Lee `b`: {c0, c1} ⟶ {c0, c2} [c0→c0, c1→c2]
- Lee `b`: {c0, c2} ⟶ {c0} [c0→c0]
- Lee `b`: {c0} ⟶ {c0} [c0→c0]
- **Rechazada**: ningún estado de {c0} es de aceptación.

## Cadena `bb`

- Inicio: {c0}
- Lee `b`: {c0} ⟶ {c0} [c0→c0]
- Lee `b`: {c0} ⟶ {c0} [c0→c0]
- **Rechazada**: ningún estado de {c0} es de aceptación.
