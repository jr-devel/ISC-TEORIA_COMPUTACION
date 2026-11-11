# Recorridos: Lista 3 · Ejercicio 239

Expresión regular sobre {0, 1} para: Cadenas que comienzan con 01 o terminan con 10.

Autómata: `lista3-239` (AFN-λ).

## Cadena `01`

- Inicio: {q24}; con cierre λ, {q24, q0, q18, q16, q12, q14, q19, q20}
- Lee `0`: {q24, q0, q18, q16, q12, q14, q19, q20} ⟶ {q1, q2, q16, q12, q13, q14, q17, q19, q20} [q0→q1, q12→q13]; cierre λ añade {q2, q16, q12, q14, q17, q19, q20}
- Lee `1`: {q1, q2, q16, q12, q13, q14, q17, q19, q20} ⟶ {q3, q10, q8, q4, q6, q11, q16, q12, q14, q15, q17, q19, q20, q21, q22, q25} [q14→q15, q2→q3, q20→q21]; cierre λ añade {q10, q8, q4, q6, q11, q16, q12, q14, q17, q19, q20, q22, q25}
- **Aceptada**: queda {q25} ∈ F.

## Cadena `010`

- Inicio: {q24}; con cierre λ, {q24, q0, q18, q16, q12, q14, q19, q20}
- Lee `0`: {q24, q0, q18, q16, q12, q14, q19, q20} ⟶ {q1, q2, q16, q12, q13, q14, q17, q19, q20} [q0→q1, q12→q13]; cierre λ añade {q2, q16, q12, q14, q17, q19, q20}
- Lee `1`: {q1, q2, q16, q12, q13, q14, q17, q19, q20} ⟶ {q3, q10, q8, q4, q6, q11, q16, q12, q14, q15, q17, q19, q20, q21, q22, q25} [q14→q15, q2→q3, q20→q21]; cierre λ añade {q10, q8, q4, q6, q11, q16, q12, q14, q17, q19, q20, q22, q25}
- Lee `0`: {q3, q10, q8, q4, q6, q11, q16, q12, q14, q15, q17, q19, q20, q21, q22, q25} ⟶ {q8, q4, q5, q6, q9, q11, q16, q12, q13, q14, q17, q19, q20, q23, q25} [q12→q13, q22→q23, q4→q5]; cierre λ añade {q8, q4, q6, q9, q11, q16, q12, q14, q17, q19, q20, q25}
- **Aceptada**: queda {q25} ∈ F.

## Cadena `10010`

- Inicio: {q24}; con cierre λ, {q24, q0, q18, q16, q12, q14, q19, q20}
- Lee `1`: {q24, q0, q18, q16, q12, q14, q19, q20} ⟶ {q16, q12, q14, q15, q17, q19, q20, q21, q22} [q14→q15, q20→q21]; cierre λ añade {q16, q12, q14, q17, q19, q20, q22}
- Lee `0`: {q16, q12, q14, q15, q17, q19, q20, q21, q22} ⟶ {q16, q12, q13, q14, q17, q19, q20, q23, q25} [q12→q13, q22→q23]; cierre λ añade {q16, q12, q14, q17, q19, q20, q25}
- Lee `0`: {q16, q12, q13, q14, q17, q19, q20, q23, q25} ⟶ {q16, q12, q13, q14, q17, q19, q20} [q12→q13]; cierre λ añade {q16, q12, q14, q17, q19, q20}
- Lee `1`: {q16, q12, q13, q14, q17, q19, q20} ⟶ {q16, q12, q14, q15, q17, q19, q20, q21, q22} [q14→q15, q20→q21]; cierre λ añade {q16, q12, q14, q17, q19, q20, q22}
- Lee `0`: {q16, q12, q14, q15, q17, q19, q20, q21, q22} ⟶ {q16, q12, q13, q14, q17, q19, q20, q23, q25} [q12→q13, q22→q23]; cierre λ añade {q16, q12, q14, q17, q19, q20, q25}
- **Aceptada**: queda {q25} ∈ F.

## Cadena `0100101`

