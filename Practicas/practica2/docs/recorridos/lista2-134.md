# Recorridos: Lista 2 · Ejercicio 134

L(M) = {w ∈ {a, b, c}* : w contiene el patrón abac}.

Autómata: `lista2-134` (AFD).

## Cadena `abac`

- Inicio: {λ}
- Lee `a`: {λ} ⟶ {a} [λ→a]
- Lee `b`: {a} ⟶ {ab} [a→ab]
- Lee `a`: {ab} ⟶ {aba} [ab→aba]
- Lee `c`: {aba} ⟶ {abac} [aba→abac]
- **Aceptada**: queda {abac} ∈ F.

## Cadena `abaca`

- Inicio: {λ}
- Lee `a`: {λ} ⟶ {a} [λ→a]
- Lee `b`: {a} ⟶ {ab} [a→ab]
- Lee `a`: {ab} ⟶ {aba} [ab→aba]
- Lee `c`: {aba} ⟶ {abac} [aba→abac]
- Lee `a`: {abac} ⟶ {abac} [abac→abac]
- **Aceptada**: queda {abac} ∈ F.

## Cadena `bbaabac`

- Inicio: {λ}
- Lee `b`: {λ} ⟶ {λ} [λ→λ]
- Lee `b`: {λ} ⟶ {λ} [λ→λ]
- Lee `a`: {λ} ⟶ {a} [λ→a]
- Lee `a`: {a} ⟶ {a} [a→a]
- Lee `b`: {a} ⟶ {ab} [a→ab]
- Lee `a`: {ab} ⟶ {aba} [ab→aba]
- Lee `c`: {aba} ⟶ {abac} [aba→abac]
- **Aceptada**: queda {abac} ∈ F.

## Cadena `abacbbcbb`

- Inicio: {λ}
- Lee `a`: {λ} ⟶ {a} [λ→a]
- Lee `b`: {a} ⟶ {ab} [a→ab]
- Lee `a`: {ab} ⟶ {aba} [ab→aba]
- Lee `c`: {aba} ⟶ {abac} [aba→abac]
- Lee `b`: {abac} ⟶ {abac} [abac→abac]
- Lee `b`: {abac} ⟶ {abac} [abac→abac]
- Lee `c`: {abac} ⟶ {abac} [abac→abac]
- Lee `b`: {abac} ⟶ {abac} [abac→abac]
- Lee `b`: {abac} ⟶ {abac} [abac→abac]
- **Aceptada**: queda {abac} ∈ F.

## Cadena `ababacccacab`

- Inicio: {λ}
- Lee `a`: {λ} ⟶ {a} [λ→a]
- Lee `b`: {a} ⟶ {ab} [a→ab]
- Lee `a`: {ab} ⟶ {aba} [ab→aba]
- Lee `b`: {aba} ⟶ {ab} [aba→ab]
- Lee `a`: {ab} ⟶ {aba} [ab→aba]
- Lee `c`: {aba} ⟶ {abac} [aba→abac]
- Lee `c`: {abac} ⟶ {abac} [abac→abac]
- Lee `c`: {abac} ⟶ {abac} [abac→abac]
- Lee `a`: {abac} ⟶ {abac} [abac→abac]
- Lee `c`: {abac} ⟶ {abac} [abac→abac]
- Lee `a`: {abac} ⟶ {abac} [abac→abac]
- Lee `b`: {abac} ⟶ {abac} [abac→abac]
- **Aceptada**: queda {abac} ∈ F.

## Cadena λ

- Inicio: {λ}
- **Rechazada**: ningún estado de {λ} es de aceptación.

## Cadena `c`

- Inicio: {λ}
- Lee `c`: {λ} ⟶ {λ} [λ→λ]
- **Rechazada**: ningún estado de {λ} es de aceptación.

## Cadena `bcc`

- Inicio: {λ}
- Lee `b`: {λ} ⟶ {λ} [λ→λ]
- Lee `c`: {λ} ⟶ {λ} [λ→λ]
- Lee `c`: {λ} ⟶ {λ} [λ→λ]
- **Rechazada**: ningún estado de {λ} es de aceptación.

## Cadena `ccaba`

- Inicio: {λ}
- Lee `c`: {λ} ⟶ {λ} [λ→λ]
- Lee `c`: {λ} ⟶ {λ} [λ→λ]
- Lee `a`: {λ} ⟶ {a} [λ→a]
- Lee `b`: {a} ⟶ {ab} [a→ab]
- Lee `a`: {ab} ⟶ {aba} [ab→aba]
- **Rechazada**: ningún estado de {aba} es de aceptación.

## Cadena `acbcbbcc`

- Inicio: {λ}
- Lee `a`: {λ} ⟶ {a} [λ→a]
- Lee `c`: {a} ⟶ {λ} [a→λ]
- Lee `b`: {λ} ⟶ {λ} [λ→λ]
- Lee `c`: {λ} ⟶ {λ} [λ→λ]
- Lee `b`: {λ} ⟶ {λ} [λ→λ]
- Lee `b`: {λ} ⟶ {λ} [λ→λ]
- Lee `c`: {λ} ⟶ {λ} [λ→λ]
- Lee `c`: {λ} ⟶ {λ} [λ→λ]
- **Rechazada**: ningún estado de {λ} es de aceptación.

## Cadena `aaa`

- Inicio: {λ}
- Lee `a`: {λ} ⟶ {a} [λ→a]
- Lee `a`: {a} ⟶ {a} [a→a]
- Lee `a`: {a} ⟶ {a} [a→a]
- **Rechazada**: ningún estado de {a} es de aceptación.
