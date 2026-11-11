# Recorridos: Lista 2 · Ejercicio 118

L = {w ∈ Σ3* : w = axabya, x, y ∈ Σ3*}.

Autómata: `lista2-118` (AFD).

## Cadena `aaba`

- Inicio: {ini}
- Lee `a`: {ini} ⟶ {a} [ini→a]
- Lee `a`: {a} ⟶ {a·a} [a→a·a]
- Lee `b`: {a·a} ⟶ {ab} [a·a→ab]
- Lee `a`: {ab} ⟶ {ab·a} [ab→ab·a]
- **Aceptada**: queda {ab·a} ∈ F.

## Cadena `aabba`

- Inicio: {ini}
- Lee `a`: {ini} ⟶ {a} [ini→a]
- Lee `a`: {a} ⟶ {a·a} [a→a·a]
- Lee `b`: {a·a} ⟶ {ab} [a·a→ab]
- Lee `b`: {ab} ⟶ {ab} [ab→ab]
- Lee `a`: {ab} ⟶ {ab·a} [ab→ab·a]
- **Aceptada**: queda {ab·a} ∈ F.

## Cadena `aabbaaa`

- Inicio: {ini}
- Lee `a`: {ini} ⟶ {a} [ini→a]
- Lee `a`: {a} ⟶ {a·a} [a→a·a]
- Lee `b`: {a·a} ⟶ {ab} [a·a→ab]
- Lee `b`: {ab} ⟶ {ab} [ab→ab]
- Lee `a`: {ab} ⟶ {ab·a} [ab→ab·a]
- Lee `a`: {ab·a} ⟶ {ab·a} [ab·a→ab·a]
- Lee `a`: {ab·a} ⟶ {ab·a} [ab·a→ab·a]
- **Aceptada**: queda {ab·a} ∈ F.

## Cadena `abbbaabba`

- Inicio: {ini}
- Lee `a`: {ini} ⟶ {a} [ini→a]
- Lee `b`: {a} ⟶ {a} [a→a]
- Lee `b`: {a} ⟶ {a} [a→a]
- Lee `b`: {a} ⟶ {a} [a→a]
- Lee `a`: {a} ⟶ {a·a} [a→a·a]
- Lee `a`: {a·a} ⟶ {a·a} [a·a→a·a]
- Lee `b`: {a·a} ⟶ {ab} [a·a→ab]
- Lee `b`: {ab} ⟶ {ab} [ab→ab]
- Lee `a`: {ab} ⟶ {ab·a} [ab→ab·a]
- **Aceptada**: queda {ab·a} ∈ F.

## Cadena `aabbbaabaaaa`

- Inicio: {ini}
- Lee `a`: {ini} ⟶ {a} [ini→a]
- Lee `a`: {a} ⟶ {a·a} [a→a·a]
- Lee `b`: {a·a} ⟶ {ab} [a·a→ab]
- Lee `b`: {ab} ⟶ {ab} [ab→ab]
- Lee `b`: {ab} ⟶ {ab} [ab→ab]
- Lee `a`: {ab} ⟶ {ab·a} [ab→ab·a]
- Lee `a`: {ab·a} ⟶ {ab·a} [ab·a→ab·a]
- Lee `b`: {ab·a} ⟶ {ab} [ab·a→ab]
- Lee `a`: {ab} ⟶ {ab·a} [ab→ab·a]
- Lee `a`: {ab·a} ⟶ {ab·a} [ab·a→ab·a]
- Lee `a`: {ab·a} ⟶ {ab·a} [ab·a→ab·a]
- Lee `a`: {ab·a} ⟶ {ab·a} [ab·a→ab·a]
- **Aceptada**: queda {ab·a} ∈ F.

## Cadena λ

- Inicio: {ini}
- **Rechazada**: ningún estado de {ini} es de aceptación.

## Cadena `a`

- Inicio: {ini}
- Lee `a`: {ini} ⟶ {a} [ini→a]
- **Rechazada**: ningún estado de {a} es de aceptación.

## Cadena `bbb`

- Inicio: {ini}
- Lee `b`: {ini} ⟶ {muerto} [ini→muerto]
- Lee `b`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `b`: {muerto} ⟶ {muerto} [muerto→muerto]
- **Rechazada**: ningún estado de {muerto} es de aceptación.

## Cadena `babbb`

- Inicio: {ini}
- Lee `b`: {ini} ⟶ {muerto} [ini→muerto]
- Lee `a`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `b`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `b`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `b`: {muerto} ⟶ {muerto} [muerto→muerto]
- **Rechazada**: ningún estado de {muerto} es de aceptación.

## Cadena `babaaabb`

- Inicio: {ini}
- Lee `b`: {ini} ⟶ {muerto} [ini→muerto]
- Lee `a`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `b`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `a`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `a`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `a`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `b`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `b`: {muerto} ⟶ {muerto} [muerto→muerto]
- **Rechazada**: ningún estado de {muerto} es de aceptación.

## Cadena `bab`

- Inicio: {ini}
- Lee `b`: {ini} ⟶ {muerto} [ini→muerto]
- Lee `a`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `b`: {muerto} ⟶ {muerto} [muerto→muerto]
- **Rechazada**: ningún estado de {muerto} es de aceptación.