- Inicio: {q24}; con cierre λ, {q24, q0, q18, q16, q12, q14, q19, q20}
- Lee `0`: {q24, q0, q18, q16, q12, q14, q19, q20} ⟶ {q1, q2, q16, q12, q13, q14, q17, q19, q20} [q0→q1, q12→q13]; cierre λ añade {q2, q16, q12, q14, q17, q19, q20}
- Lee `1`: {q1, q2, q16, q12, q13, q14, q17, q19, q20} ⟶ {q3, q10, q8, q4, q6, q11, q16, q12, q14, q15, q17, q19, q20, q21, q22, q25} [q14→q15, q2→q3, q20→q21]; cierre λ añade {q10, q8, q4, q6, q11, q16, q12, q14, q17, q19, q20, q22, q25}
- Lee `0`: {q3, q10, q8, q4, q6, q11, q16, q12, q14, q15, q17, q19, q20, q21, q22, q25} ⟶ {q8, q4, q5, q6, q9, q11, q16, q12, q13, q14, q17, q19, q20, q23, q25} [q12→q13, q22→q23, q4→q5]; cierre λ añade {q8, q4, q6, q9, q11, q16, q12, q14, q17, q19, q20, q25}
- Lee `0`: {q8, q4, q5, q6, q9, q11, q16, q12, q13, q14, q17, q19, q20, q23, q25} ⟶ {q8, q4, q5, q6, q9, q11, q16, q12, q13, q14, q17, q19, q20, q25} [q12→q13, q4→q5]; cierre λ añade {q8, q4, q6, q9, q11, q16, q12, q14, q17, q19, q20, q25}
- Lee `1`: {q8, q4, q5, q6, q9, q11, q16, q12, q13, q14, q17, q19, q20, q25} ⟶ {q8, q4, q6, q7, q9, q11, q16, q12, q14, q15, q17, q19, q20, q21, q22, q25} [q14→q15, q20→q21, q6→q7]; cierre λ añade {q8, q4, q6, q9, q11, q16, q12, q14, q17, q19, q20, q22, q25}
- Lee `0`: {q8, q4, q6, q7, q9, q11, q16, q12, q14, q15, q17, q19, q20, q21, q22, q25} ⟶ {q8, q4, q5, q6, q9, q11, q16, q12, q13, q14, q17, q19, q20, q23, q25} [q12→q13, q22→q23, q4→q5]; cierre λ añade {q8, q4, q6, q9, q11, q16, q12, q14, q17, q19, q20, q25}
- Lee `1`: {q8, q4, q5, q6, q9, q11, q16, q12, q13, q14, q17, q19, q20, q23, q25} ⟶ {q8, q4, q6, q7, q9, q11, q16, q12, q14, q15, q17, q19, q20, q21, q22, q25} [q14→q15, q20→q21, q6→q7]; cierre λ añade {q8, q4, q6, q9, q11, q16, q12, q14, q17, q19, q20, q22, q25}
- **Aceptada**: queda {q25} ∈ F.

## Cadena `0110110001`

