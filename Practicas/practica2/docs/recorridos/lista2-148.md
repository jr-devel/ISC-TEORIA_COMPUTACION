# Recorridos: Lista 2 · Ejercicio 148

AFD del progreso de un alumno en Teoría de la Computación (convocatorias de febrero, septiembre y diciembre; Σ = {P, N, A, S}; no más de dos presentaciones por año; termina al aprobar).

Autómata: `lista2-148` (AFD).

## Cadena `PA`

- Inicio: {feb0}
- Lee `P`: {feb0} ⟶ {feb0?} [feb0→feb0?]
- Lee `A`: {feb0?} ⟶ {APROBADO} [feb0?→APROBADO]
- **Aceptada**: queda {APROBADO} ∈ F.

## Cadena `NPA`

- Inicio: {feb0}
- Lee `N`: {feb0} ⟶ {sep0} [feb0→sep0]
- Lee `P`: {sep0} ⟶ {sep0?} [sep0→sep0?]
- Lee `A`: {sep0?} ⟶ {APROBADO} [sep0?→APROBADO]
- **Aceptada**: queda {APROBADO} ∈ F.

## Cadena `NPSPA`

- Inicio: {feb0}
- Lee `N`: {feb0} ⟶ {sep0} [feb0→sep0]
- Lee `P`: {sep0} ⟶ {sep0?} [sep0→sep0?]
- Lee `S`: {sep0?} ⟶ {dic1} [sep0?→dic1]
- Lee `P`: {dic1} ⟶ {dic1?} [dic1→dic1?]
- Lee `A`: {dic1?} ⟶ {APROBADO} [dic1?→APROBADO]
- **Aceptada**: queda {APROBADO} ∈ F.

## Cadena `NPSPSPA`

- Inicio: {feb0}
- Lee `N`: {feb0} ⟶ {sep0} [feb0→sep0]
- Lee `P`: {sep0} ⟶ {sep0?} [sep0→sep0?]
- Lee `S`: {sep0?} ⟶ {dic1} [sep0?→dic1]
- Lee `P`: {dic1} ⟶ {dic1?} [dic1→dic1?]
- Lee `S`: {dic1?} ⟶ {feb0} [dic1?→feb0]
- Lee `P`: {feb0} ⟶ {feb0?} [feb0→feb0?]
- Lee `A`: {feb0?} ⟶ {APROBADO} [feb0?→APROBADO]
- **Aceptada**: queda {APROBADO} ∈ F.

## Cadena `NPSNPSNNPA`

- Inicio: {feb0}
- Lee `N`: {feb0} ⟶ {sep0} [feb0→sep0]
- Lee `P`: {sep0} ⟶ {sep0?} [sep0→sep0?]
- Lee `S`: {sep0?} ⟶ {dic1} [sep0?→dic1]
- Lee `N`: {dic1} ⟶ {feb0} [dic1→feb0]
- Lee `P`: {feb0} ⟶ {feb0?} [feb0→feb0?]
- Lee `S`: {feb0?} ⟶ {sep1} [feb0?→sep1]
- Lee `N`: {sep1} ⟶ {dic1} [sep1→dic1]
- Lee `N`: {dic1} ⟶ {feb0} [dic1→feb0]
- Lee `P`: {feb0} ⟶ {feb0?} [feb0→feb0?]
- Lee `A`: {feb0?} ⟶ {APROBADO} [feb0?→APROBADO]
- **Aceptada**: queda {APROBADO} ∈ F.

## Cadena λ

- Inicio: {feb0}
- **Rechazada**: ningún estado de {feb0} es de aceptación.

## Cadena `N`

- Inicio: {feb0}
- Lee `N`: {feb0} ⟶ {sep0} [feb0→sep0]
- **Rechazada**: ningún estado de {sep0} es de aceptación.

## Cadena `PAS`

- Inicio: {feb0}
- Lee `P`: {feb0} ⟶ {feb0?} [feb0→feb0?]
- Lee `A`: {feb0?} ⟶ {APROBADO} [feb0?→APROBADO]
- Lee `S`: {APROBADO} ⟶ {muerto} [APROBADO→muerto]
- **Rechazada**: ningún estado de {muerto} es de aceptación.

## Cadena `NAPAS`

- Inicio: {feb0}
- Lee `N`: {feb0} ⟶ {sep0} [feb0→sep0]
- Lee `A`: {sep0} ⟶ {muerto} [sep0→muerto]
- Lee `P`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `A`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `S`: {muerto} ⟶ {muerto} [muerto→muerto]
- **Rechazada**: ningún estado de {muerto} es de aceptación.

## Cadena `NNNPASAA`

- Inicio: {feb0}
- Lee `N`: {feb0} ⟶ {sep0} [feb0→sep0]
- Lee `N`: {sep0} ⟶ {dic0} [sep0→dic0]
- Lee `N`: {dic0} ⟶ {feb0} [dic0→feb0]
- Lee `P`: {feb0} ⟶ {feb0?} [feb0→feb0?]
- Lee `A`: {feb0?} ⟶ {APROBADO} [feb0?→APROBADO]
- Lee `S`: {APROBADO} ⟶ {muerto} [APROBADO→muerto]
- Lee `A`: {muerto} ⟶ {muerto} [muerto→muerto]
- Lee `A`: {muerto} ⟶ {muerto} [muerto→muerto]
- **Rechazada**: ningún estado de {muerto} es de aceptación.

## Cadena `P`

- Inicio: {feb0}
- Lee `P`: {feb0} ⟶ {feb0?} [feb0→feb0?]
- **Rechazada**: ningún estado de {feb0?} es de aceptación.
