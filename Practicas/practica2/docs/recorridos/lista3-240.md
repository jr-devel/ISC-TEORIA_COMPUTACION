# Recorridos: Lista 3 · Ejercicio 240

Expresión regular sobre {0, 1} para: Cadenas de longitud par que contienen 01.

Autómata: `lista3-240` (AFN-λ).

## Cadena `01`

- Inicio: {q76}; con cierre λ, {q76, q12, q4, q0, q2, q13, q14, q36, q32, q34}
- Lee `0`: {q76, q12, q4, q0, q2, q13, q14, q36, q32, q34} ⟶ {q1, q5, q10, q6, q8, q15, q16, q33, q37, q50, q42, q38, q40, q51, q52} [q0→q1, q14→q15, q32→q33]; cierre λ añade {q5, q10, q6, q8, q16, q37, q50, q42, q38, q40, q51, q52}
- Lee `1`: {q1, q5, q10, q6, q8, q15, q16, q33, q37, q50, q42, q38, q40, q51, q52} ⟶ {q4, q0, q2, q9, q11, q13, q14, q17, q30, q22, q18, q20, q31, q41, q43, q48, q44, q46, q77} [q16→q17, q40→q41, q8→q9]; cierre λ añade {q4, q0, q2, q11, q13, q14, q30, q22, q18, q20, q31, q43, q48, q44, q46, q77}
- **Aceptada**: queda {q77} ∈ F.

## Cadena `100010`

- Inicio: {q76}; con cierre λ, {q76, q12, q4, q0, q2, q13, q14, q36, q32, q34}
- Lee `1`: {q76, q12, q4, q0, q2, q13, q14, q36, q32, q34} ⟶ {q3, q5, q10, q6, q8, q35, q37, q50, q42, q38, q40, q51, q52} [q2→q3, q34→q35]; cierre λ añade {q5, q10, q6, q8, q37, q50, q42, q38, q40, q51, q52}
- Lee `0`: {q3, q5, q10, q6, q8, q35, q37, q50, q42, q38, q40, q51, q52} ⟶ {q4, q0, q2, q7, q11, q13, q14, q39, q43, q48, q44, q46, q53, q54} [q38→q39, q52→q53, q6→q7]; cierre λ añade {q4, q0, q2, q11, q13, q14, q43, q48, q44, q46, q54}
- Lee `0`: {q4, q0, q2, q7, q11, q13, q14, q39, q43, q48, q44, q46, q53, q54} ⟶ {q1, q5, q10, q6, q8, q15, q16, q42, q38, q40, q45, q49, q51, q52} [q0→q1, q14→q15, q44→q45]; cierre λ añade {q5, q10, q6, q8, q16, q42, q38, q40, q49, q51, q52}
- Lee `0`: {q1, q5, q10, q6, q8, q15, q16, q42, q38, q40, q45, q49, q51, q52} ⟶ {q4, q0, q2, q7, q11, q13, q14, q39, q43, q48, q44, q46, q53, q54} [q38→q39, q52→q53, q6→q7]; cierre λ añade {q4, q0, q2, q11, q13, q14, q43, q48, q44, q46, q54}
- Lee `1`: {q4, q0, q2, q7, q11, q13, q14, q39, q43, q48, q44, q46, q53, q54} ⟶ {q3, q5, q10, q6, q8, q42, q38, q40, q47, q49, q51, q52, q55, q68, q60, q56, q58, q69, q74, q70, q72} [q2→q3, q46→q47, q54→q55]; cierre λ añade {q5, q10, q6, q8, q42, q38, q40, q49, q51, q52, q68, q60, q56, q58, q69, q74, q70, q72}
- Lee `0`: {q3, q5, q10, q6, q8, q42, q38, q40, q47, q49, q51, q52, q55, q68, q60, q56, q58, q69, q74, q70, q72} ⟶ {q4, q0, q2, q7, q11, q13, q14, q39, q43, q48, q44, q46, q53, q54, q57, q61, q66, q62, q64, q71, q75, q77} [q38→q39, q52→q53, q56→q57, q6→q7, q70→q71]; cierre λ añade {q4, q0, q2, q11, q13, q14, q43, q48, q44, q46, q54, q61, q66, q62, q64, q75, q77}
- **Aceptada**: queda {q77} ∈ F.

