# Recorridos: Lista 3 · AFN del problema 122

AFN para el problema 122: Las palabras de Σ1 tales que cualquier cadena de tres símbolos consecutivos tiene un 0.

Autómata: `lista3-afn-122` (AFD).

## Cadena λ

- Inicio: {0 sin 0}
- **Aceptada**: queda {0 sin 0} ∈ F.

## Cadena `1`

- Inicio: {0 sin 0}
- Lee `1`: {0 sin 0} ⟶ {1 sin 0} [0 sin 0→1 sin 0]
- **Aceptada**: queda {1 sin 0} ∈ F.

## Cadena `012`

- Inicio: {0 sin 0}
- Lee `0`: {0 sin 0} ⟶ {0 sin 0} [0 sin 0→0 sin 0]
- Lee `1`: {0 sin 0} ⟶ {1 sin 0} [0 sin 0→1 sin 0]
- Lee `2`: {1 sin 0} ⟶ {2 sin 0} [1 sin 0→2 sin 0]
- **Aceptada**: queda {2 sin 0} ∈ F.

## Cadena `20102`

- Inicio: {0 sin 0}
- Lee `2`: {0 sin 0} ⟶ {1 sin 0} [0 sin 0→1 sin 0]
- Lee `0`: {1 sin 0} ⟶ {0 sin 0} [1 sin 0→0 sin 0]
- Lee `1`: {0 sin 0} ⟶ {1 sin 0} [0 sin 0→1 sin 0]
- Lee `0`: {1 sin 0} ⟶ {0 sin 0} [1 sin 0→0 sin 0]
- Lee `2`: {0 sin 0} ⟶ {1 sin 0} [0 sin 0→1 sin 0]
- **Aceptada**: queda {1 sin 0} ∈ F.

## Cadena `10200220`

- Inicio: {0 sin 0}
- Lee `1`: {0 sin 0} ⟶ {1 sin 0} [0 sin 0→1 sin 0]
- Lee `0`: {1 sin 0} ⟶ {0 sin 0} [1 sin 0→0 sin 0]
- Lee `2`: {0 sin 0} ⟶ {1 sin 0} [0 sin 0→1 sin 0]
- Lee `0`: {1 sin 0} ⟶ {0 sin 0} [1 sin 0→0 sin 0]
- Lee `0`: {0 sin 0} ⟶ {0 sin 0} [0 sin 0→0 sin 0]
- Lee `2`: {0 sin 0} ⟶ {1 sin 0} [0 sin 0→1 sin 0]
- Lee `2`: {1 sin 0} ⟶ {2 sin 0} [1 sin 0→2 sin 0]
- Lee `0`: {2 sin 0} ⟶ {0 sin 0} [2 sin 0→0 sin 0]
- **Aceptada**: queda {0 sin 0} ∈ F.

## Cadena `112`

- Inicio: {0 sin 0}
- Lee `1`: {0 sin 0} ⟶ {1 sin 0} [0 sin 0→1 sin 0]
- Lee `1`: {1 sin 0} ⟶ {2 sin 0} [1 sin 0→2 sin 0]
- Lee `2`: {2 sin 0} ⟶ ∅ [ninguna transición]
- **Rechazada**: no queda ningún estado activo.

## Cadena `1120`

- Inicio: {0 sin 0}
- Lee `1`: {0 sin 0} ⟶ {1 sin 0} [0 sin 0→1 sin 0]
- Lee `1`: {1 sin 0} ⟶ {2 sin 0} [1 sin 0→2 sin 0]
- Lee `2`: {2 sin 0} ⟶ ∅ [ninguna transición]
- Lee `0`: ∅ ⟶ ∅ [ninguna transición]
- **Rechazada**: no queda ningún estado activo.

## Cadena `202211`

- Inicio: {0 sin 0}
- Lee `2`: {0 sin 0} ⟶ {1 sin 0} [0 sin 0→1 sin 0]
- Lee `0`: {1 sin 0} ⟶ {0 sin 0} [1 sin 0→0 sin 0]
- Lee `2`: {0 sin 0} ⟶ {1 sin 0} [0 sin 0→1 sin 0]
- Lee `2`: {1 sin 0} ⟶ {2 sin 0} [1 sin 0→2 sin 0]
- Lee `1`: {2 sin 0} ⟶ ∅ [ninguna transición]
- Lee `1`: ∅ ⟶ ∅ [ninguna transición]
- **Rechazada**: no queda ningún estado activo.

## Cadena `01200211`

- Inicio: {0 sin 0}
- Lee `0`: {0 sin 0} ⟶ {0 sin 0} [0 sin 0→0 sin 0]
- Lee `1`: {0 sin 0} ⟶ {1 sin 0} [0 sin 0→1 sin 0]
- Lee `2`: {1 sin 0} ⟶ {2 sin 0} [1 sin 0→2 sin 0]
- Lee `0`: {2 sin 0} ⟶ {0 sin 0} [2 sin 0→0 sin 0]
- Lee `0`: {0 sin 0} ⟶ {0 sin 0} [0 sin 0→0 sin 0]
- Lee `2`: {0 sin 0} ⟶ {1 sin 0} [0 sin 0→1 sin 0]
- Lee `1`: {1 sin 0} ⟶ {2 sin 0} [1 sin 0→2 sin 0]
- Lee `1`: {2 sin 0} ⟶ ∅ [ninguna transición]
- **Rechazada**: no queda ningún estado activo.

## Cadena `00221111212`

- Inicio: {0 sin 0}
- Lee `0`: {0 sin 0} ⟶ {0 sin 0} [0 sin 0→0 sin 0]
- Lee `0`: {0 sin 0} ⟶ {0 sin 0} [0 sin 0→0 sin 0]
- Lee `2`: {0 sin 0} ⟶ {1 sin 0} [0 sin 0→1 sin 0]
- Lee `2`: {1 sin 0} ⟶ {2 sin 0} [1 sin 0→2 sin 0]
- Lee `1`: {2 sin 0} ⟶ ∅ [ninguna transición]
- Lee `1`: ∅ ⟶ ∅ [ninguna transición]
- Lee `1`: ∅ ⟶ ∅ [ninguna transición]
- Lee `1`: ∅ ⟶ ∅ [ninguna transición]
- Lee `2`: ∅ ⟶ ∅ [ninguna transición]
- Lee `1`: ∅ ⟶ ∅ [ninguna transición]
- Lee `2`: ∅ ⟶ ∅ [ninguna transición]
- **Rechazada**: no queda ningún estado activo.
