# Recorridos: Lista 2 · Ejercicio 120

Las palabras de Σ1 tales que el primer carácter y el último son distintos.

Autómata: `lista2-120` (AFD).

## Cadena `21`

- Inicio: {ini}
- Lee `2`: {ini} ⟶ {2…=} [ini→2…=]
- Lee `1`: {2…=} ⟶ {2…≠} [2…=→2…≠]
- **Aceptada**: queda {2…≠} ∈ F.

## Cadena `012`

- Inicio: {ini}
- Lee `0`: {ini} ⟶ {0…=} [ini→0…=]
- Lee `1`: {0…=} ⟶ {0…≠} [0…=→0…≠]
- Lee `2`: {0…≠} ⟶ {0…≠} [0…≠→0…≠]
- **Aceptada**: queda {0…≠} ∈ F.

## Cadena `20001`

- Inicio: {ini}
- Lee `2`: {ini} ⟶ {2…=} [ini→2…=]
- Lee `0`: {2…=} ⟶ {2…≠} [2…=→2…≠]
- Lee `0`: {2…≠} ⟶ {2…≠} [2…≠→2…≠]
- Lee `0`: {2…≠} ⟶ {2…≠} [2…≠→2…≠]
- Lee `1`: {2…≠} ⟶ {2…≠} [2…≠→2…≠]
- **Aceptada**: queda {2…≠} ∈ F.

## Cadena `0222011`

- Inicio: {ini}
- Lee `0`: {ini} ⟶ {0…=} [ini→0…=]
- Lee `2`: {0…=} ⟶ {0…≠} [0…=→0…≠]
- Lee `2`: {0…≠} ⟶ {0…≠} [0…≠→0…≠]
- Lee `2`: {0…≠} ⟶ {0…≠} [0…≠→0…≠]
- Lee `0`: {0…≠} ⟶ {0…=} [0…≠→0…=]
- Lee `1`: {0…=} ⟶ {0…≠} [0…=→0…≠]
- Lee `1`: {0…≠} ⟶ {0…≠} [0…≠→0…≠]
- **Aceptada**: queda {0…≠} ∈ F.

## Cadena `2022102021`

- Inicio: {ini}
- Lee `2`: {ini} ⟶ {2…=} [ini→2…=]
- Lee `0`: {2…=} ⟶ {2…≠} [2…=→2…≠]
- Lee `2`: {2…≠} ⟶ {2…=} [2…≠→2…=]
- Lee `2`: {2…=} ⟶ {2…=} [2…=→2…=]
- Lee `1`: {2…=} ⟶ {2…≠} [2…=→2…≠]
- Lee `0`: {2…≠} ⟶ {2…≠} [2…≠→2…≠]
- Lee `2`: {2…≠} ⟶ {2…=} [2…≠→2…=]
- Lee `0`: {2…=} ⟶ {2…≠} [2…=→2…≠]
- Lee `2`: {2…≠} ⟶ {2…=} [2…≠→2…=]
- Lee `1`: {2…=} ⟶ {2…≠} [2…=→2…≠]
- **Aceptada**: queda {2…≠} ∈ F.

## Cadena λ

- Inicio: {ini}
- **Rechazada**: ningún estado de {ini} es de aceptación.

## Cadena `0`

- Inicio: {ini}
- Lee `0`: {ini} ⟶ {0…=} [ini→0…=]
- **Rechazada**: ningún estado de {0…=} es de aceptación.

## Cadena `222`

- Inicio: {ini}
- Lee `2`: {ini} ⟶ {2…=} [ini→2…=]
- Lee `2`: {2…=} ⟶ {2…=} [2…=→2…=]
- Lee `2`: {2…=} ⟶ {2…=} [2…=→2…=]
- **Rechazada**: ningún estado de {2…=} es de aceptación.

## Cadena `10011`

- Inicio: {ini}
- Lee `1`: {ini} ⟶ {1…=} [ini→1…=]
- Lee `0`: {1…=} ⟶ {1…≠} [1…=→1…≠]
- Lee `0`: {1…≠} ⟶ {1…≠} [1…≠→1…≠]
- Lee `1`: {1…≠} ⟶ {1…=} [1…≠→1…=]
- Lee `1`: {1…=} ⟶ {1…=} [1…=→1…=]
- **Rechazada**: ningún estado de {1…=} es de aceptación.

## Cadena `10102211`

- Inicio: {ini}
- Lee `1`: {ini} ⟶ {1…=} [ini→1…=]
- Lee `0`: {1…=} ⟶ {1…≠} [1…=→1…≠]
- Lee `1`: {1…≠} ⟶ {1…=} [1…≠→1…=]
- Lee `0`: {1…=} ⟶ {1…≠} [1…=→1…≠]
- Lee `2`: {1…≠} ⟶ {1…≠} [1…≠→1…≠]
- Lee `2`: {1…≠} ⟶ {1…≠} [1…≠→1…≠]
- Lee `1`: {1…≠} ⟶ {1…=} [1…≠→1…=]
- Lee `1`: {1…=} ⟶ {1…=} [1…=→1…=]
- **Rechazada**: ningún estado de {1…=} es de aceptación.

## Cadena `01`

- Inicio: {ini}
- Lee `0`: {ini} ⟶ {0…=} [ini→0…=]
- Lee `1`: {0…=} ⟶ {0…≠} [0…=→0…≠]
- **Aceptada**: queda {0…≠} ∈ F.

## Cadena `1`

- Inicio: {ini}
- Lee `1`: {ini} ⟶ {1…=} [ini→1…=]
- **Rechazada**: ningún estado de {1…=} es de aceptación.
