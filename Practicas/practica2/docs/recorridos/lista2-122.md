# Recorridos: Lista 2 · Ejercicio 122

Las palabras de Σ1 tales que cualquier cadena de tres símbolos consecutivos tiene un 0.

Autómata: `lista2-122` (AFD).

## Cadena λ

- Inicio: {0 sin 0}
- **Aceptada**: queda {0 sin 0} ∈ F.

## Cadena `1`

- Inicio: {0 sin 0}
- Lee `1`: {0 sin 0} ⟶ {1 sin 0} [0 sin 0→1 sin 0]
- **Aceptada**: queda {1 sin 0} ∈ F.

## Cadena `100`

- Inicio: {0 sin 0}
- Lee `1`: {0 sin 0} ⟶ {1 sin 0} [0 sin 0→1 sin 0]
- Lee `0`: {1 sin 0} ⟶ {0 sin 0} [1 sin 0→0 sin 0]
- Lee `0`: {0 sin 0} ⟶ {0 sin 0} [0 sin 0→0 sin 0]
- **Aceptada**: queda {0 sin 0} ∈ F.

## Cadena `22010`

- Inicio: {0 sin 0}
- Lee `2`: {0 sin 0} ⟶ {1 sin 0} [0 sin 0→1 sin 0]
- Lee `2`: {1 sin 0} ⟶ {2 sin 0} [1 sin 0→2 sin 0]
- Lee `0`: {2 sin 0} ⟶ {0 sin 0} [2 sin 0→0 sin 0]
- Lee `1`: {0 sin 0} ⟶ {1 sin 0} [0 sin 0→1 sin 0]
- Lee `0`: {1 sin 0} ⟶ {0 sin 0} [1 sin 0→0 sin 0]
- **Aceptada**: queda {0 sin 0} ∈ F.

## Cadena `20202021`

- Inicio: {0 sin 0}
- Lee `2`: {0 sin 0} ⟶ {1 sin 0} [0 sin 0→1 sin 0]
- Lee `0`: {1 sin 0} ⟶ {0 sin 0} [1 sin 0→0 sin 0]
- Lee `2`: {0 sin 0} ⟶ {1 sin 0} [0 sin 0→1 sin 0]
- Lee `0`: {1 sin 0} ⟶ {0 sin 0} [1 sin 0→0 sin 0]
- Lee `2`: {0 sin 0} ⟶ {1 sin 0} [0 sin 0→1 sin 0]
- Lee `0`: {1 sin 0} ⟶ {0 sin 0} [1 sin 0→0 sin 0]
- Lee `2`: {0 sin 0} ⟶ {1 sin 0} [0 sin 0→1 sin 0]
- Lee `1`: {1 sin 0} ⟶ {2 sin 0} [1 sin 0→2 sin 0]
- **Aceptada**: queda {2 sin 0} ∈ F.

## Cadena `112`

- Inicio: {0 sin 0}
- Lee `1`: {0 sin 0} ⟶ {1 sin 0} [0 sin 0→1 sin 0]
- Lee `1`: {1 sin 0} ⟶ {2 sin 0} [1 sin 0→2 sin 0]
- Lee `2`: {2 sin 0} ⟶ {muerto} [2 sin 0→muerto]
- **Rechazada**: ningún estado de {muerto} es de aceptación.

## Cadena `0122`

- Inicio: {0 sin 0}
- Lee `0`: {0 sin 0} ⟶ {0 sin 0} [0 sin 0→0 sin 0]
- Lee `1`: {0 sin 0} ⟶ {1 sin 0} [0 sin 0→1 sin 0]
- Lee `2`: {1 sin 0} ⟶ {2 sin 0} [1 sin 0→2 sin 0]
- Lee `2`: {2 sin 0} ⟶ {muerto} [2 sin 0→muerto]
- **Rechazada**: ningún estado de {muerto} es de aceptación.

## Cadena `122010`

- Inicio: {0 sin 0}
- Lee `1`: {0 sin 0} ⟶ {1 sin 0} [0 sin 0→1 sin 0]
- Lee `2`: {1 sin 0} ⟶ {2 sin 0} [1 sin 0→2 sin 0]
- Lee `2`: {2 sin 0} ⟶ {muerto} [2 sin 0→muerto]
- Lee `0`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `1`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `0`: {muerto} ⟶ {muerto} [muerto→muerto]
- **Rechazada**: ningún estado de {muerto} es de aceptación.

## Cadena `21110110`

- Inicio: {0 sin 0}
- Lee `2`: {0 sin 0} ⟶ {1 sin 0} [0 sin 0→1 sin 0]
- Lee `1`: {1 sin 0} ⟶ {2 sin 0} [1 sin 0→2 sin 0]
- Lee `1`: {2 sin 0} ⟶ {muerto} [2 sin 0→muerto]
- Lee `1`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `0`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `1`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `1`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `0`: {muerto} ⟶ {muerto} [muerto→muerto]
- **Rechazada**: ningún estado de {muerto} es de aceptación.

## Cadena `01112200022`

- Inicio: {0 sin 0}
- Lee `0`: {0 sin 0} ⟶ {0 sin 0} [0 sin 0→0 sin 0]
- Lee `1`: {0 sin 0} ⟶ {1 sin 0} [0 sin 0→1 sin 0]
- Lee `1`: {1 sin 0} ⟶ {2 sin 0} [1 sin 0→2 sin 0]
- Lee `1`: {2 sin 0} ⟶ {muerto} [2 sin 0→muerto]
- Lee `2`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `2`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `0`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `0`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `0`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `2`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `2`: {muerto} ⟶ {muerto} [muerto→muerto]
- **Rechazada**: ningún estado de {muerto} es de aceptación.
