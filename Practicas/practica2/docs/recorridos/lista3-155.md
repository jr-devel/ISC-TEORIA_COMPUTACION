# Recorridos: Lista 3 · Ejercicio 155

Diagrama y simplificación del AFD de la tabla 155.

Autómata: `lista3-155` (AFD).

## Cadena `010`

- Inicio: {A}
- Lee `0`: {A} ⟶ {B} [A→B]
- Lee `1`: {B} ⟶ {E} [B→E]
- Lee `0`: {E} ⟶ {F} [E→F]
- **Aceptada**: queda {F} ∈ F.

## Cadena `1100`

- Inicio: {A}
- Lee `1`: {A} ⟶ {C} [A→C]
- Lee `1`: {C} ⟶ {G} [C→G]
- Lee `0`: {G} ⟶ {E} [G→E]
- Lee `0`: {E} ⟶ {F} [E→F]
- **Aceptada**: queda {F} ∈ F.

## Cadena `101010`

- Inicio: {A}
- Lee `1`: {A} ⟶ {C} [A→C]
- Lee `0`: {C} ⟶ {K} [C→K]
- Lee `1`: {K} ⟶ {D} [K→D]
- Lee `0`: {D} ⟶ {H} [D→H]
- Lee `1`: {H} ⟶ {K} [H→K]
- Lee `0`: {K} ⟶ {F} [K→F]
- **Aceptada**: queda {F} ∈ F.

## Cadena `01101110`

- Inicio: {A}
- Lee `0`: {A} ⟶ {B} [A→B]
- Lee `1`: {B} ⟶ {E} [B→E]
- Lee `1`: {E} ⟶ {D} [E→D]
- Lee `0`: {D} ⟶ {H} [D→H]
- Lee `1`: {H} ⟶ {K} [H→K]
- Lee `1`: {K} ⟶ {D} [K→D]
- Lee `1`: {D} ⟶ {E} [D→E]
- Lee `0`: {E} ⟶ {F} [E→F]
- **Aceptada**: queda {F} ∈ F.

## Cadena `01101101110`

- Inicio: {A}
- Lee `0`: {A} ⟶ {B} [A→B]
- Lee `1`: {B} ⟶ {E} [B→E]
- Lee `1`: {E} ⟶ {D} [E→D]
- Lee `0`: {D} ⟶ {H} [D→H]
- Lee `1`: {H} ⟶ {K} [H→K]
- Lee `1`: {K} ⟶ {D} [K→D]
- Lee `0`: {D} ⟶ {H} [D→H]
- Lee `1`: {H} ⟶ {K} [H→K]
- Lee `1`: {K} ⟶ {D} [K→D]
- Lee `1`: {D} ⟶ {E} [D→E]
- Lee `0`: {E} ⟶ {F} [E→F]
- **Aceptada**: queda {F} ∈ F.

## Cadena λ

- Inicio: {A}
- **Rechazada**: ningún estado de {A} es de aceptación.

## Cadena `0`

- Inicio: {A}
- Lee `0`: {A} ⟶ {B} [A→B]
- **Rechazada**: ningún estado de {B} es de aceptación.

## Cadena `110`

- Inicio: {A}
- Lee `1`: {A} ⟶ {C} [A→C]
- Lee `1`: {C} ⟶ {G} [C→G]
- Lee `0`: {G} ⟶ {E} [G→E]
- **Rechazada**: ningún estado de {E} es de aceptación.

## Cadena `01011`

- Inicio: {A}
- Lee `0`: {A} ⟶ {B} [A→B]
- Lee `1`: {B} ⟶ {E} [B→E]
- Lee `0`: {E} ⟶ {F} [E→F]
- Lee `1`: {F} ⟶ {G} [F→G]
- Lee `1`: {G} ⟶ {G} [G→G]
- **Rechazada**: ningún estado de {G} es de aceptación.

## Cadena `11011100`

- Inicio: {A}
- Lee `1`: {A} ⟶ {C} [A→C]
- Lee `1`: {C} ⟶ {G} [C→G]
- Lee `0`: {G} ⟶ {E} [G→E]
- Lee `1`: {E} ⟶ {D} [E→D]
- Lee `1`: {D} ⟶ {E} [D→E]
- Lee `1`: {E} ⟶ {D} [E→D]
- Lee `0`: {D} ⟶ {H} [D→H]
- Lee `0`: {H} ⟶ {B} [H→B]
- **Rechazada**: ningún estado de {B} es de aceptación.

## Cadena `01`

- Inicio: {A}
- Lee `0`: {A} ⟶ {B} [A→B]
- Lee `1`: {B} ⟶ {E} [B→E]
- **Rechazada**: ningún estado de {E} es de aceptación.
