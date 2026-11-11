# Recorridos: Lista 3 · Ejercicio 260

AFD equivalente al AFN de la tabla 260; describa cómo se obtuvo.

Autómata: `lista3-260` (AFN).

## Cadena `10`

- Inicio: {A}
- Lee `1`: {A} ⟶ {B, C} [A→B, A→C] (bifurcación)
- Lee `0`: {B, C} ⟶ {A, B, C, D} [B→A, B→B, B→D, C→A, C→C] (bifurcación)
- **Aceptada**: queda {D} ∈ F.

## Cadena `101`

- Inicio: {A}
- Lee `1`: {A} ⟶ {B, C} [A→B, A→C] (bifurcación)
- Lee `0`: {B, C} ⟶ {A, B, C, D} [B→A, B→B, B→D, C→A, C→C] (bifurcación)
- Lee `1`: {A, B, C, D} ⟶ {A, B, C, D, E} [A→B, A→C, B→C, B→D, C→A, C→E, D→D, D→E] (bifurcación)
- **Aceptada**: queda {D} ∈ F.

## Cadena `10011`

- Inicio: {A}
- Lee `1`: {A} ⟶ {B, C} [A→B, A→C] (bifurcación)
- Lee `0`: {B, C} ⟶ {A, B, C, D} [B→A, B→B, B→D, C→A, C→C] (bifurcación)
- Lee `0`: {A, B, C, D} ⟶ {A, B, C, D} [B→A, B→B, B→D, C→A, C→C]
- Lee `1`: {A, B, C, D} ⟶ {A, B, C, D, E} [A→B, A→C, B→C, B→D, C→A, C→E, D→D, D→E] (bifurcación)
- Lee `1`: {A, B, C, D, E} ⟶ {A, B, C, D, E} [A→B, A→C, B→C, B→D, C→A, C→E, D→D, D→E]
- **Aceptada**: queda {D} ∈ F.

## Cadena `1001000`

- Inicio: {A}
- Lee `1`: {A} ⟶ {B, C} [A→B, A→C] (bifurcación)
- Lee `0`: {B, C} ⟶ {A, B, C, D} [B→A, B→B, B→D, C→A, C→C] (bifurcación)
- Lee `0`: {A, B, C, D} ⟶ {A, B, C, D} [B→A, B→B, B→D, C→A, C→C]
- Lee `1`: {A, B, C, D} ⟶ {A, B, C, D, E} [A→B, A→C, B→C, B→D, C→A, C→E, D→D, D→E] (bifurcación)
- Lee `0`: {A, B, C, D, E} ⟶ {A, B, C, D, E} [B→A, B→B, B→D, C→A, C→C, E→A, E→E]
- Lee `0`: {A, B, C, D, E} ⟶ {A, B, C, D, E} [B→A, B→B, B→D, C→A, C→C, E→A, E→E]
- Lee `0`: {A, B, C, D, E} ⟶ {A, B, C, D, E} [B→A, B→B, B→D, C→A, C→C, E→A, E→E]
- **Aceptada**: queda {D} ∈ F.

## Cadena `1000111101`

- Inicio: {A}
- Lee `1`: {A} ⟶ {B, C} [A→B, A→C] (bifurcación)
- Lee `0`: {B, C} ⟶ {A, B, C, D} [B→A, B→B, B→D, C→A, C→C] (bifurcación)
- Lee `0`: {A, B, C, D} ⟶ {A, B, C, D} [B→A, B→B, B→D, C→A, C→C]
- Lee `0`: {A, B, C, D} ⟶ {A, B, C, D} [B→A, B→B, B→D, C→A, C→C]
- Lee `1`: {A, B, C, D} ⟶ {A, B, C, D, E} [A→B, A→C, B→C, B→D, C→A, C→E, D→D, D→E] (bifurcación)
- Lee `1`: {A, B, C, D, E} ⟶ {A, B, C, D, E} [A→B, A→C, B→C, B→D, C→A, C→E, D→D, D→E]
- Lee `1`: {A, B, C, D, E} ⟶ {A, B, C, D, E} [A→B, A→C, B→C, B→D, C→A, C→E, D→D, D→E]
- Lee `1`: {A, B, C, D, E} ⟶ {A, B, C, D, E} [A→B, A→C, B→C, B→D, C→A, C→E, D→D, D→E]
- Lee `0`: {A, B, C, D, E} ⟶ {A, B, C, D, E} [B→A, B→B, B→D, C→A, C→C, E→A, E→E]
- Lee `1`: {A, B, C, D, E} ⟶ {A, B, C, D, E} [A→B, A→C, B→C, B→D, C→A, C→E, D→D, D→E]
- **Aceptada**: queda {D} ∈ F.

## Cadena λ

- Inicio: {A}
- **Rechazada**: ningún estado de {A} es de aceptación.

## Cadena `1`

- Inicio: {A}
- Lee `1`: {A} ⟶ {B, C} [A→B, A→C] (bifurcación)
- **Rechazada**: ningún estado de {B, C} es de aceptación.

## Cadena `011`

- Inicio: {A}
- Lee `0`: {A} ⟶ ∅ [ninguna transición]
- Lee `1`: ∅ ⟶ ∅ [ninguna transición]
- Lee `1`: ∅ ⟶ ∅ [ninguna transición]
- **Rechazada**: no queda ningún estado activo.

## Cadena `00101`

- Inicio: {A}
- Lee `0`: {A} ⟶ ∅ [ninguna transición]
- Lee `0`: ∅ ⟶ ∅ [ninguna transición]
- Lee `1`: ∅ ⟶ ∅ [ninguna transición]
- Lee `0`: ∅ ⟶ ∅ [ninguna transición]
- Lee `1`: ∅ ⟶ ∅ [ninguna transición]
- **Rechazada**: no queda ningún estado activo.

## Cadena `00111110`

- Inicio: {A}
- Lee `0`: {A} ⟶ ∅ [ninguna transición]
- Lee `0`: ∅ ⟶ ∅ [ninguna transición]
- Lee `1`: ∅ ⟶ ∅ [ninguna transición]
- Lee `1`: ∅ ⟶ ∅ [ninguna transición]
- Lee `1`: ∅ ⟶ ∅ [ninguna transición]
- Lee `1`: ∅ ⟶ ∅ [ninguna transición]
- Lee `1`: ∅ ⟶ ∅ [ninguna transición]
- Lee `0`: ∅ ⟶ ∅ [ninguna transición]
- **Rechazada**: no queda ningún estado activo.
