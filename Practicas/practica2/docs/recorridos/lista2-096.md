# Recorridos: Lista 2 · Ejercicio 096

Las palabras de Σ1 con prefijo 20 y longitud 4.

Autómata: `lista2-096` (AFD).

## Cadena `2000`

- Inicio: {L0}
- Lee `2`: {L0} ⟶ {L1} [L0→L1]
- Lee `0`: {L1} ⟶ {L2} [L1→L2]
- Lee `0`: {L2} ⟶ {L3} [L2→L3]
- Lee `0`: {L3} ⟶ {L4} [L3→L4]
- **Aceptada**: queda {L4} ∈ F.

## Cadena `2001`

- Inicio: {L0}
- Lee `2`: {L0} ⟶ {L1} [L0→L1]
- Lee `0`: {L1} ⟶ {L2} [L1→L2]
- Lee `0`: {L2} ⟶ {L3} [L2→L3]
- Lee `1`: {L3} ⟶ {L4} [L3→L4]
- **Aceptada**: queda {L4} ∈ F.

## Cadena `2002`

- Inicio: {L0}
- Lee `2`: {L0} ⟶ {L1} [L0→L1]
- Lee `0`: {L1} ⟶ {L2} [L1→L2]
- Lee `0`: {L2} ⟶ {L3} [L2→L3]
- Lee `2`: {L3} ⟶ {L4} [L3→L4]
- **Aceptada**: queda {L4} ∈ F.

## Cadena `2011`

- Inicio: {L0}
- Lee `2`: {L0} ⟶ {L1} [L0→L1]
- Lee `0`: {L1} ⟶ {L2} [L1→L2]
- Lee `1`: {L2} ⟶ {L3} [L2→L3]
- Lee `1`: {L3} ⟶ {L4} [L3→L4]
- **Aceptada**: queda {L4} ∈ F.

## Cadena `2021`

- Inicio: {L0}
- Lee `2`: {L0} ⟶ {L1} [L0→L1]
- Lee `0`: {L1} ⟶ {L2} [L1→L2]
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
- Lee `1`: {L0} ⟶ {muerto} [L0→muerto]
- Lee `0`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `1`: {muerto} ⟶ {muerto} [muerto→muerto]
- **Rechazada**: ningún estado de {muerto} es de aceptación.

## Cadena `20100`

- Inicio: {L0}
- Lee `2`: {L0} ⟶ {L1} [L0→L1]
- Lee `0`: {L1} ⟶ {L2} [L1→L2]
- Lee `1`: {L2} ⟶ {L3} [L2→L3]
- Lee `0`: {L3} ⟶ {L4} [L3→L4]
- Lee `0`: {L4} ⟶ {muerto} [L4→muerto]
- **Rechazada**: ningún estado de {muerto} es de aceptación.

## Cadena `20122121`

- Inicio: {L0}
- Lee `2`: {L0} ⟶ {L1} [L0→L1]
- Lee `0`: {L1} ⟶ {L2} [L1→L2]
- Lee `1`: {L2} ⟶ {L3} [L2→L3]
- Lee `2`: {L3} ⟶ {L4} [L3→L4]
- Lee `2`: {L4} ⟶ {muerto} [L4→muerto]
- Lee `1`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `2`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `1`: {muerto} ⟶ {muerto} [muerto→muerto]
- **Rechazada**: ningún estado de {muerto} es de aceptación.

## Cadena `2012`

- Inicio: {L0}
- Lee `2`: {L0} ⟶ {L1} [L0→L1]
- Lee `0`: {L1} ⟶ {L2} [L1→L2]
- Lee `1`: {L2} ⟶ {L3} [L2→L3]
- Lee `2`: {L3} ⟶ {L4} [L3→L4]
- **Aceptada**: queda {L4} ∈ F.

## Cadena `210`

- Inicio: {L0}
- Lee `2`: {L0} ⟶ {L1} [L0→L1]
- Lee `1`: {L1} ⟶ {muerto} [L1→muerto]
- Lee `0`: {muerto} ⟶ {muerto} [muerto→muerto]
- **Rechazada**: ningún estado de {muerto} es de aceptación.
