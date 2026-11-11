# Recorridos: Lista 2 · Ejercicio 121

Las palabras de Σ1 de longitud 3n tales que cada bloque de longitud 3 tiene al menos un 0.

Autómata: `lista2-121` (AFD).

## Cadena λ

- Inicio: {b0}
- **Aceptada**: queda {b0} ∈ F.

## Cadena `011`

- Inicio: {b0}
- Lee `0`: {b0} ⟶ {b1+0} [b0→b1+0]
- Lee `1`: {b1+0} ⟶ {b2+0} [b1+0→b2+0]
- Lee `1`: {b2+0} ⟶ {b0} [b2+0→b0]
- **Aceptada**: queda {b0} ∈ F.

## Cadena `012220`

- Inicio: {b0}
- Lee `0`: {b0} ⟶ {b1+0} [b0→b1+0]
- Lee `1`: {b1+0} ⟶ {b2+0} [b1+0→b2+0]
- Lee `2`: {b2+0} ⟶ {b0} [b2+0→b0]
- Lee `2`: {b0} ⟶ {b1} [b0→b1]
- Lee `2`: {b1} ⟶ {b2} [b1→b2]
- Lee `0`: {b2} ⟶ {b0} [b2→b0]
- **Aceptada**: queda {b0} ∈ F.

## Cadena `012020210`

- Inicio: {b0}
- Lee `0`: {b0} ⟶ {b1+0} [b0→b1+0]
- Lee `1`: {b1+0} ⟶ {b2+0} [b1+0→b2+0]
- Lee `2`: {b2+0} ⟶ {b0} [b2+0→b0]
- Lee `0`: {b0} ⟶ {b1+0} [b0→b1+0]
- Lee `2`: {b1+0} ⟶ {b2+0} [b1+0→b2+0]
- Lee `0`: {b2+0} ⟶ {b0} [b2+0→b0]
- Lee `2`: {b0} ⟶ {b1} [b0→b1]
- Lee `1`: {b1} ⟶ {b2} [b1→b2]
- Lee `0`: {b2} ⟶ {b0} [b2→b0]
- **Aceptada**: queda {b0} ∈ F.

## Cadena `100100102`

- Inicio: {b0}
- Lee `1`: {b0} ⟶ {b1} [b0→b1]
- Lee `0`: {b1} ⟶ {b2+0} [b1→b2+0]
- Lee `0`: {b2+0} ⟶ {b0} [b2+0→b0]
- Lee `1`: {b0} ⟶ {b1} [b0→b1]
- Lee `0`: {b1} ⟶ {b2+0} [b1→b2+0]
- Lee `0`: {b2+0} ⟶ {b0} [b2+0→b0]
- Lee `1`: {b0} ⟶ {b1} [b0→b1]
- Lee `0`: {b1} ⟶ {b2+0} [b1→b2+0]
- Lee `2`: {b2+0} ⟶ {b0} [b2+0→b0]
- **Aceptada**: queda {b0} ∈ F.

## Cadena `2`

- Inicio: {b0}
- Lee `2`: {b0} ⟶ {b1} [b0→b1]
- **Rechazada**: ningún estado de {b1} es de aceptación.

## Cadena `02`

- Inicio: {b0}
- Lee `0`: {b0} ⟶ {b1+0} [b0→b1+0]
- Lee `2`: {b1+0} ⟶ {b2+0} [b1+0→b2+0]
- **Rechazada**: ningún estado de {b2+0} es de aceptación.

## Cadena `0202`

- Inicio: {b0}
- Lee `0`: {b0} ⟶ {b1+0} [b0→b1+0]
- Lee `2`: {b1+0} ⟶ {b2+0} [b1+0→b2+0]
- Lee `0`: {b2+0} ⟶ {b0} [b2+0→b0]
- Lee `2`: {b0} ⟶ {b1} [b0→b1]
- **Rechazada**: ningún estado de {b1} es de aceptación.

## Cadena `111101`

- Inicio: {b0}
- Lee `1`: {b0} ⟶ {b1} [b0→b1]
- Lee `1`: {b1} ⟶ {b2} [b1→b2]
- Lee `1`: {b2} ⟶ {muerto} [b2→muerto]
- Lee `1`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `0`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `1`: {muerto} ⟶ {muerto} [muerto→muerto]
- **Rechazada**: ningún estado de {muerto} es de aceptación.

## Cadena `002111012`

- Inicio: {b0}
- Lee `0`: {b0} ⟶ {b1+0} [b0→b1+0]
- Lee `0`: {b1+0} ⟶ {b2+0} [b1+0→b2+0]
- Lee `2`: {b2+0} ⟶ {b0} [b2+0→b0]
- Lee `1`: {b0} ⟶ {b1} [b0→b1]
- Lee `1`: {b1} ⟶ {b2} [b1→b2]
- Lee `1`: {b2} ⟶ {muerto} [b2→muerto]
- Lee `0`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `1`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `2`: {muerto} ⟶ {muerto} [muerto→muerto]
- **Rechazada**: ningún estado de {muerto} es de aceptación.
