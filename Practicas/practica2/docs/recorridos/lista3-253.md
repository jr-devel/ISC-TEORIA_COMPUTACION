# Recorridos: Lista 3 · Ejercicio 253

AFN-λ equivalente a la expresión (0 + (11 + 00)*)(11 + 10 + 01)*(λ + 110).

Autómata: `lista3-253` (AFN-λ).

## Cadena λ

- Inicio: {q14}; con cierre λ, {q14, q0, q12, q10, q2, q6, q13, q15, q32, q30, q24, q16, q20, q26, q33, q42, q34, q35, q36, q43}
- **Aceptada**: queda {q43} ∈ F.

## Cadena `0`

- Inicio: {q14}; con cierre λ, {q14, q0, q12, q10, q2, q6, q13, q15, q32, q30, q24, q16, q20, q26, q33, q42, q34, q35, q36, q43}
- Lee `0`: {q14, q0, q12, q10, q2, q6, q13, q15, q32, q30, q24, q16, q20, q26, q33, q42, q34, q35, q36, q43} ⟶ {q1, q7, q8, q15, q32, q30, q24, q16, q20, q26, q27, q28, q33, q42, q34, q35, q36, q43} [q0→q1, q26→q27, q6→q7]; cierre λ añade {q8, q15, q32, q30, q24, q16, q20, q26, q28, q33, q42, q34, q35, q36, q43}
- **Aceptada**: queda {q43} ∈ F.

## Cadena `010`

- Inicio: {q14}; con cierre λ, {q14, q0, q12, q10, q2, q6, q13, q15, q32, q30, q24, q16, q20, q26, q33, q42, q34, q35, q36, q43}
- Lee `0`: {q14, q0, q12, q10, q2, q6, q13, q15, q32, q30, q24, q16, q20, q26, q33, q42, q34, q35, q36, q43} ⟶ {q1, q7, q8, q15, q32, q30, q24, q16, q20, q26, q27, q28, q33, q42, q34, q35, q36, q43} [q0→q1, q26→q27, q6→q7]; cierre λ añade {q8, q15, q32, q30, q24, q16, q20, q26, q28, q33, q42, q34, q35, q36, q43}
- Lee `1`: {q1, q7, q8, q15, q32, q30, q24, q16, q20, q26, q27, q28, q33, q42, q34, q35, q36, q43} ⟶ {q30, q24, q16, q17, q18, q20, q21, q22, q26, q29, q31, q33, q42, q34, q35, q36, q37, q38, q43} [q16→q17, q20→q21, q28→q29, q36→q37]; cierre λ añade {q30, q24, q16, q18, q20, q22, q26, q31, q33, q42, q34, q35, q36, q38, q43}
- Lee `0`: {q30, q24, q16, q17, q18, q20, q21, q22, q26, q29, q31, q33, q42, q34, q35, q36, q37, q38, q43} ⟶ {q30, q24, q16, q20, q23, q25, q26, q27, q28, q31, q33, q42, q34, q35, q36, q43} [q22→q23, q26→q27]; cierre λ añade {q30, q24, q16, q20, q25, q26, q28, q31, q33, q42, q34, q35, q36, q43}
- **Aceptada**: queda {q43} ∈ F.

## Cadena `01111`

