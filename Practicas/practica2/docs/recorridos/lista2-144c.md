# Recorridos: Lista 2 · Ejercicio 144c

c) El conjunto de cadenas que contienen aaa.

Autómata: `lista2-144c` (AFD).

## Cadena `aaa`

- Inicio: {λ}
- Lee `a`: {λ} ⟶ {a} [λ→a]
- Lee `a`: {a} ⟶ {aa} [a→aa]
- Lee `a`: {aa} ⟶ {aaa} [aa→aaa]
- **Aceptada**: queda {aaa} ∈ F.

## Cadena `baaa`

- Inicio: {λ}
- Lee `b`: {λ} ⟶ {λ} [λ→λ]
- Lee `a`: {λ} ⟶ {a} [λ→a]
- Lee `a`: {a} ⟶ {aa} [a→aa]
- Lee `a`: {aa} ⟶ {aaa} [aa→aaa]
- **Aceptada**: queda {aaa} ∈ F.

## Cadena `baaaaa`

- Inicio: {λ}
- Lee `b`: {λ} ⟶ {λ} [λ→λ]
- Lee `a`: {λ} ⟶ {a} [λ→a]
- Lee `a`: {a} ⟶ {aa} [a→aa]
- Lee `a`: {aa} ⟶ {aaa} [aa→aaa]
- Lee `a`: {aaa} ⟶ {aaa} [aaa→aaa]
- Lee `a`: {aaa} ⟶ {aaa} [aaa→aaa]
- **Aceptada**: queda {aaa} ∈ F.

## Cadena `aaababbb`

- Inicio: {λ}
- Lee `a`: {λ} ⟶ {a} [λ→a]
- Lee `a`: {a} ⟶ {aa} [a→aa]
- Lee `a`: {aa} ⟶ {aaa} [aa→aaa]
- Lee `b`: {aaa} ⟶ {aaa} [aaa→aaa]
- Lee `a`: {aaa} ⟶ {aaa} [aaa→aaa]
- Lee `b`: {aaa} ⟶ {aaa} [aaa→aaa]
- Lee `b`: {aaa} ⟶ {aaa} [aaa→aaa]
- Lee `b`: {aaa} ⟶ {aaa} [aaa→aaa]
- **Aceptada**: queda {aaa} ∈ F.

## Cadena `aaabbaabbaa`

- Inicio: {λ}
- Lee `a`: {λ} ⟶ {a} [λ→a]
- Lee `a`: {a} ⟶ {aa} [a→aa]
- Lee `a`: {aa} ⟶ {aaa} [aa→aaa]
- Lee `b`: {aaa} ⟶ {aaa} [aaa→aaa]
- Lee `b`: {aaa} ⟶ {aaa} [aaa→aaa]
- Lee `a`: {aaa} ⟶ {aaa} [aaa→aaa]
- Lee `a`: {aaa} ⟶ {aaa} [aaa→aaa]
- Lee `b`: {aaa} ⟶ {aaa} [aaa→aaa]
- Lee `b`: {aaa} ⟶ {aaa} [aaa→aaa]
- Lee `a`: {aaa} ⟶ {aaa} [aaa→aaa]
- Lee `a`: {aaa} ⟶ {aaa} [aaa→aaa]
- **Aceptada**: queda {aaa} ∈ F.

## Cadena λ

- Inicio: {λ}
- **Rechazada**: ningún estado de {λ} es de aceptación.

## Cadena `a`

- Inicio: {λ}
- Lee `a`: {λ} ⟶ {a} [λ→a]
- **Rechazada**: ningún estado de {a} es de aceptación.

## Cadena `abb`

- Inicio: {λ}
- Lee `a`: {λ} ⟶ {a} [λ→a]
- Lee `b`: {a} ⟶ {λ} [a→λ]
- Lee `b`: {λ} ⟶ {λ} [λ→λ]
- **Rechazada**: ningún estado de {λ} es de aceptación.

## Cadena `abbab`

- Inicio: {λ}
- Lee `a`: {λ} ⟶ {a} [λ→a]
- Lee `b`: {a} ⟶ {λ} [a→λ]
- Lee `b`: {λ} ⟶ {λ} [λ→λ]
- Lee `a`: {λ} ⟶ {a} [λ→a]
- Lee `b`: {a} ⟶ {λ} [a→λ]
- **Rechazada**: ningún estado de {λ} es de aceptación.

## Cadena `bbabbaab`

- Inicio: {λ}
- Lee `b`: {λ} ⟶ {λ} [λ→λ]
- Lee `b`: {λ} ⟶ {λ} [λ→λ]
- Lee `a`: {λ} ⟶ {a} [λ→a]
- Lee `b`: {a} ⟶ {λ} [a→λ]
- Lee `b`: {λ} ⟶ {λ} [λ→λ]
- Lee `a`: {λ} ⟶ {a} [λ→a]
- Lee `a`: {a} ⟶ {aa} [a→aa]
- Lee `b`: {aa} ⟶ {λ} [aa→λ]
- **Rechazada**: ningún estado de {λ} es de aceptación.

## Cadena `ab`

- Inicio: {λ}
- Lee `a`: {λ} ⟶ {a} [λ→a]
- Lee `b`: {a} ⟶ {λ} [a→λ]
- **Rechazada**: ningún estado de {λ} es de aceptación.
