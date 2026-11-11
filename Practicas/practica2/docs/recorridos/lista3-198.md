# Recorridos: Lista 3 · Ejercicio 198

AFN-λ de la tabla 198: diagrama, AFD equivalente e incisos.

Autómata: `lista3-198` (AFN-λ).

## Cadena `1`

- Inicio: {A}; con cierre λ, {A, B, C}
- Lee `1`: {A, B, C} ⟶ {B, C, D} [C→C, C→D]; cierre λ añade {B}
- **Aceptada**: queda {D} ∈ F.

## Cadena `01`

- Inicio: {A}; con cierre λ, {A, B, C}
- Lee `0`: {A, B, C} ⟶ {B, C} [A→B, B→C]
- Lee `1`: {B, C} ⟶ {B, C, D} [C→C, C→D]; cierre λ añade {B}
- **Aceptada**: queda {D} ∈ F.

## Cadena `0011`

- Inicio: {A}; con cierre λ, {A, B, C}
- Lee `0`: {A, B, C} ⟶ {B, C} [A→B, B→C]
- Lee `0`: {B, C} ⟶ {B, C} [B→C]; cierre λ añade {B}
- Lee `1`: {B, C} ⟶ {B, C, D} [C→C, C→D]; cierre λ añade {B}
- Lee `1`: {B, C, D} ⟶ {B, C, D} [C→C, C→D, D→B]
- **Aceptada**: queda {D} ∈ F.

## Cadena `001101`

- Inicio: {A}; con cierre λ, {A, B, C}
- Lee `0`: {A, B, C} ⟶ {B, C} [A→B, B→C]
- Lee `0`: {B, C} ⟶ {B, C} [B→C]; cierre λ añade {B}
- Lee `1`: {B, C} ⟶ {B, C, D} [C→C, C→D]; cierre λ añade {B}
- Lee `1`: {B, C, D} ⟶ {B, C, D} [C→C, C→D, D→B]
- Lee `0`: {B, C, D} ⟶ {B, C} [B→C]; cierre λ añade {B}
- Lee `1`: {B, C} ⟶ {B, C, D} [C→C, C→D]; cierre λ añade {B}
- **Aceptada**: queda {D} ∈ F.

## Cadena `000111111`

- Inicio: {A}; con cierre λ, {A, B, C}
- Lee `0`: {A, B, C} ⟶ {B, C} [A→B, B→C]
- Lee `0`: {B, C} ⟶ {B, C} [B→C]; cierre λ añade {B}
- Lee `0`: {B, C} ⟶ {B, C} [B→C]; cierre λ añade {B}
- Lee `1`: {B, C} ⟶ {B, C, D} [C→C, C→D]; cierre λ añade {B}
- Lee `1`: {B, C, D} ⟶ {B, C, D} [C→C, C→D, D→B]
- Lee `1`: {B, C, D} ⟶ {B, C, D} [C→C, C→D, D→B]
- Lee `1`: {B, C, D} ⟶ {B, C, D} [C→C, C→D, D→B]
- Lee `1`: {B, C, D} ⟶ {B, C, D} [C→C, C→D, D→B]
- Lee `1`: {B, C, D} ⟶ {B, C, D} [C→C, C→D, D→B]
- **Aceptada**: queda {D} ∈ F.

## Cadena λ

- Inicio: {A}; con cierre λ, {A, B, C}
- **Rechazada**: ningún estado de {A, B, C} es de aceptación.

## Cadena `0`

- Inicio: {A}; con cierre λ, {A, B, C}
- Lee `0`: {A, B, C} ⟶ {B, C} [A→B, B→C]
- **Rechazada**: ningún estado de {B, C} es de aceptación.

## Cadena `000`

- Inicio: {A}; con cierre λ, {A, B, C}
- Lee `0`: {A, B, C} ⟶ {B, C} [A→B, B→C]
- Lee `0`: {B, C} ⟶ {B, C} [B→C]; cierre λ añade {B}
- Lee `0`: {B, C} ⟶ {B, C} [B→C]; cierre λ añade {B}
- **Rechazada**: ningún estado de {B, C} es de aceptación.

## Cadena `00100`

- Inicio: {A}; con cierre λ, {A, B, C}
- Lee `0`: {A, B, C} ⟶ {B, C} [A→B, B→C]
- Lee `0`: {B, C} ⟶ {B, C} [B→C]; cierre λ añade {B}
- Lee `1`: {B, C} ⟶ {B, C, D} [C→C, C→D]; cierre λ añade {B}
- Lee `0`: {B, C, D} ⟶ {B, C} [B→C]; cierre λ añade {B}
- Lee `0`: {B, C} ⟶ {B, C} [B→C]; cierre λ añade {B}
- **Rechazada**: ningún estado de {B, C} es de aceptación.

## Cadena `10110010`

- Inicio: {A}; con cierre λ, {A, B, C}
- Lee `1`: {A, B, C} ⟶ {B, C, D} [C→C, C→D]; cierre λ añade {B}
- Lee `0`: {B, C, D} ⟶ {B, C} [B→C]; cierre λ añade {B}
- Lee `1`: {B, C} ⟶ {B, C, D} [C→C, C→D]; cierre λ añade {B}
- Lee `1`: {B, C, D} ⟶ {B, C, D} [C→C, C→D, D→B]
- Lee `0`: {B, C, D} ⟶ {B, C} [B→C]; cierre λ añade {B}
- Lee `0`: {B, C} ⟶ {B, C} [B→C]; cierre λ añade {B}
- Lee `1`: {B, C} ⟶ {B, C, D} [C→C, C→D]; cierre λ añade {B}
- Lee `0`: {B, C, D} ⟶ {B, C} [B→C]; cierre λ añade {B}
- **Rechazada**: ningún estado de {B, C} es de aceptación.
