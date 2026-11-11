# Recorridos: Lista 3 · Ejercicio 238

Expresión regular sobre {0, 1} para: L = Σ³ ∪ Σ⁵.

Autómata: `lista3-238` (AFN-λ).

## Cadena `000`

- Inicio: {q4}; con cierre λ, {q4, q0, q2}
- Lee `0`: {q4, q0, q2} ⟶ {q1, q5, q10, q6, q8} [q0→q1]; cierre λ añade {q5, q10, q6, q8}
- Lee `0`: {q1, q5, q10, q6, q8} ⟶ {q7, q11, q16, q12, q14} [q6→q7]; cierre λ añade {q11, q16, q12, q14}
- Lee `0`: {q7, q11, q16, q12, q14} ⟶ {q13, q17, q32, q18, q19, q24, q20, q22, q33} [q12→q13]; cierre λ añade {q17, q32, q18, q19, q24, q20, q22, q33}
- **Aceptada**: queda {q33} ∈ F.

## Cadena `001`

- Inicio: {q4}; con cierre λ, {q4, q0, q2}
- Lee `0`: {q4, q0, q2} ⟶ {q1, q5, q10, q6, q8} [q0→q1]; cierre λ añade {q5, q10, q6, q8}
- Lee `0`: {q1, q5, q10, q6, q8} ⟶ {q7, q11, q16, q12, q14} [q6→q7]; cierre λ añade {q11, q16, q12, q14}
- Lee `1`: {q7, q11, q16, q12, q14} ⟶ {q15, q17, q32, q18, q19, q24, q20, q22, q33} [q14→q15]; cierre λ añade {q17, q32, q18, q19, q24, q20, q22, q33}
- **Aceptada**: queda {q33} ∈ F.

## Cadena `101`

- Inicio: {q4}; con cierre λ, {q4, q0, q2}
- Lee `1`: {q4, q0, q2} ⟶ {q3, q5, q10, q6, q8} [q2→q3]; cierre λ añade {q5, q10, q6, q8}
- Lee `0`: {q3, q5, q10, q6, q8} ⟶ {q7, q11, q16, q12, q14} [q6→q7]; cierre λ añade {q11, q16, q12, q14}
- Lee `1`: {q7, q11, q16, q12, q14} ⟶ {q15, q17, q32, q18, q19, q24, q20, q22, q33} [q14→q15]; cierre λ añade {q17, q32, q18, q19, q24, q20, q22, q33}
- **Aceptada**: queda {q33} ∈ F.

## Cadena `111`

- Inicio: {q4}; con cierre λ, {q4, q0, q2}
- Lee `1`: {q4, q0, q2} ⟶ {q3, q5, q10, q6, q8} [q2→q3]; cierre λ añade {q5, q10, q6, q8}
- Lee `1`: {q3, q5, q10, q6, q8} ⟶ {q9, q11, q16, q12, q14} [q8→q9]; cierre λ añade {q11, q16, q12, q14}
- Lee `1`: {q9, q11, q16, q12, q14} ⟶ {q15, q17, q32, q18, q19, q24, q20, q22, q33} [q14→q15]; cierre λ añade {q17, q32, q18, q19, q24, q20, q22, q33}
- **Aceptada**: queda {q33} ∈ F.

## Cadena `11100`

- Inicio: {q4}; con cierre λ, {q4, q0, q2}
- Lee `1`: {q4, q0, q2} ⟶ {q3, q5, q10, q6, q8} [q2→q3]; cierre λ añade {q5, q10, q6, q8}
- Lee `1`: {q3, q5, q10, q6, q8} ⟶ {q9, q11, q16, q12, q14} [q8→q9]; cierre λ añade {q11, q16, q12, q14}
- Lee `1`: {q9, q11, q16, q12, q14} ⟶ {q15, q17, q32, q18, q19, q24, q20, q22, q33} [q14→q15]; cierre λ añade {q17, q32, q18, q19, q24, q20, q22, q33}
- Lee `0`: {q15, q17, q32, q18, q19, q24, q20, q22, q33} ⟶ {q21, q25, q30, q26, q28} [q20→q21]; cierre λ añade {q25, q30, q26, q28}
- Lee `0`: {q21, q25, q30, q26, q28} ⟶ {q27, q31, q33} [q26→q27]; cierre λ añade {q31, q33}
- **Aceptada**: queda {q33} ∈ F.

## Cadena λ

- Inicio: {q4}; con cierre λ, {q4, q0, q2}
- **Rechazada**: ningún estado de {q4, q0, q2} es de aceptación.

## Cadena `0`

