# Recorridos: Lista 2 · Ejercicio 108

Las palabras de Σ2 que incluyen abbcb y cbaabb sin traslaparse (abbcbaabb no pertenece).

Autómata: `lista2-108` (AFD).

## Cadena `cbaabbabbcb`

- Inicio: {[λ ; λ]}
- Lee `c`: {[λ ; λ]} ⟶ {[λ ; c]} [[λ ; λ]→[λ ; c]]
- Lee `b`: {[λ ; c]} ⟶ {[λ ; cb]} [[λ ; c]→[λ ; cb]]
- Lee `a`: {[λ ; cb]} ⟶ {[a ; cba]} [[λ ; cb]→[a ; cba]]
- Lee `a`: {[a ; cba]} ⟶ {[a ; cbaa]} [[a ; cba]→[a ; cbaa]]
- Lee `b`: {[a ; cbaa]} ⟶ {[ab ; cbaab]} [[a ; cbaa]→[ab ; cbaab]]
- Lee `b`: {[ab ; cbaab]} ⟶ {[abb ; cbaabb|λ]} [[ab ; cbaab]→[abb ; cbaabb|λ]]
- Lee `a`: {[abb ; cbaabb|λ]} ⟶ {[a ; cbaabb|a]} [[abb ; cbaabb|λ]→[a ; cbaabb|a]]
- Lee `b`: {[a ; cbaabb|a]} ⟶ {[ab ; cbaabb|ab]} [[a ; cbaabb|a]→[ab ; cbaabb|ab]]
- Lee `b`: {[ab ; cbaabb|ab]} ⟶ {[abb ; cbaabb|abb]} [[ab ; cbaabb|ab]→[abb ; cbaabb|abb]]
- Lee `c`: {[abb ; cbaabb|abb]} ⟶ {[abbc ; cbaabb|abbc]} [[abb ; cbaabb|abb]→[abbc ; cbaabb|abbc]]
- Lee `b`: {[abbc ; cbaabb|abbc]} ⟶ {[abbcb|λ ; ✓]} [[abbc ; cbaabb|abbc]→[abbcb|λ ; ✓]]
- **Aceptada**: queda {[abbcb|λ ; ✓]} ∈ F.

## Cadena `0cbaabbabbcb`

- Inicio: {[λ ; λ]}
- Lee `0`: {[λ ; λ]} ⟶ {[λ ; λ]} [[λ ; λ]→[λ ; λ]]
- Lee `c`: {[λ ; λ]} ⟶ {[λ ; c]} [[λ ; λ]→[λ ; c]]
- Lee `b`: {[λ ; c]} ⟶ {[λ ; cb]} [[λ ; c]→[λ ; cb]]
- Lee `a`: {[λ ; cb]} ⟶ {[a ; cba]} [[λ ; cb]→[a ; cba]]
- Lee `a`: {[a ; cba]} ⟶ {[a ; cbaa]} [[a ; cba]→[a ; cbaa]]
- Lee `b`: {[a ; cbaa]} ⟶ {[ab ; cbaab]} [[a ; cbaa]→[ab ; cbaab]]
- Lee `b`: {[ab ; cbaab]} ⟶ {[abb ; cbaabb|λ]} [[ab ; cbaab]→[abb ; cbaabb|λ]]
- Lee `a`: {[abb ; cbaabb|λ]} ⟶ {[a ; cbaabb|a]} [[abb ; cbaabb|λ]→[a ; cbaabb|a]]
- Lee `b`: {[a ; cbaabb|a]} ⟶ {[ab ; cbaabb|ab]} [[a ; cbaabb|a]→[ab ; cbaabb|ab]]
- Lee `b`: {[ab ; cbaabb|ab]} ⟶ {[abb ; cbaabb|abb]} [[ab ; cbaabb|ab]→[abb ; cbaabb|abb]]
- Lee `c`: {[abb ; cbaabb|abb]} ⟶ {[abbc ; cbaabb|abbc]} [[abb ; cbaabb|abb]→[abbc ; cbaabb|abbc]]
- Lee `b`: {[abbc ; cbaabb|abbc]} ⟶ {[abbcb|λ ; ✓]} [[abbc ; cbaabb|abbc]→[abbcb|λ ; ✓]]
- **Aceptada**: queda {[abbcb|λ ; ✓]} ∈ F.

