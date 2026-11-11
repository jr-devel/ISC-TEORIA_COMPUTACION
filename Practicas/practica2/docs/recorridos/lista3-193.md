# Recorridos: Lista 3 · Ejercicio 193

AFN de la tabla 193: AFD equivalente y δ̂(Z, ω).

Autómata: `lista3-193` (AFN).

## Cadena `11`

- Inicio: {A}
- Lee `1`: {A} ⟶ {B, C} [A→B, A→C] (bifurcación)
- Lee `1`: {B, C} ⟶ {A, B, C, D} [B→B, B→C, B→D, C→A, C→C] (bifurcación)
- **Aceptada**: queda {D} ∈ F.

## Cadena `110`

- Inicio: {A}
- Lee `1`: {A} ⟶ {B, C} [A→B, A→C] (bifurcación)
- Lee `1`: {B, C} ⟶ {A, B, C, D} [B→B, B→C, B→D, C→A, C→C] (bifurcación)
- Lee `0`: {A, B, C, D} ⟶ {A, C, D} [B→A, B→D, C→C, D→C]
- **Aceptada**: queda {D} ∈ F.

## Cadena `10101`

- Inicio: {A}
- Lee `1`: {A} ⟶ {B, C} [A→B, A→C] (bifurcación)
- Lee `0`: {B, C} ⟶ {A, C, D} [B→A, B→D, C→C] (bifurcación)
- Lee `1`: {A, C, D} ⟶ {A, B, C, D} [A→B, A→C, C→A, C→C, D→D] (bifurcación)
- Lee `0`: {A, B, C, D} ⟶ {A, C, D} [B→A, B→D, C→C, D→C]
- Lee `1`: {A, C, D} ⟶ {A, B, C, D} [A→B, A→C, C→A, C→C, D→D] (bifurcación)
- **Aceptada**: queda {D} ∈ F.

## Cadena `1111101`

- Inicio: {A}
- Lee `1`: {A} ⟶ {B, C} [A→B, A→C] (bifurcación)
- Lee `1`: {B, C} ⟶ {A, B, C, D} [B→B, B→C, B→D, C→A, C→C] (bifurcación)
- Lee `1`: {A, B, C, D} ⟶ {A, B, C, D} [A→B, A→C, B→B, B→C, B→D, C→A, C→C, D→D]
- Lee `1`: {A, B, C, D} ⟶ {A, B, C, D} [A→B, A→C, B→B, B→C, B→D, C→A, C→C, D→D]
- Lee `1`: {A, B, C, D} ⟶ {A, B, C, D} [A→B, A→C, B→B, B→C, B→D, C→A, C→C, D→D]
- Lee `0`: {A, B, C, D} ⟶ {A, C, D} [B→A, B→D, C→C, D→C]
- Lee `1`: {A, C, D} ⟶ {A, B, C, D} [A→B, A→C, C→A, C→C, D→D] (bifurcación)
- **Aceptada**: queda {D} ∈ F.

## Cadena `1100001111`

- Inicio: {A}
- Lee `1`: {A} ⟶ {B, C} [A→B, A→C] (bifurcación)
- Lee `1`: {B, C} ⟶ {A, B, C, D} [B→B, B→C, B→D, C→A, C→C] (bifurcación)
- Lee `0`: {A, B, C, D} ⟶ {A, C, D} [B→A, B→D, C→C, D→C]
- Lee `0`: {A, C, D} ⟶ {C} [C→C, D→C]
- Lee `0`: {C} ⟶ {C} [C→C]
- Lee `0`: {C} ⟶ {C} [C→C]
- Lee `1`: {C} ⟶ {A, C} [C→A, C→C] (bifurcación)
- Lee `1`: {A, C} ⟶ {A, B, C} [A→B, A→C, C→A, C→C] (bifurcación)
- Lee `1`: {A, B, C} ⟶ {A, B, C, D} [A→B, A→C, B→B, B→C, B→D, C→A, C→C] (bifurcación)
- Lee `1`: {A, B, C, D} ⟶ {A, B, C, D} [A→B, A→C, B→B, B→C, B→D, C→A, C→C, D→D]
- **Aceptada**: queda {D} ∈ F.

## Cadena λ

- Inicio: {A}
- **Rechazada**: ningún estado de {A} es de aceptación.

## Cadena `1`

- Inicio: {A}
- Lee `1`: {A} ⟶ {B, C} [A→B, A→C] (bifurcación)
- **Rechazada**: ningún estado de {B, C} es de aceptación.

## Cadena `000`

- Inicio: {A}
- Lee `0`: {A} ⟶ ∅ [ninguna transición]
- Lee `0`: ∅ ⟶ ∅ [ninguna transición]
- Lee `0`: ∅ ⟶ ∅ [ninguna transición]
- **Rechazada**: no queda ningún estado activo.

## Cadena `00011`

- Inicio: {A}
- Lee `0`: {A} ⟶ ∅ [ninguna transición]
- Lee `0`: ∅ ⟶ ∅ [ninguna transición]
- Lee `0`: ∅ ⟶ ∅ [ninguna transición]
- Lee `1`: ∅ ⟶ ∅ [ninguna transición]
- Lee `1`: ∅ ⟶ ∅ [ninguna transición]
- **Rechazada**: no queda ningún estado activo.

## Cadena `01110101`

- Inicio: {A}
- Lee `0`: {A} ⟶ ∅ [ninguna transición]
- Lee `1`: ∅ ⟶ ∅ [ninguna transición]
- Lee `1`: ∅ ⟶ ∅ [ninguna transición]
- Lee `1`: ∅ ⟶ ∅ [ninguna transición]
- Lee `0`: ∅ ⟶ ∅ [ninguna transición]
- Lee `1`: ∅ ⟶ ∅ [ninguna transición]
- Lee `0`: ∅ ⟶ ∅ [ninguna transición]
- Lee `1`: ∅ ⟶ ∅ [ninguna transición]
- **Rechazada**: no queda ningún estado activo.

## Cadena `10`

- Inicio: {A}
- Lee `1`: {A} ⟶ {B, C} [A→B, A→C] (bifurcación)
- Lee `0`: {B, C} ⟶ {A, C, D} [B→A, B→D, C→C] (bifurcación)
- **Aceptada**: queda {D} ∈ F.

## Cadena `0`

- Inicio: {A}
- Lee `0`: {A} ⟶ ∅ [ninguna transición]
- **Rechazada**: no queda ningún estado activo.
