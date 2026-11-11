# Recorridos: Lista 2 · Ejercicio 114

L = {w ∈ Σ3* : w = aⁿbᵐ, m, n ∈ N}.

Autómata: `lista2-114` (AFD).

## Cadena λ

- Inicio: {a*}
- **Aceptada**: queda {a*} ∈ F.

## Cadena `a`

- Inicio: {a*}
- Lee `a`: {a*} ⟶ {a*} [a*→a*]
- **Aceptada**: queda {a*} ∈ F.

## Cadena `aaa`

- Inicio: {a*}
- Lee `a`: {a*} ⟶ {a*} [a*→a*]
- Lee `a`: {a*} ⟶ {a*} [a*→a*]
- Lee `a`: {a*} ⟶ {a*} [a*→a*]
- **Aceptada**: queda {a*} ∈ F.

## Cadena `abbbb`

- Inicio: {a*}
- Lee `a`: {a*} ⟶ {a*} [a*→a*]
- Lee `b`: {a*} ⟶ {a*b+} [a*→a*b+]
- Lee `b`: {a*b+} ⟶ {a*b+} [a*b+→a*b+]
- Lee `b`: {a*b+} ⟶ {a*b+} [a*b+→a*b+]
- Lee `b`: {a*b+} ⟶ {a*b+} [a*b+→a*b+]
- **Aceptada**: queda {a*b+} ∈ F.

## Cadena `aabbbbbb`

- Inicio: {a*}
- Lee `a`: {a*} ⟶ {a*} [a*→a*]
- Lee `a`: {a*} ⟶ {a*} [a*→a*]
- Lee `b`: {a*} ⟶ {a*b+} [a*→a*b+]
- Lee `b`: {a*b+} ⟶ {a*b+} [a*b+→a*b+]
- Lee `b`: {a*b+} ⟶ {a*b+} [a*b+→a*b+]
- Lee `b`: {a*b+} ⟶ {a*b+} [a*b+→a*b+]
- Lee `b`: {a*b+} ⟶ {a*b+} [a*b+→a*b+]
- Lee `b`: {a*b+} ⟶ {a*b+} [a*b+→a*b+]
- **Aceptada**: queda {a*b+} ∈ F.

## Cadena `ba`

- Inicio: {a*}
- Lee `b`: {a*} ⟶ {a*b+} [a*→a*b+]
- Lee `a`: {a*b+} ⟶ {muerto} [a*b+→muerto]
- **Rechazada**: ningún estado de {muerto} es de aceptación.

## Cadena `baa`

- Inicio: {a*}
- Lee `b`: {a*} ⟶ {a*b+} [a*→a*b+]
- Lee `a`: {a*b+} ⟶ {muerto} [a*b+→muerto]
- Lee `a`: {muerto} ⟶ {muerto} [muerto→muerto]
- **Rechazada**: ningún estado de {muerto} es de aceptación.

## Cadena `baaab`

- Inicio: {a*}
- Lee `b`: {a*} ⟶ {a*b+} [a*→a*b+]
- Lee `a`: {a*b+} ⟶ {muerto} [a*b+→muerto]
- Lee `a`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `a`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `b`: {muerto} ⟶ {muerto} [muerto→muerto]
- **Rechazada**: ningún estado de {muerto} es de aceptación.

## Cadena `bbaabbb`

- Inicio: {a*}
- Lee `b`: {a*} ⟶ {a*b+} [a*→a*b+]
- Lee `b`: {a*b+} ⟶ {a*b+} [a*b+→a*b+]
- Lee `a`: {a*b+} ⟶ {muerto} [a*b+→muerto]
- Lee `a`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `b`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `b`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `b`: {muerto} ⟶ {muerto} [muerto→muerto]
- **Rechazada**: ningún estado de {muerto} es de aceptación.

## Cadena `aaaababbab`

- Inicio: {a*}
- Lee `a`: {a*} ⟶ {a*} [a*→a*]
- Lee `a`: {a*} ⟶ {a*} [a*→a*]
- Lee `a`: {a*} ⟶ {a*} [a*→a*]
- Lee `a`: {a*} ⟶ {a*} [a*→a*]
- Lee `b`: {a*} ⟶ {a*b+} [a*→a*b+]
- Lee `a`: {a*b+} ⟶ {muerto} [a*b+→muerto]
- Lee `b`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `b`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `a`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `b`: {muerto} ⟶ {muerto} [muerto→muerto]
- **Rechazada**: ningún estado de {muerto} es de aceptación.
