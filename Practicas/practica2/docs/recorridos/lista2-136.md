# Recorridos: Lista 2 · Ejercicio 136

Dado Σ = {a, b}, AFD para L = {aᵐbⁿ : m, n > 0}.

Autómata: `lista2-136` (AFD).

## Cadena `ab`

- Inicio: {ini}
- Lee `a`: {ini} ⟶ {a+} [ini→a+]
- Lee `b`: {a+} ⟶ {a+b+} [a+→a+b+]
- **Aceptada**: queda {a+b+} ∈ F.

## Cadena `aab`

- Inicio: {ini}
- Lee `a`: {ini} ⟶ {a+} [ini→a+]
- Lee `a`: {a+} ⟶ {a+} [a+→a+]
- Lee `b`: {a+} ⟶ {a+b+} [a+→a+b+]
- **Aceptada**: queda {a+b+} ∈ F.

## Cadena `aaabb`

- Inicio: {ini}
- Lee `a`: {ini} ⟶ {a+} [ini→a+]
- Lee `a`: {a+} ⟶ {a+} [a+→a+]
- Lee `a`: {a+} ⟶ {a+} [a+→a+]
- Lee `b`: {a+} ⟶ {a+b+} [a+→a+b+]
- Lee `b`: {a+b+} ⟶ {a+b+} [a+b+→a+b+]
- **Aceptada**: queda {a+b+} ∈ F.

## Cadena `aaaaabb`

- Inicio: {ini}
- Lee `a`: {ini} ⟶ {a+} [ini→a+]
- Lee `a`: {a+} ⟶ {a+} [a+→a+]
- Lee `a`: {a+} ⟶ {a+} [a+→a+]
- Lee `a`: {a+} ⟶ {a+} [a+→a+]
- Lee `a`: {a+} ⟶ {a+} [a+→a+]
- Lee `b`: {a+} ⟶ {a+b+} [a+→a+b+]
- Lee `b`: {a+b+} ⟶ {a+b+} [a+b+→a+b+]
- **Aceptada**: queda {a+b+} ∈ F.

## Cadena `aaaaaaabbb`

- Inicio: {ini}
- Lee `a`: {ini} ⟶ {a+} [ini→a+]
- Lee `a`: {a+} ⟶ {a+} [a+→a+]
- Lee `a`: {a+} ⟶ {a+} [a+→a+]
- Lee `a`: {a+} ⟶ {a+} [a+→a+]
- Lee `a`: {a+} ⟶ {a+} [a+→a+]
- Lee `a`: {a+} ⟶ {a+} [a+→a+]
- Lee `a`: {a+} ⟶ {a+} [a+→a+]
- Lee `b`: {a+} ⟶ {a+b+} [a+→a+b+]
- Lee `b`: {a+b+} ⟶ {a+b+} [a+b+→a+b+]
- Lee `b`: {a+b+} ⟶ {a+b+} [a+b+→a+b+]
- **Aceptada**: queda {a+b+} ∈ F.

## Cadena λ

- Inicio: {ini}
- **Rechazada**: ningún estado de {ini} es de aceptación.

## Cadena `a`

- Inicio: {ini}
- Lee `a`: {ini} ⟶ {a+} [ini→a+]
- **Rechazada**: ningún estado de {a+} es de aceptación.

## Cadena `bbb`

- Inicio: {ini}
- Lee `b`: {ini} ⟶ {muerto} [ini→muerto]
- Lee `b`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `b`: {muerto} ⟶ {muerto} [muerto→muerto]
- **Rechazada**: ningún estado de {muerto} es de aceptación.

## Cadena `babaa`

- Inicio: {ini}
- Lee `b`: {ini} ⟶ {muerto} [ini→muerto]
- Lee `a`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `b`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `a`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `a`: {muerto} ⟶ {muerto} [muerto→muerto]
- **Rechazada**: ningún estado de {muerto} es de aceptación.

## Cadena `bbbabbba`

- Inicio: {ini}
- Lee `b`: {ini} ⟶ {muerto} [ini→muerto]
- Lee `b`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `b`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `a`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `b`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `b`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `b`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `a`: {muerto} ⟶ {muerto} [muerto→muerto]
- **Rechazada**: ningún estado de {muerto} es de aceptación.

## Cadena `b`

- Inicio: {ini}
- Lee `b`: {ini} ⟶ {muerto} [ini→muerto]
- **Rechazada**: ningún estado de {muerto} es de aceptación.
