# Recorridos: Lista 3 · AFN del problema 123

AFN para el problema 123: Las palabras de Σ3 de la forma wxw donde w ∈ Σ3² y x ∈ Σ3*.

Autómata: `lista3-afn-123` (AFN).

## Cadena `abab`

- Inicio: {q0}
- Lee `a`: {q0} ⟶ {aa1, ab1} [q0→aa1, q0→ab1] (bifurcación)
- Lee `b`: {aa1, ab1} ⟶ {ab2} [ab1→ab2]
- Lee `a`: {ab2} ⟶ {ab2, ab3} [ab2→ab2, ab2→ab3] (bifurcación)
- Lee `b`: {ab2, ab3} ⟶ {ab2, F} [ab2→ab2, ab3→F]
- **Aceptada**: queda {F} ∈ F.

## Cadena `aaaaa`

- Inicio: {q0}
- Lee `a`: {q0} ⟶ {aa1, ab1} [q0→aa1, q0→ab1] (bifurcación)
- Lee `a`: {aa1, ab1} ⟶ {aa2} [aa1→aa2]
- Lee `a`: {aa2} ⟶ {aa2, aa3} [aa2→aa2, aa2→aa3] (bifurcación)
- Lee `a`: {aa2, aa3} ⟶ {aa2, aa3, F} [aa2→aa2, aa2→aa3, aa3→F] (bifurcación)
- Lee `a`: {aa2, aa3, F} ⟶ {aa2, aa3, F} [aa2→aa2, aa2→aa3, aa3→F]
- **Aceptada**: queda {F} ∈ F.

## Cadena `aababaa`

- Inicio: {q0}
- Lee `a`: {q0} ⟶ {aa1, ab1} [q0→aa1, q0→ab1] (bifurcación)
- Lee `a`: {aa1, ab1} ⟶ {aa2} [aa1→aa2]
- Lee `b`: {aa2} ⟶ {aa2} [aa2→aa2]
- Lee `a`: {aa2} ⟶ {aa2, aa3} [aa2→aa2, aa2→aa3] (bifurcación)
- Lee `b`: {aa2, aa3} ⟶ {aa2} [aa2→aa2]
- Lee `a`: {aa2} ⟶ {aa2, aa3} [aa2→aa2, aa2→aa3] (bifurcación)
- Lee `a`: {aa2, aa3} ⟶ {aa2, aa3, F} [aa2→aa2, aa2→aa3, aa3→F] (bifurcación)
- **Aceptada**: queda {F} ∈ F.

## Cadena `bbbabbabb`

- Inicio: {q0}
- Lee `b`: {q0} ⟶ {ba1, bb1} [q0→ba1, q0→bb1] (bifurcación)
- Lee `b`: {ba1, bb1} ⟶ {bb2} [bb1→bb2]
- Lee `b`: {bb2} ⟶ {bb2, bb3} [bb2→bb2, bb2→bb3] (bifurcación)
- Lee `a`: {bb2, bb3} ⟶ {bb2} [bb2→bb2]
- Lee `b`: {bb2} ⟶ {bb2, bb3} [bb2→bb2, bb2→bb3] (bifurcación)
- Lee `b`: {bb2, bb3} ⟶ {bb2, bb3, F} [bb2→bb2, bb2→bb3, bb3→F] (bifurcación)
- Lee `a`: {bb2, bb3, F} ⟶ {bb2} [bb2→bb2]
- Lee `b`: {bb2} ⟶ {bb2, bb3} [bb2→bb2, bb2→bb3] (bifurcación)
- Lee `b`: {bb2, bb3} ⟶ {bb2, bb3, F} [bb2→bb2, bb2→bb3, bb3→F] (bifurcación)
- **Aceptada**: queda {F} ∈ F.

## Cadena `bbaabbaababb`

