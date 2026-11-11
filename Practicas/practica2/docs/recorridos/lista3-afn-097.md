# Recorridos: Lista 3 · AFN del problema 097

AFN para el problema 97: Las palabras de Σ1 cuya longitud es un múltiplo de 3.

Autómata: `lista3-afn-097` (AFD).

## Cadena λ

- Inicio: {r0}
- **Aceptada**: queda {r0} ∈ F.

## Cadena `120`

- Inicio: {r0}
- Lee `1`: {r0} ⟶ {r1} [r0→r1]
- Lee `2`: {r1} ⟶ {r2} [r1→r2]
- Lee `0`: {r2} ⟶ {r0} [r2→r0]
- **Aceptada**: queda {r0} ∈ F.

## Cadena `200`

- Inicio: {r0}
- Lee `2`: {r0} ⟶ {r1} [r0→r1]
- Lee `0`: {r1} ⟶ {r2} [r1→r2]
- Lee `0`: {r2} ⟶ {r0} [r2→r0]
- **Aceptada**: queda {r0} ∈ F.

## Cadena `100020`

- Inicio: {r0}
- Lee `1`: {r0} ⟶ {r1} [r0→r1]
- Lee `0`: {r1} ⟶ {r2} [r1→r2]
- Lee `0`: {r2} ⟶ {r0} [r2→r0]
- Lee `0`: {r0} ⟶ {r1} [r0→r1]
- Lee `2`: {r1} ⟶ {r2} [r1→r2]
- Lee `0`: {r2} ⟶ {r0} [r2→r0]
- **Aceptada**: queda {r0} ∈ F.

## Cadena `121121201`

- Inicio: {r0}
- Lee `1`: {r0} ⟶ {r1} [r0→r1]
- Lee `2`: {r1} ⟶ {r2} [r1→r2]
- Lee `1`: {r2} ⟶ {r0} [r2→r0]
- Lee `1`: {r0} ⟶ {r1} [r0→r1]
- Lee `2`: {r1} ⟶ {r2} [r1→r2]
- Lee `1`: {r2} ⟶ {r0} [r2→r0]
- Lee `2`: {r0} ⟶ {r1} [r0→r1]
- Lee `0`: {r1} ⟶ {r2} [r1→r2]
- Lee `1`: {r2} ⟶ {r0} [r2→r0]
- **Aceptada**: queda {r0} ∈ F.

## Cadena `1`

- Inicio: {r0}
- Lee `1`: {r0} ⟶ {r1} [r0→r1]
- **Rechazada**: ningún estado de {r1} es de aceptación.

## Cadena `21`

- Inicio: {r0}
- Lee `2`: {r0} ⟶ {r1} [r0→r1]
- Lee `1`: {r1} ⟶ {r2} [r1→r2]
- **Rechazada**: ningún estado de {r2} es de aceptación.

## Cadena `2102`

- Inicio: {r0}
- Lee `2`: {r0} ⟶ {r1} [r0→r1]
- Lee `1`: {r1} ⟶ {r2} [r1→r2]
- Lee `0`: {r2} ⟶ {r0} [r2→r0]
- Lee `2`: {r0} ⟶ {r1} [r0→r1]
- **Rechazada**: ningún estado de {r1} es de aceptación.

## Cadena `01102021`

- Inicio: {r0}
- Lee `0`: {r0} ⟶ {r1} [r0→r1]
- Lee `1`: {r1} ⟶ {r2} [r1→r2]
- Lee `1`: {r2} ⟶ {r0} [r2→r0]
- Lee `0`: {r0} ⟶ {r1} [r0→r1]
- Lee `2`: {r1} ⟶ {r2} [r1→r2]
- Lee `0`: {r2} ⟶ {r0} [r2→r0]
- Lee `2`: {r0} ⟶ {r1} [r0→r1]
- Lee `1`: {r1} ⟶ {r2} [r1→r2]
- **Rechazada**: ningún estado de {r2} es de aceptación.

## Cadena `12220210`

- Inicio: {r0}
- Lee `1`: {r0} ⟶ {r1} [r0→r1]
- Lee `2`: {r1} ⟶ {r2} [r1→r2]
- Lee `2`: {r2} ⟶ {r0} [r2→r0]
- Lee `2`: {r0} ⟶ {r1} [r0→r1]
- Lee `0`: {r1} ⟶ {r2} [r1→r2]
- Lee `2`: {r2} ⟶ {r0} [r2→r0]
- Lee `1`: {r0} ⟶ {r1} [r0→r1]
- Lee `0`: {r1} ⟶ {r2} [r1→r2]
- **Rechazada**: ningún estado de {r2} es de aceptación.
