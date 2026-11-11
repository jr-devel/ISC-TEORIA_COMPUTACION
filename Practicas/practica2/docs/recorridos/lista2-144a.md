# Recorridos: Lista 2 · Ejercicio 144a

a) El conjunto de cadenas sobre {a, b} que comienzan con a.

Autómata: `lista2-144a` (AFD).

## Cadena `a`

- Inicio: {λ}
- Lee `a`: {λ} ⟶ {a} [λ→a]
- **Aceptada**: queda {a} ∈ F.

## Cadena `aa`

- Inicio: {λ}
- Lee `a`: {λ} ⟶ {a} [λ→a]
- Lee `a`: {a} ⟶ {a} [a→a]
- **Aceptada**: queda {a} ∈ F.

## Cadena `abaa`

- Inicio: {λ}
- Lee `a`: {λ} ⟶ {a} [λ→a]
- Lee `b`: {a} ⟶ {a} [a→a]
- Lee `a`: {a} ⟶ {a} [a→a]
- Lee `a`: {a} ⟶ {a} [a→a]
- **Aceptada**: queda {a} ∈ F.

## Cadena `aaaaba`

- Inicio: {λ}
- Lee `a`: {λ} ⟶ {a} [λ→a]
- Lee `a`: {a} ⟶ {a} [a→a]
- Lee `a`: {a} ⟶ {a} [a→a]
- Lee `a`: {a} ⟶ {a} [a→a]
- Lee `b`: {a} ⟶ {a} [a→a]
- Lee `a`: {a} ⟶ {a} [a→a]
- **Aceptada**: queda {a} ∈ F.

## Cadena `aaaaaaabb`

- Inicio: {λ}
- Lee `a`: {λ} ⟶ {a} [λ→a]
- Lee `a`: {a} ⟶ {a} [a→a]
- Lee `a`: {a} ⟶ {a} [a→a]
- Lee `a`: {a} ⟶ {a} [a→a]
- Lee `a`: {a} ⟶ {a} [a→a]
- Lee `a`: {a} ⟶ {a} [a→a]
- Lee `a`: {a} ⟶ {a} [a→a]
- Lee `b`: {a} ⟶ {a} [a→a]
- Lee `b`: {a} ⟶ {a} [a→a]
- **Aceptada**: queda {a} ∈ F.

## Cadena λ

- Inicio: {λ}
- **Rechazada**: ningún estado de {λ} es de aceptación.

## Cadena `b`

- Inicio: {λ}
- Lee `b`: {λ} ⟶ {muerto} [λ→muerto]
- **Rechazada**: ningún estado de {muerto} es de aceptación.

## Cadena `bba`

- Inicio: {λ}
- Lee `b`: {λ} ⟶ {muerto} [λ→muerto]
- Lee `b`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `a`: {muerto} ⟶ {muerto} [muerto→muerto]
- **Rechazada**: ningún estado de {muerto} es de aceptación.

## Cadena `baaba`

- Inicio: {λ}
- Lee `b`: {λ} ⟶ {muerto} [λ→muerto]
- Lee `a`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `a`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `b`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `a`: {muerto} ⟶ {muerto} [muerto→muerto]
- **Rechazada**: ningún estado de {muerto} es de aceptación.

## Cadena `baaabbbb`

- Inicio: {λ}
- Lee `b`: {λ} ⟶ {muerto} [λ→muerto]
- Lee `a`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `a`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `a`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `b`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `b`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `b`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `b`: {muerto} ⟶ {muerto} [muerto→muerto]
- **Rechazada**: ningún estado de {muerto} es de aceptación.
