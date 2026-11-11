# Recorridos: Lista 2 · Ejercicio 128

Sea L el lenguaje del autómata del diagrama. Encuentre un AFD para L2 = {w : wa ∈ L para algún símbolo a}.

Autómata: `lista2-128` (AFD).

## Cadena `10`

- Inicio: {A}
- Lee `1`: {A} ⟶ {C} [A→C]
- Lee `0`: {C} ⟶ {D} [C→D]
- **Aceptada**: queda {D} ∈ F.

## Cadena `001`

- Inicio: {A}
- Lee `0`: {A} ⟶ {B} [A→B]
- Lee `0`: {B} ⟶ {C} [B→C]
- Lee `1`: {C} ⟶ {E} [C→E]
- **Aceptada**: queda {E} ∈ F.

## Cadena `10100`

- Inicio: {A}
- Lee `1`: {A} ⟶ {C} [A→C]
- Lee `0`: {C} ⟶ {D} [C→D]
- Lee `1`: {D} ⟶ {E} [D→E]
- Lee `0`: {E} ⟶ {E} [E→E]
- Lee `0`: {E} ⟶ {E} [E→E]
- **Aceptada**: queda {E} ∈ F.

## Cadena `0010101`

- Inicio: {A}
- Lee `0`: {A} ⟶ {B} [A→B]
- Lee `0`: {B} ⟶ {C} [B→C]
- Lee `1`: {C} ⟶ {E} [C→E]
- Lee `0`: {E} ⟶ {E} [E→E]
- Lee `1`: {E} ⟶ {F} [E→F]
- Lee `0`: {F} ⟶ {D} [F→D]
- Lee `1`: {D} ⟶ {E} [D→E]
- **Aceptada**: queda {E} ∈ F.

## Cadena `0100011101`

- Inicio: {A}
- Lee `0`: {A} ⟶ {B} [A→B]
- Lee `1`: {B} ⟶ {D} [B→D]
- Lee `0`: {D} ⟶ {F} [D→F]
- Lee `0`: {F} ⟶ {D} [F→D]
- Lee `0`: {D} ⟶ {F} [D→F]
- Lee `1`: {F} ⟶ {D} [F→D]
- Lee `1`: {D} ⟶ {E} [D→E]
- Lee `1`: {E} ⟶ {F} [E→F]
- Lee `0`: {F} ⟶ {D} [F→D]
- Lee `1`: {D} ⟶ {E} [D→E]
- **Aceptada**: queda {E} ∈ F.

## Cadena λ

- Inicio: {A}
- **Rechazada**: ningún estado de {A} es de aceptación.

## Cadena `1`

- Inicio: {A}
- Lee `1`: {A} ⟶ {C} [A→C]
- **Rechazada**: ningún estado de {C} es de aceptación.

## Cadena `111`

- Inicio: {A}
- Lee `1`: {A} ⟶ {C} [A→C]
- Lee `1`: {C} ⟶ {E} [C→E]
- Lee `1`: {E} ⟶ {F} [E→F]
- **Rechazada**: ningún estado de {F} es de aceptación.

## Cadena `11100`

- Inicio: {A}
- Lee `1`: {A} ⟶ {C} [A→C]
- Lee `1`: {C} ⟶ {E} [C→E]
- Lee `1`: {E} ⟶ {F} [E→F]
- Lee `0`: {F} ⟶ {D} [F→D]
- Lee `0`: {D} ⟶ {F} [D→F]
- **Rechazada**: ningún estado de {F} es de aceptación.

## Cadena `01001001`

- Inicio: {A}
- Lee `0`: {A} ⟶ {B} [A→B]
- Lee `1`: {B} ⟶ {D} [B→D]
- Lee `0`: {D} ⟶ {F} [D→F]
- Lee `0`: {F} ⟶ {D} [F→D]
- Lee `1`: {D} ⟶ {E} [D→E]
- Lee `0`: {E} ⟶ {E} [E→E]
- Lee `0`: {E} ⟶ {E} [E→E]
- Lee `1`: {E} ⟶ {F} [E→F]
- **Rechazada**: ningún estado de {F} es de aceptación.