## Cadena `00001001`

- Inicio: {q76}; con cierre λ, {q76, q12, q4, q0, q2, q13, q14, q36, q32, q34}
- Lee `0`: {q76, q12, q4, q0, q2, q13, q14, q36, q32, q34} ⟶ {q1, q5, q10, q6, q8, q15, q16, q33, q37, q50, q42, q38, q40, q51, q52} [q0→q1, q14→q15, q32→q33]; cierre λ añade {q5, q10, q6, q8, q16, q37, q50, q42, q38, q40, q51, q52}
- Lee `0`: {q1, q5, q10, q6, q8, q15, q16, q33, q37, q50, q42, q38, q40, q51, q52} ⟶ {q4, q0, q2, q7, q11, q13, q14, q39, q43, q48, q44, q46, q53, q54} [q38→q39, q52→q53, q6→q7]; cierre λ añade {q4, q0, q2, q11, q13, q14, q43, q48, q44, q46, q54}
- Lee `0`: {q4, q0, q2, q7, q11, q13, q14, q39, q43, q48, q44, q46, q53, q54} ⟶ {q1, q5, q10, q6, q8, q15, q16, q42, q38, q40, q45, q49, q51, q52} [q0→q1, q14→q15, q44→q45]; cierre λ añade {q5, q10, q6, q8, q16, q42, q38, q40, q49, q51, q52}
- Lee `0`: {q1, q5, q10, q6, q8, q15, q16, q42, q38, q40, q45, q49, q51, q52} ⟶ {q4, q0, q2, q7, q11, q13, q14, q39, q43, q48, q44, q46, q53, q54} [q38→q39, q52→q53, q6→q7]; cierre λ añade {q4, q0, q2, q11, q13, q14, q43, q48, q44, q46, q54}
- Lee `1`: {q4, q0, q2, q7, q11, q13, q14, q39, q43, q48, q44, q46, q53, q54} ⟶ {q3, q5, q10, q6, q8, q42, q38, q40, q47, q49, q51, q52, q55, q68, q60, q56, q58, q69, q74, q70, q72} [q2→q3, q46→q47, q54→q55]; cierre λ añade {q5, q10, q6, q8, q42, q38, q40, q49, q51, q52, q68, q60, q56, q58, q69, q74, q70, q72}
- Lee `0`: {q3, q5, q10, q6, q8, q42, q38, q40, q47, q49, q51, q52, q55, q68, q60, q56, q58, q69, q74, q70, q72} ⟶ {q4, q0, q2, q7, q11, q13, q14, q39, q43, q48, q44, q46, q53, q54, q57, q61, q66, q62, q64, q71, q75, q77} [q38→q39, q52→q53, q56→q57, q6→q7, q70→q71]; cierre λ añade {q4, q0, q2, q11, q13, q14, q43, q48, q44, q46, q54, q61, q66, q62, q64, q75, q77}
- Lee `0`: {q4, q0, q2, q7, q11, q13, q14, q39, q43, q48, q44, q46, q53, q54, q57, q61, q66, q62, q64, q71, q75, q77} ⟶ {q1, q5, q10, q6, q8, q15, q16, q42, q38, q40, q45, q49, q51, q52, q60, q56, q58, q63, q67, q69, q74, q70, q72} [q0→q1, q14→q15, q44→q45, q62→q63]; cierre λ añade {q5, q10, q6, q8, q16, q42, q38, q40, q49, q51, q52, q60, q56, q58, q67, q69, q74, q70, q72}
- Lee `1`: {q1, q5, q10, q6, q8, q15, q16, q42, q38, q40, q45, q49, q51, q52, q60, q56, q58, q63, q67, q69, q74, q70, q72} ⟶ {q4, q0, q2, q9, q11, q13, q14, q17, q30, q22, q18, q20, q31, q41, q43, q48, q44, q46, q59, q61, q66, q62, q64, q73, q75, q77} [q16→q17, q40→q41, q58→q59, q72→q73, q8→q9]; cierre λ añade {q4, q0, q2, q11, q13, q14, q30, q22, q18, q20, q31, q43, q48, q44, q46, q61, q66, q62, q64, q75, q77}
- **Aceptada**: queda {q77} ∈ F.

