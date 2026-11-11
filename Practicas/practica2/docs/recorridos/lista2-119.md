# Recorridos: Lista 2 · Ejercicio 119

Las palabras de Σ3 tales que después de cada subcadena aa aparece una b.

Autómata: `lista2-119` (AFD).

## Cadena λ

- Inicio: {sin a}
- **Aceptada**: queda {sin a} ∈ F.

## Cadena `a`

- Inicio: {sin a}
- Lee `a`: {sin a} ⟶ {a} [sin a→a]
- **Aceptada**: queda {a} ∈ F.

## Cadena `bbb`

- Inicio: {sin a}
- Lee `b`: {sin a} ⟶ {sin a} [sin a→sin a]
- Lee `b`: {sin a} ⟶ {sin a} [sin a→sin a]
- Lee `b`: {sin a} ⟶ {sin a} [sin a→sin a]
- **Aceptada**: queda {sin a} ∈ F.

## Cadena `ababa`

- Inicio: {sin a}
- Lee `a`: {sin a} ⟶ {a} [sin a→a]
- Lee `b`: {a} ⟶ {sin a} [a→sin a]
- Lee `a`: {sin a} ⟶ {a} [sin a→a]
- Lee `b`: {a} ⟶ {sin a} [a→sin a]
- Lee `a`: {sin a} ⟶ {a} [sin a→a]
- **Aceptada**: queda {a} ∈ F.

## Cadena `abababba`

- Inicio: {sin a}
- Lee `a`: {sin a} ⟶ {a} [sin a→a]
- Lee `b`: {a} ⟶ {sin a} [a→sin a]
- Lee `a`: {sin a} ⟶ {a} [sin a→a]
- Lee `b`: {a} ⟶ {sin a} [a→sin a]
- Lee `a`: {sin a} ⟶ {a} [sin a→a]
- Lee `b`: {a} ⟶ {sin a} [a→sin a]
- Lee `b`: {sin a} ⟶ {sin a} [sin a→sin a]
- Lee `a`: {sin a} ⟶ {a} [sin a→a]
- **Aceptada**: queda {a} ∈ F.

## Cadena `aa`

- Inicio: {sin a}
- Lee `a`: {sin a} ⟶ {a} [sin a→a]
- Lee `a`: {a} ⟶ {aa} [a→aa]
- **Rechazada**: ningún estado de {aa} es de aceptación.

## Cadena `aaa`

- Inicio: {sin a}
- Lee `a`: {sin a} ⟶ {a} [sin a→a]
- Lee `a`: {a} ⟶ {aa} [a→aa]
- Lee `a`: {aa} ⟶ {muerto} [aa→muerto]
- **Rechazada**: ningún estado de {muerto} es de aceptación.

## Cadena `abbaa`

- Inicio: {sin a}
- Lee `a`: {sin a} ⟶ {a} [sin a→a]
- Lee `b`: {a} ⟶ {sin a} [a→sin a]
- Lee `b`: {sin a} ⟶ {sin a} [sin a→sin a]
- Lee `a`: {sin a} ⟶ {a} [sin a→a]
- Lee `a`: {a} ⟶ {aa} [a→aa]
- **Rechazada**: ningún estado de {aa} es de aceptación.

## Cadena `aabaaab`

- Inicio: {sin a}
- Lee `a`: {sin a} ⟶ {a} [sin a→a]
- Lee `a`: {a} ⟶ {aa} [a→aa]
- Lee `b`: {aa} ⟶ {sin a} [aa→sin a]
- Lee `a`: {sin a} ⟶ {a} [sin a→a]
- Lee `a`: {a} ⟶ {aa} [a→aa]
- Lee `a`: {aa} ⟶ {muerto} [aa→muerto]
- Lee `b`: {muerto} ⟶ {muerto} [muerto→muerto]
- **Rechazada**: ningún estado de {muerto} es de aceptación.

## Cadena `aabababbaa`

- Inicio: {sin a}
- Lee `a`: {sin a} ⟶ {a} [sin a→a]
- Lee `a`: {a} ⟶ {aa} [a→aa]
- Lee `b`: {aa} ⟶ {sin a} [aa→sin a]
- Lee `a`: {sin a} ⟶ {a} [sin a→a]
- Lee `b`: {a} ⟶ {sin a} [a→sin a]
- Lee `a`: {sin a} ⟶ {a} [sin a→a]
- Lee `b`: {a} ⟶ {sin a} [a→sin a]
- Lee `b`: {sin a} ⟶ {sin a} [sin a→sin a]
- Lee `a`: {sin a} ⟶ {a} [sin a→a]
- Lee `a`: {a} ⟶ {aa} [a→aa]
- **Rechazada**: ningún estado de {aa} es de aceptación.