- Inicio: {q24}; con cierre λ, {q24, q0, q18, q16, q12, q14, q19, q20}
- Lee `0`: {q24, q0, q18, q16, q12, q14, q19, q20} ⟶ {q1, q2, q16, q12, q13, q14, q17, q19, q20} [q0→q1, q12→q13]; cierre λ añade {q2, q16, q12, q14, q17, q19, q20}
- Lee `1`: {q1, q2, q16, q12, q13, q14, q17, q19, q20} ⟶ {q3, q10, q8, q4, q6, q11, q16, q12, q14, q15, q17, q19, q20, q21, q22, q25} [q14→q15, q2→q3, q20→q21]; cierre λ añade {q10, q8, q4, q6, q11, q16, q12, q14, q17, q19, q20, q22, q25}
- Lee `1`: {q3, q10, q8, q4, q6, q11, q16, q12, q14, q15, q17, q19, q20, q21, q22, q25} ⟶ {q8, q4, q6, q7, q9, q11, q16, q12, q14, q15, q17, q19, q20, q21, q22, q25} [q14→q15, q20→q21, q6→q7]; cierre λ añade {q8, q4, q6, q9, q11, q16, q12, q14, q17, q19, q20, q22, q25}
- Lee `0`: {q8, q4, q6, q7, q9, q11, q16, q12, q14, q15, q17, q19, q20, q21, q22, q25} ⟶ {q8, q4, q5, q6, q9, q11, q16, q12, q13, q14, q17, q19, q20, q23, q25} [q12→q13, q22→q23, q4→q5]; cierre λ añade {q8, q4, q6, q9, q11, q16, q12, q14, q17, q19, q20, q25}
- Lee `1`: {q8, q4, q5, q6, q9, q11, q16, q12, q13, q14, q17, q19, q20, q23, q25} ⟶ {q8, q4, q6, q7, q9, q11, q16, q12, q14, q15, q17, q19, q20, q21, q22, q25} [q14→q15, q20→q21, q6→q7]; cierre λ añade {q8, q4, q6, q9, q11, q16, q12, q14, q17, q19, q20, q22, q25}
- Lee `1`: {q8, q4, q6, q7, q9, q11, q16, q12, q14, q15, q17, q19, q20, q21, q22, q25} ⟶ {q8, q4, q6, q7, q9, q11, q16, q12, q14, q15, q17, q19, q20, q21, q22, q25} [q14→q15, q20→q21, q6→q7]; cierre λ añade {q8, q4, q6, q9, q11, q16, q12, q14, q17, q19, q20, q22, q25}
- Lee `0`: {q8, q4, q6, q7, q9, q11, q16, q12, q14, q15, q17, q19, q20, q21, q22, q25} ⟶ {q8, q4, q5, q6, q9, q11, q16, q12, q13, q14, q17, q19, q20, q23, q25} [q12→q13, q22→q23, q4→q5]; cierre λ añade {q8, q4, q6, q9, q11, q16, q12, q14, q17, q19, q20, q25}
- Lee `0`: {q8, q4, q5, q6, q9, q11, q16, q12, q13, q14, q17, q19, q20, q23, q25} ⟶ {q8, q4, q5, q6, q9, q11, q16, q12, q13, q14, q17, q19, q20, q25} [q12→q13, q4→q5]; cierre λ añade {q8, q4, q6, q9, q11, q16, q12, q14, q17, q19, q20, q25}
- Lee `0`: {q8, q4, q5, q6, q9, q11, q16, q12, q13, q14, q17, q19, q20, q25} ⟶ {q8, q4, q5, q6, q9, q11, q16, q12, q13, q14, q17, q19, q20, q25} [q12→q13, q4→q5]; cierre λ añade {q8, q4, q6, q9, q11, q16, q12, q14, q17, q19, q20, q25}
- Lee `1`: {q8, q4, q5, q6, q9, q11, q16, q12, q13, q14, q17, q19, q20, q25} ⟶ {q8, q4, q6, q7, q9, q11, q16, q12, q14, q15, q17, q19, q20, q21, q22, q25} [q14→q15, q20→q21, q6→q7]; cierre λ añade {q8, q4, q6, q9, q11, q16, q12, q14, q17, q19, q20, q22, q25}
- **Aceptada**: queda {q25} ∈ F.

## Cadena λ

- Inicio: {q24}; con cierre λ, {q24, q0, q18, q16, q12, q14, q19, q20}
- **Rechazada**: ningún estado de {q24, q0, q18, q16, q12, q14, q19, q20} es de aceptación.

## Cadena `0`

- Inicio: {q24}; con cierre λ, {q24, q0, q18, q16, q12, q14, q19, q20}
- Lee `0`: {q24, q0, q18, q16, q12, q14, q19, q20} ⟶ {q1, q2, q16, q12, q13, q14, q17, q19, q20} [q0→q1, q12→q13]; cierre λ añade {q2, q16, q12, q14, q17, q19, q20}
- **Rechazada**: ningún estado de {q1, q2, q16, q12, q13, q14, q17, q19, q20} es de aceptación.

## Cadena `001`

- Inicio: {q24}; con cierre λ, {q24, q0, q18, q16, q12, q14, q19, q20}
- Lee `0`: {q24, q0, q18, q16, q12, q14, q19, q20} ⟶ {q1, q2, q16, q12, q13, q14, q17, q19, q20} [q0→q1, q12→q13]; cierre λ añade {q2, q16, q12, q14, q17, q19, q20}
- Lee `0`: {q1, q2, q16, q12, q13, q14, q17, q19, q20} ⟶ {q16, q12, q13, q14, q17, q19, q20} [q12→q13]; cierre λ añade {q16, q12, q14, q17, q19, q20}
- Lee `1`: {q16, q12, q13, q14, q17, q19, q20} ⟶ {q16, q12, q14, q15, q17, q19, q20, q21, q22} [q14→q15, q20→q21]; cierre λ añade {q16, q12, q14, q17, q19, q20, q22}
- **Rechazada**: ningún estado de {q16, q12, q14, q15, q17, q19, q20, q21, q22} es de aceptación.

