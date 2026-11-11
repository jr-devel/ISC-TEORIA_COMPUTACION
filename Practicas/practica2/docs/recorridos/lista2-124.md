# Recorridos: Lista 2 · Ejercicio 124

Mecanismo de tres palancas con canicas (Σ = {0, 1}); se acepta si la última canica sale por A.

Autómata: `lista2-124` (AFD).

## Cadena `0`

- Inicio: {III}
- Lee `0`: {III} ⟶ {DIIa} [III→DIIa]
- **Aceptada**: queda {DIIa} ∈ F.

## Cadena `01`

- Inicio: {III}
- Lee `0`: {III} ⟶ {DIIa} [III→DIIa]
- Lee `1`: {DIIa} ⟶ {DDDa} [DIIa→DDDa]
- **Aceptada**: queda {DDDa} ∈ F.

## Cadena `0010`

- Inicio: {III}
- Lee `0`: {III} ⟶ {DIIa} [III→DIIa]
- Lee `0`: {DIIa} ⟶ {IIDa} [DIIa→IIDa]
- Lee `1`: {IIDa} ⟶ {IDIr} [IIDa→IDIr]
- Lee `0`: {IDIr} ⟶ {DDIa} [IDIr→DDIa]
- **Aceptada**: queda {DDIa} ∈ F.

## Cadena `010110`

- Inicio: {III}
- Lee `0`: {III} ⟶ {DIIa} [III→DIIa]
- Lee `1`: {DIIa} ⟶ {DDDa} [DIIa→DDDa]
- Lee `0`: {DDDa} ⟶ {IDIr} [DDDa→IDIr]
- Lee `1`: {IDIr} ⟶ {IIIr} [IDIr→IIIr]
- Lee `1`: {IIIr} ⟶ {IDDa} [IIIr→IDDa]
- Lee `0`: {IDDa} ⟶ {DDDa} [IDDa→DDDa]
- **Aceptada**: queda {DDDa} ∈ F.

## Cadena `101101100`

- Inicio: {III}
- Lee `1`: {III} ⟶ {IDDa} [III→IDDa]
- Lee `0`: {IDDa} ⟶ {DDDa} [IDDa→DDDa]
- Lee `1`: {DDDa} ⟶ {DIDr} [DDDa→DIDr]
- Lee `1`: {DIDr} ⟶ {DDIr} [DIDr→DDIr]
- Lee `0`: {DDIr} ⟶ {IDDa} [DDIr→IDDa]
- Lee `1`: {IDDa} ⟶ {IIDr} [IDDa→IIDr]
- Lee `1`: {IIDr} ⟶ {IDIr} [IIDr→IDIr]
- Lee `0`: {IDIr} ⟶ {DDIa} [IDIr→DDIa]
- Lee `0`: {DDIa} ⟶ {IDDa} [DDIa→IDDa]
- **Aceptada**: queda {IDDa} ∈ F.

## Cadena λ

- Inicio: {III}
- **Rechazada**: ningún estado de {III} es de aceptación.

## Cadena `1010`

- Inicio: {III}
- Lee `1`: {III} ⟶ {IDDa} [III→IDDa]
- Lee `0`: {IDDa} ⟶ {DDDa} [IDDa→DDDa]
- Lee `1`: {DDDa} ⟶ {DIDr} [DDDa→DIDr]
- Lee `0`: {DIDr} ⟶ {IIIr} [DIDr→IIIr]
- **Rechazada**: ningún estado de {IIIr} es de aceptación.

## Cadena `00101`

- Inicio: {III}
- Lee `0`: {III} ⟶ {DIIa} [III→DIIa]
- Lee `0`: {DIIa} ⟶ {IIDa} [DIIa→IIDa]
- Lee `1`: {IIDa} ⟶ {IDIr} [IIDa→IDIr]
- Lee `0`: {IDIr} ⟶ {DDIa} [IDIr→DDIa]
- Lee `1`: {DDIa} ⟶ {DIIr} [DDIa→DIIr]
- **Rechazada**: ningún estado de {DIIr} es de aceptación.

## Cadena `001111`

- Inicio: {III}
- Lee `0`: {III} ⟶ {DIIa} [III→DIIa]
- Lee `0`: {DIIa} ⟶ {IIDa} [DIIa→IIDa]
- Lee `1`: {IIDa} ⟶ {IDIr} [IIDa→IDIr]
- Lee `1`: {IDIr} ⟶ {IIIr} [IDIr→IIIr]
- Lee `1`: {IIIr} ⟶ {IDDa} [IIIr→IDDa]
- Lee `1`: {IDDa} ⟶ {IIDr} [IDDa→IIDr]
- **Rechazada**: ningún estado de {IIDr} es de aceptación.

## Cadena `01000001`

- Inicio: {III}
- Lee `0`: {III} ⟶ {DIIa} [III→DIIa]
- Lee `1`: {DIIa} ⟶ {DDDa} [DIIa→DDDa]
- Lee `0`: {DDDa} ⟶ {IDIr} [DDDa→IDIr]
- Lee `0`: {IDIr} ⟶ {DDIa} [IDIr→DDIa]
- Lee `0`: {DDIa} ⟶ {IDDa} [DDIa→IDDa]
- Lee `0`: {IDDa} ⟶ {DDDa} [IDDa→DDDa]
- Lee `0`: {DDDa} ⟶ {IDIr} [DDDa→IDIr]
- Lee `1`: {IDIr} ⟶ {IIIr} [IDIr→IIIr]
- **Rechazada**: ningún estado de {IIIr} es de aceptación.
