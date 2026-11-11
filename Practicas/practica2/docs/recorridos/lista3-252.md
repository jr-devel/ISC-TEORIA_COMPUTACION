# Recorridos: Lista 3 · Ejercicio 252

AFN-λ equivalente a la expresión (0 + 1)*(00 + 11) + (00 + 11)(0 + 1)*.

Autómata: `lista3-252` (AFN-λ).

## Cadena `00`

- Inicio: {q36}; con cierre λ, {q36, q6, q4, q0, q2, q7, q16, q8, q12, q26, q18, q22}
- Lee `0`: {q36, q6, q4, q0, q2, q7, q16, q8, q12, q26, q18, q22} ⟶ {q4, q0, q1, q2, q5, q7, q16, q8, q9, q10, q12, q19, q20} [q0→q1, q18→q19, q8→q9]; cierre λ añade {q4, q0, q2, q5, q7, q16, q8, q10, q12, q20}
- Lee `0`: {q4, q0, q1, q2, q5, q7, q16, q8, q9, q10, q12, q19, q20} ⟶ {q4, q0, q1, q2, q5, q7, q16, q8, q9, q10, q11, q12, q17, q21, q27, q34, q32, q28, q30, q35, q37} [q0→q1, q10→q11, q20→q21, q8→q9]; cierre λ añade {q4, q0, q2, q5, q7, q16, q8, q10, q12, q17, q27, q34, q32, q28, q30, q35, q37}
- **Aceptada**: queda {q37} ∈ F.

## Cadena `110`

- Inicio: {q36}; con cierre λ, {q36, q6, q4, q0, q2, q7, q16, q8, q12, q26, q18, q22}
- Lee `1`: {q36, q6, q4, q0, q2, q7, q16, q8, q12, q26, q18, q22} ⟶ {q4, q0, q2, q3, q5, q7, q16, q8, q12, q13, q14, q23, q24} [q12→q13, q2→q3, q22→q23]; cierre λ añade {q4, q0, q2, q5, q7, q16, q8, q12, q14, q24}
- Lee `1`: {q4, q0, q2, q3, q5, q7, q16, q8, q12, q13, q14, q23, q24} ⟶ {q4, q0, q2, q3, q5, q7, q16, q8, q12, q13, q14, q15, q17, q25, q27, q34, q32, q28, q30, q35, q37} [q12→q13, q14→q15, q2→q3, q24→q25]; cierre λ añade {q4, q0, q2, q5, q7, q16, q8, q12, q14, q17, q27, q34, q32, q28, q30, q35, q37}
- Lee `0`: {q4, q0, q2, q3, q5, q7, q16, q8, q12, q13, q14, q15, q17, q25, q27, q34, q32, q28, q30, q35, q37} ⟶ {q4, q0, q1, q2, q5, q7, q16, q8, q9, q10, q12, q32, q28, q29, q30, q33, q35, q37} [q0→q1, q28→q29, q8→q9]; cierre λ añade {q4, q0, q2, q5, q7, q16, q8, q10, q12, q32, q28, q30, q33, q35, q37}
- **Aceptada**: queda {q37} ∈ F.

## Cadena `01111`

- Inicio: {q36}; con cierre λ, {q36, q6, q4, q0, q2, q7, q16, q8, q12, q26, q18, q22}
- Lee `0`: {q36, q6, q4, q0, q2, q7, q16, q8, q12, q26, q18, q22} ⟶ {q4, q0, q1, q2, q5, q7, q16, q8, q9, q10, q12, q19, q20} [q0→q1, q18→q19, q8→q9]; cierre λ añade {q4, q0, q2, q5, q7, q16, q8, q10, q12, q20}
- Lee `1`: {q4, q0, q1, q2, q5, q7, q16, q8, q9, q10, q12, q19, q20} ⟶ {q4, q0, q2, q3, q5, q7, q16, q8, q12, q13, q14} [q12→q13, q2→q3]; cierre λ añade {q4, q0, q2, q5, q7, q16, q8, q12, q14}
- Lee `1`: {q4, q0, q2, q3, q5, q7, q16, q8, q12, q13, q14} ⟶ {q4, q0, q2, q3, q5, q7, q16, q8, q12, q13, q14, q15, q17, q37} [q12→q13, q14→q15, q2→q3]; cierre λ añade {q4, q0, q2, q5, q7, q16, q8, q12, q14, q17, q37}
- Lee `1`: {q4, q0, q2, q3, q5, q7, q16, q8, q12, q13, q14, q15, q17, q37} ⟶ {q4, q0, q2, q3, q5, q7, q16, q8, q12, q13, q14, q15, q17, q37} [q12→q13, q14→q15, q2→q3]; cierre λ añade {q4, q0, q2, q5, q7, q16, q8, q12, q14, q17, q37}
- Lee `1`: {q4, q0, q2, q3, q5, q7, q16, q8, q12, q13, q14, q15, q17, q37} ⟶ {q4, q0, q2, q3, q5, q7, q16, q8, q12, q13, q14, q15, q17, q37} [q12→q13, q14→q15, q2→q3]; cierre λ añade {q4, q0, q2, q5, q7, q16, q8, q12, q14, q17, q37}
- **Aceptada**: queda {q37} ∈ F.

