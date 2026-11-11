# Recorridos: Lista 3 · Ejercicio 157

Diagrama y simplificación del AFD de la tabla 157 (tabla transcrita del diagrama).

Autómata: `lista3-157` (AFD).

## Cadena `1`

- Inicio: {A}
- Lee `1`: {A} ⟶ {F} [A→F]
- **Aceptada**: queda {F} ∈ F.

## Cadena `10`

- Inicio: {A}
- Lee `1`: {A} ⟶ {F} [A→F]
- Lee `0`: {F} ⟶ {F} [F→F]
- **Aceptada**: queda {F} ∈ F.

## Cadena `0100`

- Inicio: {A}
- Lee `0`: {A} ⟶ {B} [A→B]
- Lee `1`: {B} ⟶ {E} [B→E]
- Lee `0`: {E} ⟶ {F} [E→F]
- Lee `0`: {F} ⟶ {F} [F→F]
- **Aceptada**: queda {F} ∈ F.

## Cadena `100000`

- Inicio: {A}
- Lee `1`: {A} ⟶ {F} [A→F]
- Lee `0`: {F} ⟶ {F} [F→F]
- Lee `0`: {F} ⟶ {F} [F→F]
- Lee `0`: {F} ⟶ {F} [F→F]
- Lee `0`: {F} ⟶ {F} [F→F]
- Lee `0`: {F} ⟶ {F} [F→F]
- **Aceptada**: queda {F} ∈ F.

## Cadena `111001010`

- Inicio: {A}
- Lee `1`: {A} ⟶ {F} [A→F]
- Lee `1`: {F} ⟶ {B} [F→B]
- Lee `1`: {B} ⟶ {E} [B→E]
- Lee `0`: {E} ⟶ {F} [E→F]
- Lee `0`: {F} ⟶ {F} [F→F]
- Lee `1`: {F} ⟶ {B} [F→B]
- Lee `0`: {B} ⟶ {C} [B→C]
- Lee `1`: {C} ⟶ {E} [C→E]
- Lee `0`: {E} ⟶ {F} [E→F]
- **Aceptada**: queda {F} ∈ F.

## Cadena λ

- Inicio: {A}
- **Rechazada**: ningún estado de {A} es de aceptación.

## Cadena `0`

- Inicio: {A}
- Lee `0`: {A} ⟶ {B} [A→B]
- **Rechazada**: ningún estado de {B} es de aceptación.

## Cadena `001`

- Inicio: {A}
- Lee `0`: {A} ⟶ {B} [A→B]
- Lee `0`: {B} ⟶ {C} [B→C]
- Lee `1`: {C} ⟶ {E} [C→E]
- **Rechazada**: ningún estado de {E} es de aceptación.

## Cadena `00111`

- Inicio: {A}
- Lee `0`: {A} ⟶ {B} [A→B]
- Lee `0`: {B} ⟶ {C} [B→C]
- Lee `1`: {C} ⟶ {E} [C→E]
- Lee `1`: {E} ⟶ {D} [E→D]
- Lee `1`: {D} ⟶ {E} [D→E]
- **Rechazada**: ningún estado de {E} es de aceptación.

## Cadena `01010110`

- Inicio: {A}
- Lee `0`: {A} ⟶ {B} [A→B]
- Lee `1`: {B} ⟶ {E} [B→E]
- Lee `0`: {E} ⟶ {F} [E→F]
- Lee `1`: {F} ⟶ {B} [F→B]
- Lee `0`: {B} ⟶ {C} [B→C]
- Lee `1`: {C} ⟶ {E} [C→E]
- Lee `1`: {E} ⟶ {D} [E→D]
- Lee `0`: {D} ⟶ {B} [D→B]
- **Rechazada**: ningún estado de {B} es de aceptación.
