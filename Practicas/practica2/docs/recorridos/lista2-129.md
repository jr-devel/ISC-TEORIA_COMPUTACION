# Recorridos: Lista 2 · Ejercicio 129

AFD dado: palabras de {a, b}* que no contienen tres b consecutivas.

Autómata: `lista2-129` (AFD).

## Cadena λ

- Inicio: {q0}
- **Aceptada**: queda {q0} ∈ F.

## Cadena `b`

- Inicio: {q0}
- Lee `b`: {q0} ⟶ {q1} [q0→q1]
- **Aceptada**: queda {q1} ∈ F.

## Cadena `baa`

- Inicio: {q0}
- Lee `b`: {q0} ⟶ {q1} [q0→q1]
- Lee `a`: {q1} ⟶ {q0} [q1→q0]
- Lee `a`: {q0} ⟶ {q0} [q0→q0]
- **Aceptada**: queda {q0} ∈ F.

## Cadena `babba`

- Inicio: {q0}
- Lee `b`: {q0} ⟶ {q1} [q0→q1]
- Lee `a`: {q1} ⟶ {q0} [q1→q0]
- Lee `b`: {q0} ⟶ {q1} [q0→q1]
- Lee `b`: {q1} ⟶ {q2} [q1→q2]
- Lee `a`: {q2} ⟶ {q0} [q2→q0]
- **Aceptada**: queda {q0} ∈ F.

## Cadena `abbababa`

- Inicio: {q0}
- Lee `a`: {q0} ⟶ {q0} [q0→q0]
- Lee `b`: {q0} ⟶ {q1} [q0→q1]
- Lee `b`: {q1} ⟶ {q2} [q1→q2]
- Lee `a`: {q2} ⟶ {q0} [q2→q0]
- Lee `b`: {q0} ⟶ {q1} [q0→q1]
- Lee `a`: {q1} ⟶ {q0} [q1→q0]
- Lee `b`: {q0} ⟶ {q1} [q0→q1]
- Lee `a`: {q1} ⟶ {q0} [q1→q0]
- **Aceptada**: queda {q0} ∈ F.

## Cadena `bbb`

- Inicio: {q0}
- Lee `b`: {q0} ⟶ {q1} [q0→q1]
- Lee `b`: {q1} ⟶ {q2} [q1→q2]
- Lee `b`: {q2} ⟶ {q3} [q2→q3]
- **Rechazada**: ningún estado de {q3} es de aceptación.

## Cadena `abbb`

- Inicio: {q0}
- Lee `a`: {q0} ⟶ {q0} [q0→q0]
- Lee `b`: {q0} ⟶ {q1} [q0→q1]
- Lee `b`: {q1} ⟶ {q2} [q1→q2]
- Lee `b`: {q2} ⟶ {q3} [q2→q3]
- **Rechazada**: ningún estado de {q3} es de aceptación.

## Cadena `abbbaa`

- Inicio: {q0}
- Lee `a`: {q0} ⟶ {q0} [q0→q0]
- Lee `b`: {q0} ⟶ {q1} [q0→q1]
- Lee `b`: {q1} ⟶ {q2} [q1→q2]
- Lee `b`: {q2} ⟶ {q3} [q2→q3]
- Lee `a`: {q3} ⟶ {q3} [q3→q3]
- Lee `a`: {q3} ⟶ {q3} [q3→q3]
- **Rechazada**: ningún estado de {q3} es de aceptación.

## Cadena `abbbabba`

- Inicio: {q0}
- Lee `a`: {q0} ⟶ {q0} [q0→q0]
- Lee `b`: {q0} ⟶ {q1} [q0→q1]
- Lee `b`: {q1} ⟶ {q2} [q1→q2]
- Lee `b`: {q2} ⟶ {q3} [q2→q3]
- Lee `a`: {q3} ⟶ {q3} [q3→q3]
- Lee `b`: {q3} ⟶ {q3} [q3→q3]
- Lee `b`: {q3} ⟶ {q3} [q3→q3]
- Lee `a`: {q3} ⟶ {q3} [q3→q3]
- **Rechazada**: ningún estado de {q3} es de aceptación.

## Cadena `abbabbbaaaa`

- Inicio: {q0}
- Lee `a`: {q0} ⟶ {q0} [q0→q0]
- Lee `b`: {q0} ⟶ {q1} [q0→q1]
- Lee `b`: {q1} ⟶ {q2} [q1→q2]
- Lee `a`: {q2} ⟶ {q0} [q2→q0]
- Lee `b`: {q0} ⟶ {q1} [q0→q1]
- Lee `b`: {q1} ⟶ {q2} [q1→q2]
- Lee `b`: {q2} ⟶ {q3} [q2→q3]
- Lee `a`: {q3} ⟶ {q3} [q3→q3]
- Lee `a`: {q3} ⟶ {q3} [q3→q3]
- Lee `a`: {q3} ⟶ {q3} [q3→q3]
- Lee `a`: {q3} ⟶ {q3} [q3→q3]
- **Rechazada**: ningún estado de {q3} es de aceptación.
