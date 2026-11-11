# Recorridos: Lista 2 · Ejercicio 100

Las palabras de Σ2 tales que el primer símbolo es una letra y el segundo es un dígito.

Autómata: `lista2-100` (AFD).

## Cadena `a1`

- Inicio: {ini}
- Lee `a`: {ini} ⟶ {letra} [ini→letra]
- Lee `1`: {letra} ⟶ {ok} [letra→ok]
- **Aceptada**: queda {ok} ∈ F.

## Cadena `b1b`

- Inicio: {ini}
- Lee `b`: {ini} ⟶ {letra} [ini→letra]
- Lee `1`: {letra} ⟶ {ok} [letra→ok]
- Lee `b`: {ok} ⟶ {ok} [ok→ok]
- **Aceptada**: queda {ok} ∈ F.

## Cadena `c0aa0`

- Inicio: {ini}
- Lee `c`: {ini} ⟶ {letra} [ini→letra]
- Lee `0`: {letra} ⟶ {ok} [letra→ok]
- Lee `a`: {ok} ⟶ {ok} [ok→ok]
- Lee `a`: {ok} ⟶ {ok} [ok→ok]
- Lee `0`: {ok} ⟶ {ok} [ok→ok]
- **Aceptada**: queda {ok} ∈ F.

## Cadena `b00c1ac`

- Inicio: {ini}
- Lee `b`: {ini} ⟶ {letra} [ini→letra]
- Lee `0`: {letra} ⟶ {ok} [letra→ok]
- Lee `0`: {ok} ⟶ {ok} [ok→ok]
- Lee `c`: {ok} ⟶ {ok} [ok→ok]
- Lee `1`: {ok} ⟶ {ok} [ok→ok]
- Lee `a`: {ok} ⟶ {ok} [ok→ok]
- Lee `c`: {ok} ⟶ {ok} [ok→ok]
- **Aceptada**: queda {ok} ∈ F.

## Cadena `b1bb11cbb0`

- Inicio: {ini}
- Lee `b`: {ini} ⟶ {letra} [ini→letra]
- Lee `1`: {letra} ⟶ {ok} [letra→ok]
- Lee `b`: {ok} ⟶ {ok} [ok→ok]
- Lee `b`: {ok} ⟶ {ok} [ok→ok]
- Lee `1`: {ok} ⟶ {ok} [ok→ok]
- Lee `1`: {ok} ⟶ {ok} [ok→ok]
- Lee `c`: {ok} ⟶ {ok} [ok→ok]
- Lee `b`: {ok} ⟶ {ok} [ok→ok]
- Lee `b`: {ok} ⟶ {ok} [ok→ok]
- Lee `0`: {ok} ⟶ {ok} [ok→ok]
- **Aceptada**: queda {ok} ∈ F.

## Cadena λ

- Inicio: {ini}
- **Rechazada**: ningún estado de {ini} es de aceptación.

## Cadena `b`

- Inicio: {ini}
- Lee `b`: {ini} ⟶ {letra} [ini→letra]
- **Rechazada**: ningún estado de {letra} es de aceptación.

## Cadena `0a0`

- Inicio: {ini}
- Lee `0`: {ini} ⟶ {muerto} [ini→muerto]
- Lee `a`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `0`: {muerto} ⟶ {muerto} [muerto→muerto]
- **Rechazada**: ningún estado de {muerto} es de aceptación.

## Cadena `1ac0a`

- Inicio: {ini}
- Lee `1`: {ini} ⟶ {muerto} [ini→muerto]
- Lee `a`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `c`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `0`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `a`: {muerto} ⟶ {muerto} [muerto→muerto]
- **Rechazada**: ningún estado de {muerto} es de aceptación.

## Cadena `0ca00ba0`

- Inicio: {ini}
- Lee `0`: {ini} ⟶ {muerto} [ini→muerto]
- Lee `c`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `a`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `0`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `0`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `b`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `a`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `0`: {muerto} ⟶ {muerto} [muerto→muerto]
- **Rechazada**: ningún estado de {muerto} es de aceptación.

## Cadena `b1`

- Inicio: {ini}
- Lee `b`: {ini} ⟶ {letra} [ini→letra]
- Lee `1`: {letra} ⟶ {ok} [letra→ok]
- **Aceptada**: queda {ok} ∈ F.

## Cadena `1`

- Inicio: {ini}
- Lee `1`: {ini} ⟶ {muerto} [ini→muerto]
- **Rechazada**: ningún estado de {muerto} es de aceptación.