## Cadena `0cbaabba0abbcb`

- Inicio: {[λ ; λ]}
- Lee `0`: {[λ ; λ]} ⟶ {[λ ; λ]} [[λ ; λ]→[λ ; λ]]
- Lee `c`: {[λ ; λ]} ⟶ {[λ ; c]} [[λ ; λ]→[λ ; c]]
- Lee `b`: {[λ ; c]} ⟶ {[λ ; cb]} [[λ ; c]→[λ ; cb]]
- Lee `a`: {[λ ; cb]} ⟶ {[a ; cba]} [[λ ; cb]→[a ; cba]]
- Lee `a`: {[a ; cba]} ⟶ {[a ; cbaa]} [[a ; cba]→[a ; cbaa]]
- Lee `b`: {[a ; cbaa]} ⟶ {[ab ; cbaab]} [[a ; cbaa]→[ab ; cbaab]]
- Lee `b`: {[ab ; cbaab]} ⟶ {[abb ; cbaabb|λ]} [[ab ; cbaab]→[abb ; cbaabb|λ]]
- Lee `a`: {[abb ; cbaabb|λ]} ⟶ {[a ; cbaabb|a]} [[abb ; cbaabb|λ]→[a ; cbaabb|a]]
- Lee `0`: {[a ; cbaabb|a]} ⟶ {[λ ; cbaabb|λ]} [[a ; cbaabb|a]→[λ ; cbaabb|λ]]
- Lee `a`: {[λ ; cbaabb|λ]} ⟶ {[a ; cbaabb|a]} [[λ ; cbaabb|λ]→[a ; cbaabb|a]]
- Lee `b`: {[a ; cbaabb|a]} ⟶ {[ab ; cbaabb|ab]} [[a ; cbaabb|a]→[ab ; cbaabb|ab]]
- Lee `b`: {[ab ; cbaabb|ab]} ⟶ {[abb ; cbaabb|abb]} [[ab ; cbaabb|ab]→[abb ; cbaabb|abb]]
- Lee `c`: {[abb ; cbaabb|abb]} ⟶ {[abbc ; cbaabb|abbc]} [[abb ; cbaabb|abb]→[abbc ; cbaabb|abbc]]
- Lee `b`: {[abbc ; cbaabb|abbc]} ⟶ {[abbcb|λ ; ✓]} [[abbc ; cbaabb|abbc]→[abbcb|λ ; ✓]]
- **Aceptada**: queda {[abbcb|λ ; ✓]} ∈ F.

## Cadena `0bacbaabbcabbcb1`

- Inicio: {[λ ; λ]}
- Lee `0`: {[λ ; λ]} ⟶ {[λ ; λ]} [[λ ; λ]→[λ ; λ]]
- Lee `b`: {[λ ; λ]} ⟶ {[λ ; λ]} [[λ ; λ]→[λ ; λ]]
- Lee `a`: {[λ ; λ]} ⟶ {[a ; λ]} [[λ ; λ]→[a ; λ]]
- Lee `c`: {[a ; λ]} ⟶ {[λ ; c]} [[a ; λ]→[λ ; c]]
- Lee `b`: {[λ ; c]} ⟶ {[λ ; cb]} [[λ ; c]→[λ ; cb]]
- Lee `a`: {[λ ; cb]} ⟶ {[a ; cba]} [[λ ; cb]→[a ; cba]]
- Lee `a`: {[a ; cba]} ⟶ {[a ; cbaa]} [[a ; cba]→[a ; cbaa]]
- Lee `b`: {[a ; cbaa]} ⟶ {[ab ; cbaab]} [[a ; cbaa]→[ab ; cbaab]]
- Lee `b`: {[ab ; cbaab]} ⟶ {[abb ; cbaabb|λ]} [[ab ; cbaab]→[abb ; cbaabb|λ]]
- Lee `c`: {[abb ; cbaabb|λ]} ⟶ {[abbc ; cbaabb|λ]} [[abb ; cbaabb|λ]→[abbc ; cbaabb|λ]]
- Lee `a`: {[abbc ; cbaabb|λ]} ⟶ {[a ; cbaabb|a]} [[abbc ; cbaabb|λ]→[a ; cbaabb|a]]
- Lee `b`: {[a ; cbaabb|a]} ⟶ {[ab ; cbaabb|ab]} [[a ; cbaabb|a]→[ab ; cbaabb|ab]]
- Lee `b`: {[ab ; cbaabb|ab]} ⟶ {[abb ; cbaabb|abb]} [[ab ; cbaabb|ab]→[abb ; cbaabb|abb]]
- Lee `c`: {[abb ; cbaabb|abb]} ⟶ {[abbc ; cbaabb|abbc]} [[abb ; cbaabb|abb]→[abbc ; cbaabb|abbc]]
- Lee `b`: {[abbc ; cbaabb|abbc]} ⟶ {[abbcb|λ ; ✓]} [[abbc ; cbaabb|abbc]→[abbcb|λ ; ✓]]
- Lee `1`: {[abbcb|λ ; ✓]} ⟶ {[abbcb|λ ; ✓]} [[abbcb|λ ; ✓]→[abbcb|λ ; ✓]]
- **Aceptada**: queda {[abbcb|λ ; ✓]} ∈ F.

