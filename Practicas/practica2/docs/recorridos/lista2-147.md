# Recorridos: Lista 2 · Ejercicio 147

AFD que lee un número binario de izquierda a derecha y lo acepta si es múltiplo de 6.

Autómata: `lista2-147` (AFD).

## Cadena `0`

- Inicio: {ini}
- Lee `0`: {ini} ⟶ {r0} [ini→r0]
- **Aceptada**: queda {r0} ∈ F.

## Cadena `00`

- Inicio: {ini}
- Lee `0`: {ini} ⟶ {r0} [ini→r0]
- Lee `0`: {r0} ⟶ {r0} [r0→r0]
- **Aceptada**: queda {r0} ∈ F.

## Cadena `0000`

- Inicio: {ini}
- Lee `0`: {ini} ⟶ {r0} [ini→r0]
- Lee `0`: {r0} ⟶ {r0} [r0→r0]
- Lee `0`: {r0} ⟶ {r0} [r0→r0]
- Lee `0`: {r0} ⟶ {r0} [r0→r0]
- **Aceptada**: queda {r0} ∈ F.

## Cadena `110000`

- Inicio: {ini}
- Lee `1`: {ini} ⟶ {r1} [ini→r1]
- Lee `1`: {r1} ⟶ {r3} [r1→r3]
- Lee `0`: {r3} ⟶ {r0} [r3→r0]
- Lee `0`: {r0} ⟶ {r0} [r0→r0]
- Lee `0`: {r0} ⟶ {r0} [r0→r0]
- Lee `0`: {r0} ⟶ {r0} [r0→r0]
- **Aceptada**: queda {r0} ∈ F.

## Cadena `101010000`

- Inicio: {ini}
- Lee `1`: {ini} ⟶ {r1} [ini→r1]
- Lee `0`: {r1} ⟶ {r2} [r1→r2]
- Lee `1`: {r2} ⟶ {r5} [r2→r5]
- Lee `0`: {r5} ⟶ {r4} [r5→r4]
- Lee `1`: {r4} ⟶ {r3} [r4→r3]
- Lee `0`: {r3} ⟶ {r0} [r3→r0]
- Lee `0`: {r0} ⟶ {r0} [r0→r0]
- Lee `0`: {r0} ⟶ {r0} [r0→r0]
- Lee `0`: {r0} ⟶ {r0} [r0→r0]
- **Aceptada**: queda {r0} ∈ F.

## Cadena λ

- Inicio: {ini}
- **Rechazada**: ningún estado de {ini} es de aceptación.

## Cadena `1`

- Inicio: {ini}
- Lee `1`: {ini} ⟶ {r1} [ini→r1]
- **Rechazada**: ningún estado de {r1} es de aceptación.

## Cadena `010`

- Inicio: {ini}
- Lee `0`: {ini} ⟶ {r0} [ini→r0]
- Lee `1`: {r0} ⟶ {r1} [r0→r1]
- Lee `0`: {r1} ⟶ {r2} [r1→r2]
- **Rechazada**: ningún estado de {r2} es de aceptación.

## Cadena `10111`

- Inicio: {ini}
- Lee `1`: {ini} ⟶ {r1} [ini→r1]
- Lee `0`: {r1} ⟶ {r2} [r1→r2]
- Lee `1`: {r2} ⟶ {r5} [r2→r5]
- Lee `1`: {r5} ⟶ {r5} [r5→r5]
- Lee `1`: {r5} ⟶ {r5} [r5→r5]
- **Rechazada**: ningún estado de {r5} es de aceptación.

## Cadena `01100111`

- Inicio: {ini}
- Lee `0`: {ini} ⟶ {r0} [ini→r0]
- Lee `1`: {r0} ⟶ {r1} [r0→r1]
- Lee `1`: {r1} ⟶ {r3} [r1→r3]
- Lee `0`: {r3} ⟶ {r0} [r3→r0]
- Lee `0`: {r0} ⟶ {r0} [r0→r0]
- Lee `1`: {r0} ⟶ {r1} [r0→r1]
- Lee `1`: {r1} ⟶ {r3} [r1→r3]
- Lee `1`: {r3} ⟶ {r1} [r3→r1]
- **Rechazada**: ningún estado de {r1} es de aceptación.