## Cadena `000111111010`

- Inicio: {q76}; con cierre λ, {q76, q12, q4, q0, q2, q13, q14, q36, q32, q34}
- Lee `0`: {q76, q12, q4, q0, q2, q13, q14, q36, q32, q34} ⟶ {q1, q5, q10, q6, q8, q15, q16, q33, q37, q50, q42, q38, q40, q51, q52} [q0→q1, q14→q15, q32→q33]; cierre λ añade {q5, q10, q6, q8, q16, q37, q50, q42, q38, q40, q51, q52}
- Lee `0`: {q1, q5, q10, q6, q8, q15, q16, q33, q37, q50, q42, q38, q40, q51, q52} ⟶ {q4, q0, q2, q7, q11, q13, q14, q39, q43, q48, q44, q46, q53, q54} [q38→q39, q52→q53, q6→q7]; cierre λ añade {q4, q0, q2, q11, q13, q14, q43, q48, q44, q46, q54}
- Lee `0`: {q4, q0, q2, q7, q11, q13, q14, q39, q43, q48, q44, q46, q53, q54} ⟶ {q1, q5, q10, q6, q8, q15, q16, q42, q38, q40, q45, q49, q51, q52} [q0→q1, q14→q15, q44→q45]; cierre λ añade {q5, q10, q6, q8, q16, q42, q38, q40, q49, q51, q52}
- Lee `1`: {q1, q5, q10, q6, q8, q15, q16, q42, q38, q40, q45, q49, q51, q52} ⟶ {q4, q0, q2, q9, q11, q13, q14, q17, q30, q22, q18, q20, q31, q41, q43, q48, q44, q46, q77} [q16→q17, q40→q41, q8→q9]; cierre λ añade {q4, q0, q2, q11, q13, q14, q30, q22, q18, q20, q31, q43, q48, q44, q46, q77}
- Lee `1`: {q4, q0, q2, q9, q11, q13, q14, q17, q30, q22, q18, q20, q31, q41, q43, q48, q44, q46, q77} ⟶ {q3, q5, q10, q6, q8, q21, q23, q28, q24, q26, q42, q38, q40, q47, q49, q51, q52} [q2→q3, q20→q21, q46→q47]; cierre λ añade {q5, q10, q6, q8, q23, q28, q24, q26, q42, q38, q40, q49, q51, q52}
- Lee `1`: {q3, q5, q10, q6, q8, q21, q23, q28, q24, q26, q42, q38, q40, q47, q49, q51, q52} ⟶ {q4, q0, q2, q9, q11, q13, q14, q22, q18, q20, q27, q29, q31, q41, q43, q48, q44, q46, q77} [q26→q27, q40→q41, q8→q9]; cierre λ añade {q4, q0, q2, q11, q13, q14, q22, q18, q20, q29, q31, q43, q48, q44, q46, q77}
- Lee `1`: {q4, q0, q2, q9, q11, q13, q14, q22, q18, q20, q27, q29, q31, q41, q43, q48, q44, q46, q77} ⟶ {q3, q5, q10, q6, q8, q21, q23, q28, q24, q26, q42, q38, q40, q47, q49, q51, q52} [q2→q3, q20→q21, q46→q47]; cierre λ añade {q5, q10, q6, q8, q23, q28, q24, q26, q42, q38, q40, q49, q51, q52}
- Lee `1`: {q3, q5, q10, q6, q8, q21, q23, q28, q24, q26, q42, q38, q40, q47, q49, q51, q52} ⟶ {q4, q0, q2, q9, q11, q13, q14, q22, q18, q20, q27, q29, q31, q41, q43, q48, q44, q46, q77} [q26→q27, q40→q41, q8→q9]; cierre λ añade {q4, q0, q2, q11, q13, q14, q22, q18, q20, q29, q31, q43, q48, q44, q46, q77}
- Lee `1`: {q4, q0, q2, q9, q11, q13, q14, q22, q18, q20, q27, q29, q31, q41, q43, q48, q44, q46, q77} ⟶ {q3, q5, q10, q6, q8, q21, q23, q28, q24, q26, q42, q38, q40, q47, q49, q51, q52} [q2→q3, q20→q21, q46→q47]; cierre λ añade {q5, q10, q6, q8, q23, q28, q24, q26, q42, q38, q40, q49, q51, q52}
- Lee `0`: {q3, q5, q10, q6, q8, q21, q23, q28, q24, q26, q42, q38, q40, q47, q49, q51, q52} ⟶ {q4, q0, q2, q7, q11, q13, q14, q22, q18, q20, q25, q29, q31, q39, q43, q48, q44, q46, q53, q54, q77} [q24→q25, q38→q39, q52→q53, q6→q7]; cierre λ añade {q4, q0, q2, q11, q13, q14, q22, q18, q20, q29, q31, q43, q48, q44, q46, q54, q77}
- Lee `1`: {q4, q0, q2, q7, q11, q13, q14, q22, q18, q20, q25, q29, q31, q39, q43, q48, q44, q46, q53, q54, q77} ⟶ {q3, q5, q10, q6, q8, q21, q23, q28, q24, q26, q42, q38, q40, q47, q49, q51, q52, q55, q68, q60, q56, q58, q69, q74, q70, q72} [q2→q3, q20→q21, q46→q47, q54→q55]; cierre λ añade {q5, q10, q6, q8, q23, q28, q24, q26, q42, q38, q40, q49, q51, q52, q68, q60, q56, q58, q69, q74, q70, q72}
- Lee `0`: {q3, q5, q10, q6, q8, q21, q23, q28, q24, q26, q42, q38, q40, q47, q49, q51, q52, q55, q68, q60, q56, q58, q69, q74, q70, q72} ⟶ {q4, q0, q2, q7, q11, q13, q14, q22, q18, q20, q25, q29, q31, q39, q43, q48, q44, q46, q53, q54, q57, q61, q66, q62, q64, q71, q75, q77} [q24→q25, q38→q39, q52→q53, q56→q57, q6→q7, q70→q71]; cierre λ añade {q4, q0, q2, q11, q13, q14, q22, q18, q20, q29, q31, q43, q48, q44, q46, q54, q61, q66, q62, q64, q75, q77}
- **Aceptada**: queda {q77} ∈ F.

