# Recorridos: Lista 2 · Ejercicio 142a

a) LA = (ab)* = {(ab)ⁿ : n ≥ 0}.

Autómata: `lista2-142a` (AFD).

## Cadena λ

- Inicio: {(ab)*}
- **Aceptada**: queda {(ab)*} ∈ F.

## Cadena `ab`

- Inicio: {(ab)*}
- Lee `a`: {(ab)*} ⟶ {…a} [(ab)*→…a]
- Lee `b`: {…a} ⟶ {(ab)*} […a→(ab)*]
- **Aceptada**: queda {(ab)*} ∈ F.

## Cadena `abab`

- Inicio: {(ab)*}
- Lee `a`: {(ab)*} ⟶ {…a} [(ab)*→…a]
- Lee `b`: {…a} ⟶ {(ab)*} […a→(ab)*]
- Lee `a`: {(ab)*} ⟶ {…a} [(ab)*→…a]
- Lee `b`: {…a} ⟶ {(ab)*} […a→(ab)*]
- **Aceptada**: queda {(ab)*} ∈ F.

## Cadena `abababababab`

- Inicio: {(ab)*}
- Lee `a`: {(ab)*} ⟶ {…a} [(ab)*→…a]
- Lee `b`: {…a} ⟶ {(ab)*} […a→(ab)*]
- Lee `a`: {(ab)*} ⟶ {…a} [(ab)*→…a]
- Lee `b`: {…a} ⟶ {(ab)*} […a→(ab)*]
- Lee `a`: {(ab)*} ⟶ {…a} [(ab)*→…a]
- Lee `b`: {…a} ⟶ {(ab)*} […a→(ab)*]
- Lee `a`: {(ab)*} ⟶ {…a} [(ab)*→…a]
- Lee `b`: {…a} ⟶ {(ab)*} […a→(ab)*]
- Lee `a`: {(ab)*} ⟶ {…a} [(ab)*→…a]
- Lee `b`: {…a} ⟶ {(ab)*} […a→(ab)*]
- Lee `a`: {(ab)*} ⟶ {…a} [(ab)*→…a]
- Lee `b`: {…a} ⟶ {(ab)*} […a→(ab)*]
- **Aceptada**: queda {(ab)*} ∈ F.

## Cadena `ababababababab`

- Inicio: {(ab)*}
- Lee `a`: {(ab)*} ⟶ {…a} [(ab)*→…a]
- Lee `b`: {…a} ⟶ {(ab)*} […a→(ab)*]
- Lee `a`: {(ab)*} ⟶ {…a} [(ab)*→…a]
- Lee `b`: {…a} ⟶ {(ab)*} […a→(ab)*]
- Lee `a`: {(ab)*} ⟶ {…a} [(ab)*→…a]
- Lee `b`: {…a} ⟶ {(ab)*} […a→(ab)*]
- Lee `a`: {(ab)*} ⟶ {…a} [(ab)*→…a]
- Lee `b`: {…a} ⟶ {(ab)*} […a→(ab)*]
- Lee `a`: {(ab)*} ⟶ {…a} [(ab)*→…a]
- Lee `b`: {…a} ⟶ {(ab)*} […a→(ab)*]
- Lee `a`: {(ab)*} ⟶ {…a} [(ab)*→…a]
- Lee `b`: {…a} ⟶ {(ab)*} […a→(ab)*]
- Lee `a`: {(ab)*} ⟶ {…a} [(ab)*→…a]
- Lee `b`: {…a} ⟶ {(ab)*} […a→(ab)*]
- **Aceptada**: queda {(ab)*} ∈ F.

## Cadena `a`

- Inicio: {(ab)*}
- Lee `a`: {(ab)*} ⟶ {…a} [(ab)*→…a]
- **Rechazada**: ningún estado de {…a} es de aceptación.

## Cadena `aa`

- Inicio: {(ab)*}
- Lee `a`: {(ab)*} ⟶ {…a} [(ab)*→…a]
- Lee `a`: {…a} ⟶ {muerto} […a→muerto]
- **Rechazada**: ningún estado de {muerto} es de aceptación.

## Cadena `abba`

- Inicio: {(ab)*}
- Lee `a`: {(ab)*} ⟶ {…a} [(ab)*→…a]
- Lee `b`: {…a} ⟶ {(ab)*} […a→(ab)*]
- Lee `b`: {(ab)*} ⟶ {muerto} [(ab)*→muerto]
- Lee `a`: {muerto} ⟶ {muerto} [muerto→muerto]
- **Rechazada**: ningún estado de {muerto} es de aceptación.

## Cadena `bbbbba`

- Inicio: {(ab)*}
- Lee `b`: {(ab)*} ⟶ {muerto} [(ab)*→muerto]
- Lee `b`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `b`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `b`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `b`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `a`: {muerto} ⟶ {muerto} [muerto→muerto]
- **Rechazada**: ningún estado de {muerto} es de aceptación.

## Cadena `aaaaaabab`

- Inicio: {(ab)*}
- Lee `a`: {(ab)*} ⟶ {…a} [(ab)*→…a]
- Lee `a`: {…a} ⟶ {muerto} […a→muerto]
- Lee `a`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `a`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `a`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `a`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `b`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `a`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `b`: {muerto} ⟶ {muerto} [muerto→muerto]
- **Rechazada**: ningún estado de {muerto} es de aceptación.
