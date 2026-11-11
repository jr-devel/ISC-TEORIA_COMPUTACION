# Recorridos: Lista 3 · AFN del problema 096

AFN para el problema 96: Las palabras de Σ1 con prefijo 20 y longitud 4.

Autómata: `lista3-afn-096` (AFD).

## Cadena `2001`

- Inicio: {L0}
- Lee `2`: {L0} ⟶ {L1} [L0→L1]
- Lee `0`: {L1} ⟶ {L2} [L1→L2]
- Lee `0`: {L2} ⟶ {L3} [L2→L3]
- Lee `1`: {L3} ⟶ {L4} [L3→L4]
- **Aceptada**: queda {L4} ∈ F.

## Cadena `2010`

- Inicio: {L0}
- Lee `2`: {L0} ⟶ {L1} [L0→L1]
- Lee `0`: {L1} ⟶ {L2} [L1→L2]
- Lee `1`: {L2} ⟶ {L3} [L2→L3]
- Lee `0`: {L3} ⟶ {L4} [L3→L4]
- **Aceptada**: queda {L4} ∈ F.

## Cadena `2011`

- Inicio: {L0}
- Lee `2`: {L0} ⟶ {L1} [L0→L1]
- Lee `0`: {L1} ⟶ {L2} [L1→L2]
- Lee `1`: {L2} ⟶ {L3} [L2→L3]
- Lee `1`: {L3} ⟶ {L4} [L3→L4]
- **Aceptada**: queda {L4} ∈ F.

## Cadena `2020`

- Inicio: {L0}
- Lee `2`: {L0} ⟶ {L1} [L0→L1]
- Lee `0`: {L1} ⟶ {L2} [L1→L2]
- Lee `2`: {L2} ⟶ {L3} [L2→L3]
- Lee `0`: {L3} ⟶ {L4} [L3→L4]
- **Aceptada**: queda {L4} ∈ F.

## Cadena `2022`

- Inicio: {L0}
- Lee `2`: {L0} ⟶ {L1} [L0→L1]
- Lee `0`: {L1} ⟶ {L2} [L1→L2]
- Lee `2`: {L2} ⟶ {L3} [L2→L3]
- Lee `2`: {L3} ⟶ {L4} [L3→L4]
- **Aceptada**: queda {L4} ∈ F.

## Cadena λ

- Inicio: {L0}
- **Rechazada**: ningún estado de {L0} es de aceptación.

## Cadena `1`

- Inicio: {L0}
- Lee `1`: {L0} ⟶ ∅ [ninguna transición]
- **Rechazada**: no queda ningún estado activo.

## Cadena `220`

- Inicio: {L0}
- Lee `2`: {L0} ⟶ {L1} [L0→L1]
- Lee `2`: {L1} ⟶ ∅ [ninguna transición]
- Lee `0`: ∅ ⟶ ∅ [ninguna transición]
- **Rechazada**: no queda ningún estado activo.

## Cadena `02000`

- Inicio: {L0}
- Lee `0`: {L0} ⟶ ∅ [ninguna transición]
- Lee `2`: ∅ ⟶ ∅ [ninguna transición]
- Lee `0`: ∅ ⟶ ∅ [ninguna transición]
- Lee `0`: ∅ ⟶ ∅ [ninguna transición]
- Lee `0`: ∅ ⟶ ∅ [ninguna transición]
- **Rechazada**: no queda ningún estado activo.

## Cadena `11121222`

- Inicio: {L0}
- Lee `1`: {L0} ⟶ ∅ [ninguna transición]
- Lee `1`: ∅ ⟶ ∅ [ninguna transición]
- Lee `1`: ∅ ⟶ ∅ [ninguna transición]
- Lee `2`: ∅ ⟶ ∅ [ninguna transición]
- Lee `1`: ∅ ⟶ ∅ [ninguna transición]
- Lee `2`: ∅ ⟶ ∅ [ninguna transición]
- Lee `2`: ∅ ⟶ ∅ [ninguna transición]
- Lee `2`: ∅ ⟶ ∅ [ninguna transición]
- **Rechazada**: no queda ningún estado activo.

## Cadena `2021`

- Inicio: {L0}
- Lee `2`: {L0} ⟶ {L1} [L0→L1]
- Lee `0`: {L1} ⟶ {L2} [L1→L2]
- Lee `2`: {L2} ⟶ {L3} [L2→L3]
- Lee `1`: {L3} ⟶ {L4} [L3→L4]
- **Aceptada**: queda {L4} ∈ F.

## Cadena `121`

- Inicio: {L0}
- Lee `1`: {L0} ⟶ ∅ [ninguna transición]
- Lee `2`: ∅ ⟶ ∅ [ninguna transición]
- Lee `1`: ∅ ⟶ ∅ [ninguna transición]
- **Rechazada**: no queda ningún estado activo.
