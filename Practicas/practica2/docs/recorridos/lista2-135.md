# Recorridos: Lista 2 · Ejercicio 135

Dado Σ = {a, b}, AFD para L = {bᵐabⁿ : m, n > 0}.

Autómata: `lista2-135` (AFD).

## Cadena `bab`

- Inicio: {ini}
- Lee `b`: {ini} ⟶ {b+} [ini→b+]
- Lee `a`: {b+} ⟶ {b+a} [b+→b+a]
- Lee `b`: {b+a} ⟶ {b+ab+} [b+a→b+ab+]
- **Aceptada**: queda {b+ab+} ∈ F.

## Cadena `babb`

- Inicio: {ini}
- Lee `b`: {ini} ⟶ {b+} [ini→b+]
- Lee `a`: {b+} ⟶ {b+a} [b+→b+a]
- Lee `b`: {b+a} ⟶ {b+ab+} [b+a→b+ab+]
- Lee `b`: {b+ab+} ⟶ {b+ab+} [b+ab+→b+ab+]
- **Aceptada**: queda {b+ab+} ∈ F.

## Cadena `bbbbab`

- Inicio: {ini}
- Lee `b`: {ini} ⟶ {b+} [ini→b+]
- Lee `b`: {b+} ⟶ {b+} [b+→b+]
- Lee `b`: {b+} ⟶ {b+} [b+→b+]
- Lee `b`: {b+} ⟶ {b+} [b+→b+]
- Lee `a`: {b+} ⟶ {b+a} [b+→b+a]
- Lee `b`: {b+a} ⟶ {b+ab+} [b+a→b+ab+]
- **Aceptada**: queda {b+ab+} ∈ F.

## Cadena `bbabbbbb`

- Inicio: {ini}
- Lee `b`: {ini} ⟶ {b+} [ini→b+]
- Lee `b`: {b+} ⟶ {b+} [b+→b+]
- Lee `a`: {b+} ⟶ {b+a} [b+→b+a]
- Lee `b`: {b+a} ⟶ {b+ab+} [b+a→b+ab+]
- Lee `b`: {b+ab+} ⟶ {b+ab+} [b+ab+→b+ab+]
- Lee `b`: {b+ab+} ⟶ {b+ab+} [b+ab+→b+ab+]
- Lee `b`: {b+ab+} ⟶ {b+ab+} [b+ab+→b+ab+]
- Lee `b`: {b+ab+} ⟶ {b+ab+} [b+ab+→b+ab+]
- **Aceptada**: queda {b+ab+} ∈ F.

## Cadena `bbbabbbbbbb`

- Inicio: {ini}
- Lee `b`: {ini} ⟶ {b+} [ini→b+]
- Lee `b`: {b+} ⟶ {b+} [b+→b+]
- Lee `b`: {b+} ⟶ {b+} [b+→b+]
- Lee `a`: {b+} ⟶ {b+a} [b+→b+a]
- Lee `b`: {b+a} ⟶ {b+ab+} [b+a→b+ab+]
- Lee `b`: {b+ab+} ⟶ {b+ab+} [b+ab+→b+ab+]
- Lee `b`: {b+ab+} ⟶ {b+ab+} [b+ab+→b+ab+]
- Lee `b`: {b+ab+} ⟶ {b+ab+} [b+ab+→b+ab+]
- Lee `b`: {b+ab+} ⟶ {b+ab+} [b+ab+→b+ab+]
- Lee `b`: {b+ab+} ⟶ {b+ab+} [b+ab+→b+ab+]
- Lee `b`: {b+ab+} ⟶ {b+ab+} [b+ab+→b+ab+]
- **Aceptada**: queda {b+ab+} ∈ F.

## Cadena λ

- Inicio: {ini}
- **Rechazada**: ningún estado de {ini} es de aceptación.

## Cadena `b`

- Inicio: {ini}
- Lee `b`: {ini} ⟶ {b+} [ini→b+]
- **Rechazada**: ningún estado de {b+} es de aceptación.

## Cadena `bba`

- Inicio: {ini}
- Lee `b`: {ini} ⟶ {b+} [ini→b+]
- Lee `b`: {b+} ⟶ {b+} [b+→b+]
- Lee `a`: {b+} ⟶ {b+a} [b+→b+a]
- **Rechazada**: ningún estado de {b+a} es de aceptación.

## Cadena `aabbb`

- Inicio: {ini}
- Lee `a`: {ini} ⟶ {muerto} [ini→muerto]
- Lee `a`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `b`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `b`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `b`: {muerto} ⟶ {muerto} [muerto→muerto]
- **Rechazada**: ningún estado de {muerto} es de aceptación.

## Cadena `abbaaaba`

- Inicio: {ini}
- Lee `a`: {ini} ⟶ {muerto} [ini→muerto]
- Lee `b`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `b`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `a`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `a`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `a`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `b`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `a`: {muerto} ⟶ {muerto} [muerto→muerto]
- **Rechazada**: ningún estado de {muerto} es de aceptación.

## Cadena `aa`

- Inicio: {ini}
- Lee `a`: {ini} ⟶ {muerto} [ini→muerto]
- Lee `a`: {muerto} ⟶ {muerto} [muerto→muerto]
- **Rechazada**: ningún estado de {muerto} es de aceptación.
