# Recorridos: Lista 3 · AFN del problema 121

AFN para el problema 121: Las palabras de Σ1 de longitud 3n tales que cada bloque de longitud 3 tiene al menos un 0.

Autómata: `lista3-afn-121` (AFD).

## Cadena λ

- Inicio: {b0}
- **Aceptada**: queda {b0} ∈ F.

## Cadena `021`

- Inicio: {b0}
- Lee `0`: {b0} ⟶ {b1+0} [b0→b1+0]
- Lee `2`: {b1+0} ⟶ {b2+0} [b1+0→b2+0]
- Lee `1`: {b2+0} ⟶ {b0} [b2+0→b0]
- **Aceptada**: queda {b0} ∈ F.

## Cadena `020001`

- Inicio: {b0}
- Lee `0`: {b0} ⟶ {b1+0} [b0→b1+0]
- Lee `2`: {b1+0} ⟶ {b2+0} [b1+0→b2+0]
- Lee `0`: {b2+0} ⟶ {b0} [b2+0→b0]
- Lee `0`: {b0} ⟶ {b1+0} [b0→b1+0]
- Lee `0`: {b1+0} ⟶ {b2+0} [b1+0→b2+0]
- Lee `1`: {b2+0} ⟶ {b0} [b2+0→b0]
- **Aceptada**: queda {b0} ∈ F.

## Cadena `120100`

- Inicio: {b0}
- Lee `1`: {b0} ⟶ {b1} [b0→b1]
- Lee `2`: {b1} ⟶ {b2} [b1→b2]
- Lee `0`: {b2} ⟶ {b0} [b2→b0]
- Lee `1`: {b0} ⟶ {b1} [b0→b1]
- Lee `0`: {b1} ⟶ {b2+0} [b1→b2+0]
- Lee `0`: {b2+0} ⟶ {b0} [b2+0→b0]
- **Aceptada**: queda {b0} ∈ F.

## Cadena `021022022`

- Inicio: {b0}
- Lee `0`: {b0} ⟶ {b1+0} [b0→b1+0]
- Lee `2`: {b1+0} ⟶ {b2+0} [b1+0→b2+0]
- Lee `1`: {b2+0} ⟶ {b0} [b2+0→b0]
- Lee `0`: {b0} ⟶ {b1+0} [b0→b1+0]
- Lee `2`: {b1+0} ⟶ {b2+0} [b1+0→b2+0]
- Lee `2`: {b2+0} ⟶ {b0} [b2+0→b0]
- Lee `0`: {b0} ⟶ {b1+0} [b0→b1+0]
- Lee `2`: {b1+0} ⟶ {b2+0} [b1+0→b2+0]
- Lee `2`: {b2+0} ⟶ {b0} [b2+0→b0]
- **Aceptada**: queda {b0} ∈ F.

## Cadena `2`

- Inicio: {b0}
- Lee `2`: {b0} ⟶ {b1} [b0→b1]
- **Rechazada**: ningún estado de {b1} es de aceptación.

## Cadena `01`

- Inicio: {b0}
- Lee `0`: {b0} ⟶ {b1+0} [b0→b1+0]
- Lee `1`: {b1+0} ⟶ {b2+0} [b1+0→b2+0]
- **Rechazada**: ningún estado de {b2+0} es de aceptación.

## Cadena `0022`

- Inicio: {b0}
- Lee `0`: {b0} ⟶ {b1+0} [b0→b1+0]
- Lee `0`: {b1+0} ⟶ {b2+0} [b1+0→b2+0]
- Lee `2`: {b2+0} ⟶ {b0} [b2+0→b0]
- Lee `2`: {b0} ⟶ {b1} [b0→b1]
- **Rechazada**: ningún estado de {b1} es de aceptación.

## Cadena `011222`

- Inicio: {b0}
- Lee `0`: {b0} ⟶ {b1+0} [b0→b1+0]
- Lee `1`: {b1+0} ⟶ {b2+0} [b1+0→b2+0]
- Lee `1`: {b2+0} ⟶ {b0} [b2+0→b0]
- Lee `2`: {b0} ⟶ {b1} [b0→b1]
- Lee `2`: {b1} ⟶ {b2} [b1→b2]
- Lee `2`: {b2} ⟶ ∅ [ninguna transición]
- **Rechazada**: no queda ningún estado activo.

## Cadena `210110211`

- Inicio: {b0}
- Lee `2`: {b0} ⟶ {b1} [b0→b1]
- Lee `1`: {b1} ⟶ {b2} [b1→b2]
- Lee `0`: {b2} ⟶ {b0} [b2→b0]
- Lee `1`: {b0} ⟶ {b1} [b0→b1]
- Lee `1`: {b1} ⟶ {b2} [b1→b2]
- Lee `0`: {b2} ⟶ {b0} [b2→b0]
- Lee `2`: {b0} ⟶ {b1} [b0→b1]
- Lee `1`: {b1} ⟶ {b2} [b1→b2]
- Lee `1`: {b2} ⟶ ∅ [ninguna transición]
- **Rechazada**: no queda ningún estado activo.
