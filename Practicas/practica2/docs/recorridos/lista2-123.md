# Recorridos: Lista 2 · Ejercicio 123

Las palabras de Σ3 de la forma wxw donde w ∈ Σ3² y x ∈ Σ3*.

Autómata: `lista2-123` (AFD).

## Cadena `bbbb`

- Inicio: {ini}
- Lee `b`: {ini} ⟶ {b} [ini→b]
- Lee `b`: {b} ⟶ {bb:∅} [b→bb:∅]
- Lee `b`: {bb:∅} ⟶ {bb:b…} [bb:∅→bb:b…]
- Lee `b`: {bb:b…} ⟶ {bb:bb} [bb:b…→bb:bb]
- **Aceptada**: queda {bb:bb} ∈ F.

## Cadena `abbab`

- Inicio: {ini}
- Lee `a`: {ini} ⟶ {a} [ini→a]
- Lee `b`: {a} ⟶ {ab:∅} [a→ab:∅]
- Lee `b`: {ab:∅} ⟶ {ab:∅} [ab:∅→ab:∅]
- Lee `a`: {ab:∅} ⟶ {ab:a…} [ab:∅→ab:a…]
- Lee `b`: {ab:a…} ⟶ {ab:ab} [ab:a…→ab:ab]
- **Aceptada**: queda {ab:ab} ∈ F.

## Cadena `bbbbabb`

- Inicio: {ini}
- Lee `b`: {ini} ⟶ {b} [ini→b]
- Lee `b`: {b} ⟶ {bb:∅} [b→bb:∅]
- Lee `b`: {bb:∅} ⟶ {bb:b…} [bb:∅→bb:b…]
- Lee `b`: {bb:b…} ⟶ {bb:bb} [bb:b…→bb:bb]
- Lee `a`: {bb:bb} ⟶ {bb:∅} [bb:bb→bb:∅]
- Lee `b`: {bb:∅} ⟶ {bb:b…} [bb:∅→bb:b…]
- Lee `b`: {bb:b…} ⟶ {bb:bb} [bb:b…→bb:bb]
- **Aceptada**: queda {bb:bb} ∈ F.

## Cadena `abaabbbab`

- Inicio: {ini}
- Lee `a`: {ini} ⟶ {a} [ini→a]
- Lee `b`: {a} ⟶ {ab:∅} [a→ab:∅]
- Lee `a`: {ab:∅} ⟶ {ab:a…} [ab:∅→ab:a…]
- Lee `a`: {ab:a…} ⟶ {ab:a…} [ab:a…→ab:a…]
- Lee `b`: {ab:a…} ⟶ {ab:ab} [ab:a…→ab:ab]
- Lee `b`: {ab:ab} ⟶ {ab:∅} [ab:ab→ab:∅]
- Lee `b`: {ab:∅} ⟶ {ab:∅} [ab:∅→ab:∅]
- Lee `a`: {ab:∅} ⟶ {ab:a…} [ab:∅→ab:a…]
- Lee `b`: {ab:a…} ⟶ {ab:ab} [ab:a…→ab:ab]
- **Aceptada**: queda {ab:ab} ∈ F.

## Cadena `abbaabaaaaab`

- Inicio: {ini}
- Lee `a`: {ini} ⟶ {a} [ini→a]
- Lee `b`: {a} ⟶ {ab:∅} [a→ab:∅]
- Lee `b`: {ab:∅} ⟶ {ab:∅} [ab:∅→ab:∅]
- Lee `a`: {ab:∅} ⟶ {ab:a…} [ab:∅→ab:a…]
- Lee `a`: {ab:a…} ⟶ {ab:a…} [ab:a…→ab:a…]
- Lee `b`: {ab:a…} ⟶ {ab:ab} [ab:a…→ab:ab]
- Lee `a`: {ab:ab} ⟶ {ab:a…} [ab:ab→ab:a…]
- Lee `a`: {ab:a…} ⟶ {ab:a…} [ab:a…→ab:a…]
- Lee `a`: {ab:a…} ⟶ {ab:a…} [ab:a…→ab:a…]
- Lee `a`: {ab:a…} ⟶ {ab:a…} [ab:a…→ab:a…]
- Lee `a`: {ab:a…} ⟶ {ab:a…} [ab:a…→ab:a…]
- Lee `b`: {ab:a…} ⟶ {ab:ab} [ab:a…→ab:ab]
- **Aceptada**: queda {ab:ab} ∈ F.

## Cadena λ

- Inicio: {ini}
- **Rechazada**: ningún estado de {ini} es de aceptación.

## Cadena `a`

- Inicio: {ini}
- Lee `a`: {ini} ⟶ {a} [ini→a]
- **Rechazada**: ningún estado de {a} es de aceptación.

## Cadena `bab`

- Inicio: {ini}
- Lee `b`: {ini} ⟶ {b} [ini→b]
- Lee `a`: {b} ⟶ {ba:∅} [b→ba:∅]
- Lee `b`: {ba:∅} ⟶ {ba:b…} [ba:∅→ba:b…]
- **Rechazada**: ningún estado de {ba:b…} es de aceptación.

## Cadena `babbb`

- Inicio: {ini}
- Lee `b`: {ini} ⟶ {b} [ini→b]
- Lee `a`: {b} ⟶ {ba:∅} [b→ba:∅]
- Lee `b`: {ba:∅} ⟶ {ba:b…} [ba:∅→ba:b…]
- Lee `b`: {ba:b…} ⟶ {ba:b…} [ba:b…→ba:b…]
- Lee `b`: {ba:b…} ⟶ {ba:b…} [ba:b…→ba:b…]
- **Rechazada**: ningún estado de {ba:b…} es de aceptación.

## Cadena `aabbbbba`

- Inicio: {ini}
- Lee `a`: {ini} ⟶ {a} [ini→a]
- Lee `a`: {a} ⟶ {aa:∅} [a→aa:∅]
- Lee `b`: {aa:∅} ⟶ {aa:∅} [aa:∅→aa:∅]
- Lee `b`: {aa:∅} ⟶ {aa:∅} [aa:∅→aa:∅]
- Lee `b`: {aa:∅} ⟶ {aa:∅} [aa:∅→aa:∅]
- Lee `b`: {aa:∅} ⟶ {aa:∅} [aa:∅→aa:∅]
- Lee `b`: {aa:∅} ⟶ {aa:∅} [aa:∅→aa:∅]
- Lee `a`: {aa:∅} ⟶ {aa:a…} [aa:∅→aa:a…]
- **Rechazada**: ningún estado de {aa:a…} es de aceptación.

## Cadena `abab`

- Inicio: {ini}
- Lee `a`: {ini} ⟶ {a} [ini→a]
- Lee `b`: {a} ⟶ {ab:∅} [a→ab:∅]
- Lee `a`: {ab:∅} ⟶ {ab:a…} [ab:∅→ab:a…]
- Lee `b`: {ab:a…} ⟶ {ab:ab} [ab:a…→ab:ab]
- **Aceptada**: queda {ab:ab} ∈ F.

## Cadena `aaa`

- Inicio: {ini}
- Lee `a`: {ini} ⟶ {a} [ini→a]
- Lee `a`: {a} ⟶ {aa:∅} [a→aa:∅]
- Lee `a`: {aa:∅} ⟶ {aa:a…} [aa:∅→aa:a…]
- **Rechazada**: ningún estado de {aa:a…} es de aceptación.
