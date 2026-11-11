# Recorridos: Lista 2 · Ejercicio 127

Sea A un AFD. ¿Cuál es el lenguaje del autómata si F = Q?

Autómata: `lista2-127` (AFD).

## Cadena λ

- Inicio: {par}
- **Aceptada**: queda {par} ∈ F.

## Cadena `1`

- Inicio: {par}
- Lee `1`: {par} ⟶ {par} [par→par]
- **Aceptada**: queda {par} ∈ F.

## Cadena `100`

- Inicio: {par}
- Lee `1`: {par} ⟶ {par} [par→par]
- Lee `0`: {par} ⟶ {impar} [par→impar]
- Lee `0`: {impar} ⟶ {par} [impar→par]
- **Aceptada**: queda {par} ∈ F.

## Cadena `00001`

- Inicio: {par}
- Lee `0`: {par} ⟶ {impar} [par→impar]
- Lee `0`: {impar} ⟶ {par} [impar→par]
- Lee `0`: {par} ⟶ {impar} [par→impar]
- Lee `0`: {impar} ⟶ {par} [impar→par]
- Lee `1`: {par} ⟶ {par} [par→par]
- **Aceptada**: queda {par} ∈ F.

## Cadena `00111011`

- Inicio: {par}
- Lee `0`: {par} ⟶ {impar} [par→impar]
- Lee `0`: {impar} ⟶ {par} [impar→par]
- Lee `1`: {par} ⟶ {par} [par→par]
- Lee `1`: {par} ⟶ {par} [par→par]
- Lee `1`: {par} ⟶ {par} [par→par]
- Lee `0`: {par} ⟶ {impar} [par→impar]
- Lee `1`: {impar} ⟶ {impar} [impar→impar]
- Lee `1`: {impar} ⟶ {impar} [impar→impar]
- **Aceptada**: queda {impar} ∈ F.
