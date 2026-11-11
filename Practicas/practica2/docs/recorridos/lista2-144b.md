# Recorridos: Lista 2 · Ejercicio 144b

b) El conjunto de cadenas que comienzan con a y terminan con b.

Autómata: `lista2-144b` (AFD).

## Cadena `ab`

- Inicio: {ini}
- Lee `a`: {ini} ⟶ {a…} [ini→a…]
- Lee `b`: {a…} ⟶ {a…b} [a…→a…b]
- **Aceptada**: queda {a…b} ∈ F.

## Cadena `aab`

- Inicio: {ini}
- Lee `a`: {ini} ⟶ {a…} [ini→a…]
- Lee `a`: {a…} ⟶ {a…} [a…→a…]
- Lee `b`: {a…} ⟶ {a…b} [a…→a…b]
- **Aceptada**: queda {a…b} ∈ F.

## Cadena `aaaab`

- Inicio: {ini}
- Lee `a`: {ini} ⟶ {a…} [ini→a…]
- Lee `a`: {a…} ⟶ {a…} [a…→a…]
- Lee `a`: {a…} ⟶ {a…} [a…→a…]
- Lee `a`: {a…} ⟶ {a…} [a…→a…]
- Lee `b`: {a…} ⟶ {a…b} [a…→a…b]
- **Aceptada**: queda {a…b} ∈ F.

## Cadena `aaabaab`

- Inicio: {ini}
- Lee `a`: {ini} ⟶ {a…} [ini→a…]
- Lee `a`: {a…} ⟶ {a…} [a…→a…]
- Lee `a`: {a…} ⟶ {a…} [a…→a…]
- Lee `b`: {a…} ⟶ {a…b} [a…→a…b]
- Lee `a`: {a…b} ⟶ {a…} [a…b→a…]
- Lee `a`: {a…} ⟶ {a…} [a…→a…]
- Lee `b`: {a…} ⟶ {a…b} [a…→a…b]
- **Aceptada**: queda {a…b} ∈ F.

## Cadena `aaaaaaaaab`

- Inicio: {ini}
- Lee `a`: {ini} ⟶ {a…} [ini→a…]
- Lee `a`: {a…} ⟶ {a…} [a…→a…]
- Lee `a`: {a…} ⟶ {a…} [a…→a…]
- Lee `a`: {a…} ⟶ {a…} [a…→a…]
- Lee `a`: {a…} ⟶ {a…} [a…→a…]
- Lee `a`: {a…} ⟶ {a…} [a…→a…]
- Lee `a`: {a…} ⟶ {a…} [a…→a…]
- Lee `a`: {a…} ⟶ {a…} [a…→a…]
- Lee `a`: {a…} ⟶ {a…} [a…→a…]
- Lee `b`: {a…} ⟶ {a…b} [a…→a…b]
- **Aceptada**: queda {a…b} ∈ F.

## Cadena λ

- Inicio: {ini}
- **Rechazada**: ningún estado de {ini} es de aceptación.

## Cadena `a`

- Inicio: {ini}
- Lee `a`: {ini} ⟶ {a…} [ini→a…]
- **Rechazada**: ningún estado de {a…} es de aceptación.

## Cadena `aba`

- Inicio: {ini}
- Lee `a`: {ini} ⟶ {a…} [ini→a…]
- Lee `b`: {a…} ⟶ {a…b} [a…→a…b]
- Lee `a`: {a…b} ⟶ {a…} [a…b→a…]
- **Rechazada**: ningún estado de {a…} es de aceptación.

## Cadena `babba`

- Inicio: {ini}
- Lee `b`: {ini} ⟶ {muerto} [ini→muerto]
- Lee `a`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `b`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `b`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `a`: {muerto} ⟶ {muerto} [muerto→muerto]
- **Rechazada**: ningún estado de {muerto} es de aceptación.

## Cadena `aaabaaaa`

- Inicio: {ini}
- Lee `a`: {ini} ⟶ {a…} [ini→a…]
- Lee `a`: {a…} ⟶ {a…} [a…→a…]
- Lee `a`: {a…} ⟶ {a…} [a…→a…]
- Lee `b`: {a…} ⟶ {a…b} [a…→a…b]
- Lee `a`: {a…b} ⟶ {a…} [a…b→a…]
- Lee `a`: {a…} ⟶ {a…} [a…→a…]
- Lee `a`: {a…} ⟶ {a…} [a…→a…]
- Lee `a`: {a…} ⟶ {a…} [a…→a…]
- **Rechazada**: ningún estado de {a…} es de aceptación.

## Cadena `b`

- Inicio: {ini}
- Lee `b`: {ini} ⟶ {muerto} [ini→muerto]
- **Rechazada**: ningún estado de {muerto} es de aceptación.
