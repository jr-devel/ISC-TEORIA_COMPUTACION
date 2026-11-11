# Recorridos: Lista 2 · Ejercicio 145

AFD que lee un número binario de derecha a izquierda e identifica los múltiplos de 5.

Autómata: `lista2-145` (AFD).

## Cadena `0`

- Inicio: {ini}
- Lee `0`: {ini} ⟶ {t0} [ini→t0]
- **Aceptada**: queda {t0} ∈ F.

## Cadena `00`

- Inicio: {ini}
- Lee `0`: {ini} ⟶ {t0} [ini→t0]
- Lee `0`: {t0} ⟶ {t0} [t0→t0]
- **Aceptada**: queda {t0} ∈ F.

## Cadena `1111`

- Inicio: {ini}
- Lee `1`: {ini} ⟶ {t2} [ini→t2]
- Lee `1`: {t2} ⟶ {t3} [t2→t3]
- Lee `1`: {t3} ⟶ {t1} [t3→t1]
- Lee `1`: {t1} ⟶ {t0} [t1→t0]
- **Aceptada**: queda {t0} ∈ F.

## Cadena `000000`

- Inicio: {ini}
- Lee `0`: {ini} ⟶ {t0} [ini→t0]
- Lee `0`: {t0} ⟶ {t0} [t0→t0]
- Lee `0`: {t0} ⟶ {t0} [t0→t0]
- Lee `0`: {t0} ⟶ {t0} [t0→t0]
- Lee `0`: {t0} ⟶ {t0} [t0→t0]
- Lee `0`: {t0} ⟶ {t0} [t0→t0]
- **Aceptada**: queda {t0} ∈ F.

## Cadena `001010000`

- Inicio: {ini}
- Lee `0`: {ini} ⟶ {t0} [ini→t0]
- Lee `0`: {t0} ⟶ {t0} [t0→t0]
- Lee `1`: {t0} ⟶ {t2} [t0→t2]
- Lee `0`: {t2} ⟶ {t1} [t2→t1]
- Lee `1`: {t1} ⟶ {t0} [t1→t0]
- Lee `0`: {t0} ⟶ {t0} [t0→t0]
- Lee `0`: {t0} ⟶ {t0} [t0→t0]
- Lee `0`: {t0} ⟶ {t0} [t0→t0]
- Lee `0`: {t0} ⟶ {t0} [t0→t0]
- **Aceptada**: queda {t0} ∈ F.

## Cadena λ

- Inicio: {ini}
- **Rechazada**: ningún estado de {ini} es de aceptación.

## Cadena `1`

- Inicio: {ini}
- Lee `1`: {ini} ⟶ {t2} [ini→t2]
- **Rechazada**: ningún estado de {t2} es de aceptación.

## Cadena `111`

- Inicio: {ini}
- Lee `1`: {ini} ⟶ {t2} [ini→t2]
- Lee `1`: {t2} ⟶ {t3} [t2→t3]
- Lee `1`: {t3} ⟶ {t1} [t3→t1]
- **Rechazada**: ningún estado de {t1} es de aceptación.

## Cadena `01110`

- Inicio: {ini}
- Lee `0`: {ini} ⟶ {t0} [ini→t0]
- Lee `1`: {t0} ⟶ {t2} [t0→t2]
- Lee `1`: {t2} ⟶ {t3} [t2→t3]
- Lee `1`: {t3} ⟶ {t1} [t3→t1]
- Lee `0`: {t1} ⟶ {t3} [t1→t3]
- **Rechazada**: ningún estado de {t3} es de aceptación.

## Cadena `01000111`

- Inicio: {ini}
- Lee `0`: {ini} ⟶ {t0} [ini→t0]
- Lee `1`: {t0} ⟶ {t2} [t0→t2]
- Lee `0`: {t2} ⟶ {t1} [t2→t1]
- Lee `0`: {t1} ⟶ {t3} [t1→t3]
- Lee `0`: {t3} ⟶ {t4} [t3→t4]
- Lee `1`: {t4} ⟶ {t4} [t4→t4]
- Lee `1`: {t4} ⟶ {t4} [t4→t4]
- Lee `1`: {t4} ⟶ {t4} [t4→t4]
- **Rechazada**: ningún estado de {t4} es de aceptación.
