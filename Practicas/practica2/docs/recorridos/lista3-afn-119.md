# Recorridos: Lista 3 · AFN del problema 119

AFN para el problema 119: Las palabras de Σ3 tales que después de cada subcadena aa aparece una b.

Autómata: `lista3-afn-119` (AFD).

## Cadena λ

- Inicio: {sin a}
- **Aceptada**: queda {sin a} ∈ F.

## Cadena `b`

- Inicio: {sin a}
- Lee `b`: {sin a} ⟶ {sin a} [sin a→sin a]
- **Aceptada**: queda {sin a} ∈ F.

## Cadena `aba`

- Inicio: {sin a}
- Lee `a`: {sin a} ⟶ {a} [sin a→a]
- Lee `b`: {a} ⟶ {sin a} [a→sin a]
- Lee `a`: {sin a} ⟶ {a} [sin a→a]
- **Aceptada**: queda {a} ∈ F.

## Cadena `babba`

- Inicio: {sin a}
- Lee `b`: {sin a} ⟶ {sin a} [sin a→sin a]
- Lee `a`: {sin a} ⟶ {a} [sin a→a]
- Lee `b`: {a} ⟶ {sin a} [a→sin a]
- Lee `b`: {sin a} ⟶ {sin a} [sin a→sin a]
- Lee `a`: {sin a} ⟶ {a} [sin a→a]
- **Aceptada**: queda {a} ∈ F.

## Cadena `bbbabbbb`

- Inicio: {sin a}
- Lee `b`: {sin a} ⟶ {sin a} [sin a→sin a]
- Lee `b`: {sin a} ⟶ {sin a} [sin a→sin a]
- Lee `b`: {sin a} ⟶ {sin a} [sin a→sin a]
- Lee `a`: {sin a} ⟶ {a} [sin a→a]
- Lee `b`: {a} ⟶ {sin a} [a→sin a]
- Lee `b`: {sin a} ⟶ {sin a} [sin a→sin a]
- Lee `b`: {sin a} ⟶ {sin a} [sin a→sin a]
- Lee `b`: {sin a} ⟶ {sin a} [sin a→sin a]
- **Aceptada**: queda {sin a} ∈ F.

## Cadena `aa`

- Inicio: {sin a}
- Lee `a`: {sin a} ⟶ {a} [sin a→a]
- Lee `a`: {a} ⟶ {aa} [a→aa]
- **Rechazada**: ningún estado de {aa} es de aceptación.

## Cadena `aaa`

- Inicio: {sin a}
- Lee `a`: {sin a} ⟶ {a} [sin a→a]
- Lee `a`: {a} ⟶ {aa} [a→aa]
- Lee `a`: {aa} ⟶ ∅ [ninguna transición]
- **Rechazada**: no queda ningún estado activo.

## Cadena `aabaa`

- Inicio: {sin a}
- Lee `a`: {sin a} ⟶ {a} [sin a→a]
- Lee `a`: {a} ⟶ {aa} [a→aa]
- Lee `b`: {aa} ⟶ {sin a} [aa→sin a]
- Lee `a`: {sin a} ⟶ {a} [sin a→a]
- Lee `a`: {a} ⟶ {aa} [a→aa]
- **Rechazada**: ningún estado de {aa} es de aceptación.

## Cadena `babbbaa`

- Inicio: {sin a}
- Lee `b`: {sin a} ⟶ {sin a} [sin a→sin a]
- Lee `a`: {sin a} ⟶ {a} [sin a→a]
- Lee `b`: {a} ⟶ {sin a} [a→sin a]
- Lee `b`: {sin a} ⟶ {sin a} [sin a→sin a]
- Lee `b`: {sin a} ⟶ {sin a} [sin a→sin a]
- Lee `a`: {sin a} ⟶ {a} [sin a→a]
- Lee `a`: {a} ⟶ {aa} [a→aa]
- **Rechazada**: ningún estado de {aa} es de aceptación.

## Cadena `aaaaaaaabb`

- Inicio: {sin a}
- Lee `a`: {sin a} ⟶ {a} [sin a→a]
- Lee `a`: {a} ⟶ {aa} [a→aa]
- Lee `a`: {aa} ⟶ ∅ [ninguna transición]
- Lee `a`: ∅ ⟶ ∅ [ninguna transición]
- Lee `a`: ∅ ⟶ ∅ [ninguna transición]
- Lee `a`: ∅ ⟶ ∅ [ninguna transición]
- Lee `a`: ∅ ⟶ ∅ [ninguna transición]
- Lee `a`: ∅ ⟶ ∅ [ninguna transición]
- Lee `b`: ∅ ⟶ ∅ [ninguna transición]
- Lee `b`: ∅ ⟶ ∅ [ninguna transición]
- **Rechazada**: no queda ningún estado activo.
