# Recorridos: Lista 2 · Ejercicio 105

Las palabras de Σ3 que terminan con la cadena abaa.

Autómata: `lista2-105` (AFD).

## Cadena `abaa`

- Inicio: {λ}
- Lee `a`: {λ} ⟶ {a} [λ→a]
- Lee `b`: {a} ⟶ {ab} [a→ab]
- Lee `a`: {ab} ⟶ {aba} [ab→aba]
- Lee `a`: {aba} ⟶ {abaa} [aba→abaa]
- **Aceptada**: queda {abaa} ∈ F.

## Cadena `aabaa`

- Inicio: {λ}
- Lee `a`: {λ} ⟶ {a} [λ→a]
- Lee `a`: {a} ⟶ {a} [a→a]
- Lee `b`: {a} ⟶ {ab} [a→ab]
- Lee `a`: {ab} ⟶ {aba} [ab→aba]
- Lee `a`: {aba} ⟶ {abaa} [aba→abaa]
- **Aceptada**: queda {abaa} ∈ F.

## Cadena `bbaabaa`

- Inicio: {λ}
- Lee `b`: {λ} ⟶ {λ} [λ→λ]
- Lee `b`: {λ} ⟶ {λ} [λ→λ]
- Lee `a`: {λ} ⟶ {a} [λ→a]
- Lee `a`: {a} ⟶ {a} [a→a]
- Lee `b`: {a} ⟶ {ab} [a→ab]
- Lee `a`: {ab} ⟶ {aba} [ab→aba]
- Lee `a`: {aba} ⟶ {abaa} [aba→abaa]
- **Aceptada**: queda {abaa} ∈ F.

## Cadena `aabababaa`

- Inicio: {λ}
- Lee `a`: {λ} ⟶ {a} [λ→a]
- Lee `a`: {a} ⟶ {a} [a→a]
- Lee `b`: {a} ⟶ {ab} [a→ab]
- Lee `a`: {ab} ⟶ {aba} [ab→aba]
- Lee `b`: {aba} ⟶ {ab} [aba→ab]
- Lee `a`: {ab} ⟶ {aba} [ab→aba]
- Lee `b`: {aba} ⟶ {ab} [aba→ab]
- Lee `a`: {ab} ⟶ {aba} [ab→aba]
- Lee `a`: {aba} ⟶ {abaa} [aba→abaa]
- **Aceptada**: queda {abaa} ∈ F.

## Cadena `babbabbbabaa`

- Inicio: {λ}
- Lee `b`: {λ} ⟶ {λ} [λ→λ]
- Lee `a`: {λ} ⟶ {a} [λ→a]
- Lee `b`: {a} ⟶ {ab} [a→ab]
- Lee `b`: {ab} ⟶ {λ} [ab→λ]
- Lee `a`: {λ} ⟶ {a} [λ→a]
- Lee `b`: {a} ⟶ {ab} [a→ab]
- Lee `b`: {ab} ⟶ {λ} [ab→λ]
- Lee `b`: {λ} ⟶ {λ} [λ→λ]
- Lee `a`: {λ} ⟶ {a} [λ→a]
- Lee `b`: {a} ⟶ {ab} [a→ab]
- Lee `a`: {ab} ⟶ {aba} [ab→aba]
- Lee `a`: {aba} ⟶ {abaa} [aba→abaa]
- **Aceptada**: queda {abaa} ∈ F.

## Cadena λ

- Inicio: {λ}
- **Rechazada**: ningún estado de {λ} es de aceptación.

## Cadena `a`

- Inicio: {λ}
- Lee `a`: {λ} ⟶ {a} [λ→a]
- **Rechazada**: ningún estado de {a} es de aceptación.

## Cadena `abb`

- Inicio: {λ}
- Lee `a`: {λ} ⟶ {a} [λ→a]
- Lee `b`: {a} ⟶ {ab} [a→ab]
- Lee `b`: {ab} ⟶ {λ} [ab→λ]
- **Rechazada**: ningún estado de {λ} es de aceptación.

## Cadena `baaaa`

- Inicio: {λ}
- Lee `b`: {λ} ⟶ {λ} [λ→λ]
- Lee `a`: {λ} ⟶ {a} [λ→a]
- Lee `a`: {a} ⟶ {a} [a→a]
- Lee `a`: {a} ⟶ {a} [a→a]
- Lee `a`: {a} ⟶ {a} [a→a]
- **Rechazada**: ningún estado de {a} es de aceptación.

## Cadena `bababbaa`

- Inicio: {λ}
- Lee `b`: {λ} ⟶ {λ} [λ→λ]
- Lee `a`: {λ} ⟶ {a} [λ→a]
- Lee `b`: {a} ⟶ {ab} [a→ab]
- Lee `a`: {ab} ⟶ {aba} [ab→aba]
- Lee `b`: {aba} ⟶ {ab} [aba→ab]
- Lee `b`: {ab} ⟶ {λ} [ab→λ]
- Lee `a`: {λ} ⟶ {a} [λ→a]
- Lee `a`: {a} ⟶ {a} [a→a]
- **Rechazada**: ningún estado de {a} es de aceptación.

## Cadena `bbb`

- Inicio: {λ}
- Lee `b`: {λ} ⟶ {λ} [λ→λ]
- Lee `b`: {λ} ⟶ {λ} [λ→λ]
- Lee `b`: {λ} ⟶ {λ} [λ→λ]
- **Rechazada**: ningún estado de {λ} es de aceptación.
