# Recorridos: Lista 3 · Ejercicio 199

AFN-λ de la tabla 199: diagrama, AFD equivalente e incisos.

Autómata: `lista3-199` (AFN-λ).

## Cadena λ

- Inicio: {A}; con cierre λ, {A, B, C, E}
- **Aceptada**: queda {E} ∈ F.

## Cadena `1`

- Inicio: {A}; con cierre λ, {A, B, C, E}
- Lee `1`: {A, B, C, E} ⟶ {A, B, C, D, E} [B→B, C→A, C→C, E→D]; cierre λ añade {E}
- **Aceptada**: queda {D, E} ∈ F.

## Cadena `011`

- Inicio: {A}; con cierre λ, {A, B, C, E}
- Lee `0`: {A, B, C, E} ⟶ {E} [A→E, B→E]
- Lee `1`: {E} ⟶ {D} [E→D]
- Lee `1`: {D} ⟶ {D} [D→D]
- **Aceptada**: queda {D} ∈ F.

## Cadena `11111`

- Inicio: {A}; con cierre λ, {A, B, C, E}
- Lee `1`: {A, B, C, E} ⟶ {A, B, C, D, E} [B→B, C→A, C→C, E→D]; cierre λ añade {E}
- Lee `1`: {A, B, C, D, E} ⟶ {A, B, C, D, E} [B→B, C→A, C→C, D→D, E→D]; cierre λ añade {E}
- Lee `1`: {A, B, C, D, E} ⟶ {A, B, C, D, E} [B→B, C→A, C→C, D→D, E→D]; cierre λ añade {E}
- Lee `1`: {A, B, C, D, E} ⟶ {A, B, C, D, E} [B→B, C→A, C→C, D→D, E→D]; cierre λ añade {E}
- Lee `1`: {A, B, C, D, E} ⟶ {A, B, C, D, E} [B→B, C→A, C→C, D→D, E→D]; cierre λ añade {E}
- **Aceptada**: queda {D, E} ∈ F.

## Cadena `11101111`

- Inicio: {A}; con cierre λ, {A, B, C, E}
- Lee `1`: {A, B, C, E} ⟶ {A, B, C, D, E} [B→B, C→A, C→C, E→D]; cierre λ añade {E}
- Lee `1`: {A, B, C, D, E} ⟶ {A, B, C, D, E} [B→B, C→A, C→C, D→D, E→D]; cierre λ añade {E}
- Lee `1`: {A, B, C, D, E} ⟶ {A, B, C, D, E} [B→B, C→A, C→C, D→D, E→D]; cierre λ añade {E}
- Lee `0`: {A, B, C, D, E} ⟶ {E} [A→E, B→E]
- Lee `1`: {E} ⟶ {D} [E→D]
- Lee `1`: {D} ⟶ {D} [D→D]
- Lee `1`: {D} ⟶ {D} [D→D]
- Lee `1`: {D} ⟶ {D} [D→D]
- **Aceptada**: queda {D} ∈ F.

## Cadena `00`

- Inicio: {A}; con cierre λ, {A, B, C, E}
- Lee `0`: {A, B, C, E} ⟶ {E} [A→E, B→E]
- Lee `0`: {E} ⟶ ∅ [ninguna transición]
- **Rechazada**: no queda ningún estado activo.

## Cadena `001`

- Inicio: {A}; con cierre λ, {A, B, C, E}
- Lee `0`: {A, B, C, E} ⟶ {E} [A→E, B→E]
- Lee `0`: {E} ⟶ ∅ [ninguna transición]
- Lee `1`: ∅ ⟶ ∅ [ninguna transición]
- **Rechazada**: no queda ningún estado activo.

## Cadena `10110`

- Inicio: {A}; con cierre λ, {A, B, C, E}
- Lee `1`: {A, B, C, E} ⟶ {A, B, C, D, E} [B→B, C→A, C→C, E→D]; cierre λ añade {E}
- Lee `0`: {A, B, C, D, E} ⟶ {E} [A→E, B→E]
- Lee `1`: {E} ⟶ {D} [E→D]
- Lee `1`: {D} ⟶ {D} [D→D]
- Lee `0`: {D} ⟶ ∅ [ninguna transición]
- **Rechazada**: no queda ningún estado activo.

## Cadena `0101100`

- Inicio: {A}; con cierre λ, {A, B, C, E}
- Lee `0`: {A, B, C, E} ⟶ {E} [A→E, B→E]
- Lee `1`: {E} ⟶ {D} [E→D]
- Lee `0`: {D} ⟶ ∅ [ninguna transición]
- Lee `1`: ∅ ⟶ ∅ [ninguna transición]
- Lee `1`: ∅ ⟶ ∅ [ninguna transición]
- Lee `0`: ∅ ⟶ ∅ [ninguna transición]
- Lee `0`: ∅ ⟶ ∅ [ninguna transición]
- **Rechazada**: no queda ningún estado activo.

## Cadena `1111001100`

- Inicio: {A}; con cierre λ, {A, B, C, E}
- Lee `1`: {A, B, C, E} ⟶ {A, B, C, D, E} [B→B, C→A, C→C, E→D]; cierre λ añade {E}
- Lee `1`: {A, B, C, D, E} ⟶ {A, B, C, D, E} [B→B, C→A, C→C, D→D, E→D]; cierre λ añade {E}
- Lee `1`: {A, B, C, D, E} ⟶ {A, B, C, D, E} [B→B, C→A, C→C, D→D, E→D]; cierre λ añade {E}
- Lee `1`: {A, B, C, D, E} ⟶ {A, B, C, D, E} [B→B, C→A, C→C, D→D, E→D]; cierre λ añade {E}
- Lee `0`: {A, B, C, D, E} ⟶ {E} [A→E, B→E]
- Lee `0`: {E} ⟶ ∅ [ninguna transición]
- Lee `1`: ∅ ⟶ ∅ [ninguna transición]
- Lee `1`: ∅ ⟶ ∅ [ninguna transición]
- Lee `0`: ∅ ⟶ ∅ [ninguna transición]
- Lee `0`: ∅ ⟶ ∅ [ninguna transición]
- **Rechazada**: no queda ningún estado activo.