## Cadena `100000000110`

- Inicio: {q76}; con cierre λ, {q76, q12, q4, q0, q2, q13, q14, q36, q32, q34}
- Lee `1`: {q76, q12, q4, q0, q2, q13, q14, q36, q32, q34} ⟶ {q3, q5, q10, q6, q8, q35, q37, q50, q42, q38, q40, q51, q52} [q2→q3, q34→q35]; cierre λ añade {q5, q10, q6, q8, q37, q50, q42, q38, q40, q51, q52}
- Lee `0`: {q3, q5, q10, q6, q8, q35, q37, q50, q42, q38, q40, q51, q52} ⟶ {q4, q0, q2, q7, q11, q13, q14, q39, q43, q48, q44, q46, q53, q54} [q38→q39, q52→q53, q6→q7]; cierre λ añade {q4, q0, q2, q11, q13, q14, q43, q48, q44, q46, q54}
- Lee `0`: {q4, q0, q2, q7, q11, q13, q14, q39, q43, q48, q44, q46, q53, q54} ⟶ {q1, q5, q10, q6, q8, q15, q16, q42, q38, q40, q45, q49, q51, q52} [q0→q1, q14→q15, q44→q45]; cierre λ añade {q5, q10, q6, q8, q16, q42, q38, q40, q49, q51, q52}
- Lee `0`: {q1, q5, q10, q6, q8, q15, q16, q42, q38, q40, q45, q49, q51, q52} ⟶ {q4, q0, q2, q7, q11, q13, q14, q39, q43, q48, q44, q46, q53, q54} [q38→q39, q52→q53, q6→q7]; cierre λ añade {q4, q0, q2, q11, q13, q14, q43, q48, q44, q46, q54}
- Lee `0`: {q4, q0, q2, q7, q11, q13, q14, q39, q43, q48, q44, q46, q53, q54} ⟶ {q1, q5, q10, q6, q8, q15, q16, q42, q38, q40, q45, q49, q51, q52} [q0→q1, q14→q15, q44→q45]; cierre λ añade {q5, q10, q6, q8, q16, q42, q38, q40, q49, q51, q52}
- Lee `0`: {q1, q5, q10, q6, q8, q15, q16, q42, q38, q40, q45, q49, q51, q52} ⟶ {q4, q0, q2, q7, q11, q13, q14, q39, q43, q48, q44, q46, q53, q54} [q38→q39, q52→q53, q6→q7]; cierre λ añade {q4, q0, q2, q11, q13, q14, q43, q48, q44, q46, q54}
- Lee `0`: {q4, q0, q2, q7, q11, q13, q14, q39, q43, q48, q44, q46, q53, q54} ⟶ {q1, q5, q10, q6, q8, q15, q16, q42, q38, q40, q45, q49, q51, q52} [q0→q1, q14→q15, q44→q45]; cierre λ añade {q5, q10, q6, q8, q16, q42, q38, q40, q49, q51, q52}
- Lee `0`: {q1, q5, q10, q6, q8, q15, q16, q42, q38, q40, q45, q49, q51, q52} ⟶ {q4, q0, q2, q7, q11, q13, q14, q39, q43, q48, q44, q46, q53, q54} [q38→q39, q52→q53, q6→q7]; cierre λ añade {q4, q0, q2, q11, q13, q14, q43, q48, q44, q46, q54}
- Lee `0`: {q4, q0, q2, q7, q11, q13, q14, q39, q43, q48, q44, q46, q53, q54} ⟶ {q1, q5, q10, q6, q8, q15, q16, q42, q38, q40, q45, q49, q51, q52} [q0→q1, q14→q15, q44→q45]; cierre λ añade {q5, q10, q6, q8, q16, q42, q38, q40, q49, q51, q52}
- Lee `1`: {q1, q5, q10, q6, q8, q15, q16, q42, q38, q40, q45, q49, q51, q52} ⟶ {q4, q0, q2, q9, q11, q13, q14, q17, q30, q22, q18, q20, q31, q41, q43, q48, q44, q46, q77} [q16→q17, q40→q41, q8→q9]; cierre λ añade {q4, q0, q2, q11, q13, q14, q30, q22, q18, q20, q31, q43, q48, q44, q46, q77}
- Lee `1`: {q4, q0, q2, q9, q11, q13, q14, q17, q30, q22, q18, q20, q31, q41, q43, q48, q44, q46, q77} ⟶ {q3, q5, q10, q6, q8, q21, q23, q28, q24, q26, q42, q38, q40, q47, q49, q51, q52} [q2→q3, q20→q21, q46→q47]; cierre λ añade {q5, q10, q6, q8, q23, q28, q24, q26, q42, q38, q40, q49, q51, q52}
- Lee `0`: {q3, q5, q10, q6, q8, q21, q23, q28, q24, q26, q42, q38, q40, q47, q49, q51, q52} ⟶ {q4, q0, q2, q7, q11, q13, q14, q22, q18, q20, q25, q29, q31, q39, q43, q48, q44, q46, q53, q54, q77} [q24→q25, q38→q39, q52→q53, q6→q7]; cierre λ añade {q4, q0, q2, q11, q13, q14, q22, q18, q20, q29, q31, q43, q48, q44, q46, q54, q77}
- **Aceptada**: queda {q77} ∈ F.