## Cadena `1101100`

- Inicio: {q36}; con cierre λ, {q36, q6, q4, q0, q2, q7, q16, q8, q12, q26, q18, q22}
- Lee `1`: {q36, q6, q4, q0, q2, q7, q16, q8, q12, q26, q18, q22} ⟶ {q4, q0, q2, q3, q5, q7, q16, q8, q12, q13, q14, q23, q24} [q12→q13, q2→q3, q22→q23]; cierre λ añade {q4, q0, q2, q5, q7, q16, q8, q12, q14, q24}
- Lee `1`: {q4, q0, q2, q3, q5, q7, q16, q8, q12, q13, q14, q23, q24} ⟶ {q4, q0, q2, q3, q5, q7, q16, q8, q12, q13, q14, q15, q17, q25, q27, q34, q32, q28, q30, q35, q37} [q12→q13, q14→q15, q2→q3, q24→q25]; cierre λ añade {q4, q0, q2, q5, q7, q16, q8, q12, q14, q17, q27, q34, q32, q28, q30, q35, q37}
- Lee `0`: {q4, q0, q2, q3, q5, q7, q16, q8, q12, q13, q14, q15, q17, q25, q27, q34, q32, q28, q30, q35, q37} ⟶ {q4, q0, q1, q2, q5, q7, q16, q8, q9, q10, q12, q32, q28, q29, q30, q33, q35, q37} [q0→q1, q28→q29, q8→q9]; cierre λ añade {q4, q0, q2, q5, q7, q16, q8, q10, q12, q32, q28, q30, q33, q35, q37}
- Lee `1`: {q4, q0, q1, q2, q5, q7, q16, q8, q9, q10, q12, q32, q28, q29, q30, q33, q35, q37} ⟶ {q4, q0, q2, q3, q5, q7, q16, q8, q12, q13, q14, q32, q28, q30, q31, q33, q35, q37} [q12→q13, q2→q3, q30→q31]; cierre λ añade {q4, q0, q2, q5, q7, q16, q8, q12, q14, q32, q28, q30, q33, q35, q37}
- Lee `1`: {q4, q0, q2, q3, q5, q7, q16, q8, q12, q13, q14, q32, q28, q30, q31, q33, q35, q37} ⟶ {q4, q0, q2, q3, q5, q7, q16, q8, q12, q13, q14, q15, q17, q32, q28, q30, q31, q33, q35, q37} [q12→q13, q14→q15, q2→q3, q30→q31]; cierre λ añade {q4, q0, q2, q5, q7, q16, q8, q12, q14, q17, q32, q28, q30, q33, q35, q37}
- Lee `0`: {q4, q0, q2, q3, q5, q7, q16, q8, q12, q13, q14, q15, q17, q32, q28, q30, q31, q33, q35, q37} ⟶ {q4, q0, q1, q2, q5, q7, q16, q8, q9, q10, q12, q32, q28, q29, q30, q33, q35, q37} [q0→q1, q28→q29, q8→q9]; cierre λ añade {q4, q0, q2, q5, q7, q16, q8, q10, q12, q32, q28, q30, q33, q35, q37}
- Lee `0`: {q4, q0, q1, q2, q5, q7, q16, q8, q9, q10, q12, q32, q28, q29, q30, q33, q35, q37} ⟶ {q4, q0, q1, q2, q5, q7, q16, q8, q9, q10, q11, q12, q17, q32, q28, q29, q30, q33, q35, q37} [q0→q1, q10→q11, q28→q29, q8→q9]; cierre λ añade {q4, q0, q2, q5, q7, q16, q8, q10, q12, q17, q32, q28, q30, q33, q35, q37}
- **Aceptada**: queda {q37} ∈ F.

