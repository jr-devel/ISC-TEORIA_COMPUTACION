# Recorridos: Lista 2 · Ejercicio 104

Las palabras de Σ3 que inician con la cadena abbab.

Autómata: `lista2-104` (AFD).

## Cadena `abbab`

- Inicio: {λ}
- Lee `a`: {λ} ⟶ {a} [λ→a]
- Lee `b`: {a} ⟶ {ab} [a→ab]
- Lee `b`: {ab} ⟶ {abb} [ab→abb]
- Lee `a`: {abb} ⟶ {abba} [abb→abba]
- Lee `b`: {abba} ⟶ {abbab} [abba→abbab]
- **Aceptada**: queda {abbab} ∈ F.

## Cadena `abbaba`

- Inicio: {λ}
- Lee `a`: {λ} ⟶ {a} [λ→a]
- Lee `b`: {a} ⟶ {ab} [a→ab]
- Lee `b`: {ab} ⟶ {abb} [ab→abb]
- Lee `a`: {abb} ⟶ {abba} [abb→abba]
- Lee `b`: {abba} ⟶ {abbab} [abba→abbab]
- Lee `a`: {abbab} ⟶ {abbab} [abbab→abbab]
- **Aceptada**: queda {abbab} ∈ F.

## Cadena `abbabaab`

- Inicio: {λ}
- Lee `a`: {λ} ⟶ {a} [λ→a]
- Lee `b`: {a} ⟶ {ab} [a→ab]
- Lee `b`: {ab} ⟶ {abb} [ab→abb]
- Lee `a`: {abb} ⟶ {abba} [abb→abba]
- Lee `b`: {abba} ⟶ {abbab} [abba→abbab]
- Lee `a`: {abbab} ⟶ {abbab} [abbab→abbab]
- Lee `a`: {abbab} ⟶ {abbab} [abbab→abbab]
- Lee `b`: {abbab} ⟶ {abbab} [abbab→abbab]
- **Aceptada**: queda {abbab} ∈ F.

## Cadena `abbabbabbb`

- Inicio: {λ}
- Lee `a`: {λ} ⟶ {a} [λ→a]
- Lee `b`: {a} ⟶ {ab} [a→ab]
- Lee `b`: {ab} ⟶ {abb} [ab→abb]
- Lee `a`: {abb} ⟶ {abba} [abb→abba]
- Lee `b`: {abba} ⟶ {abbab} [abba→abbab]
- Lee `b`: {abbab} ⟶ {abbab} [abbab→abbab]
- Lee `a`: {abbab} ⟶ {abbab} [abbab→abbab]
- Lee `b`: {abbab} ⟶ {abbab} [abbab→abbab]
- Lee `b`: {abbab} ⟶ {abbab} [abbab→abbab]
- Lee `b`: {abbab} ⟶ {abbab} [abbab→abbab]
- **Aceptada**: queda {abbab} ∈ F.

## Cadena `abbabbaaaabba`

- Inicio: {λ}
- Lee `a`: {λ} ⟶ {a} [λ→a]
- Lee `b`: {a} ⟶ {ab} [a→ab]
- Lee `b`: {ab} ⟶ {abb} [ab→abb]
- Lee `a`: {abb} ⟶ {abba} [abb→abba]
- Lee `b`: {abba} ⟶ {abbab} [abba→abbab]
- Lee `b`: {abbab} ⟶ {abbab} [abbab→abbab]
- Lee `a`: {abbab} ⟶ {abbab} [abbab→abbab]
- Lee `a`: {abbab} ⟶ {abbab} [abbab→abbab]
- Lee `a`: {abbab} ⟶ {abbab} [abbab→abbab]
- Lee `a`: {abbab} ⟶ {abbab} [abbab→abbab]
- Lee `b`: {abbab} ⟶ {abbab} [abbab→abbab]
- Lee `b`: {abbab} ⟶ {abbab} [abbab→abbab]
- Lee `a`: {abbab} ⟶ {abbab} [abbab→abbab]
- **Aceptada**: queda {abbab} ∈ F.

## Cadena λ

- Inicio: {λ}
- **Rechazada**: ningún estado de {λ} es de aceptación.

## Cadena `a`

- Inicio: {λ}
- Lee `a`: {λ} ⟶ {a} [λ→a]
- **Rechazada**: ningún estado de {a} es de aceptación.

## Cadena `bab`

- Inicio: {λ}
- Lee `b`: {λ} ⟶ {muerto} [λ→muerto]
- Lee `a`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `b`: {muerto} ⟶ {muerto} [muerto→muerto]
- **Rechazada**: ningún estado de {muerto} es de aceptación.

## Cadena `bbbba`

- Inicio: {λ}
- Lee `b`: {λ} ⟶ {muerto} [λ→muerto]
- Lee `b`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `b`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `b`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `a`: {muerto} ⟶ {muerto} [muerto→muerto]
- **Rechazada**: ningún estado de {muerto} es de aceptación.

## Cadena `aabbbaba`

- Inicio: {λ}
- Lee `a`: {λ} ⟶ {a} [λ→a]
- Lee `a`: {a} ⟶ {muerto} [a→muerto]
- Lee `b`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `b`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `b`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `a`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `b`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `a`: {muerto} ⟶ {muerto} [muerto→muerto]
- **Rechazada**: ningún estado de {muerto} es de aceptación.

## Cadena `bbba`

- Inicio: {λ}
- Lee `b`: {λ} ⟶ {muerto} [λ→muerto]
- Lee `b`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `b`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `a`: {muerto} ⟶ {muerto} [muerto→muerto]
- **Rechazada**: ningún estado de {muerto} es de aceptación.