## Cadena λ

- Inicio: {q76}; con cierre λ, {q76, q12, q4, q0, q2, q13, q14, q36, q32, q34}
- **Rechazada**: ningún estado de {q76, q12, q4, q0, q2, q13, q14, q36, q32, q34} es de aceptación.

## Cadena `1`

- Inicio: {q76}; con cierre λ, {q76, q12, q4, q0, q2, q13, q14, q36, q32, q34}
- Lee `1`: {q76, q12, q4, q0, q2, q13, q14, q36, q32, q34} ⟶ {q3, q5, q10, q6, q8, q35, q37, q50, q42, q38, q40, q51, q52} [q2→q3, q34→q35]; cierre λ añade {q5, q10, q6, q8, q37, q50, q42, q38, q40, q51, q52}
- **Rechazada**: ningún estado de {q3, q5, q10, q6, q8, q35, q37, q50, q42, q38, q40, q51, q52} es de aceptación.

## Cadena `001`

- Inicio: {q76}; con cierre λ, {q76, q12, q4, q0, q2, q13, q14, q36, q32, q34}
- Lee `0`: {q76, q12, q4, q0, q2, q13, q14, q36, q32, q34} ⟶ {q1, q5, q10, q6, q8, q15, q16, q33, q37, q50, q42, q38, q40, q51, q52} [q0→q1, q14→q15, q32→q33]; cierre λ añade {q5, q10, q6, q8, q16, q37, q50, q42, q38, q40, q51, q52}
- Lee `0`: {q1, q5, q10, q6, q8, q15, q16, q33, q37, q50, q42, q38, q40, q51, q52} ⟶ {q4, q0, q2, q7, q11, q13, q14, q39, q43, q48, q44, q46, q53, q54} [q38→q39, q52→q53, q6→q7]; cierre λ añade {q4, q0, q2, q11, q13, q14, q43, q48, q44, q46, q54}
- Lee `1`: {q4, q0, q2, q7, q11, q13, q14, q39, q43, q48, q44, q46, q53, q54} ⟶ {q3, q5, q10, q6, q8, q42, q38, q40, q47, q49, q51, q52, q55, q68, q60, q56, q58, q69, q74, q70, q72} [q2→q3, q46→q47, q54→q55]; cierre λ añade {q5, q10, q6, q8, q42, q38, q40, q49, q51, q52, q68, q60, q56, q58, q69, q74, q70, q72}
- **Rechazada**: ningún estado de {q3, q5, q10, q6, q8, q42, q38, q40, q47, q49, q51, q52, q55, q68, q60, q56, q58, q69, q74, q70, q72} es de aceptación.

