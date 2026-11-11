# Recorridos: Lista 2 · Ejercicio 132

Diseñar un AFD para L = {aⁿb : n ≥ 0}.

Autómata: `lista2-132` (AFD).

## Cadena `b`

- Inicio: {a*}
- Lee `b`: {a*} ⟶ {a*b} [a*→a*b]
- **Aceptada**: queda {a*b} ∈ F.

## Cadena `ab`

- Inicio: {a*}
- Lee `a`: {a*} ⟶ {a*} [a*→a*]
- Lee `b`: {a*} ⟶ {a*b} [a*→a*b]
- **Aceptada**: queda {a*b} ∈ F.

## Cadena `aaab`

- Inicio: {a*}
- Lee `a`: {a*} ⟶ {a*} [a*→a*]
- Lee `a`: {a*} ⟶ {a*} [a*→a*]
- Lee `a`: {a*} ⟶ {a*} [a*→a*]
- Lee `b`: {a*} ⟶ {a*b} [a*→a*b]
- **Aceptada**: queda {a*b} ∈ F.

## Cadena `aaaaab`

- Inicio: {a*}
- Lee `a`: {a*} ⟶ {a*} [a*→a*]
- Lee `a`: {a*} ⟶ {a*} [a*→a*]
- Lee `a`: {a*} ⟶ {a*} [a*→a*]
- Lee `a`: {a*} ⟶ {a*} [a*→a*]
- Lee `a`: {a*} ⟶ {a*} [a*→a*]
- Lee `b`: {a*} ⟶ {a*b} [a*→a*b]
- **Aceptada**: queda {a*b} ∈ F.

## Cadena `aaaaaaaab`

- Inicio: {a*}
- Lee `a`: {a*} ⟶ {a*} [a*→a*]
- Lee `a`: {a*} ⟶ {a*} [a*→a*]
- Lee `a`: {a*} ⟶ {a*} [a*→a*]
- Lee `a`: {a*} ⟶ {a*} [a*→a*]
- Lee `a`: {a*} ⟶ {a*} [a*→a*]
- Lee `a`: {a*} ⟶ {a*} [a*→a*]
- Lee `a`: {a*} ⟶ {a*} [a*→a*]
- Lee `a`: {a*} ⟶ {a*} [a*→a*]
- Lee `b`: {a*} ⟶ {a*b} [a*→a*b]
- **Aceptada**: queda {a*b} ∈ F.

## Cadena λ

- Inicio: {a*}
- **Rechazada**: ningún estado de {a*} es de aceptación.

## Cadena `a`

- Inicio: {a*}
- Lee `a`: {a*} ⟶ {a*} [a*→a*]
- **Rechazada**: ningún estado de {a*} es de aceptación.

## Cadena `bba`

- Inicio: {a*}
- Lee `b`: {a*} ⟶ {a*b} [a*→a*b]
- Lee `b`: {a*b} ⟶ {muerto} [a*b→muerto]
- Lee `a`: {muerto} ⟶ {muerto} [muerto→muerto]
- **Rechazada**: ningún estado de {muerto} es de aceptación.

## Cadena `bbbba`

- Inicio: {a*}
- Lee `b`: {a*} ⟶ {a*b} [a*→a*b]
- Lee `b`: {a*b} ⟶ {muerto} [a*b→muerto]
- Lee `b`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `b`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `a`: {muerto} ⟶ {muerto} [muerto→muerto]
- **Rechazada**: ningún estado de {muerto} es de aceptación.

## Cadena `bbaababa`

- Inicio: {a*}
- Lee `b`: {a*} ⟶ {a*b} [a*→a*b]
- Lee `b`: {a*b} ⟶ {muerto} [a*b→muerto]
- Lee `a`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `a`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `b`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `a`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `b`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `a`: {muerto} ⟶ {muerto} [muerto→muerto]
- **Rechazada**: ningún estado de {muerto} es de aceptación.
