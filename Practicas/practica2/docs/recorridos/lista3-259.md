# Recorridos: Lista 3 · Ejercicio 259

Valores R_ij^(k) necesarios para R14^(4) y expresión regular del autómata.

Autómata: `lista3-259` (AFD).

## Cadena λ

- Inicio: {1}
- **Rechazada**: ningún estado de {1} es de aceptación.

## Cadena `b`

- Inicio: {1}
- Lee `b`: {1} ⟶ {2} [1→2]
- **Rechazada**: ningún estado de {2} es de aceptación.

## Cadena `aba`

- Inicio: {1}
- Lee `a`: {1} ⟶ {3} [1→3]
- Lee `b`: {3} ⟶ {3} [3→3]
- Lee `a`: {3} ⟶ {2} [3→2]
- **Rechazada**: ningún estado de {2} es de aceptación.

## Cadena `baaba`

- Inicio: {1}
- Lee `b`: {1} ⟶ {2} [1→2]
- Lee `a`: {2} ⟶ {1} [2→1]
- Lee `a`: {1} ⟶ {3} [1→3]
- Lee `b`: {3} ⟶ {3} [3→3]
- Lee `a`: {3} ⟶ {2} [3→2]
- **Rechazada**: ningún estado de {2} es de aceptación.

## Cadena `aabaabbb`

- Inicio: {1}
- Lee `a`: {1} ⟶ {3} [1→3]
- Lee `a`: {3} ⟶ {2} [3→2]
- Lee `b`: {2} ⟶ {3} [2→3]
- Lee `a`: {3} ⟶ {2} [3→2]
- Lee `a`: {2} ⟶ {1} [2→1]
- Lee `b`: {1} ⟶ {2} [1→2]
- Lee `b`: {2} ⟶ {3} [2→3]
- Lee `b`: {3} ⟶ {3} [3→3]
- **Rechazada**: ningún estado de {3} es de aceptación.
