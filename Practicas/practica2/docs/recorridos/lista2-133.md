# Recorridos: Lista 2 · Ejercicio 133

AFD dado con Q = {q0, q1, q2, q3}, Σ = {a, b}, F = {q0}.

Autómata: `lista2-133` (AFD).

## Cadena λ

- Inicio: {q0}
- **Aceptada**: queda {q0} ∈ F.

## Cadena `baab`

- Inicio: {q0}
- Lee `b`: {q0} ⟶ {q1} [q0→q1]
- Lee `a`: {q1} ⟶ {q3} [q1→q3]
- Lee `a`: {q3} ⟶ {q1} [q3→q1]
- Lee `b`: {q1} ⟶ {q0} [q1→q0]
- **Aceptada**: queda {q0} ∈ F.

## Cadena `bbaa`

- Inicio: {q0}
- Lee `b`: {q0} ⟶ {q1} [q0→q1]
- Lee `b`: {q1} ⟶ {q0} [q1→q0]
- Lee `a`: {q0} ⟶ {q2} [q0→q2]
- Lee `a`: {q2} ⟶ {q0} [q2→q0]
- **Aceptada**: queda {q0} ∈ F.

## Cadena `aabbaa`

- Inicio: {q0}
- Lee `a`: {q0} ⟶ {q2} [q0→q2]
- Lee `a`: {q2} ⟶ {q0} [q2→q0]
- Lee `b`: {q0} ⟶ {q1} [q0→q1]
- Lee `b`: {q1} ⟶ {q0} [q1→q0]
- Lee `a`: {q0} ⟶ {q2} [q0→q2]
- Lee `a`: {q2} ⟶ {q0} [q2→q0]
- **Aceptada**: queda {q0} ∈ F.

## Cadena `baabaa`

- Inicio: {q0}
- Lee `b`: {q0} ⟶ {q1} [q0→q1]
- Lee `a`: {q1} ⟶ {q3} [q1→q3]
- Lee `a`: {q3} ⟶ {q1} [q3→q1]
- Lee `b`: {q1} ⟶ {q0} [q1→q0]
- Lee `a`: {q0} ⟶ {q2} [q0→q2]
- Lee `a`: {q2} ⟶ {q0} [q2→q0]
- **Aceptada**: queda {q0} ∈ F.

## Cadena `a`

- Inicio: {q0}
- Lee `a`: {q0} ⟶ {q2} [q0→q2]
- **Rechazada**: ningún estado de {q2} es de aceptación.

## Cadena `ab`

- Inicio: {q0}
- Lee `a`: {q0} ⟶ {q2} [q0→q2]
- Lee `b`: {q2} ⟶ {q3} [q2→q3]
- **Rechazada**: ningún estado de {q3} es de aceptación.

## Cadena `baaa`

- Inicio: {q0}
- Lee `b`: {q0} ⟶ {q1} [q0→q1]
- Lee `a`: {q1} ⟶ {q3} [q1→q3]
- Lee `a`: {q3} ⟶ {q1} [q3→q1]
- Lee `a`: {q1} ⟶ {q3} [q1→q3]
- **Rechazada**: ningún estado de {q3} es de aceptación.

## Cadena `aabbab`

- Inicio: {q0}
- Lee `a`: {q0} ⟶ {q2} [q0→q2]
- Lee `a`: {q2} ⟶ {q0} [q2→q0]
- Lee `b`: {q0} ⟶ {q1} [q0→q1]
- Lee `b`: {q1} ⟶ {q0} [q1→q0]
- Lee `a`: {q0} ⟶ {q2} [q0→q2]
- Lee `b`: {q2} ⟶ {q3} [q2→q3]
- **Rechazada**: ningún estado de {q3} es de aceptación.

## Cadena `aaabbbbab`

- Inicio: {q0}
- Lee `a`: {q0} ⟶ {q2} [q0→q2]
- Lee `a`: {q2} ⟶ {q0} [q2→q0]
- Lee `a`: {q0} ⟶ {q2} [q0→q2]
- Lee `b`: {q2} ⟶ {q3} [q2→q3]
- Lee `b`: {q3} ⟶ {q2} [q3→q2]
- Lee `b`: {q2} ⟶ {q3} [q2→q3]
- Lee `b`: {q3} ⟶ {q2} [q3→q2]
- Lee `a`: {q2} ⟶ {q0} [q2→q0]
- Lee `b`: {q0} ⟶ {q1} [q0→q1]
- **Rechazada**: ningún estado de {q1} es de aceptación.
