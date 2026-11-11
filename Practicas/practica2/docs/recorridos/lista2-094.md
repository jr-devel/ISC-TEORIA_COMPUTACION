# Recorridos: Lista 2 · Ejercicio 094

Las palabras de Σ1 que comienzan con 1 y terminan con 2.

Autómata: `lista2-094` (AFD).

## Cadena `12`

- Inicio: {ini}
- Lee `1`: {ini} ⟶ {1·} [ini→1·]
- Lee `2`: {1·} ⟶ {1·2} [1·→1·2]
- **Aceptada**: queda {1·2} ∈ F.

## Cadena `102`

- Inicio: {ini}
- Lee `1`: {ini} ⟶ {1·} [ini→1·]
- Lee `0`: {1·} ⟶ {1·} [1·→1·]
- Lee `2`: {1·} ⟶ {1·2} [1·→1·2]
- **Aceptada**: queda {1·2} ∈ F.

## Cadena `10022`

- Inicio: {ini}
- Lee `1`: {ini} ⟶ {1·} [ini→1·]
- Lee `0`: {1·} ⟶ {1·} [1·→1·]
- Lee `0`: {1·} ⟶ {1·} [1·→1·]
- Lee `2`: {1·} ⟶ {1·2} [1·→1·2]
- Lee `2`: {1·2} ⟶ {1·2} [1·2→1·2]
- **Aceptada**: queda {1·2} ∈ F.

## Cadena `1220222`

- Inicio: {ini}
- Lee `1`: {ini} ⟶ {1·} [ini→1·]
- Lee `2`: {1·} ⟶ {1·2} [1·→1·2]
- Lee `2`: {1·2} ⟶ {1·2} [1·2→1·2]
- Lee `0`: {1·2} ⟶ {1·} [1·2→1·]
- Lee `2`: {1·} ⟶ {1·2} [1·→1·2]
- Lee `2`: {1·2} ⟶ {1·2} [1·2→1·2]
- Lee `2`: {1·2} ⟶ {1·2} [1·2→1·2]
- **Aceptada**: queda {1·2} ∈ F.

## Cadena `1212021222`

- Inicio: {ini}
- Lee `1`: {ini} ⟶ {1·} [ini→1·]
- Lee `2`: {1·} ⟶ {1·2} [1·→1·2]
- Lee `1`: {1·2} ⟶ {1·} [1·2→1·]
- Lee `2`: {1·} ⟶ {1·2} [1·→1·2]
- Lee `0`: {1·2} ⟶ {1·} [1·2→1·]
- Lee `2`: {1·} ⟶ {1·2} [1·→1·2]
- Lee `1`: {1·2} ⟶ {1·} [1·2→1·]
- Lee `2`: {1·} ⟶ {1·2} [1·→1·2]
- Lee `2`: {1·2} ⟶ {1·2} [1·2→1·2]
- Lee `2`: {1·2} ⟶ {1·2} [1·2→1·2]
- **Aceptada**: queda {1·2} ∈ F.

## Cadena λ

- Inicio: {ini}
- **Rechazada**: ningún estado de {ini} es de aceptación.

## Cadena `0`

- Inicio: {ini}
- Lee `0`: {ini} ⟶ {muerto} [ini→muerto]
- **Rechazada**: ningún estado de {muerto} es de aceptación.

## Cadena `020`

- Inicio: {ini}
- Lee `0`: {ini} ⟶ {muerto} [ini→muerto]
- Lee `2`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `0`: {muerto} ⟶ {muerto} [muerto→muerto]
- **Rechazada**: ningún estado de {muerto} es de aceptación.

## Cadena `22202`

- Inicio: {ini}
- Lee `2`: {ini} ⟶ {muerto} [ini→muerto]
- Lee `2`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `2`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `0`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `2`: {muerto} ⟶ {muerto} [muerto→muerto]
- **Rechazada**: ningún estado de {muerto} es de aceptación.

## Cadena `10012011`

- Inicio: {ini}
- Lee `1`: {ini} ⟶ {1·} [ini→1·]
- Lee `0`: {1·} ⟶ {1·} [1·→1·]
- Lee `0`: {1·} ⟶ {1·} [1·→1·]
- Lee `1`: {1·} ⟶ {1·} [1·→1·]
- Lee `2`: {1·} ⟶ {1·2} [1·→1·2]
- Lee `0`: {1·2} ⟶ {1·} [1·2→1·]
- Lee `1`: {1·} ⟶ {1·} [1·→1·]
- Lee `1`: {1·} ⟶ {1·} [1·→1·]
- **Rechazada**: ningún estado de {1·} es de aceptación.

## Cadena `2`

- Inicio: {ini}
- Lee `2`: {ini} ⟶ {muerto} [ini→muerto]
- **Rechazada**: ningún estado de {muerto} es de aceptación.
