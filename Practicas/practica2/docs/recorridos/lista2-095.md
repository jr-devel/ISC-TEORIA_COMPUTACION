# Recorridos: Lista 2 · Ejercicio 095

Las palabras de Σ1 que tienen longitud 4.

Autómata: `lista2-095` (AFD).

## Cadena `0201`

- Inicio: {L0}
- Lee `0`: {L0} ⟶ {L1} [L0→L1]
- Lee `2`: {L1} ⟶ {L2} [L1→L2]
- Lee `0`: {L2} ⟶ {L3} [L2→L3]
- Lee `1`: {L3} ⟶ {L4} [L3→L4]
- **Aceptada**: queda {L4} ∈ F.

## Cadena `1202`

- Inicio: {L0}
- Lee `1`: {L0} ⟶ {L1} [L0→L1]
- Lee `2`: {L1} ⟶ {L2} [L1→L2]
- Lee `0`: {L2} ⟶ {L3} [L2→L3]
- Lee `2`: {L3} ⟶ {L4} [L3→L4]
- **Aceptada**: queda {L4} ∈ F.

## Cadena `1220`

- Inicio: {L0}
- Lee `1`: {L0} ⟶ {L1} [L0→L1]
- Lee `2`: {L1} ⟶ {L2} [L1→L2]
- Lee `2`: {L2} ⟶ {L3} [L2→L3]
- Lee `0`: {L3} ⟶ {L4} [L3→L4]
- **Aceptada**: queda {L4} ∈ F.

## Cadena `2200`

- Inicio: {L0}
- Lee `2`: {L0} ⟶ {L1} [L0→L1]
- Lee `2`: {L1} ⟶ {L2} [L1→L2]
- Lee `0`: {L2} ⟶ {L3} [L2→L3]
- Lee `0`: {L3} ⟶ {L4} [L3→L4]
- **Aceptada**: queda {L4} ∈ F.

## Cadena `2221`

- Inicio: {L0}
- Lee `2`: {L0} ⟶ {L1} [L0→L1]
- Lee `2`: {L1} ⟶ {L2} [L1→L2]
- Lee `2`: {L2} ⟶ {L3} [L2→L3]
- Lee `1`: {L3} ⟶ {L4} [L3→L4]
- **Aceptada**: queda {L4} ∈ F.

## Cadena λ

- Inicio: {L0}
- **Rechazada**: ningún estado de {L0} es de aceptación.

## Cadena `2`

- Inicio: {L0}
- Lee `2`: {L0} ⟶ {L1} [L0→L1]
- **Rechazada**: ningún estado de {L1} es de aceptación.

## Cadena `101`

- Inicio: {L0}
- Lee `1`: {L0} ⟶ {L1} [L0→L1]
- Lee `0`: {L1} ⟶ {L2} [L1→L2]
- Lee `1`: {L2} ⟶ {L3} [L2→L3]
- **Rechazada**: ningún estado de {L3} es de aceptación.

## Cadena `22002`

- Inicio: {L0}
- Lee `2`: {L0} ⟶ {L1} [L0→L1]
- Lee `2`: {L1} ⟶ {L2} [L1→L2]
- Lee `0`: {L2} ⟶ {L3} [L2→L3]
- Lee `0`: {L3} ⟶ {L4} [L3→L4]
- Lee `2`: {L4} ⟶ {muerto} [L4→muerto]
- **Rechazada**: ningún estado de {muerto} es de aceptación.

## Cadena `00021210`

- Inicio: {L0}
- Lee `0`: {L0} ⟶ {L1} [L0→L1]
- Lee `0`: {L1} ⟶ {L2} [L1→L2]
- Lee `0`: {L2} ⟶ {L3} [L2→L3]
- Lee `2`: {L3} ⟶ {L4} [L3→L4]
- Lee `1`: {L4} ⟶ {muerto} [L4→muerto]
- Lee `2`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `1`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `0`: {muerto} ⟶ {muerto} [muerto→muerto]
- **Rechazada**: ningún estado de {muerto} es de aceptación.

## Cadena `0210`

- Inicio: {L0}
- Lee `0`: {L0} ⟶ {L1} [L0→L1]
- Lee `2`: {L1} ⟶ {L2} [L1→L2]
- Lee `1`: {L2} ⟶ {L3} [L2→L3]
- Lee `0`: {L3} ⟶ {L4} [L3→L4]
- **Aceptada**: queda {L4} ∈ F.

## Cadena `220`

- Inicio: {L0}
- Lee `2`: {L0} ⟶ {L1} [L0→L1]
- Lee `2`: {L1} ⟶ {L2} [L1→L2]
- Lee `0`: {L2} ⟶ {L3} [L2→L3]
- **Rechazada**: ningún estado de {L3} es de aceptación.