- Inicio: {q14}; con cierre λ, {q14, q0, q12, q10, q2, q6, q13, q15, q32, q30, q24, q16, q20, q26, q33, q42, q34, q35, q36, q43}
- Lee `0`: {q14, q0, q12, q10, q2, q6, q13, q15, q32, q30, q24, q16, q20, q26, q33, q42, q34, q35, q36, q43} ⟶ {q1, q7, q8, q15, q32, q30, q24, q16, q20, q26, q27, q28, q33, q42, q34, q35, q36, q43} [q0→q1, q26→q27, q6→q7]; cierre λ añade {q8, q15, q32, q30, q24, q16, q20, q26, q28, q33, q42, q34, q35, q36, q43}
- Lee `1`: {q1, q7, q8, q15, q32, q30, q24, q16, q20, q26, q27, q28, q33, q42, q34, q35, q36, q43} ⟶ {q30, q24, q16, q17, q18, q20, q21, q22, q26, q29, q31, q33, q42, q34, q35, q36, q37, q38, q43} [q16→q17, q20→q21, q28→q29, q36→q37]; cierre λ añade {q30, q24, q16, q18, q20, q22, q26, q31, q33, q42, q34, q35, q36, q38, q43}
- Lee `1`: {q30, q24, q16, q17, q18, q20, q21, q22, q26, q29, q31, q33, q42, q34, q35, q36, q37, q38, q43} ⟶ {q30, q24, q16, q17, q18, q19, q20, q21, q22, q25, q26, q31, q33, q42, q34, q35, q36, q37, q38, q39, q40, q43} [q16→q17, q18→q19, q20→q21, q36→q37, q38→q39]; cierre λ añade {q30, q24, q16, q18, q20, q22, q25, q26, q31, q33, q42, q34, q35, q36, q38, q40, q43}
- Lee `1`: {q30, q24, q16, q17, q18, q19, q20, q21, q22, q25, q26, q31, q33, q42, q34, q35, q36, q37, q38, q39, q40, q43} ⟶ {q30, q24, q16, q17, q18, q19, q20, q21, q22, q25, q26, q31, q33, q42, q34, q35, q36, q37, q38, q39, q40, q43} [q16→q17, q18→q19, q20→q21, q36→q37, q38→q39]; cierre λ añade {q30, q24, q16, q18, q20, q22, q25, q26, q31, q33, q42, q34, q35, q36, q38, q40, q43}
- Lee `1`: {q30, q24, q16, q17, q18, q19, q20, q21, q22, q25, q26, q31, q33, q42, q34, q35, q36, q37, q38, q39, q40, q43} ⟶ {q30, q24, q16, q17, q18, q19, q20, q21, q22, q25, q26, q31, q33, q42, q34, q35, q36, q37, q38, q39, q40, q43} [q16→q17, q18→q19, q20→q21, q36→q37, q38→q39]; cierre λ añade {q30, q24, q16, q18, q20, q22, q25, q26, q31, q33, q42, q34, q35, q36, q38, q40, q43}
- **Aceptada**: queda {q43} ∈ F.

## Cadena `00011011`

- Inicio: {q14}; con cierre λ, {q14, q0, q12, q10, q2, q6, q13, q15, q32, q30, q24, q16, q20, q26, q33, q42, q34, q35, q36, q43}
- Lee `0`: {q14, q0, q12, q10, q2, q6, q13, q15, q32, q30, q24, q16, q20, q26, q33, q42, q34, q35, q36, q43} ⟶ {q1, q7, q8, q15, q32, q30, q24, q16, q20, q26, q27, q28, q33, q42, q34, q35, q36, q43} [q0→q1, q26→q27, q6→q7]; cierre λ añade {q8, q15, q32, q30, q24, q16, q20, q26, q28, q33, q42, q34, q35, q36, q43}
- Lee `0`: {q1, q7, q8, q15, q32, q30, q24, q16, q20, q26, q27, q28, q33, q42, q34, q35, q36, q43} ⟶ {q10, q2, q6, q9, q11, q13, q15, q32, q30, q24, q16, q20, q26, q27, q28, q33, q42, q34, q35, q36, q43} [q26→q27, q8→q9]; cierre λ añade {q10, q2, q6, q11, q13, q15, q32, q30, q24, q16, q20, q26, q28, q33, q42, q34, q35, q36, q43}
- Lee `0`: {q10, q2, q6, q9, q11, q13, q15, q32, q30, q24, q16, q20, q26, q27, q28, q33, q42, q34, q35, q36, q43} ⟶ {q7, q8, q27, q28} [q26→q27, q6→q7]; cierre λ añade {q8, q28}
- Lee `1`: {q7, q8, q27, q28} ⟶ {q30, q24, q16, q20, q26, q29, q31, q33, q42, q34, q35, q36, q43} [q28→q29]; cierre λ añade {q30, q24, q16, q20, q26, q31, q33, q42, q34, q35, q36, q43}
- Lee `1`: {q30, q24, q16, q20, q26, q29, q31, q33, q42, q34, q35, q36, q43} ⟶ {q17, q18, q21, q22, q37, q38} [q16→q17, q20→q21, q36→q37]; cierre λ añade {q18, q22, q38}
- Lee `0`: {q17, q18, q21, q22, q37, q38} ⟶ {q30, q24, q16, q20, q23, q25, q26, q31, q33, q42, q34, q35, q36, q43} [q22→q23]; cierre λ añade {q30, q24, q16, q20, q25, q26, q31, q33, q42, q34, q35, q36, q43}
- Lee `1`: {q30, q24, q16, q20, q23, q25, q26, q31, q33, q42, q34, q35, q36, q43} ⟶ {q17, q18, q21, q22, q37, q38} [q16→q17, q20→q21, q36→q37]; cierre λ añade {q18, q22, q38}
- Lee `1`: {q17, q18, q21, q22, q37, q38} ⟶ {q30, q24, q16, q19, q20, q25, q26, q31, q33, q42, q34, q35, q36, q39, q40, q43} [q18→q19, q38→q39]; cierre λ añade {q30, q24, q16, q20, q25, q26, q31, q33, q42, q34, q35, q36, q40, q43}
- **Aceptada**: queda {q43} ∈ F.