## Cadena `0000100110`

- Inicio: {q36}; con cierre λ, {q36, q6, q4, q0, q2, q7, q16, q8, q12, q26, q18, q22}
- Lee `0`: {q36, q6, q4, q0, q2, q7, q16, q8, q12, q26, q18, q22} ⟶ {q4, q0, q1, q2, q5, q7, q16, q8, q9, q10, q12, q19, q20} [q0→q1, q18→q19, q8→q9]; cierre λ añade {q4, q0, q2, q5, q7, q16, q8, q10, q12, q20}
- Lee `0`: {q4, q0, q1, q2, q5, q7, q16, q8, q9, q10, q12, q19, q20} ⟶ {q4, q0, q1, q2, q5, q7, q16, q8, q9, q10, q11, q12, q17, q21, q27, q34, q32, q28, q30, q35, q37} [q0→q1, q10→q11, q20→q21, q8→q9]; cierre λ añade {q4, q0, q2, q5, q7, q16, q8, q10, q12, q17, q27, q34, q32, q28, q30, q35, q37}
- Lee `0`: {q4, q0, q1, q2, q5, q7, q16, q8, q9, q10, q11, q12, q17, q21, q27, q34, q32, q28, q30, q35, q37} ⟶ {q4, q0, q1, q2, q5, q7, q16, q8, q9, q10, q11, q12, q17, q32, q28, q29, q30, q33, q35, q37} [q0→q1, q10→q11, q28→q29, q8→q9]; cierre λ añade {q4, q0, q2, q5, q7, q16, q8, q10, q12, q17, q32, q28, q30, q33, q35, q37}
- Lee `0`: {q4, q0, q1, q2, q5, q7, q16, q8, q9, q10, q11, q12, q17, q32, q28, q29, q30, q33, q35, q37} ⟶ {q4, q0, q1, q2, q5, q7, q16, q8, q9, q10, q11, q12, q17, q32, q28, q29, q30, q33, q35, q37} [q0→q1, q10→q11, q28→q29, q8→q9]; cierre λ añade {q4, q0, q2, q5, q7, q16, q8, q10, q12, q17, q32, q28, q30, q33, q35, q37}
- Lee `1`: {q4, q0, q1, q2, q5, q7, q16, q8, q9, q10, q11, q12, q17, q32, q28, q29, q30, q33, q35, q37} ⟶ {q4, q0, q2, q3, q5, q7, q16, q8, q12, q13, q14, q32, q28, q30, q31, q33, q35, q37} [q12→q13, q2→q3, q30→q31]; cierre λ añade {q4, q0, q2, q5, q7, q16, q8, q12, q14, q32, q28, q30, q33, q35, q37}
- Lee `0`: {q4, q0, q2, q3, q5, q7, q16, q8, q12, q13, q14, q32, q28, q30, q31, q33, q35, q37} ⟶ {q4, q0, q1, q2, q5, q7, q16, q8, q9, q10, q12, q32, q28, q29, q30, q33, q35, q37} [q0→q1, q28→q29, q8→q9]; cierre λ añade {q4, q0, q2, q5, q7, q16, q8, q10, q12, q32, q28, q30, q33, q35, q37}
- Lee `0`: {q4, q0, q1, q2, q5, q7, q16, q8, q9, q10, q12, q32, q28, q29, q30, q33, q35, q37} ⟶ {q4, q0, q1, q2, q5, q7, q16, q8, q9, q10, q11, q12, q17, q32, q28, q29, q30, q33, q35, q37} [q0→q1, q10→q11, q28→q29, q8→q9]; cierre λ añade {q4, q0, q2, q5, q7, q16, q8, q10, q12, q17, q32, q28, q30, q33, q35, q37}
- Lee `1`: {q4, q0, q1, q2, q5, q7, q16, q8, q9, q10, q11, q12, q17, q32, q28, q29, q30, q33, q35, q37} ⟶ {q4, q0, q2, q3, q5, q7, q16, q8, q12, q13, q14, q32, q28, q30, q31, q33, q35, q37} [q12→q13, q2→q3, q30→q31]; cierre λ añade {q4, q0, q2, q5, q7, q16, q8, q12, q14, q32, q28, q30, q33, q35, q37}
- Lee `1`: {q4, q0, q2, q3, q5, q7, q16, q8, q12, q13, q14, q32, q28, q30, q31, q33, q35, q37} ⟶ {q4, q0, q2, q3, q5, q7, q16, q8, q12, q13, q14, q15, q17, q32, q28, q30, q31, q33, q35, q37} [q12→q13, q14→q15, q2→q3, q30→q31]; cierre λ añade {q4, q0, q2, q5, q7, q16, q8, q12, q14, q17, q32, q28, q30, q33, q35, q37}
- Lee `0`: {q4, q0, q2, q3, q5, q7, q16, q8, q12, q13, q14, q15, q17, q32, q28, q30, q31, q33, q35, q37} ⟶ {q4, q0, q1, q2, q5, q7, q16, q8, q9, q10, q12, q32, q28, q29, q30, q33, q35, q37} [q0→q1, q28→q29, q8→q9]; cierre λ añade {q4, q0, q2, q5, q7, q16, q8, q10, q12, q32, q28, q30, q33, q35, q37}
- **Aceptada**: queda {q37} ∈ F.

