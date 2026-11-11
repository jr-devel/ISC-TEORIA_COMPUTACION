# Recorridos: Lista 2 · Ejercicio 101

Las palabras de Σ3 que contienen la cadena aba.

Autómata: `lista2-101` (AFD).

## Cadena `aba`

- Inicio: {λ}
- Lee `a`: {λ} ⟶ {a} [λ→a]
- Lee `b`: {a} ⟶ {ab} [a→ab]
- Lee `a`: {ab} ⟶ {aba} [ab→aba]
- **Aceptada**: queda {aba} ∈ F.

## Cadena `aaba`

- Inicio: {λ}
- Lee `a`: {λ} ⟶ {a} [λ→a]
- Lee `a`: {a} ⟶ {a} [a→a]
- Lee `b`: {a} ⟶ {ab} [a→ab]
- Lee `a`: {ab} ⟶ {aba} [ab→aba]
- **Aceptada**: queda {aba} ∈ F.

## Cadena `bbabaa`

- Inicio: {λ}
- Lee `b`: {λ} ⟶ {λ} [λ→λ]
- Lee `b`: {λ} ⟶ {λ} [λ→λ]
- Lee `a`: {λ} ⟶ {a} [λ→a]
- Lee `b`: {a} ⟶ {ab} [a→ab]
- Lee `a`: {ab} ⟶ {aba} [ab→aba]
- Lee `a`: {aba} ⟶ {aba} [aba→aba]
- **Aceptada**: queda {aba} ∈ F.

## Cadena `bababbaa`

- Inicio: {λ}
- Lee `b`: {λ} ⟶ {λ} [λ→λ]
- Lee `a`: {λ} ⟶ {a} [λ→a]
- Lee `b`: {a} ⟶ {ab} [a→ab]
- Lee `a`: {ab} ⟶ {aba} [ab→aba]
- Lee `b`: {aba} ⟶ {aba} [aba→aba]
- Lee `b`: {aba} ⟶ {aba} [aba→aba]
- Lee `a`: {aba} ⟶ {aba} [aba→aba]
- Lee `a`: {aba} ⟶ {aba} [aba→aba]
- **Aceptada**: queda {aba} ∈ F.

## Cadena `aaababaaaab`

- Inicio: {λ}
- Lee `a`: {λ} ⟶ {a} [λ→a]
- Lee `a`: {a} ⟶ {a} [a→a]
- Lee `a`: {a} ⟶ {a} [a→a]
- Lee `b`: {a} ⟶ {ab} [a→ab]
- Lee `a`: {ab} ⟶ {aba} [ab→aba]
- Lee `b`: {aba} ⟶ {aba} [aba→aba]
- Lee `a`: {aba} ⟶ {aba} [aba→aba]
- Lee `a`: {aba} ⟶ {aba} [aba→aba]
- Lee `a`: {aba} ⟶ {aba} [aba→aba]
- Lee `a`: {aba} ⟶ {aba} [aba→aba]
- Lee `b`: {aba} ⟶ {aba} [aba→aba]
- **Aceptada**: queda {aba} ∈ F.

## Cadena λ

- Inicio: {λ}
- **Rechazada**: ningún estado de {λ} es de aceptación.

## Cadena `b`

- Inicio: {λ}
- Lee `b`: {λ} ⟶ {λ} [λ→λ]
- **Rechazada**: ningún estado de {λ} es de aceptación.

## Cadena `aaa`

- Inicio: {λ}
- Lee `a`: {λ} ⟶ {a} [λ→a]
- Lee `a`: {a} ⟶ {a} [a→a]
- Lee `a`: {a} ⟶ {a} [a→a]
- **Rechazada**: ningún estado de {a} es de aceptación.

## Cadena `bbbbb`

- Inicio: {λ}
- Lee `b`: {λ} ⟶ {λ} [λ→λ]
- Lee `b`: {λ} ⟶ {λ} [λ→λ]
- Lee `b`: {λ} ⟶ {λ} [λ→λ]
- Lee `b`: {λ} ⟶ {λ} [λ→λ]
- Lee `b`: {λ} ⟶ {λ} [λ→λ]
- **Rechazada**: ningún estado de {λ} es de aceptación.

## Cadena `bbaabbaa`

- Inicio: {λ}
- Lee `b`: {λ} ⟶ {λ} [λ→λ]
- Lee `b`: {λ} ⟶ {λ} [λ→λ]
- Lee `a`: {λ} ⟶ {a} [λ→a]
- Lee `a`: {a} ⟶ {a} [a→a]
- Lee `b`: {a} ⟶ {ab} [a→ab]
- Lee `b`: {ab} ⟶ {λ} [ab→λ]
- Lee `a`: {λ} ⟶ {a} [λ→a]
- Lee `a`: {a} ⟶ {a} [a→a]
- **Rechazada**: ningún estado de {a} es de aceptación.

## Cadena `ab`

- Inicio: {λ}
- Lee `a`: {λ} ⟶ {a} [λ→a]
- Lee `b`: {a} ⟶ {ab} [a→ab]
- **Rechazada**: ningún estado de {ab} es de aceptación.