## Cadena `10011`

- Inicio: {q76}; con cierre λ, {q76, q12, q4, q0, q2, q13, q14, q36, q32, q34}
- Lee `1`: {q76, q12, q4, q0, q2, q13, q14, q36, q32, q34} ⟶ {q3, q5, q10, q6, q8, q35, q37, q50, q42, q38, q40, q51, q52} [q2→q3, q34→q35]; cierre λ añade {q5, q10, q6, q8, q37, q50, q42, q38, q40, q51, q52}
- Lee `0`: {q3, q5, q10, q6, q8, q35, q37, q50, q42, q38, q40, q51, q52} ⟶ {q4, q0, q2, q7, q11, q13, q14, q39, q43, q48, q44, q46, q53, q54} [q38→q39, q52→q53, q6→q7]; cierre λ añade {q4, q0, q2, q11, q13, q14, q43, q48, q44, q46, q54}
- Lee `0`: {q4, q0, q2, q7, q11, q13, q14, q39, q43, q48, q44, q46, q53, q54} ⟶ {q1, q5, q10, q6, q8, q15, q16, q42, q38, q40, q45, q49, q51, q52} [q0→q1, q14→q15, q44→q45]; cierre λ añade {q5, q10, q6, q8, q16, q42, q38, q40, q49, q51, q52}
- Lee `1`: {q1, q5, q10, q6, q8, q15, q16, q42, q38, q40, q45, q49, q51, q52} ⟶ {q4, q0, q2, q9, q11, q13, q14, q17, q30, q22, q18, q20, q31, q41, q43, q48, q44, q46, q77} [q16→q17, q40→q41, q8→q9]; cierre λ añade {q4, q0, q2, q11, q13, q14, q30, q22, q18, q20, q31, q43, q48, q44, q46, q77}
- Lee `1`: {q4, q0, q2, q9, q11, q13, q14, q17, q30, q22, q18, q20, q31, q41, q43, q48, q44, q46, q77} ⟶ {q3, q5, q10, q6, q8, q21, q23, q28, q24, q26, q42, q38, q40, q47, q49, q51, q52} [q2→q3, q20→q21, q46→q47]; cierre λ añade {q5, q10, q6, q8, q23, q28, q24, q26, q42, q38, q40, q49, q51, q52}
- **Rechazada**: ningún estado de {q3, q5, q10, q6, q8, q21, q23, q28, q24, q26, q42, q38, q40, q47, q49, q51, q52} es de aceptación.

