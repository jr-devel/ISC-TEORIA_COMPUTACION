# Recorridos: Lista 3 · AFN del problema 104

AFN para el problema 104: Las palabras de Σ3 que inician con la cadena abbab.

Autómata: `lista3-afn-104` (AFD).

## Cadena `abbab`

- Inicio: {c0}
- Lee `a`: {c0} ⟶ {c1} [c0→c1]
- Lee `b`: {c1} ⟶ {c2} [c1→c2]
- Lee `b`: {c2} ⟶ {c3} [c2→c3]
- Lee `a`: {c3} ⟶ {c4} [c3→c4]
- Lee `b`: {c4} ⟶ {c5} [c4→c5]
- **Aceptada**: queda {c5} ∈ F.

## Cadena `abbaba`

- Inicio: {c0}
- Lee `a`: {c0} ⟶ {c1} [c0→c1]
- Lee `b`: {c1} ⟶ {c2} [c1→c2]
- Lee `b`: {c2} ⟶ {c3} [c2→c3]
- Lee `a`: {c3} ⟶ {c4} [c3→c4]
- Lee `b`: {c4} ⟶ {c5} [c4→c5]
- Lee `a`: {c5} ⟶ {c5} [c5→c5]
- **Aceptada**: queda {c5} ∈ F.

## Cadena `abbabbba`

- Inicio: {c0}
- Lee `a`: {c0} ⟶ {c1} [c0→c1]
- Lee `b`: {c1} ⟶ {c2} [c1→c2]
- Lee `b`: {c2} ⟶ {c3} [c2→c3]
- Lee `a`: {c3} ⟶ {c4} [c3→c4]
- Lee `b`: {c4} ⟶ {c5} [c4→c5]
- Lee `b`: {c5} ⟶ {c5} [c5→c5]
- Lee `b`: {c5} ⟶ {c5} [c5→c5]
- Lee `a`: {c5} ⟶ {c5} [c5→c5]
- **Aceptada**: queda {c5} ∈ F.

## Cadena `abbabbbabb`

- Inicio: {c0}
- Lee `a`: {c0} ⟶ {c1} [c0→c1]
- Lee `b`: {c1} ⟶ {c2} [c1→c2]
- Lee `b`: {c2} ⟶ {c3} [c2→c3]
- Lee `a`: {c3} ⟶ {c4} [c3→c4]
- Lee `b`: {c4} ⟶ {c5} [c4→c5]
- Lee `b`: {c5} ⟶ {c5} [c5→c5]
- Lee `b`: {c5} ⟶ {c5} [c5→c5]
- Lee `a`: {c5} ⟶ {c5} [c5→c5]
- Lee `b`: {c5} ⟶ {c5} [c5→c5]
- Lee `b`: {c5} ⟶ {c5} [c5→c5]
- **Aceptada**: queda {c5} ∈ F.

## Cadena `abbabababaaaa`

- Inicio: {c0}
- Lee `a`: {c0} ⟶ {c1} [c0→c1]
- Lee `b`: {c1} ⟶ {c2} [c1→c2]
- Lee `b`: {c2} ⟶ {c3} [c2→c3]
- Lee `a`: {c3} ⟶ {c4} [c3→c4]
- Lee `b`: {c4} ⟶ {c5} [c4→c5]
- Lee `a`: {c5} ⟶ {c5} [c5→c5]
- Lee `b`: {c5} ⟶ {c5} [c5→c5]
- Lee `a`: {c5} ⟶ {c5} [c5→c5]
- Lee `b`: {c5} ⟶ {c5} [c5→c5]
- Lee `a`: {c5} ⟶ {c5} [c5→c5]
- Lee `a`: {c5} ⟶ {c5} [c5→c5]
- Lee `a`: {c5} ⟶ {c5} [c5→c5]
- Lee `a`: {c5} ⟶ {c5} [c5→c5]
- **Aceptada**: queda {c5} ∈ F.

## Cadena λ

- Inicio: {c0}
- **Rechazada**: ningún estado de {c0} es de aceptación.

## Cadena `b`

- Inicio: {c0}
- Lee `b`: {c0} ⟶ ∅ [ninguna transición]
- **Rechazada**: no queda ningún estado activo.

## Cadena `bba`

- Inicio: {c0}
- Lee `b`: {c0} ⟶ ∅ [ninguna transición]
- Lee `b`: ∅ ⟶ ∅ [ninguna transición]
- Lee `a`: ∅ ⟶ ∅ [ninguna transición]
- **Rechazada**: no queda ningún estado activo.

## Cadena `baabb`

- Inicio: {c0}
- Lee `b`: {c0} ⟶ ∅ [ninguna transición]
- Lee `a`: ∅ ⟶ ∅ [ninguna transición]
- Lee `a`: ∅ ⟶ ∅ [ninguna transición]
- Lee `b`: ∅ ⟶ ∅ [ninguna transición]
- Lee `b`: ∅ ⟶ ∅ [ninguna transición]
- **Rechazada**: no queda ningún estado activo.

## Cadena `aabbbaba`

- Inicio: {c0}
- Lee `a`: {c0} ⟶ {c1} [c0→c1]
- Lee `a`: {c1} ⟶ ∅ [ninguna transición]
- Lee `b`: ∅ ⟶ ∅ [ninguna transición]
- Lee `b`: ∅ ⟶ ∅ [ninguna transición]
- Lee `b`: ∅ ⟶ ∅ [ninguna transición]
- Lee `a`: ∅ ⟶ ∅ [ninguna transición]
- Lee `b`: ∅ ⟶ ∅ [ninguna transición]
- Lee `a`: ∅ ⟶ ∅ [ninguna transición]
- **Rechazada**: no queda ningún estado activo.

## Cadena `abbb`

- Inicio: {c0}
- Lee `a`: {c0} ⟶ {c1} [c0→c1]
- Lee `b`: {c1} ⟶ {c2} [c1→c2]
- Lee `b`: {c2} ⟶ {c3} [c2→c3]
- Lee `b`: {c3} ⟶ ∅ [ninguna transición]
- **Rechazada**: no queda ningún estado activo.