## Cadena `1`

- Inicio: {q14}; con cierre λ, {q14, q0, q12, q10, q2, q6, q13, q15, q32, q30, q24, q16, q20, q26, q33, q42, q34, q35, q36, q43}
- Lee `1`: {q14, q0, q12, q10, q2, q6, q13, q15, q32, q30, q24, q16, q20, q26, q33, q42, q34, q35, q36, q43} ⟶ {q3, q4, q17, q18, q21, q22, q37, q38} [q16→q17, q2→q3, q20→q21, q36→q37]; cierre λ añade {q4, q18, q22, q38}
- **Rechazada**: ningún estado de {q3, q4, q17, q18, q21, q22, q37, q38} es de aceptación.

## Cadena `111`

- Inicio: {q14}; con cierre λ, {q14, q0, q12, q10, q2, q6, q13, q15, q32, q30, q24, q16, q20, q26, q33, q42, q34, q35, q36, q43}
- Lee `1`: {q14, q0, q12, q10, q2, q6, q13, q15, q32, q30, q24, q16, q20, q26, q33, q42, q34, q35, q36, q43} ⟶ {q3, q4, q17, q18, q21, q22, q37, q38} [q16→q17, q2→q3, q20→q21, q36→q37]; cierre λ añade {q4, q18, q22, q38}
- Lee `1`: {q3, q4, q17, q18, q21, q22, q37, q38} ⟶ {q10, q2, q5, q6, q11, q13, q15, q32, q30, q24, q16, q19, q20, q25, q26, q31, q33, q42, q34, q35, q36, q39, q40, q43} [q18→q19, q38→q39, q4→q5]; cierre λ añade {q10, q2, q6, q11, q13, q15, q32, q30, q24, q16, q20, q25, q26, q31, q33, q42, q34, q35, q36, q40, q43}
- Lee `1`: {q10, q2, q5, q6, q11, q13, q15, q32, q30, q24, q16, q19, q20, q25, q26, q31, q33, q42, q34, q35, q36, q39, q40, q43} ⟶ {q3, q4, q17, q18, q21, q22, q37, q38} [q16→q17, q2→q3, q20→q21, q36→q37]; cierre λ añade {q4, q18, q22, q38}
- **Rechazada**: ningún estado de {q3, q4, q17, q18, q21, q22, q37, q38} es de aceptación.

## Cadena `0111001000`

