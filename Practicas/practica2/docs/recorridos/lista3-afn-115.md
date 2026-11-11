# Recorridos: Lista 3 · AFN del problema 115

AFN para el problema 115: L = {w ∈ Σ2* : w = (abc)ⁿ, n ∈ N}.

Autómata: `lista3-afn-115` (AFD).

## Cadena λ

- Inicio: {(abc)*}
- **Aceptada**: queda {(abc)*} ∈ F.

## Cadena `abc`

- Inicio: {(abc)*}
- Lee `a`: {(abc)*} ⟶ {…a} [(abc)*→…a]
- Lee `b`: {…a} ⟶ {…ab} […a→…ab]
- Lee `c`: {…ab} ⟶ {(abc)*} […ab→(abc)*]
- **Aceptada**: queda {(abc)*} ∈ F.

## Cadena `abcabc`

- Inicio: {(abc)*}
- Lee `a`: {(abc)*} ⟶ {…a} [(abc)*→…a]
- Lee `b`: {…a} ⟶ {…ab} […a→…ab]
- Lee `c`: {…ab} ⟶ {(abc)*} […ab→(abc)*]
- Lee `a`: {(abc)*} ⟶ {…a} [(abc)*→…a]
- Lee `b`: {…a} ⟶ {…ab} […a→…ab]
- Lee `c`: {…ab} ⟶ {(abc)*} […ab→(abc)*]
- **Aceptada**: queda {(abc)*} ∈ F.

## Cadena `abcabcabc`

- Inicio: {(abc)*}
- Lee `a`: {(abc)*} ⟶ {…a} [(abc)*→…a]
- Lee `b`: {…a} ⟶ {…ab} […a→…ab]
- Lee `c`: {…ab} ⟶ {(abc)*} […ab→(abc)*]
- Lee `a`: {(abc)*} ⟶ {…a} [(abc)*→…a]
- Lee `b`: {…a} ⟶ {…ab} […a→…ab]
- Lee `c`: {…ab} ⟶ {(abc)*} […ab→(abc)*]
- Lee `a`: {(abc)*} ⟶ {…a} [(abc)*→…a]
- Lee `b`: {…a} ⟶ {…ab} […a→…ab]
- Lee `c`: {…ab} ⟶ {(abc)*} […ab→(abc)*]
- **Aceptada**: queda {(abc)*} ∈ F.

## Cadena `abcabcabcabc`

- Inicio: {(abc)*}
- Lee `a`: {(abc)*} ⟶ {…a} [(abc)*→…a]
- Lee `b`: {…a} ⟶ {…ab} […a→…ab]
- Lee `c`: {…ab} ⟶ {(abc)*} […ab→(abc)*]
- Lee `a`: {(abc)*} ⟶ {…a} [(abc)*→…a]
- Lee `b`: {…a} ⟶ {…ab} […a→…ab]
- Lee `c`: {…ab} ⟶ {(abc)*} […ab→(abc)*]
- Lee `a`: {(abc)*} ⟶ {…a} [(abc)*→…a]
- Lee `b`: {…a} ⟶ {…ab} […a→…ab]
- Lee `c`: {…ab} ⟶ {(abc)*} […ab→(abc)*]
- Lee `a`: {(abc)*} ⟶ {…a} [(abc)*→…a]
- Lee `b`: {…a} ⟶ {…ab} […a→…ab]
- Lee `c`: {…ab} ⟶ {(abc)*} […ab→(abc)*]
- **Aceptada**: queda {(abc)*} ∈ F.

## Cadena `0`

- Inicio: {(abc)*}
- Lee `0`: {(abc)*} ⟶ ∅ [ninguna transición]
- **Rechazada**: no queda ningún estado activo.

## Cadena `c1`

- Inicio: {(abc)*}
- Lee `c`: {(abc)*} ⟶ ∅ [ninguna transición]
- Lee `1`: ∅ ⟶ ∅ [ninguna transición]
- **Rechazada**: no queda ningún estado activo.

## Cadena `c01b`

- Inicio: {(abc)*}
- Lee `c`: {(abc)*} ⟶ ∅ [ninguna transición]
- Lee `0`: ∅ ⟶ ∅ [ninguna transición]
- Lee `1`: ∅ ⟶ ∅ [ninguna transición]
- Lee `b`: ∅ ⟶ ∅ [ninguna transición]
- **Rechazada**: no queda ningún estado activo.

## Cadena `0a010c`

- Inicio: {(abc)*}
- Lee `0`: {(abc)*} ⟶ ∅ [ninguna transición]
- Lee `a`: ∅ ⟶ ∅ [ninguna transición]
- Lee `0`: ∅ ⟶ ∅ [ninguna transición]
- Lee `1`: ∅ ⟶ ∅ [ninguna transición]
- Lee `0`: ∅ ⟶ ∅ [ninguna transición]
- Lee `c`: ∅ ⟶ ∅ [ninguna transición]
- **Rechazada**: no queda ningún estado activo.

## Cadena `cb010bc0a`

- Inicio: {(abc)*}
- Lee `c`: {(abc)*} ⟶ ∅ [ninguna transición]
- Lee `b`: ∅ ⟶ ∅ [ninguna transición]
- Lee `0`: ∅ ⟶ ∅ [ninguna transición]
- Lee `1`: ∅ ⟶ ∅ [ninguna transición]
- Lee `0`: ∅ ⟶ ∅ [ninguna transición]
- Lee `b`: ∅ ⟶ ∅ [ninguna transición]
- Lee `c`: ∅ ⟶ ∅ [ninguna transición]
- Lee `0`: ∅ ⟶ ∅ [ninguna transición]
- Lee `a`: ∅ ⟶ ∅ [ninguna transición]
- **Rechazada**: no queda ningún estado activo.
