# Recorridos: Lista 3 · AFN del problema 117

AFN para el problema 117: L = {w ∈ Σ3* : w = aⁿbᵐaᵖb^q, m, n, p, q ∈ N}.

Autómata: `lista3-afn-117` (AFD).

## Cadena λ

- Inicio: {f1:a*}
- **Aceptada**: queda {f1:a*} ∈ F.

## Cadena `b`

- Inicio: {f1:a*}
- Lee `b`: {f1:a*} ⟶ {f2:b*} [f1:a*→f2:b*]
- **Aceptada**: queda {f2:b*} ∈ F.

## Cadena `aaa`

- Inicio: {f1:a*}
- Lee `a`: {f1:a*} ⟶ {f1:a*} [f1:a*→f1:a*]
- Lee `a`: {f1:a*} ⟶ {f1:a*} [f1:a*→f1:a*]
- Lee `a`: {f1:a*} ⟶ {f1:a*} [f1:a*→f1:a*]
- **Aceptada**: queda {f1:a*} ∈ F.

## Cadena `bbaab`

- Inicio: {f1:a*}
- Lee `b`: {f1:a*} ⟶ {f2:b*} [f1:a*→f2:b*]
- Lee `b`: {f2:b*} ⟶ {f2:b*} [f2:b*→f2:b*]
- Lee `a`: {f2:b*} ⟶ {f3:a*} [f2:b*→f3:a*]
- Lee `a`: {f3:a*} ⟶ {f3:a*} [f3:a*→f3:a*]
- Lee `b`: {f3:a*} ⟶ {f4:b*} [f3:a*→f4:b*]
- **Aceptada**: queda {f4:b*} ∈ F.

## Cadena `aaabbabb`

- Inicio: {f1:a*}
- Lee `a`: {f1:a*} ⟶ {f1:a*} [f1:a*→f1:a*]
- Lee `a`: {f1:a*} ⟶ {f1:a*} [f1:a*→f1:a*]
- Lee `a`: {f1:a*} ⟶ {f1:a*} [f1:a*→f1:a*]
- Lee `b`: {f1:a*} ⟶ {f2:b*} [f1:a*→f2:b*]
- Lee `b`: {f2:b*} ⟶ {f2:b*} [f2:b*→f2:b*]
- Lee `a`: {f2:b*} ⟶ {f3:a*} [f2:b*→f3:a*]
- Lee `b`: {f3:a*} ⟶ {f4:b*} [f3:a*→f4:b*]
- Lee `b`: {f4:b*} ⟶ {f4:b*} [f4:b*→f4:b*]
- **Aceptada**: queda {f4:b*} ∈ F.

## Cadena `baba`

- Inicio: {f1:a*}
- Lee `b`: {f1:a*} ⟶ {f2:b*} [f1:a*→f2:b*]
- Lee `a`: {f2:b*} ⟶ {f3:a*} [f2:b*→f3:a*]
- Lee `b`: {f3:a*} ⟶ {f4:b*} [f3:a*→f4:b*]
- Lee `a`: {f4:b*} ⟶ ∅ [ninguna transición]
- **Rechazada**: no queda ningún estado activo.

## Cadena `babba`

- Inicio: {f1:a*}
- Lee `b`: {f1:a*} ⟶ {f2:b*} [f1:a*→f2:b*]
- Lee `a`: {f2:b*} ⟶ {f3:a*} [f2:b*→f3:a*]
- Lee `b`: {f3:a*} ⟶ {f4:b*} [f3:a*→f4:b*]
- Lee `b`: {f4:b*} ⟶ {f4:b*} [f4:b*→f4:b*]
- Lee `a`: {f4:b*} ⟶ ∅ [ninguna transición]
- **Rechazada**: no queda ningún estado activo.

## Cadena `babbaaa`

- Inicio: {f1:a*}
- Lee `b`: {f1:a*} ⟶ {f2:b*} [f1:a*→f2:b*]
- Lee `a`: {f2:b*} ⟶ {f3:a*} [f2:b*→f3:a*]
- Lee `b`: {f3:a*} ⟶ {f4:b*} [f3:a*→f4:b*]
- Lee `b`: {f4:b*} ⟶ {f4:b*} [f4:b*→f4:b*]
- Lee `a`: {f4:b*} ⟶ ∅ [ninguna transición]
- Lee `a`: ∅ ⟶ ∅ [ninguna transición]
- Lee `a`: ∅ ⟶ ∅ [ninguna transición]
- **Rechazada**: no queda ningún estado activo.

## Cadena `babaababb`

- Inicio: {f1:a*}
- Lee `b`: {f1:a*} ⟶ {f2:b*} [f1:a*→f2:b*]
- Lee `a`: {f2:b*} ⟶ {f3:a*} [f2:b*→f3:a*]
- Lee `b`: {f3:a*} ⟶ {f4:b*} [f3:a*→f4:b*]
- Lee `a`: {f4:b*} ⟶ ∅ [ninguna transición]
- Lee `a`: ∅ ⟶ ∅ [ninguna transición]
- Lee `b`: ∅ ⟶ ∅ [ninguna transición]
- Lee `a`: ∅ ⟶ ∅ [ninguna transición]
- Lee `b`: ∅ ⟶ ∅ [ninguna transición]
- Lee `b`: ∅ ⟶ ∅ [ninguna transición]
- **Rechazada**: no queda ningún estado activo.

## Cadena `babbabbbbbbb`

- Inicio: {f1:a*}
- Lee `b`: {f1:a*} ⟶ {f2:b*} [f1:a*→f2:b*]
- Lee `a`: {f2:b*} ⟶ {f3:a*} [f2:b*→f3:a*]
- Lee `b`: {f3:a*} ⟶ {f4:b*} [f3:a*→f4:b*]
- Lee `b`: {f4:b*} ⟶ {f4:b*} [f4:b*→f4:b*]
- Lee `a`: {f4:b*} ⟶ ∅ [ninguna transición]
- Lee `b`: ∅ ⟶ ∅ [ninguna transición]
- Lee `b`: ∅ ⟶ ∅ [ninguna transición]
- Lee `b`: ∅ ⟶ ∅ [ninguna transición]
- Lee `b`: ∅ ⟶ ∅ [ninguna transición]
- Lee `b`: ∅ ⟶ ∅ [ninguna transición]
- Lee `b`: ∅ ⟶ ∅ [ninguna transición]
- Lee `b`: ∅ ⟶ ∅ [ninguna transición]
- **Rechazada**: no queda ningún estado activo.
