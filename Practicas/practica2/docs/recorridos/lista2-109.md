# Recorridos: Lista 2 · Ejercicio 109

Las palabras de Σ2 que incluyen abbcb y cbaabb, que sí se pueden traslapar.

Autómata: `lista2-109` (AFD).

## Cadena `cbaabbcb`

- Inicio: {(λ, λ)}
- Lee `c`: {(λ, λ)} ⟶ {(λ, c)} [(λ, λ)→(λ, c)]
- Lee `b`: {(λ, c)} ⟶ {(λ, cb)} [(λ, c)→(λ, cb)]
- Lee `a`: {(λ, cb)} ⟶ {(a, cba)} [(λ, cb)→(a, cba)]
- Lee `a`: {(a, cba)} ⟶ {(a, cbaa)} [(a, cba)→(a, cbaa)]
- Lee `b`: {(a, cbaa)} ⟶ {(ab, cbaab)} [(a, cbaa)→(ab, cbaab)]
- Lee `b`: {(ab, cbaab)} ⟶ {(abb, cbaabb)} [(ab, cbaab)→(abb, cbaabb)]
- Lee `c`: {(abb, cbaabb)} ⟶ {(abbc, cbaabb)} [(abb, cbaabb)→(abbc, cbaabb)]
- Lee `b`: {(abbc, cbaabb)} ⟶ {(abbcb, cbaabb)} [(abbc, cbaabb)→(abbcb, cbaabb)]
- **Aceptada**: queda {(abbcb, cbaabb)} ∈ F.

## Cadena `0cbaabbcb`

- Inicio: {(λ, λ)}
- Lee `0`: {(λ, λ)} ⟶ {(λ, λ)} [(λ, λ)→(λ, λ)]
- Lee `c`: {(λ, λ)} ⟶ {(λ, c)} [(λ, λ)→(λ, c)]
- Lee `b`: {(λ, c)} ⟶ {(λ, cb)} [(λ, c)→(λ, cb)]
- Lee `a`: {(λ, cb)} ⟶ {(a, cba)} [(λ, cb)→(a, cba)]
- Lee `a`: {(a, cba)} ⟶ {(a, cbaa)} [(a, cba)→(a, cbaa)]
- Lee `b`: {(a, cbaa)} ⟶ {(ab, cbaab)} [(a, cbaa)→(ab, cbaab)]
- Lee `b`: {(ab, cbaab)} ⟶ {(abb, cbaabb)} [(ab, cbaab)→(abb, cbaabb)]
- Lee `c`: {(abb, cbaabb)} ⟶ {(abbc, cbaabb)} [(abb, cbaabb)→(abbc, cbaabb)]
- Lee `b`: {(abbc, cbaabb)} ⟶ {(abbcb, cbaabb)} [(abbc, cbaabb)→(abbcb, cbaabb)]
- **Aceptada**: queda {(abbcb, cbaabb)} ∈ F.

## Cadena `acacbaabbcb`

- Inicio: {(λ, λ)}
- Lee `a`: {(λ, λ)} ⟶ {(a, λ)} [(λ, λ)→(a, λ)]
- Lee `c`: {(a, λ)} ⟶ {(λ, c)} [(a, λ)→(λ, c)]
- Lee `a`: {(λ, c)} ⟶ {(a, λ)} [(λ, c)→(a, λ)]
- Lee `c`: {(a, λ)} ⟶ {(λ, c)} [(a, λ)→(λ, c)]
- Lee `b`: {(λ, c)} ⟶ {(λ, cb)} [(λ, c)→(λ, cb)]
- Lee `a`: {(λ, cb)} ⟶ {(a, cba)} [(λ, cb)→(a, cba)]
- Lee `a`: {(a, cba)} ⟶ {(a, cbaa)} [(a, cba)→(a, cbaa)]
- Lee `b`: {(a, cbaa)} ⟶ {(ab, cbaab)} [(a, cbaa)→(ab, cbaab)]
- Lee `b`: {(ab, cbaab)} ⟶ {(abb, cbaabb)} [(ab, cbaab)→(abb, cbaabb)]
- Lee `c`: {(abb, cbaabb)} ⟶ {(abbc, cbaabb)} [(abb, cbaabb)→(abbc, cbaabb)]
- Lee `b`: {(abbc, cbaabb)} ⟶ {(abbcb, cbaabb)} [(abbc, cbaabb)→(abbcb, cbaabb)]
- **Aceptada**: queda {(abbcb, cbaabb)} ∈ F.

