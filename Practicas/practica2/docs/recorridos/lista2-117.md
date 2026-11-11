# Recorridos: Lista 2 · Ejercicio 117

L = {w ∈ Σ3* : w = aⁿbᵐaᵖb^q, m, n, p, q ∈ N}.

Autómata: `lista2-117` (AFD).

## Cadena λ

- Inicio: {f1:a*}
- **Aceptada**: queda {f1:a*} ∈ F.

## Cadena `a`

- Inicio: {f1:a*}
- Lee `a`: {f1:a*} ⟶ {f1:a*} [f1:a*→f1:a*]
- **Aceptada**: queda {f1:a*} ∈ F.

## Cadena `baa`

- Inicio: {f1:a*}
- Lee `b`: {f1:a*} ⟶ {f2:b*} [f1:a*→f2:b*]
- Lee `a`: {f2:b*} ⟶ {f3:a*} [f2:b*→f3:a*]
- Lee `a`: {f3:a*} ⟶ {f3:a*} [f3:a*→f3:a*]
- **Aceptada**: queda {f3:a*} ∈ F.

## Cadena `bbaaa`

- Inicio: {f1:a*}
- Lee `b`: {f1:a*} ⟶ {f2:b*} [f1:a*→f2:b*]
- Lee `b`: {f2:b*} ⟶ {f2:b*} [f2:b*→f2:b*]
- Lee `a`: {f2:b*} ⟶ {f3:a*} [f2:b*→f3:a*]
- Lee `a`: {f3:a*} ⟶ {f3:a*} [f3:a*→f3:a*]
- Lee `a`: {f3:a*} ⟶ {f3:a*} [f3:a*→f3:a*]
- **Aceptada**: queda {f3:a*} ∈ F.

## Cadena `aaaaaaab`

- Inicio: {f1:a*}
- Lee `a`: {f1:a*} ⟶ {f1:a*} [f1:a*→f1:a*]
- Lee `a`: {f1:a*} ⟶ {f1:a*} [f1:a*→f1:a*]
- Lee `a`: {f1:a*} ⟶ {f1:a*} [f1:a*→f1:a*]
- Lee `a`: {f1:a*} ⟶ {f1:a*} [f1:a*→f1:a*]
- Lee `a`: {f1:a*} ⟶ {f1:a*} [f1:a*→f1:a*]
- Lee `a`: {f1:a*} ⟶ {f1:a*} [f1:a*→f1:a*]
- Lee `a`: {f1:a*} ⟶ {f1:a*} [f1:a*→f1:a*]
- Lee `b`: {f1:a*} ⟶ {f2:b*} [f1:a*→f2:b*]
- **Aceptada**: queda {f2:b*} ∈ F.

## Cadena `baba`

- Inicio: {f1:a*}
- Lee `b`: {f1:a*} ⟶ {f2:b*} [f1:a*→f2:b*]
- Lee `a`: {f2:b*} ⟶ {f3:a*} [f2:b*→f3:a*]
- Lee `b`: {f3:a*} ⟶ {f4:b*} [f3:a*→f4:b*]
- Lee `a`: {f4:b*} ⟶ {muerto} [f4:b*→muerto]
- **Rechazada**: ningún estado de {muerto} es de aceptación.

## Cadena `babab`

- Inicio: {f1:a*}
- Lee `b`: {f1:a*} ⟶ {f2:b*} [f1:a*→f2:b*]
- Lee `a`: {f2:b*} ⟶ {f3:a*} [f2:b*→f3:a*]
- Lee `b`: {f3:a*} ⟶ {f4:b*} [f3:a*→f4:b*]
- Lee `a`: {f4:b*} ⟶ {muerto} [f4:b*→muerto]
- Lee `b`: {muerto} ⟶ {muerto} [muerto→muerto]
- **Rechazada**: ningún estado de {muerto} es de aceptación.

## Cadena `abbbaba`

- Inicio: {f1:a*}
- Lee `a`: {f1:a*} ⟶ {f1:a*} [f1:a*→f1:a*]
- Lee `b`: {f1:a*} ⟶ {f2:b*} [f1:a*→f2:b*]
- Lee `b`: {f2:b*} ⟶ {f2:b*} [f2:b*→f2:b*]
- Lee `b`: {f2:b*} ⟶ {f2:b*} [f2:b*→f2:b*]
- Lee `a`: {f2:b*} ⟶ {f3:a*} [f2:b*→f3:a*]
- Lee `b`: {f3:a*} ⟶ {f4:b*} [f3:a*→f4:b*]
- Lee `a`: {f4:b*} ⟶ {muerto} [f4:b*→muerto]
- **Rechazada**: ningún estado de {muerto} es de aceptación.

## Cadena `bbabababa`

- Inicio: {f1:a*}
- Lee `b`: {f1:a*} ⟶ {f2:b*} [f1:a*→f2:b*]
- Lee `b`: {f2:b*} ⟶ {f2:b*} [f2:b*→f2:b*]
- Lee `a`: {f2:b*} ⟶ {f3:a*} [f2:b*→f3:a*]
- Lee `b`: {f3:a*} ⟶ {f4:b*} [f3:a*→f4:b*]
- Lee `a`: {f4:b*} ⟶ {muerto} [f4:b*→muerto]
- Lee `b`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `a`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `b`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `a`: {muerto} ⟶ {muerto} [muerto→muerto]
- **Rechazada**: ningún estado de {muerto} es de aceptación.

## Cadena `baabaaaaaaab`

- Inicio: {f1:a*}
- Lee `b`: {f1:a*} ⟶ {f2:b*} [f1:a*→f2:b*]
- Lee `a`: {f2:b*} ⟶ {f3:a*} [f2:b*→f3:a*]
- Lee `a`: {f3:a*} ⟶ {f3:a*} [f3:a*→f3:a*]
- Lee `b`: {f3:a*} ⟶ {f4:b*} [f3:a*→f4:b*]
- Lee `a`: {f4:b*} ⟶ {muerto} [f4:b*→muerto]
- Lee `a`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `a`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `a`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `a`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `a`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `a`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `b`: {muerto} ⟶ {muerto} [muerto→muerto]
- **Rechazada**: ningún estado de {muerto} es de aceptación.