- Inicio: {q0}
- Lee `b`: {q0} ⟶ {ba1, bb1} [q0→ba1, q0→bb1] (bifurcación)
- Lee `b`: {ba1, bb1} ⟶ {bb2} [bb1→bb2]
- Lee `a`: {bb2} ⟶ {bb2} [bb2→bb2]
- Lee `a`: {bb2} ⟶ {bb2} [bb2→bb2]
- Lee `b`: {bb2} ⟶ {bb2, bb3} [bb2→bb2, bb2→bb3] (bifurcación)
- Lee `b`: {bb2, bb3} ⟶ {bb2, bb3, F} [bb2→bb2, bb2→bb3, bb3→F] (bifurcación)
- Lee `a`: {bb2, bb3, F} ⟶ {bb2} [bb2→bb2]
- Lee `a`: {bb2} ⟶ {bb2} [bb2→bb2]
- Lee `b`: {bb2} ⟶ {bb2, bb3} [bb2→bb2, bb2→bb3] (bifurcación)
- Lee `a`: {bb2, bb3} ⟶ {bb2} [bb2→bb2]
- Lee `b`: {bb2} ⟶ {bb2, bb3} [bb2→bb2, bb2→bb3] (bifurcación)
- Lee `b`: {bb2, bb3} ⟶ {bb2, bb3, F} [bb2→bb2, bb2→bb3, bb3→F] (bifurcación)
- **Aceptada**: queda {F} ∈ F.

## Cadena λ

- Inicio: {q0}
- **Rechazada**: ningún estado de {q0} es de aceptación.

## Cadena `a`

- Inicio: {q0}
- Lee `a`: {q0} ⟶ {aa1, ab1} [q0→aa1, q0→ab1] (bifurcación)
- **Rechazada**: ningún estado de {aa1, ab1} es de aceptación.

## Cadena `bba`

- Inicio: {q0}
- Lee `b`: {q0} ⟶ {ba1, bb1} [q0→ba1, q0→bb1] (bifurcación)
- Lee `b`: {ba1, bb1} ⟶ {bb2} [bb1→bb2]
- Lee `a`: {bb2} ⟶ {bb2} [bb2→bb2]
- **Rechazada**: ningún estado de {bb2} es de aceptación.

## Cadena `aabbb`

- Inicio: {q0}
- Lee `a`: {q0} ⟶ {aa1, ab1} [q0→aa1, q0→ab1] (bifurcación)
- Lee `a`: {aa1, ab1} ⟶ {aa2} [aa1→aa2]
- Lee `b`: {aa2} ⟶ {aa2} [aa2→aa2]
- Lee `b`: {aa2} ⟶ {aa2} [aa2→aa2]
- Lee `b`: {aa2} ⟶ {aa2} [aa2→aa2]
- **Rechazada**: ningún estado de {aa2} es de aceptación.

## Cadena `aaabbaba`

- Inicio: {q0}
- Lee `a`: {q0} ⟶ {aa1, ab1} [q0→aa1, q0→ab1] (bifurcación)
- Lee `a`: {aa1, ab1} ⟶ {aa2} [aa1→aa2]
- Lee `a`: {aa2} ⟶ {aa2, aa3} [aa2→aa2, aa2→aa3] (bifurcación)
- Lee `b`: {aa2, aa3} ⟶ {aa2} [aa2→aa2]
- Lee `b`: {aa2} ⟶ {aa2} [aa2→aa2]
- Lee `a`: {aa2} ⟶ {aa2, aa3} [aa2→aa2, aa2→aa3] (bifurcación)
- Lee `b`: {aa2, aa3} ⟶ {aa2} [aa2→aa2]
- Lee `a`: {aa2} ⟶ {aa2, aa3} [aa2→aa2, aa2→aa3] (bifurcación)
- **Rechazada**: ningún estado de {aa2, aa3} es de aceptación.

## Cadena `aaaa`

- Inicio: {q0}
- Lee `a`: {q0} ⟶ {aa1, ab1} [q0→aa1, q0→ab1] (bifurcación)
- Lee `a`: {aa1, ab1} ⟶ {aa2} [aa1→aa2]
- Lee `a`: {aa2} ⟶ {aa2, aa3} [aa2→aa2, aa2→aa3] (bifurcación)
- Lee `a`: {aa2, aa3} ⟶ {aa2, aa3, F} [aa2→aa2, aa2→aa3, aa3→F] (bifurcación)
- **Aceptada**: queda {F} ∈ F.

## Cadena `aab`

- Inicio: {q0}
- Lee `a`: {q0} ⟶ {aa1, ab1} [q0→aa1, q0→ab1] (bifurcación)
- Lee `a`: {aa1, ab1} ⟶ {aa2} [aa1→aa2]
- Lee `b`: {aa2} ⟶ {aa2} [aa2→aa2]
- **Rechazada**: ningún estado de {aa2} es de aceptación.
