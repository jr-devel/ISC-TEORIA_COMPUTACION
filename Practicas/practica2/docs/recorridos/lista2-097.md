# Recorridos: Lista 2 · Ejercicio 097

Las palabras de Σ1 cuya longitud es un múltiplo de 3.

Autómata: `lista2-097` (AFD).

## Cadena λ

- Inicio: {r0}
- **Aceptada**: queda {r0} ∈ F.

## Cadena `212200`

- Inicio: {r0}
- Lee `2`: {r0} ⟶ {r1} [r0→r1]
- Lee `1`: {r1} ⟶ {r2} [r1→r2]
- Lee `2`: {r2} ⟶ {r0} [r2→r0]
- Lee `2`: {r0} ⟶ {r1} [r0→r1]
- Lee `0`: {r1} ⟶ {r2} [r1→r2]
- Lee `0`: {r2} ⟶ {r0} [r2→r0]
- **Aceptada**: queda {r0} ∈ F.

## Cadena `100022002`

- Inicio: {r0}
- Lee `1`: {r0} ⟶ {r1} [r0→r1]
- Lee `0`: {r1} ⟶ {r2} [r1→r2]
- Lee `0`: {r2} ⟶ {r0} [r2→r0]
- Lee `0`: {r0} ⟶ {r1} [r0→r1]
- Lee `2`: {r1} ⟶ {r2} [r1→r2]
- Lee `2`: {r2} ⟶ {r0} [r2→r0]
- Lee `0`: {r0} ⟶ {r1} [r0→r1]
- Lee `0`: {r1} ⟶ {r2} [r1→r2]
- Lee `2`: {r2} ⟶ {r0} [r2→r0]
- **Aceptada**: queda {r0} ∈ F.

## Cadena `120000112`

- Inicio: {r0}
- Lee `1`: {r0} ⟶ {r1} [r0→r1]
- Lee `2`: {r1} ⟶ {r2} [r1→r2]
- Lee `0`: {r2} ⟶ {r0} [r2→r0]
- Lee `0`: {r0} ⟶ {r1} [r0→r1]
- Lee `0`: {r1} ⟶ {r2} [r1→r2]
- Lee `0`: {r2} ⟶ {r0} [r2→r0]
- Lee `1`: {r0} ⟶ {r1} [r0→r1]
- Lee `1`: {r1} ⟶ {r2} [r1→r2]
- Lee `2`: {r2} ⟶ {r0} [r2→r0]
- **Aceptada**: queda {r0} ∈ F.

## Cadena `222022020`

- Inicio: {r0}
- Lee `2`: {r0} ⟶ {r1} [r0→r1]
- Lee `2`: {r1} ⟶ {r2} [r1→r2]
- Lee `2`: {r2} ⟶ {r0} [r2→r0]
- Lee `0`: {r0} ⟶ {r1} [r0→r1]
- Lee `2`: {r1} ⟶ {r2} [r1→r2]
- Lee `2`: {r2} ⟶ {r0} [r2→r0]
- Lee `0`: {r0} ⟶ {r1} [r0→r1]
- Lee `2`: {r1} ⟶ {r2} [r1→r2]
- Lee `0`: {r2} ⟶ {r0} [r2→r0]
- **Aceptada**: queda {r0} ∈ F.

## Cadena `1`

- Inicio: {r0}
- Lee `1`: {r0} ⟶ {r1} [r0→r1]
- **Rechazada**: ningún estado de {r1} es de aceptación.

## Cadena `20`

- Inicio: {r0}
- Lee `2`: {r0} ⟶ {r1} [r0→r1]
- Lee `0`: {r1} ⟶ {r2} [r1→r2]
- **Rechazada**: ningún estado de {r2} es de aceptación.

## Cadena `0100`

- Inicio: {r0}
- Lee `0`: {r0} ⟶ {r1} [r0→r1]
- Lee `1`: {r1} ⟶ {r2} [r1→r2]
- Lee `0`: {r2} ⟶ {r0} [r2→r0]
- Lee `0`: {r0} ⟶ {r1} [r0→r1]
- **Rechazada**: ningún estado de {r1} es de aceptación.

## Cadena `0102`

- Inicio: {r0}
- Lee `0`: {r0} ⟶ {r1} [r0→r1]
- Lee `1`: {r1} ⟶ {r2} [r1→r2]
- Lee `0`: {r2} ⟶ {r0} [r2→r0]
- Lee `2`: {r0} ⟶ {r1} [r0→r1]
- **Rechazada**: ningún estado de {r1} es de aceptación.

## Cadena `00110`

- Inicio: {r0}
- Lee `0`: {r0} ⟶ {r1} [r0→r1]
- Lee `0`: {r1} ⟶ {r2} [r1→r2]
- Lee `1`: {r2} ⟶ {r0} [r2→r0]
- Lee `1`: {r0} ⟶ {r1} [r0→r1]
- Lee `0`: {r1} ⟶ {r2} [r1→r2]
- **Rechazada**: ningún estado de {r2} es de aceptación.
