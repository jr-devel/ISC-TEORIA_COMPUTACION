# Recorridos: Lista 2 · Ejercicio 144e

e) El conjunto de números enteros con signo.

Autómata: `lista2-144e` (AFD).

## Cadena `1`

- Inicio: {ini}
- Lee `1`: {ini} ⟶ {ok} [ini→ok]
- **Aceptada**: queda {ok} ∈ F.

## Cadena `46`

- Inicio: {ini}
- Lee `4`: {ini} ⟶ {ok} [ini→ok]
- Lee `6`: {ok} ⟶ {ok} [ok→ok]
- **Aceptada**: queda {ok} ∈ F.

## Cadena `8856`

- Inicio: {ini}
- Lee `8`: {ini} ⟶ {ok} [ini→ok]
- Lee `8`: {ok} ⟶ {ok} [ok→ok]
- Lee `5`: {ok} ⟶ {ok} [ok→ok]
- Lee `6`: {ok} ⟶ {ok} [ok→ok]
- **Aceptada**: queda {ok} ∈ F.

## Cadena `658332`

- Inicio: {ini}
- Lee `6`: {ini} ⟶ {ok} [ini→ok]
- Lee `5`: {ok} ⟶ {ok} [ok→ok]
- Lee `8`: {ok} ⟶ {ok} [ok→ok]
- Lee `3`: {ok} ⟶ {ok} [ok→ok]
- Lee `3`: {ok} ⟶ {ok} [ok→ok]
- Lee `2`: {ok} ⟶ {ok} [ok→ok]
- **Aceptada**: queda {ok} ∈ F.

## Cadena `509883324`

- Inicio: {ini}
- Lee `5`: {ini} ⟶ {ok} [ini→ok]
- Lee `0`: {ok} ⟶ {ok} [ok→ok]
- Lee `9`: {ok} ⟶ {ok} [ok→ok]
- Lee `8`: {ok} ⟶ {ok} [ok→ok]
- Lee `8`: {ok} ⟶ {ok} [ok→ok]
- Lee `3`: {ok} ⟶ {ok} [ok→ok]
- Lee `3`: {ok} ⟶ {ok} [ok→ok]
- Lee `2`: {ok} ⟶ {ok} [ok→ok]
- Lee `4`: {ok} ⟶ {ok} [ok→ok]
- **Aceptada**: queda {ok} ∈ F.

## Cadena λ

- Inicio: {ini}
- **Rechazada**: ningún estado de {ini} es de aceptación.

## Cadena `-`

- Inicio: {ini}
- Lee `-`: {ini} ⟶ {signo} [ini→signo]
- **Rechazada**: ningún estado de {signo} es de aceptación.

## Cadena `6-5`

- Inicio: {ini}
- Lee `6`: {ini} ⟶ {ok} [ini→ok]
- Lee `-`: {ok} ⟶ {muerto} [ok→muerto]
- Lee `5`: {muerto} ⟶ {muerto} [muerto→muerto]
- **Rechazada**: ningún estado de {muerto} es de aceptación.

## Cadena `33-++`

- Inicio: {ini}
- Lee `3`: {ini} ⟶ {ok} [ini→ok]
- Lee `3`: {ok} ⟶ {ok} [ok→ok]
- Lee `-`: {ok} ⟶ {muerto} [ok→muerto]
- Lee `+`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `+`: {muerto} ⟶ {muerto} [muerto→muerto]
- **Rechazada**: ningún estado de {muerto} es de aceptación.

## Cadena `21296+77`

- Inicio: {ini}
- Lee `2`: {ini} ⟶ {ok} [ini→ok]
- Lee `1`: {ok} ⟶ {ok} [ok→ok]
- Lee `2`: {ok} ⟶ {ok} [ok→ok]
- Lee `9`: {ok} ⟶ {ok} [ok→ok]
- Lee `6`: {ok} ⟶ {ok} [ok→ok]
- Lee `+`: {ok} ⟶ {muerto} [ok→muerto]
- Lee `7`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `7`: {muerto} ⟶ {muerto} [muerto→muerto]
- **Rechazada**: ningún estado de {muerto} es de aceptación.

## Cadena `0`

- Inicio: {ini}
- Lee `0`: {ini} ⟶ {cero} [ini→cero]
- **Aceptada**: queda {cero} ∈ F.