## Cadena λ

- Inicio: {q36}; con cierre λ, {q36, q6, q4, q0, q2, q7, q16, q8, q12, q26, q18, q22}
- **Rechazada**: ningún estado de {q36, q6, q4, q0, q2, q7, q16, q8, q12, q26, q18, q22} es de aceptación.

## Cadena `1`

- Inicio: {q36}; con cierre λ, {q36, q6, q4, q0, q2, q7, q16, q8, q12, q26, q18, q22}
- Lee `1`: {q36, q6, q4, q0, q2, q7, q16, q8, q12, q26, q18, q22} ⟶ {q4, q0, q2, q3, q5, q7, q16, q8, q12, q13, q14, q23, q24} [q12→q13, q2→q3, q22→q23]; cierre λ añade {q4, q0, q2, q5, q7, q16, q8, q12, q14, q24}
- **Rechazada**: ningún estado de {q4, q0, q2, q3, q5, q7, q16, q8, q12, q13, q14, q23, q24} es de aceptación.

## Cadena `010`

- Inicio: {q36}; con cierre λ, {q36, q6, q4, q0, q2, q7, q16, q8, q12, q26, q18, q22}
- Lee `0`: {q36, q6, q4, q0, q2, q7, q16, q8, q12, q26, q18, q22} ⟶ {q4, q0, q1, q2, q5, q7, q16, q8, q9, q10, q12, q19, q20} [q0→q1, q18→q19, q8→q9]; cierre λ añade {q4, q0, q2, q5, q7, q16, q8, q10, q12, q20}
- Lee `1`: {q4, q0, q1, q2, q5, q7, q16, q8, q9, q10, q12, q19, q20} ⟶ {q4, q0, q2, q3, q5, q7, q16, q8, q12, q13, q14} [q12→q13, q2→q3]; cierre λ añade {q4, q0, q2, q5, q7, q16, q8, q12, q14}
- Lee `0`: {q4, q0, q2, q3, q5, q7, q16, q8, q12, q13, q14} ⟶ {q4, q0, q1, q2, q5, q7, q16, q8, q9, q10, q12} [q0→q1, q8→q9]; cierre λ añade {q4, q0, q2, q5, q7, q16, q8, q10, q12}
- **Rechazada**: ningún estado de {q4, q0, q1, q2, q5, q7, q16, q8, q9, q10, q12} es de aceptación.

## Cadena `01001`