- Inicio: {q4}; con cierre λ, {q4, q0, q2}
- Lee `0`: {q4, q0, q2} ⟶ {q1, q5, q10, q6, q8} [q0→q1]; cierre λ añade {q5, q10, q6, q8}
- **Rechazada**: ningún estado de {q1, q5, q10, q6, q8} es de aceptación.

## Cadena `0100`

- Inicio: {q4}; con cierre λ, {q4, q0, q2}
- Lee `0`: {q4, q0, q2} ⟶ {q1, q5, q10, q6, q8} [q0→q1]; cierre λ añade {q5, q10, q6, q8}
- Lee `1`: {q1, q5, q10, q6, q8} ⟶ {q9, q11, q16, q12, q14} [q8→q9]; cierre λ añade {q11, q16, q12, q14}
- Lee `0`: {q9, q11, q16, q12, q14} ⟶ {q13, q17, q32, q18, q19, q24, q20, q22, q33} [q12→q13]; cierre λ añade {q17, q32, q18, q19, q24, q20, q22, q33}
- Lee `0`: {q13, q17, q32, q18, q19, q24, q20, q22, q33} ⟶ {q21, q25, q30, q26, q28} [q20→q21]; cierre λ añade {q25, q30, q26, q28}
- **Rechazada**: ningún estado de {q21, q25, q30, q26, q28} es de aceptación.

## Cadena `0111`

- Inicio: {q4}; con cierre λ, {q4, q0, q2}
- Lee `0`: {q4, q0, q2} ⟶ {q1, q5, q10, q6, q8} [q0→q1]; cierre λ añade {q5, q10, q6, q8}
- Lee `1`: {q1, q5, q10, q6, q8} ⟶ {q9, q11, q16, q12, q14} [q8→q9]; cierre λ añade {q11, q16, q12, q14}
- Lee `1`: {q9, q11, q16, q12, q14} ⟶ {q15, q17, q32, q18, q19, q24, q20, q22, q33} [q14→q15]; cierre λ añade {q17, q32, q18, q19, q24, q20, q22, q33}
- Lee `1`: {q15, q17, q32, q18, q19, q24, q20, q22, q33} ⟶ {q23, q25, q30, q26, q28} [q22→q23]; cierre λ añade {q25, q30, q26, q28}
- **Rechazada**: ningún estado de {q23, q25, q30, q26, q28} es de aceptación.

## Cadena `10100011101001`

- Inicio: {q4}; con cierre λ, {q4, q0, q2}
- Lee `1`: {q4, q0, q2} ⟶ {q3, q5, q10, q6, q8} [q2→q3]; cierre λ añade {q5, q10, q6, q8}
- Lee `0`: {q3, q5, q10, q6, q8} ⟶ {q7, q11, q16, q12, q14} [q6→q7]; cierre λ añade {q11, q16, q12, q14}
- Lee `1`: {q7, q11, q16, q12, q14} ⟶ {q15, q17, q32, q18, q19, q24, q20, q22, q33} [q14→q15]; cierre λ añade {q17, q32, q18, q19, q24, q20, q22, q33}
- Lee `0`: {q15, q17, q32, q18, q19, q24, q20, q22, q33} ⟶ {q21, q25, q30, q26, q28} [q20→q21]; cierre λ añade {q25, q30, q26, q28}
- Lee `0`: {q21, q25, q30, q26, q28} ⟶ {q27, q31, q33} [q26→q27]; cierre λ añade {q31, q33}
- Lee `0`: {q27, q31, q33} ⟶ ∅ [ninguna transición]
- Lee `1`: ∅ ⟶ ∅ [ninguna transición]
- Lee `1`: ∅ ⟶ ∅ [ninguna transición]
- Lee `1`: ∅ ⟶ ∅ [ninguna transición]
- Lee `0`: ∅ ⟶ ∅ [ninguna transición]
- Lee `1`: ∅ ⟶ ∅ [ninguna transición]
- Lee `0`: ∅ ⟶ ∅ [ninguna transición]
- Lee `0`: ∅ ⟶ ∅ [ninguna transición]
- Lee `1`: ∅ ⟶ ∅ [ninguna transición]
- **Rechazada**: no queda ningún estado activo.

## Cadena `00`

- Inicio: {q4}; con cierre λ, {q4, q0, q2}
- Lee `0`: {q4, q0, q2} ⟶ {q1, q5, q10, q6, q8} [q0→q1]; cierre λ añade {q5, q10, q6, q8}
- Lee `0`: {q1, q5, q10, q6, q8} ⟶ {q7, q11, q16, q12, q14} [q6→q7]; cierre λ añade {q11, q16, q12, q14}
- **Rechazada**: ningún estado de {q7, q11, q16, q12, q14} es de aceptación.