- Inicio: {q14}; con cierre λ, {q14, q0, q12, q10, q2, q6, q13, q15, q32, q30, q24, q16, q20, q26, q33, q42, q34, q35, q36, q43}
- Lee `0`: {q14, q0, q12, q10, q2, q6, q13, q15, q32, q30, q24, q16, q20, q26, q33, q42, q34, q35, q36, q43} ⟶ {q1, q7, q8, q15, q32, q30, q24, q16, q20, q26, q27, q28, q33, q42, q34, q35, q36, q43} [q0→q1, q26→q27, q6→q7]; cierre λ añade {q8, q15, q32, q30, q24, q16, q20, q26, q28, q33, q42, q34, q35, q36, q43}
- Lee `1`: {q1, q7, q8, q15, q32, q30, q24, q16, q20, q26, q27, q28, q33, q42, q34, q35, q36, q43} ⟶ {q30, q24, q16, q17, q18, q20, q21, q22, q26, q29, q31, q33, q42, q34, q35, q36, q37, q38, q43} [q16→q17, q20→q21, q28→q29, q36→q37]; cierre λ añade {q30, q24, q16, q18, q20, q22, q26, q31, q33, q42, q34, q35, q36, q38, q43}
- Lee `1`: {q30, q24, q16, q17, q18, q20, q21, q22, q26, q29, q31, q33, q42, q34, q35, q36, q37, q38, q43} ⟶ {q30, q24, q16, q17, q18, q19, q20, q21, q22, q25, q26, q31, q33, q42, q34, q35, q36, q37, q38, q39, q40, q43} [q16→q17, q18→q19, q20→q21, q36→q37, q38→q39]; cierre λ añade {q30, q24, q16, q18, q20, q22, q25, q26, q31, q33, q42, q34, q35, q36, q38, q40, q43}
- Lee `1`: {q30, q24, q16, q17, q18, q19, q20, q21, q22, q25, q26, q31, q33, q42, q34, q35, q36, q37, q38, q39, q40, q43} ⟶ {q30, q24, q16, q17, q18, q19, q20, q21, q22, q25, q26, q31, q33, q42, q34, q35, q36, q37, q38, q39, q40, q43} [q16→q17, q18→q19, q20→q21, q36→q37, q38→q39]; cierre λ añade {q30, q24, q16, q18, q20, q22, q25, q26, q31, q33, q42, q34, q35, q36, q38, q40, q43}
- Lee `0`: {q30, q24, q16, q17, q18, q19, q20, q21, q22, q25, q26, q31, q33, q42, q34, q35, q36, q37, q38, q39, q40, q43} ⟶ {q30, q24, q16, q20, q23, q25, q26, q27, q28, q31, q33, q42, q34, q35, q36, q41, q43} [q22→q23, q26→q27, q40→q41]; cierre λ añade {q30, q24, q16, q20, q25, q26, q28, q31, q33, q42, q34, q35, q36, q43}
- Lee `0`: {q30, q24, q16, q20, q23, q25, q26, q27, q28, q31, q33, q42, q34, q35, q36, q41, q43} ⟶ {q27, q28} [q26→q27]; cierre λ añade {q28}
- Lee `1`: {q27, q28} ⟶ {q30, q24, q16, q20, q26, q29, q31, q33, q42, q34, q35, q36, q43} [q28→q29]; cierre λ añade {q30, q24, q16, q20, q26, q31, q33, q42, q34, q35, q36, q43}
- Lee `0`: {q30, q24, q16, q20, q26, q29, q31, q33, q42, q34, q35, q36, q43} ⟶ {q27, q28} [q26→q27]; cierre λ añade {q28}
- Lee `0`: {q27, q28} ⟶ ∅ [ninguna transición]
- Lee `0`: ∅ ⟶ ∅ [ninguna transición]
- **Rechazada**: no queda ningún estado activo.

## Cadena `0110110000000`