## Cadena `c1cbaabbabbcbca11`

- Inicio: {[λ ; λ]}
- Lee `c`: {[λ ; λ]} ⟶ {[λ ; c]} [[λ ; λ]→[λ ; c]]
- Lee `1`: {[λ ; c]} ⟶ {[λ ; λ]} [[λ ; c]→[λ ; λ]]
- Lee `c`: {[λ ; λ]} ⟶ {[λ ; c]} [[λ ; λ]→[λ ; c]]
- Lee `b`: {[λ ; c]} ⟶ {[λ ; cb]} [[λ ; c]→[λ ; cb]]
- Lee `a`: {[λ ; cb]} ⟶ {[a ; cba]} [[λ ; cb]→[a ; cba]]
- Lee `a`: {[a ; cba]} ⟶ {[a ; cbaa]} [[a ; cba]→[a ; cbaa]]
- Lee `b`: {[a ; cbaa]} ⟶ {[ab ; cbaab]} [[a ; cbaa]→[ab ; cbaab]]
- Lee `b`: {[ab ; cbaab]} ⟶ {[abb ; cbaabb|λ]} [[ab ; cbaab]→[abb ; cbaabb|λ]]
- Lee `a`: {[abb ; cbaabb|λ]} ⟶ {[a ; cbaabb|a]} [[abb ; cbaabb|λ]→[a ; cbaabb|a]]
- Lee `b`: {[a ; cbaabb|a]} ⟶ {[ab ; cbaabb|ab]} [[a ; cbaabb|a]→[ab ; cbaabb|ab]]
- Lee `b`: {[ab ; cbaabb|ab]} ⟶ {[abb ; cbaabb|abb]} [[ab ; cbaabb|ab]→[abb ; cbaabb|abb]]
- Lee `c`: {[abb ; cbaabb|abb]} ⟶ {[abbc ; cbaabb|abbc]} [[abb ; cbaabb|abb]→[abbc ; cbaabb|abbc]]
- Lee `b`: {[abbc ; cbaabb|abbc]} ⟶ {[abbcb|λ ; ✓]} [[abbc ; cbaabb|abbc]→[abbcb|λ ; ✓]]
- Lee `c`: {[abbcb|λ ; ✓]} ⟶ {[abbcb|c ; ✓]} [[abbcb|λ ; ✓]→[abbcb|c ; ✓]]
- Lee `a`: {[abbcb|c ; ✓]} ⟶ {[abbcb|λ ; ✓]} [[abbcb|c ; ✓]→[abbcb|λ ; ✓]]
- Lee `1`: {[abbcb|λ ; ✓]} ⟶ {[abbcb|λ ; ✓]} [[abbcb|λ ; ✓]→[abbcb|λ ; ✓]]
- Lee `1`: {[abbcb|λ ; ✓]} ⟶ {[abbcb|λ ; ✓]} [[abbcb|λ ; ✓]→[abbcb|λ ; ✓]]
- **Aceptada**: queda {[abbcb|λ ; ✓]} ∈ F.

## Cadena λ

- Inicio: {[λ ; λ]}
- **Rechazada**: ningún estado de {[λ ; λ]} es de aceptación.

## Cadena `b`

