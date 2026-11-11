# Recorridos: Lista 3 · Ejercicio 192

AFN de la tabla 192: AFD equivalente y δ̂(Z, ω).

Autómata: `lista3-192` (AFN).

## Cadena `1`

- Inicio: {A}
- Lee `1`: {A} ⟶ {B, C} [A→B, A→C] (bifurcación)
- **Aceptada**: queda {C} ∈ F.

## Cadena `10`

- Inicio: {A}
- Lee `1`: {A} ⟶ {B, C} [A→B, A→C] (bifurcación)
- Lee `0`: {B, C} ⟶ {A, B, C} [B→A, B→B, C→A, C→C] (bifurcación)
- **Aceptada**: queda {C} ∈ F.

## Cadena `1010`

- Inicio: {A}
- Lee `1`: {A} ⟶ {B, C} [A→B, A→C] (bifurcación)
- Lee `0`: {B, C} ⟶ {A, B, C} [B→A, B→B, C→A, C→C] (bifurcación)
- Lee `1`: {A, B, C} ⟶ {B, C} [A→B, A→C]
- Lee `0`: {B, C} ⟶ {A, B, C} [B→A, B→B, C→A, C→C] (bifurcación)
- **Aceptada**: queda {C} ∈ F.

## Cadena `000001`

- Inicio: {A}
- Lee `0`: {A} ⟶ {B} [A→B]
- Lee `0`: {B} ⟶ {A, B} [B→A, B→B] (bifurcación)
- Lee `0`: {A, B} ⟶ {A, B} [A→B, B→A, B→B]
- Lee `0`: {A, B} ⟶ {A, B} [A→B, B→A, B→B]
- Lee `0`: {A, B} ⟶ {A, B} [A→B, B→A, B→B]
- Lee `1`: {A, B} ⟶ {B, C} [A→B, A→C]
- **Aceptada**: queda {C} ∈ F.

## Cadena `001000000`

- Inicio: {A}
- Lee `0`: {A} ⟶ {B} [A→B]
- Lee `0`: {B} ⟶ {A, B} [B→A, B→B] (bifurcación)
- Lee `1`: {A, B} ⟶ {B, C} [A→B, A→C]
- Lee `0`: {B, C} ⟶ {A, B, C} [B→A, B→B, C→A, C→C] (bifurcación)
- Lee `0`: {A, B, C} ⟶ {A, B, C} [A→B, B→A, B→B, C→A, C→C]
- Lee `0`: {A, B, C} ⟶ {A, B, C} [A→B, B→A, B→B, C→A, C→C]
- Lee `0`: {A, B, C} ⟶ {A, B, C} [A→B, B→A, B→B, C→A, C→C]
- Lee `0`: {A, B, C} ⟶ {A, B, C} [A→B, B→A, B→B, C→A, C→C]
- Lee `0`: {A, B, C} ⟶ {A, B, C} [A→B, B→A, B→B, C→A, C→C]
- **Aceptada**: queda {C} ∈ F.

## Cadena λ

- Inicio: {A}
- **Rechazada**: ningún estado de {A} es de aceptación.

## Cadena `0`

- Inicio: {A}
- Lee `0`: {A} ⟶ {B} [A→B]
- **Rechazada**: ningún estado de {B} es de aceptación.

## Cadena `111`

- Inicio: {A}
- Lee `1`: {A} ⟶ {B, C} [A→B, A→C] (bifurcación)
- Lee `1`: {B, C} ⟶ ∅ [ninguna transición]
- Lee `1`: ∅ ⟶ ∅ [ninguna transición]
- **Rechazada**: no queda ningún estado activo.

## Cadena `00110`

- Inicio: {A}
- Lee `0`: {A} ⟶ {B} [A→B]
- Lee `0`: {B} ⟶ {A, B} [B→A, B→B] (bifurcación)
- Lee `1`: {A, B} ⟶ {B, C} [A→B, A→C]
- Lee `1`: {B, C} ⟶ ∅ [ninguna transición]
- Lee `0`: ∅ ⟶ ∅ [ninguna transición]
- **Rechazada**: no queda ningún estado activo.

## Cadena `11000101`

- Inicio: {A}
- Lee `1`: {A} ⟶ {B, C} [A→B, A→C] (bifurcación)
- Lee `1`: {B, C} ⟶ ∅ [ninguna transición]
- Lee `0`: ∅ ⟶ ∅ [ninguna transición]
- Lee `0`: ∅ ⟶ ∅ [ninguna transición]
- Lee `0`: ∅ ⟶ ∅ [ninguna transición]
- Lee `1`: ∅ ⟶ ∅ [ninguna transición]
- Lee `0`: ∅ ⟶ ∅ [ninguna transición]
- Lee `1`: ∅ ⟶ ∅ [ninguna transición]
- **Rechazada**: no queda ningún estado activo.
