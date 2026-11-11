# Recorridos: Lista 2 · Ejercicio 144d

d) El conjunto de números enteros (sin signo).

Autómata: `lista2-144d` (AFD).

## Cadena `8`

- Inicio: {ini}
- Lee `8`: {ini} ⟶ {ok} [ini→ok]
- **Aceptada**: queda {ok} ∈ F.

## Cadena `43`

- Inicio: {ini}
- Lee `4`: {ini} ⟶ {ok} [ini→ok]
- Lee `3`: {ok} ⟶ {ok} [ok→ok]
- **Aceptada**: queda {ok} ∈ F.

## Cadena `2415`

- Inicio: {ini}
- Lee `2`: {ini} ⟶ {ok} [ini→ok]
- Lee `4`: {ok} ⟶ {ok} [ok→ok]
- Lee `1`: {ok} ⟶ {ok} [ok→ok]
- Lee `5`: {ok} ⟶ {ok} [ok→ok]
- **Aceptada**: queda {ok} ∈ F.

## Cadena `117250`

- Inicio: {ini}
- Lee `1`: {ini} ⟶ {ok} [ini→ok]
- Lee `1`: {ok} ⟶ {ok} [ok→ok]
- Lee `7`: {ok} ⟶ {ok} [ok→ok]
- Lee `2`: {ok} ⟶ {ok} [ok→ok]
- Lee `5`: {ok} ⟶ {ok} [ok→ok]
- Lee `0`: {ok} ⟶ {ok} [ok→ok]
- **Aceptada**: queda {ok} ∈ F.

## Cadena `438013017`

- Inicio: {ini}
- Lee `4`: {ini} ⟶ {ok} [ini→ok]
- Lee `3`: {ok} ⟶ {ok} [ok→ok]
- Lee `8`: {ok} ⟶ {ok} [ok→ok]
- Lee `0`: {ok} ⟶ {ok} [ok→ok]
- Lee `1`: {ok} ⟶ {ok} [ok→ok]
- Lee `3`: {ok} ⟶ {ok} [ok→ok]
- Lee `0`: {ok} ⟶ {ok} [ok→ok]
- Lee `1`: {ok} ⟶ {ok} [ok→ok]
- Lee `7`: {ok} ⟶ {ok} [ok→ok]
- **Aceptada**: queda {ok} ∈ F.

## Cadena λ

- Inicio: {ini}
- **Rechazada**: ningún estado de {ini} es de aceptación.

## Cadena `0800`

- Inicio: {ini}
- Lee `0`: {ini} ⟶ {cero} [ini→cero]
- Lee `8`: {cero} ⟶ {muerto} [cero→muerto]
- Lee `0`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `0`: {muerto} ⟶ {muerto} [muerto→muerto]
- **Rechazada**: ningún estado de {muerto} es de aceptación.

## Cadena `001388`

- Inicio: {ini}
- Lee `0`: {ini} ⟶ {cero} [ini→cero]
- Lee `0`: {cero} ⟶ {muerto} [cero→muerto]
- Lee `1`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `3`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `8`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `8`: {muerto} ⟶ {muerto} [muerto→muerto]
- **Rechazada**: ningún estado de {muerto} es de aceptación.

## Cadena `0883244971`

- Inicio: {ini}
- Lee `0`: {ini} ⟶ {cero} [ini→cero]
- Lee `8`: {cero} ⟶ {muerto} [cero→muerto]
- Lee `8`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `3`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `2`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `4`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `4`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `9`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `7`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `1`: {muerto} ⟶ {muerto} [muerto→muerto]
- **Rechazada**: ningún estado de {muerto} es de aceptación.

## Cadena `09967547184791`

- Inicio: {ini}
- Lee `0`: {ini} ⟶ {cero} [ini→cero]
- Lee `9`: {cero} ⟶ {muerto} [cero→muerto]
- Lee `9`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `6`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `7`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `5`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `4`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `7`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `1`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `8`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `4`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `7`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `9`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `1`: {muerto} ⟶ {muerto} [muerto→muerto]
- **Rechazada**: ningún estado de {muerto} es de aceptación.

## Cadena `2`

- Inicio: {ini}
- Lee `2`: {ini} ⟶ {ok} [ini→ok]
- **Aceptada**: queda {ok} ∈ F.