- Inicio: {q14}; con cierre λ, {q14, q0, q12, q10, q2, q6, q13, q15, q32, q30, q24, q16, q20, q26, q33, q42, q34, q35, q36, q43}
- Lee `0`: {q14, q0, q12, q10, q2, q6, q13, q15, q32, q30, q24, q16, q20, q26, q33, q42, q34, q35, q36, q43} ⟶ {q1, q7, q8, q15, q32, q30, q24, q16, q20, q26, q27, q28, q33, q42, q34, q35, q36, q43} [q0→q1, q26→q27, q6→q7]; cierre λ añade {q8, q15, q32, q30, q24, q16, q20, q26, q28, q33, q42, q34, q35, q36, q43}
- Lee `1`: {q1, q7, q8, q15, q32, q30, q24, q16, q20, q26, q27, q28, q33, q42, q34, q35, q36, q43} ⟶ {q30, q24, q16, q17, q18, q20, q21, q22, q26, q29, q31, q33, q42, q34, q35, q36, q37, q38, q43} [q16→q17, q20→q21, q28→q29, q36→q37]; cierre λ añade {q30, q24, q16, q18, q20, q22, q26, q31, q33, q42, q34, q35, q36, q38, q43}
- Lee `1`: {q30, q24, q16, q17, q18, q20, q21, q22, q26, q29, q31, q33, q42, q34, q35, q36, q37, q38, q43} ⟶ {q30, q24, q16, q17, q18, q19, q20, q21, q22, q25, q26, q31, q33, q42, q34, q35, q36, q37, q38, q39, q40, q43} [q16→q17, q18→q19, q20→q21, q36→q37, q38→q39]; cierre λ añade {q30, q24, q16, q18, q20, q22, q25, q26, q31, q33, q42, q34, q35, q36, q38, q40, q43}
- Lee `0`: {q30, q24, q16, q17, q18, q19, q20, q21, q22, q25, q26, q31, q33, q42, q34, q35, q36, q37, q38, q39, q40, q43} ⟶ {q30, q24, q16, q20, q23, q25, q26, q27, q28, q31, q33, q42, q34, q35, q36, q41, q43} [q22→q23, q26→q27, q40→q41]; cierre λ añade {q30, q24, q16, q20, q25, q26, q28, q31, q33, q42, q34, q35, q36, q43}
- Lee `1`: {q30, q24, q16, q20, q23, q25, q26, q27, q28, q31, q33, q42, q34, q35, q36, q41, q43} ⟶ {q30, q24, q16, q17, q18, q20, q21, q22, q26, q29, q31, q33, q42, q34, q35, q36, q37, q38, q43} [q16→q17, q20→q21, q28→q29, q36→q37]; cierre λ añade {q30, q24, q16, q18, q20, q22, q26, q31, q33, q42, q34, q35, q36, q38, q43}
- Lee `1`: {q30, q24, q16, q17, q18, q20, q21, q22, q26, q29, q31, q33, q42, q34, q35, q36, q37, q38, q43} ⟶ {q30, q24, q16, q17, q18, q19, q20, q21, q22, q25, q26, q31, q33, q42, q34, q35, q36, q37, q38, q39, q40, q43} [q16→q17, q18→q19, q20→q21, q36→q37, q38→q39]; cierre λ añade {q30, q24, q16, q18, q20, q22, q25, q26, q31, q33, q42, q34, q35, q36, q38, q40, q43}
- Lee `0`: {q30, q24, q16, q17, q18, q19, q20, q21, q22, q25, q26, q31, q33, q42, q34, q35, q36, q37, q38, q39, q40, q43} ⟶ {q30, q24, q16, q20, q23, q25, q26, q27, q28, q31, q33, q42, q34, q35, q36, q41, q43} [q22→q23, q26→q27, q40→q41]; cierre λ añade {q30, q24, q16, q20, q25, q26, q28, q31, q33, q42, q34, q35, q36, q43}
- Lee `0`: {q30, q24, q16, q20, q23, q25, q26, q27, q28, q31, q33, q42, q34, q35, q36, q41, q43} ⟶ {q27, q28} [q26→q27]; cierre λ añade {q28}
- Lee `0`: {q27, q28} ⟶ ∅ [ninguna transición]
- Lee `0`: ∅ ⟶ ∅ [ninguna transición]
- Lee `0`: ∅ ⟶ ∅ [ninguna transición]
- Lee `0`: ∅ ⟶ ∅ [ninguna transición]
- Lee `0`: ∅ ⟶ ∅ [ninguna transición]
- **Rechazada**: no queda ningún estado activo.

## Cadena `00101011100000`

