# Recorridos: Lista 2 · Ejercicio 142b

b) LB = {(ab)ⁿ : n ≥ 1}.

Autómata: `lista2-142b` (AFD).

## Cadena `ab`

- Inicio: {ini}
- Lee `a`: {ini} ⟶ {…a} [ini→…a]
- Lee `b`: {…a} ⟶ {…ab} […a→…ab]
- **Aceptada**: queda {…ab} ∈ F.

## Cadena `abab`

- Inicio: {ini}
- Lee `a`: {ini} ⟶ {…a} [ini→…a]
- Lee `b`: {…a} ⟶ {…ab} […a→…ab]
- Lee `a`: {…ab} ⟶ {…a} […ab→…a]
- Lee `b`: {…a} ⟶ {…ab} […a→…ab]
- **Aceptada**: queda {…ab} ∈ F.

## Cadena `ababab`

- Inicio: {ini}
- Lee `a`: {ini} ⟶ {…a} [ini→…a]
- Lee `b`: {…a} ⟶ {…ab} […a→…ab]
- Lee `a`: {…ab} ⟶ {…a} […ab→…a]
- Lee `b`: {…a} ⟶ {…ab} […a→…ab]
- Lee `a`: {…ab} ⟶ {…a} […ab→…a]
- Lee `b`: {…a} ⟶ {…ab} […a→…ab]
- **Aceptada**: queda {…ab} ∈ F.

## Cadena `abababab`

- Inicio: {ini}
- Lee `a`: {ini} ⟶ {…a} [ini→…a]
- Lee `b`: {…a} ⟶ {…ab} […a→…ab]
- Lee `a`: {…ab} ⟶ {…a} […ab→…a]
- Lee `b`: {…a} ⟶ {…ab} […a→…ab]
- Lee `a`: {…ab} ⟶ {…a} […ab→…a]
- Lee `b`: {…a} ⟶ {…ab} […a→…ab]
- Lee `a`: {…ab} ⟶ {…a} […ab→…a]
- Lee `b`: {…a} ⟶ {…ab} […a→…ab]
- **Aceptada**: queda {…ab} ∈ F.

## Cadena `abababababab`

- Inicio: {ini}
- Lee `a`: {ini} ⟶ {…a} [ini→…a]
- Lee `b`: {…a} ⟶ {…ab} […a→…ab]
- Lee `a`: {…ab} ⟶ {…a} […ab→…a]
- Lee `b`: {…a} ⟶ {…ab} […a→…ab]
- Lee `a`: {…ab} ⟶ {…a} […ab→…a]
- Lee `b`: {…a} ⟶ {…ab} […a→…ab]
- Lee `a`: {…ab} ⟶ {…a} […ab→…a]
- Lee `b`: {…a} ⟶ {…ab} […a→…ab]
- Lee `a`: {…ab} ⟶ {…a} […ab→…a]
- Lee `b`: {…a} ⟶ {…ab} […a→…ab]
- Lee `a`: {…ab} ⟶ {…a} […ab→…a]
- Lee `b`: {…a} ⟶ {…ab} […a→…ab]
- **Aceptada**: queda {…ab} ∈ F.

## Cadena λ

- Inicio: {ini}
- **Rechazada**: ningún estado de {ini} es de aceptación.

## Cadena `a`

- Inicio: {ini}
- Lee `a`: {ini} ⟶ {…a} [ini→…a]
- **Rechazada**: ningún estado de {…a} es de aceptación.

## Cadena `aba`

- Inicio: {ini}
- Lee `a`: {ini} ⟶ {…a} [ini→…a]
- Lee `b`: {…a} ⟶ {…ab} […a→…ab]
- Lee `a`: {…ab} ⟶ {…a} […ab→…a]
- **Rechazada**: ningún estado de {…a} es de aceptación.

## Cadena `aabaa`

- Inicio: {ini}
- Lee `a`: {ini} ⟶ {…a} [ini→…a]
- Lee `a`: {…a} ⟶ {muerto} […a→muerto]
- Lee `b`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `a`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `a`: {muerto} ⟶ {muerto} [muerto→muerto]
- **Rechazada**: ningún estado de {muerto} es de aceptación.

## Cadena `bbbbabab`

- Inicio: {ini}
- Lee `b`: {ini} ⟶ {muerto} [ini→muerto]
- Lee `b`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `b`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `b`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `a`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `b`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `a`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `b`: {muerto} ⟶ {muerto} [muerto→muerto]
- **Rechazada**: ningún estado de {muerto} es de aceptación.

## Cadena `b`

- Inicio: {ini}
- Lee `b`: {ini} ⟶ {muerto} [ini→muerto]
- **Rechazada**: ningún estado de {muerto} es de aceptación.
