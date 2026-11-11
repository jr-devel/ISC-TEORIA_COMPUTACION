# Recorridos: Lista 2 · Ejercicio 141

L = {w ∈ {0, 1}* : cada 0 en w tiene un 1 inmediatamente a su derecha}.

Autómata: `lista2-141` (AFD).

## Cadena λ

- Inicio: {ok}
- **Aceptada**: queda {ok} ∈ F.

## Cadena `1`

- Inicio: {ok}
- Lee `1`: {ok} ⟶ {ok} [ok→ok]
- **Aceptada**: queda {ok} ∈ F.

## Cadena `111`

- Inicio: {ok}
- Lee `1`: {ok} ⟶ {ok} [ok→ok]
- Lee `1`: {ok} ⟶ {ok} [ok→ok]
- Lee `1`: {ok} ⟶ {ok} [ok→ok]
- **Aceptada**: queda {ok} ∈ F.

## Cadena `11111`

- Inicio: {ok}
- Lee `1`: {ok} ⟶ {ok} [ok→ok]
- Lee `1`: {ok} ⟶ {ok} [ok→ok]
- Lee `1`: {ok} ⟶ {ok} [ok→ok]
- Lee `1`: {ok} ⟶ {ok} [ok→ok]
- Lee `1`: {ok} ⟶ {ok} [ok→ok]
- **Aceptada**: queda {ok} ∈ F.

## Cadena `01110111`

- Inicio: {ok}
- Lee `0`: {ok} ⟶ {0?} [ok→0?]
- Lee `1`: {0?} ⟶ {ok} [0?→ok]
- Lee `1`: {ok} ⟶ {ok} [ok→ok]
- Lee `1`: {ok} ⟶ {ok} [ok→ok]
- Lee `0`: {ok} ⟶ {0?} [ok→0?]
- Lee `1`: {0?} ⟶ {ok} [0?→ok]
- Lee `1`: {ok} ⟶ {ok} [ok→ok]
- Lee `1`: {ok} ⟶ {ok} [ok→ok]
- **Aceptada**: queda {ok} ∈ F.

## Cadena `0`

- Inicio: {ok}
- Lee `0`: {ok} ⟶ {0?} [ok→0?]
- **Rechazada**: ningún estado de {0?} es de aceptación.

## Cadena `00`

- Inicio: {ok}
- Lee `0`: {ok} ⟶ {0?} [ok→0?]
- Lee `0`: {0?} ⟶ {muerto} [0?→muerto]
- **Rechazada**: ningún estado de {muerto} es de aceptación.

## Cadena `0100`

- Inicio: {ok}
- Lee `0`: {ok} ⟶ {0?} [ok→0?]
- Lee `1`: {0?} ⟶ {ok} [0?→ok]
- Lee `0`: {ok} ⟶ {0?} [ok→0?]
- Lee `0`: {0?} ⟶ {muerto} [0?→muerto]
- **Rechazada**: ningún estado de {muerto} es de aceptación.

## Cadena `101001`

- Inicio: {ok}
- Lee `1`: {ok} ⟶ {ok} [ok→ok]
- Lee `0`: {ok} ⟶ {0?} [ok→0?]
- Lee `1`: {0?} ⟶ {ok} [0?→ok]
- Lee `0`: {ok} ⟶ {0?} [ok→0?]
- Lee `0`: {0?} ⟶ {muerto} [0?→muerto]
- Lee `1`: {muerto} ⟶ {muerto} [muerto→muerto]
- **Rechazada**: ningún estado de {muerto} es de aceptación.

## Cadena `110010110`

- Inicio: {ok}
- Lee `1`: {ok} ⟶ {ok} [ok→ok]
- Lee `1`: {ok} ⟶ {ok} [ok→ok]
- Lee `0`: {ok} ⟶ {0?} [ok→0?]
- Lee `0`: {0?} ⟶ {muerto} [0?→muerto]
- Lee `1`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `0`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `1`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `1`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `0`: {muerto} ⟶ {muerto} [muerto→muerto]
- **Rechazada**: ningún estado de {muerto} es de aceptación.
