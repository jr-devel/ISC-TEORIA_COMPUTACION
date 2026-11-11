# Recorridos: Lista 3 · Ejercicio 197

AFN-λ de la tabla 197: diagrama, AFD equivalente e incisos.

Autómata: `lista3-197` (AFN-λ).

## Cadena λ

- Inicio: {A}; con cierre λ, {A, B, C, D}
- **Aceptada**: queda {D} ∈ F.

## Cadena `0`

- Inicio: {A}; con cierre λ, {A, B, C, D}
- Lee `0`: {A, B, C, D} ⟶ {A, B, C, D} [A→B, A→D, B→A, B→C]
- **Aceptada**: queda {D} ∈ F.

## Cadena `000`

- Inicio: {A}; con cierre λ, {A, B, C, D}
- Lee `0`: {A, B, C, D} ⟶ {A, B, C, D} [A→B, A→D, B→A, B→C]
- Lee `0`: {A, B, C, D} ⟶ {A, B, C, D} [A→B, A→D, B→A, B→C]
- Lee `0`: {A, B, C, D} ⟶ {A, B, C, D} [A→B, A→D, B→A, B→C]
- **Aceptada**: queda {D} ∈ F.

## Cadena `11110`

- Inicio: {A}; con cierre λ, {A, B, C, D}
- Lee `1`: {A, B, C, D} ⟶ {A, B, C, D} [B→D, C→A, C→C, D→D]; cierre λ añade {B}
- Lee `1`: {A, B, C, D} ⟶ {A, B, C, D} [B→D, C→A, C→C, D→D]; cierre λ añade {B}
- Lee `1`: {A, B, C, D} ⟶ {A, B, C, D} [B→D, C→A, C→C, D→D]; cierre λ añade {B}
- Lee `1`: {A, B, C, D} ⟶ {A, B, C, D} [B→D, C→A, C→C, D→D]; cierre λ añade {B}
- Lee `0`: {A, B, C, D} ⟶ {A, B, C, D} [A→B, A→D, B→A, B→C]
- **Aceptada**: queda {D} ∈ F.

## Cadena `11110111`

- Inicio: {A}; con cierre λ, {A, B, C, D}
- Lee `1`: {A, B, C, D} ⟶ {A, B, C, D} [B→D, C→A, C→C, D→D]; cierre λ añade {B}
- Lee `1`: {A, B, C, D} ⟶ {A, B, C, D} [B→D, C→A, C→C, D→D]; cierre λ añade {B}
- Lee `1`: {A, B, C, D} ⟶ {A, B, C, D} [B→D, C→A, C→C, D→D]; cierre λ añade {B}
- Lee `1`: {A, B, C, D} ⟶ {A, B, C, D} [B→D, C→A, C→C, D→D]; cierre λ añade {B}
- Lee `0`: {A, B, C, D} ⟶ {A, B, C, D} [A→B, A→D, B→A, B→C]
- Lee `1`: {A, B, C, D} ⟶ {A, B, C, D} [B→D, C→A, C→C, D→D]; cierre λ añade {B}
- Lee `1`: {A, B, C, D} ⟶ {A, B, C, D} [B→D, C→A, C→C, D→D]; cierre λ añade {B}
- Lee `1`: {A, B, C, D} ⟶ {A, B, C, D} [B→D, C→A, C→C, D→D]; cierre λ añade {B}
- **Aceptada**: queda {D} ∈ F.
