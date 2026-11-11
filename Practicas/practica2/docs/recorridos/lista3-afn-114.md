# Recorridos: Lista 3 · AFN del problema 114

AFN para el problema 114: L = {w ∈ Σ3* : w = aⁿbᵐ, m, n ∈ N}.

Autómata: `lista3-afn-114` (AFD).

## Cadena λ

- Inicio: {a*}
- **Aceptada**: queda {a*} ∈ F.

## Cadena `b`

- Inicio: {a*}
- Lee `b`: {a*} ⟶ {a*b+} [a*→a*b+]
- **Aceptada**: queda {a*b+} ∈ F.

## Cadena `aaa`

- Inicio: {a*}
- Lee `a`: {a*} ⟶ {a*} [a*→a*]
- Lee `a`: {a*} ⟶ {a*} [a*→a*]
- Lee `a`: {a*} ⟶ {a*} [a*→a*]
- **Aceptada**: queda {a*} ∈ F.

## Cadena `aaabb`

- Inicio: {a*}
- Lee `a`: {a*} ⟶ {a*} [a*→a*]
- Lee `a`: {a*} ⟶ {a*} [a*→a*]
- Lee `a`: {a*} ⟶ {a*} [a*→a*]
- Lee `b`: {a*} ⟶ {a*b+} [a*→a*b+]
- Lee `b`: {a*b+} ⟶ {a*b+} [a*b+→a*b+]
- **Aceptada**: queda {a*b+} ∈ F.

## Cadena `aaaaaaab`

- Inicio: {a*}
- Lee `a`: {a*} ⟶ {a*} [a*→a*]
- Lee `a`: {a*} ⟶ {a*} [a*→a*]
- Lee `a`: {a*} ⟶ {a*} [a*→a*]
- Lee `a`: {a*} ⟶ {a*} [a*→a*]
- Lee `a`: {a*} ⟶ {a*} [a*→a*]
- Lee `a`: {a*} ⟶ {a*} [a*→a*]
- Lee `a`: {a*} ⟶ {a*} [a*→a*]
- Lee `b`: {a*} ⟶ {a*b+} [a*→a*b+]
- **Aceptada**: queda {a*b+} ∈ F.

## Cadena `ba`

- Inicio: {a*}
- Lee `b`: {a*} ⟶ {a*b+} [a*→a*b+]
- Lee `a`: {a*b+} ⟶ ∅ [ninguna transición]
- **Rechazada**: no queda ningún estado activo.

## Cadena `baa`

- Inicio: {a*}
- Lee `b`: {a*} ⟶ {a*b+} [a*→a*b+]
- Lee `a`: {a*b+} ⟶ ∅ [ninguna transición]
- Lee `a`: ∅ ⟶ ∅ [ninguna transición]
- **Rechazada**: no queda ningún estado activo.

## Cadena `aabaa`

- Inicio: {a*}
- Lee `a`: {a*} ⟶ {a*} [a*→a*]
- Lee `a`: {a*} ⟶ {a*} [a*→a*]
- Lee `b`: {a*} ⟶ {a*b+} [a*→a*b+]
- Lee `a`: {a*b+} ⟶ ∅ [ninguna transición]
- Lee `a`: ∅ ⟶ ∅ [ninguna transición]
- **Rechazada**: no queda ningún estado activo.

## Cadena `babbbbb`

- Inicio: {a*}
- Lee `b`: {a*} ⟶ {a*b+} [a*→a*b+]
- Lee `a`: {a*b+} ⟶ ∅ [ninguna transición]
- Lee `b`: ∅ ⟶ ∅ [ninguna transición]
- Lee `b`: ∅ ⟶ ∅ [ninguna transición]
- Lee `b`: ∅ ⟶ ∅ [ninguna transición]
- Lee `b`: ∅ ⟶ ∅ [ninguna transición]
- Lee `b`: ∅ ⟶ ∅ [ninguna transición]
- **Rechazada**: no queda ningún estado activo.

## Cadena `abaabbbabb`

- Inicio: {a*}
- Lee `a`: {a*} ⟶ {a*} [a*→a*]
- Lee `b`: {a*} ⟶ {a*b+} [a*→a*b+]
- Lee `a`: {a*b+} ⟶ ∅ [ninguna transición]
- Lee `a`: ∅ ⟶ ∅ [ninguna transición]
- Lee `b`: ∅ ⟶ ∅ [ninguna transición]
- Lee `b`: ∅ ⟶ ∅ [ninguna transición]
- Lee `b`: ∅ ⟶ ∅ [ninguna transición]
- Lee `a`: ∅ ⟶ ∅ [ninguna transición]
- Lee `b`: ∅ ⟶ ∅ [ninguna transición]
- Lee `b`: ∅ ⟶ ∅ [ninguna transición]
- **Rechazada**: no queda ningún estado activo.
