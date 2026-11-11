# Recorridos: Lista 2 · Ejercicio 138

AFD para las palabras sobre {a, b} cuyo número de bes es divisible entre tres.

Autómata: `lista2-138` (AFD).

## Cadena λ

- Inicio: {b≡0}
- **Aceptada**: queda {b≡0} ∈ F.

## Cadena `a`

- Inicio: {b≡0}
- Lee `a`: {b≡0} ⟶ {b≡0} [b≡0→b≡0]
- **Aceptada**: queda {b≡0} ∈ F.

## Cadena `aaa`

- Inicio: {b≡0}
- Lee `a`: {b≡0} ⟶ {b≡0} [b≡0→b≡0]
- Lee `a`: {b≡0} ⟶ {b≡0} [b≡0→b≡0]
- Lee `a`: {b≡0} ⟶ {b≡0} [b≡0→b≡0]
- **Aceptada**: queda {b≡0} ∈ F.

## Cadena `aabbb`

- Inicio: {b≡0}
- Lee `a`: {b≡0} ⟶ {b≡0} [b≡0→b≡0]
- Lee `a`: {b≡0} ⟶ {b≡0} [b≡0→b≡0]
- Lee `b`: {b≡0} ⟶ {b≡1} [b≡0→b≡1]
- Lee `b`: {b≡1} ⟶ {b≡2} [b≡1→b≡2]
- Lee `b`: {b≡2} ⟶ {b≡0} [b≡2→b≡0]
- **Aceptada**: queda {b≡0} ∈ F.

## Cadena `bbabbabb`

- Inicio: {b≡0}
- Lee `b`: {b≡0} ⟶ {b≡1} [b≡0→b≡1]
- Lee `b`: {b≡1} ⟶ {b≡2} [b≡1→b≡2]
- Lee `a`: {b≡2} ⟶ {b≡2} [b≡2→b≡2]
- Lee `b`: {b≡2} ⟶ {b≡0} [b≡2→b≡0]
- Lee `b`: {b≡0} ⟶ {b≡1} [b≡0→b≡1]
- Lee `a`: {b≡1} ⟶ {b≡1} [b≡1→b≡1]
- Lee `b`: {b≡1} ⟶ {b≡2} [b≡1→b≡2]
- Lee `b`: {b≡2} ⟶ {b≡0} [b≡2→b≡0]
- **Aceptada**: queda {b≡0} ∈ F.

## Cadena `b`

- Inicio: {b≡0}
- Lee `b`: {b≡0} ⟶ {b≡1} [b≡0→b≡1]
- **Rechazada**: ningún estado de {b≡1} es de aceptación.

## Cadena `ba`

- Inicio: {b≡0}
- Lee `b`: {b≡0} ⟶ {b≡1} [b≡0→b≡1]
- Lee `a`: {b≡1} ⟶ {b≡1} [b≡1→b≡1]
- **Rechazada**: ningún estado de {b≡1} es de aceptación.

## Cadena `abba`

- Inicio: {b≡0}
- Lee `a`: {b≡0} ⟶ {b≡0} [b≡0→b≡0]
- Lee `b`: {b≡0} ⟶ {b≡1} [b≡0→b≡1]
- Lee `b`: {b≡1} ⟶ {b≡2} [b≡1→b≡2]
- Lee `a`: {b≡2} ⟶ {b≡2} [b≡2→b≡2]
- **Rechazada**: ningún estado de {b≡2} es de aceptación.

## Cadena `aabbaa`

- Inicio: {b≡0}
- Lee `a`: {b≡0} ⟶ {b≡0} [b≡0→b≡0]
- Lee `a`: {b≡0} ⟶ {b≡0} [b≡0→b≡0]
- Lee `b`: {b≡0} ⟶ {b≡1} [b≡0→b≡1]
- Lee `b`: {b≡1} ⟶ {b≡2} [b≡1→b≡2]
- Lee `a`: {b≡2} ⟶ {b≡2} [b≡2→b≡2]
- Lee `a`: {b≡2} ⟶ {b≡2} [b≡2→b≡2]
- **Rechazada**: ningún estado de {b≡2} es de aceptación.

## Cadena `baaaaaaba`

- Inicio: {b≡0}
- Lee `b`: {b≡0} ⟶ {b≡1} [b≡0→b≡1]
- Lee `a`: {b≡1} ⟶ {b≡1} [b≡1→b≡1]
- Lee `a`: {b≡1} ⟶ {b≡1} [b≡1→b≡1]
- Lee `a`: {b≡1} ⟶ {b≡1} [b≡1→b≡1]
- Lee `a`: {b≡1} ⟶ {b≡1} [b≡1→b≡1]
- Lee `a`: {b≡1} ⟶ {b≡1} [b≡1→b≡1]
- Lee `a`: {b≡1} ⟶ {b≡1} [b≡1→b≡1]
- Lee `b`: {b≡1} ⟶ {b≡2} [b≡1→b≡2]
- Lee `a`: {b≡2} ⟶ {b≡2} [b≡2→b≡2]
- **Rechazada**: ningún estado de {b≡2} es de aceptación.
