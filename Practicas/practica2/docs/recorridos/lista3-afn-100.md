# Recorridos: Lista 3 · AFN del problema 100

AFN para el problema 100: Las palabras de Σ2 tales que el primer símbolo es una letra y el segundo es un dígito.

Autómata: `lista3-afn-100` (AFD).

## Cadena `c1`

- Inicio: {q0}
- Lee `c`: {q0} ⟶ {q1} [q0→q1]
- Lee `1`: {q1} ⟶ {q2} [q1→q2]
- **Aceptada**: queda {q2} ∈ F.

## Cadena `b01`

- Inicio: {q0}
- Lee `b`: {q0} ⟶ {q1} [q0→q1]
- Lee `0`: {q1} ⟶ {q2} [q1→q2]
- Lee `1`: {q2} ⟶ {q2} [q2→q2]
- **Aceptada**: queda {q2} ∈ F.

## Cadena `b0a0a`

- Inicio: {q0}
- Lee `b`: {q0} ⟶ {q1} [q0→q1]
- Lee `0`: {q1} ⟶ {q2} [q1→q2]
- Lee `a`: {q2} ⟶ {q2} [q2→q2]
- Lee `0`: {q2} ⟶ {q2} [q2→q2]
- Lee `a`: {q2} ⟶ {q2} [q2→q2]
- **Aceptada**: queda {q2} ∈ F.

## Cadena `c0ba100`

- Inicio: {q0}
- Lee `c`: {q0} ⟶ {q1} [q0→q1]
- Lee `0`: {q1} ⟶ {q2} [q1→q2]
- Lee `b`: {q2} ⟶ {q2} [q2→q2]
- Lee `a`: {q2} ⟶ {q2} [q2→q2]
- Lee `1`: {q2} ⟶ {q2} [q2→q2]
- Lee `0`: {q2} ⟶ {q2} [q2→q2]
- Lee `0`: {q2} ⟶ {q2} [q2→q2]
- **Aceptada**: queda {q2} ∈ F.

## Cadena `b1cca1a1ac`

- Inicio: {q0}
- Lee `b`: {q0} ⟶ {q1} [q0→q1]
- Lee `1`: {q1} ⟶ {q2} [q1→q2]
- Lee `c`: {q2} ⟶ {q2} [q2→q2]
- Lee `c`: {q2} ⟶ {q2} [q2→q2]
- Lee `a`: {q2} ⟶ {q2} [q2→q2]
- Lee `1`: {q2} ⟶ {q2} [q2→q2]
- Lee `a`: {q2} ⟶ {q2} [q2→q2]
- Lee `1`: {q2} ⟶ {q2} [q2→q2]
- Lee `a`: {q2} ⟶ {q2} [q2→q2]
- Lee `c`: {q2} ⟶ {q2} [q2→q2]
- **Aceptada**: queda {q2} ∈ F.

## Cadena λ

- Inicio: {q0}
- **Rechazada**: ningún estado de {q0} es de aceptación.

## Cadena `0`

- Inicio: {q0}
- Lee `0`: {q0} ⟶ ∅ [ninguna transición]
- **Rechazada**: no queda ningún estado activo.

## Cadena `bcb`

- Inicio: {q0}
- Lee `b`: {q0} ⟶ {q1} [q0→q1]
- Lee `c`: {q1} ⟶ ∅ [ninguna transición]
- Lee `b`: ∅ ⟶ ∅ [ninguna transición]
- **Rechazada**: no queda ningún estado activo.

## Cadena `0a0b0`

- Inicio: {q0}
- Lee `0`: {q0} ⟶ ∅ [ninguna transición]
- Lee `a`: ∅ ⟶ ∅ [ninguna transición]
- Lee `0`: ∅ ⟶ ∅ [ninguna transición]
- Lee `b`: ∅ ⟶ ∅ [ninguna transición]
- Lee `0`: ∅ ⟶ ∅ [ninguna transición]
- **Rechazada**: no queda ningún estado activo.

## Cadena `caab1cab`

- Inicio: {q0}
- Lee `c`: {q0} ⟶ {q1} [q0→q1]
- Lee `a`: {q1} ⟶ ∅ [ninguna transición]
- Lee `a`: ∅ ⟶ ∅ [ninguna transición]
- Lee `b`: ∅ ⟶ ∅ [ninguna transición]
- Lee `1`: ∅ ⟶ ∅ [ninguna transición]
- Lee `c`: ∅ ⟶ ∅ [ninguna transición]
- Lee `a`: ∅ ⟶ ∅ [ninguna transición]
- Lee `b`: ∅ ⟶ ∅ [ninguna transición]
- **Rechazada**: no queda ningún estado activo.

## Cadena `b0`

- Inicio: {q0}
- Lee `b`: {q0} ⟶ {q1} [q0→q1]
- Lee `0`: {q1} ⟶ {q2} [q1→q2]
- **Aceptada**: queda {q2} ∈ F.
