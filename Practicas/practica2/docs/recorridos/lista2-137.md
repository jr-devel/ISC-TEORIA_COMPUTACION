# Recorridos: Lista 2 · Ejercicio 137

AFD que reconozca las cadenas sobre {a, b} que comienzan con el prefijo ab.

Autómata: `lista2-137` (AFD).

## Cadena `ab`

- Inicio: {λ}
- Lee `a`: {λ} ⟶ {a} [λ→a]
- Lee `b`: {a} ⟶ {ab} [a→ab]
- **Aceptada**: queda {ab} ∈ F.

## Cadena `aba`

- Inicio: {λ}
- Lee `a`: {λ} ⟶ {a} [λ→a]
- Lee `b`: {a} ⟶ {ab} [a→ab]
- Lee `a`: {ab} ⟶ {ab} [ab→ab]
- **Aceptada**: queda {ab} ∈ F.

## Cadena `abbbb`

- Inicio: {λ}
- Lee `a`: {λ} ⟶ {a} [λ→a]
- Lee `b`: {a} ⟶ {ab} [a→ab]
- Lee `b`: {ab} ⟶ {ab} [ab→ab]
- Lee `b`: {ab} ⟶ {ab} [ab→ab]
- Lee `b`: {ab} ⟶ {ab} [ab→ab]
- **Aceptada**: queda {ab} ∈ F.

## Cadena `abaaaaa`

- Inicio: {λ}
- Lee `a`: {λ} ⟶ {a} [λ→a]
- Lee `b`: {a} ⟶ {ab} [a→ab]
- Lee `a`: {ab} ⟶ {ab} [ab→ab]
- Lee `a`: {ab} ⟶ {ab} [ab→ab]
- Lee `a`: {ab} ⟶ {ab} [ab→ab]
- Lee `a`: {ab} ⟶ {ab} [ab→ab]
- Lee `a`: {ab} ⟶ {ab} [ab→ab]
- **Aceptada**: queda {ab} ∈ F.

## Cadena `abaaabaaab`

- Inicio: {λ}
- Lee `a`: {λ} ⟶ {a} [λ→a]
- Lee `b`: {a} ⟶ {ab} [a→ab]
- Lee `a`: {ab} ⟶ {ab} [ab→ab]
- Lee `a`: {ab} ⟶ {ab} [ab→ab]
- Lee `a`: {ab} ⟶ {ab} [ab→ab]
- Lee `b`: {ab} ⟶ {ab} [ab→ab]
- Lee `a`: {ab} ⟶ {ab} [ab→ab]
- Lee `a`: {ab} ⟶ {ab} [ab→ab]
- Lee `a`: {ab} ⟶ {ab} [ab→ab]
- Lee `b`: {ab} ⟶ {ab} [ab→ab]
- **Aceptada**: queda {ab} ∈ F.

## Cadena λ

- Inicio: {λ}
- **Rechazada**: ningún estado de {λ} es de aceptación.

## Cadena `b`

- Inicio: {λ}
- Lee `b`: {λ} ⟶ {muerto} [λ→muerto]
- **Rechazada**: ningún estado de {muerto} es de aceptación.

## Cadena `bab`

- Inicio: {λ}
- Lee `b`: {λ} ⟶ {muerto} [λ→muerto]
- Lee `a`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `b`: {muerto} ⟶ {muerto} [muerto→muerto]
- **Rechazada**: ningún estado de {muerto} es de aceptación.

## Cadena `bbbab`

- Inicio: {λ}
- Lee `b`: {λ} ⟶ {muerto} [λ→muerto]
- Lee `b`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `b`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `a`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `b`: {muerto} ⟶ {muerto} [muerto→muerto]
- **Rechazada**: ningún estado de {muerto} es de aceptación.

## Cadena `bbabaaba`

- Inicio: {λ}
- Lee `b`: {λ} ⟶ {muerto} [λ→muerto]
- Lee `b`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `a`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `b`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `a`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `a`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `b`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `a`: {muerto} ⟶ {muerto} [muerto→muerto]
- **Rechazada**: ningún estado de {muerto} es de aceptación.

## Cadena `a`

- Inicio: {λ}
- Lee `a`: {λ} ⟶ {a} [λ→a]
- **Rechazada**: ningún estado de {a} es de aceptación.