## Cadena `11011`

- Inicio: {q24}; con cierre λ, {q24, q0, q18, q16, q12, q14, q19, q20}
- Lee `1`: {q24, q0, q18, q16, q12, q14, q19, q20} ⟶ {q16, q12, q14, q15, q17, q19, q20, q21, q22} [q14→q15, q20→q21]; cierre λ añade {q16, q12, q14, q17, q19, q20, q22}
- Lee `1`: {q16, q12, q14, q15, q17, q19, q20, q21, q22} ⟶ {q16, q12, q14, q15, q17, q19, q20, q21, q22} [q14→q15, q20→q21]; cierre λ añade {q16, q12, q14, q17, q19, q20, q22}
- Lee `0`: {q16, q12, q14, q15, q17, q19, q20, q21, q22} ⟶ {q16, q12, q13, q14, q17, q19, q20, q23, q25} [q12→q13, q22→q23]; cierre λ añade {q16, q12, q14, q17, q19, q20, q25}
- Lee `1`: {q16, q12, q13, q14, q17, q19, q20, q23, q25} ⟶ {q16, q12, q14, q15, q17, q19, q20, q21, q22} [q14→q15, q20→q21]; cierre λ añade {q16, q12, q14, q17, q19, q20, q22}
- Lee `1`: {q16, q12, q14, q15, q17, q19, q20, q21, q22} ⟶ {q16, q12, q14, q15, q17, q19, q20, q21, q22} [q14→q15, q20→q21]; cierre λ añade {q16, q12, q14, q17, q19, q20, q22}
- **Rechazada**: ningún estado de {q16, q12, q14, q15, q17, q19, q20, q21, q22} es de aceptación.

## Cadena `10101001`

- Inicio: {q24}; con cierre λ, {q24, q0, q18, q16, q12, q14, q19, q20}
- Lee `1`: {q24, q0, q18, q16, q12, q14, q19, q20} ⟶ {q16, q12, q14, q15, q17, q19, q20, q21, q22} [q14→q15, q20→q21]; cierre λ añade {q16, q12, q14, q17, q19, q20, q22}
- Lee `0`: {q16, q12, q14, q15, q17, q19, q20, q21, q22} ⟶ {q16, q12, q13, q14, q17, q19, q20, q23, q25} [q12→q13, q22→q23]; cierre λ añade {q16, q12, q14, q17, q19, q20, q25}
- Lee `1`: {q16, q12, q13, q14, q17, q19, q20, q23, q25} ⟶ {q16, q12, q14, q15, q17, q19, q20, q21, q22} [q14→q15, q20→q21]; cierre λ añade {q16, q12, q14, q17, q19, q20, q22}
- Lee `0`: {q16, q12, q14, q15, q17, q19, q20, q21, q22} ⟶ {q16, q12, q13, q14, q17, q19, q20, q23, q25} [q12→q13, q22→q23]; cierre λ añade {q16, q12, q14, q17, q19, q20, q25}
- Lee `1`: {q16, q12, q13, q14, q17, q19, q20, q23, q25} ⟶ {q16, q12, q14, q15, q17, q19, q20, q21, q22} [q14→q15, q20→q21]; cierre λ añade {q16, q12, q14, q17, q19, q20, q22}
- Lee `0`: {q16, q12, q14, q15, q17, q19, q20, q21, q22} ⟶ {q16, q12, q13, q14, q17, q19, q20, q23, q25} [q12→q13, q22→q23]; cierre λ añade {q16, q12, q14, q17, q19, q20, q25}
- Lee `0`: {q16, q12, q13, q14, q17, q19, q20, q23, q25} ⟶ {q16, q12, q13, q14, q17, q19, q20} [q12→q13]; cierre λ añade {q16, q12, q14, q17, q19, q20}
- Lee `1`: {q16, q12, q13, q14, q17, q19, q20} ⟶ {q16, q12, q14, q15, q17, q19, q20, q21, q22} [q14→q15, q20→q21]; cierre λ añade {q16, q12, q14, q17, q19, q20, q22}
- **Rechazada**: ningún estado de {q16, q12, q14, q15, q17, q19, q20, q21, q22} es de aceptación.
