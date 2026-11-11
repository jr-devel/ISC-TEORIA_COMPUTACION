# Recorridos: Lista 2 · Ejercicio 115

L = {w ∈ Σ2* : w = (abc)ⁿ, n ∈ N}.

Autómata: `lista2-115` (AFD).

## Cadena λ

- Inicio: {(abc)*}
- **Aceptada**: queda {(abc)*} ∈ F.

## Cadena `abc`

- Inicio: {(abc)*}
- Lee `a`: {(abc)*} ⟶ {…a} [(abc)*→…a]
- Lee `b`: {…a} ⟶ {…ab} […a→…ab]
- Lee `c`: {…ab} ⟶ {(abc)*} […ab→(abc)*]
- **Aceptada**: queda {(abc)*} ∈ F.

## Cadena `abcabc`

- Inicio: {(abc)*}
- Lee `a`: {(abc)*} ⟶ {…a} [(abc)*→…a]
- Lee `b`: {…a} ⟶ {…ab} […a→…ab]
- Lee `c`: {…ab} ⟶ {(abc)*} […ab→(abc)*]
- Lee `a`: {(abc)*} ⟶ {…a} [(abc)*→…a]
- Lee `b`: {…a} ⟶ {…ab} […a→…ab]
- Lee `c`: {…ab} ⟶ {(abc)*} […ab→(abc)*]
- **Aceptada**: queda {(abc)*} ∈ F.

## Cadena `abcabcabc`

- Inicio: {(abc)*}
- Lee `a`: {(abc)*} ⟶ {…a} [(abc)*→…a]
- Lee `b`: {…a} ⟶ {…ab} […a→…ab]
- Lee `c`: {…ab} ⟶ {(abc)*} […ab→(abc)*]
- Lee `a`: {(abc)*} ⟶ {…a} [(abc)*→…a]
- Lee `b`: {…a} ⟶ {…ab} […a→…ab]
- Lee `c`: {…ab} ⟶ {(abc)*} […ab→(abc)*]
- Lee `a`: {(abc)*} ⟶ {…a} [(abc)*→…a]
- Lee `b`: {…a} ⟶ {…ab} […a→…ab]
- Lee `c`: {…ab} ⟶ {(abc)*} […ab→(abc)*]
- **Aceptada**: queda {(abc)*} ∈ F.

## Cadena `abcabcabcabc`

- Inicio: {(abc)*}
- Lee `a`: {(abc)*} ⟶ {…a} [(abc)*→…a]
- Lee `b`: {…a} ⟶ {…ab} […a→…ab]
- Lee `c`: {…ab} ⟶ {(abc)*} […ab→(abc)*]
- Lee `a`: {(abc)*} ⟶ {…a} [(abc)*→…a]
- Lee `b`: {…a} ⟶ {…ab} […a→…ab]
- Lee `c`: {…ab} ⟶ {(abc)*} […ab→(abc)*]
- Lee `a`: {(abc)*} ⟶ {…a} [(abc)*→…a]
- Lee `b`: {…a} ⟶ {…ab} […a→…ab]
- Lee `c`: {…ab} ⟶ {(abc)*} […ab→(abc)*]
- Lee `a`: {(abc)*} ⟶ {…a} [(abc)*→…a]
- Lee `b`: {…a} ⟶ {…ab} […a→…ab]
- Lee `c`: {…ab} ⟶ {(abc)*} […ab→(abc)*]
- **Aceptada**: queda {(abc)*} ∈ F.

## Cadena `1`

- Inicio: {(abc)*}
- Lee `1`: {(abc)*} ⟶ {muerto} [(abc)*→muerto]
- **Rechazada**: ningún estado de {muerto} es de aceptación.

## Cadena `ba`

- Inicio: {(abc)*}
- Lee `b`: {(abc)*} ⟶ {muerto} [(abc)*→muerto]
- Lee `a`: {muerto} ⟶ {muerto} [muerto→muerto]
- **Rechazada**: ningún estado de {muerto} es de aceptación.

## Cadena `cbaa`

- Inicio: {(abc)*}
- Lee `c`: {(abc)*} ⟶ {muerto} [(abc)*→muerto]
- Lee `b`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `a`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `a`: {muerto} ⟶ {muerto} [muerto→muerto]
- **Rechazada**: ningún estado de {muerto} es de aceptación.

## Cadena `ca1bba`

- Inicio: {(abc)*}
- Lee `c`: {(abc)*} ⟶ {muerto} [(abc)*→muerto]
- Lee `a`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `1`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `b`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `b`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `a`: {muerto} ⟶ {muerto} [muerto→muerto]
- **Rechazada**: ningún estado de {muerto} es de aceptación.

## Cadena `ba1bc11cb`

- Inicio: {(abc)*}
- Lee `b`: {(abc)*} ⟶ {muerto} [(abc)*→muerto]
- Lee `a`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `1`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `b`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `c`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `1`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `1`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `c`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `b`: {muerto} ⟶ {muerto} [muerto→muerto]
- **Rechazada**: ningún estado de {muerto} es de aceptación.