## Cadena `11110000`

- Inicio: {q76}; con cierre λ, {q76, q12, q4, q0, q2, q13, q14, q36, q32, q34}
- Lee `1`: {q76, q12, q4, q0, q2, q13, q14, q36, q32, q34} ⟶ {q3, q5, q10, q6, q8, q35, q37, q50, q42, q38, q40, q51, q52} [q2→q3, q34→q35]; cierre λ añade {q5, q10, q6, q8, q37, q50, q42, q38, q40, q51, q52}
- Lee `1`: {q3, q5, q10, q6, q8, q35, q37, q50, q42, q38, q40, q51, q52} ⟶ {q4, q0, q2, q9, q11, q13, q14, q41, q43, q48, q44, q46} [q40→q41, q8→q9]; cierre λ añade {q4, q0, q2, q11, q13, q14, q43, q48, q44, q46}
- Lee `1`: {q4, q0, q2, q9, q11, q13, q14, q41, q43, q48, q44, q46} ⟶ {q3, q5, q10, q6, q8, q42, q38, q40, q47, q49, q51, q52} [q2→q3, q46→q47]; cierre λ añade {q5, q10, q6, q8, q42, q38, q40, q49, q51, q52}
- Lee `1`: {q3, q5, q10, q6, q8, q42, q38, q40, q47, q49, q51, q52} ⟶ {q4, q0, q2, q9, q11, q13, q14, q41, q43, q48, q44, q46} [q40→q41, q8→q9]; cierre λ añade {q4, q0, q2, q11, q13, q14, q43, q48, q44, q46}
- Lee `0`: {q4, q0, q2, q9, q11, q13, q14, q41, q43, q48, q44, q46} ⟶ {q1, q5, q10, q6, q8, q15, q16, q42, q38, q40, q45, q49, q51, q52} [q0→q1, q14→q15, q44→q45]; cierre λ añade {q5, q10, q6, q8, q16, q42, q38, q40, q49, q51, q52}
- Lee `0`: {q1, q5, q10, q6, q8, q15, q16, q42, q38, q40, q45, q49, q51, q52} ⟶ {q4, q0, q2, q7, q11, q13, q14, q39, q43, q48, q44, q46, q53, q54} [q38→q39, q52→q53, q6→q7]; cierre λ añade {q4, q0, q2, q11, q13, q14, q43, q48, q44, q46, q54}
- Lee `0`: {q4, q0, q2, q7, q11, q13, q14, q39, q43, q48, q44, q46, q53, q54} ⟶ {q1, q5, q10, q6, q8, q15, q16, q42, q38, q40, q45, q49, q51, q52} [q0→q1, q14→q15, q44→q45]; cierre λ añade {q5, q10, q6, q8, q16, q42, q38, q40, q49, q51, q52}
- Lee `0`: {q1, q5, q10, q6, q8, q15, q16, q42, q38, q40, q45, q49, q51, q52} ⟶ {q4, q0, q2, q7, q11, q13, q14, q39, q43, q48, q44, q46, q53, q54} [q38→q39, q52→q53, q6→q7]; cierre λ añade {q4, q0, q2, q11, q13, q14, q43, q48, q44, q46, q54}
- **Rechazada**: ningún estado de {q4, q0, q2, q7, q11, q13, q14, q39, q43, q48, q44, q46, q53, q54} es de aceptación.