## Cadena `cbaabbcb10000`

- Inicio: {(λ, λ)}
- Lee `c`: {(λ, λ)} ⟶ {(λ, c)} [(λ, λ)→(λ, c)]
- Lee `b`: {(λ, c)} ⟶ {(λ, cb)} [(λ, c)→(λ, cb)]
- Lee `a`: {(λ, cb)} ⟶ {(a, cba)} [(λ, cb)→(a, cba)]
- Lee `a`: {(a, cba)} ⟶ {(a, cbaa)} [(a, cba)→(a, cbaa)]
- Lee `b`: {(a, cbaa)} ⟶ {(ab, cbaab)} [(a, cbaa)→(ab, cbaab)]
- Lee `b`: {(ab, cbaab)} ⟶ {(abb, cbaabb)} [(ab, cbaab)→(abb, cbaabb)]
- Lee `c`: {(abb, cbaabb)} ⟶ {(abbc, cbaabb)} [(abb, cbaabb)→(abbc, cbaabb)]
- Lee `b`: {(abbc, cbaabb)} ⟶ {(abbcb, cbaabb)} [(abbc, cbaabb)→(abbcb, cbaabb)]
- Lee `1`: {(abbcb, cbaabb)} ⟶ {(abbcb, cbaabb)} [(abbcb, cbaabb)→(abbcb, cbaabb)]
- Lee `0`: {(abbcb, cbaabb)} ⟶ {(abbcb, cbaabb)} [(abbcb, cbaabb)→(abbcb, cbaabb)]
- Lee `0`: {(abbcb, cbaabb)} ⟶ {(abbcb, cbaabb)} [(abbcb, cbaabb)→(abbcb, cbaabb)]
- Lee `0`: {(abbcb, cbaabb)} ⟶ {(abbcb, cbaabb)} [(abbcb, cbaabb)→(abbcb, cbaabb)]
- Lee `0`: {(abbcb, cbaabb)} ⟶ {(abbcb, cbaabb)} [(abbcb, cbaabb)→(abbcb, cbaabb)]
- **Aceptada**: queda {(abbcb, cbaabb)} ∈ F.

## Cadena `0a111acbaabbcb`

- Inicio: {(λ, λ)}
- Lee `0`: {(λ, λ)} ⟶ {(λ, λ)} [(λ, λ)→(λ, λ)]
- Lee `a`: {(λ, λ)} ⟶ {(a, λ)} [(λ, λ)→(a, λ)]
- Lee `1`: {(a, λ)} ⟶ {(λ, λ)} [(a, λ)→(λ, λ)]
- Lee `1`: {(λ, λ)} ⟶ {(λ, λ)} [(λ, λ)→(λ, λ)]
- Lee `1`: {(λ, λ)} ⟶ {(λ, λ)} [(λ, λ)→(λ, λ)]
- Lee `a`: {(λ, λ)} ⟶ {(a, λ)} [(λ, λ)→(a, λ)]
- Lee `c`: {(a, λ)} ⟶ {(λ, c)} [(a, λ)→(λ, c)]
- Lee `b`: {(λ, c)} ⟶ {(λ, cb)} [(λ, c)→(λ, cb)]
- Lee `a`: {(λ, cb)} ⟶ {(a, cba)} [(λ, cb)→(a, cba)]
- Lee `a`: {(a, cba)} ⟶ {(a, cbaa)} [(a, cba)→(a, cbaa)]
- Lee `b`: {(a, cbaa)} ⟶ {(ab, cbaab)} [(a, cbaa)→(ab, cbaab)]
- Lee `b`: {(ab, cbaab)} ⟶ {(abb, cbaabb)} [(ab, cbaab)→(abb, cbaabb)]
- Lee `c`: {(abb, cbaabb)} ⟶ {(abbc, cbaabb)} [(abb, cbaabb)→(abbc, cbaabb)]
- Lee `b`: {(abbc, cbaabb)} ⟶ {(abbcb, cbaabb)} [(abbc, cbaabb)→(abbcb, cbaabb)]
- **Aceptada**: queda {(abbcb, cbaabb)} ∈ F.

