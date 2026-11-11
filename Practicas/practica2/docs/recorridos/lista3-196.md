# Recorridos: Lista 3 · Ejercicio 196

AFN-λ de la tabla 196: diagrama, AFD equivalente e incisos.

Autómata: `lista3-196` (AFN-λ).

## Cadena `1`

- Inicio: {A}; con cierre λ, {A, B}
- Lee `1`: {A, B} ⟶ {C} [B→C]
- **Aceptada**: queda {C} ∈ F.

## Cadena `01`

- Inicio: {A}; con cierre λ, {A, B}
- Lee `0`: {A, B} ⟶ {A, B} [A→A, B→A, B→B]
- Lee `1`: {A, B} ⟶ {C} [B→C]
- **Aceptada**: queda {C} ∈ F.

## Cadena `0001`

- Inicio: {A}; con cierre λ, {A, B}
- Lee `0`: {A, B} ⟶ {A, B} [A→A, B→A, B→B]
- Lee `0`: {A, B} ⟶ {A, B} [A→A, B→A, B→B]
- Lee `0`: {A, B} ⟶ {A, B} [A→A, B→A, B→B]
- Lee `1`: {A, B} ⟶ {C} [B→C]
- **Aceptada**: queda {C} ∈ F.

## Cadena `000001`

- Inicio: {A}; con cierre λ, {A, B}
- Lee `0`: {A, B} ⟶ {A, B} [A→A, B→A, B→B]
- Lee `0`: {A, B} ⟶ {A, B} [A→A, B→A, B→B]
- Lee `0`: {A, B} ⟶ {A, B} [A→A, B→A, B→B]
- Lee `0`: {A, B} ⟶ {A, B} [A→A, B→A, B→B]
- Lee `0`: {A, B} ⟶ {A, B} [A→A, B→A, B→B]
- Lee `1`: {A, B} ⟶ {C} [B→C]
- **Aceptada**: queda {C} ∈ F.

## Cadena `000000001`

- Inicio: {A}; con cierre λ, {A, B}
- Lee `0`: {A, B} ⟶ {A, B} [A→A, B→A, B→B]
- Lee `0`: {A, B} ⟶ {A, B} [A→A, B→A, B→B]
- Lee `0`: {A, B} ⟶ {A, B} [A→A, B→A, B→B]
- Lee `0`: {A, B} ⟶ {A, B} [A→A, B→A, B→B]
- Lee `0`: {A, B} ⟶ {A, B} [A→A, B→A, B→B]
- Lee `0`: {A, B} ⟶ {A, B} [A→A, B→A, B→B]
- Lee `0`: {A, B} ⟶ {A, B} [A→A, B→A, B→B]
- Lee `0`: {A, B} ⟶ {A, B} [A→A, B→A, B→B]
- Lee `1`: {A, B} ⟶ {C} [B→C]
- **Aceptada**: queda {C} ∈ F.

## Cadena λ

- Inicio: {A}; con cierre λ, {A, B}
- **Rechazada**: ningún estado de {A, B} es de aceptación.

## Cadena `0`

- Inicio: {A}; con cierre λ, {A, B}
- Lee `0`: {A, B} ⟶ {A, B} [A→A, B→A, B→B]
- **Rechazada**: ningún estado de {A, B} es de aceptación.

## Cadena `010`

- Inicio: {A}; con cierre λ, {A, B}
- Lee `0`: {A, B} ⟶ {A, B} [A→A, B→A, B→B]
- Lee `1`: {A, B} ⟶ {C} [B→C]
- Lee `0`: {C} ⟶ ∅ [ninguna transición]
- **Rechazada**: no queda ningún estado activo.

## Cadena `11001`

- Inicio: {A}; con cierre λ, {A, B}
- Lee `1`: {A, B} ⟶ {C} [B→C]
- Lee `1`: {C} ⟶ ∅ [ninguna transición]
- Lee `0`: ∅ ⟶ ∅ [ninguna transición]
- Lee `0`: ∅ ⟶ ∅ [ninguna transición]
- Lee `1`: ∅ ⟶ ∅ [ninguna transición]
- **Rechazada**: no queda ningún estado activo.

## Cadena `11101110`

- Inicio: {A}; con cierre λ, {A, B}
- Lee `1`: {A, B} ⟶ {C} [B→C]
- Lee `1`: {C} ⟶ ∅ [ninguna transición]
- Lee `1`: ∅ ⟶ ∅ [ninguna transición]
- Lee `0`: ∅ ⟶ ∅ [ninguna transición]
- Lee `1`: ∅ ⟶ ∅ [ninguna transición]
- Lee `1`: ∅ ⟶ ∅ [ninguna transición]
- Lee `1`: ∅ ⟶ ∅ [ninguna transición]
- Lee `0`: ∅ ⟶ ∅ [ninguna transición]
- **Rechazada**: no queda ningún estado activo.