- Inicio: {[λ ; λ]}
- Lee `b`: {[λ ; λ]} ⟶ {[λ ; λ]} [[λ ; λ]→[λ ; λ]]
- **Rechazada**: ningún estado de {[λ ; λ]} es de aceptación.

## Cadena `acb`

- Inicio: {[λ ; λ]}
- Lee `a`: {[λ ; λ]} ⟶ {[a ; λ]} [[λ ; λ]→[a ; λ]]
- Lee `c`: {[a ; λ]} ⟶ {[λ ; c]} [[a ; λ]→[λ ; c]]
- Lee `b`: {[λ ; c]} ⟶ {[λ ; cb]} [[λ ; c]→[λ ; cb]]
- **Rechazada**: ningún estado de {[λ ; cb]} es de aceptación.

## Cadena `ababc`

- Inicio: {[λ ; λ]}
- Lee `a`: {[λ ; λ]} ⟶ {[a ; λ]} [[λ ; λ]→[a ; λ]]
- Lee `b`: {[a ; λ]} ⟶ {[ab ; λ]} [[a ; λ]→[ab ; λ]]
- Lee `a`: {[ab ; λ]} ⟶ {[a ; λ]} [[ab ; λ]→[a ; λ]]
- Lee `b`: {[a ; λ]} ⟶ {[ab ; λ]} [[a ; λ]→[ab ; λ]]
- Lee `c`: {[ab ; λ]} ⟶ {[λ ; c]} [[ab ; λ]→[λ ; c]]
- **Rechazada**: ningún estado de {[λ ; c]} es de aceptación.

## Cadena `0bc11caa`

- Inicio: {[λ ; λ]}
- Lee `0`: {[λ ; λ]} ⟶ {[λ ; λ]} [[λ ; λ]→[λ ; λ]]
- Lee `b`: {[λ ; λ]} ⟶ {[λ ; λ]} [[λ ; λ]→[λ ; λ]]
- Lee `c`: {[λ ; λ]} ⟶ {[λ ; c]} [[λ ; λ]→[λ ; c]]
- Lee `1`: {[λ ; c]} ⟶ {[λ ; λ]} [[λ ; c]→[λ ; λ]]
- Lee `1`: {[λ ; λ]} ⟶ {[λ ; λ]} [[λ ; λ]→[λ ; λ]]
- Lee `c`: {[λ ; λ]} ⟶ {[λ ; c]} [[λ ; λ]→[λ ; c]]
- Lee `a`: {[λ ; c]} ⟶ {[a ; λ]} [[λ ; c]→[a ; λ]]
- Lee `a`: {[a ; λ]} ⟶ {[a ; λ]} [[a ; λ]→[a ; λ]]
- **Rechazada**: ningún estado de {[a ; λ]} es de aceptación.

## Cadena `bab1a0100b`

- Inicio: {[λ ; λ]}
- Lee `b`: {[λ ; λ]} ⟶ {[λ ; λ]} [[λ ; λ]→[λ ; λ]]
- Lee `a`: {[λ ; λ]} ⟶ {[a ; λ]} [[λ ; λ]→[a ; λ]]
- Lee `b`: {[a ; λ]} ⟶ {[ab ; λ]} [[a ; λ]→[ab ; λ]]
- Lee `1`: {[ab ; λ]} ⟶ {[λ ; λ]} [[ab ; λ]→[λ ; λ]]
- Lee `a`: {[λ ; λ]} ⟶ {[a ; λ]} [[λ ; λ]→[a ; λ]]
- Lee `0`: {[a ; λ]} ⟶ {[λ ; λ]} [[a ; λ]→[λ ; λ]]
- Lee `1`: {[λ ; λ]} ⟶ {[λ ; λ]} [[λ ; λ]→[λ ; λ]]
- Lee `0`: {[λ ; λ]} ⟶ {[λ ; λ]} [[λ ; λ]→[λ ; λ]]
- Lee `0`: {[λ ; λ]} ⟶ {[λ ; λ]} [[λ ; λ]→[λ ; λ]]
- Lee `b`: {[λ ; λ]} ⟶ {[λ ; λ]} [[λ ; λ]→[λ ; λ]]
- **Rechazada**: ningún estado de {[λ ; λ]} es de aceptación.