## Cadena λ

- Inicio: {(λ, λ)}
- **Rechazada**: ningún estado de {(λ, λ)} es de aceptación.

## Cadena `1`

- Inicio: {(λ, λ)}
- Lee `1`: {(λ, λ)} ⟶ {(λ, λ)} [(λ, λ)→(λ, λ)]
- **Rechazada**: ningún estado de {(λ, λ)} es de aceptación.

## Cadena `b0c`

- Inicio: {(λ, λ)}
- Lee `b`: {(λ, λ)} ⟶ {(λ, λ)} [(λ, λ)→(λ, λ)]
- Lee `0`: {(λ, λ)} ⟶ {(λ, λ)} [(λ, λ)→(λ, λ)]
- Lee `c`: {(λ, λ)} ⟶ {(λ, c)} [(λ, λ)→(λ, c)]
- **Rechazada**: ningún estado de {(λ, c)} es de aceptación.

## Cadena `1c1ab`

- Inicio: {(λ, λ)}
- Lee `1`: {(λ, λ)} ⟶ {(λ, λ)} [(λ, λ)→(λ, λ)]
- Lee `c`: {(λ, λ)} ⟶ {(λ, c)} [(λ, λ)→(λ, c)]
- Lee `1`: {(λ, c)} ⟶ {(λ, λ)} [(λ, c)→(λ, λ)]
- Lee `a`: {(λ, λ)} ⟶ {(a, λ)} [(λ, λ)→(a, λ)]
- Lee `b`: {(a, λ)} ⟶ {(ab, λ)} [(a, λ)→(ab, λ)]
- **Rechazada**: ningún estado de {(ab, λ)} es de aceptación.

## Cadena `1111cccb`

- Inicio: {(λ, λ)}
- Lee `1`: {(λ, λ)} ⟶ {(λ, λ)} [(λ, λ)→(λ, λ)]
- Lee `1`: {(λ, λ)} ⟶ {(λ, λ)} [(λ, λ)→(λ, λ)]
- Lee `1`: {(λ, λ)} ⟶ {(λ, λ)} [(λ, λ)→(λ, λ)]
- Lee `1`: {(λ, λ)} ⟶ {(λ, λ)} [(λ, λ)→(λ, λ)]
- Lee `c`: {(λ, λ)} ⟶ {(λ, c)} [(λ, λ)→(λ, c)]
- Lee `c`: {(λ, c)} ⟶ {(λ, c)} [(λ, c)→(λ, c)]
- Lee `c`: {(λ, c)} ⟶ {(λ, c)} [(λ, c)→(λ, c)]
- Lee `b`: {(λ, c)} ⟶ {(λ, cb)} [(λ, c)→(λ, cb)]
- **Rechazada**: ningún estado de {(λ, cb)} es de aceptación.

## Cadena `cbbcccb`

- Inicio: {(λ, λ)}
- Lee `c`: {(λ, λ)} ⟶ {(λ, c)} [(λ, λ)→(λ, c)]
- Lee `b`: {(λ, c)} ⟶ {(λ, cb)} [(λ, c)→(λ, cb)]
- Lee `b`: {(λ, cb)} ⟶ {(λ, λ)} [(λ, cb)→(λ, λ)]
- Lee `c`: {(λ, λ)} ⟶ {(λ, c)} [(λ, λ)→(λ, c)]
- Lee `c`: {(λ, c)} ⟶ {(λ, c)} [(λ, c)→(λ, c)]
- Lee `c`: {(λ, c)} ⟶ {(λ, c)} [(λ, c)→(λ, c)]
- Lee `b`: {(λ, c)} ⟶ {(λ, cb)} [(λ, c)→(λ, cb)]
- **Rechazada**: ningún estado de {(λ, cb)} es de aceptación.