- Inicio: {q14}; con cierre λ, {q14, q0, q12, q10, q2, q6, q13, q15, q32, q30, q24, q16, q20, q26, q33, q42, q34, q35, q36, q43}
- Lee `0`: {q14, q0, q12, q10, q2, q6, q13, q15, q32, q30, q24, q16, q20, q26, q33, q42, q34, q35, q36, q43} ⟶ {q1, q7, q8, q15, q32, q30, q24, q16, q20, q26, q27, q28, q33, q42, q34, q35, q36, q43} [q0→q1, q26→q27, q6→q7]; cierre λ añade {q8, q15, q32, q30, q24, q16, q20, q26, q28, q33, q42, q34, q35, q36, q43}
- Lee `0`: {q1, q7, q8, q15, q32, q30, q24, q16, q20, q26, q27, q28, q33, q42, q34, q35, q36, q43} ⟶ {q10, q2, q6, q9, q11, q13, q15, q32, q30, q24, q16, q20, q26, q27, q28, q33, q42, q34, q35, q36, q43} [q26→q27, q8→q9]; cierre λ añade {q10, q2, q6, q11, q13, q15, q32, q30, q24, q16, q20, q26, q28, q33, q42, q34, q35, q36, q43}
- Lee `1`: {q10, q2, q6, q9, q11, q13, q15, q32, q30, q24, q16, q20, q26, q27, q28, q33, q42, q34, q35, q36, q43} ⟶ {q3, q4, q30, q24, q16, q17, q18, q20, q21, q22, q26, q29, q31, q33, q42, q34, q35, q36, q37, q38, q43} [q16→q17, q2→q3, q20→q21, q28→q29, q36→q37]; cierre λ añade {q4, q30, q24, q16, q18, q20, q22, q26, q31, q33, q42, q34, q35, q36, q38, q43}
- Lee `0`: {q3, q4, q30, q24, q16, q17, q18, q20, q21, q22, q26, q29, q31, q33, q42, q34, q35, q36, q37, q38, q43} ⟶ {q30, q24, q16, q20, q23, q25, q26, q27, q28, q31, q33, q42, q34, q35, q36, q43} [q22→q23, q26→q27]; cierre λ añade {q30, q24, q16, q20, q25, q26, q28, q31, q33, q42, q34, q35, q36, q43}
- Lee `1`: {q30, q24, q16, q20, q23, q25, q26, q27, q28, q31, q33, q42, q34, q35, q36, q43} ⟶ {q30, q24, q16, q17, q18, q20, q21, q22, q26, q29, q31, q33, q42, q34, q35, q36, q37, q38, q43} [q16→q17, q20→q21, q28→q29, q36→q37]; cierre λ añade {q30, q24, q16, q18, q20, q22, q26, q31, q33, q42, q34, q35, q36, q38, q43}
- Lee `0`: {q30, q24, q16, q17, q18, q20, q21, q22, q26, q29, q31, q33, q42, q34, q35, q36, q37, q38, q43} ⟶ {q30, q24, q16, q20, q23, q25, q26, q27, q28, q31, q33, q42, q34, q35, q36, q43} [q22→q23, q26→q27]; cierre λ añade {q30, q24, q16, q20, q25, q26, q28, q31, q33, q42, q34, q35, q36, q43}
- Lee `1`: {q30, q24, q16, q20, q23, q25, q26, q27, q28, q31, q33, q42, q34, q35, q36, q43} ⟶ {q30, q24, q16, q17, q18, q20, q21, q22, q26, q29, q31, q33, q42, q34, q35, q36, q37, q38, q43} [q16→q17, q20→q21, q28→q29, q36→q37]; cierre λ añade {q30, q24, q16, q18, q20, q22, q26, q31, q33, q42, q34, q35, q36, q38, q43}
- Lee `1`: {q30, q24, q16, q17, q18, q20, q21, q22, q26, q29, q31, q33, q42, q34, q35, q36, q37, q38, q43} ⟶ {q30, q24, q16, q17, q18, q19, q20, q21, q22, q25, q26, q31, q33, q42, q34, q35, q36, q37, q38, q39, q40, q43} [q16→q17, q18→q19, q20→q21, q36→q37, q38→q39]; cierre λ añade {q30, q24, q16, q18, q20, q22, q25, q26, q31, q33, q42, q34, q35, q36, q38, q40, q43}
- Lee `1`: {q30, q24, q16, q17, q18, q19, q20, q21, q22, q25, q26, q31, q33, q42, q34, q35, q36, q37, q38, q39, q40, q43} ⟶ {q30, q24, q16, q17, q18, q19, q20, q21, q22, q25, q26, q31, q33, q42, q34, q35, q36, q37, q38, q39, q40, q43} [q16→q17, q18→q19, q20→q21, q36→q37, q38→q39]; cierre λ añade {q30, q24, q16, q18, q20, q22, q25, q26, q31, q33, q42, q34, q35, q36, q38, q40, q43}
- Lee `0`: {q30, q24, q16, q17, q18, q19, q20, q21, q22, q25, q26, q31, q33, q42, q34, q35, q36, q37, q38, q39, q40, q43} ⟶ {q30, q24, q16, q20, q23, q25, q26, q27, q28, q31, q33, q42, q34, q35, q36, q41, q43} [q22→q23, q26→q27, q40→q41]; cierre λ añade {q30, q24, q16, q20, q25, q26, q28, q31, q33, q42, q34, q35, q36, q43}
- Lee `0`: {q30, q24, q16, q20, q23, q25, q26, q27, q28, q31, q33, q42, q34, q35, q36, q41, q43} ⟶ {q27, q28} [q26→q27]; cierre λ añade {q28}
- Lee `0`: {q27, q28} ⟶ ∅ [ninguna transición]
- Lee `0`: ∅ ⟶ ∅ [ninguna transición]
- Lee `0`: ∅ ⟶ ∅ [ninguna transición]
- **Rechazada**: no queda ningún estado activo.
