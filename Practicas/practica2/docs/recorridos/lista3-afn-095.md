# Recorridos: Lista 3 · AFN del problema 095

AFN para el problema 95: Las palabras de Σ1 que tienen longitud 4.

Autómata: `lista3-afn-095` (AFD).

## Cadena `0100`

- Inicio: {L0}
- Lee `0`: {L0} ⟶ {L1} [L0→L1]
- Lee `1`: {L1} ⟶ {L2} [L1→L2]
- Lee `0`: {L2} ⟶ {L3} [L2→L3]
- Lee `0`: {L3} ⟶ {L4} [L3→L4]
- **Aceptada**: queda {L4} ∈ F.

## Cadena `1102`

- Inicio: {L0}
- Lee `1`: {L0} ⟶ {L1} [L0→L1]
- Lee `1`: {L1} ⟶ {L2} [L1→L2]
- Lee `0`: {L2} ⟶ {L3} [L2→L3]
- Lee `2`: {L3} ⟶ {L4} [L3→L4]
- **Aceptada**: queda {L4} ∈ F.

## Cadena `1111`

- Inicio: {L0}
- Lee `1`: {L0} ⟶ {L1} [L0→L1]
- Lee `1`: {L1} ⟶ {L2} [L1→L2]
- Lee `1`: {L2} ⟶ {L3} [L2→L3]
- Lee `1`: {L3} ⟶ {L4} [L3→L4]
- **Aceptada**: queda {L4} ∈ F.

## Cadena `1112`

- Inicio: {L0}
- Lee `1`: {L0} ⟶ {L1} [L0→L1]
- Lee `1`: {L1} ⟶ {L2} [L1→L2]
- Lee `1`: {L2} ⟶ {L3} [L2→L3]
- Lee `2`: {L3} ⟶ {L4} [L3→L4]
- **Aceptada**: queda {L4} ∈ F.

## Cadena `2122`

- Inicio: {L0}
- Lee `2`: {L0} ⟶ {L1} [L0→L1]
- Lee `1`: {L1} ⟶ {L2} [L1→L2]
- Lee `2`: {L2} ⟶ {L3} [L2→L3]
- Lee `2`: {L3} ⟶ {L4} [L3→L4]
- **Aceptada**: queda {L4} ∈ F.

## Cadena λ

- Inicio: {L0}
- **Rechazada**: ningún estado de {L0} es de aceptación.

## Cadena `0`

- Inicio: {L0}
- Lee `0`: {L0} ⟶ {L1} [L0→L1]
- **Rechazada**: ningún estado de {L1} es de aceptación.

## Cadena `221`

- Inicio: {L0}
- Lee `2`: {L0} ⟶ {L1} [L0→L1]
- Lee `2`: {L1} ⟶ {L2} [L1→L2]
- Lee `1`: {L2} ⟶ {L3} [L2→L3]
- **Rechazada**: ningún estado de {L3} es de aceptación.

## Cadena `02020`

- Inicio: {L0}
- Lee `0`: {L0} ⟶ {L1} [L0→L1]
- Lee `2`: {L1} ⟶ {L2} [L1→L2]
- Lee `0`: {L2} ⟶ {L3} [L2→L3]
- Lee `2`: {L3} ⟶ {L4} [L3→L4]
- Lee `0`: {L4} ⟶ ∅ [ninguna transición]
- **Rechazada**: no queda ningún estado activo.

## Cadena `01010112`

- Inicio: {L0}
- Lee `0`: {L0} ⟶ {L1} [L0→L1]
- Lee `1`: {L1} ⟶ {L2} [L1→L2]
- Lee `0`: {L2} ⟶ {L3} [L2→L3]
- Lee `1`: {L3} ⟶ {L4} [L3→L4]
- Lee `0`: {L4} ⟶ ∅ [ninguna transición]
- Lee `1`: ∅ ⟶ ∅ [ninguna transición]
- Lee `1`: ∅ ⟶ ∅ [ninguna transición]
- Lee `2`: ∅ ⟶ ∅ [ninguna transición]
- **Rechazada**: no queda ningún estado activo.

## Cadena `1200`

- Inicio: {L0}
- Lee `1`: {L0} ⟶ {L1} [L0→L1]
- Lee `2`: {L1} ⟶ {L2} [L1→L2]
- Lee `0`: {L2} ⟶ {L3} [L2→L3]
- Lee `0`: {L3} ⟶ {L4} [L3→L4]
- **Aceptada**: queda {L4} ∈ F.

## Cadena `100`

- Inicio: {L0}
- Lee `1`: {L0} ⟶ {L1} [L0→L1]
- Lee `0`: {L1} ⟶ {L2} [L1→L2]
- Lee `0`: {L2} ⟶ {L3} [L2→L3]
- **Rechazada**: ningún estado de {L3} es de aceptación.
