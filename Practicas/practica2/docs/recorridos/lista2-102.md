# Recorridos: Lista 2 · Ejercicio 102

Las palabras de Σ3 que contienen la cadena abbbab.

Autómata: `lista2-102` (AFD).

## Cadena `abbbab`

- Inicio: {λ}
- Lee `a`: {λ} ⟶ {a} [λ→a]
- Lee `b`: {a} ⟶ {ab} [a→ab]
- Lee `b`: {ab} ⟶ {abb} [ab→abb]
- Lee `b`: {abb} ⟶ {abbb} [abb→abbb]
- Lee `a`: {abbb} ⟶ {abbba} [abbb→abbba]
- Lee `b`: {abbba} ⟶ {abbbab} [abbba→abbbab]
- **Aceptada**: queda {abbbab} ∈ F.

## Cadena `abbbaba`

- Inicio: {λ}
- Lee `a`: {λ} ⟶ {a} [λ→a]
- Lee `b`: {a} ⟶ {ab} [a→ab]
- Lee `b`: {ab} ⟶ {abb} [ab→abb]
- Lee `b`: {abb} ⟶ {abbb} [abb→abbb]
- Lee `a`: {abbb} ⟶ {abbba} [abbb→abbba]
- Lee `b`: {abbba} ⟶ {abbbab} [abbba→abbbab]
- Lee `a`: {abbbab} ⟶ {abbbab} [abbbab→abbbab]
- **Aceptada**: queda {abbbab} ∈ F.

## Cadena `aabbbabab`

- Inicio: {λ}
- Lee `a`: {λ} ⟶ {a} [λ→a]
- Lee `a`: {a} ⟶ {a} [a→a]
- Lee `b`: {a} ⟶ {ab} [a→ab]
- Lee `b`: {ab} ⟶ {abb} [ab→abb]
- Lee `b`: {abb} ⟶ {abbb} [abb→abbb]
- Lee `a`: {abbb} ⟶ {abbba} [abbb→abbba]
- Lee `b`: {abbba} ⟶ {abbbab} [abbba→abbbab]
- Lee `a`: {abbbab} ⟶ {abbbab} [abbbab→abbbab]
- Lee `b`: {abbbab} ⟶ {abbbab} [abbbab→abbbab]
- **Aceptada**: queda {abbbab} ∈ F.

## Cadena `babaaabbbab`

- Inicio: {λ}
- Lee `b`: {λ} ⟶ {λ} [λ→λ]
- Lee `a`: {λ} ⟶ {a} [λ→a]
- Lee `b`: {a} ⟶ {ab} [a→ab]
- Lee `a`: {ab} ⟶ {a} [ab→a]
- Lee `a`: {a} ⟶ {a} [a→a]
- Lee `a`: {a} ⟶ {a} [a→a]
- Lee `b`: {a} ⟶ {ab} [a→ab]
- Lee `b`: {ab} ⟶ {abb} [ab→abb]
- Lee `b`: {abb} ⟶ {abbb} [abb→abbb]
- Lee `a`: {abbb} ⟶ {abbba} [abbb→abbba]
- Lee `b`: {abbba} ⟶ {abbbab} [abbba→abbbab]
- **Aceptada**: queda {abbbab} ∈ F.

## Cadena `babbbababbbabb`

- Inicio: {λ}
- Lee `b`: {λ} ⟶ {λ} [λ→λ]
- Lee `a`: {λ} ⟶ {a} [λ→a]
- Lee `b`: {a} ⟶ {ab} [a→ab]
- Lee `b`: {ab} ⟶ {abb} [ab→abb]
- Lee `b`: {abb} ⟶ {abbb} [abb→abbb]
- Lee `a`: {abbb} ⟶ {abbba} [abbb→abbba]
- Lee `b`: {abbba} ⟶ {abbbab} [abbba→abbbab]
- Lee `a`: {abbbab} ⟶ {abbbab} [abbbab→abbbab]
- Lee `b`: {abbbab} ⟶ {abbbab} [abbbab→abbbab]
- Lee `b`: {abbbab} ⟶ {abbbab} [abbbab→abbbab]
- Lee `b`: {abbbab} ⟶ {abbbab} [abbbab→abbbab]
- Lee `a`: {abbbab} ⟶ {abbbab} [abbbab→abbbab]
- Lee `b`: {abbbab} ⟶ {abbbab} [abbbab→abbbab]
- Lee `b`: {abbbab} ⟶ {abbbab} [abbbab→abbbab]
- **Aceptada**: queda {abbbab} ∈ F.

## Cadena λ

- Inicio: {λ}
- **Rechazada**: ningún estado de {λ} es de aceptación.

## Cadena `b`

- Inicio: {λ}
- Lee `b`: {λ} ⟶ {λ} [λ→λ]
- **Rechazada**: ningún estado de {λ} es de aceptación.

## Cadena `aab`

- Inicio: {λ}
- Lee `a`: {λ} ⟶ {a} [λ→a]
- Lee `a`: {a} ⟶ {a} [a→a]
- Lee `b`: {a} ⟶ {ab} [a→ab]
- **Rechazada**: ningún estado de {ab} es de aceptación.

## Cadena `bbbaa`

- Inicio: {λ}
- Lee `b`: {λ} ⟶ {λ} [λ→λ]
- Lee `b`: {λ} ⟶ {λ} [λ→λ]
- Lee `b`: {λ} ⟶ {λ} [λ→λ]
- Lee `a`: {λ} ⟶ {a} [λ→a]
- Lee `a`: {a} ⟶ {a} [a→a]
- **Rechazada**: ningún estado de {a} es de aceptación.

## Cadena `aabaabaa`

- Inicio: {λ}
- Lee `a`: {λ} ⟶ {a} [λ→a]
- Lee `a`: {a} ⟶ {a} [a→a]
- Lee `b`: {a} ⟶ {ab} [a→ab]
- Lee `a`: {ab} ⟶ {a} [ab→a]
- Lee `a`: {a} ⟶ {a} [a→a]
- Lee `b`: {a} ⟶ {ab} [a→ab]
- Lee `a`: {ab} ⟶ {a} [ab→a]
- Lee `a`: {a} ⟶ {a} [a→a]
- **Rechazada**: ningún estado de {a} es de aceptación.

## Cadena `baaab`

- Inicio: {λ}
- Lee `b`: {λ} ⟶ {λ} [λ→λ]
- Lee `a`: {λ} ⟶ {a} [λ→a]
- Lee `a`: {a} ⟶ {a} [a→a]
- Lee `a`: {a} ⟶ {a} [a→a]
- Lee `b`: {a} ⟶ {ab} [a→ab]
- **Rechazada**: ningún estado de {ab} es de aceptación.