- Inicio: {q36}; con cierre λ, {q36, q6, q4, q0, q2, q7, q16, q8, q12, q26, q18, q22}
- Lee `0`: {q36, q6, q4, q0, q2, q7, q16, q8, q12, q26, q18, q22} ⟶ {q4, q0, q1, q2, q5, q7, q16, q8, q9, q10, q12, q19, q20} [q0→q1, q18→q19, q8→q9]; cierre λ añade {q4, q0, q2, q5, q7, q16, q8, q10, q12, q20}
- Lee `1`: {q4, q0, q1, q2, q5, q7, q16, q8, q9, q10, q12, q19, q20} ⟶ {q4, q0, q2, q3, q5, q7, q16, q8, q12, q13, q14} [q12→q13, q2→q3]; cierre λ añade {q4, q0, q2, q5, q7, q16, q8, q12, q14}
- Lee `0`: {q4, q0, q2, q3, q5, q7, q16, q8, q12, q13, q14} ⟶ {q4, q0, q1, q2, q5, q7, q16, q8, q9, q10, q12} [q0→q1, q8→q9]; cierre λ añade {q4, q0, q2, q5, q7, q16, q8, q10, q12}
- Lee `0`: {q4, q0, q1, q2, q5, q7, q16, q8, q9, q10, q12} ⟶ {q4, q0, q1, q2, q5, q7, q16, q8, q9, q10, q11, q12, q17, q37} [q0→q1, q10→q11, q8→q9]; cierre λ añade {q4, q0, q2, q5, q7, q16, q8, q10, q12, q17, q37}
- Lee `1`: {q4, q0, q1, q2, q5, q7, q16, q8, q9, q10, q11, q12, q17, q37} ⟶ {q4, q0, q2, q3, q5, q7, q16, q8, q12, q13, q14} [q12→q13, q2→q3]; cierre λ añade {q4, q0, q2, q5, q7, q16, q8, q12, q14}
- **Rechazada**: ningún estado de {q4, q0, q2, q3, q5, q7, q16, q8, q12, q13, q14} es de aceptación.

## Cadena `01110101`

- Inicio: {q36}; con cierre λ, {q36, q6, q4, q0, q2, q7, q16, q8, q12, q26, q18, q22}
- Lee `0`: {q36, q6, q4, q0, q2, q7, q16, q8, q12, q26, q18, q22} ⟶ {q4, q0, q1, q2, q5, q7, q16, q8, q9, q10, q12, q19, q20} [q0→q1, q18→q19, q8→q9]; cierre λ añade {q4, q0, q2, q5, q7, q16, q8, q10, q12, q20}
- Lee `1`: {q4, q0, q1, q2, q5, q7, q16, q8, q9, q10, q12, q19, q20} ⟶ {q4, q0, q2, q3, q5, q7, q16, q8, q12, q13, q14} [q12→q13, q2→q3]; cierre λ añade {q4, q0, q2, q5, q7, q16, q8, q12, q14}
- Lee `1`: {q4, q0, q2, q3, q5, q7, q16, q8, q12, q13, q14} ⟶ {q4, q0, q2, q3, q5, q7, q16, q8, q12, q13, q14, q15, q17, q37} [q12→q13, q14→q15, q2→q3]; cierre λ añade {q4, q0, q2, q5, q7, q16, q8, q12, q14, q17, q37}
- Lee `1`: {q4, q0, q2, q3, q5, q7, q16, q8, q12, q13, q14, q15, q17, q37} ⟶ {q4, q0, q2, q3, q5, q7, q16, q8, q12, q13, q14, q15, q17, q37} [q12→q13, q14→q15, q2→q3]; cierre λ añade {q4, q0, q2, q5, q7, q16, q8, q12, q14, q17, q37}
- Lee `0`: {q4, q0, q2, q3, q5, q7, q16, q8, q12, q13, q14, q15, q17, q37} ⟶ {q4, q0, q1, q2, q5, q7, q16, q8, q9, q10, q12} [q0→q1, q8→q9]; cierre λ añade {q4, q0, q2, q5, q7, q16, q8, q10, q12}
- Lee `1`: {q4, q0, q1, q2, q5, q7, q16, q8, q9, q10, q12} ⟶ {q4, q0, q2, q3, q5, q7, q16, q8, q12, q13, q14} [q12→q13, q2→q3]; cierre λ añade {q4, q0, q2, q5, q7, q16, q8, q12, q14}
- Lee `0`: {q4, q0, q2, q3, q5, q7, q16, q8, q12, q13, q14} ⟶ {q4, q0, q1, q2, q5, q7, q16, q8, q9, q10, q12} [q0→q1, q8→q9]; cierre λ añade {q4, q0, q2, q5, q7, q16, q8, q10, q12}
- Lee `1`: {q4, q0, q1, q2, q5, q7, q16, q8, q9, q10, q12} ⟶ {q4, q0, q2, q3, q5, q7, q16, q8, q12, q13, q14} [q12→q13, q2→q3]; cierre λ añade {q4, q0, q2, q5, q7, q16, q8, q12, q14}
- **Rechazada**: ningún estado de {q4, q0, q2, q3, q5, q7, q16, q8, q12, q13, q14} es de aceptación.
