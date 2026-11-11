# Recorridos: Lista 2 · Ejercicio 103

Las palabras de Σ3 que contienen la cadena aabbba.

Autómata: `lista2-103` (AFD).

## Cadena `aabbba`

- Inicio: {λ}
- Lee `a`: {λ} ⟶ {a} [λ→a]
- Lee `a`: {a} ⟶ {aa} [a→aa]
- Lee `b`: {aa} ⟶ {aab} [aa→aab]
- Lee `b`: {aab} ⟶ {aabb} [aab→aabb]
- Lee `b`: {aabb} ⟶ {aabbb} [aabb→aabbb]
- Lee `a`: {aabbb} ⟶ {aabbba} [aabbb→aabbba]
- **Aceptada**: queda {aabbba} ∈ F.

## Cadena `aabbbab`

- Inicio: {λ}
- Lee `a`: {λ} ⟶ {a} [λ→a]
- Lee `a`: {a} ⟶ {aa} [a→aa]
- Lee `b`: {aa} ⟶ {aab} [aa→aab]
- Lee `b`: {aab} ⟶ {aabb} [aab→aabb]
- Lee `b`: {aabb} ⟶ {aabbb} [aabb→aabbb]
- Lee `a`: {aabbb} ⟶ {aabbba} [aabbb→aabbba]
- Lee `b`: {aabbba} ⟶ {aabbba} [aabbba→aabbba]
- **Aceptada**: queda {aabbba} ∈ F.

## Cadena `aaaabbbab`

- Inicio: {λ}
- Lee `a`: {λ} ⟶ {a} [λ→a]
- Lee `a`: {a} ⟶ {aa} [a→aa]
- Lee `a`: {aa} ⟶ {aa} [aa→aa]
- Lee `a`: {aa} ⟶ {aa} [aa→aa]
- Lee `b`: {aa} ⟶ {aab} [aa→aab]
- Lee `b`: {aab} ⟶ {aabb} [aab→aabb]
- Lee `b`: {aabb} ⟶ {aabbb} [aabb→aabbb]
- Lee `a`: {aabbb} ⟶ {aabbba} [aabbb→aabbba]
- Lee `b`: {aabbba} ⟶ {aabbba} [aabbba→aabbba]
- **Aceptada**: queda {aabbba} ∈ F.

## Cadena `ababbaabbba`

- Inicio: {λ}
- Lee `a`: {λ} ⟶ {a} [λ→a]
- Lee `b`: {a} ⟶ {λ} [a→λ]
- Lee `a`: {λ} ⟶ {a} [λ→a]
- Lee `b`: {a} ⟶ {λ} [a→λ]
- Lee `b`: {λ} ⟶ {λ} [λ→λ]
- Lee `a`: {λ} ⟶ {a} [λ→a]
- Lee `a`: {a} ⟶ {aa} [a→aa]
- Lee `b`: {aa} ⟶ {aab} [aa→aab]
- Lee `b`: {aab} ⟶ {aabb} [aab→aabb]
- Lee `b`: {aabb} ⟶ {aabbb} [aabb→aabbb]
- Lee `a`: {aabbb} ⟶ {aabbba} [aabbb→aabbba]
- **Aceptada**: queda {aabbba} ∈ F.

## Cadena `aaabbaabaabbba`

- Inicio: {λ}
- Lee `a`: {λ} ⟶ {a} [λ→a]
- Lee `a`: {a} ⟶ {aa} [a→aa]
- Lee `a`: {aa} ⟶ {aa} [aa→aa]
- Lee `b`: {aa} ⟶ {aab} [aa→aab]
- Lee `b`: {aab} ⟶ {aabb} [aab→aabb]
- Lee `a`: {aabb} ⟶ {a} [aabb→a]
- Lee `a`: {a} ⟶ {aa} [a→aa]
- Lee `b`: {aa} ⟶ {aab} [aa→aab]
- Lee `a`: {aab} ⟶ {a} [aab→a]
- Lee `a`: {a} ⟶ {aa} [a→aa]
- Lee `b`: {aa} ⟶ {aab} [aa→aab]
- Lee `b`: {aab} ⟶ {aabb} [aab→aabb]
- Lee `b`: {aabb} ⟶ {aabbb} [aabb→aabbb]
- Lee `a`: {aabbb} ⟶ {aabbba} [aabbb→aabbba]
- **Aceptada**: queda {aabbba} ∈ F.

## Cadena λ

- Inicio: {λ}
- **Rechazada**: ningún estado de {λ} es de aceptación.

## Cadena `a`

- Inicio: {λ}
- Lee `a`: {λ} ⟶ {a} [λ→a]
- **Rechazada**: ningún estado de {a} es de aceptación.

## Cadena `aab`

- Inicio: {λ}
- Lee `a`: {λ} ⟶ {a} [λ→a]
- Lee `a`: {a} ⟶ {aa} [a→aa]
- Lee `b`: {aa} ⟶ {aab} [aa→aab]
- **Rechazada**: ningún estado de {aab} es de aceptación.

## Cadena `aaaaa`

- Inicio: {λ}
- Lee `a`: {λ} ⟶ {a} [λ→a]
- Lee `a`: {a} ⟶ {aa} [a→aa]
- Lee `a`: {aa} ⟶ {aa} [aa→aa]
- Lee `a`: {aa} ⟶ {aa} [aa→aa]
- Lee `a`: {aa} ⟶ {aa} [aa→aa]
- **Rechazada**: ningún estado de {aa} es de aceptación.

## Cadena `baaaaabb`

- Inicio: {λ}
- Lee `b`: {λ} ⟶ {λ} [λ→λ]
- Lee `a`: {λ} ⟶ {a} [λ→a]
- Lee `a`: {a} ⟶ {aa} [a→aa]
- Lee `a`: {aa} ⟶ {aa} [aa→aa]
- Lee `a`: {aa} ⟶ {aa} [aa→aa]
- Lee `a`: {aa} ⟶ {aa} [aa→aa]
- Lee `b`: {aa} ⟶ {aab} [aa→aab]
- Lee `b`: {aab} ⟶ {aabb} [aab→aabb]
- **Rechazada**: ningún estado de {aabb} es de aceptación.

## Cadena `aabab`

- Inicio: {λ}
- Lee `a`: {λ} ⟶ {a} [λ→a]
- Lee `a`: {a} ⟶ {aa} [a→aa]
- Lee `b`: {aa} ⟶ {aab} [aa→aab]
- Lee `a`: {aab} ⟶ {a} [aab→a]
- Lee `b`: {a} ⟶ {λ} [a→λ]
- **Rechazada**: ningún estado de {λ} es de aceptación.
