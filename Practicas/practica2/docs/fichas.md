# Fichas de diseño y pruebas de las Listas 2 y 3

Cada ficha documenta el diseño, la tabla de transiciones y las cinco cadenas válidas y cinco inválidas, con el resultado obtenido en el simulador. El recorrido completo de cada cadena (estados activos en cada paso, transiciones usadas y bifurcaciones) está en `docs/recorridos/`, un archivo por ejercicio.

## Lista 2 · Ejercicio 094

**Enunciado.** Las palabras de Σ1 que comienzan con 1 y terminan con 2.

**Clase.** AFD: Cada par (estado, símbolo) tiene a lo sumo un destino y no hay transiciones λ. **Archivos.** `automatas/afd/lista2-094.jff` (y `.json`, `.xml`).

**Diseño.** El primer símbolo decide si la cadena puede pertenecer; después sólo importa si el último símbolo es 2.

| δ      | 0      | 1      | 2      | Qué recuerda del prefijo leído           |
|--------|--------|--------|--------|------------------------------------------|
| → ini  | muerto | 1·     | muerto | no se ha leído nada                      |
| muerto | muerto | muerto | muerto | no empezó con 1                          |
| 1·     | 1·     | 1·     | 1·2    | empezó con 1 y el último símbolo no es 2 |
| \* 1·2 | 1·     | 1·     | 1·2    | empezó con 1 y el último símbolo es 2    |

Tabla de transiciones (→ inicial, \* aceptación, — sin transición).

| Cadena       | Longitud | Esperado | Obtenido | Tipo de caso                                     |
|--------------|:--------:|----------|----------|--------------------------------------------------|
| `12`         |    2     | acepta   | acepta   | válida                                           |
| `102`        |    3     | acepta   | acepta   | válida                                           |
| `10022`      |    5     | acepta   | acepta   | válida                                           |
| `1220222`    |    7     | acepta   | acepta   | válida                                           |
| `1212021222` |    10    | acepta   | acepta   | válida                                           |
| λ            |    0     | rechaza  | rechaza  | inválida                                         |
| `0`          |    1     | rechaza  | rechaza  | inválida                                         |
| `020`        |    3     | rechaza  | rechaza  | inválida                                         |
| `22202`      |    5     | rechaza  | rechaza  | inválida                                         |
| `10012011`   |    8     | rechaza  | rechaza  | inválida                                         |
| `2`          |    1     | rechaza  | rechaza  | frontera: justo por debajo de la longitud mínima |

Cadenas de prueba.

## Lista 2 · Ejercicio 095

**Enunciado.** Las palabras de Σ1 que tienen longitud 4.

**Clase.** AFD: Cada par (estado, símbolo) tiene a lo sumo un destino y no hay transiciones λ. **Archivos.** `automatas/afd/lista2-095.jff` (y `.json`, `.xml`).

**Diseño.** Un contador de longitud saturado en 5.

| δ      | 0      | 1      | 2      | Qué recuerda del prefijo leído |
|--------|--------|--------|--------|--------------------------------|
| → L0   | L1     | L1     | L1     | se han leído 0 símbolos        |
| L1     | L2     | L2     | L2     | se han leído 1 símbolos        |
| L2     | L3     | L3     | L3     | se han leído 2 símbolos        |
| L3     | L4     | L4     | L4     | se han leído 3 símbolos        |
| \* L4  | muerto | muerto | muerto | se han leído 4 símbolos        |
| muerto | muerto | muerto | muerto | la longitud ya pasó de 4       |

Tabla de transiciones (→ inicial, \* aceptación, — sin transición).

| Cadena     | Longitud | Esperado | Obtenido | Tipo de caso                                     |
|------------|:--------:|----------|----------|--------------------------------------------------|
| `0201`     |    4     | acepta   | acepta   | válida                                           |
| `1202`     |    4     | acepta   | acepta   | válida                                           |
| `1220`     |    4     | acepta   | acepta   | válida                                           |
| `2200`     |    4     | acepta   | acepta   | válida                                           |
| `2221`     |    4     | acepta   | acepta   | válida                                           |
| λ          |    0     | rechaza  | rechaza  | inválida                                         |
| `2`        |    1     | rechaza  | rechaza  | inválida                                         |
| `101`      |    3     | rechaza  | rechaza  | inválida                                         |
| `22002`    |    5     | rechaza  | rechaza  | inválida                                         |
| `00021210` |    8     | rechaza  | rechaza  | inválida                                         |
| `0210`     |    4     | acepta   | acepta   | frontera: aceptada más corta                     |
| `220`      |    3     | rechaza  | rechaza  | frontera: justo por debajo de la longitud mínima |

Cadenas de prueba.

## Lista 2 · Ejercicio 096

**Enunciado.** Las palabras de Σ1 con prefijo 20 y longitud 4.

**Clase.** AFD: Cada par (estado, símbolo) tiene a lo sumo un destino y no hay transiciones λ. **Archivos.** `automatas/afd/lista2-096.jff` (y `.json`, `.xml`).

**Diseño.** Los dos primeros estados verifican el prefijo 20 y los dos siguientes cuentan la longitud.

| δ      | 0      | 1      | 2      | Qué recuerda del prefijo leído                            |
|--------|--------|--------|--------|-----------------------------------------------------------|
| → L0   | muerto | muerto | L1     | se han leído 0 símbolos y el prefijo es compatible con 20 |
| muerto | muerto | muerto | muerto | prefijo distinto de 20 o longitud mayor que 4             |
| L1     | L2     | muerto | muerto | se han leído 1 símbolos y el prefijo es compatible con 20 |
| L2     | L3     | L3     | L3     | se han leído 2 símbolos y el prefijo es compatible con 20 |
| L3     | L4     | L4     | L4     | se han leído 3 símbolos y el prefijo es compatible con 20 |
| \* L4  | muerto | muerto | muerto | se han leído 4 símbolos y el prefijo es compatible con 20 |

Tabla de transiciones (→ inicial, \* aceptación, — sin transición).

| Cadena     | Longitud | Esperado | Obtenido | Tipo de caso                                     |
|------------|:--------:|----------|----------|--------------------------------------------------|
| `2000`     |    4     | acepta   | acepta   | válida                                           |
| `2001`     |    4     | acepta   | acepta   | válida                                           |
| `2002`     |    4     | acepta   | acepta   | válida                                           |
| `2011`     |    4     | acepta   | acepta   | válida                                           |
| `2021`     |    4     | acepta   | acepta   | válida                                           |
| λ          |    0     | rechaza  | rechaza  | inválida                                         |
| `2`        |    1     | rechaza  | rechaza  | inválida                                         |
| `101`      |    3     | rechaza  | rechaza  | inválida                                         |
| `20100`    |    5     | rechaza  | rechaza  | inválida                                         |
| `20122121` |    8     | rechaza  | rechaza  | inválida                                         |
| `2012`     |    4     | acepta   | acepta   | frontera: aceptada más corta                     |
| `210`      |    3     | rechaza  | rechaza  | frontera: justo por debajo de la longitud mínima |

Cadenas de prueba.

## Lista 2 · Ejercicio 097

**Enunciado.** Las palabras de Σ1 cuya longitud es un múltiplo de 3.

**Clase.** AFD: Cada par (estado, símbolo) tiene a lo sumo un destino y no hay transiciones λ. **Archivos.** `automatas/afd/lista2-097.jff` (y `.json`, `.xml`).

**Diseño.** Basta recordar la longitud módulo 3; λ tiene longitud 0, que es múltiplo de 3.

| δ      | 0   | 1   | 2   | Qué recuerda del prefijo leído   |
|--------|-----|-----|-----|----------------------------------|
| →\* r0 | r1  | r1  | r1  | la longitud leída es ≡ 0 (mod 3) |
| r1     | r2  | r2  | r2  | la longitud leída es ≡ 1 (mod 3) |
| r2     | r0  | r0  | r0  | la longitud leída es ≡ 2 (mod 3) |

Tabla de transiciones (→ inicial, \* aceptación, — sin transición).

| Cadena      | Longitud | Esperado | Obtenido | Tipo de caso |
|-------------|:--------:|----------|----------|--------------|
| λ           |    0     | acepta   | acepta   | válida       |
| `212200`    |    6     | acepta   | acepta   | válida       |
| `100022002` |    9     | acepta   | acepta   | válida       |
| `120000112` |    9     | acepta   | acepta   | válida       |
| `222022020` |    9     | acepta   | acepta   | válida       |
| `1`         |    1     | rechaza  | rechaza  | inválida     |
| `20`        |    2     | rechaza  | rechaza  | inválida     |
| `0100`      |    4     | rechaza  | rechaza  | inválida     |
| `0102`      |    4     | rechaza  | rechaza  | inválida     |
| `00110`     |    5     | rechaza  | rechaza  | inválida     |

Cadenas de prueba.

## Lista 2 · Ejercicio 098

**Enunciado.** Las palabras de Σ1 que terminan con la cadena 00102.

**Clase.** AFD: Cada par (estado, símbolo) tiene a lo sumo un destino y no hay transiciones λ. **Archivos.** `automatas/afd/lista2-098.jff` (y `.json`, `.xml`).

**Diseño.** Autómata de búsqueda de patrones (Knuth-Morris-Pratt): cada estado guarda el sufijo más largo leído que es prefijo de 00102; se acepta cuando ese sufijo es el patrón completo.

| δ        | 0    | 1   | 2     | Qué recuerda del prefijo leído                                                              |
|----------|------|-----|-------|---------------------------------------------------------------------------------------------|
| → λ      | 0    | λ   | λ     | el sufijo más largo leído que es prefijo de 00102 es λ                                      |
| 0        | 00   | λ   | λ     | el sufijo más largo leído que es prefijo de 00102 es 0                                      |
| 00       | 00   | 001 | λ     | el sufijo más largo leído que es prefijo de 00102 es 00                                     |
| 001      | 0010 | λ   | λ     | el sufijo más largo leído que es prefijo de 00102 es 001                                    |
| 0010     | 00   | λ   | 00102 | el sufijo más largo leído que es prefijo de 00102 es 0010                                   |
| \* 00102 | 0    | λ   | λ     | el sufijo más largo leído que es prefijo de 00102 es 00102 (la cadena termina en el patrón) |

Tabla de transiciones (→ inicial, \* aceptación, — sin transición).

| Cadena          | Longitud | Esperado | Obtenido | Tipo de caso                                     |
|-----------------|:--------:|----------|----------|--------------------------------------------------|
| `00102`         |    5     | acepta   | acepta   | válida                                           |
| `000102`        |    6     | acepta   | acepta   | válida                                           |
| `00000102`      |    8     | acepta   | acepta   | válida                                           |
| `0101000102`    |    10    | acepta   | acepta   | válida                                           |
| `2220001100102` |    13    | acepta   | acepta   | válida                                           |
| λ               |    0     | rechaza  | rechaza  | inválida                                         |
| `0`             |    1     | rechaza  | rechaza  | inválida                                         |
| `202`           |    3     | rechaza  | rechaza  | inválida                                         |
| `11021`         |    5     | rechaza  | rechaza  | inválida                                         |
| `12222012`      |    8     | rechaza  | rechaza  | inválida                                         |
| `0201`          |    4     | rechaza  | rechaza  | frontera: justo por debajo de la longitud mínima |

Cadenas de prueba.

## Lista 2 · Ejercicio 099

**Enunciado.** Las palabras de Σ1 que terminan con la cadena 001001.

**Clase.** AFD: Cada par (estado, símbolo) tiene a lo sumo un destino y no hay transiciones λ. **Archivos.** `automatas/afd/lista2-099.jff` (y `.json`, `.xml`).

**Diseño.** Autómata de búsqueda de patrones (Knuth-Morris-Pratt): cada estado guarda el sufijo más largo leído que es prefijo de 001001; se acepta cuando ese sufijo es el patrón completo.

| δ         | 0     | 1      | 2   | Qué recuerda del prefijo leído                                                                |
|-----------|-------|--------|-----|-----------------------------------------------------------------------------------------------|
| → λ       | 0     | λ      | λ   | el sufijo más largo leído que es prefijo de 001001 es λ                                       |
| 0         | 00    | λ      | λ   | el sufijo más largo leído que es prefijo de 001001 es 0                                       |
| 00        | 00    | 001    | λ   | el sufijo más largo leído que es prefijo de 001001 es 00                                      |
| 001       | 0010  | λ      | λ   | el sufijo más largo leído que es prefijo de 001001 es 001                                     |
| 0010      | 00100 | λ      | λ   | el sufijo más largo leído que es prefijo de 001001 es 0010                                    |
| 00100     | 00    | 001001 | λ   | el sufijo más largo leído que es prefijo de 001001 es 00100                                   |
| \* 001001 | 0010  | λ      | λ   | el sufijo más largo leído que es prefijo de 001001 es 001001 (la cadena termina en el patrón) |

Tabla de transiciones (→ inicial, \* aceptación, — sin transición).

| Cadena           | Longitud | Esperado | Obtenido | Tipo de caso                                     |
|------------------|:--------:|----------|----------|--------------------------------------------------|
| `001001`         |    6     | acepta   | acepta   | válida                                           |
| `1001001`        |    7     | acepta   | acepta   | válida                                           |
| `120001001`      |    9     | acepta   | acepta   | válida                                           |
| `10212001001`    |    11    | acepta   | acepta   | válida                                           |
| `22102001001001` |    14    | acepta   | acepta   | válida                                           |
| λ                |    0     | rechaza  | rechaza  | inválida                                         |
| `1`              |    1     | rechaza  | rechaza  | inválida                                         |
| `002`            |    3     | rechaza  | rechaza  | inválida                                         |
| `11011`          |    5     | rechaza  | rechaza  | inválida                                         |
| `21012122`       |    8     | rechaza  | rechaza  | inválida                                         |
| `11111`          |    5     | rechaza  | rechaza  | frontera: justo por debajo de la longitud mínima |

Cadenas de prueba.

## Lista 2 · Ejercicio 100

**Enunciado.** Las palabras de Σ2 tales que el primer símbolo es una letra y el segundo es un dígito.

**Clase.** AFD: Cada par (estado, símbolo) tiene a lo sumo un destino y no hay transiciones λ. **Archivos.** `automatas/afd/lista2-100.jff` (y `.json`, `.xml`).

**Diseño.** Sólo importan los dos primeros símbolos; después el autómata se queda en el estado de aceptación.

| δ      | 0      | 1      | a      | b      | c      | Qué recuerda del prefijo leído               |
|--------|--------|--------|--------|--------|--------|----------------------------------------------|
| → ini  | muerto | muerto | letra  | letra  | letra  | no se ha leído nada                          |
| letra  | ok     | ok     | muerto | muerto | muerto | el primer símbolo es una letra               |
| muerto | muerto | muerto | muerto | muerto | muerto | los dos primeros no cumplen                  |
| \* ok  | ok     | ok     | ok     | ok     | ok     | los dos primeros símbolos son letra y dígito |

Tabla de transiciones (→ inicial, \* aceptación, — sin transición).

| Cadena       | Longitud | Esperado | Obtenido | Tipo de caso                                     |
|--------------|:--------:|----------|----------|--------------------------------------------------|
| `a1`         |    2     | acepta   | acepta   | válida                                           |
| `b1b`        |    3     | acepta   | acepta   | válida                                           |
| `c0aa0`      |    5     | acepta   | acepta   | válida                                           |
| `b00c1ac`    |    7     | acepta   | acepta   | válida                                           |
| `b1bb11cbb0` |    10    | acepta   | acepta   | válida                                           |
| λ            |    0     | rechaza  | rechaza  | inválida                                         |
| `b`          |    1     | rechaza  | rechaza  | inválida                                         |
| `0a0`        |    3     | rechaza  | rechaza  | inválida                                         |
| `1ac0a`      |    5     | rechaza  | rechaza  | inválida                                         |
| `0ca00ba0`   |    8     | rechaza  | rechaza  | inválida                                         |
| `b1`         |    2     | acepta   | acepta   | frontera: aceptada más corta                     |
| `1`          |    1     | rechaza  | rechaza  | frontera: justo por debajo de la longitud mínima |

Cadenas de prueba.

## Lista 2 · Ejercicio 101

**Enunciado.** Las palabras de Σ3 que contienen la cadena aba.

**Clase.** AFD: Cada par (estado, símbolo) tiene a lo sumo un destino y no hay transiciones λ. **Archivos.** `automatas/afd/lista2-101.jff` (y `.json`, `.xml`).

**Diseño.** Búsqueda de aba con el autómata de Knuth-Morris-Pratt; al completar el patrón el estado es absorbente.

| δ      | a   | b   | Qué recuerda del prefijo leído                                            |
|--------|-----|-----|---------------------------------------------------------------------------|
| → λ    | a   | λ   | aún no aparece aba; el sufijo más largo leído que es prefijo de aba es λ  |
| a      | a   | ab  | aún no aparece aba; el sufijo más largo leído que es prefijo de aba es a  |
| ab     | aba | λ   | aún no aparece aba; el sufijo más largo leído que es prefijo de aba es ab |
| \* aba | aba | aba | ya apareció aba                                                           |

Tabla de transiciones (→ inicial, \* aceptación, — sin transición).

| Cadena        | Longitud | Esperado | Obtenido | Tipo de caso                                     |
|---------------|:--------:|----------|----------|--------------------------------------------------|
| `aba`         |    3     | acepta   | acepta   | válida                                           |
| `aaba`        |    4     | acepta   | acepta   | válida                                           |
| `bbabaa`      |    6     | acepta   | acepta   | válida                                           |
| `bababbaa`    |    8     | acepta   | acepta   | válida                                           |
| `aaababaaaab` |    11    | acepta   | acepta   | válida                                           |
| λ             |    0     | rechaza  | rechaza  | inválida                                         |
| `b`           |    1     | rechaza  | rechaza  | inválida                                         |
| `aaa`         |    3     | rechaza  | rechaza  | inválida                                         |
| `bbbbb`       |    5     | rechaza  | rechaza  | inválida                                         |
| `bbaabbaa`    |    8     | rechaza  | rechaza  | inválida                                         |
| `ab`          |    2     | rechaza  | rechaza  | frontera: justo por debajo de la longitud mínima |

Cadenas de prueba.

## Lista 2 · Ejercicio 102

**Enunciado.** Las palabras de Σ3 que contienen la cadena abbbab.

**Clase.** AFD: Cada par (estado, símbolo) tiene a lo sumo un destino y no hay transiciones λ. **Archivos.** `automatas/afd/lista2-102.jff` (y `.json`, `.xml`).

**Diseño.** Búsqueda de abbbab con el autómata de Knuth-Morris-Pratt; al completar el patrón el estado es absorbente.

| δ         | a      | b      | Qué recuerda del prefijo leído                                                     |
|-----------|--------|--------|------------------------------------------------------------------------------------|
| → λ       | a      | λ      | aún no aparece abbbab; el sufijo más largo leído que es prefijo de abbbab es λ     |
| a         | a      | ab     | aún no aparece abbbab; el sufijo más largo leído que es prefijo de abbbab es a     |
| ab        | a      | abb    | aún no aparece abbbab; el sufijo más largo leído que es prefijo de abbbab es ab    |
| abb       | a      | abbb   | aún no aparece abbbab; el sufijo más largo leído que es prefijo de abbbab es abb   |
| abbb      | abbba  | λ      | aún no aparece abbbab; el sufijo más largo leído que es prefijo de abbbab es abbb  |
| abbba     | a      | abbbab | aún no aparece abbbab; el sufijo más largo leído que es prefijo de abbbab es abbba |
| \* abbbab | abbbab | abbbab | ya apareció abbbab                                                                 |

Tabla de transiciones (→ inicial, \* aceptación, — sin transición).

| Cadena           | Longitud | Esperado | Obtenido | Tipo de caso                                     |
|------------------|:--------:|----------|----------|--------------------------------------------------|
| `abbbab`         |    6     | acepta   | acepta   | válida                                           |
| `abbbaba`        |    7     | acepta   | acepta   | válida                                           |
| `aabbbabab`      |    9     | acepta   | acepta   | válida                                           |
| `babaaabbbab`    |    11    | acepta   | acepta   | válida                                           |
| `babbbababbbabb` |    14    | acepta   | acepta   | válida                                           |
| λ                |    0     | rechaza  | rechaza  | inválida                                         |
| `b`              |    1     | rechaza  | rechaza  | inválida                                         |
| `aab`            |    3     | rechaza  | rechaza  | inválida                                         |
| `bbbaa`          |    5     | rechaza  | rechaza  | inválida                                         |
| `aabaabaa`       |    8     | rechaza  | rechaza  | inválida                                         |
| `baaab`          |    5     | rechaza  | rechaza  | frontera: justo por debajo de la longitud mínima |

Cadenas de prueba.

## Lista 2 · Ejercicio 103

**Enunciado.** Las palabras de Σ3 que contienen la cadena aabbba.

**Clase.** AFD: Cada par (estado, símbolo) tiene a lo sumo un destino y no hay transiciones λ. **Archivos.** `automatas/afd/lista2-103.jff` (y `.json`, `.xml`).

**Diseño.** Búsqueda de aabbba con el autómata de Knuth-Morris-Pratt; al completar el patrón el estado es absorbente.

| δ         | a      | b      | Qué recuerda del prefijo leído                                                     |
|-----------|--------|--------|------------------------------------------------------------------------------------|
| → λ       | a      | λ      | aún no aparece aabbba; el sufijo más largo leído que es prefijo de aabbba es λ     |
| a         | aa     | λ      | aún no aparece aabbba; el sufijo más largo leído que es prefijo de aabbba es a     |
| aa        | aa     | aab    | aún no aparece aabbba; el sufijo más largo leído que es prefijo de aabbba es aa    |
| aab       | a      | aabb   | aún no aparece aabbba; el sufijo más largo leído que es prefijo de aabbba es aab   |
| aabb      | a      | aabbb  | aún no aparece aabbba; el sufijo más largo leído que es prefijo de aabbba es aabb  |
| aabbb     | aabbba | λ      | aún no aparece aabbba; el sufijo más largo leído que es prefijo de aabbba es aabbb |
| \* aabbba | aabbba | aabbba | ya apareció aabbba                                                                 |

Tabla de transiciones (→ inicial, \* aceptación, — sin transición).

| Cadena           | Longitud | Esperado | Obtenido | Tipo de caso                                     |
|------------------|:--------:|----------|----------|--------------------------------------------------|
| `aabbba`         |    6     | acepta   | acepta   | válida                                           |
| `aabbbab`        |    7     | acepta   | acepta   | válida                                           |
| `aaaabbbab`      |    9     | acepta   | acepta   | válida                                           |
| `ababbaabbba`    |    11    | acepta   | acepta   | válida                                           |
| `aaabbaabaabbba` |    14    | acepta   | acepta   | válida                                           |
| λ                |    0     | rechaza  | rechaza  | inválida                                         |
| `a`              |    1     | rechaza  | rechaza  | inválida                                         |
| `aab`            |    3     | rechaza  | rechaza  | inválida                                         |
| `aaaaa`          |    5     | rechaza  | rechaza  | inválida                                         |
| `baaaaabb`       |    8     | rechaza  | rechaza  | inválida                                         |
| `aabab`          |    5     | rechaza  | rechaza  | frontera: justo por debajo de la longitud mínima |

Cadenas de prueba.

## Lista 2 · Ejercicio 106

**Enunciado.** Las palabras de Σ1 que incluyen la subcadena 1101001.

**Clase.** AFD: Cada par (estado, símbolo) tiene a lo sumo un destino y no hay transiciones λ. **Archivos.** `automatas/afd/lista2-106.jff` (y `.json`, `.xml`).

**Diseño.** Búsqueda de 1101001 con el autómata de Knuth-Morris-Pratt; al completar el patrón el estado es absorbente.

| δ          | 0       | 1       | 2       | Qué recuerda del prefijo leído                                                        |
|------------|---------|---------|---------|---------------------------------------------------------------------------------------|
| → λ        | λ       | 1       | λ       | aún no aparece 1101001; el sufijo más largo leído que es prefijo de 1101001 es λ      |
| 1          | λ       | 11      | λ       | aún no aparece 1101001; el sufijo más largo leído que es prefijo de 1101001 es 1      |
| 11         | 110     | 11      | λ       | aún no aparece 1101001; el sufijo más largo leído que es prefijo de 1101001 es 11     |
| 110        | λ       | 1101    | λ       | aún no aparece 1101001; el sufijo más largo leído que es prefijo de 1101001 es 110    |
| 1101       | 11010   | 11      | λ       | aún no aparece 1101001; el sufijo más largo leído que es prefijo de 1101001 es 1101   |
| 11010      | 110100  | 1       | λ       | aún no aparece 1101001; el sufijo más largo leído que es prefijo de 1101001 es 11010  |
| 110100     | λ       | 1101001 | λ       | aún no aparece 1101001; el sufijo más largo leído que es prefijo de 1101001 es 110100 |
| \* 1101001 | 1101001 | 1101001 | 1101001 | ya apareció 1101001                                                                   |

Tabla de transiciones (→ inicial, \* aceptación, — sin transición).

| Cadena           | Longitud | Esperado | Obtenido | Tipo de caso                                     |
|------------------|:--------:|----------|----------|--------------------------------------------------|
| `1101001`        |    7     | acepta   | acepta   | válida                                           |
| `11010010`       |    8     | acepta   | acepta   | válida                                           |
| `0021101001`     |    10    | acepta   | acepta   | válida                                           |
| `111101001110`   |    12    | acepta   | acepta   | válida                                           |
| `11010012101111` |    14    | acepta   | acepta   | válida                                           |
| λ                |    0     | rechaza  | rechaza  | inválida                                         |
| `0`              |    1     | rechaza  | rechaza  | inválida                                         |
| `122`            |    3     | rechaza  | rechaza  | inválida                                         |
| `10110`          |    5     | rechaza  | rechaza  | inválida                                         |
| `22012221`       |    8     | rechaza  | rechaza  | inválida                                         |
| `101012`         |    6     | rechaza  | rechaza  | frontera: justo por debajo de la longitud mínima |

Cadenas de prueba.

## Lista 2 · Ejercicio 104

**Enunciado.** Las palabras de Σ3 que inician con la cadena abbab.

**Clase.** AFD: Cada par (estado, símbolo) tiene a lo sumo un destino y no hay transiciones λ. **Archivos.** `automatas/afd/lista2-104.jff` (y `.json`, `.xml`).

**Diseño.** Una cadena de estados verifica el prefijo; cualquier discrepancia lleva a muerto.

| δ        | a      | b      | Qué recuerda del prefijo leído                |
|----------|--------|--------|-----------------------------------------------|
| → λ      | a      | muerto | se han leído los primeros 0 símbolos de abbab |
| a        | muerto | ab     | se han leído los primeros 1 símbolos de abbab |
| muerto   | muerto | muerto | el prefijo leído no coincide con abbab        |
| ab       | muerto | abb    | se han leído los primeros 2 símbolos de abbab |
| abb      | abba   | muerto | se han leído los primeros 3 símbolos de abbab |
| abba     | muerto | abbab  | se han leído los primeros 4 símbolos de abbab |
| \* abbab | abbab  | abbab  | ya se leyó el prefijo abbab                   |

Tabla de transiciones (→ inicial, \* aceptación, — sin transición).

| Cadena          | Longitud | Esperado | Obtenido | Tipo de caso                                     |
|-----------------|:--------:|----------|----------|--------------------------------------------------|
| `abbab`         |    5     | acepta   | acepta   | válida                                           |
| `abbaba`        |    6     | acepta   | acepta   | válida                                           |
| `abbabaab`      |    8     | acepta   | acepta   | válida                                           |
| `abbabbabbb`    |    10    | acepta   | acepta   | válida                                           |
| `abbabbaaaabba` |    13    | acepta   | acepta   | válida                                           |
| λ               |    0     | rechaza  | rechaza  | inválida                                         |
| `a`             |    1     | rechaza  | rechaza  | inválida                                         |
| `bab`           |    3     | rechaza  | rechaza  | inválida                                         |
| `bbbba`         |    5     | rechaza  | rechaza  | inválida                                         |
| `aabbbaba`      |    8     | rechaza  | rechaza  | inválida                                         |
| `bbba`          |    4     | rechaza  | rechaza  | frontera: justo por debajo de la longitud mínima |

Cadenas de prueba.

## Lista 2 · Ejercicio 105

**Enunciado.** Las palabras de Σ3 que terminan con la cadena abaa.

**Clase.** AFD: Cada par (estado, símbolo) tiene a lo sumo un destino y no hay transiciones λ. **Archivos.** `automatas/afd/lista2-105.jff` (y `.json`, `.xml`).

**Diseño.** Autómata de Knuth-Morris-Pratt sin estado absorbente.

| δ       | a    | b   | Qué recuerda del prefijo leído                                                            |
|---------|------|-----|-------------------------------------------------------------------------------------------|
| → λ     | a    | λ   | el sufijo más largo leído que es prefijo de abaa es λ                                     |
| a       | a    | ab  | el sufijo más largo leído que es prefijo de abaa es a                                     |
| ab      | aba  | λ   | el sufijo más largo leído que es prefijo de abaa es ab                                    |
| aba     | abaa | ab  | el sufijo más largo leído que es prefijo de abaa es aba                                   |
| \* abaa | a    | ab  | el sufijo más largo leído que es prefijo de abaa es abaa (la cadena termina en el patrón) |

Tabla de transiciones (→ inicial, \* aceptación, — sin transición).

| Cadena         | Longitud | Esperado | Obtenido | Tipo de caso                                     |
|----------------|:--------:|----------|----------|--------------------------------------------------|
| `abaa`         |    4     | acepta   | acepta   | válida                                           |
| `aabaa`        |    5     | acepta   | acepta   | válida                                           |
| `bbaabaa`      |    7     | acepta   | acepta   | válida                                           |
| `aabababaa`    |    9     | acepta   | acepta   | válida                                           |
| `babbabbbabaa` |    12    | acepta   | acepta   | válida                                           |
| λ              |    0     | rechaza  | rechaza  | inválida                                         |
| `a`            |    1     | rechaza  | rechaza  | inválida                                         |
| `abb`          |    3     | rechaza  | rechaza  | inválida                                         |
| `baaaa`        |    5     | rechaza  | rechaza  | inválida                                         |
| `bababbaa`     |    8     | rechaza  | rechaza  | inválida                                         |
| `bbb`          |    3     | rechaza  | rechaza  | frontera: justo por debajo de la longitud mínima |

Cadenas de prueba.

## Lista 2 · Ejercicio 107

**Enunciado.** Las palabras de Σ1 que incluyen al menos una vez 0101 y al menos una vez 021.

**Clase.** AFD: Cada par (estado, símbolo) tiene a lo sumo un destino y no hay transiciones λ. **Archivos.** `automatas/afd/lista2-107.jff` (y `.json`, `.xml`).

**Diseño.** Producto de los autómatas que buscan 0101 y 021: cada estado es un par (avance en 0101, avance en 021).

| δ              | 0           | 1           | 2           | Qué recuerda del prefijo leído                |
|----------------|-------------|-------------|-------------|-----------------------------------------------|
| → (λ, λ)       | (0, 0)      | (λ, λ)      | (λ, λ)      | en el primer autómata λ, en el segundo λ      |
| (0, 0)         | (0, 0)      | (01, λ)     | (λ, 02)     | en el primer autómata 0, en el segundo 0      |
| (01, λ)        | (010, 0)    | (λ, λ)      | (λ, λ)      | en el primer autómata 01, en el segundo λ     |
| (λ, 02)        | (0, 0)      | (λ, 021)    | (λ, λ)      | en el primer autómata λ, en el segundo 02     |
| (010, 0)       | (0, 0)      | (0101, λ)   | (λ, 02)     | en el primer autómata 010, en el segundo 0    |
| (λ, 021)       | (0, 021)    | (λ, 021)    | (λ, 021)    | en el primer autómata λ, en el segundo 021    |
| (0101, λ)      | (0101, 0)   | (0101, λ)   | (0101, λ)   | en el primer autómata 0101, en el segundo λ   |
| (0, 021)       | (0, 021)    | (01, 021)   | (λ, 021)    | en el primer autómata 0, en el segundo 021    |
| (0101, 0)      | (0101, 0)   | (0101, λ)   | (0101, 02)  | en el primer autómata 0101, en el segundo 0   |
| (01, 021)      | (010, 021)  | (λ, 021)    | (λ, 021)    | en el primer autómata 01, en el segundo 021   |
| (0101, 02)     | (0101, 0)   | (0101, 021) | (0101, λ)   | en el primer autómata 0101, en el segundo 02  |
| (010, 021)     | (0, 021)    | (0101, 021) | (λ, 021)    | en el primer autómata 010, en el segundo 021  |
| \* (0101, 021) | (0101, 021) | (0101, 021) | (0101, 021) | en el primer autómata 0101, en el segundo 021 |

Tabla de transiciones (→ inicial, \* aceptación, — sin transición).

| Cadena           | Longitud | Esperado | Obtenido | Tipo de caso                                     |
|------------------|:--------:|----------|----------|--------------------------------------------------|
| `0101021`        |    7     | acepta   | acepta   | válida                                           |
| `01012021`       |    8     | acepta   | acepta   | válida                                           |
| `0101002120`     |    10    | acepta   | acepta   | válida                                           |
| `012010120210`   |    12    | acepta   | acepta   | válida                                           |
| `22001010021221` |    14    | acepta   | acepta   | válida                                           |
| λ                |    0     | rechaza  | rechaza  | inválida                                         |
| `1`              |    1     | rechaza  | rechaza  | inválida                                         |
| `010`            |    3     | rechaza  | rechaza  | inválida                                         |
| `20200`          |    5     | rechaza  | rechaza  | inválida                                         |
| `11210010`       |    8     | rechaza  | rechaza  | inválida                                         |
| `0210101`        |    7     | acepta   | acepta   | frontera: aceptada más corta                     |
| `111100`         |    6     | rechaza  | rechaza  | frontera: justo por debajo de la longitud mínima |

Cadenas de prueba.

## Lista 2 · Ejercicio 109

**Enunciado.** Las palabras de Σ2 que incluyen abbcb y cbaabb, que sí se pueden traslapar.

**Clase.** AFD: Cada par (estado, símbolo) tiene a lo sumo un destino y no hay transiciones λ. **Archivos.** `automatas/afd/lista2-109.jff` (y `.json`, `.xml`).

**Diseño.** Producto de los dos buscadores de patrones: como pueden traslaparse, cada patrón se busca de forma independiente.

| δ                  | 0               | 1               | a               | b               | c               | Qué recuerda del prefijo leído                    |
|--------------------|-----------------|-----------------|-----------------|-----------------|-----------------|---------------------------------------------------|
| → (λ, λ)           | (λ, λ)          | (λ, λ)          | (a, λ)          | (λ, λ)          | (λ, c)          | en el primer autómata λ, en el segundo λ          |
| (a, λ)             | (λ, λ)          | (λ, λ)          | (a, λ)          | (ab, λ)         | (λ, c)          | en el primer autómata a, en el segundo λ          |
| (λ, c)             | (λ, λ)          | (λ, λ)          | (a, λ)          | (λ, cb)         | (λ, c)          | en el primer autómata λ, en el segundo c          |
| (ab, λ)            | (λ, λ)          | (λ, λ)          | (a, λ)          | (abb, λ)        | (λ, c)          | en el primer autómata ab, en el segundo λ         |
| (λ, cb)            | (λ, λ)          | (λ, λ)          | (a, cba)        | (λ, λ)          | (λ, c)          | en el primer autómata λ, en el segundo cb         |
| (abb, λ)           | (λ, λ)          | (λ, λ)          | (a, λ)          | (λ, λ)          | (abbc, c)       | en el primer autómata abb, en el segundo λ        |
| (a, cba)           | (λ, λ)          | (λ, λ)          | (a, cbaa)       | (ab, λ)         | (λ, c)          | en el primer autómata a, en el segundo cba        |
| (abbc, c)          | (λ, λ)          | (λ, λ)          | (a, λ)          | (abbcb, cb)     | (λ, c)          | en el primer autómata abbc, en el segundo c       |
| (a, cbaa)          | (λ, λ)          | (λ, λ)          | (a, λ)          | (ab, cbaab)     | (λ, c)          | en el primer autómata a, en el segundo cbaa       |
| (abbcb, cb)        | (abbcb, λ)      | (abbcb, λ)      | (abbcb, cba)    | (abbcb, λ)      | (abbcb, c)      | en el primer autómata abbcb, en el segundo cb     |
| (ab, cbaab)        | (λ, λ)          | (λ, λ)          | (a, λ)          | (abb, cbaabb)   | (λ, c)          | en el primer autómata ab, en el segundo cbaab     |
| (abbcb, cba)       | (abbcb, λ)      | (abbcb, λ)      | (abbcb, cbaa)   | (abbcb, λ)      | (abbcb, c)      | en el primer autómata abbcb, en el segundo cba    |
| (abbcb, λ)         | (abbcb, λ)      | (abbcb, λ)      | (abbcb, λ)      | (abbcb, λ)      | (abbcb, c)      | en el primer autómata abbcb, en el segundo λ      |
| (abbcb, c)         | (abbcb, λ)      | (abbcb, λ)      | (abbcb, λ)      | (abbcb, cb)     | (abbcb, c)      | en el primer autómata abbcb, en el segundo c      |
| (abb, cbaabb)      | (λ, cbaabb)     | (λ, cbaabb)     | (a, cbaabb)     | (λ, cbaabb)     | (abbc, cbaabb)  | en el primer autómata abb, en el segundo cbaabb   |
| (abbcb, cbaa)      | (abbcb, λ)      | (abbcb, λ)      | (abbcb, λ)      | (abbcb, cbaab)  | (abbcb, c)      | en el primer autómata abbcb, en el segundo cbaa   |
| (a, cbaabb)        | (λ, cbaabb)     | (λ, cbaabb)     | (a, cbaabb)     | (ab, cbaabb)    | (λ, cbaabb)     | en el primer autómata a, en el segundo cbaabb     |
| (λ, cbaabb)        | (λ, cbaabb)     | (λ, cbaabb)     | (a, cbaabb)     | (λ, cbaabb)     | (λ, cbaabb)     | en el primer autómata λ, en el segundo cbaabb     |
| (abbc, cbaabb)     | (λ, cbaabb)     | (λ, cbaabb)     | (a, cbaabb)     | (abbcb, cbaabb) | (λ, cbaabb)     | en el primer autómata abbc, en el segundo cbaabb  |
| (abbcb, cbaab)     | (abbcb, λ)      | (abbcb, λ)      | (abbcb, λ)      | (abbcb, cbaabb) | (abbcb, c)      | en el primer autómata abbcb, en el segundo cbaab  |
| (ab, cbaabb)       | (λ, cbaabb)     | (λ, cbaabb)     | (a, cbaabb)     | (abb, cbaabb)   | (λ, cbaabb)     | en el primer autómata ab, en el segundo cbaabb    |
| \* (abbcb, cbaabb) | (abbcb, cbaabb) | (abbcb, cbaabb) | (abbcb, cbaabb) | (abbcb, cbaabb) | (abbcb, cbaabb) | en el primer autómata abbcb, en el segundo cbaabb |

Tabla de transiciones (→ inicial, \* aceptación, — sin transición).

| Cadena           | Longitud | Esperado | Obtenido | Tipo de caso                                     |
|------------------|:--------:|----------|----------|--------------------------------------------------|
| `cbaabbcb`       |    8     | acepta   | acepta   | válida                                           |
| `0cbaabbcb`      |    9     | acepta   | acepta   | válida                                           |
| `acacbaabbcb`    |    11    | acepta   | acepta   | válida                                           |
| `cbaabbcb10000`  |    13    | acepta   | acepta   | válida                                           |
| `0a111acbaabbcb` |    14    | acepta   | acepta   | válida                                           |
| λ                |    0     | rechaza  | rechaza  | inválida                                         |
| `1`              |    1     | rechaza  | rechaza  | inválida                                         |
| `b0c`            |    3     | rechaza  | rechaza  | inválida                                         |
| `1c1ab`          |    5     | rechaza  | rechaza  | inválida                                         |
| `1111cccb`       |    8     | rechaza  | rechaza  | inválida                                         |
| `cbbcccb`        |    7     | rechaza  | rechaza  | frontera: justo por debajo de la longitud mínima |

Cadenas de prueba.

## Lista 2 · Ejercicio 108

**Enunciado.** Las palabras de Σ2 que incluyen abbcb y cbaabb sin traslaparse (abbcbaabb no pertenece).

**Clase.** AFD: Cada par (estado, símbolo) tiene a lo sumo un destino y no hay transiciones λ. **Archivos.** `automatas/afd/lista2-108.jff` (y `.json`, `.xml`).

**Diseño.** Dos búsquedas secuenciales en paralelo: abbcb y, a partir de donde termina, cbaabb; y el orden inverso. Al terminar el primer patrón la búsqueda del segundo empieza de cero, lo que impide el traslape.

| δ                             | 0                        | 1                        | a                           | b                             | c                           | Qué recuerda del prefijo leído                                                    |
|-------------------------------|--------------------------|--------------------------|-----------------------------|-------------------------------|-----------------------------|-----------------------------------------------------------------------------------|
| → \[λ ; λ\]                   | \[λ ; λ\]                | \[λ ; λ\]                | \[a ; λ\]                   | \[λ ; λ\]                     | \[λ ; c\]                   | primera componente: búsqueda de abbcb y después cbaabb; segunda: el orden inverso |
| \[a ; λ\]                     | \[λ ; λ\]                | \[λ ; λ\]                | \[a ; λ\]                   | \[ab ; λ\]                    | \[λ ; c\]                   | primera componente: búsqueda de abbcb y después cbaabb; segunda: el orden inverso |
| \[λ ; c\]                     | \[λ ; λ\]                | \[λ ; λ\]                | \[a ; λ\]                   | \[λ ; cb\]                    | \[λ ; c\]                   | primera componente: búsqueda de abbcb y después cbaabb; segunda: el orden inverso |
| \[ab ; λ\]                    | \[λ ; λ\]                | \[λ ; λ\]                | \[a ; λ\]                   | \[abb ; λ\]                   | \[λ ; c\]                   | primera componente: búsqueda de abbcb y después cbaabb; segunda: el orden inverso |
| \[λ ; cb\]                    | \[λ ; λ\]                | \[λ ; λ\]                | \[a ; cba\]                 | \[λ ; λ\]                     | \[λ ; c\]                   | primera componente: búsqueda de abbcb y después cbaabb; segunda: el orden inverso |
| \[abb ; λ\]                   | \[λ ; λ\]                | \[λ ; λ\]                | \[a ; λ\]                   | \[λ ; λ\]                     | \[abbc ; c\]                | primera componente: búsqueda de abbcb y después cbaabb; segunda: el orden inverso |
| \[a ; cba\]                   | \[λ ; λ\]                | \[λ ; λ\]                | \[a ; cbaa\]                | \[ab ; λ\]                    | \[λ ; c\]                   | primera componente: búsqueda de abbcb y después cbaabb; segunda: el orden inverso |
| \[abbc ; c\]                  | \[λ ; λ\]                | \[λ ; λ\]                | \[a ; λ\]                   | \[abbcb\|λ ; cb\]             | \[λ ; c\]                   | primera componente: búsqueda de abbcb y después cbaabb; segunda: el orden inverso |
| \[a ; cbaa\]                  | \[λ ; λ\]                | \[λ ; λ\]                | \[a ; λ\]                   | \[ab ; cbaab\]                | \[λ ; c\]                   | primera componente: búsqueda de abbcb y después cbaabb; segunda: el orden inverso |
| \[abbcb\|λ ; cb\]             | \[abbcb\|λ ; λ\]         | \[abbcb\|λ ; λ\]         | \[abbcb\|λ ; cba\]          | \[abbcb\|λ ; λ\]              | \[abbcb\|c ; c\]            | primera componente: búsqueda de abbcb y después cbaabb; segunda: el orden inverso |
| \[ab ; cbaab\]                | \[λ ; λ\]                | \[λ ; λ\]                | \[a ; λ\]                   | \[abb ; cbaabb\|λ\]           | \[λ ; c\]                   | primera componente: búsqueda de abbcb y después cbaabb; segunda: el orden inverso |
| \[abbcb\|λ ; cba\]            | \[abbcb\|λ ; λ\]         | \[abbcb\|λ ; λ\]         | \[abbcb\|λ ; cbaa\]         | \[abbcb\|λ ; λ\]              | \[abbcb\|c ; c\]            | primera componente: búsqueda de abbcb y después cbaabb; segunda: el orden inverso |
| \[abbcb\|λ ; λ\]              | \[abbcb\|λ ; λ\]         | \[abbcb\|λ ; λ\]         | \[abbcb\|λ ; λ\]            | \[abbcb\|λ ; λ\]              | \[abbcb\|c ; c\]            | primera componente: búsqueda de abbcb y después cbaabb; segunda: el orden inverso |
| \[abbcb\|c ; c\]              | \[abbcb\|λ ; λ\]         | \[abbcb\|λ ; λ\]         | \[abbcb\|λ ; λ\]            | \[abbcb\|cb ; cb\]            | \[abbcb\|c ; c\]            | primera componente: búsqueda de abbcb y después cbaabb; segunda: el orden inverso |
| \[abb ; cbaabb\|λ\]           | \[λ ; cbaabb\|λ\]        | \[λ ; cbaabb\|λ\]        | \[a ; cbaabb\|a\]           | \[λ ; cbaabb\|λ\]             | \[abbc ; cbaabb\|λ\]        | primera componente: búsqueda de abbcb y después cbaabb; segunda: el orden inverso |
| \[abbcb\|λ ; cbaa\]           | \[abbcb\|λ ; λ\]         | \[abbcb\|λ ; λ\]         | \[abbcb\|λ ; λ\]            | \[abbcb\|λ ; cbaab\]          | \[abbcb\|c ; c\]            | primera componente: búsqueda de abbcb y después cbaabb; segunda: el orden inverso |
| \[abbcb\|cb ; cb\]            | \[abbcb\|λ ; λ\]         | \[abbcb\|λ ; λ\]         | \[abbcb\|cba ; cba\]        | \[abbcb\|λ ; λ\]              | \[abbcb\|c ; c\]            | primera componente: búsqueda de abbcb y después cbaabb; segunda: el orden inverso |
| \[a ; cbaabb\|a\]             | \[λ ; cbaabb\|λ\]        | \[λ ; cbaabb\|λ\]        | \[a ; cbaabb\|a\]           | \[ab ; cbaabb\|ab\]           | \[λ ; cbaabb\|λ\]           | primera componente: búsqueda de abbcb y después cbaabb; segunda: el orden inverso |
| \[λ ; cbaabb\|λ\]             | \[λ ; cbaabb\|λ\]        | \[λ ; cbaabb\|λ\]        | \[a ; cbaabb\|a\]           | \[λ ; cbaabb\|λ\]             | \[λ ; cbaabb\|λ\]           | primera componente: búsqueda de abbcb y después cbaabb; segunda: el orden inverso |
| \[abbc ; cbaabb\|λ\]          | \[λ ; cbaabb\|λ\]        | \[λ ; cbaabb\|λ\]        | \[a ; cbaabb\|a\]           | \[abbcb\|λ ; cbaabb\|λ\]      | \[λ ; cbaabb\|λ\]           | primera componente: búsqueda de abbcb y después cbaabb; segunda: el orden inverso |
| \[abbcb\|λ ; cbaab\]          | \[abbcb\|λ ; λ\]         | \[abbcb\|λ ; λ\]         | \[abbcb\|λ ; λ\]            | \[abbcb\|λ ; cbaabb\|λ\]      | \[abbcb\|c ; c\]            | primera componente: búsqueda de abbcb y después cbaabb; segunda: el orden inverso |
| \[abbcb\|cba ; cba\]          | \[abbcb\|λ ; λ\]         | \[abbcb\|λ ; λ\]         | \[abbcb\|cbaa ; cbaa\]      | \[abbcb\|λ ; λ\]              | \[abbcb\|c ; c\]            | primera componente: búsqueda de abbcb y después cbaabb; segunda: el orden inverso |
| \[ab ; cbaabb\|ab\]           | \[λ ; cbaabb\|λ\]        | \[λ ; cbaabb\|λ\]        | \[a ; cbaabb\|a\]           | \[abb ; cbaabb\|abb\]         | \[λ ; cbaabb\|λ\]           | primera componente: búsqueda de abbcb y después cbaabb; segunda: el orden inverso |
| \[abbcb\|λ ; cbaabb\|λ\]      | \[abbcb\|λ ; cbaabb\|λ\] | \[abbcb\|λ ; cbaabb\|λ\] | \[abbcb\|λ ; cbaabb\|a\]    | \[abbcb\|λ ; cbaabb\|λ\]      | \[abbcb\|c ; cbaabb\|λ\]    | primera componente: búsqueda de abbcb y después cbaabb; segunda: el orden inverso |
| \[abbcb\|cbaa ; cbaa\]        | \[abbcb\|λ ; λ\]         | \[abbcb\|λ ; λ\]         | \[abbcb\|λ ; λ\]            | \[abbcb\|cbaab ; cbaab\]      | \[abbcb\|c ; c\]            | primera componente: búsqueda de abbcb y después cbaabb; segunda: el orden inverso |
| \[abb ; cbaabb\|abb\]         | \[λ ; cbaabb\|λ\]        | \[λ ; cbaabb\|λ\]        | \[a ; cbaabb\|a\]           | \[λ ; cbaabb\|λ\]             | \[abbc ; cbaabb\|abbc\]     | primera componente: búsqueda de abbcb y después cbaabb; segunda: el orden inverso |
| \[abbcb\|λ ; cbaabb\|a\]      | \[abbcb\|λ ; cbaabb\|λ\] | \[abbcb\|λ ; cbaabb\|λ\] | \[abbcb\|λ ; cbaabb\|a\]    | \[abbcb\|λ ; cbaabb\|ab\]     | \[abbcb\|c ; cbaabb\|λ\]    | primera componente: búsqueda de abbcb y después cbaabb; segunda: el orden inverso |
| \[abbcb\|c ; cbaabb\|λ\]      | \[abbcb\|λ ; cbaabb\|λ\] | \[abbcb\|λ ; cbaabb\|λ\] | \[abbcb\|λ ; cbaabb\|a\]    | \[abbcb\|cb ; cbaabb\|λ\]     | \[abbcb\|c ; cbaabb\|λ\]    | primera componente: búsqueda de abbcb y después cbaabb; segunda: el orden inverso |
| \[abbcb\|cbaab ; cbaab\]      | \[abbcb\|λ ; λ\]         | \[abbcb\|λ ; λ\]         | \[abbcb\|λ ; λ\]            | \[✓ ; cbaabb\|λ\]             | \[abbcb\|c ; c\]            | primera componente: búsqueda de abbcb y después cbaabb; segunda: el orden inverso |
| \[abbc ; cbaabb\|abbc\]       | \[λ ; cbaabb\|λ\]        | \[λ ; cbaabb\|λ\]        | \[a ; cbaabb\|a\]           | \[abbcb\|λ ; ✓\]              | \[λ ; cbaabb\|λ\]           | primera componente: búsqueda de abbcb y después cbaabb; segunda: el orden inverso |
| \[abbcb\|λ ; cbaabb\|ab\]     | \[abbcb\|λ ; cbaabb\|λ\] | \[abbcb\|λ ; cbaabb\|λ\] | \[abbcb\|λ ; cbaabb\|a\]    | \[abbcb\|λ ; cbaabb\|abb\]    | \[abbcb\|c ; cbaabb\|λ\]    | primera componente: búsqueda de abbcb y después cbaabb; segunda: el orden inverso |
| \[abbcb\|cb ; cbaabb\|λ\]     | \[abbcb\|λ ; cbaabb\|λ\] | \[abbcb\|λ ; cbaabb\|λ\] | \[abbcb\|cba ; cbaabb\|a\]  | \[abbcb\|λ ; cbaabb\|λ\]      | \[abbcb\|c ; cbaabb\|λ\]    | primera componente: búsqueda de abbcb y después cbaabb; segunda: el orden inverso |
| \* \[✓ ; cbaabb\|λ\]          | \[✓ ; cbaabb\|λ\]        | \[✓ ; cbaabb\|λ\]        | \[✓ ; cbaabb\|a\]           | \[✓ ; cbaabb\|λ\]             | \[✓ ; cbaabb\|λ\]           | primera componente: búsqueda de abbcb y después cbaabb; segunda: el orden inverso |
| \* \[abbcb\|λ ; ✓\]           | \[abbcb\|λ ; ✓\]         | \[abbcb\|λ ; ✓\]         | \[abbcb\|λ ; ✓\]            | \[abbcb\|λ ; ✓\]              | \[abbcb\|c ; ✓\]            | primera componente: búsqueda de abbcb y después cbaabb; segunda: el orden inverso |
| \[abbcb\|λ ; cbaabb\|abb\]    | \[abbcb\|λ ; cbaabb\|λ\] | \[abbcb\|λ ; cbaabb\|λ\] | \[abbcb\|λ ; cbaabb\|a\]    | \[abbcb\|λ ; cbaabb\|λ\]      | \[abbcb\|c ; cbaabb\|abbc\] | primera componente: búsqueda de abbcb y después cbaabb; segunda: el orden inverso |
| \[abbcb\|cba ; cbaabb\|a\]    | \[abbcb\|λ ; cbaabb\|λ\] | \[abbcb\|λ ; cbaabb\|λ\] | \[abbcb\|cbaa ; cbaabb\|a\] | \[abbcb\|λ ; cbaabb\|ab\]     | \[abbcb\|c ; cbaabb\|λ\]    | primera componente: búsqueda de abbcb y después cbaabb; segunda: el orden inverso |
| \* \[✓ ; cbaabb\|a\]          | \[✓ ; cbaabb\|λ\]        | \[✓ ; cbaabb\|λ\]        | \[✓ ; cbaabb\|a\]           | \[✓ ; cbaabb\|ab\]            | \[✓ ; cbaabb\|λ\]           | primera componente: búsqueda de abbcb y después cbaabb; segunda: el orden inverso |
| \* \[abbcb\|c ; ✓\]           | \[abbcb\|λ ; ✓\]         | \[abbcb\|λ ; ✓\]         | \[abbcb\|λ ; ✓\]            | \[abbcb\|cb ; ✓\]             | \[abbcb\|c ; ✓\]            | primera componente: búsqueda de abbcb y después cbaabb; segunda: el orden inverso |
| \[abbcb\|c ; cbaabb\|abbc\]   | \[abbcb\|λ ; cbaabb\|λ\] | \[abbcb\|λ ; cbaabb\|λ\] | \[abbcb\|λ ; cbaabb\|a\]    | \[abbcb\|cb ; ✓\]             | \[abbcb\|c ; cbaabb\|λ\]    | primera componente: búsqueda de abbcb y después cbaabb; segunda: el orden inverso |
| \[abbcb\|cbaa ; cbaabb\|a\]   | \[abbcb\|λ ; cbaabb\|λ\] | \[abbcb\|λ ; cbaabb\|λ\] | \[abbcb\|λ ; cbaabb\|a\]    | \[abbcb\|cbaab ; cbaabb\|ab\] | \[abbcb\|c ; cbaabb\|λ\]    | primera componente: búsqueda de abbcb y después cbaabb; segunda: el orden inverso |
| \* \[✓ ; cbaabb\|ab\]         | \[✓ ; cbaabb\|λ\]        | \[✓ ; cbaabb\|λ\]        | \[✓ ; cbaabb\|a\]           | \[✓ ; cbaabb\|abb\]           | \[✓ ; cbaabb\|λ\]           | primera componente: búsqueda de abbcb y después cbaabb; segunda: el orden inverso |
| \* \[abbcb\|cb ; ✓\]          | \[abbcb\|λ ; ✓\]         | \[abbcb\|λ ; ✓\]         | \[abbcb\|cba ; ✓\]          | \[abbcb\|λ ; ✓\]              | \[abbcb\|c ; ✓\]            | primera componente: búsqueda de abbcb y después cbaabb; segunda: el orden inverso |
| \[abbcb\|cbaab ; cbaabb\|ab\] | \[abbcb\|λ ; cbaabb\|λ\] | \[abbcb\|λ ; cbaabb\|λ\] | \[abbcb\|λ ; cbaabb\|a\]    | \[✓ ; cbaabb\|abb\]           | \[abbcb\|c ; cbaabb\|λ\]    | primera componente: búsqueda de abbcb y después cbaabb; segunda: el orden inverso |
| \* \[✓ ; cbaabb\|abb\]        | \[✓ ; cbaabb\|λ\]        | \[✓ ; cbaabb\|λ\]        | \[✓ ; cbaabb\|a\]           | \[✓ ; cbaabb\|λ\]             | \[✓ ; cbaabb\|abbc\]        | primera componente: búsqueda de abbcb y después cbaabb; segunda: el orden inverso |
| \* \[abbcb\|cba ; ✓\]         | \[abbcb\|λ ; ✓\]         | \[abbcb\|λ ; ✓\]         | \[abbcb\|cbaa ; ✓\]         | \[abbcb\|λ ; ✓\]              | \[abbcb\|c ; ✓\]            | primera componente: búsqueda de abbcb y después cbaabb; segunda: el orden inverso |
| \* \[✓ ; cbaabb\|abbc\]       | \[✓ ; cbaabb\|λ\]        | \[✓ ; cbaabb\|λ\]        | \[✓ ; cbaabb\|a\]           | \[✓ ; ✓\]                     | \[✓ ; cbaabb\|λ\]           | primera componente: búsqueda de abbcb y después cbaabb; segunda: el orden inverso |
| \* \[abbcb\|cbaa ; ✓\]        | \[abbcb\|λ ; ✓\]         | \[abbcb\|λ ; ✓\]         | \[abbcb\|λ ; ✓\]            | \[abbcb\|cbaab ; ✓\]          | \[abbcb\|c ; ✓\]            | primera componente: búsqueda de abbcb y después cbaabb; segunda: el orden inverso |
| \* \[✓ ; ✓\]                  | \[✓ ; ✓\]                | \[✓ ; ✓\]                | \[✓ ; ✓\]                   | \[✓ ; ✓\]                     | \[✓ ; ✓\]                   | primera componente: búsqueda de abbcb y después cbaabb; segunda: el orden inverso |
| \* \[abbcb\|cbaab ; ✓\]       | \[abbcb\|λ ; ✓\]         | \[abbcb\|λ ; ✓\]         | \[abbcb\|λ ; ✓\]            | \[✓ ; ✓\]                     | \[abbcb\|c ; ✓\]            | primera componente: búsqueda de abbcb y después cbaabb; segunda: el orden inverso |

Tabla de transiciones (→ inicial, \* aceptación, — sin transición).

| Cadena              | Longitud | Esperado | Obtenido | Tipo de caso                                     |
|---------------------|:--------:|----------|----------|--------------------------------------------------|
| `cbaabbabbcb`       |    11    | acepta   | acepta   | válida                                           |
| `0cbaabbabbcb`      |    12    | acepta   | acepta   | válida                                           |
| `0cbaabba0abbcb`    |    14    | acepta   | acepta   | válida                                           |
| `0bacbaabbcabbcb1`  |    16    | acepta   | acepta   | válida                                           |
| `c1cbaabbabbcbca11` |    17    | acepta   | acepta   | válida                                           |
| λ                   |    0     | rechaza  | rechaza  | inválida                                         |
| `b`                 |    1     | rechaza  | rechaza  | inválida                                         |
| `acb`               |    3     | rechaza  | rechaza  | inválida                                         |
| `ababc`             |    5     | rechaza  | rechaza  | inválida                                         |
| `0bc11caa`          |    8     | rechaza  | rechaza  | inválida                                         |
| `bab1a0100b`        |    10    | rechaza  | rechaza  | frontera: justo por debajo de la longitud mínima |

Cadenas de prueba.

## Lista 2 · Ejercicio 110

**Enunciado.** Las palabras de Σ1 que contienen exactamente tres veces la subcadena 01.

**Clase.** AFD: Cada par (estado, símbolo) tiene a lo sumo un destino y no hay transiciones λ. **Archivos.** `automatas/afd/lista2-110.jff` (y `.json`, `.xml`).

**Diseño.** Cada estado combina el número de apariciones de 01 (0 a 3, y muerto si pasa de 3) con el avance en el patrón; 01 no puede traslaparse consigo mismo.

| δ      | 0      | 1      | 2      | Qué recuerda del prefijo leído               |
|--------|--------|--------|--------|----------------------------------------------|
| → 0·λ  | 0·0    | 0·λ    | 0·λ    | van 0 apariciones; el sufijo útil leído es λ |
| 0·0    | 0·0    | 1·λ    | 0·λ    | van 0 apariciones; el sufijo útil leído es 0 |
| 1·λ    | 1·0    | 1·λ    | 1·λ    | van 1 apariciones; el sufijo útil leído es λ |
| 1·0    | 1·0    | 2·λ    | 1·λ    | van 1 apariciones; el sufijo útil leído es 0 |
| 2·λ    | 2·0    | 2·λ    | 2·λ    | van 2 apariciones; el sufijo útil leído es λ |
| 2·0    | 2·0    | 3·λ    | 2·λ    | van 2 apariciones; el sufijo útil leído es 0 |
| \* 3·λ | 3·0    | 3·λ    | 3·λ    | van 3 apariciones; el sufijo útil leído es λ |
| \* 3·0 | 3·0    | muerto | 3·λ    | van 3 apariciones; el sufijo útil leído es 0 |
| muerto | muerto | muerto | muerto | ya hay más de 3 apariciones de 01            |

Tabla de transiciones (→ inicial, \* aceptación, — sin transición).

| Cadena           | Longitud | Esperado | Obtenido | Tipo de caso                                     |
|------------------|:--------:|----------|----------|--------------------------------------------------|
| `010101`         |    6     | acepta   | acepta   | válida                                           |
| `0101201`        |    7     | acepta   | acepta   | válida                                           |
| `001201012`      |    9     | acepta   | acepta   | válida                                           |
| `20011101010`    |    11    | acepta   | acepta   | válida                                           |
| `10112010000112` |    14    | acepta   | acepta   | válida                                           |
| λ                |    0     | rechaza  | rechaza  | inválida                                         |
| `1`              |    1     | rechaza  | rechaza  | inválida                                         |
| `022`            |    3     | rechaza  | rechaza  | inválida                                         |
| `10210`          |    5     | rechaza  | rechaza  | inválida                                         |
| `12110121`       |    8     | rechaza  | rechaza  | inválida                                         |
| `02210`          |    5     | rechaza  | rechaza  | frontera: justo por debajo de la longitud mínima |

Cadenas de prueba.

## Lista 2 · Ejercicio 111

**Enunciado.** Las palabras de Σ1 que contienen exactamente tres veces la subcadena 01002.

**Clase.** AFD: Cada par (estado, símbolo) tiene a lo sumo un destino y no hay transiciones λ. **Archivos.** `automatas/afd/lista2-111.jff` (y `.json`, `.xml`).

**Diseño.** Cada estado combina el número de apariciones de 01002 (0 a 3, y muerto si pasa de 3) con el avance en el patrón; 01002 no puede traslaparse consigo mismo.

| δ         | 0      | 1      | 2      | Qué recuerda del prefijo leído                  |
|-----------|--------|--------|--------|-------------------------------------------------|
| → 0·λ     | 0·0    | 0·λ    | 0·λ    | van 0 apariciones; el sufijo útil leído es λ    |
| 0·0       | 0·0    | 0·01   | 0·λ    | van 0 apariciones; el sufijo útil leído es 0    |
| 0·01      | 0·010  | 0·λ    | 0·λ    | van 0 apariciones; el sufijo útil leído es 01   |
| 0·010     | 0·0100 | 0·01   | 0·λ    | van 0 apariciones; el sufijo útil leído es 010  |
| 0·0100    | 0·0    | 0·01   | 1·λ    | van 0 apariciones; el sufijo útil leído es 0100 |
| 1·λ       | 1·0    | 1·λ    | 1·λ    | van 1 apariciones; el sufijo útil leído es λ    |
| 1·0       | 1·0    | 1·01   | 1·λ    | van 1 apariciones; el sufijo útil leído es 0    |
| 1·01      | 1·010  | 1·λ    | 1·λ    | van 1 apariciones; el sufijo útil leído es 01   |
| 1·010     | 1·0100 | 1·01   | 1·λ    | van 1 apariciones; el sufijo útil leído es 010  |
| 1·0100    | 1·0    | 1·01   | 2·λ    | van 1 apariciones; el sufijo útil leído es 0100 |
| 2·λ       | 2·0    | 2·λ    | 2·λ    | van 2 apariciones; el sufijo útil leído es λ    |
| 2·0       | 2·0    | 2·01   | 2·λ    | van 2 apariciones; el sufijo útil leído es 0    |
| 2·01      | 2·010  | 2·λ    | 2·λ    | van 2 apariciones; el sufijo útil leído es 01   |
| 2·010     | 2·0100 | 2·01   | 2·λ    | van 2 apariciones; el sufijo útil leído es 010  |
| 2·0100    | 2·0    | 2·01   | 3·λ    | van 2 apariciones; el sufijo útil leído es 0100 |
| \* 3·λ    | 3·0    | 3·λ    | 3·λ    | van 3 apariciones; el sufijo útil leído es λ    |
| \* 3·0    | 3·0    | 3·01   | 3·λ    | van 3 apariciones; el sufijo útil leído es 0    |
| \* 3·01   | 3·010  | 3·λ    | 3·λ    | van 3 apariciones; el sufijo útil leído es 01   |
| \* 3·010  | 3·0100 | 3·01   | 3·λ    | van 3 apariciones; el sufijo útil leído es 010  |
| \* 3·0100 | 3·0    | 3·01   | muerto | van 3 apariciones; el sufijo útil leído es 0100 |
| muerto    | muerto | muerto | muerto | ya hay más de 3 apariciones de 01002            |

Tabla de transiciones (→ inicial, \* aceptación, — sin transición).

| Cadena                  | Longitud | Esperado | Obtenido | Tipo de caso                                     |
|-------------------------|:--------:|----------|----------|--------------------------------------------------|
| `010020100201002`       |    15    | acepta   | acepta   | válida                                           |
| `0100201002001002`      |    16    | acepta   | acepta   | válida                                           |
| `010020010020101002`    |    18    | acepta   | acepta   | válida                                           |
| `10100210100201002110`  |    20    | acepta   | acepta   | válida                                           |
| `211010020100201002001` |    21    | acepta   | acepta   | válida                                           |
| λ                       |    0     | rechaza  | rechaza  | inválida                                         |
| `0`                     |    1     | rechaza  | rechaza  | inválida                                         |
| `111`                   |    3     | rechaza  | rechaza  | inválida                                         |
| `20011`                 |    5     | rechaza  | rechaza  | inválida                                         |
| `12220221`              |    8     | rechaza  | rechaza  | inválida                                         |
| `01122210022010`        |    14    | rechaza  | rechaza  | frontera: justo por debajo de la longitud mínima |

Cadenas de prueba.

## Lista 2 · Ejercicio 112

**Enunciado.** Las palabras de Σ1 que contienen dos veces 010 sin traslaparse (01010 no pertenece, 010010 sí).

**Clase.** AFD: Cada par (estado, símbolo) tiene a lo sumo un destino y no hay transiciones λ. **Archivos.** `automatas/afd/lista2-112.jff` (y `.json`, `.xml`).

**Diseño.** Se interpreta «al menos dos apariciones disjuntas». Tras completar 010 la búsqueda reinicia desde λ, de modo que la siguiente aparición no reutiliza el último 0.

| δ     | 0   | 1    | 2   | Qué recuerda del prefijo leído                |
|-------|-----|------|-----|-----------------------------------------------|
| → 0·λ | 0·0 | 0·λ  | 0·λ | van 0 apariciones; el sufijo útil leído es λ  |
| 0·0   | 0·0 | 0·01 | 0·λ | van 0 apariciones; el sufijo útil leído es 0  |
| 0·01  | 1·λ | 0·λ  | 0·λ | van 0 apariciones; el sufijo útil leído es 01 |
| 1·λ   | 1·0 | 1·λ  | 1·λ | van 1 apariciones; el sufijo útil leído es λ  |
| 1·0   | 1·0 | 1·01 | 1·λ | van 1 apariciones; el sufijo útil leído es 0  |
| 1·01  | 2+  | 1·λ  | 1·λ | van 1 apariciones; el sufijo útil leído es 01 |
| \* 2+ | 2+  | 2+   | 2+  | ya hay 2 apariciones de 010                   |

Tabla de transiciones (→ inicial, \* aceptación, — sin transición).

| Cadena           | Longitud | Esperado | Obtenido | Tipo de caso                                     |
|------------------|:--------:|----------|----------|--------------------------------------------------|
| `010010`         |    6     | acepta   | acepta   | válida                                           |
| `0100010`        |    7     | acepta   | acepta   | válida                                           |
| `001001012`      |    9     | acepta   | acepta   | válida                                           |
| `22010010022`    |    11    | acepta   | acepta   | válida                                           |
| `00101111201000` |    14    | acepta   | acepta   | válida                                           |
| λ                |    0     | rechaza  | rechaza  | inválida                                         |
| `2`              |    1     | rechaza  | rechaza  | inválida                                         |
| `122`            |    3     | rechaza  | rechaza  | inválida                                         |
| `10021`          |    5     | rechaza  | rechaza  | inválida                                         |
| `12120021`       |    8     | rechaza  | rechaza  | inválida                                         |
| `20101`          |    5     | rechaza  | rechaza  | frontera: justo por debajo de la longitud mínima |

Cadenas de prueba.

## Lista 2 · Ejercicio 113

**Enunciado.** Las palabras de Σ1 que contienen dos veces 010, que sí se pueden traslapar.

**Clase.** AFD: Cada par (estado, símbolo) tiene a lo sumo un destino y no hay transiciones λ. **Archivos.** `automatas/afd/lista2-113.jff` (y `.json`, `.xml`).

**Diseño.** Igual que 112, pero tras completar 010 el autómata conserva el borde 0, que puede iniciar la siguiente aparición (01010).

| δ     | 0   | 1    | 2   | Qué recuerda del prefijo leído                |
|-------|-----|------|-----|-----------------------------------------------|
| → 0·λ | 0·0 | 0·λ  | 0·λ | van 0 apariciones; el sufijo útil leído es λ  |
| 0·0   | 0·0 | 0·01 | 0·λ | van 0 apariciones; el sufijo útil leído es 0  |
| 0·01  | 1·0 | 0·λ  | 0·λ | van 0 apariciones; el sufijo útil leído es 01 |
| 1·0   | 1·0 | 1·01 | 1·λ | van 1 apariciones; el sufijo útil leído es 0  |
| 1·01  | 2+  | 1·λ  | 1·λ | van 1 apariciones; el sufijo útil leído es 01 |
| 1·λ   | 1·0 | 1·λ  | 1·λ | van 1 apariciones; el sufijo útil leído es λ  |
| \* 2+ | 2+  | 2+   | 2+  | ya hay 2 apariciones de 010                   |

Tabla de transiciones (→ inicial, \* aceptación, — sin transición).

| Cadena          | Longitud | Esperado | Obtenido | Tipo de caso                                     |
|-----------------|:--------:|----------|----------|--------------------------------------------------|
| `01010`         |    5     | acepta   | acepta   | válida                                           |
| `010010`        |    6     | acepta   | acepta   | válida                                           |
| `01010101`      |    8     | acepta   | acepta   | válida                                           |
| `0101000102`    |    10    | acepta   | acepta   | válida                                           |
| `0102001001111` |    13    | acepta   | acepta   | válida                                           |
| λ               |    0     | rechaza  | rechaza  | inválida                                         |
| `1`             |    1     | rechaza  | rechaza  | inválida                                         |
| `012`           |    3     | rechaza  | rechaza  | inválida                                         |
| `12200`         |    5     | rechaza  | rechaza  | inválida                                         |
| `22111210`      |    8     | rechaza  | rechaza  | inválida                                         |
| `0100`          |    4     | rechaza  | rechaza  | frontera: justo por debajo de la longitud mínima |

Cadenas de prueba.

## Lista 2 · Ejercicio 114

**Enunciado.** L = {w ∈ Σ3\* : w = aⁿbᵐ, m, n ∈ N}.

**Clase.** AFD: Cada par (estado, símbolo) tiene a lo sumo un destino y no hay transiciones λ. **Archivos.** `automatas/afd/lista2-114.jff` (y `.json`, `.xml`).

**Diseño.** Dos fases: aes y después bes.

| δ        | a      | b      | Qué recuerda del prefijo leído  |
|----------|--------|--------|---------------------------------|
| →\* a\*  | a\*    | a\*b+  | sólo se han leído aes           |
| \* a\*b+ | muerto | a\*b+  | ya empezaron las bes            |
| muerto   | muerto | muerto | apareció una a después de una b |

Tabla de transiciones (→ inicial, \* aceptación, — sin transición).

| Cadena       | Longitud | Esperado | Obtenido | Tipo de caso |
|--------------|:--------:|----------|----------|--------------|
| λ            |    0     | acepta   | acepta   | válida       |
| `a`          |    1     | acepta   | acepta   | válida       |
| `aaa`        |    3     | acepta   | acepta   | válida       |
| `abbbb`      |    5     | acepta   | acepta   | válida       |
| `aabbbbbb`   |    8     | acepta   | acepta   | válida       |
| `ba`         |    2     | rechaza  | rechaza  | inválida     |
| `baa`        |    3     | rechaza  | rechaza  | inválida     |
| `baaab`      |    5     | rechaza  | rechaza  | inválida     |
| `bbaabbb`    |    7     | rechaza  | rechaza  | inválida     |
| `aaaababbab` |    10    | rechaza  | rechaza  | inválida     |

Cadenas de prueba.

## Lista 2 · Ejercicio 115

**Enunciado.** L = {w ∈ Σ2\* : w = (abc)ⁿ, n ∈ N}.

**Clase.** AFD: Cada par (estado, símbolo) tiene a lo sumo un destino y no hay transiciones λ. **Archivos.** `automatas/afd/lista2-115.jff` (y `.json`, `.xml`).

**Diseño.** Ciclo de tres estados que sigue el bloque abc.

| δ           | 0      | 1      | a      | b      | c       | Qué recuerda del prefijo leído     |
|-------------|--------|--------|--------|--------|---------|------------------------------------|
| →\* (abc)\* | muerto | muerto | …a     | muerto | muerto  | se han leído bloques abc completos |
| …a          | muerto | muerto | muerto | …ab    | muerto  | falta bc                           |
| muerto      | muerto | muerto | muerto | muerto | muerto  | se rompió el patrón                |
| …ab         | muerto | muerto | muerto | muerto | (abc)\* | falta c                            |

Tabla de transiciones (→ inicial, \* aceptación, — sin transición).

| Cadena         | Longitud | Esperado | Obtenido | Tipo de caso |
|----------------|:--------:|----------|----------|--------------|
| λ              |    0     | acepta   | acepta   | válida       |
| `abc`          |    3     | acepta   | acepta   | válida       |
| `abcabc`       |    6     | acepta   | acepta   | válida       |
| `abcabcabc`    |    9     | acepta   | acepta   | válida       |
| `abcabcabcabc` |    12    | acepta   | acepta   | válida       |
| `1`            |    1     | rechaza  | rechaza  | inválida     |
| `ba`           |    2     | rechaza  | rechaza  | inválida     |
| `cbaa`         |    4     | rechaza  | rechaza  | inválida     |
| `ca1bba`       |    6     | rechaza  | rechaza  | inválida     |
| `ba1bc11cb`    |    9     | rechaza  | rechaza  | inválida     |

Cadenas de prueba.

## Lista 2 · Ejercicio 117

**Enunciado.** L = {w ∈ Σ3\* : w = aⁿbᵐaᵖb^q, m, n, p, q ∈ N}.

**Clase.** AFD: Cada par (estado, símbolo) tiene a lo sumo un destino y no hay transiciones λ. **Archivos.** `automatas/afd/lista2-117.jff` (y `.json`, `.xml`).

**Diseño.** Cuatro fases; cada cambio de letra avanza una fase.

| δ          | a      | b      | Qué recuerda del prefijo leído           |
|------------|--------|--------|------------------------------------------|
| →\* f1:a\* | f1:a\* | f2:b\* | se está en el bloque 1 de a*b*a*b*       |
| \* f2:b\*  | f3:a\* | f2:b\* | se está en el bloque 2 de a*b*a*b*       |
| \* f3:a\*  | f3:a\* | f4:b\* | se está en el bloque 3 de a*b*a*b*       |
| \* f4:b\*  | muerto | f4:b\* | se está en el bloque 4 de a*b*a*b*       |
| muerto     | muerto | muerto | la cadena ya tiene más de cuatro bloques |

Tabla de transiciones (→ inicial, \* aceptación, — sin transición).

| Cadena         | Longitud | Esperado | Obtenido | Tipo de caso |
|----------------|:--------:|----------|----------|--------------|
| λ              |    0     | acepta   | acepta   | válida       |
| `a`            |    1     | acepta   | acepta   | válida       |
| `baa`          |    3     | acepta   | acepta   | válida       |
| `bbaaa`        |    5     | acepta   | acepta   | válida       |
| `aaaaaaab`     |    8     | acepta   | acepta   | válida       |
| `baba`         |    4     | rechaza  | rechaza  | inválida     |
| `babab`        |    5     | rechaza  | rechaza  | inválida     |
| `abbbaba`      |    7     | rechaza  | rechaza  | inválida     |
| `bbabababa`    |    9     | rechaza  | rechaza  | inválida     |
| `baabaaaaaaab` |    12    | rechaza  | rechaza  | inválida     |

Cadenas de prueba.

## Lista 2 · Ejercicio 118

**Enunciado.** L = {w ∈ Σ3\* : w = axabya, x, y ∈ Σ3\*}.

**Clase.** AFD: Cada par (estado, símbolo) tiene a lo sumo un destino y no hay transiciones λ. **Archivos.** `automatas/afd/lista2-118.jff` (y `.json`, `.xml`).

**Diseño.** La primera a no puede ser la del ab interior (debe haber una a inicial propia), y la a final debe ir después de la b.

| δ       | a      | b      | Qué recuerda del prefijo leído                                 |
|---------|--------|--------|----------------------------------------------------------------|
| → ini   | a      | muerto | no se ha leído nada                                            |
| a       | a·a    | a      | empieza con a; aún no hay una a utilizable para el ab interior |
| muerto  | muerto | muerto | la cadena no empieza con a                                     |
| a·a     | a·a    | ab     | el último símbolo es una a que puede iniciar el ab interior    |
| ab      | ab·a   | ab     | ya apareció el ab interior; el último símbolo no es a          |
| \* ab·a | ab·a   | ab     | ya apareció el ab interior y el último símbolo es a            |

Tabla de transiciones (→ inicial, \* aceptación, — sin transición).

| Cadena         | Longitud | Esperado | Obtenido | Tipo de caso                                     |
|----------------|:--------:|----------|----------|--------------------------------------------------|
| `aaba`         |    4     | acepta   | acepta   | válida                                           |
| `aabba`        |    5     | acepta   | acepta   | válida                                           |
| `aabbaaa`      |    7     | acepta   | acepta   | válida                                           |
| `abbbaabba`    |    9     | acepta   | acepta   | válida                                           |
| `aabbbaabaaaa` |    12    | acepta   | acepta   | válida                                           |
| λ              |    0     | rechaza  | rechaza  | inválida                                         |
| `a`            |    1     | rechaza  | rechaza  | inválida                                         |
| `bbb`          |    3     | rechaza  | rechaza  | inválida                                         |
| `babbb`        |    5     | rechaza  | rechaza  | inválida                                         |
| `babaaabb`     |    8     | rechaza  | rechaza  | inválida                                         |
| `bab`          |    3     | rechaza  | rechaza  | frontera: justo por debajo de la longitud mínima |

Cadenas de prueba.

## Lista 2 · Ejercicio 119

**Enunciado.** Las palabras de Σ3 tales que después de cada subcadena aa aparece una b.

**Clase.** AFD: Cada par (estado, símbolo) tiene a lo sumo un destino y no hay transiciones λ. **Archivos.** `automatas/afd/lista2-119.jff` (y `.json`, `.xml`).

**Diseño.** Cada aa debe ir seguida inmediatamente de b: se prohíbe aaa y terminar en aa. Basta contar las aes finales.

| δ         | a      | b      | Qué recuerda del prefijo leído           |
|-----------|--------|--------|------------------------------------------|
| →\* sin a | a      | sin a  | la cadena termina con 0 aes consecutivas |
| \* a      | aa     | sin a  | la cadena termina con 1 aes consecutivas |
| aa        | muerto | sin a  | la cadena termina con 2 aes consecutivas |
| muerto    | muerto | muerto | apareció aaa                             |

Tabla de transiciones (→ inicial, \* aceptación, — sin transición).

| Cadena       | Longitud | Esperado | Obtenido | Tipo de caso |
|--------------|:--------:|----------|----------|--------------|
| λ            |    0     | acepta   | acepta   | válida       |
| `a`          |    1     | acepta   | acepta   | válida       |
| `bbb`        |    3     | acepta   | acepta   | válida       |
| `ababa`      |    5     | acepta   | acepta   | válida       |
| `abababba`   |    8     | acepta   | acepta   | válida       |
| `aa`         |    2     | rechaza  | rechaza  | inválida     |
| `aaa`        |    3     | rechaza  | rechaza  | inválida     |
| `abbaa`      |    5     | rechaza  | rechaza  | inválida     |
| `aabaaab`    |    7     | rechaza  | rechaza  | inválida     |
| `aabababbaa` |    10    | rechaza  | rechaza  | inválida     |

Cadenas de prueba.

## Lista 2 · Ejercicio 120

**Enunciado.** Las palabras de Σ1 tales que el primer carácter y el último son distintos.

**Clase.** AFD: Cada par (estado, símbolo) tiene a lo sumo un destino y no hay transiciones λ. **Archivos.** `automatas/afd/lista2-120.jff` (y `.json`, `.xml`).

**Diseño.** Se recuerda el primer símbolo y si el último coincide con él.

| δ      | 0   | 1   | 2   | Qué recuerda del prefijo leído                |
|--------|-----|-----|-----|-----------------------------------------------|
| → ini  | 0…= | 1…= | 2…= | no se ha leído nada                           |
| 0…=    | 0…= | 0…≠ | 0…≠ | empieza con 0 y el último símbolo es igual    |
| 1…=    | 1…≠ | 1…= | 1…≠ | empieza con 1 y el último símbolo es igual    |
| 2…=    | 2…≠ | 2…≠ | 2…= | empieza con 2 y el último símbolo es igual    |
| \* 0…≠ | 0…= | 0…≠ | 0…≠ | empieza con 0 y el último símbolo es distinto |
| \* 1…≠ | 1…≠ | 1…= | 1…≠ | empieza con 1 y el último símbolo es distinto |
| \* 2…≠ | 2…≠ | 2…≠ | 2…= | empieza con 2 y el último símbolo es distinto |

Tabla de transiciones (→ inicial, \* aceptación, — sin transición).

| Cadena       | Longitud | Esperado | Obtenido | Tipo de caso                                     |
|--------------|:--------:|----------|----------|--------------------------------------------------|
| `21`         |    2     | acepta   | acepta   | válida                                           |
| `012`        |    3     | acepta   | acepta   | válida                                           |
| `20001`      |    5     | acepta   | acepta   | válida                                           |
| `0222011`    |    7     | acepta   | acepta   | válida                                           |
| `2022102021` |    10    | acepta   | acepta   | válida                                           |
| λ            |    0     | rechaza  | rechaza  | inválida                                         |
| `0`          |    1     | rechaza  | rechaza  | inválida                                         |
| `222`        |    3     | rechaza  | rechaza  | inválida                                         |
| `10011`      |    5     | rechaza  | rechaza  | inválida                                         |
| `10102211`   |    8     | rechaza  | rechaza  | inválida                                         |
| `01`         |    2     | acepta   | acepta   | frontera: aceptada más corta                     |
| `1`          |    1     | rechaza  | rechaza  | frontera: justo por debajo de la longitud mínima |

Cadenas de prueba.

## Lista 2 · Ejercicio 121

**Enunciado.** Las palabras de Σ1 de longitud 3n tales que cada bloque de longitud 3 tiene al menos un 0.

**Clase.** AFD: Cada par (estado, símbolo) tiene a lo sumo un destino y no hay transiciones λ. **Archivos.** `automatas/afd/lista2-121.jff` (y `.json`, `.xml`).

**Diseño.** Se lleva la posición dentro del bloque y si el bloque ya contiene un 0. λ (n = 0) se acepta.

| δ      | 0      | 1      | 2      | Qué recuerda del prefijo leído                             |
|--------|--------|--------|--------|------------------------------------------------------------|
| →\* b0 | b1+0   | b1     | b1     | posición 0 dentro del bloque; aún no hay un 0 en el bloque |
| b1+0   | b2+0   | b2+0   | b2+0   | posición 1 dentro del bloque; ya hay un 0 en el bloque     |
| b1     | b2+0   | b2     | b2     | posición 1 dentro del bloque; aún no hay un 0 en el bloque |
| b2+0   | b0     | b0     | b0     | posición 2 dentro del bloque; ya hay un 0 en el bloque     |
| b2     | b0     | muerto | muerto | posición 2 dentro del bloque; aún no hay un 0 en el bloque |
| muerto | muerto | muerto | muerto | un bloque terminó sin 0                                    |

Tabla de transiciones (→ inicial, \* aceptación, — sin transición).

| Cadena      | Longitud | Esperado | Obtenido | Tipo de caso |
|-------------|:--------:|----------|----------|--------------|
| λ           |    0     | acepta   | acepta   | válida       |
| `011`       |    3     | acepta   | acepta   | válida       |
| `012220`    |    6     | acepta   | acepta   | válida       |
| `012020210` |    9     | acepta   | acepta   | válida       |
| `100100102` |    9     | acepta   | acepta   | válida       |
| `2`         |    1     | rechaza  | rechaza  | inválida     |
| `02`        |    2     | rechaza  | rechaza  | inválida     |
| `0202`      |    4     | rechaza  | rechaza  | inválida     |
| `111101`    |    6     | rechaza  | rechaza  | inválida     |
| `002111012` |    9     | rechaza  | rechaza  | inválida     |

Cadenas de prueba.

## Lista 2 · Ejercicio 122

**Enunciado.** Las palabras de Σ1 tales que cualquier cadena de tres símbolos consecutivos tiene un 0.

**Clase.** AFD: Cada par (estado, símbolo) tiene a lo sumo un destino y no hay transiciones λ. **Archivos.** `automatas/afd/lista2-122.jff` (y `.json`, `.xml`).

**Diseño.** Basta contar cuántos símbolos distintos de 0 hay al final; tres seguidos invalidan la cadena.

| δ           | 0       | 1       | 2       | Qué recuerda del prefijo leído            |
|-------------|---------|---------|---------|-------------------------------------------|
| →\* 0 sin 0 | 0 sin 0 | 1 sin 0 | 1 sin 0 | los últimos 0 símbolos son distintos de 0 |
| \* 1 sin 0  | 0 sin 0 | 2 sin 0 | 2 sin 0 | los últimos 1 símbolos son distintos de 0 |
| \* 2 sin 0  | 0 sin 0 | muerto  | muerto  | los últimos 2 símbolos son distintos de 0 |
| muerto      | muerto  | muerto  | muerto  | hubo tres símbolos seguidos sin 0         |

Tabla de transiciones (→ inicial, \* aceptación, — sin transición).

| Cadena        | Longitud | Esperado | Obtenido | Tipo de caso |
|---------------|:--------:|----------|----------|--------------|
| λ             |    0     | acepta   | acepta   | válida       |
| `1`           |    1     | acepta   | acepta   | válida       |
| `100`         |    3     | acepta   | acepta   | válida       |
| `22010`       |    5     | acepta   | acepta   | válida       |
| `20202021`    |    8     | acepta   | acepta   | válida       |
| `112`         |    3     | rechaza  | rechaza  | inválida     |
| `0122`        |    4     | rechaza  | rechaza  | inválida     |
| `122010`      |    6     | rechaza  | rechaza  | inválida     |
| `21110110`    |    8     | rechaza  | rechaza  | inválida     |
| `01112200022` |    11    | rechaza  | rechaza  | inválida     |

Cadenas de prueba.

## Lista 2 · Ejercicio 123

**Enunciado.** Las palabras de Σ3 de la forma wxw donde w ∈ Σ3² y x ∈ Σ3\*.

**Clase.** AFD: Cada par (estado, símbolo) tiene a lo sumo un destino y no hay transiciones λ. **Archivos.** `automatas/afd/lista2-123.jff` (y `.json`, `.xml`).

**Diseño.** Se memoriza w (los dos primeros símbolos) y, para cada w, tres situaciones: la cadena termina en w, el último símbolo es la primera letra de w, u otra. Tras los dos primeros símbolos el estado es «otra» aunque la cadena termine en w, porque las dos copias de w no pueden traslaparse (se exige longitud ≥ 4).

| δ        | a     | b     | Qué recuerda del prefijo leído                                                    |
|----------|-------|-------|-----------------------------------------------------------------------------------|
| → ini    | a     | b     | no se ha leído nada                                                               |
| a        | aa:∅  | ab:∅  | el primer símbolo es a                                                            |
| b        | ba:∅  | bb:∅  | el primer símbolo es b                                                            |
| aa:∅     | aa:a… | aa:∅  | w = aa; el final leído no sirve para la copia final de w (o la longitud aún es 2) |
| ab:∅     | ab:a… | ab:∅  | w = ab; el final leído no sirve para la copia final de w (o la longitud aún es 2) |
| ba:∅     | ba:∅  | ba:b… | w = ba; el final leído no sirve para la copia final de w (o la longitud aún es 2) |
| bb:∅     | bb:∅  | bb:b… | w = bb; el final leído no sirve para la copia final de w (o la longitud aún es 2) |
| aa:a…    | aa:aa | aa:∅  | w = aa; el último símbolo es a, que puede iniciar la copia final de w             |
| ab:a…    | ab:a… | ab:ab | w = ab; el último símbolo es a, que puede iniciar la copia final de w             |
| ba:b…    | ba:ba | ba:b… | w = ba; el último símbolo es b, que puede iniciar la copia final de w             |
| bb:b…    | bb:∅  | bb:bb | w = bb; el último símbolo es b, que puede iniciar la copia final de w             |
| \* aa:aa | aa:aa | aa:∅  | w = aa y la cadena (de longitud ≥ 4) termina en aa                                |
| \* ab:ab | ab:a… | ab:∅  | w = ab y la cadena (de longitud ≥ 4) termina en ab                                |
| \* ba:ba | ba:∅  | ba:b… | w = ba y la cadena (de longitud ≥ 4) termina en ba                                |
| \* bb:bb | bb:∅  | bb:bb | w = bb y la cadena (de longitud ≥ 4) termina en bb                                |

Tabla de transiciones (→ inicial, \* aceptación, — sin transición).

| Cadena         | Longitud | Esperado | Obtenido | Tipo de caso                                     |
|----------------|:--------:|----------|----------|--------------------------------------------------|
| `bbbb`         |    4     | acepta   | acepta   | válida                                           |
| `abbab`        |    5     | acepta   | acepta   | válida                                           |
| `bbbbabb`      |    7     | acepta   | acepta   | válida                                           |
| `abaabbbab`    |    9     | acepta   | acepta   | válida                                           |
| `abbaabaaaaab` |    12    | acepta   | acepta   | válida                                           |
| λ              |    0     | rechaza  | rechaza  | inválida                                         |
| `a`            |    1     | rechaza  | rechaza  | inválida                                         |
| `bab`          |    3     | rechaza  | rechaza  | inválida                                         |
| `babbb`        |    5     | rechaza  | rechaza  | inválida                                         |
| `aabbbbba`     |    8     | rechaza  | rechaza  | inválida                                         |
| `abab`         |    4     | acepta   | acepta   | frontera: aceptada más corta                     |
| `aaa`          |    3     | rechaza  | rechaza  | frontera: justo por debajo de la longitud mínima |

Cadenas de prueba.

## Lista 2 · Ejercicio 124

**Enunciado.** Mecanismo de tres palancas con canicas (Σ = {0, 1}); se acepta si la última canica sale por A.

**Clase.** AFD: Cada par (estado, símbolo) tiene a lo sumo un destino y no hay transiciones λ. **Archivos.** `automatas/afd/lista2-124.jff` (y `.json`, `.xml`).

**Diseño.** Ver el análisis del mecanismo.

| δ       | 0    | 1    | Qué recuerda del prefijo leído                                                                                       |
|---------|------|------|----------------------------------------------------------------------------------------------------------------------|
| → III   | DIIa | IDDa | palancas izquierda=I, derecha=I, central=I (I: desvía a la izquierda, D: a la derecha); aún no cae ninguna canica    |
| \* DIIa | IIDa | DDDa | palancas izquierda=D, derecha=I, central=I (I: desvía a la izquierda, D: a la derecha); la última canica salió por A |
| \* IDDa | DDDa | IIDr | palancas izquierda=I, derecha=D, central=D (I: desvía a la izquierda, D: a la derecha); la última canica salió por A |
| \* IIDa | DIDa | IDIr | palancas izquierda=I, derecha=I, central=D (I: desvía a la izquierda, D: a la derecha); la última canica salió por A |
| \* DDDa | IDIr | DIDr | palancas izquierda=D, derecha=D, central=D (I: desvía a la izquierda, D: a la derecha); la última canica salió por A |
| IIDr    | DIDa | IDIr | palancas izquierda=I, derecha=I, central=D (I: desvía a la izquierda, D: a la derecha); la última canica salió por R |
| \* DIDa | IIIr | DDIr | palancas izquierda=D, derecha=I, central=D (I: desvía a la izquierda, D: a la derecha); la última canica salió por A |
| IDIr    | DDIa | IIIr | palancas izquierda=I, derecha=D, central=I (I: desvía a la izquierda, D: a la derecha); la última canica salió por R |
| DIDr    | IIIr | DDIr | palancas izquierda=D, derecha=I, central=D (I: desvía a la izquierda, D: a la derecha); la última canica salió por R |
| IIIr    | DIIa | IDDa | palancas izquierda=I, derecha=I, central=I (I: desvía a la izquierda, D: a la derecha); la última canica salió por R |
| DDIr    | IDDa | DIIr | palancas izquierda=D, derecha=D, central=I (I: desvía a la izquierda, D: a la derecha); la última canica salió por R |
| \* DDIa | IDDa | DIIr | palancas izquierda=D, derecha=D, central=I (I: desvía a la izquierda, D: a la derecha); la última canica salió por A |
| DIIr    | IIDa | DDDa | palancas izquierda=D, derecha=I, central=I (I: desvía a la izquierda, D: a la derecha); la última canica salió por R |

Tabla de transiciones (→ inicial, \* aceptación, — sin transición).

| Cadena      | Longitud | Esperado | Obtenido | Tipo de caso |
|-------------|:--------:|----------|----------|--------------|
| `0`         |    1     | acepta   | acepta   | válida       |
| `01`        |    2     | acepta   | acepta   | válida       |
| `0010`      |    4     | acepta   | acepta   | válida       |
| `010110`    |    6     | acepta   | acepta   | válida       |
| `101101100` |    9     | acepta   | acepta   | válida       |
| λ           |    0     | rechaza  | rechaza  | inválida     |
| `1010`      |    4     | rechaza  | rechaza  | inválida     |
| `00101`     |    5     | rechaza  | rechaza  | inválida     |
| `001111`    |    6     | rechaza  | rechaza  | inválida     |
| `01000001`  |    8     | rechaza  | rechaza  | inválida     |

Cadenas de prueba.

## Lista 2 · Ejercicio 125

**Enunciado.** Sea A = (Q, Σ, δ, A0, F) un AFD. ¿Cuál es el lenguaje de A’ = (Q, Σ, δ, A0, Q  F)?

**Clase.** AFD: Cada par (estado, símbolo) tiene a lo sumo un destino y no hay transiciones λ. **Archivos.** `automatas/afd/lista2-125.jff` (y `.json`, `.xml`).

**Diseño.** Como ejemplo se complementa el AFD de 139 (número par de ceros).

| δ        | 0     | 1     | Qué recuerda del prefijo leído       |
|----------|-------|-------|--------------------------------------|
| → par    | impar | par   | se ha leído un número par de ceros   |
| \* impar | par   | impar | se ha leído un número impar de ceros |

Tabla de transiciones (→ inicial, \* aceptación, — sin transición).

| Cadena      | Longitud | Esperado | Obtenido | Tipo de caso |
|-------------|:--------:|----------|----------|--------------|
| `0`         |    1     | acepta   | acepta   | válida       |
| `01`        |    2     | acepta   | acepta   | válida       |
| `1101`      |    4     | acepta   | acepta   | válida       |
| `111011`    |    6     | acepta   | acepta   | válida       |
| `110000000` |    9     | acepta   | acepta   | válida       |
| λ           |    0     | rechaza  | rechaza  | inválida     |
| `1`         |    1     | rechaza  | rechaza  | inválida     |
| `100`       |    3     | rechaza  | rechaza  | inválida     |
| `00010`     |    5     | rechaza  | rechaza  | inválida     |
| `01101001`  |    8     | rechaza  | rechaza  | inválida     |

Cadenas de prueba.

## Lista 2 · Ejercicio 126

**Enunciado.** Sea A un AFD. ¿Cuál es el lenguaje del autómata si F = ∅?

**Clase.** AFD: Cada par (estado, símbolo) tiene a lo sumo un destino y no hay transiciones λ. **Archivos.** `automatas/afd/lista2-126.jff` (y `.json`, `.xml`).

**Diseño.** Ejemplo: el AFD de 139 con F = ∅.

| δ     | 0     | 1     | Qué recuerda del prefijo leído |
|-------|-------|-------|--------------------------------|
| → par | impar | par   | número par de ceros            |
| impar | par   | impar | número impar de ceros          |

Tabla de transiciones (→ inicial, \* aceptación, — sin transición).

| Cadena     | Longitud | Esperado | Obtenido | Tipo de caso |
|------------|:--------:|----------|----------|--------------|
| λ          |    0     | rechaza  | rechaza  | inválida     |
| `1`        |    1     | rechaza  | rechaza  | inválida     |
| `001`      |    3     | rechaza  | rechaza  | inválida     |
| `10111`    |    5     | rechaza  | rechaza  | inválida     |
| `10001101` |    8     | rechaza  | rechaza  | inválida     |

Cadenas de prueba.

## Lista 2 · Ejercicio 127

**Enunciado.** Sea A un AFD. ¿Cuál es el lenguaje del autómata si F = Q?

**Clase.** AFD: Cada par (estado, símbolo) tiene a lo sumo un destino y no hay transiciones λ. **Archivos.** `automatas/afd/lista2-127.jff` (y `.json`, `.xml`).

**Diseño.** Ejemplo: el AFD de 139 con F = Q.

| δ        | 0     | 1     | Qué recuerda del prefijo leído |
|----------|-------|-------|--------------------------------|
| →\* par  | impar | par   | número par de ceros            |
| \* impar | par   | impar | número impar de ceros          |

Tabla de transiciones (→ inicial, \* aceptación, — sin transición).

| Cadena     | Longitud | Esperado | Obtenido | Tipo de caso |
|------------|:--------:|----------|----------|--------------|
| λ          |    0     | acepta   | acepta   | válida       |
| `1`        |    1     | acepta   | acepta   | válida       |
| `100`      |    3     | acepta   | acepta   | válida       |
| `00001`    |    5     | acepta   | acepta   | válida       |
| `00111011` |    8     | acepta   | acepta   | válida       |

Cadenas de prueba.

## Lista 2 · Ejercicio 128

**Enunciado.** Sea L el lenguaje del autómata del diagrama. Encuentre un AFD para L2 = {w : wa ∈ L para algún símbolo a}.

**Clase.** AFD: Cada par (estado, símbolo) tiene a lo sumo un destino y no hay transiciones λ. **Archivos.** `automatas/afd/lista2-128.jff` (y `.json`, `.xml`).

**Diseño.** Se conservan los estados y las transiciones; un estado q es de aceptación en el nuevo autómata si algún símbolo lo lleva a F. Como δ(D, 0) = F y δ(E, 1) = F, F’ = {D, E}.

| δ    | 0   | 1   | Qué recuerda del prefijo leído           |
|------|-----|-----|------------------------------------------|
| → A  | B   | C   | mismo estado que en el autómata original |
| B    | C   | D   | mismo estado que en el autómata original |
| C    | D   | E   | mismo estado que en el autómata original |
| \* D | F   | E   | mismo estado que en el autómata original |
| \* E | E   | F   | mismo estado que en el autómata original |
| F    | D   | D   | mismo estado que en el autómata original |

Tabla de transiciones (→ inicial, \* aceptación, — sin transición).

| Cadena       | Longitud | Esperado | Obtenido | Tipo de caso |
|--------------|:--------:|----------|----------|--------------|
| `10`         |    2     | acepta   | acepta   | válida       |
| `001`        |    3     | acepta   | acepta   | válida       |
| `10100`      |    5     | acepta   | acepta   | válida       |
| `0010101`    |    7     | acepta   | acepta   | válida       |
| `0100011101` |    10    | acepta   | acepta   | válida       |
| λ            |    0     | rechaza  | rechaza  | inválida     |
| `1`          |    1     | rechaza  | rechaza  | inválida     |
| `111`        |    3     | rechaza  | rechaza  | inválida     |
| `11100`      |    5     | rechaza  | rechaza  | inválida     |
| `01001001`   |    8     | rechaza  | rechaza  | inválida     |

Cadenas de prueba.

## Lista 2 · Ejercicio 129

**Enunciado.** AFD dado: palabras de {a, b}\* que no contienen tres b consecutivas.

**Clase.** AFD: Cada par (estado, símbolo) tiene a lo sumo un destino y no hay transiciones λ. **Archivos.** `automatas/afd/lista2-129.jff` (y `.json`, `.xml`).

**Diseño.** qᵢ (i ≤ 2) indica que la cadena termina con i bes seguidas; q3, que ya apareció bbb.

| δ      | a   | b   |
|--------|-----|-----|
| →\* q0 | q0  | q1  |
| \* q1  | q0  | q2  |
| \* q2  | q0  | q3  |
| q3     | q3  | q3  |

Tabla de transiciones (→ inicial, \* aceptación, — sin transición).

| Cadena        | Longitud | Esperado | Obtenido | Tipo de caso |
|---------------|:--------:|----------|----------|--------------|
| λ             |    0     | acepta   | acepta   | válida       |
| `b`           |    1     | acepta   | acepta   | válida       |
| `baa`         |    3     | acepta   | acepta   | válida       |
| `babba`       |    5     | acepta   | acepta   | válida       |
| `abbababa`    |    8     | acepta   | acepta   | válida       |
| `bbb`         |    3     | rechaza  | rechaza  | inválida     |
| `abbb`        |    4     | rechaza  | rechaza  | inválida     |
| `abbbaa`      |    6     | rechaza  | rechaza  | inválida     |
| `abbbabba`    |    8     | rechaza  | rechaza  | inválida     |
| `abbabbbaaaa` |    11    | rechaza  | rechaza  | inválida     |

Cadenas de prueba.

## Lista 2 · Ejercicio 130

**Enunciado.** AFD dado M = ({q1, q2, q3}, {0, 1}, δ, q1, {q2}).

**Clase.** AFD: Cada par (estado, símbolo) tiene a lo sumo un destino y no hay transiciones λ. **Archivos.** `automatas/afd/lista2-130.jff` (y `.json`, `.xml`).

**Diseño.** q1: aún no hay unos. Después del primer 1, cada 1 lleva a q2 y los ceros alternan q3 y q2.

| δ     | 0   | 1   |
|-------|-----|-----|
| → q1  | q1  | q2  |
| \* q2 | q3  | q2  |
| q3    | q2  | q2  |

Tabla de transiciones (→ inicial, \* aceptación, — sin transición).

| Cadena      | Longitud | Esperado | Obtenido | Tipo de caso |
|-------------|:--------:|----------|----------|--------------|
| `1`         |    1     | acepta   | acepta   | válida       |
| `01`        |    2     | acepta   | acepta   | válida       |
| `1001`      |    4     | acepta   | acepta   | válida       |
| `011100`    |    6     | acepta   | acepta   | válida       |
| `101001100` |    9     | acepta   | acepta   | válida       |
| λ           |    0     | rechaza  | rechaza  | inválida     |
| `0`         |    1     | rechaza  | rechaza  | inválida     |
| `000`       |    3     | rechaza  | rechaza  | inválida     |
| `00110`     |    5     | rechaza  | rechaza  | inválida     |
| `11100110`  |    8     | rechaza  | rechaza  | inválida     |

Cadenas de prueba.

## Lista 2 · Ejercicio 131

**Enunciado.** AFD dado M = ({q1, q2}, {0, 1}, δ, q1, {q2}).

**Clase.** AFD: Cada par (estado, símbolo) tiene a lo sumo un destino y no hay transiciones λ. **Archivos.** `automatas/afd/lista2-131.jff` (y `.json`, `.xml`).

**Diseño.** q2 significa que el último símbolo leído es 1.

| δ     | 0   | 1   |
|-------|-----|-----|
| → q1  | q1  | q2  |
| \* q2 | q1  | q2  |

Tabla de transiciones (→ inicial, \* aceptación, — sin transición).

| Cadena      | Longitud | Esperado | Obtenido | Tipo de caso |
|-------------|:--------:|----------|----------|--------------|
| `1`         |    1     | acepta   | acepta   | válida       |
| `11`        |    2     | acepta   | acepta   | válida       |
| `0111`      |    4     | acepta   | acepta   | válida       |
| `100111`    |    6     | acepta   | acepta   | válida       |
| `000010011` |    9     | acepta   | acepta   | válida       |
| λ           |    0     | rechaza  | rechaza  | inválida     |
| `0`         |    1     | rechaza  | rechaza  | inválida     |
| `010`       |    3     | rechaza  | rechaza  | inválida     |
| `01100`     |    5     | rechaza  | rechaza  | inválida     |
| `01110010`  |    8     | rechaza  | rechaza  | inválida     |

Cadenas de prueba.

## Lista 2 · Ejercicio 132

**Enunciado.** Diseñar un AFD para L = {aⁿb : n ≥ 0}.

**Clase.** AFD: Cada par (estado, símbolo) tiene a lo sumo un destino y no hay transiciones λ. **Archivos.** `automatas/afd/lista2-132.jff` (y `.json`, `.xml`).

**Diseño.** Ciclo de aes y una única b final.

| δ       | a      | b      | Qué recuerda del prefijo leído |
|---------|--------|--------|--------------------------------|
| → a\*   | a\*    | a\*b   | sólo se han leído aes          |
| \* a\*b | muerto | muerto | se leyó la única b             |
| muerto  | muerto | muerto | hubo algo después de la b      |

Tabla de transiciones (→ inicial, \* aceptación, — sin transición).

| Cadena      | Longitud | Esperado | Obtenido | Tipo de caso |
|-------------|:--------:|----------|----------|--------------|
| `b`         |    1     | acepta   | acepta   | válida       |
| `ab`        |    2     | acepta   | acepta   | válida       |
| `aaab`      |    4     | acepta   | acepta   | válida       |
| `aaaaab`    |    6     | acepta   | acepta   | válida       |
| `aaaaaaaab` |    9     | acepta   | acepta   | válida       |
| λ           |    0     | rechaza  | rechaza  | inválida     |
| `a`         |    1     | rechaza  | rechaza  | inválida     |
| `bba`       |    3     | rechaza  | rechaza  | inválida     |
| `bbbba`     |    5     | rechaza  | rechaza  | inválida     |
| `bbaababa`  |    8     | rechaza  | rechaza  | inválida     |

Cadenas de prueba.

## Lista 2 · Ejercicio 133

**Enunciado.** AFD dado con Q = {q0, q1, q2, q3}, Σ = {a, b}, F = {q0}.

**Clase.** AFD: Cada par (estado, símbolo) tiene a lo sumo un destino y no hay transiciones λ. **Archivos.** `automatas/afd/lista2-133.jff` (y `.json`, `.xml`).

**Diseño.** q0 = (a par, b par), q1 = (a par, b impar), q2 = (a impar, b par), q3 = (a impar, b impar).

| δ      | a   | b   |
|--------|-----|-----|
| →\* q0 | q2  | q1  |
| q1     | q3  | q0  |
| q2     | q0  | q3  |
| q3     | q1  | q2  |

Tabla de transiciones (→ inicial, \* aceptación, — sin transición).

| Cadena      | Longitud | Esperado | Obtenido | Tipo de caso |
|-------------|:--------:|----------|----------|--------------|
| λ           |    0     | acepta   | acepta   | válida       |
| `baab`      |    4     | acepta   | acepta   | válida       |
| `bbaa`      |    4     | acepta   | acepta   | válida       |
| `aabbaa`    |    6     | acepta   | acepta   | válida       |
| `baabaa`    |    6     | acepta   | acepta   | válida       |
| `a`         |    1     | rechaza  | rechaza  | inválida     |
| `ab`        |    2     | rechaza  | rechaza  | inválida     |
| `baaa`      |    4     | rechaza  | rechaza  | inválida     |
| `aabbab`    |    6     | rechaza  | rechaza  | inválida     |
| `aaabbbbab` |    9     | rechaza  | rechaza  | inválida     |

Cadenas de prueba.

## Lista 2 · Ejercicio 134

**Enunciado.** L(M) = {w ∈ {a, b, c}\* : w contiene el patrón abac}.

**Clase.** AFD: Cada par (estado, símbolo) tiene a lo sumo un destino y no hay transiciones λ. **Archivos.** `automatas/afd/lista2-134.jff` (y `.json`, `.xml`).

**Diseño.** Autómata de búsqueda de abac (Knuth-Morris-Pratt).

| δ       | a    | b    | c    | Qué recuerda del prefijo leído                                               |
|---------|------|------|------|------------------------------------------------------------------------------|
| → λ     | a    | λ    | λ    | aún no aparece abac; el sufijo más largo leído que es prefijo de abac es λ   |
| a       | a    | ab   | λ    | aún no aparece abac; el sufijo más largo leído que es prefijo de abac es a   |
| ab      | aba  | λ    | λ    | aún no aparece abac; el sufijo más largo leído que es prefijo de abac es ab  |
| aba     | a    | ab   | abac | aún no aparece abac; el sufijo más largo leído que es prefijo de abac es aba |
| \* abac | abac | abac | abac | ya apareció abac                                                             |

Tabla de transiciones (→ inicial, \* aceptación, — sin transición).

| Cadena         | Longitud | Esperado | Obtenido | Tipo de caso                                     |
|----------------|:--------:|----------|----------|--------------------------------------------------|
| `abac`         |    4     | acepta   | acepta   | válida                                           |
| `abaca`        |    5     | acepta   | acepta   | válida                                           |
| `bbaabac`      |    7     | acepta   | acepta   | válida                                           |
| `abacbbcbb`    |    9     | acepta   | acepta   | válida                                           |
| `ababacccacab` |    12    | acepta   | acepta   | válida                                           |
| λ              |    0     | rechaza  | rechaza  | inválida                                         |
| `c`            |    1     | rechaza  | rechaza  | inválida                                         |
| `bcc`          |    3     | rechaza  | rechaza  | inválida                                         |
| `ccaba`        |    5     | rechaza  | rechaza  | inválida                                         |
| `acbcbbcc`     |    8     | rechaza  | rechaza  | inválida                                         |
| `aaa`          |    3     | rechaza  | rechaza  | frontera: justo por debajo de la longitud mínima |

Cadenas de prueba.

## Lista 2 · Ejercicio 135

**Enunciado.** Dado Σ = {a, b}, AFD para L = {bᵐabⁿ : m, n \> 0}.

**Clase.** AFD: Cada par (estado, símbolo) tiene a lo sumo un destino y no hay transiciones λ. **Archivos.** `automatas/afd/lista2-135.jff` (y `.json`, `.xml`).

**Diseño.** Cuatro fases; m \> 0 y n \> 0 exigen al menos una b en cada lado.

| δ        | a      | b      | Qué recuerda del prefijo leído |
|----------|--------|--------|--------------------------------|
| → ini    | muerto | b+     | no se ha leído nada            |
| muerto   | muerto | muerto | la cadena no tiene la forma    |
| b+       | b+a    | b+     | una o más bes iniciales        |
| b+a      | muerto | b+ab+  | bes y la a                     |
| \* b+ab+ | muerto | b+ab+  | bes, la a y una o más bes      |

Tabla de transiciones (→ inicial, \* aceptación, — sin transición).

| Cadena        | Longitud | Esperado | Obtenido | Tipo de caso                                     |
|---------------|:--------:|----------|----------|--------------------------------------------------|
| `bab`         |    3     | acepta   | acepta   | válida                                           |
| `babb`        |    4     | acepta   | acepta   | válida                                           |
| `bbbbab`      |    6     | acepta   | acepta   | válida                                           |
| `bbabbbbb`    |    8     | acepta   | acepta   | válida                                           |
| `bbbabbbbbbb` |    11    | acepta   | acepta   | válida                                           |
| λ             |    0     | rechaza  | rechaza  | inválida                                         |
| `b`           |    1     | rechaza  | rechaza  | inválida                                         |
| `bba`         |    3     | rechaza  | rechaza  | inválida                                         |
| `aabbb`       |    5     | rechaza  | rechaza  | inválida                                         |
| `abbaaaba`    |    8     | rechaza  | rechaza  | inválida                                         |
| `aa`          |    2     | rechaza  | rechaza  | frontera: justo por debajo de la longitud mínima |

Cadenas de prueba.

## Lista 2 · Ejercicio 136

**Enunciado.** Dado Σ = {a, b}, AFD para L = {aᵐbⁿ : m, n \> 0}.

**Clase.** AFD: Cada par (estado, símbolo) tiene a lo sumo un destino y no hay transiciones λ. **Archivos.** `automatas/afd/lista2-136.jff` (y `.json`, `.xml`).

**Diseño.** Tres fases con al menos un símbolo en cada bloque.

| δ       | a      | b      | Qué recuerda del prefijo leído |
|---------|--------|--------|--------------------------------|
| → ini   | a+     | muerto | no se ha leído nada            |
| a+      | a+     | a+b+   | una o más aes                  |
| muerto  | muerto | muerto | orden incorrecto               |
| \* a+b+ | muerto | a+b+   | aes y una o más bes            |

Tabla de transiciones (→ inicial, \* aceptación, — sin transición).

| Cadena       | Longitud | Esperado | Obtenido | Tipo de caso                                     |
|--------------|:--------:|----------|----------|--------------------------------------------------|
| `ab`         |    2     | acepta   | acepta   | válida                                           |
| `aab`        |    3     | acepta   | acepta   | válida                                           |
| `aaabb`      |    5     | acepta   | acepta   | válida                                           |
| `aaaaabb`    |    7     | acepta   | acepta   | válida                                           |
| `aaaaaaabbb` |    10    | acepta   | acepta   | válida                                           |
| λ            |    0     | rechaza  | rechaza  | inválida                                         |
| `a`          |    1     | rechaza  | rechaza  | inválida                                         |
| `bbb`        |    3     | rechaza  | rechaza  | inválida                                         |
| `babaa`      |    5     | rechaza  | rechaza  | inválida                                         |
| `bbbabbba`   |    8     | rechaza  | rechaza  | inválida                                         |
| `b`          |    1     | rechaza  | rechaza  | frontera: justo por debajo de la longitud mínima |

Cadenas de prueba.

## Lista 2 · Ejercicio 137

**Enunciado.** AFD que reconozca las cadenas sobre {a, b} que comienzan con el prefijo ab.

**Clase.** AFD: Cada par (estado, símbolo) tiene a lo sumo un destino y no hay transiciones λ. **Archivos.** `automatas/afd/lista2-137.jff` (y `.json`, `.xml`).

**Diseño.** Se verifica el prefijo y después se acepta todo.

| δ      | a      | b      | Qué recuerda del prefijo leído             |
|--------|--------|--------|--------------------------------------------|
| → λ    | a      | muerto | se han leído los primeros 0 símbolos de ab |
| a      | muerto | ab     | se han leído los primeros 1 símbolos de ab |
| muerto | muerto | muerto | el prefijo leído no coincide con ab        |
| \* ab  | ab     | ab     | ya se leyó el prefijo ab                   |

Tabla de transiciones (→ inicial, \* aceptación, — sin transición).

| Cadena       | Longitud | Esperado | Obtenido | Tipo de caso                                     |
|--------------|:--------:|----------|----------|--------------------------------------------------|
| `ab`         |    2     | acepta   | acepta   | válida                                           |
| `aba`        |    3     | acepta   | acepta   | válida                                           |
| `abbbb`      |    5     | acepta   | acepta   | válida                                           |
| `abaaaaa`    |    7     | acepta   | acepta   | válida                                           |
| `abaaabaaab` |    10    | acepta   | acepta   | válida                                           |
| λ            |    0     | rechaza  | rechaza  | inválida                                         |
| `b`          |    1     | rechaza  | rechaza  | inválida                                         |
| `bab`        |    3     | rechaza  | rechaza  | inválida                                         |
| `bbbab`      |    5     | rechaza  | rechaza  | inválida                                         |
| `bbabaaba`   |    8     | rechaza  | rechaza  | inválida                                         |
| `a`          |    1     | rechaza  | rechaza  | frontera: justo por debajo de la longitud mínima |

Cadenas de prueba.

## Lista 2 · Ejercicio 138

**Enunciado.** AFD para las palabras sobre {a, b} cuyo número de bes es divisible entre tres.

**Clase.** AFD: Cada par (estado, símbolo) tiene a lo sumo un destino y no hay transiciones λ. **Archivos.** `automatas/afd/lista2-138.jff` (y `.json`, `.xml`).

**Diseño.** Contador de bes módulo 3; las aes no cambian de estado.

| δ       | a   | b   | Qué recuerda del prefijo leído  |
|---------|-----|-----|---------------------------------|
| →\* b≡0 | b≡0 | b≡1 | el número de bes es ≡ 0 (mod 3) |
| b≡1     | b≡1 | b≡2 | el número de bes es ≡ 1 (mod 3) |
| b≡2     | b≡2 | b≡0 | el número de bes es ≡ 2 (mod 3) |

Tabla de transiciones (→ inicial, \* aceptación, — sin transición).

| Cadena      | Longitud | Esperado | Obtenido | Tipo de caso |
|-------------|:--------:|----------|----------|--------------|
| λ           |    0     | acepta   | acepta   | válida       |
| `a`         |    1     | acepta   | acepta   | válida       |
| `aaa`       |    3     | acepta   | acepta   | válida       |
| `aabbb`     |    5     | acepta   | acepta   | válida       |
| `bbabbabb`  |    8     | acepta   | acepta   | válida       |
| `b`         |    1     | rechaza  | rechaza  | inválida     |
| `ba`        |    2     | rechaza  | rechaza  | inválida     |
| `abba`      |    4     | rechaza  | rechaza  | inválida     |
| `aabbaa`    |    6     | rechaza  | rechaza  | inválida     |
| `baaaaaaba` |    9     | rechaza  | rechaza  | inválida     |

Cadenas de prueba.

## Lista 2 · Ejercicio 139

**Enunciado.** Autómata que acepte las cadenas en {0, 1}\* con un número par de ceros.

**Clase.** AFD: Cada par (estado, símbolo) tiene a lo sumo un destino y no hay transiciones λ. **Archivos.** `automatas/afd/lista2-139.jff` (y `.json`, `.xml`).

**Diseño.** Paridad de ceros.

| δ       | 0     | 1     | Qué recuerda del prefijo leído       |
|---------|-------|-------|--------------------------------------|
| →\* par | impar | par   | se ha leído un número par de ceros   |
| impar   | par   | impar | se ha leído un número impar de ceros |

Tabla de transiciones (→ inicial, \* aceptación, — sin transición).

| Cadena      | Longitud | Esperado | Obtenido | Tipo de caso |
|-------------|:--------:|----------|----------|--------------|
| λ           |    0     | acepta   | acepta   | válida       |
| `1`         |    1     | acepta   | acepta   | válida       |
| `010`       |    3     | acepta   | acepta   | válida       |
| `10000`     |    5     | acepta   | acepta   | válida       |
| `11100111`  |    8     | acepta   | acepta   | válida       |
| `0`         |    1     | rechaza  | rechaza  | inválida     |
| `01`        |    2     | rechaza  | rechaza  | inválida     |
| `0100`      |    4     | rechaza  | rechaza  | inválida     |
| `000100`    |    6     | rechaza  | rechaza  | inválida     |
| `011011110` |    9     | rechaza  | rechaza  | inválida     |

Cadenas de prueba.

## Lista 2 · Ejercicio 140a

**Enunciado.** a) Cadenas sobre {0, 1} con un número impar de ceros.

**Clase.** AFD: Cada par (estado, símbolo) tiene a lo sumo un destino y no hay transiciones λ. **Archivos.** `automatas/afd/lista2-140a.jff` (y `.json`, `.xml`).

**Diseño.** Paridad de ceros; acepta impar.

| δ        | 0     | 1     | Qué recuerda del prefijo leído |
|----------|-------|-------|--------------------------------|
| → par    | impar | par   | número par de ceros            |
| \* impar | par   | impar | número impar de ceros          |

Tabla de transiciones (→ inicial, \* aceptación, — sin transición).

| Cadena      | Longitud | Esperado | Obtenido | Tipo de caso |
|-------------|:--------:|----------|----------|--------------|
| `0`         |    1     | acepta   | acepta   | válida       |
| `10`        |    2     | acepta   | acepta   | válida       |
| `1110`      |    4     | acepta   | acepta   | válida       |
| `001011`    |    6     | acepta   | acepta   | válida       |
| `011010001` |    9     | acepta   | acepta   | válida       |
| λ           |    0     | rechaza  | rechaza  | inválida     |
| `1`         |    1     | rechaza  | rechaza  | inválida     |
| `100`       |    3     | rechaza  | rechaza  | inválida     |
| `00001`     |    5     | rechaza  | rechaza  | inválida     |
| `10010011`  |    8     | rechaza  | rechaza  | inválida     |

Cadenas de prueba.

## Lista 2 · Ejercicio 140b

**Enunciado.** b) Cadenas sobre {0, 1} con un número par de ceros y un número par de unos.

**Clase.** AFD: Cada par (estado, símbolo) tiene a lo sumo un destino y no hay transiciones λ. **Archivos.** `automatas/afd/lista2-140b.jff` (y `.json`, `.xml`).

**Diseño.** Producto de las dos paridades.

| δ        | 0    | 1    | Qué recuerda del prefijo leído |
|----------|------|------|--------------------------------|
| →\* 0p1p | 0i1p | 0p1i | ceros pares, unos pares        |
| 0i1p     | 0p1p | 0i1i | ceros impares, unos pares      |
| 0p1i     | 0i1i | 0p1p | ceros pares, unos impares      |
| 0i1i     | 0p1i | 0i1p | ceros impares, unos impares    |

Tabla de transiciones (→ inicial, \* aceptación, — sin transición).

| Cadena         | Longitud | Esperado | Obtenido | Tipo de caso |
|----------------|:--------:|----------|----------|--------------|
| λ              |    0     | acepta   | acepta   | válida       |
| `11`           |    2     | acepta   | acepta   | válida       |
| `0000`         |    4     | acepta   | acepta   | válida       |
| `01100110`     |    8     | acepta   | acepta   | válida       |
| `001110000100` |    12    | acepta   | acepta   | válida       |
| `1`            |    1     | rechaza  | rechaza  | inválida     |
| `10`           |    2     | rechaza  | rechaza  | inválida     |
| `0100`         |    4     | rechaza  | rechaza  | inválida     |
| `111000`       |    6     | rechaza  | rechaza  | inválida     |
| `111101010`    |    9     | rechaza  | rechaza  | inválida     |

Cadenas de prueba.

## Lista 2 · Ejercicio 141

**Enunciado.** L = {w ∈ {0, 1}\* : cada 0 en w tiene un 1 inmediatamente a su derecha}.

**Clase.** AFD: Cada par (estado, símbolo) tiene a lo sumo un destino y no hay transiciones λ. **Archivos.** `automatas/afd/lista2-141.jff` (y `.json`, `.xml`).

**Diseño.** Un estado de espera después de cada 0.

| δ      | 0      | 1      | Qué recuerda del prefijo leído |
|--------|--------|--------|--------------------------------|
| →\* ok | 0?     | ok     | todo 0 leído ya tiene su 1     |
| 0?     | muerto | ok     | el último 0 aún espera su 1    |
| muerto | muerto | muerto | un 0 no fue seguido de 1       |

Tabla de transiciones (→ inicial, \* aceptación, — sin transición).

| Cadena      | Longitud | Esperado | Obtenido | Tipo de caso |
|-------------|:--------:|----------|----------|--------------|
| λ           |    0     | acepta   | acepta   | válida       |
| `1`         |    1     | acepta   | acepta   | válida       |
| `111`       |    3     | acepta   | acepta   | válida       |
| `11111`     |    5     | acepta   | acepta   | válida       |
| `01110111`  |    8     | acepta   | acepta   | válida       |
| `0`         |    1     | rechaza  | rechaza  | inválida     |
| `00`        |    2     | rechaza  | rechaza  | inválida     |
| `0100`      |    4     | rechaza  | rechaza  | inválida     |
| `101001`    |    6     | rechaza  | rechaza  | inválida     |
| `110010110` |    9     | rechaza  | rechaza  | inválida     |

Cadenas de prueba.

## Lista 2 · Ejercicio 142a

**Enunciado.** a) LA = (ab)\* = {(ab)ⁿ : n ≥ 0}.

**Clase.** AFD: Cada par (estado, símbolo) tiene a lo sumo un destino y no hay transiciones λ. **Archivos.** `automatas/afd/lista2-142a.jff` (y `.json`, `.xml`).

**Diseño.** El enunciado indica que λ no se acepta, pero (ab)\* con n ≥ 0 sí la contiene; se sigue la definición del lenguaje y se acepta λ. El inciso b) es la versión sin λ.

| δ          | a      | b      | Qué recuerda del prefijo leído             |
|------------|--------|--------|--------------------------------------------|
| →\* (ab)\* | …a     | muerto | se han leído bloques ab completos (o nada) |
| …a         | muerto | (ab)\* | falta la b del bloque                      |
| muerto     | muerto | muerto | se rompió el patrón                        |

Tabla de transiciones (→ inicial, \* aceptación, — sin transición).

| Cadena           | Longitud | Esperado | Obtenido | Tipo de caso |
|------------------|:--------:|----------|----------|--------------|
| λ                |    0     | acepta   | acepta   | válida       |
| `ab`             |    2     | acepta   | acepta   | válida       |
| `abab`           |    4     | acepta   | acepta   | válida       |
| `abababababab`   |    12    | acepta   | acepta   | válida       |
| `ababababababab` |    14    | acepta   | acepta   | válida       |
| `a`              |    1     | rechaza  | rechaza  | inválida     |
| `aa`             |    2     | rechaza  | rechaza  | inválida     |
| `abba`           |    4     | rechaza  | rechaza  | inválida     |
| `bbbbba`         |    6     | rechaza  | rechaza  | inválida     |
| `aaaaaabab`      |    9     | rechaza  | rechaza  | inválida     |

Cadenas de prueba.

## Lista 2 · Ejercicio 142b

**Enunciado.** b) LB = {(ab)ⁿ : n ≥ 1}.

**Clase.** AFD: Cada par (estado, símbolo) tiene a lo sumo un destino y no hay transiciones λ. **Archivos.** `automatas/afd/lista2-142b.jff` (y `.json`, `.xml`).

**Diseño.** Como a) pero el estado inicial no es de aceptación.

| δ      | a      | b      | Qué recuerda del prefijo leído |
|--------|--------|--------|--------------------------------|
| → ini  | …a     | muerto | no se ha leído nada            |
| …a     | muerto | …ab    | falta la b del bloque          |
| muerto | muerto | muerto | se rompió el patrón            |
| \* …ab | …a     | muerto | uno o más bloques ab           |

Tabla de transiciones (→ inicial, \* aceptación, — sin transición).

| Cadena         | Longitud | Esperado | Obtenido | Tipo de caso                                     |
|----------------|:--------:|----------|----------|--------------------------------------------------|
| `ab`           |    2     | acepta   | acepta   | válida                                           |
| `abab`         |    4     | acepta   | acepta   | válida                                           |
| `ababab`       |    6     | acepta   | acepta   | válida                                           |
| `abababab`     |    8     | acepta   | acepta   | válida                                           |
| `abababababab` |    12    | acepta   | acepta   | válida                                           |
| λ              |    0     | rechaza  | rechaza  | inválida                                         |
| `a`            |    1     | rechaza  | rechaza  | inválida                                         |
| `aba`          |    3     | rechaza  | rechaza  | inválida                                         |
| `aabaa`        |    5     | rechaza  | rechaza  | inválida                                         |
| `bbbbabab`     |    8     | rechaza  | rechaza  | inválida                                         |
| `b`            |    1     | rechaza  | rechaza  | frontera: justo por debajo de la longitud mínima |

Cadenas de prueba.

## Lista 2 · Ejercicio 144a

**Enunciado.** a) El conjunto de cadenas sobre {a, b} que comienzan con a.

**Clase.** AFD: Cada par (estado, símbolo) tiene a lo sumo un destino y no hay transiciones λ. **Archivos.** `automatas/afd/lista2-144a.jff` (y `.json`, `.xml`).

**Diseño.** Se verifica el primer símbolo.

| δ      | a      | b      | Qué recuerda del prefijo leído            |
|--------|--------|--------|-------------------------------------------|
| → λ    | a      | muerto | se han leído los primeros 0 símbolos de a |
| \* a   | a      | a      | ya se leyó el prefijo a                   |
| muerto | muerto | muerto | el prefijo leído no coincide con a        |

Tabla de transiciones (→ inicial, \* aceptación, — sin transición).

| Cadena      | Longitud | Esperado | Obtenido | Tipo de caso |
|-------------|:--------:|----------|----------|--------------|
| `a`         |    1     | acepta   | acepta   | válida       |
| `aa`        |    2     | acepta   | acepta   | válida       |
| `abaa`      |    4     | acepta   | acepta   | válida       |
| `aaaaba`    |    6     | acepta   | acepta   | válida       |
| `aaaaaaabb` |    9     | acepta   | acepta   | válida       |
| λ           |    0     | rechaza  | rechaza  | inválida     |
| `b`         |    1     | rechaza  | rechaza  | inválida     |
| `bba`       |    3     | rechaza  | rechaza  | inválida     |
| `baaba`     |    5     | rechaza  | rechaza  | inválida     |
| `baaabbbb`  |    8     | rechaza  | rechaza  | inválida     |

Cadenas de prueba.

## Lista 2 · Ejercicio 144b

**Enunciado.** b) El conjunto de cadenas que comienzan con a y terminan con b.

**Clase.** AFD: Cada par (estado, símbolo) tiene a lo sumo un destino y no hay transiciones λ. **Archivos.** `automatas/afd/lista2-144b.jff` (y `.json`, `.xml`).

**Diseño.** Igual que 94 con otro alfabeto.

| δ      | a      | b      | Qué recuerda del prefijo leído    |
|--------|--------|--------|-----------------------------------|
| → ini  | a…     | muerto | no se ha leído nada               |
| a…     | a…     | a…b    | empieza con a y el último no es b |
| muerto | muerto | muerto | no empieza con a                  |
| \* a…b | a…     | a…b    | empieza con a y el último es b    |

Tabla de transiciones (→ inicial, \* aceptación, — sin transición).

| Cadena       | Longitud | Esperado | Obtenido | Tipo de caso                                     |
|--------------|:--------:|----------|----------|--------------------------------------------------|
| `ab`         |    2     | acepta   | acepta   | válida                                           |
| `aab`        |    3     | acepta   | acepta   | válida                                           |
| `aaaab`      |    5     | acepta   | acepta   | válida                                           |
| `aaabaab`    |    7     | acepta   | acepta   | válida                                           |
| `aaaaaaaaab` |    10    | acepta   | acepta   | válida                                           |
| λ            |    0     | rechaza  | rechaza  | inválida                                         |
| `a`          |    1     | rechaza  | rechaza  | inválida                                         |
| `aba`        |    3     | rechaza  | rechaza  | inválida                                         |
| `babba`      |    5     | rechaza  | rechaza  | inválida                                         |
| `aaabaaaa`   |    8     | rechaza  | rechaza  | inválida                                         |
| `b`          |    1     | rechaza  | rechaza  | frontera: justo por debajo de la longitud mínima |

Cadenas de prueba.

## Lista 2 · Ejercicio 144c

**Enunciado.** c) El conjunto de cadenas que contienen aaa.

**Clase.** AFD: Cada par (estado, símbolo) tiene a lo sumo un destino y no hay transiciones λ. **Archivos.** `automatas/afd/lista2-144c.jff` (y `.json`, `.xml`).

**Diseño.** Búsqueda del patrón aaa.

| δ      | a   | b   | Qué recuerda del prefijo leído                                            |
|--------|-----|-----|---------------------------------------------------------------------------|
| → λ    | a   | λ   | aún no aparece aaa; el sufijo más largo leído que es prefijo de aaa es λ  |
| a      | aa  | λ   | aún no aparece aaa; el sufijo más largo leído que es prefijo de aaa es a  |
| aa     | aaa | λ   | aún no aparece aaa; el sufijo más largo leído que es prefijo de aaa es aa |
| \* aaa | aaa | aaa | ya apareció aaa                                                           |

Tabla de transiciones (→ inicial, \* aceptación, — sin transición).

| Cadena        | Longitud | Esperado | Obtenido | Tipo de caso                                     |
|---------------|:--------:|----------|----------|--------------------------------------------------|
| `aaa`         |    3     | acepta   | acepta   | válida                                           |
| `baaa`        |    4     | acepta   | acepta   | válida                                           |
| `baaaaa`      |    6     | acepta   | acepta   | válida                                           |
| `aaababbb`    |    8     | acepta   | acepta   | válida                                           |
| `aaabbaabbaa` |    11    | acepta   | acepta   | válida                                           |
| λ             |    0     | rechaza  | rechaza  | inválida                                         |
| `a`           |    1     | rechaza  | rechaza  | inválida                                         |
| `abb`         |    3     | rechaza  | rechaza  | inválida                                         |
| `abbab`       |    5     | rechaza  | rechaza  | inválida                                         |
| `bbabbaab`    |    8     | rechaza  | rechaza  | inválida                                         |
| `ab`          |    2     | rechaza  | rechaza  | frontera: justo por debajo de la longitud mínima |

Cadenas de prueba.

## Lista 2 · Ejercicio 144d

**Enunciado.** d) El conjunto de números enteros (sin signo).

**Clase.** AFD: Cada par (estado, símbolo) tiene a lo sumo un destino y no hay transiciones λ. **Archivos.** `automatas/afd/lista2-144d.jff` (y `.json`, `.xml`).

**Diseño.** Se interpreta un entero como una cadena no vacía de dígitos sin ceros a la izquierda (salvo el propio 0).

| δ       | 0      | 1      | 2      | 3      | 4      | 5      | 6      | 7      | 8      | 9      | Qué recuerda del prefijo leído         |
|---------|--------|--------|--------|--------|--------|--------|--------|--------|--------|--------|----------------------------------------|
| → ini   | cero   | ok     | ok     | ok     | ok     | ok     | ok     | ok     | ok     | ok     | no se ha leído nada                    |
| \* cero | muerto | muerto | muerto | muerto | muerto | muerto | muerto | muerto | muerto | muerto | el número es 0                         |
| \* ok   | ok     | ok     | ok     | ok     | ok     | ok     | ok     | ok     | ok     | ok     | dígito inicial distinto de 0 y dígitos |
| muerto  | muerto | muerto | muerto | muerto | muerto | muerto | muerto | muerto | muerto | muerto | cero a la izquierda                    |

Tabla de transiciones (→ inicial, \* aceptación, — sin transición).

| Cadena           | Longitud | Esperado | Obtenido | Tipo de caso                 |
|------------------|:--------:|----------|----------|------------------------------|
| `8`              |    1     | acepta   | acepta   | válida                       |
| `43`             |    2     | acepta   | acepta   | válida                       |
| `2415`           |    4     | acepta   | acepta   | válida                       |
| `117250`         |    6     | acepta   | acepta   | válida                       |
| `438013017`      |    9     | acepta   | acepta   | válida                       |
| λ                |    0     | rechaza  | rechaza  | inválida                     |
| `0800`           |    4     | rechaza  | rechaza  | inválida                     |
| `001388`         |    6     | rechaza  | rechaza  | inválida                     |
| `0883244971`     |    10    | rechaza  | rechaza  | inválida                     |
| `09967547184791` |    14    | rechaza  | rechaza  | inválida                     |
| `2`              |    1     | acepta   | acepta   | frontera: aceptada más corta |

Cadenas de prueba.

## Lista 2 · Ejercicio 144e

**Enunciado.** e) El conjunto de números enteros con signo.

**Clase.** AFD: Cada par (estado, símbolo) tiene a lo sumo un destino y no hay transiciones λ. **Archivos.** `automatas/afd/lista2-144e.jff` (y `.json`, `.xml`).

**Diseño.** Signo opcional (+ o −) seguido de un entero como en d).

| δ       | \+     | \-     | 0      | 1      | 2      | 3      | 4      | 5      | 6      | 7      | 8      | 9      | Qué recuerda del prefijo leído  |
|---------|--------|--------|--------|--------|--------|--------|--------|--------|--------|--------|--------|--------|---------------------------------|
| → ini   | signo  | signo  | cero   | ok     | ok     | ok     | ok     | ok     | ok     | ok     | ok     | ok     | no se ha leído nada             |
| \* cero | muerto | muerto | muerto | muerto | muerto | muerto | muerto | muerto | muerto | muerto | muerto | muerto | el número es 0                  |
| \* ok   | muerto | muerto | ok     | ok     | ok     | ok     | ok     | ok     | ok     | ok     | ok     | ok     | dígitos sin cero a la izquierda |
| signo   | muerto | muerto | cero   | ok     | ok     | ok     | ok     | ok     | ok     | ok     | ok     | ok     | se leyó el signo                |
| muerto  | muerto | muerto | muerto | muerto | muerto | muerto | muerto | muerto | muerto | muerto | muerto | muerto | forma inválida                  |

Tabla de transiciones (→ inicial, \* aceptación, — sin transición).

| Cadena      | Longitud | Esperado | Obtenido | Tipo de caso                 |
|-------------|:--------:|----------|----------|------------------------------|
| `1`         |    1     | acepta   | acepta   | válida                       |
| `46`        |    2     | acepta   | acepta   | válida                       |
| `8856`      |    4     | acepta   | acepta   | válida                       |
| `658332`    |    6     | acepta   | acepta   | válida                       |
| `509883324` |    9     | acepta   | acepta   | válida                       |
| λ           |    0     | rechaza  | rechaza  | inválida                     |
| `-`         |    1     | rechaza  | rechaza  | inválida                     |
| `6-5`       |    3     | rechaza  | rechaza  | inválida                     |
| `33-++`     |    5     | rechaza  | rechaza  | inválida                     |
| `21296+77`  |    8     | rechaza  | rechaza  | inválida                     |
| `0`         |    1     | acepta   | acepta   | frontera: aceptada más corta |

Cadenas de prueba.

## Lista 2 · Ejercicio 145

**Enunciado.** AFD que lee un número binario de derecha a izquierda e identifica los múltiplos de 5.

**Clase.** AFD: Cada par (estado, símbolo) tiene a lo sumo un destino y no hay transiciones λ. **Archivos.** `automatas/afd/lista2-145.jff` (y `.json`, `.xml`).

**Diseño.** El primer bit leído es el menos significativo. Si los bits restantes forman (de derecha a izquierda) el número V, leer el bit b hace que el valor total sea b + 2V; así, si se necesita que el total sea ≡ t, el resto debe valer V ≡ (t − b)·2⁻¹ = 3(t − b) (mod 5). El estado guarda ese valor t pendiente: se empieza pidiendo t = 0 y se acepta si, al terminar, lo pendiente es 0. La cadena vacía no es un número y se rechaza.

| δ     | 0   | 1   | Qué recuerda del prefijo leído                                                                    |
|-------|-----|-----|---------------------------------------------------------------------------------------------------|
| → ini | t0  | t2  | no se ha leído ningún bit                                                                         |
| \* t0 | t0  | t2  | los bits que faltan, leídos como número desde su bit menos significativo, deben valer ≡ 0 (mod 5) |
| t2    | t1  | t3  | los bits que faltan, leídos como número desde su bit menos significativo, deben valer ≡ 2 (mod 5) |
| t1    | t3  | t0  | los bits que faltan, leídos como número desde su bit menos significativo, deben valer ≡ 1 (mod 5) |
| t3    | t4  | t1  | los bits que faltan, leídos como número desde su bit menos significativo, deben valer ≡ 3 (mod 5) |
| t4    | t2  | t4  | los bits que faltan, leídos como número desde su bit menos significativo, deben valer ≡ 4 (mod 5) |

Tabla de transiciones (→ inicial, \* aceptación, — sin transición).

| Cadena      | Longitud | Esperado | Obtenido | Tipo de caso |
|-------------|:--------:|----------|----------|--------------|
| `0`         |    1     | acepta   | acepta   | válida       |
| `00`        |    2     | acepta   | acepta   | válida       |
| `1111`      |    4     | acepta   | acepta   | válida       |
| `000000`    |    6     | acepta   | acepta   | válida       |
| `001010000` |    9     | acepta   | acepta   | válida       |
| λ           |    0     | rechaza  | rechaza  | inválida     |
| `1`         |    1     | rechaza  | rechaza  | inválida     |
| `111`       |    3     | rechaza  | rechaza  | inválida     |
| `01110`     |    5     | rechaza  | rechaza  | inválida     |
| `01000111`  |    8     | rechaza  | rechaza  | inválida     |

Cadenas de prueba.

## Lista 2 · Ejercicio 146

**Enunciado.** AFD que lee un número binario de izquierda a derecha y lo acepta si es múltiplo de 5.

**Clase.** AFD: Cada par (estado, símbolo) tiene a lo sumo un destino y no hay transiciones λ. **Archivos.** `automatas/afd/lista2-146.jff` (y `.json`, `.xml`).

**Diseño.** Leer un bit b convierte el valor v en 2v + b, así que basta el residuo mod 5. La cadena vacía no representa un número y se rechaza.

| δ     | 0   | 1   | Qué recuerda del prefijo leído |
|-------|-----|-----|--------------------------------|
| → ini | r0  | r1  | no se ha leído ningún bit      |
| \* r0 | r0  | r1  | el número leído es ≡ 0 (mod 5) |
| r1    | r2  | r3  | el número leído es ≡ 1 (mod 5) |
| r2    | r4  | r0  | el número leído es ≡ 2 (mod 5) |
| r3    | r1  | r2  | el número leído es ≡ 3 (mod 5) |
| r4    | r3  | r4  | el número leído es ≡ 4 (mod 5) |

Tabla de transiciones (→ inicial, \* aceptación, — sin transición).

| Cadena      | Longitud | Esperado | Obtenido | Tipo de caso |
|-------------|:--------:|----------|----------|--------------|
| `0`         |    1     | acepta   | acepta   | válida       |
| `00`        |    2     | acepta   | acepta   | válida       |
| `0000`      |    4     | acepta   | acepta   | válida       |
| `011110`    |    6     | acepta   | acepta   | válida       |
| `101000000` |    9     | acepta   | acepta   | válida       |
| λ           |    0     | rechaza  | rechaza  | inválida     |
| `1`         |    1     | rechaza  | rechaza  | inválida     |
| `010`       |    3     | rechaza  | rechaza  | inválida     |
| `01011`     |    5     | rechaza  | rechaza  | inválida     |
| `11000100`  |    8     | rechaza  | rechaza  | inválida     |

Cadenas de prueba.

## Lista 2 · Ejercicio 147

**Enunciado.** AFD que lee un número binario de izquierda a derecha y lo acepta si es múltiplo de 6.

**Clase.** AFD: Cada par (estado, símbolo) tiene a lo sumo un destino y no hay transiciones λ. **Archivos.** `automatas/afd/lista2-147.jff` (y `.json`, `.xml`).

**Diseño.** Leer un bit b convierte el valor v en 2v + b, así que basta el residuo mod 6. La cadena vacía no representa un número y se rechaza. Este AFD de 7 estados se puede minimizar a 4: r y r + 3 tienen el mismo sucesor (2(r + 3) ≡ 2r), de modo que {r1, r4}, {r2, r5} e {ini, r3} son equivalentes; es la caracterización «múltiplo de 3 y par».

| δ     | 0   | 1   | Qué recuerda del prefijo leído |
|-------|-----|-----|--------------------------------|
| → ini | r0  | r1  | no se ha leído ningún bit      |
| \* r0 | r0  | r1  | el número leído es ≡ 0 (mod 6) |
| r1    | r2  | r3  | el número leído es ≡ 1 (mod 6) |
| r2    | r4  | r5  | el número leído es ≡ 2 (mod 6) |
| r3    | r0  | r1  | el número leído es ≡ 3 (mod 6) |
| r4    | r2  | r3  | el número leído es ≡ 4 (mod 6) |
| r5    | r4  | r5  | el número leído es ≡ 5 (mod 6) |

Tabla de transiciones (→ inicial, \* aceptación, — sin transición).

| Cadena      | Longitud | Esperado | Obtenido | Tipo de caso |
|-------------|:--------:|----------|----------|--------------|
| `0`         |    1     | acepta   | acepta   | válida       |
| `00`        |    2     | acepta   | acepta   | válida       |
| `0000`      |    4     | acepta   | acepta   | válida       |
| `110000`    |    6     | acepta   | acepta   | válida       |
| `101010000` |    9     | acepta   | acepta   | válida       |
| λ           |    0     | rechaza  | rechaza  | inválida     |
| `1`         |    1     | rechaza  | rechaza  | inválida     |
| `010`       |    3     | rechaza  | rechaza  | inválida     |
| `10111`     |    5     | rechaza  | rechaza  | inválida     |
| `01100111`  |    8     | rechaza  | rechaza  | inválida     |

Cadenas de prueba.

## Lista 2 · Ejercicio 148

**Enunciado.** AFD del progreso de un alumno en Teoría de la Computación (convocatorias de febrero, septiembre y diciembre; Σ = {P, N, A, S}; no más de dos presentaciones por año; termina al aprobar).

**Clase.** AFD: Cada par (estado, símbolo) tiene a lo sumo un destino y no hay transiciones λ. **Archivos.** `automatas/afd/lista2-148.jff` (y `.json`, `.xml`).

**Diseño.** Interpretación: en cada convocatoria el alumno no se presenta (N) o se presenta (P) y después aprueba (A) o suspende (S). Se cuentan las presentaciones del año; con dos, en la convocatoria restante sólo cabe N. Después de diciembre empieza un año nuevo con el contador en cero. APROBADO es el único estado de aceptación y cualquier símbolo posterior lleva a muerto.

| δ           | A        | N      | P      | S      | Qué recuerda del prefijo leído                                                            |
|-------------|----------|--------|--------|--------|-------------------------------------------------------------------------------------------|
| → feb0      | muerto   | sep0   | feb0?  | muerto | convocatoria de feb, 0 presentaciones usadas en el año; decide si se presenta             |
| muerto      | muerto   | muerto | muerto | muerto | secuencia inválida                                                                        |
| sep0        | muerto   | dic0   | sep0?  | muerto | convocatoria de sep, 0 presentaciones usadas en el año; decide si se presenta             |
| feb0?       | APROBADO | muerto | muerto | sep1   | convocatoria de feb, 0 presentaciones usadas en el año; se presentó y espera el resultado |
| dic0        | muerto   | feb0   | dic0?  | muerto | convocatoria de dic, 0 presentaciones usadas en el año; decide si se presenta             |
| sep0?       | APROBADO | muerto | muerto | dic1   | convocatoria de sep, 0 presentaciones usadas en el año; se presentó y espera el resultado |
| \* APROBADO | muerto   | muerto | muerto | muerto | aprobó el curso                                                                           |
| sep1        | muerto   | dic1   | sep1?  | muerto | convocatoria de sep, 1 presentaciones usadas en el año; decide si se presenta             |
| dic0?       | APROBADO | muerto | muerto | feb0   | convocatoria de dic, 0 presentaciones usadas en el año; se presentó y espera el resultado |
| dic1        | muerto   | feb0   | dic1?  | muerto | convocatoria de dic, 1 presentaciones usadas en el año; decide si se presenta             |
| sep1?       | APROBADO | muerto | muerto | dic2   | convocatoria de sep, 1 presentaciones usadas en el año; se presentó y espera el resultado |
| dic1?       | APROBADO | muerto | muerto | feb0   | convocatoria de dic, 1 presentaciones usadas en el año; se presentó y espera el resultado |
| dic2        | muerto   | feb0   | muerto | muerto | convocatoria de dic, 2 presentaciones usadas en el año; decide si se presenta             |

Tabla de transiciones (→ inicial, \* aceptación, — sin transición).

| Cadena       | Longitud | Esperado | Obtenido | Tipo de caso                                     |
|--------------|:--------:|----------|----------|--------------------------------------------------|
| `PA`         |    2     | acepta   | acepta   | válida                                           |
| `NPA`        |    3     | acepta   | acepta   | válida                                           |
| `NPSPA`      |    5     | acepta   | acepta   | válida                                           |
| `NPSPSPA`    |    7     | acepta   | acepta   | válida                                           |
| `NPSNPSNNPA` |    10    | acepta   | acepta   | válida                                           |
| λ            |    0     | rechaza  | rechaza  | inválida                                         |
| `N`          |    1     | rechaza  | rechaza  | inválida                                         |
| `PAS`        |    3     | rechaza  | rechaza  | inválida                                         |
| `NAPAS`      |    5     | rechaza  | rechaza  | inválida                                         |
| `NNNPASAA`   |    8     | rechaza  | rechaza  | inválida                                         |
| `P`          |    1     | rechaza  | rechaza  | frontera: justo por debajo de la longitud mínima |

Cadenas de prueba.

## Lista 2 · Ejercicio 149

**Enunciado.** AFD de la tabla (→A, C final). Halle δ(B, 0), δ(C, 1), δ̂(A, 1101), δ̂(A, 01001).

**Clase.** AFD: Cada par (estado, símbolo) tiene a lo sumo un destino y no hay transiciones λ. **Archivos.** `automatas/afd/lista2-149.jff` (y `.json`, `.xml`).

**Diseño.** Q = {A, B, C}, Σ = {0, 1}, A0 = A, F = {C}.

| δ    | 0   | 1   |
|------|-----|-----|
| → A  | B   | C   |
| B    | A   | C   |
| \* C | C   | A   |

Tabla de transiciones (→ inicial, \* aceptación, — sin transición).

| Cadena      | Longitud | Esperado | Obtenido | Tipo de caso |
|-------------|:--------:|----------|----------|--------------|
| `1`         |    1     | acepta   | acepta   | válida       |
| `10`        |    2     | acepta   | acepta   | válida       |
| `1110`      |    4     | acepta   | acepta   | válida       |
| `111110`    |    6     | acepta   | acepta   | válida       |
| `110001000` |    9     | acepta   | acepta   | válida       |
| λ           |    0     | rechaza  | rechaza  | inválida     |
| `0`         |    1     | rechaza  | rechaza  | inválida     |
| `011`       |    3     | rechaza  | rechaza  | inválida     |
| `10010`     |    5     | rechaza  | rechaza  | inválida     |
| `00110000`  |    8     | rechaza  | rechaza  | inválida     |

Cadenas de prueba.

## Lista 2 · Ejercicio 150

**Enunciado.** AFD de la tabla (→A; B, C, D finales). Halle δ̂(B, 10a11), δ̂(B, aa1100), δ̂(A, a01a01), δ̂(C, a11a00).

**Clase.** AFD: Cada par (estado, símbolo) tiene a lo sumo un destino y no hay transiciones λ. **Archivos.** `automatas/afd/lista2-150.jff` (y `.json`, `.xml`).

**Diseño.** Q = {A, B, C, D}, Σ = {0, 1, a}, A0 = A, F = {B, C, D}.

| δ    | 0   | 1   | a   |
|------|-----|-----|-----|
| → A  | B   | C   | D   |
| \* B | B   | C   | C   |
| \* C | A   | A   | D   |
| \* D | B   | B   | B   |

Tabla de transiciones (→ inicial, \* aceptación, — sin transición).

| Cadena         | Longitud | Esperado | Obtenido | Tipo de caso |
|----------------|:--------:|----------|----------|--------------|
| `1`            |    1     | acepta   | acepta   | válida       |
| `aa`           |    2     | acepta   | acepta   | válida       |
| `1a01`         |    4     | acepta   | acepta   | válida       |
| `1a001a`       |    6     | acepta   | acepta   | válida       |
| `0a01a1001`    |    9     | acepta   | acepta   | válida       |
| λ              |    0     | rechaza  | rechaza  | inválida     |
| `01011`        |    5     | rechaza  | rechaza  | inválida     |
| `0aa10a0`      |    7     | rechaza  | rechaza  | inválida     |
| `001a01011`    |    9     | rechaza  | rechaza  | inválida     |
| `0a001a0100a0` |    12    | rechaza  | rechaza  | inválida     |

Cadenas de prueba.

## Lista 3 · Ejercicio 151

**Enunciado.** Diagrama y simplificación del AFD de la tabla 151.

**Clase.** AFD: Cada par (estado, símbolo) tiene a lo sumo un destino y no hay transiciones λ. **Archivos.** `automatas/afd/lista3-151.jff` (y `.json`, `.xml`).

**Diseño.** Primero se eliminan los estados que no se alcanzan desde el inicial; después se refina la partición {F, Q − F} hasta que se estabiliza.

| δ    | 0   | 1   |
|------|-----|-----|
| → A  | C   | E   |
| B    | F   | E   |
| \* C | A   | G   |
| D    | C   | E   |
| \* E | I   | B   |
| \* F | D   | H   |
| G    | F   | I   |
| H    | C   | J   |
| I    | J   | E   |
| J    | I   | E   |

Tabla de transiciones (→ inicial, \* aceptación, — sin transición).

| Cadena           | Longitud | Esperado | Obtenido | Tipo de caso |
|------------------|:--------:|----------|----------|--------------|
| `1`              |    1     | acepta   | acepta   | válida       |
| `0111`           |    4     | acepta   | acepta   | válida       |
| `1001`           |    4     | acepta   | acepta   | válida       |
| `0100111`        |    7     | acepta   | acepta   | válida       |
| `0010111011001`  |    13    | acepta   | acepta   | válida       |
| λ                |    0     | rechaza  | rechaza  | inválida     |
| `001001000`      |    9     | rechaza  | rechaza  | inválida     |
| `100100000`      |    9     | rechaza  | rechaza  | inválida     |
| `1101000000`     |    10    | rechaza  | rechaza  | inválida     |
| `01000100000101` |    14    | rechaza  | rechaza  | inválida     |

Cadenas de prueba.

## Lista 3 · Ejercicio 152

**Enunciado.** Diagrama y simplificación del AFD de la tabla 152.

**Clase.** AFD: Cada par (estado, símbolo) tiene a lo sumo un destino y no hay transiciones λ. **Archivos.** `automatas/afd/lista3-152.jff` (y `.json`, `.xml`).

**Diseño.** Primero se eliminan los estados que no se alcanzan desde el inicial; después se refina la partición {F, Q − F} hasta que se estabiliza.

| δ    | 0   | 1   | 2   |
|------|-----|-----|-----|
| → A  | C   | E   | B   |
| B    | D   | E   | B   |
| C    | A   | D   | F   |
| \* D | F   | B   | C   |
| \* E | F   | B   | A   |
| \* F | D   | B   | C   |

Tabla de transiciones (→ inicial, \* aceptación, — sin transición).

| Cadena      | Longitud | Esperado | Obtenido | Tipo de caso |
|-------------|:--------:|----------|----------|--------------|
| `1`         |    1     | acepta   | acepta   | válida       |
| `02`        |    2     | acepta   | acepta   | válida       |
| `2021`      |    4     | acepta   | acepta   | válida       |
| `210201`    |    6     | acepta   | acepta   | válida       |
| `000111100` |    9     | acepta   | acepta   | válida       |
| λ           |    0     | rechaza  | rechaza  | inválida     |
| `0`         |    1     | rechaza  | rechaza  | inválida     |
| `211`       |    3     | rechaza  | rechaza  | inválida     |
| `02002`     |    5     | rechaza  | rechaza  | inválida     |
| `12111020`  |    8     | rechaza  | rechaza  | inválida     |

Cadenas de prueba.

## Lista 3 · Ejercicio 153

**Enunciado.** Diagrama y simplificación del AFD de la tabla 153.

**Clase.** AFD: Cada par (estado, símbolo) tiene a lo sumo un destino y no hay transiciones λ. **Archivos.** `automatas/afd/lista3-153.jff` (y `.json`, `.xml`).

**Diseño.** Primero se eliminan los estados que no se alcanzan desde el inicial; después se refina la partición {F, Q − F} hasta que se estabiliza.

| δ    | 0   | 1   |
|------|-----|-----|
| → A  | B   | C   |
| B    | D   | E   |
| C    | F   | G   |
| \* D | D   | E   |
| E    | F   | G   |
| \* F | E   | D   |
| \* G | F   | G   |

Tabla de transiciones (→ inicial, \* aceptación, — sin transición).

| Cadena       | Longitud | Esperado | Obtenido | Tipo de caso                                     |
|--------------|:--------:|----------|----------|--------------------------------------------------|
| `10`         |    2     | acepta   | acepta   | válida                                           |
| `101`        |    3     | acepta   | acepta   | válida                                           |
| `01101`      |    5     | acepta   | acepta   | válida                                           |
| `0011000`    |    7     | acepta   | acepta   | válida                                           |
| `1000000010` |    10    | acepta   | acepta   | válida                                           |
| λ            |    0     | rechaza  | rechaza  | inválida                                         |
| `1`          |    1     | rechaza  | rechaza  | inválida                                         |
| `100`        |    3     | rechaza  | rechaza  | inválida                                         |
| `10101`      |    5     | rechaza  | rechaza  | inválida                                         |
| `00101001`   |    8     | rechaza  | rechaza  | inválida                                         |
| `0`          |    1     | rechaza  | rechaza  | frontera: justo por debajo de la longitud mínima |

Cadenas de prueba.

## Lista 3 · Ejercicio 154

**Enunciado.** Diagrama y simplificación del AFD de la tabla 154.

**Clase.** AFD: Cada par (estado, símbolo) tiene a lo sumo un destino y no hay transiciones λ. **Archivos.** `automatas/afd/lista3-154.jff` (y `.json`, `.xml`).

**Diseño.** Primero se eliminan los estados que no se alcanzan desde el inicial; después se refina la partición {F, Q − F} hasta que se estabiliza.

| δ    | 0   | 1   |
|------|-----|-----|
| → A  | D   | K   |
| B    | H   | K   |
| C    | I   | E   |
| D    | C   | G   |
| \* E | K   | I   |
| F    | B   | E   |
| \* G | C   | I   |
| \* H | C   | B   |
| I    | G   | K   |
| \* J | F   | B   |
| K    | C   | F   |

Tabla de transiciones (→ inicial, \* aceptación, — sin transición).

| Cadena       | Longitud | Esperado | Obtenido | Tipo de caso |
|--------------|:--------:|----------|----------|--------------|
| `01`         |    2     | acepta   | acepta   | válida       |
| `001`        |    3     | acepta   | acepta   | válida       |
| `10110`      |    5     | acepta   | acepta   | válida       |
| `1111001`    |    7     | acepta   | acepta   | válida       |
| `1001000000` |    10    | acepta   | acepta   | válida       |
| λ            |    0     | rechaza  | rechaza  | inválida     |
| `1`          |    1     | rechaza  | rechaza  | inválida     |
| `100`        |    3     | rechaza  | rechaza  | inválida     |
| `00010`      |    5     | rechaza  | rechaza  | inválida     |
| `00111110`   |    8     | rechaza  | rechaza  | inválida     |

Cadenas de prueba.

## Lista 3 · Ejercicio 155

**Enunciado.** Diagrama y simplificación del AFD de la tabla 155.

**Clase.** AFD: Cada par (estado, símbolo) tiene a lo sumo un destino y no hay transiciones λ. **Archivos.** `automatas/afd/lista3-155.jff` (y `.json`, `.xml`).

**Diseño.** Primero se eliminan los estados que no se alcanzan desde el inicial; después se refina la partición {F, Q − F} hasta que se estabiliza.

| δ    | 0   | 1   |
|------|-----|-----|
| → A  | B   | C   |
| B    | D   | E   |
| C    | K   | G   |
| D    | H   | E   |
| E    | F   | D   |
| \* F | J   | G   |
| G    | E   | G   |
| H    | B   | K   |
| I    | C   | A   |
| J    | D   | G   |
| K    | F   | D   |
| L    | C   | J   |

Tabla de transiciones (→ inicial, \* aceptación, — sin transición).

| Cadena        | Longitud | Esperado | Obtenido | Tipo de caso                                     |
|---------------|:--------:|----------|----------|--------------------------------------------------|
| `010`         |    3     | acepta   | acepta   | válida                                           |
| `1100`        |    4     | acepta   | acepta   | válida                                           |
| `101010`      |    6     | acepta   | acepta   | válida                                           |
| `01101110`    |    8     | acepta   | acepta   | válida                                           |
| `01101101110` |    11    | acepta   | acepta   | válida                                           |
| λ             |    0     | rechaza  | rechaza  | inválida                                         |
| `0`           |    1     | rechaza  | rechaza  | inválida                                         |
| `110`         |    3     | rechaza  | rechaza  | inválida                                         |
| `01011`       |    5     | rechaza  | rechaza  | inválida                                         |
| `11011100`    |    8     | rechaza  | rechaza  | inválida                                         |
| `01`          |    2     | rechaza  | rechaza  | frontera: justo por debajo de la longitud mínima |

Cadenas de prueba.

## Lista 3 · Ejercicio 156

**Enunciado.** Diagrama y simplificación del AFD de la tabla 156 (tabla transcrita del diagrama).

**Clase.** AFD: Cada par (estado, símbolo) tiene a lo sumo un destino y no hay transiciones λ. **Archivos.** `automatas/afd/lista3-156.jff` (y `.json`, `.xml`).

**Diseño.** Primero se eliminan los estados que no se alcanzan desde el inicial; después se refina la partición {F, Q − F} hasta que se estabiliza.

| δ    | 0   | 1   |
|------|-----|-----|
| → A  | B   | C   |
| B    | C   | E   |
| C    | D   | C   |
| D    | C   | E   |
| \* E | B   | E   |

Tabla de transiciones (→ inicial, \* aceptación, — sin transición).

| Cadena       | Longitud | Esperado | Obtenido | Tipo de caso |
|--------------|:--------:|----------|----------|--------------|
| `01`         |    2     | acepta   | acepta   | válida       |
| `011`        |    3     | acepta   | acepta   | válida       |
| `10001`      |    5     | acepta   | acepta   | válida       |
| `1100011`    |    7     | acepta   | acepta   | válida       |
| `1100000001` |    10    | acepta   | acepta   | válida       |
| λ            |    0     | rechaza  | rechaza  | inválida     |
| `1`          |    1     | rechaza  | rechaza  | inválida     |
| `010`        |    3     | rechaza  | rechaza  | inválida     |
| `10000`      |    5     | rechaza  | rechaza  | inválida     |
| `10000001`   |    8     | rechaza  | rechaza  | inválida     |

Cadenas de prueba.

## Lista 3 · Ejercicio 157

**Enunciado.** Diagrama y simplificación del AFD de la tabla 157 (tabla transcrita del diagrama).

**Clase.** AFD: Cada par (estado, símbolo) tiene a lo sumo un destino y no hay transiciones λ. **Archivos.** `automatas/afd/lista3-157.jff` (y `.json`, `.xml`).

**Diseño.** Primero se eliminan los estados que no se alcanzan desde el inicial; después se refina la partición {F, Q − F} hasta que se estabiliza.

| δ    | 0   | 1   |
|------|-----|-----|
| → A  | B   | F   |
| B    | C   | E   |
| C    | D   | E   |
| D    | B   | E   |
| E    | F   | D   |
| \* F | F   | B   |

Tabla de transiciones (→ inicial, \* aceptación, — sin transición).

| Cadena      | Longitud | Esperado | Obtenido | Tipo de caso |
|-------------|:--------:|----------|----------|--------------|
| `1`         |    1     | acepta   | acepta   | válida       |
| `10`        |    2     | acepta   | acepta   | válida       |
| `0100`      |    4     | acepta   | acepta   | válida       |
| `100000`    |    6     | acepta   | acepta   | válida       |
| `111001010` |    9     | acepta   | acepta   | válida       |
| λ           |    0     | rechaza  | rechaza  | inválida     |
| `0`         |    1     | rechaza  | rechaza  | inválida     |
| `001`       |    3     | rechaza  | rechaza  | inválida     |
| `00111`     |    5     | rechaza  | rechaza  | inválida     |
| `01010110`  |    8     | rechaza  | rechaza  | inválida     |

Cadenas de prueba.

## Lista 3 · Ejercicio 158

**Enunciado.** Describa lo que hace el AFN del diagrama 158.

**Clase.** AFD: Cada par (estado, símbolo) tiene a lo sumo un destino y no hay transiciones λ. **Archivos.** `automatas/afd/lista3-158.jff` (y `.json`, `.xml`).

**Diseño.** El autómata acepta únicamente la cadena 01: L = {01}. Las transiciones que faltan llevan a un rechazo implícito.

| δ     | 0   | 1   |
|-------|-----|-----|
| → q1  | q2  | —   |
| q2    | —   | q3  |
| \* q3 | —   | —   |

Tabla de transiciones (→ inicial, \* aceptación, — sin transición).

| Cadena     | Longitud | Esperado | Obtenido | Tipo de caso |
|------------|:--------:|----------|----------|--------------|
| `01`       |    2     | acepta   | acepta   | válida       |
| λ          |    0     | rechaza  | rechaza  | inválida     |
| `1`        |    1     | rechaza  | rechaza  | inválida     |
| `111`      |    3     | rechaza  | rechaza  | inválida     |
| `00101`    |    5     | rechaza  | rechaza  | inválida     |
| `11110010` |    8     | rechaza  | rechaza  | inválida     |

Cadenas de prueba.

## Lista 3 · Ejercicio 159

**Enunciado.** Describa lo que hace el AFN del diagrama 159.

**Clase.** AFD: Cada par (estado, símbolo) tiene a lo sumo un destino y no hay transiciones λ. **Archivos.** `automatas/afd/lista3-159.jff` (y `.json`, `.xml`).

**Diseño.** El autómata acepta las cadenas formadas por unos seguidos de 01: L = 1\*01. Las transiciones que faltan llevan a un rechazo implícito.

| δ     | 0   | 1   |
|-------|-----|-----|
| → q1  | q2  | q1  |
| q2    | —   | q3  |
| \* q3 | —   | —   |

Tabla de transiciones (→ inicial, \* aceptación, — sin transición).

| Cadena       | Longitud | Esperado | Obtenido | Tipo de caso                                     |
|--------------|:--------:|----------|----------|--------------------------------------------------|
| `01`         |    2     | acepta   | acepta   | válida                                           |
| `101`        |    3     | acepta   | acepta   | válida                                           |
| `11101`      |    5     | acepta   | acepta   | válida                                           |
| `1111101`    |    7     | acepta   | acepta   | válida                                           |
| `1111111101` |    10    | acepta   | acepta   | válida                                           |
| λ            |    0     | rechaza  | rechaza  | inválida                                         |
| `0`          |    1     | rechaza  | rechaza  | inválida                                         |
| `001`        |    3     | rechaza  | rechaza  | inválida                                         |
| `01010`      |    5     | rechaza  | rechaza  | inválida                                         |
| `11101100`   |    8     | rechaza  | rechaza  | inválida                                         |
| `1`          |    1     | rechaza  | rechaza  | frontera: justo por debajo de la longitud mínima |

Cadenas de prueba.

## Lista 3 · Ejercicio 160

**Enunciado.** Describa lo que hace el AFN del diagrama 160.

**Clase.** AFD: Cada par (estado, símbolo) tiene a lo sumo un destino y no hay transiciones λ. **Archivos.** `automatas/afd/lista3-160.jff` (y `.json`, `.xml`).

**Diseño.** El autómata acepta las cadenas que empiezan con 01: L = 01(0 + 1)\*. Las transiciones que faltan llevan a un rechazo implícito.

| δ     | 0   | 1   |
|-------|-----|-----|
| → q1  | q2  | —   |
| q2    | —   | q3  |
| \* q3 | q3  | q3  |

Tabla de transiciones (→ inicial, \* aceptación, — sin transición).

| Cadena       | Longitud | Esperado | Obtenido | Tipo de caso |
|--------------|:--------:|----------|----------|--------------|
| `01`         |    2     | acepta   | acepta   | válida       |
| `011`        |    3     | acepta   | acepta   | válida       |
| `01100`      |    5     | acepta   | acepta   | válida       |
| `0110100`    |    7     | acepta   | acepta   | válida       |
| `0111101100` |    10    | acepta   | acepta   | válida       |
| λ            |    0     | rechaza  | rechaza  | inválida     |
| `1`          |    1     | rechaza  | rechaza  | inválida     |
| `101`        |    3     | rechaza  | rechaza  | inválida     |
| `00001`      |    5     | rechaza  | rechaza  | inválida     |
| `11101101`   |    8     | rechaza  | rechaza  | inválida     |

Cadenas de prueba.

## Lista 3 · Ejercicio 161

**Enunciado.** Describa lo que hace el AFN del diagrama 161.

**Clase.** AFD: Cada par (estado, símbolo) tiene a lo sumo un destino y no hay transiciones λ. **Archivos.** `automatas/afd/lista3-161.jff` (y `.json`, `.xml`).

**Diseño.** El autómata acepta las repeticiones del bloque 010, incluida λ: L = (010)\*. Las transiciones que faltan llevan a un rechazo implícito.

| δ      | 0   | 1   |
|--------|-----|-----|
| →\* q1 | q2  | —   |
| q2     | —   | q3  |
| q3     | q1  | —   |

Tabla de transiciones (→ inicial, \* aceptación, — sin transición).

| Cadena         | Longitud | Esperado | Obtenido | Tipo de caso |
|----------------|:--------:|----------|----------|--------------|
| λ              |    0     | acepta   | acepta   | válida       |
| `010`          |    3     | acepta   | acepta   | válida       |
| `010010`       |    6     | acepta   | acepta   | válida       |
| `010010010`    |    9     | acepta   | acepta   | válida       |
| `010010010010` |    12    | acepta   | acepta   | válida       |
| `0`            |    1     | rechaza  | rechaza  | inválida     |
| `01`           |    2     | rechaza  | rechaza  | inválida     |
| `0100`         |    4     | rechaza  | rechaza  | inválida     |
| `110101`       |    6     | rechaza  | rechaza  | inválida     |
| `000011110`    |    9     | rechaza  | rechaza  | inválida     |

Cadenas de prueba.

## Lista 3 · AFN del problema 094

**Enunciado.** AFN para el problema 94: Las palabras de Σ1 que comienzan con 1 y terminan con 2.

**Clase.** AFN: Hay elección: δ(q1, 2) = {q1, q2}. **Archivos.** `automatas/afnd/lista3-afn-094.jff` (y `.json`, `.xml`).

**Diseño.** Tras el 1 inicial, el AFN adivina cuándo lee el último símbolo, que debe ser 2.

| δ     | 0    | 1    | 2        |
|-------|------|------|----------|
| → q0  | ∅    | {q1} | ∅        |
| q1    | {q1} | {q1} | {q1, q2} |
| \* q2 | ∅    | ∅    | ∅        |

Tabla de transiciones (→ inicial, \* aceptación, — sin transición).

| Cadena       | Longitud | Esperado | Obtenido | Tipo de caso                                     |
|--------------|:--------:|----------|----------|--------------------------------------------------|
| `12`         |    2     | acepta   | acepta   | válida                                           |
| `102`        |    3     | acepta   | acepta   | válida                                           |
| `11012`      |    5     | acepta   | acepta   | válida                                           |
| `1022012`    |    7     | acepta   | acepta   | válida                                           |
| `1021101222` |    10    | acepta   | acepta   | válida                                           |
| λ            |    0     | rechaza  | rechaza  | inválida                                         |
| `2`          |    1     | rechaza  | rechaza  | inválida                                         |
| `212`        |    3     | rechaza  | rechaza  | inválida                                         |
| `00012`      |    5     | rechaza  | rechaza  | inválida                                         |
| `20021021`   |    8     | rechaza  | rechaza  | inválida                                         |
| `0`          |    1     | rechaza  | rechaza  | frontera: justo por debajo de la longitud mínima |

Cadenas de prueba.

## Lista 3 · AFN del problema 095

**Enunciado.** AFN para el problema 95: Las palabras de Σ1 que tienen longitud 4.

**Clase.** AFD: Cada par (estado, símbolo) tiene a lo sumo un destino y no hay transiciones λ. **Archivos.** `automatas/afd/lista3-afn-095.jff` (y `.json`, `.xml`).

**Diseño.** No hay una versión no determinista más simple: el lenguaje depende de contar (longitud, apariciones o fases). Se presenta el AFD del problema sin el estado muerto; una función de transición parcial es un caso particular de AFN.

| δ     | 0   | 1   | 2   |
|-------|-----|-----|-----|
| → L0  | L1  | L1  | L1  |
| L1    | L2  | L2  | L2  |
| L2    | L3  | L3  | L3  |
| L3    | L4  | L4  | L4  |
| \* L4 | —   | —   | —   |

Tabla de transiciones (→ inicial, \* aceptación, — sin transición).

| Cadena     | Longitud | Esperado | Obtenido | Tipo de caso                                     |
|------------|:--------:|----------|----------|--------------------------------------------------|
| `0100`     |    4     | acepta   | acepta   | válida                                           |
| `1102`     |    4     | acepta   | acepta   | válida                                           |
| `1111`     |    4     | acepta   | acepta   | válida                                           |
| `1112`     |    4     | acepta   | acepta   | válida                                           |
| `2122`     |    4     | acepta   | acepta   | válida                                           |
| λ          |    0     | rechaza  | rechaza  | inválida                                         |
| `0`        |    1     | rechaza  | rechaza  | inválida                                         |
| `221`      |    3     | rechaza  | rechaza  | inválida                                         |
| `02020`    |    5     | rechaza  | rechaza  | inválida                                         |
| `01010112` |    8     | rechaza  | rechaza  | inválida                                         |
| `1200`     |    4     | acepta   | acepta   | frontera: aceptada más corta                     |
| `100`      |    3     | rechaza  | rechaza  | frontera: justo por debajo de la longitud mínima |

Cadenas de prueba.

## Lista 3 · AFN del problema 096

**Enunciado.** AFN para el problema 96: Las palabras de Σ1 con prefijo 20 y longitud 4.

**Clase.** AFD: Cada par (estado, símbolo) tiene a lo sumo un destino y no hay transiciones λ. **Archivos.** `automatas/afd/lista3-afn-096.jff` (y `.json`, `.xml`).

**Diseño.** No hay una versión no determinista más simple: el lenguaje depende de contar (longitud, apariciones o fases). Se presenta el AFD del problema sin el estado muerto; una función de transición parcial es un caso particular de AFN.

| δ     | 0   | 1   | 2   |
|-------|-----|-----|-----|
| → L0  | —   | —   | L1  |
| L1    | L2  | —   | —   |
| L2    | L3  | L3  | L3  |
| L3    | L4  | L4  | L4  |
| \* L4 | —   | —   | —   |

Tabla de transiciones (→ inicial, \* aceptación, — sin transición).

| Cadena     | Longitud | Esperado | Obtenido | Tipo de caso                                     |
|------------|:--------:|----------|----------|--------------------------------------------------|
| `2001`     |    4     | acepta   | acepta   | válida                                           |
| `2010`     |    4     | acepta   | acepta   | válida                                           |
| `2011`     |    4     | acepta   | acepta   | válida                                           |
| `2020`     |    4     | acepta   | acepta   | válida                                           |
| `2022`     |    4     | acepta   | acepta   | válida                                           |
| λ          |    0     | rechaza  | rechaza  | inválida                                         |
| `1`        |    1     | rechaza  | rechaza  | inválida                                         |
| `220`      |    3     | rechaza  | rechaza  | inválida                                         |
| `02000`    |    5     | rechaza  | rechaza  | inválida                                         |
| `11121222` |    8     | rechaza  | rechaza  | inválida                                         |
| `2021`     |    4     | acepta   | acepta   | frontera: aceptada más corta                     |
| `121`      |    3     | rechaza  | rechaza  | frontera: justo por debajo de la longitud mínima |

Cadenas de prueba.

## Lista 3 · AFN del problema 097

**Enunciado.** AFN para el problema 97: Las palabras de Σ1 cuya longitud es un múltiplo de 3.

**Clase.** AFD: Cada par (estado, símbolo) tiene a lo sumo un destino y no hay transiciones λ. **Archivos.** `automatas/afd/lista3-afn-097.jff` (y `.json`, `.xml`).

**Diseño.** No hay una versión no determinista más simple: el lenguaje depende de contar (longitud, apariciones o fases). Se presenta el AFD del problema sin el estado muerto; una función de transición parcial es un caso particular de AFN.

| δ      | 0   | 1   | 2   |
|--------|-----|-----|-----|
| →\* r0 | r1  | r1  | r1  |
| r1     | r2  | r2  | r2  |
| r2     | r0  | r0  | r0  |

Tabla de transiciones (→ inicial, \* aceptación, — sin transición).

| Cadena      | Longitud | Esperado | Obtenido | Tipo de caso |
|-------------|:--------:|----------|----------|--------------|
| λ           |    0     | acepta   | acepta   | válida       |
| `120`       |    3     | acepta   | acepta   | válida       |
| `200`       |    3     | acepta   | acepta   | válida       |
| `100020`    |    6     | acepta   | acepta   | válida       |
| `121121201` |    9     | acepta   | acepta   | válida       |
| `1`         |    1     | rechaza  | rechaza  | inválida     |
| `21`        |    2     | rechaza  | rechaza  | inválida     |
| `2102`      |    4     | rechaza  | rechaza  | inválida     |
| `01102021`  |    8     | rechaza  | rechaza  | inválida     |
| `12220210`  |    8     | rechaza  | rechaza  | inválida     |

Cadenas de prueba.

## Lista 3 · AFN del problema 098

**Enunciado.** AFN para el problema 98: Las palabras de Σ1 que terminan con la cadena 00102.

**Clase.** AFN: Hay elección: δ(c0, 0) = {c0, c1}. **Archivos.** `automatas/afnd/lista3-afn-098.jff` (y `.json`, `.xml`).

**Diseño.** Ciclo en c0 y una cadena de estados que adivina dónde empieza el sufijo 00102.

| δ     | 0        | 1    | 2    |
|-------|----------|------|------|
| → c0  | {c0, c1} | {c0} | {c0} |
| c1    | {c2}     | ∅    | ∅    |
| c2    | ∅        | {c3} | ∅    |
| c3    | {c4}     | ∅    | ∅    |
| c4    | ∅        | ∅    | {c5} |
| \* c5 | ∅        | ∅    | ∅    |

Tabla de transiciones (→ inicial, \* aceptación, — sin transición).

| Cadena          | Longitud | Esperado | Obtenido | Tipo de caso                                     |
|-----------------|:--------:|----------|----------|--------------------------------------------------|
| `00102`         |    5     | acepta   | acepta   | válida                                           |
| `100102`        |    6     | acepta   | acepta   | válida                                           |
| `20000102`      |    8     | acepta   | acepta   | válida                                           |
| `2100200102`    |    10    | acepta   | acepta   | válida                                           |
| `0221101000102` |    13    | acepta   | acepta   | válida                                           |
| λ               |    0     | rechaza  | rechaza  | inválida                                         |
| `2`             |    1     | rechaza  | rechaza  | inválida                                         |
| `122`           |    3     | rechaza  | rechaza  | inválida                                         |
| `11100`         |    5     | rechaza  | rechaza  | inválida                                         |
| `22220002`      |    8     | rechaza  | rechaza  | inválida                                         |
| `0222`          |    4     | rechaza  | rechaza  | frontera: justo por debajo de la longitud mínima |

Cadenas de prueba.

## Lista 3 · AFN del problema 099

**Enunciado.** AFN para el problema 99: Las palabras de Σ1 que terminan con la cadena 001001.

**Clase.** AFN: Hay elección: δ(c0, 0) = {c0, c1}. **Archivos.** `automatas/afnd/lista3-afn-099.jff` (y `.json`, `.xml`).

**Diseño.** Ciclo en c0 y una cadena que adivina dónde empieza el sufijo 001001.

| δ     | 0        | 1    | 2    |
|-------|----------|------|------|
| → c0  | {c0, c1} | {c0} | {c0} |
| c1    | {c2}     | ∅    | ∅    |
| c2    | ∅        | {c3} | ∅    |
| c3    | {c4}     | ∅    | ∅    |
| c4    | {c5}     | ∅    | ∅    |
| c5    | ∅        | {c6} | ∅    |
| \* c6 | ∅        | ∅    | ∅    |

Tabla de transiciones (→ inicial, \* aceptación, — sin transición).

| Cadena           | Longitud | Esperado | Obtenido | Tipo de caso                                     |
|------------------|:--------:|----------|----------|--------------------------------------------------|
| `001001`         |    6     | acepta   | acepta   | válida                                           |
| `1001001`        |    7     | acepta   | acepta   | válida                                           |
| `121001001`      |    9     | acepta   | acepta   | válida                                           |
| `10211001001`    |    11    | acepta   | acepta   | válida                                           |
| `00200202001001` |    14    | acepta   | acepta   | válida                                           |
| λ                |    0     | rechaza  | rechaza  | inválida                                         |
| `2`              |    1     | rechaza  | rechaza  | inválida                                         |
| `120`            |    3     | rechaza  | rechaza  | inválida                                         |
| `22202`          |    5     | rechaza  | rechaza  | inválida                                         |
| `02211011`       |    8     | rechaza  | rechaza  | inválida                                         |
| `02210`          |    5     | rechaza  | rechaza  | frontera: justo por debajo de la longitud mínima |

Cadenas de prueba.

## Lista 3 · AFN del problema 100

**Enunciado.** AFN para el problema 100: Las palabras de Σ2 tales que el primer símbolo es una letra y el segundo es un dígito.

**Clase.** AFD: Cada par (estado, símbolo) tiene a lo sumo un destino y no hay transiciones λ. **Archivos.** `automatas/afd/lista3-afn-100.jff` (y `.json`, `.xml`).

**Diseño.** Letra, dígito y cualquier continuación; sin estado muerto.

| δ     | 0   | 1   | a   | b   | c   |
|-------|-----|-----|-----|-----|-----|
| → q0  | —   | —   | q1  | q1  | q1  |
| q1    | q2  | q2  | —   | —   | —   |
| \* q2 | q2  | q2  | q2  | q2  | q2  |

Tabla de transiciones (→ inicial, \* aceptación, — sin transición).

| Cadena       | Longitud | Esperado | Obtenido | Tipo de caso                 |
|--------------|:--------:|----------|----------|------------------------------|
| `c1`         |    2     | acepta   | acepta   | válida                       |
| `b01`        |    3     | acepta   | acepta   | válida                       |
| `b0a0a`      |    5     | acepta   | acepta   | válida                       |
| `c0ba100`    |    7     | acepta   | acepta   | válida                       |
| `b1cca1a1ac` |    10    | acepta   | acepta   | válida                       |
| λ            |    0     | rechaza  | rechaza  | inválida                     |
| `0`          |    1     | rechaza  | rechaza  | inválida                     |
| `bcb`        |    3     | rechaza  | rechaza  | inválida                     |
| `0a0b0`      |    5     | rechaza  | rechaza  | inválida                     |
| `caab1cab`   |    8     | rechaza  | rechaza  | inválida                     |
| `b0`         |    2     | acepta   | acepta   | frontera: aceptada más corta |

Cadenas de prueba.

## Lista 3 · AFN del problema 101

**Enunciado.** AFN para el problema 101: Las palabras de Σ3 que contienen la cadena aba.

**Clase.** AFN: Hay elección: δ(c0, a) = {c0, c1}. **Archivos.** `automatas/afnd/lista3-afn-101.jff` (y `.json`, `.xml`).

**Diseño.** El AFN adivina dónde empieza aba: ciclo inicial, el patrón y ciclo final. No necesita los retrocesos del autómata de Knuth-Morris-Pratt.

| δ     | a        | b    |
|-------|----------|------|
| → c0  | {c0, c1} | {c0} |
| c1    | ∅        | {c2} |
| c2    | {c3}     | ∅    |
| \* c3 | {c3}     | {c3} |

Tabla de transiciones (→ inicial, \* aceptación, — sin transición).

| Cadena        | Longitud | Esperado | Obtenido | Tipo de caso                                     |
|---------------|:--------:|----------|----------|--------------------------------------------------|
| `aba`         |    3     | acepta   | acepta   | válida                                           |
| `abab`        |    4     | acepta   | acepta   | válida                                           |
| `abaaab`      |    6     | acepta   | acepta   | válida                                           |
| `abbbabab`    |    8     | acepta   | acepta   | válida                                           |
| `baababbbaba` |    11    | acepta   | acepta   | válida                                           |
| λ             |    0     | rechaza  | rechaza  | inválida                                         |
| `b`           |    1     | rechaza  | rechaza  | inválida                                         |
| `aaa`         |    3     | rechaza  | rechaza  | inválida                                         |
| `babba`       |    5     | rechaza  | rechaza  | inválida                                         |
| `aaaaabbb`    |    8     | rechaza  | rechaza  | inválida                                         |
| `bb`          |    2     | rechaza  | rechaza  | frontera: justo por debajo de la longitud mínima |

Cadenas de prueba.

## Lista 3 · AFN del problema 102

**Enunciado.** AFN para el problema 102: Las palabras de Σ3 que contienen la cadena abbbab.

**Clase.** AFN: Hay elección: δ(c0, a) = {c0, c1}. **Archivos.** `automatas/afnd/lista3-afn-102.jff` (y `.json`, `.xml`).

**Diseño.** El AFN adivina dónde empieza abbbab: ciclo inicial, el patrón y ciclo final. No necesita los retrocesos del autómata de Knuth-Morris-Pratt.

| δ     | a        | b    |
|-------|----------|------|
| → c0  | {c0, c1} | {c0} |
| c1    | ∅        | {c2} |
| c2    | ∅        | {c3} |
| c3    | ∅        | {c4} |
| c4    | {c5}     | ∅    |
| c5    | ∅        | {c6} |
| \* c6 | {c6}     | {c6} |

Tabla de transiciones (→ inicial, \* aceptación, — sin transición).

| Cadena           | Longitud | Esperado | Obtenido | Tipo de caso                                     |
|------------------|:--------:|----------|----------|--------------------------------------------------|
| `abbbab`         |    6     | acepta   | acepta   | válida                                           |
| `abbbabb`        |    7     | acepta   | acepta   | válida                                           |
| `abbbabaaa`      |    9     | acepta   | acepta   | válida                                           |
| `abbaabbbaba`    |    11    | acepta   | acepta   | válida                                           |
| `bbbabbbabbbbaa` |    14    | acepta   | acepta   | válida                                           |
| λ                |    0     | rechaza  | rechaza  | inválida                                         |
| `a`              |    1     | rechaza  | rechaza  | inválida                                         |
| `baa`            |    3     | rechaza  | rechaza  | inválida                                         |
| `bbbaa`          |    5     | rechaza  | rechaza  | inválida                                         |
| `bbbbbaba`       |    8     | rechaza  | rechaza  | inválida                                         |
| `aabab`          |    5     | rechaza  | rechaza  | frontera: justo por debajo de la longitud mínima |

Cadenas de prueba.

## Lista 3 · AFN del problema 103

**Enunciado.** AFN para el problema 103: Las palabras de Σ3 que contienen la cadena aabbba.

**Clase.** AFN: Hay elección: δ(c0, a) = {c0, c1}. **Archivos.** `automatas/afnd/lista3-afn-103.jff` (y `.json`, `.xml`).

**Diseño.** El AFN adivina dónde empieza aabbba: ciclo inicial, el patrón y ciclo final. No necesita los retrocesos del autómata de Knuth-Morris-Pratt.

| δ     | a        | b    |
|-------|----------|------|
| → c0  | {c0, c1} | {c0} |
| c1    | {c2}     | ∅    |
| c2    | ∅        | {c3} |
| c3    | ∅        | {c4} |
| c4    | ∅        | {c5} |
| c5    | {c6}     | ∅    |
| \* c6 | {c6}     | {c6} |

Tabla de transiciones (→ inicial, \* aceptación, — sin transición).

| Cadena           | Longitud | Esperado | Obtenido | Tipo de caso                                     |
|------------------|:--------:|----------|----------|--------------------------------------------------|
| `aabbba`         |    6     | acepta   | acepta   | válida                                           |
| `baabbba`        |    7     | acepta   | acepta   | válida                                           |
| `babaabbba`      |    9     | acepta   | acepta   | válida                                           |
| `ababaabbbaa`    |    11    | acepta   | acepta   | válida                                           |
| `aaabbbaaaaabbb` |    14    | acepta   | acepta   | válida                                           |
| λ                |    0     | rechaza  | rechaza  | inválida                                         |
| `a`              |    1     | rechaza  | rechaza  | inválida                                         |
| `aaa`            |    3     | rechaza  | rechaza  | inválida                                         |
| `bbabb`          |    5     | rechaza  | rechaza  | inválida                                         |
| `baabbaaa`       |    8     | rechaza  | rechaza  | inválida                                         |
| `ababb`          |    5     | rechaza  | rechaza  | frontera: justo por debajo de la longitud mínima |

Cadenas de prueba.

## Lista 3 · AFN del problema 104

**Enunciado.** AFN para el problema 104: Las palabras de Σ3 que inician con la cadena abbab.

**Clase.** AFD: Cada par (estado, símbolo) tiene a lo sumo un destino y no hay transiciones λ. **Archivos.** `automatas/afd/lista3-afn-104.jff` (y `.json`, `.xml`).

**Diseño.** El prefijo abbab y un ciclo final; sin estado muerto.

| δ     | a   | b   |
|-------|-----|-----|
| → c0  | c1  | —   |
| c1    | —   | c2  |
| c2    | —   | c3  |
| c3    | c4  | —   |
| c4    | —   | c5  |
| \* c5 | c5  | c5  |

Tabla de transiciones (→ inicial, \* aceptación, — sin transición).

| Cadena          | Longitud | Esperado | Obtenido | Tipo de caso                                     |
|-----------------|:--------:|----------|----------|--------------------------------------------------|
| `abbab`         |    5     | acepta   | acepta   | válida                                           |
| `abbaba`        |    6     | acepta   | acepta   | válida                                           |
| `abbabbba`      |    8     | acepta   | acepta   | válida                                           |
| `abbabbbabb`    |    10    | acepta   | acepta   | válida                                           |
| `abbabababaaaa` |    13    | acepta   | acepta   | válida                                           |
| λ               |    0     | rechaza  | rechaza  | inválida                                         |
| `b`             |    1     | rechaza  | rechaza  | inválida                                         |
| `bba`           |    3     | rechaza  | rechaza  | inválida                                         |
| `baabb`         |    5     | rechaza  | rechaza  | inválida                                         |
| `aabbbaba`      |    8     | rechaza  | rechaza  | inválida                                         |
| `abbb`          |    4     | rechaza  | rechaza  | frontera: justo por debajo de la longitud mínima |

Cadenas de prueba.

## Lista 3 · AFN del problema 105

**Enunciado.** AFN para el problema 105: Las palabras de Σ3 que terminan con la cadena abaa.

**Clase.** AFN: Hay elección: δ(c0, a) = {c0, c1}. **Archivos.** `automatas/afnd/lista3-afn-105.jff` (y `.json`, `.xml`).

**Diseño.** Ciclo inicial y el sufijo abaa.

| δ     | a        | b    |
|-------|----------|------|
| → c0  | {c0, c1} | {c0} |
| c1    | ∅        | {c2} |
| c2    | {c3}     | ∅    |
| c3    | {c4}     | ∅    |
| \* c4 | ∅        | ∅    |

Tabla de transiciones (→ inicial, \* aceptación, — sin transición).

| Cadena         | Longitud | Esperado | Obtenido | Tipo de caso                                     |
|----------------|:--------:|----------|----------|--------------------------------------------------|
| `abaa`         |    4     | acepta   | acepta   | válida                                           |
| `babaa`        |    5     | acepta   | acepta   | válida                                           |
| `bababaa`      |    7     | acepta   | acepta   | válida                                           |
| `aaabaabaa`    |    9     | acepta   | acepta   | válida                                           |
| `bababaababaa` |    12    | acepta   | acepta   | válida                                           |
| λ              |    0     | rechaza  | rechaza  | inválida                                         |
| `a`            |    1     | rechaza  | rechaza  | inválida                                         |
| `aaa`          |    3     | rechaza  | rechaza  | inválida                                         |
| `bbaab`        |    5     | rechaza  | rechaza  | inválida                                         |
| `bbbbaaba`     |    8     | rechaza  | rechaza  | inválida                                         |
| `aba`          |    3     | rechaza  | rechaza  | frontera: justo por debajo de la longitud mínima |

Cadenas de prueba.

## Lista 3 · AFN del problema 106

**Enunciado.** AFN para el problema 106: Las palabras de Σ1 que incluyen la subcadena 1101001.

**Clase.** AFN: Hay elección: δ(c0, 1) = {c0, c1}. **Archivos.** `automatas/afnd/lista3-afn-106.jff` (y `.json`, `.xml`).

**Diseño.** El AFN adivina dónde empieza 1101001: ciclo inicial, el patrón y ciclo final. No necesita los retrocesos del autómata de Knuth-Morris-Pratt.

| δ     | 0    | 1        | 2    |
|-------|------|----------|------|
| → c0  | {c0} | {c0, c1} | {c0} |
| c1    | ∅    | {c2}     | ∅    |
| c2    | {c3} | ∅        | ∅    |
| c3    | ∅    | {c4}     | ∅    |
| c4    | {c5} | ∅        | ∅    |
| c5    | {c6} | ∅        | ∅    |
| c6    | ∅    | {c7}     | ∅    |
| \* c7 | {c7} | {c7}     | {c7} |

Tabla de transiciones (→ inicial, \* aceptación, — sin transición).

| Cadena           | Longitud | Esperado | Obtenido | Tipo de caso                                     |
|------------------|:--------:|----------|----------|--------------------------------------------------|
| `1101001`        |    7     | acepta   | acepta   | válida                                           |
| `11010010`       |    8     | acepta   | acepta   | válida                                           |
| `1101001110`     |    10    | acepta   | acepta   | válida                                           |
| `212011010012`   |    12    | acepta   | acepta   | válida                                           |
| `20000110100120` |    14    | acepta   | acepta   | válida                                           |
| λ                |    0     | rechaza  | rechaza  | inválida                                         |
| `2`              |    1     | rechaza  | rechaza  | inválida                                         |
| `210`            |    3     | rechaza  | rechaza  | inválida                                         |
| `21220`          |    5     | rechaza  | rechaza  | inválida                                         |
| `22110022`       |    8     | rechaza  | rechaza  | inválida                                         |
| `221200`         |    6     | rechaza  | rechaza  | frontera: justo por debajo de la longitud mínima |

Cadenas de prueba.

## Lista 3 · AFN del problema 107

**Enunciado.** AFN para el problema 107: Las palabras de Σ1 que incluyen al menos una vez 0101 y al menos una vez 021.

**Clase.** AFN: Hay elección: δ(c0c0, 0) = {c0c0, c0c1, c1c0, c1c1}. **Archivos.** `automatas/afnd/lista3-afn-107.jff` (y `.json`, `.xml`).

**Diseño.** Intersección de los AFN de «contiene 0101» y «contiene 021» con la construcción de producto; cada estado es un par cᵢcⱼ. Como las dos apariciones pueden traslaparse, no basta con concatenar los patrones.

| δ       | 0                        | 1      | 2      |
|---------|--------------------------|--------|--------|
| → c0c0  | {c0c0, c0c1, c1c0, c1c1} | {c0c0} | {c0c0} |
| c0c1    | ∅                        | ∅      | {c0c2} |
| c1c0    | ∅                        | {c2c0} | ∅      |
| c1c1    | ∅                        | ∅      | ∅      |
| c0c2    | ∅                        | {c0c3} | ∅      |
| c2c0    | {c3c0, c3c1}             | ∅      | ∅      |
| c0c3    | {c0c3, c1c3}             | {c0c3} | {c0c3} |
| c3c0    | ∅                        | {c4c0} | ∅      |
| c3c1    | ∅                        | ∅      | ∅      |
| c1c3    | ∅                        | {c2c3} | ∅      |
| c4c0    | {c4c0, c4c1}             | {c4c0} | {c4c0} |
| c2c3    | {c3c3}                   | ∅      | ∅      |
| c4c1    | ∅                        | ∅      | {c4c2} |
| c3c3    | ∅                        | {c4c3} | ∅      |
| c4c2    | ∅                        | {c4c3} | ∅      |
| \* c4c3 | {c4c3}                   | {c4c3} | {c4c3} |

Tabla de transiciones (→ inicial, \* aceptación, — sin transición).

| Cadena           | Longitud | Esperado | Obtenido | Tipo de caso                                     |
|------------------|:--------:|----------|----------|--------------------------------------------------|
| `0101021`        |    7     | acepta   | acepta   | válida                                           |
| `20210101`       |    8     | acepta   | acepta   | válida                                           |
| `0212100101`     |    10    | acepta   | acepta   | válida                                           |
| `021112010101`   |    12    | acepta   | acepta   | válida                                           |
| `10202021010111` |    14    | acepta   | acepta   | válida                                           |
| λ                |    0     | rechaza  | rechaza  | inválida                                         |
| `0`              |    1     | rechaza  | rechaza  | inválida                                         |
| `201`            |    3     | rechaza  | rechaza  | inválida                                         |
| `21202`          |    5     | rechaza  | rechaza  | inválida                                         |
| `20001211`       |    8     | rechaza  | rechaza  | inválida                                         |
| `0210101`        |    7     | acepta   | acepta   | frontera: aceptada más corta                     |
| `101002`         |    6     | rechaza  | rechaza  | frontera: justo por debajo de la longitud mínima |

Cadenas de prueba.

## Lista 3 · AFN del problema 108

**Enunciado.** AFN para el problema 108: Las palabras de Σ2 que incluyen abbcb y cbaabb sin traslaparse (abbcbaabb no pertenece).

**Clase.** AFN: Hay elección: δ(i, a) = {i, x1}. **Archivos.** `automatas/afnd/lista3-afn-108.jff` (y `.json`, `.xml`).

**Diseño.** Dos ramas desde el estado inicial: abbcb y después cbaabb, o cbaabb y después abbcb. El segundo patrón empieza después de que el primero terminó, lo que impide el traslape.

| δ     | 0    | 1    | a        | b    | c        |
|-------|------|------|----------|------|----------|
| → i   | {i}  | {i}  | {i, x1}  | {i}  | {i, y1}  |
| x1    | ∅    | ∅    | ∅        | {x2} | ∅        |
| x2    | ∅    | ∅    | ∅        | {x3} | ∅        |
| x3    | ∅    | ∅    | ∅        | ∅    | {x4}     |
| x4    | ∅    | ∅    | ∅        | {x5} | ∅        |
| x5    | {x5} | {x5} | {x5}     | {x5} | {x5, Y1} |
| Y1    | ∅    | ∅    | ∅        | {Y2} | ∅        |
| Y2    | ∅    | ∅    | {Y3}     | ∅    | ∅        |
| Y3    | ∅    | ∅    | {Y4}     | ∅    | ∅        |
| Y4    | ∅    | ∅    | ∅        | {Y5} | ∅        |
| Y5    | ∅    | ∅    | ∅        | {Y6} | ∅        |
| \* Y6 | {Y6} | {Y6} | {Y6}     | {Y6} | {Y6}     |
| y1    | ∅    | ∅    | ∅        | {y2} | ∅        |
| y2    | ∅    | ∅    | {y3}     | ∅    | ∅        |
| y3    | ∅    | ∅    | {y4}     | ∅    | ∅        |
| y4    | ∅    | ∅    | ∅        | {y5} | ∅        |
| y5    | ∅    | ∅    | ∅        | {y6} | ∅        |
| y6    | {y6} | {y6} | {y6, X1} | {y6} | {y6}     |
| X1    | ∅    | ∅    | ∅        | {X2} | ∅        |
| X2    | ∅    | ∅    | ∅        | {X3} | ∅        |
| X3    | ∅    | ∅    | ∅        | ∅    | {X4}     |
| X4    | ∅    | ∅    | ∅        | {X5} | ∅        |
| \* X5 | {X5} | {X5} | {X5}     | {X5} | {X5}     |

Tabla de transiciones (→ inicial, \* aceptación, — sin transición).

| Cadena              | Longitud | Esperado | Obtenido | Tipo de caso                                     |
|---------------------|:--------:|----------|----------|--------------------------------------------------|
| `abbcbcbaabb`       |    11    | acepta   | acepta   | válida                                           |
| `cbaabb1abbcb`      |    12    | acepta   | acepta   | válida                                           |
| `a1abbcbcbaabba`    |    14    | acepta   | acepta   | válida                                           |
| `cbaabb1abbcb0010`  |    16    | acepta   | acepta   | válida                                           |
| `1bbccbaabb0abbcba` |    17    | acepta   | acepta   | válida                                           |
| λ                   |    0     | rechaza  | rechaza  | inválida                                         |
| `c`                 |    1     | rechaza  | rechaza  | inválida                                         |
| `1b0`               |    3     | rechaza  | rechaza  | inválida                                         |
| `cac1b`             |    5     | rechaza  | rechaza  | inválida                                         |
| `baa1a0aa`          |    8     | rechaza  | rechaza  | inválida                                         |
| `0b0ac0b0ab`        |    10    | rechaza  | rechaza  | frontera: justo por debajo de la longitud mínima |

Cadenas de prueba.

## Lista 3 · AFN del problema 109

**Enunciado.** AFN para el problema 109: Las palabras de Σ2 que incluyen abbcb y cbaabb, que sí se pueden traslapar.

**Clase.** AFN: Hay elección: δ(c0c0, a) = {c0c0, c1c0}. **Archivos.** `automatas/afnd/lista3-afn-109.jff` (y `.json`, `.xml`).

**Diseño.** Intersección de los dos AFN «contiene» por la construcción de producto, que admite traslapes.

| δ       | 0      | 1      | a            | b      | c            |
|---------|--------|--------|--------------|--------|--------------|
| → c0c0  | {c0c0} | {c0c0} | {c0c0, c1c0} | {c0c0} | {c0c0, c0c1} |
| c1c0    | ∅      | ∅      | ∅            | {c2c0} | ∅            |
| c0c1    | ∅      | ∅      | ∅            | {c0c2} | ∅            |
| c2c0    | ∅      | ∅      | ∅            | {c3c0} | ∅            |
| c0c2    | ∅      | ∅      | {c0c3, c1c3} | ∅      | ∅            |
| c3c0    | ∅      | ∅      | ∅            | ∅      | {c4c0, c4c1} |
| c0c3    | ∅      | ∅      | {c0c4, c1c4} | ∅      | ∅            |
| c1c3    | ∅      | ∅      | ∅            | ∅      | ∅            |
| c4c0    | ∅      | ∅      | ∅            | {c5c0} | ∅            |
| c4c1    | ∅      | ∅      | ∅            | {c5c2} | ∅            |
| c0c4    | ∅      | ∅      | ∅            | {c0c5} | ∅            |
| c1c4    | ∅      | ∅      | ∅            | {c2c5} | ∅            |
| c5c0    | {c5c0} | {c5c0} | {c5c0}       | {c5c0} | {c5c0, c5c1} |
| c5c2    | ∅      | ∅      | {c5c3}       | ∅      | ∅            |
| c0c5    | ∅      | ∅      | ∅            | {c0c6} | ∅            |
| c2c5    | ∅      | ∅      | ∅            | {c3c6} | ∅            |
| c5c1    | ∅      | ∅      | ∅            | {c5c2} | ∅            |
| c5c3    | ∅      | ∅      | {c5c4}       | ∅      | ∅            |
| c0c6    | {c0c6} | {c0c6} | {c0c6, c1c6} | {c0c6} | {c0c6}       |
| c3c6    | ∅      | ∅      | ∅            | ∅      | {c4c6}       |
| c5c4    | ∅      | ∅      | ∅            | {c5c5} | ∅            |
| c1c6    | ∅      | ∅      | ∅            | {c2c6} | ∅            |
| c4c6    | ∅      | ∅      | ∅            | {c5c6} | ∅            |
| c5c5    | ∅      | ∅      | ∅            | {c5c6} | ∅            |
| c2c6    | ∅      | ∅      | ∅            | {c3c6} | ∅            |
| \* c5c6 | {c5c6} | {c5c6} | {c5c6}       | {c5c6} | {c5c6}       |

Tabla de transiciones (→ inicial, \* aceptación, — sin transición).

| Cadena           | Longitud | Esperado | Obtenido | Tipo de caso                                     |
|------------------|:--------:|----------|----------|--------------------------------------------------|
| `cbaabbcb`       |    8     | acepta   | acepta   | válida                                           |
| `acbaabbcb`      |    9     | acepta   | acepta   | válida                                           |
| `1acbaabbcba`    |    11    | acepta   | acepta   | válida                                           |
| `011cbaabbcbbb`  |    13    | acepta   | acepta   | válida                                           |
| `1a0c0cbaabbcba` |    14    | acepta   | acepta   | válida                                           |
| λ                |    0     | rechaza  | rechaza  | inválida                                         |
| `a`              |    1     | rechaza  | rechaza  | inválida                                         |
| `1ac`            |    3     | rechaza  | rechaza  | inválida                                         |
| `1ab00`          |    5     | rechaza  | rechaza  | inválida                                         |
| `cbaaac01`       |    8     | rechaza  | rechaza  | inválida                                         |
| `abc0bca`        |    7     | rechaza  | rechaza  | frontera: justo por debajo de la longitud mínima |

Cadenas de prueba.

## Lista 3 · AFN del problema 110

**Enunciado.** AFN para el problema 110: Las palabras de Σ1 que contienen exactamente tres veces la subcadena 01.

**Clase.** AFD: Cada par (estado, símbolo) tiene a lo sumo un destino y no hay transiciones λ. **Archivos.** `automatas/afd/lista3-afn-110.jff` (y `.json`, `.xml`).

**Diseño.** No hay una versión no determinista más simple: el lenguaje depende de contar (longitud, apariciones o fases). Se presenta el AFD del problema sin el estado muerto; una función de transición parcial es un caso particular de AFN.

| δ      | 0   | 1   | 2   |
|--------|-----|-----|-----|
| → 0·λ  | 0·0 | 0·λ | 0·λ |
| 0·0    | 0·0 | 1·λ | 0·λ |
| 1·λ    | 1·0 | 1·λ | 1·λ |
| 1·0    | 1·0 | 2·λ | 1·λ |
| 2·λ    | 2·0 | 2·λ | 2·λ |
| 2·0    | 2·0 | 3·λ | 2·λ |
| \* 3·λ | 3·0 | 3·λ | 3·λ |
| \* 3·0 | 3·0 | —   | 3·λ |

Tabla de transiciones (→ inicial, \* aceptación, — sin transición).

| Cadena           | Longitud | Esperado | Obtenido | Tipo de caso                                     |
|------------------|:--------:|----------|----------|--------------------------------------------------|
| `010101`         |    6     | acepta   | acepta   | válida                                           |
| `2010101`        |    7     | acepta   | acepta   | válida                                           |
| `010010120`      |    9     | acepta   | acepta   | válida                                           |
| `00120001001`    |    11    | acepta   | acepta   | válida                                           |
| `00001001201000` |    14    | acepta   | acepta   | válida                                           |
| λ                |    0     | rechaza  | rechaza  | inválida                                         |
| `2`              |    1     | rechaza  | rechaza  | inválida                                         |
| `020`            |    3     | rechaza  | rechaza  | inválida                                         |
| `20111`          |    5     | rechaza  | rechaza  | inválida                                         |
| `11010012`       |    8     | rechaza  | rechaza  | inválida                                         |
| `00001`          |    5     | rechaza  | rechaza  | frontera: justo por debajo de la longitud mínima |

Cadenas de prueba.

## Lista 3 · AFN del problema 111

**Enunciado.** AFN para el problema 111: Las palabras de Σ1 que contienen exactamente tres veces la subcadena 01002.

**Clase.** AFD: Cada par (estado, símbolo) tiene a lo sumo un destino y no hay transiciones λ. **Archivos.** `automatas/afd/lista3-afn-111.jff` (y `.json`, `.xml`).

**Diseño.** No hay una versión no determinista más simple: el lenguaje depende de contar (longitud, apariciones o fases). Se presenta el AFD del problema sin el estado muerto; una función de transición parcial es un caso particular de AFN.

| δ         | 0      | 1    | 2   |
|-----------|--------|------|-----|
| → 0·λ     | 0·0    | 0·λ  | 0·λ |
| 0·0       | 0·0    | 0·01 | 0·λ |
| 0·01      | 0·010  | 0·λ  | 0·λ |
| 0·010     | 0·0100 | 0·01 | 0·λ |
| 0·0100    | 0·0    | 0·01 | 1·λ |
| 1·λ       | 1·0    | 1·λ  | 1·λ |
| 1·0       | 1·0    | 1·01 | 1·λ |
| 1·01      | 1·010  | 1·λ  | 1·λ |
| 1·010     | 1·0100 | 1·01 | 1·λ |
| 1·0100    | 1·0    | 1·01 | 2·λ |
| 2·λ       | 2·0    | 2·λ  | 2·λ |
| 2·0       | 2·0    | 2·01 | 2·λ |
| 2·01      | 2·010  | 2·λ  | 2·λ |
| 2·010     | 2·0100 | 2·01 | 2·λ |
| 2·0100    | 2·0    | 2·01 | 3·λ |
| \* 3·λ    | 3·0    | 3·λ  | 3·λ |
| \* 3·0    | 3·0    | 3·01 | 3·λ |
| \* 3·01   | 3·010  | 3·λ  | 3·λ |
| \* 3·010  | 3·0100 | 3·01 | 3·λ |
| \* 3·0100 | 3·0    | 3·01 | —   |

Tabla de transiciones (→ inicial, \* aceptación, — sin transición).

| Cadena                  | Longitud | Esperado | Obtenido | Tipo de caso                                     |
|-------------------------|:--------:|----------|----------|--------------------------------------------------|
| `010020100201002`       |    15    | acepta   | acepta   | válida                                           |
| `0100200100201002`      |    16    | acepta   | acepta   | válida                                           |
| `010020201002010021`    |    18    | acepta   | acepta   | válida                                           |
| `12010022100100201002`  |    20    | acepta   | acepta   | válida                                           |
| `010022001220100201002` |    21    | acepta   | acepta   | válida                                           |
| λ                       |    0     | rechaza  | rechaza  | inválida                                         |
| `1`                     |    1     | rechaza  | rechaza  | inválida                                         |
| `022`                   |    3     | rechaza  | rechaza  | inválida                                         |
| `12110`                 |    5     | rechaza  | rechaza  | inválida                                         |
| `20021000`              |    8     | rechaza  | rechaza  | inválida                                         |
| `21120022200202`        |    14    | rechaza  | rechaza  | frontera: justo por debajo de la longitud mínima |

Cadenas de prueba.

## Lista 3 · AFN del problema 112

**Enunciado.** AFN para el problema 112: Las palabras de Σ1 que contienen dos veces 010 sin traslaparse (01010 no pertenece, 010010 sí).

**Clase.** AFN: Hay elección: δ(i, 0) = {i, a1}. **Archivos.** `automatas/afnd/lista3-afn-112.jff` (y `.json`, `.xml`).

**Diseño.** Σ*010Σ*010Σ\*: dos copias de 010 separadas por un ciclo; la segunda empieza después de que termina la primera.

| δ     | 0        | 1    | 2    |
|-------|----------|------|------|
| → i   | {i, a1}  | {i}  | {i}  |
| a1    | ∅        | {a2} | ∅    |
| a2    | {a3}     | ∅    | ∅    |
| a3    | {a3, b1} | {a3} | {a3} |
| b1    | ∅        | {b2} | ∅    |
| b2    | {b3}     | ∅    | ∅    |
| \* b3 | {b3}     | {b3} | {b3} |

Tabla de transiciones (→ inicial, \* aceptación, — sin transición).

| Cadena           | Longitud | Esperado | Obtenido | Tipo de caso                                     |
|------------------|:--------:|----------|----------|--------------------------------------------------|
| `010010`         |    6     | acepta   | acepta   | válida                                           |
| `0100010`        |    7     | acepta   | acepta   | válida                                           |
| `100100100`      |    9     | acepta   | acepta   | válida                                           |
| `01022010022`    |    11    | acepta   | acepta   | válida                                           |
| `22120010010201` |    14    | acepta   | acepta   | válida                                           |
| λ                |    0     | rechaza  | rechaza  | inválida                                         |
| `1`              |    1     | rechaza  | rechaza  | inválida                                         |
| `122`            |    3     | rechaza  | rechaza  | inválida                                         |
| `02122`          |    5     | rechaza  | rechaza  | inválida                                         |
| `22210211`       |    8     | rechaza  | rechaza  | inválida                                         |
| `10002`          |    5     | rechaza  | rechaza  | frontera: justo por debajo de la longitud mínima |

Cadenas de prueba.

## Lista 3 · AFN del problema 113

**Enunciado.** AFN para el problema 113: Las palabras de Σ1 que contienen dos veces 010, que sí se pueden traslapar.

**Clase.** AFN: Hay elección: δ(i, 0) = {i, a1, o1}. **Archivos.** `automatas/afnd/lista3-afn-113.jff` (y `.json`, `.xml`).

**Diseño.** Σ*(010Σ*010 + 01010)Σ\*: dos apariciones disjuntas o una sola cadena 01010 en la que comparten el 0 central.

| δ     | 0           | 1    | 2    |
|-------|-------------|------|------|
| → i   | {i, a1, o1} | {i}  | {i}  |
| a1    | ∅           | {a2} | ∅    |
| a2    | {a3}        | ∅    | ∅    |
| a3    | {a3, b1}    | {a3} | {a3} |
| b1    | ∅           | {b2} | ∅    |
| b2    | {b3}        | ∅    | ∅    |
| \* b3 | {b3}        | {b3} | {b3} |
| o1    | ∅           | {o2} | ∅    |
| o2    | {o3}        | ∅    | ∅    |
| o3    | ∅           | {o4} | ∅    |
| o4    | {b3}        | ∅    | ∅    |

Tabla de transiciones (→ inicial, \* aceptación, — sin transición).

| Cadena          | Longitud | Esperado | Obtenido | Tipo de caso                                     |
|-----------------|:--------:|----------|----------|--------------------------------------------------|
| `01010`         |    5     | acepta   | acepta   | válida                                           |
| `010101`        |    6     | acepta   | acepta   | válida                                           |
| `20101001`      |    8     | acepta   | acepta   | válida                                           |
| `0101020211`    |    10    | acepta   | acepta   | válida                                           |
| `2101022220102` |    13    | acepta   | acepta   | válida                                           |
| λ               |    0     | rechaza  | rechaza  | inválida                                         |
| `0`             |    1     | rechaza  | rechaza  | inválida                                         |
| `222`           |    3     | rechaza  | rechaza  | inválida                                         |
| `22201`         |    5     | rechaza  | rechaza  | inválida                                         |
| `11210000`      |    8     | rechaza  | rechaza  | inválida                                         |
| `0111`          |    4     | rechaza  | rechaza  | frontera: justo por debajo de la longitud mínima |

Cadenas de prueba.

## Lista 3 · AFN del problema 114

**Enunciado.** AFN para el problema 114: L = {w ∈ Σ3\* : w = aⁿbᵐ, m, n ∈ N}.

**Clase.** AFD: Cada par (estado, símbolo) tiene a lo sumo un destino y no hay transiciones λ. **Archivos.** `automatas/afd/lista3-afn-114.jff` (y `.json`, `.xml`).

**Diseño.** No hay una versión no determinista más simple: el lenguaje depende de contar (longitud, apariciones o fases). Se presenta el AFD del problema sin el estado muerto; una función de transición parcial es un caso particular de AFN.

| δ        | a   | b     |
|----------|-----|-------|
| →\* a\*  | a\* | a\*b+ |
| \* a\*b+ | —   | a\*b+ |

Tabla de transiciones (→ inicial, \* aceptación, — sin transición).

| Cadena       | Longitud | Esperado | Obtenido | Tipo de caso |
|--------------|:--------:|----------|----------|--------------|
| λ            |    0     | acepta   | acepta   | válida       |
| `b`          |    1     | acepta   | acepta   | válida       |
| `aaa`        |    3     | acepta   | acepta   | válida       |
| `aaabb`      |    5     | acepta   | acepta   | válida       |
| `aaaaaaab`   |    8     | acepta   | acepta   | válida       |
| `ba`         |    2     | rechaza  | rechaza  | inválida     |
| `baa`        |    3     | rechaza  | rechaza  | inválida     |
| `aabaa`      |    5     | rechaza  | rechaza  | inválida     |
| `babbbbb`    |    7     | rechaza  | rechaza  | inválida     |
| `abaabbbabb` |    10    | rechaza  | rechaza  | inválida     |

Cadenas de prueba.

## Lista 3 · AFN del problema 115

**Enunciado.** AFN para el problema 115: L = {w ∈ Σ2\* : w = (abc)ⁿ, n ∈ N}.

**Clase.** AFD: Cada par (estado, símbolo) tiene a lo sumo un destino y no hay transiciones λ. **Archivos.** `automatas/afd/lista3-afn-115.jff` (y `.json`, `.xml`).

**Diseño.** No hay una versión no determinista más simple: el lenguaje depende de contar (longitud, apariciones o fases). Se presenta el AFD del problema sin el estado muerto; una función de transición parcial es un caso particular de AFN.

| δ           | 0   | 1   | a   | b   | c       |
|-------------|-----|-----|-----|-----|---------|
| →\* (abc)\* | —   | —   | …a  | —   | —       |
| …a          | —   | —   | —   | …ab | —       |
| …ab         | —   | —   | —   | —   | (abc)\* |

Tabla de transiciones (→ inicial, \* aceptación, — sin transición).

| Cadena         | Longitud | Esperado | Obtenido | Tipo de caso |
|----------------|:--------:|----------|----------|--------------|
| λ              |    0     | acepta   | acepta   | válida       |
| `abc`          |    3     | acepta   | acepta   | válida       |
| `abcabc`       |    6     | acepta   | acepta   | válida       |
| `abcabcabc`    |    9     | acepta   | acepta   | válida       |
| `abcabcabcabc` |    12    | acepta   | acepta   | válida       |
| `0`            |    1     | rechaza  | rechaza  | inválida     |
| `c1`           |    2     | rechaza  | rechaza  | inválida     |
| `c01b`         |    4     | rechaza  | rechaza  | inválida     |
| `0a010c`       |    6     | rechaza  | rechaza  | inválida     |
| `cb010bc0a`    |    9     | rechaza  | rechaza  | inválida     |

Cadenas de prueba.

## Lista 3 · AFN del problema 117

**Enunciado.** AFN para el problema 117: L = {w ∈ Σ3\* : w = aⁿbᵐaᵖb^q, m, n, p, q ∈ N}.

**Clase.** AFD: Cada par (estado, símbolo) tiene a lo sumo un destino y no hay transiciones λ. **Archivos.** `automatas/afd/lista3-afn-117.jff` (y `.json`, `.xml`).

**Diseño.** No hay una versión no determinista más simple: el lenguaje depende de contar (longitud, apariciones o fases). Se presenta el AFD del problema sin el estado muerto; una función de transición parcial es un caso particular de AFN.

| δ          | a      | b      |
|------------|--------|--------|
| →\* f1:a\* | f1:a\* | f2:b\* |
| \* f2:b\*  | f3:a\* | f2:b\* |
| \* f3:a\*  | f3:a\* | f4:b\* |
| \* f4:b\*  | —      | f4:b\* |

Tabla de transiciones (→ inicial, \* aceptación, — sin transición).

| Cadena         | Longitud | Esperado | Obtenido | Tipo de caso |
|----------------|:--------:|----------|----------|--------------|
| λ              |    0     | acepta   | acepta   | válida       |
| `b`            |    1     | acepta   | acepta   | válida       |
| `aaa`          |    3     | acepta   | acepta   | válida       |
| `bbaab`        |    5     | acepta   | acepta   | válida       |
| `aaabbabb`     |    8     | acepta   | acepta   | válida       |
| `baba`         |    4     | rechaza  | rechaza  | inválida     |
| `babba`        |    5     | rechaza  | rechaza  | inválida     |
| `babbaaa`      |    7     | rechaza  | rechaza  | inválida     |
| `babaababb`    |    9     | rechaza  | rechaza  | inválida     |
| `babbabbbbbbb` |    12    | rechaza  | rechaza  | inválida     |

Cadenas de prueba.

## Lista 3 · AFN del problema 118

**Enunciado.** AFN para el problema 118: L = {w ∈ Σ3\* : w = axabya, x, y ∈ Σ3\*}.

**Clase.** AFN: Hay elección: δ(q1, a) = {q1, q2}. **Archivos.** `automatas/afnd/lista3-afn-118.jff` (y `.json`, `.xml`).

**Diseño.** Sigue literalmente axabya: a, ciclo x, ab, ciclo y, a final.

| δ     | a        | b    |
|-------|----------|------|
| → q0  | {q1}     | ∅    |
| q1    | {q1, q2} | {q1} |
| q2    | ∅        | {q3} |
| q3    | {q3, q4} | {q3} |
| \* q4 | ∅        | ∅    |

Tabla de transiciones (→ inicial, \* aceptación, — sin transición).

| Cadena         | Longitud | Esperado | Obtenido | Tipo de caso |
|----------------|:--------:|----------|----------|--------------|
| `aaba`         |    4     | acepta   | acepta   | válida       |
| `aabba`        |    5     | acepta   | acepta   | válida       |
| `ababaaa`      |    7     | acepta   | acepta   | válida       |
| `ababbbbaa`    |    9     | acepta   | acepta   | válida       |
| `aababaaabaaa` |    12    | acepta   | acepta   | válida       |
| λ              |    0     | rechaza  | rechaza  | inválida     |
| `a`            |    1     | rechaza  | rechaza  | inválida     |
| `baa`          |    3     | rechaza  | rechaza  | inválida     |
| `abbaa`        |    5     | rechaza  | rechaza  | inválida     |
| `abaabbab`     |    8     | rechaza  | rechaza  | inválida     |

Cadenas de prueba.

## Lista 3 · AFN del problema 119

**Enunciado.** AFN para el problema 119: Las palabras de Σ3 tales que después de cada subcadena aa aparece una b.

**Clase.** AFD: Cada par (estado, símbolo) tiene a lo sumo un destino y no hay transiciones λ. **Archivos.** `automatas/afd/lista3-afn-119.jff` (y `.json`, `.xml`).

**Diseño.** No hay una versión no determinista más simple: el lenguaje depende de contar (longitud, apariciones o fases). Se presenta el AFD del problema sin el estado muerto; una función de transición parcial es un caso particular de AFN.

| δ         | a   | b     |
|-----------|-----|-------|
| →\* sin a | a   | sin a |
| \* a      | aa  | sin a |
| aa        | —   | sin a |

Tabla de transiciones (→ inicial, \* aceptación, — sin transición).

| Cadena       | Longitud | Esperado | Obtenido | Tipo de caso |
|--------------|:--------:|----------|----------|--------------|
| λ            |    0     | acepta   | acepta   | válida       |
| `b`          |    1     | acepta   | acepta   | válida       |
| `aba`        |    3     | acepta   | acepta   | válida       |
| `babba`      |    5     | acepta   | acepta   | válida       |
| `bbbabbbb`   |    8     | acepta   | acepta   | válida       |
| `aa`         |    2     | rechaza  | rechaza  | inválida     |
| `aaa`        |    3     | rechaza  | rechaza  | inválida     |
| `aabaa`      |    5     | rechaza  | rechaza  | inválida     |
| `babbbaa`    |    7     | rechaza  | rechaza  | inválida     |
| `aaaaaaaabb` |    10    | rechaza  | rechaza  | inválida     |

Cadenas de prueba.

## Lista 3 · AFN del problema 120

**Enunciado.** AFN para el problema 120: Las palabras de Σ1 tales que el primer carácter y el último son distintos.

**Clase.** AFN: Hay elección: δ(s0, 1) = {s0, f}. **Archivos.** `automatas/afnd/lista3-afn-120.jff` (y `.json`, `.xml`).

**Diseño.** El estado sₓ recuerda el primer símbolo x; el AFN adivina el último símbolo, que debe ser distinto de x.

| δ    | 0       | 1       | 2       |
|------|---------|---------|---------|
| → q0 | {s0}    | {s1}    | {s2}    |
| s0   | {s0}    | {s0, f} | {s0, f} |
| s1   | {s1, f} | {s1}    | {s1, f} |
| s2   | {s2, f} | {s2, f} | {s2}    |
| \* f | ∅       | ∅       | ∅       |

Tabla de transiciones (→ inicial, \* aceptación, — sin transición).

| Cadena       | Longitud | Esperado | Obtenido | Tipo de caso                                     |
|--------------|:--------:|----------|----------|--------------------------------------------------|
| `12`         |    2     | acepta   | acepta   | válida                                           |
| `211`        |    3     | acepta   | acepta   | válida                                           |
| `12002`      |    5     | acepta   | acepta   | válida                                           |
| `1202000`    |    7     | acepta   | acepta   | válida                                           |
| `0121120211` |    10    | acepta   | acepta   | válida                                           |
| λ            |    0     | rechaza  | rechaza  | inválida                                         |
| `1`          |    1     | rechaza  | rechaza  | inválida                                         |
| `222`        |    3     | rechaza  | rechaza  | inválida                                         |
| `21012`      |    5     | rechaza  | rechaza  | inválida                                         |
| `02120120`   |    8     | rechaza  | rechaza  | inválida                                         |
| `02`         |    2     | acepta   | acepta   | frontera: aceptada más corta                     |
| `2`          |    1     | rechaza  | rechaza  | frontera: justo por debajo de la longitud mínima |

Cadenas de prueba.

## Lista 3 · AFN del problema 121

**Enunciado.** AFN para el problema 121: Las palabras de Σ1 de longitud 3n tales que cada bloque de longitud 3 tiene al menos un 0.

**Clase.** AFD: Cada par (estado, símbolo) tiene a lo sumo un destino y no hay transiciones λ. **Archivos.** `automatas/afd/lista3-afn-121.jff` (y `.json`, `.xml`).

**Diseño.** No hay una versión no determinista más simple: el lenguaje depende de contar (longitud, apariciones o fases). Se presenta el AFD del problema sin el estado muerto; una función de transición parcial es un caso particular de AFN.

| δ      | 0    | 1    | 2    |
|--------|------|------|------|
| →\* b0 | b1+0 | b1   | b1   |
| b1+0   | b2+0 | b2+0 | b2+0 |
| b1     | b2+0 | b2   | b2   |
| b2+0   | b0   | b0   | b0   |
| b2     | b0   | —    | —    |

Tabla de transiciones (→ inicial, \* aceptación, — sin transición).

| Cadena      | Longitud | Esperado | Obtenido | Tipo de caso |
|-------------|:--------:|----------|----------|--------------|
| λ           |    0     | acepta   | acepta   | válida       |
| `021`       |    3     | acepta   | acepta   | válida       |
| `020001`    |    6     | acepta   | acepta   | válida       |
| `120100`    |    6     | acepta   | acepta   | válida       |
| `021022022` |    9     | acepta   | acepta   | válida       |
| `2`         |    1     | rechaza  | rechaza  | inválida     |
| `01`        |    2     | rechaza  | rechaza  | inválida     |
| `0022`      |    4     | rechaza  | rechaza  | inválida     |
| `011222`    |    6     | rechaza  | rechaza  | inválida     |
| `210110211` |    9     | rechaza  | rechaza  | inválida     |

Cadenas de prueba.

## Lista 3 · AFN del problema 122

**Enunciado.** AFN para el problema 122: Las palabras de Σ1 tales que cualquier cadena de tres símbolos consecutivos tiene un 0.

**Clase.** AFD: Cada par (estado, símbolo) tiene a lo sumo un destino y no hay transiciones λ. **Archivos.** `automatas/afd/lista3-afn-122.jff` (y `.json`, `.xml`).

**Diseño.** No hay una versión no determinista más simple: el lenguaje depende de contar (longitud, apariciones o fases). Se presenta el AFD del problema sin el estado muerto; una función de transición parcial es un caso particular de AFN.

| δ           | 0       | 1       | 2       |
|-------------|---------|---------|---------|
| →\* 0 sin 0 | 0 sin 0 | 1 sin 0 | 1 sin 0 |
| \* 1 sin 0  | 0 sin 0 | 2 sin 0 | 2 sin 0 |
| \* 2 sin 0  | 0 sin 0 | —       | —       |

Tabla de transiciones (→ inicial, \* aceptación, — sin transición).

| Cadena        | Longitud | Esperado | Obtenido | Tipo de caso |
|---------------|:--------:|----------|----------|--------------|
| λ             |    0     | acepta   | acepta   | válida       |
| `1`           |    1     | acepta   | acepta   | válida       |
| `012`         |    3     | acepta   | acepta   | válida       |
| `20102`       |    5     | acepta   | acepta   | válida       |
| `10200220`    |    8     | acepta   | acepta   | válida       |
| `112`         |    3     | rechaza  | rechaza  | inválida     |
| `1120`        |    4     | rechaza  | rechaza  | inválida     |
| `202211`      |    6     | rechaza  | rechaza  | inválida     |
| `01200211`    |    8     | rechaza  | rechaza  | inválida     |
| `00221111212` |    11    | rechaza  | rechaza  | inválida     |

Cadenas de prueba.

## Lista 3 · AFN del problema 123

**Enunciado.** AFN para el problema 123: Las palabras de Σ3 de la forma wxw donde w ∈ Σ3² y x ∈ Σ3\*.

**Clase.** AFN: Hay elección: δ(q0, a) = {aa1, ab1}. **Archivos.** `automatas/afnd/lista3-afn-123.jff` (y `.json`, `.xml`).

**Diseño.** Una rama por cada w ∈ Σ3²: se lee w, un ciclo para x y otra vez w. El AFN adivina cuándo empieza la copia final.

| δ    | a          | b          |
|------|------------|------------|
| → q0 | {aa1, ab1} | {ba1, bb1} |
| aa1  | {aa2}      | ∅          |
| aa2  | {aa2, aa3} | {aa2}      |
| aa3  | {F}        | ∅          |
| ab1  | ∅          | {ab2}      |
| ab2  | {ab2, ab3} | {ab2}      |
| ab3  | ∅          | {F}        |
| ba1  | {ba2}      | ∅          |
| ba2  | {ba2}      | {ba2, ba3} |
| ba3  | {F}        | ∅          |
| bb1  | ∅          | {bb2}      |
| bb2  | {bb2}      | {bb2, bb3} |
| bb3  | ∅          | {F}        |
| \* F | ∅          | ∅          |

Tabla de transiciones (→ inicial, \* aceptación, — sin transición).

| Cadena         | Longitud | Esperado | Obtenido | Tipo de caso                                     |
|----------------|:--------:|----------|----------|--------------------------------------------------|
| `abab`         |    4     | acepta   | acepta   | válida                                           |
| `aaaaa`        |    5     | acepta   | acepta   | válida                                           |
| `aababaa`      |    7     | acepta   | acepta   | válida                                           |
| `bbbabbabb`    |    9     | acepta   | acepta   | válida                                           |
| `bbaabbaababb` |    12    | acepta   | acepta   | válida                                           |
| λ              |    0     | rechaza  | rechaza  | inválida                                         |
| `a`            |    1     | rechaza  | rechaza  | inválida                                         |
| `bba`          |    3     | rechaza  | rechaza  | inválida                                         |
| `aabbb`        |    5     | rechaza  | rechaza  | inválida                                         |
| `aaabbaba`     |    8     | rechaza  | rechaza  | inválida                                         |
| `aaaa`         |    4     | acepta   | acepta   | frontera: aceptada más corta                     |
| `aab`          |    3     | rechaza  | rechaza  | frontera: justo por debajo de la longitud mínima |

Cadenas de prueba.

## Lista 3 · Ejercicio 189

**Enunciado.** AFN sobre {0, 1} para las palabras que contienen 00101 o 00110; recorrido de 1001011.

**Clase.** AFN: Hay elección: δ(i, 0) = {i, c1}. **Archivos.** `automatas/afnd/lista3-189.jff` (y `.json`, `.xml`).

**Diseño.** Los dos patrones comparten el prefijo 001, así que se escribe una sola vez y se bifurca en 01 y 10.

| δ    | 0       | 1    |
|------|---------|------|
| → i  | {i, c1} | {i}  |
| c1   | {c2}    | ∅    |
| c2   | ∅       | {c3} |
| c3   | {u4}    | {d4} |
| u4   | ∅       | {f}  |
| \* f | {f}     | {f}  |
| d4   | {f}     | ∅    |

Tabla de transiciones (→ inicial, \* aceptación, — sin transición).

| Cadena          | Longitud | Esperado | Obtenido | Tipo de caso                                     |
|-----------------|:--------:|----------|----------|--------------------------------------------------|
| `00110`         |    5     | acepta   | acepta   | válida                                           |
| `100110`        |    6     | acepta   | acepta   | válida                                           |
| `00101100`      |    8     | acepta   | acepta   | válida                                           |
| `0100101101`    |    10    | acepta   | acepta   | válida                                           |
| `1001101110001` |    13    | acepta   | acepta   | válida                                           |
| λ               |    0     | rechaza  | rechaza  | inválida                                         |
| `0`             |    1     | rechaza  | rechaza  | inválida                                         |
| `101`           |    3     | rechaza  | rechaza  | inválida                                         |
| `01101`         |    5     | rechaza  | rechaza  | inválida                                         |
| `01100000`      |    8     | rechaza  | rechaza  | inválida                                         |
| `00101`         |    5     | acepta   | acepta   | frontera: aceptada más corta                     |
| `0110`          |    4     | rechaza  | rechaza  | frontera: justo por debajo de la longitud mínima |

Cadenas de prueba.

## Lista 3 · Ejercicio 190

**Enunciado.** AFN sobre {0, 1} para las palabras que contienen 11010 y 10100; recorrido de 01101010100.

**Clase.** AFN: Hay elección: δ(c0c0, 1) = {c0c0, c0c1, c1c0, c1c1}. **Archivos.** `automatas/afnd/lista3-190.jff` (y `.json`, `.xml`).

**Diseño.** Producto de los AFN «contiene 11010» y «contiene 10100»; los patrones pueden traslaparse (110100 contiene ambos), por eso no basta concatenarlos.

| δ       | 0      | 1                        |
|---------|--------|--------------------------|
| → c0c0  | {c0c0} | {c0c0, c0c1, c1c0, c1c1} |
| c0c1    | {c0c2} | ∅                        |
| c1c0    | ∅      | {c2c0, c2c1}             |
| c1c1    | ∅      | ∅                        |
| c0c2    | ∅      | {c0c3, c1c3}             |
| c2c0    | {c3c0} | ∅                        |
| c2c1    | {c3c2} | ∅                        |
| c0c3    | {c0c4} | ∅                        |
| c1c3    | ∅      | ∅                        |
| c3c0    | ∅      | {c4c0, c4c1}             |
| c3c2    | ∅      | {c4c3}                   |
| c0c4    | {c0c5} | ∅                        |
| c4c0    | {c5c0} | ∅                        |
| c4c1    | {c5c2} | ∅                        |
| c4c3    | {c5c4} | ∅                        |
| c0c5    | {c0c5} | {c0c5, c1c5}             |
| c5c0    | {c5c0} | {c5c0, c5c1}             |
| c5c2    | ∅      | {c5c3}                   |
| c5c4    | {c5c5} | ∅                        |
| c1c5    | ∅      | {c2c5}                   |
| c5c1    | {c5c2} | ∅                        |
| c5c3    | {c5c4} | ∅                        |
| \* c5c5 | {c5c5} | {c5c5}                   |
| c2c5    | {c3c5} | ∅                        |
| c3c5    | ∅      | {c4c5}                   |
| c4c5    | {c5c5} | ∅                        |

Tabla de transiciones (→ inicial, \* aceptación, — sin transición).

| Cadena           | Longitud | Esperado | Obtenido | Tipo de caso                                     |
|------------------|:--------:|----------|----------|--------------------------------------------------|
| `110100`         |    6     | acepta   | acepta   | válida                                           |
| `1101001`        |    7     | acepta   | acepta   | válida                                           |
| `110100010`      |    9     | acepta   | acepta   | válida                                           |
| `01110100001`    |    11    | acepta   | acepta   | válida                                           |
| `01100001110100` |    14    | acepta   | acepta   | válida                                           |
| λ                |    0     | rechaza  | rechaza  | inválida                                         |
| `0`              |    1     | rechaza  | rechaza  | inválida                                         |
| `001`            |    3     | rechaza  | rechaza  | inválida                                         |
| `01011`          |    5     | rechaza  | rechaza  | inválida                                         |
| `01011001`       |    8     | rechaza  | rechaza  | inválida                                         |
| `00010`          |    5     | rechaza  | rechaza  | frontera: justo por debajo de la longitud mínima |

Cadenas de prueba.

## Lista 3 · Ejercicio 192

**Enunciado.** AFN de la tabla 192: AFD equivalente y δ̂(Z, ω).

**Clase.** AFN: Hay elección: δ(A, 1) = {B, C}. **Archivos.** `automatas/afnd/lista3-192.jff` (y `.json`, `.xml`).

**Diseño.** Construcción de subconjuntos (sólo alcanzables). El AFD asociado tiene un estado por subconjunto, así que δ̂\_D(Z, ω) es el subconjunto δ̂(Z, ω).

| δ    | 0      | 1      |
|------|--------|--------|
| → A  | {B}    | {B, C} |
| B    | {A, B} | ∅      |
| \* C | {A, C} | ∅      |

Tabla de transiciones (→ inicial, \* aceptación, — sin transición).

| Cadena      | Longitud | Esperado | Obtenido | Tipo de caso |
|-------------|:--------:|----------|----------|--------------|
| `1`         |    1     | acepta   | acepta   | válida       |
| `10`        |    2     | acepta   | acepta   | válida       |
| `1010`      |    4     | acepta   | acepta   | válida       |
| `000001`    |    6     | acepta   | acepta   | válida       |
| `001000000` |    9     | acepta   | acepta   | válida       |
| λ           |    0     | rechaza  | rechaza  | inválida     |
| `0`         |    1     | rechaza  | rechaza  | inválida     |
| `111`       |    3     | rechaza  | rechaza  | inválida     |
| `00110`     |    5     | rechaza  | rechaza  | inválida     |
| `11000101`  |    8     | rechaza  | rechaza  | inválida     |

Cadenas de prueba.

## Lista 3 · Ejercicio 193

**Enunciado.** AFN de la tabla 193: AFD equivalente y δ̂(Z, ω).

**Clase.** AFN: Hay elección: δ(A, 1) = {B, C}. **Archivos.** `automatas/afnd/lista3-193.jff` (y `.json`, `.xml`).

**Diseño.** Construcción de subconjuntos (sólo alcanzables). El AFD asociado tiene un estado por subconjunto, así que δ̂\_D(Z, ω) es el subconjunto δ̂(Z, ω).

| δ    | 0      | 1         |
|------|--------|-----------|
| → A  | ∅      | {B, C}    |
| B    | {A, D} | {B, C, D} |
| C    | {C}    | {A, C}    |
| \* D | {C}    | {D}       |

Tabla de transiciones (→ inicial, \* aceptación, — sin transición).

| Cadena       | Longitud | Esperado | Obtenido | Tipo de caso                                     |
|--------------|:--------:|----------|----------|--------------------------------------------------|
| `11`         |    2     | acepta   | acepta   | válida                                           |
| `110`        |    3     | acepta   | acepta   | válida                                           |
| `10101`      |    5     | acepta   | acepta   | válida                                           |
| `1111101`    |    7     | acepta   | acepta   | válida                                           |
| `1100001111` |    10    | acepta   | acepta   | válida                                           |
| λ            |    0     | rechaza  | rechaza  | inválida                                         |
| `1`          |    1     | rechaza  | rechaza  | inválida                                         |
| `000`        |    3     | rechaza  | rechaza  | inválida                                         |
| `00011`      |    5     | rechaza  | rechaza  | inválida                                         |
| `01110101`   |    8     | rechaza  | rechaza  | inválida                                         |
| `10`         |    2     | acepta   | acepta   | frontera: aceptada más corta                     |
| `0`          |    1     | rechaza  | rechaza  | frontera: justo por debajo de la longitud mínima |

Cadenas de prueba.

## Lista 3 · Ejercicio 194

**Enunciado.** AFN de la tabla 194: AFD equivalente y δ̂(Z, ω).

**Clase.** AFN: Hay elección: δ(A, 0) = {A, B}. **Archivos.** `automatas/afnd/lista3-194.jff` (y `.json`, `.xml`).

**Diseño.** Construcción de subconjuntos (sólo alcanzables). El AFD asociado tiene un estado por subconjunto, así que δ̂\_D(Z, ω) es el subconjunto δ̂(Z, ω).

| δ    | 0      | 1            | 2   |
|------|--------|--------------|-----|
| → A  | {A, B} | {A, C}       | {A} |
| B    | ∅      | ∅            | ∅   |
| \* C | {A, B} | {A, B, C, D} | ∅   |
| \* D | {B}    | {A}          | ∅   |

Tabla de transiciones (→ inicial, \* aceptación, — sin transición).

| Cadena      | Longitud | Esperado | Obtenido | Tipo de caso |
|-------------|:--------:|----------|----------|--------------|
| `1`         |    1     | acepta   | acepta   | válida       |
| `11`        |    2     | acepta   | acepta   | válida       |
| `0011`      |    4     | acepta   | acepta   | válida       |
| `102211`    |    6     | acepta   | acepta   | válida       |
| `111212021` |    9     | acepta   | acepta   | válida       |
| λ           |    0     | rechaza  | rechaza  | inválida     |
| `2`         |    1     | rechaza  | rechaza  | inválida     |
| `220`       |    3     | rechaza  | rechaza  | inválida     |
| `11222`     |    5     | rechaza  | rechaza  | inválida     |
| `02122220`  |    8     | rechaza  | rechaza  | inválida     |

Cadenas de prueba.

## Lista 3 · Ejercicio 195

**Enunciado.** AFN de la tabla 195: AFD equivalente y δ̂(Z, ω).

**Clase.** AFN: Hay elección: δ(A, 0) = {A, B}. **Archivos.** `automatas/afnd/lista3-195.jff` (y `.json`, `.xml`).

**Diseño.** Construcción de subconjuntos (sólo alcanzables). El AFD asociado tiene un estado por subconjunto, así que δ̂\_D(Z, ω) es el subconjunto δ̂(Z, ω).

| δ    | 0      | 1      |
|------|--------|--------|
| → A  | {A, B} | {A}    |
| B    | {A}    | {C}    |
| \* C | {A}    | {D}    |
| D    | {D}    | {E}    |
| \* E | {E}    | {C, D} |

Tabla de transiciones (→ inicial, \* aceptación, — sin transición).

| Cadena       | Longitud | Esperado | Obtenido | Tipo de caso |
|--------------|:--------:|----------|----------|--------------|
| `01`         |    2     | acepta   | acepta   | válida       |
| `101`        |    3     | acepta   | acepta   | válida       |
| `01110`      |    5     | acepta   | acepta   | válida       |
| `0100111`    |    7     | acepta   | acepta   | válida       |
| `1001110111` |    10    | acepta   | acepta   | válida       |
| λ            |    0     | rechaza  | rechaza  | inválida     |
| `1`          |    1     | rechaza  | rechaza  | inválida     |
| `011`        |    3     | rechaza  | rechaza  | inválida     |
| `00010`      |    5     | rechaza  | rechaza  | inválida     |
| `11100110`   |    8     | rechaza  | rechaza  | inválida     |

Cadenas de prueba.

## Lista 3 · Ejercicio 196

**Enunciado.** AFN-λ de la tabla 196: diagrama, AFD equivalente e incisos.

**Clase.** AFN-λ: Tiene transiciones λ, por ejemplo δ(A, λ) ∋ B. **Archivos.** `automatas/afnd-lambda/lista3-196.jff` (y `.json`, `.xml`).

**Diseño.** La tabla incluye una columna λ. Se calcula la cerradura de cada estado, se eliminan las transiciones λ y se aplica la construcción de subconjuntos.

| δ    | 0      | 1   | λ   |
|------|--------|-----|-----|
| → A  | {A}    | ∅   | {B} |
| B    | {A, B} | {C} | ∅   |
| \* C | ∅      | ∅   | ∅   |

Tabla de transiciones (→ inicial, \* aceptación, — sin transición).

| Cadena      | Longitud | Esperado | Obtenido | Tipo de caso |
|-------------|:--------:|----------|----------|--------------|
| `1`         |    1     | acepta   | acepta   | válida       |
| `01`        |    2     | acepta   | acepta   | válida       |
| `0001`      |    4     | acepta   | acepta   | válida       |
| `000001`    |    6     | acepta   | acepta   | válida       |
| `000000001` |    9     | acepta   | acepta   | válida       |
| λ           |    0     | rechaza  | rechaza  | inválida     |
| `0`         |    1     | rechaza  | rechaza  | inválida     |
| `010`       |    3     | rechaza  | rechaza  | inválida     |
| `11001`     |    5     | rechaza  | rechaza  | inválida     |
| `11101110`  |    8     | rechaza  | rechaza  | inválida     |

Cadenas de prueba.

## Lista 3 · Ejercicio 197

**Enunciado.** AFN-λ de la tabla 197: diagrama, AFD equivalente e incisos.

**Clase.** AFN-λ: Tiene transiciones λ, por ejemplo δ(A, λ) ∋ C. **Archivos.** `automatas/afnd-lambda/lista3-197.jff` (y `.json`, `.xml`).

**Diseño.** La tabla incluye una columna λ. Se calcula la cerradura de cada estado, se eliminan las transiciones λ y se aplica la construcción de subconjuntos.

| δ    | 0      | 1      | λ   |
|------|--------|--------|-----|
| → A  | {B, D} | ∅      | {C} |
| B    | {A, C} | {D}    | {D} |
| C    | ∅      | {A, C} | {B} |
| \* D | ∅      | {D}    | ∅   |

Tabla de transiciones (→ inicial, \* aceptación, — sin transición).

| Cadena     | Longitud | Esperado | Obtenido | Tipo de caso |
|------------|:--------:|----------|----------|--------------|
| λ          |    0     | acepta   | acepta   | válida       |
| `0`        |    1     | acepta   | acepta   | válida       |
| `000`      |    3     | acepta   | acepta   | válida       |
| `11110`    |    5     | acepta   | acepta   | válida       |
| `11110111` |    8     | acepta   | acepta   | válida       |

Cadenas de prueba.

## Lista 3 · Ejercicio 198

**Enunciado.** AFN-λ de la tabla 198: diagrama, AFD equivalente e incisos.

**Clase.** AFN-λ: Tiene transiciones λ, por ejemplo δ(A, λ) ∋ C. **Archivos.** `automatas/afnd-lambda/lista3-198.jff` (y `.json`, `.xml`).

**Diseño.** La tabla incluye una columna λ. Se calcula la cerradura de cada estado, se eliminan las transiciones λ y se aplica la construcción de subconjuntos.

| δ    | 0   | 1      | λ   |
|------|-----|--------|-----|
| → A  | {B} | ∅      | {C} |
| B    | {C} | ∅      | ∅   |
| C    | ∅   | {C, D} | {B} |
| \* D | ∅   | {B}    | ∅   |

Tabla de transiciones (→ inicial, \* aceptación, — sin transición).

| Cadena      | Longitud | Esperado | Obtenido | Tipo de caso |
|-------------|:--------:|----------|----------|--------------|
| `1`         |    1     | acepta   | acepta   | válida       |
| `01`        |    2     | acepta   | acepta   | válida       |
| `0011`      |    4     | acepta   | acepta   | válida       |
| `001101`    |    6     | acepta   | acepta   | válida       |
| `000111111` |    9     | acepta   | acepta   | válida       |
| λ           |    0     | rechaza  | rechaza  | inválida     |
| `0`         |    1     | rechaza  | rechaza  | inválida     |
| `000`       |    3     | rechaza  | rechaza  | inválida     |
| `00100`     |    5     | rechaza  | rechaza  | inválida     |
| `10110010`  |    8     | rechaza  | rechaza  | inválida     |

Cadenas de prueba.

## Lista 3 · Ejercicio 199

**Enunciado.** AFN-λ de la tabla 199: diagrama, AFD equivalente e incisos.

**Clase.** AFN-λ: Tiene transiciones λ, por ejemplo δ(A, λ) ∋ B. **Archivos.** `automatas/afnd-lambda/lista3-199.jff` (y `.json`, `.xml`).

**Diseño.** La tabla incluye una columna λ. Se calcula la cerradura de cada estado, se eliminan las transiciones λ y se aplica la construcción de subconjuntos.

| δ    | 0   | 1      | λ      |
|------|-----|--------|--------|
| → A  | {E} | ∅      | {B, C} |
| B    | {E} | {B}    | ∅      |
| C    | ∅   | {A, C} | {E}    |
| \* D | ∅   | {D}    | ∅      |
| \* E | ∅   | {D}    | ∅      |

Tabla de transiciones (→ inicial, \* aceptación, — sin transición).

| Cadena       | Longitud | Esperado | Obtenido | Tipo de caso |
|--------------|:--------:|----------|----------|--------------|
| λ            |    0     | acepta   | acepta   | válida       |
| `1`          |    1     | acepta   | acepta   | válida       |
| `011`        |    3     | acepta   | acepta   | válida       |
| `11111`      |    5     | acepta   | acepta   | válida       |
| `11101111`   |    8     | acepta   | acepta   | válida       |
| `00`         |    2     | rechaza  | rechaza  | inválida     |
| `001`        |    3     | rechaza  | rechaza  | inválida     |
| `10110`      |    5     | rechaza  | rechaza  | inválida     |
| `0101100`    |    7     | rechaza  | rechaza  | inválida     |
| `1111001100` |    10    | rechaza  | rechaza  | inválida     |

Cadenas de prueba.

## Lista 3 · Ejercicio 200

**Enunciado.** AFN-λ de la tabla 200: diagrama, AFD equivalente e incisos.

**Clase.** AFN-λ: Tiene transiciones λ, por ejemplo δ(A, λ) ∋ B. **Archivos.** `automatas/afnd-lambda/lista3-200.jff` (y `.json`, `.xml`).

**Diseño.** La tabla incluye una columna λ. Se calcula la cerradura de cada estado, se eliminan las transiciones λ y se aplica la construcción de subconjuntos.

| δ    | 0      | 1         | λ      |
|------|--------|-----------|--------|
| → A  | {F}    | {A, C, F} | {B}    |
| B    | {C, D} | {B, E}    | ∅      |
| C    | ∅      | {A, C}    | {E}    |
| \* D | {A, C} | {B, E}    | {E, F} |
| \* E | ∅      | {D}       | ∅      |
| F    | {B, E} | ∅         | {E}    |

Tabla de transiciones (→ inicial, \* aceptación, — sin transición).

| Cadena      | Longitud | Esperado | Obtenido | Tipo de caso                 |
|-------------|:--------:|----------|----------|------------------------------|
| `1`         |    1     | acepta   | acepta   | válida                       |
| `01`        |    2     | acepta   | acepta   | válida                       |
| `1000`      |    4     | acepta   | acepta   | válida                       |
| `100100`    |    6     | acepta   | acepta   | válida                       |
| `101010101` |    9     | acepta   | acepta   | válida                       |
| λ           |    0     | rechaza  | rechaza  | inválida                     |
| `0`         |    1     | acepta   | acepta   | frontera: aceptada más corta |

Cadenas de prueba.

## Lista 3 · Ejercicio 236

**Enunciado.** Expresión regular sobre {0, 1} para: L = {x001y : x, y ∈ Σ\*}.

**Clase.** AFN-λ: Tiene transiciones λ, por ejemplo δ(q6, λ) ∋ q4. **Archivos.** `automatas/afnd-lambda/lista3-236.jff` (y `.json`, `.xml`).

**Diseño.** La expresión se convierte en AFN-λ con la construcción de Thompson y se verifica contra la definición del lenguaje.

| δ      | 0     | 1     | λ          |
|--------|-------|-------|------------|
| → q6   | ∅     | ∅     | {q4, q7}   |
| q4     | ∅     | ∅     | {q0, q2}   |
| q0     | {q1}  | ∅     | ∅          |
| q1     | ∅     | ∅     | {q5}       |
| q2     | ∅     | {q3}  | ∅          |
| q3     | ∅     | ∅     | {q5}       |
| q5     | ∅     | ∅     | {q4, q7}   |
| q7     | ∅     | ∅     | {q8}       |
| q8     | {q9}  | ∅     | ∅          |
| q9     | ∅     | ∅     | {q10}      |
| q10    | {q11} | ∅     | ∅          |
| q11    | ∅     | ∅     | {q12}      |
| q12    | ∅     | {q13} | ∅          |
| q13    | ∅     | ∅     | {q20}      |
| q20    | ∅     | ∅     | {q18, q21} |
| q18    | ∅     | ∅     | {q14, q16} |
| q14    | {q15} | ∅     | ∅          |
| q15    | ∅     | ∅     | {q19}      |
| q16    | ∅     | {q17} | ∅          |
| q17    | ∅     | ∅     | {q19}      |
| q19    | ∅     | ∅     | {q18, q21} |
| \* q21 | ∅     | ∅     | ∅          |

Tabla de transiciones (→ inicial, \* aceptación, — sin transición).

| Cadena        | Longitud | Esperado | Obtenido | Tipo de caso                                     |
|---------------|:--------:|----------|----------|--------------------------------------------------|
| `001`         |    3     | acepta   | acepta   | válida                                           |
| `0001`        |    4     | acepta   | acepta   | válida                                           |
| `001010`      |    6     | acepta   | acepta   | válida                                           |
| `00100001`    |    8     | acepta   | acepta   | válida                                           |
| `10010011110` |    11    | acepta   | acepta   | válida                                           |
| λ             |    0     | rechaza  | rechaza  | inválida                                         |
| `0`           |    1     | rechaza  | rechaza  | inválida                                         |
| `100`         |    3     | rechaza  | rechaza  | inválida                                         |
| `01010`       |    5     | rechaza  | rechaza  | inválida                                         |
| `01000000`    |    8     | rechaza  | rechaza  | inválida                                         |
| `00`          |    2     | rechaza  | rechaza  | frontera: justo por debajo de la longitud mínima |

Cadenas de prueba.

## Lista 3 · Ejercicio 237

**Enunciado.** Expresión regular sobre {0, 1} para: L = {x010 : x ∈ Σ\*}.

**Clase.** AFN-λ: Tiene transiciones λ, por ejemplo δ(q6, λ) ∋ q4. **Archivos.** `automatas/afnd-lambda/lista3-237.jff` (y `.json`, `.xml`).

**Diseño.** La expresión se convierte en AFN-λ con la construcción de Thompson y se verifica contra la definición del lenguaje.

| δ      | 0     | 1     | λ        |
|--------|-------|-------|----------|
| → q6   | ∅     | ∅     | {q4, q7} |
| q4     | ∅     | ∅     | {q0, q2} |
| q0     | {q1}  | ∅     | ∅        |
| q1     | ∅     | ∅     | {q5}     |
| q2     | ∅     | {q3}  | ∅        |
| q3     | ∅     | ∅     | {q5}     |
| q5     | ∅     | ∅     | {q4, q7} |
| q7     | ∅     | ∅     | {q8}     |
| q8     | {q9}  | ∅     | ∅        |
| q9     | ∅     | ∅     | {q10}    |
| q10    | ∅     | {q11} | ∅        |
| q11    | ∅     | ∅     | {q12}    |
| q12    | {q13} | ∅     | ∅        |
| \* q13 | ∅     | ∅     | ∅        |

Tabla de transiciones (→ inicial, \* aceptación, — sin transición).

| Cadena        | Longitud | Esperado | Obtenido | Tipo de caso                                     |
|---------------|:--------:|----------|----------|--------------------------------------------------|
| `010`         |    3     | acepta   | acepta   | válida                                           |
| `0010`        |    4     | acepta   | acepta   | válida                                           |
| `111010`      |    6     | acepta   | acepta   | válida                                           |
| `01001010`    |    8     | acepta   | acepta   | válida                                           |
| `01110100010` |    11    | acepta   | acepta   | válida                                           |
| λ             |    0     | rechaza  | rechaza  | inválida                                         |
| `0`           |    1     | rechaza  | rechaza  | inválida                                         |
| `110`         |    3     | rechaza  | rechaza  | inválida                                         |
| `00110`       |    5     | rechaza  | rechaza  | inválida                                         |
| `00001011`    |    8     | rechaza  | rechaza  | inválida                                         |
| `11`          |    2     | rechaza  | rechaza  | frontera: justo por debajo de la longitud mínima |

Cadenas de prueba.

## Lista 3 · Ejercicio 238

**Enunciado.** Expresión regular sobre {0, 1} para: L = Σ³ ∪ Σ⁵.

**Clase.** AFN-λ: Tiene transiciones λ, por ejemplo δ(q4, λ) ∋ q0. **Archivos.** `automatas/afnd-lambda/lista3-238.jff` (y `.json`, `.xml`).

**Diseño.** La expresión se convierte en AFN-λ con la construcción de Thompson y se verifica contra la definición del lenguaje.

| δ      | 0     | 1     | λ          |
|--------|-------|-------|------------|
| → q4   | ∅     | ∅     | {q0, q2}   |
| q0     | {q1}  | ∅     | ∅          |
| q1     | ∅     | ∅     | {q5}       |
| q2     | ∅     | {q3}  | ∅          |
| q3     | ∅     | ∅     | {q5}       |
| q5     | ∅     | ∅     | {q10}      |
| q10    | ∅     | ∅     | {q6, q8}   |
| q6     | {q7}  | ∅     | ∅          |
| q7     | ∅     | ∅     | {q11}      |
| q8     | ∅     | {q9}  | ∅          |
| q9     | ∅     | ∅     | {q11}      |
| q11    | ∅     | ∅     | {q16}      |
| q16    | ∅     | ∅     | {q12, q14} |
| q12    | {q13} | ∅     | ∅          |
| q13    | ∅     | ∅     | {q17}      |
| q14    | ∅     | {q15} | ∅          |
| q15    | ∅     | ∅     | {q17}      |
| q17    | ∅     | ∅     | {q32}      |
| q32    | ∅     | ∅     | {q18, q24} |
| q18    | ∅     | ∅     | {q19}      |
| q19    | ∅     | ∅     | {q33}      |
| q24    | ∅     | ∅     | {q20, q22} |
| q20    | {q21} | ∅     | ∅          |
| q21    | ∅     | ∅     | {q25}      |
| q22    | ∅     | {q23} | ∅          |
| q23    | ∅     | ∅     | {q25}      |
| q25    | ∅     | ∅     | {q30}      |
| q30    | ∅     | ∅     | {q26, q28} |
| q26    | {q27} | ∅     | ∅          |
| q27    | ∅     | ∅     | {q31}      |
| q28    | ∅     | {q29} | ∅          |
| q29    | ∅     | ∅     | {q31}      |
| q31    | ∅     | ∅     | {q33}      |
| \* q33 | ∅     | ∅     | ∅          |

Tabla de transiciones (→ inicial, \* aceptación, — sin transición).

| Cadena           | Longitud | Esperado | Obtenido | Tipo de caso                                     |
|------------------|:--------:|----------|----------|--------------------------------------------------|
| `000`            |    3     | acepta   | acepta   | válida                                           |
| `001`            |    3     | acepta   | acepta   | válida                                           |
| `101`            |    3     | acepta   | acepta   | válida                                           |
| `111`            |    3     | acepta   | acepta   | válida                                           |
| `11100`          |    5     | acepta   | acepta   | válida                                           |
| λ                |    0     | rechaza  | rechaza  | inválida                                         |
| `0`              |    1     | rechaza  | rechaza  | inválida                                         |
| `0100`           |    4     | rechaza  | rechaza  | inválida                                         |
| `0111`           |    4     | rechaza  | rechaza  | inválida                                         |
| `10100011101001` |    14    | rechaza  | rechaza  | inválida                                         |
| `00`             |    2     | rechaza  | rechaza  | frontera: justo por debajo de la longitud mínima |

Cadenas de prueba.

## Lista 3 · Ejercicio 239

**Enunciado.** Expresión regular sobre {0, 1} para: Cadenas que comienzan con 01 o terminan con 10.

**Clase.** AFN-λ: Tiene transiciones λ, por ejemplo δ(q24, λ) ∋ q0. **Archivos.** `automatas/afnd-lambda/lista3-239.jff` (y `.json`, `.xml`).

**Diseño.** La expresión se convierte en AFN-λ con la construcción de Thompson y se verifica contra la definición del lenguaje.

| δ      | 0     | 1     | λ          |
|--------|-------|-------|------------|
| → q24  | ∅     | ∅     | {q0, q18}  |
| q0     | {q1}  | ∅     | ∅          |
| q1     | ∅     | ∅     | {q2}       |
| q2     | ∅     | {q3}  | ∅          |
| q3     | ∅     | ∅     | {q10}      |
| q10    | ∅     | ∅     | {q8, q11}  |
| q8     | ∅     | ∅     | {q4, q6}   |
| q4     | {q5}  | ∅     | ∅          |
| q5     | ∅     | ∅     | {q9}       |
| q6     | ∅     | {q7}  | ∅          |
| q7     | ∅     | ∅     | {q9}       |
| q9     | ∅     | ∅     | {q8, q11}  |
| q11    | ∅     | ∅     | {q25}      |
| q18    | ∅     | ∅     | {q16, q19} |
| q16    | ∅     | ∅     | {q12, q14} |
| q12    | {q13} | ∅     | ∅          |
| q13    | ∅     | ∅     | {q17}      |
| q14    | ∅     | {q15} | ∅          |
| q15    | ∅     | ∅     | {q17}      |
| q17    | ∅     | ∅     | {q16, q19} |
| q19    | ∅     | ∅     | {q20}      |
| q20    | ∅     | {q21} | ∅          |
| q21    | ∅     | ∅     | {q22}      |
| q22    | {q23} | ∅     | ∅          |
| q23    | ∅     | ∅     | {q25}      |
| \* q25 | ∅     | ∅     | ∅          |

Tabla de transiciones (→ inicial, \* aceptación, — sin transición).

| Cadena       | Longitud | Esperado | Obtenido | Tipo de caso |
|--------------|:--------:|----------|----------|--------------|
| `01`         |    2     | acepta   | acepta   | válida       |
| `010`        |    3     | acepta   | acepta   | válida       |
| `10010`      |    5     | acepta   | acepta   | válida       |
| `0100101`    |    7     | acepta   | acepta   | válida       |
| `0110110001` |    10    | acepta   | acepta   | válida       |
| λ            |    0     | rechaza  | rechaza  | inválida     |
| `0`          |    1     | rechaza  | rechaza  | inválida     |
| `001`        |    3     | rechaza  | rechaza  | inválida     |
| `11011`      |    5     | rechaza  | rechaza  | inválida     |
| `10101001`   |    8     | rechaza  | rechaza  | inválida     |

Cadenas de prueba.

## Lista 3 · Ejercicio 240

**Enunciado.** Expresión regular sobre {0, 1} para: Cadenas de longitud par que contienen 01.

**Clase.** AFN-λ: Tiene transiciones λ, por ejemplo δ(q76, λ) ∋ q12. **Archivos.** `automatas/afnd-lambda/lista3-240.jff` (y `.json`, `.xml`).

**Diseño.** La expresión se convierte en AFN-λ con la construcción de Thompson y se verifica contra la definición del lenguaje.

| δ      | 0     | 1     | λ          |
|--------|-------|-------|------------|
| → q76  | ∅     | ∅     | {q12, q36} |
| q12    | ∅     | ∅     | {q4, q13}  |
| q4     | ∅     | ∅     | {q0, q2}   |
| q0     | {q1}  | ∅     | ∅          |
| q1     | ∅     | ∅     | {q5}       |
| q2     | ∅     | {q3}  | ∅          |
| q3     | ∅     | ∅     | {q5}       |
| q5     | ∅     | ∅     | {q10}      |
| q10    | ∅     | ∅     | {q6, q8}   |
| q6     | {q7}  | ∅     | ∅          |
| q7     | ∅     | ∅     | {q11}      |
| q8     | ∅     | {q9}  | ∅          |
| q9     | ∅     | ∅     | {q11}      |
| q11    | ∅     | ∅     | {q4, q13}  |
| q13    | ∅     | ∅     | {q14}      |
| q14    | {q15} | ∅     | ∅          |
| q15    | ∅     | ∅     | {q16}      |
| q16    | ∅     | {q17} | ∅          |
| q17    | ∅     | ∅     | {q30}      |
| q30    | ∅     | ∅     | {q22, q31} |
| q22    | ∅     | ∅     | {q18, q20} |
| q18    | {q19} | ∅     | ∅          |
| q19    | ∅     | ∅     | {q23}      |
| q20    | ∅     | {q21} | ∅          |
| q21    | ∅     | ∅     | {q23}      |
| q23    | ∅     | ∅     | {q28}      |
| q28    | ∅     | ∅     | {q24, q26} |
| q24    | {q25} | ∅     | ∅          |
| q25    | ∅     | ∅     | {q29}      |
| q26    | ∅     | {q27} | ∅          |
| q27    | ∅     | ∅     | {q29}      |
| q29    | ∅     | ∅     | {q22, q31} |
| q31    | ∅     | ∅     | {q77}      |
| q36    | ∅     | ∅     | {q32, q34} |
| q32    | {q33} | ∅     | ∅          |
| q33    | ∅     | ∅     | {q37}      |
| q34    | ∅     | {q35} | ∅          |
| q35    | ∅     | ∅     | {q37}      |
| q37    | ∅     | ∅     | {q50}      |
| q50    | ∅     | ∅     | {q42, q51} |
| q42    | ∅     | ∅     | {q38, q40} |
| q38    | {q39} | ∅     | ∅          |
| q39    | ∅     | ∅     | {q43}      |
| q40    | ∅     | {q41} | ∅          |
| q41    | ∅     | ∅     | {q43}      |
| q43    | ∅     | ∅     | {q48}      |
| q48    | ∅     | ∅     | {q44, q46} |
| q44    | {q45} | ∅     | ∅          |
| q45    | ∅     | ∅     | {q49}      |
| q46    | ∅     | {q47} | ∅          |
| q47    | ∅     | ∅     | {q49}      |
| q49    | ∅     | ∅     | {q42, q51} |
| q51    | ∅     | ∅     | {q52}      |
| q52    | {q53} | ∅     | ∅          |
| q53    | ∅     | ∅     | {q54}      |
| q54    | ∅     | {q55} | ∅          |
| q55    | ∅     | ∅     | {q68}      |
| q68    | ∅     | ∅     | {q60, q69} |
| q60    | ∅     | ∅     | {q56, q58} |
| q56    | {q57} | ∅     | ∅          |
| q57    | ∅     | ∅     | {q61}      |
| q58    | ∅     | {q59} | ∅          |
| q59    | ∅     | ∅     | {q61}      |
| q61    | ∅     | ∅     | {q66}      |
| q66    | ∅     | ∅     | {q62, q64} |
| q62    | {q63} | ∅     | ∅          |
| q63    | ∅     | ∅     | {q67}      |
| q64    | ∅     | {q65} | ∅          |
| q65    | ∅     | ∅     | {q67}      |
| q67    | ∅     | ∅     | {q60, q69} |
| q69    | ∅     | ∅     | {q74}      |
| q74    | ∅     | ∅     | {q70, q72} |
| q70    | {q71} | ∅     | ∅          |
| q71    | ∅     | ∅     | {q75}      |
| q72    | ∅     | {q73} | ∅          |
| q73    | ∅     | ∅     | {q75}      |
| q75    | ∅     | ∅     | {q77}      |
| \* q77 | ∅     | ∅     | ∅          |

Tabla de transiciones (→ inicial, \* aceptación, — sin transición).

| Cadena         | Longitud | Esperado | Obtenido | Tipo de caso |
|----------------|:--------:|----------|----------|--------------|
| `01`           |    2     | acepta   | acepta   | válida       |
| `100010`       |    6     | acepta   | acepta   | válida       |
| `00001001`     |    8     | acepta   | acepta   | válida       |
| `000111111010` |    12    | acepta   | acepta   | válida       |
| `100000000110` |    12    | acepta   | acepta   | válida       |
| λ              |    0     | rechaza  | rechaza  | inválida     |
| `1`            |    1     | rechaza  | rechaza  | inválida     |
| `001`          |    3     | rechaza  | rechaza  | inválida     |
| `10011`        |    5     | rechaza  | rechaza  | inválida     |
| `11110000`     |    8     | rechaza  | rechaza  | inválida     |

Cadenas de prueba.

## Lista 3 · Ejercicio 241

**Enunciado.** AFN-λ equivalente a la expresión 0 + 1.

**Clase.** AFN-λ: Tiene transiciones λ, por ejemplo δ(q4, λ) ∋ q0. **Archivos.** `automatas/afnd-lambda/lista3-241.jff` (y `.json`, `.xml`).

**Diseño.** Construcción de Thompson: casos básicos y una construcción por cada operador, de dentro hacia fuera.

| δ     | 0    | 1    | λ        |
|-------|------|------|----------|
| → q4  | ∅    | ∅    | {q0, q2} |
| q0    | {q1} | ∅    | ∅        |
| q1    | ∅    | ∅    | {q5}     |
| q2    | ∅    | {q3} | ∅        |
| q3    | ∅    | ∅    | {q5}     |
| \* q5 | ∅    | ∅    | ∅        |

Tabla de transiciones (→ inicial, \* aceptación, — sin transición).

| Cadena   | Longitud | Esperado | Obtenido | Tipo de caso |
|----------|:--------:|----------|----------|--------------|
| `0`      |    1     | acepta   | acepta   | válida       |
| `1`      |    1     | acepta   | acepta   | válida       |
| λ        |    0     | rechaza  | rechaza  | inválida     |
| `100`    |    3     | rechaza  | rechaza  | inválida     |
| `000010` |    6     | rechaza  | rechaza  | inválida     |
| `001010` |    6     | rechaza  | rechaza  | inválida     |
| `110110` |    6     | rechaza  | rechaza  | inválida     |

Cadenas de prueba.

## Lista 3 · Ejercicio 242

**Enunciado.** AFN-λ equivalente a la expresión 0\* + 1.

**Clase.** AFN-λ: Tiene transiciones λ, por ejemplo δ(q6, λ) ∋ q2. **Archivos.** `automatas/afnd-lambda/lista3-242.jff` (y `.json`, `.xml`).

**Diseño.** Construcción de Thompson: casos básicos y una construcción por cada operador, de dentro hacia fuera.

| δ     | 0    | 1    | λ        |
|-------|------|------|----------|
| → q6  | ∅    | ∅    | {q2, q4} |
| q2    | ∅    | ∅    | {q0, q3} |
| q0    | {q1} | ∅    | ∅        |
| q1    | ∅    | ∅    | {q0, q3} |
| q3    | ∅    | ∅    | {q7}     |
| q4    | ∅    | {q5} | ∅        |
| q5    | ∅    | ∅    | {q7}     |
| \* q7 | ∅    | ∅    | ∅        |

Tabla de transiciones (→ inicial, \* aceptación, — sin transición).

| Cadena       | Longitud | Esperado | Obtenido | Tipo de caso |
|--------------|:--------:|----------|----------|--------------|
| λ            |    0     | acepta   | acepta   | válida       |
| `1`          |    1     | acepta   | acepta   | válida       |
| `000`        |    3     | acepta   | acepta   | válida       |
| `00000`      |    5     | acepta   | acepta   | válida       |
| `00000000`   |    8     | acepta   | acepta   | válida       |
| `10`         |    2     | rechaza  | rechaza  | inválida     |
| `011`        |    3     | rechaza  | rechaza  | inválida     |
| `10001`      |    5     | rechaza  | rechaza  | inválida     |
| `1011100`    |    7     | rechaza  | rechaza  | inválida     |
| `0110011100` |    10    | rechaza  | rechaza  | inválida     |

Cadenas de prueba.

## Lista 3 · Ejercicio 243

**Enunciado.** AFN-λ equivalente a la expresión (0 + 1)\*.

**Clase.** AFN-λ: Tiene transiciones λ, por ejemplo δ(q6, λ) ∋ q4. **Archivos.** `automatas/afnd-lambda/lista3-243.jff` (y `.json`, `.xml`).

**Diseño.** Construcción de Thompson: casos básicos y una construcción por cada operador, de dentro hacia fuera.

| δ     | 0    | 1    | λ        |
|-------|------|------|----------|
| → q6  | ∅    | ∅    | {q4, q7} |
| q4    | ∅    | ∅    | {q0, q2} |
| q0    | {q1} | ∅    | ∅        |
| q1    | ∅    | ∅    | {q5}     |
| q2    | ∅    | {q3} | ∅        |
| q3    | ∅    | ∅    | {q5}     |
| q5    | ∅    | ∅    | {q4, q7} |
| \* q7 | ∅    | ∅    | ∅        |

Tabla de transiciones (→ inicial, \* aceptación, — sin transición).

| Cadena     | Longitud | Esperado | Obtenido | Tipo de caso |
|------------|:--------:|----------|----------|--------------|
| λ          |    0     | acepta   | acepta   | válida       |
| `0`        |    1     | acepta   | acepta   | válida       |
| `001`      |    3     | acepta   | acepta   | válida       |
| `11011`    |    5     | acepta   | acepta   | válida       |
| `10010111` |    8     | acepta   | acepta   | válida       |

Cadenas de prueba.

## Lista 3 · Ejercicio 244

**Enunciado.** AFN-λ equivalente a la expresión 0(0 + 1).

**Clase.** AFN-λ: Tiene transiciones λ, por ejemplo δ(q1, λ) ∋ q6. **Archivos.** `automatas/afnd-lambda/lista3-244.jff` (y `.json`, `.xml`).

**Diseño.** Construcción de Thompson: casos básicos y una construcción por cada operador, de dentro hacia fuera.

| δ     | 0    | 1    | λ        |
|-------|------|------|----------|
| → q0  | {q1} | ∅    | ∅        |
| q1    | ∅    | ∅    | {q6}     |
| q6    | ∅    | ∅    | {q2, q4} |
| q2    | {q3} | ∅    | ∅        |
| q3    | ∅    | ∅    | {q7}     |
| q4    | ∅    | {q5} | ∅        |
| q5    | ∅    | ∅    | {q7}     |
| \* q7 | ∅    | ∅    | ∅        |

Tabla de transiciones (→ inicial, \* aceptación, — sin transición).

| Cadena     | Longitud | Esperado | Obtenido | Tipo de caso |
|------------|:--------:|----------|----------|--------------|
| `00`       |    2     | acepta   | acepta   | válida       |
| `01`       |    2     | acepta   | acepta   | válida       |
| λ          |    0     | rechaza  | rechaza  | inválida     |
| `1`        |    1     | rechaza  | rechaza  | inválida     |
| `100`      |    3     | rechaza  | rechaza  | inválida     |
| `11010`    |    5     | rechaza  | rechaza  | inválida     |
| `01110100` |    8     | rechaza  | rechaza  | inválida     |

Cadenas de prueba.

## Lista 3 · Ejercicio 245

**Enunciado.** AFN-λ equivalente a la expresión 0(0 + 1)\*.

**Clase.** AFN-λ: Tiene transiciones λ, por ejemplo δ(q1, λ) ∋ q8. **Archivos.** `automatas/afnd-lambda/lista3-245.jff` (y `.json`, `.xml`).

**Diseño.** Construcción de Thompson: casos básicos y una construcción por cada operador, de dentro hacia fuera.

| δ     | 0    | 1    | λ        |
|-------|------|------|----------|
| → q0  | {q1} | ∅    | ∅        |
| q1    | ∅    | ∅    | {q8}     |
| q8    | ∅    | ∅    | {q6, q9} |
| q6    | ∅    | ∅    | {q2, q4} |
| q2    | {q3} | ∅    | ∅        |
| q3    | ∅    | ∅    | {q7}     |
| q4    | ∅    | {q5} | ∅        |
| q5    | ∅    | ∅    | {q7}     |
| q7    | ∅    | ∅    | {q6, q9} |
| \* q9 | ∅    | ∅    | ∅        |

Tabla de transiciones (→ inicial, \* aceptación, — sin transición).

| Cadena      | Longitud | Esperado | Obtenido | Tipo de caso |
|-------------|:--------:|----------|----------|--------------|
| `0`         |    1     | acepta   | acepta   | válida       |
| `01`        |    2     | acepta   | acepta   | válida       |
| `0000`      |    4     | acepta   | acepta   | válida       |
| `001110`    |    6     | acepta   | acepta   | válida       |
| `011001010` |    9     | acepta   | acepta   | válida       |
| λ           |    0     | rechaza  | rechaza  | inválida     |
| `1`         |    1     | rechaza  | rechaza  | inválida     |
| `110`       |    3     | rechaza  | rechaza  | inválida     |
| `11100`     |    5     | rechaza  | rechaza  | inválida     |
| `10000111`  |    8     | rechaza  | rechaza  | inválida     |

Cadenas de prueba.

## Lista 3 · Ejercicio 246

**Enunciado.** AFN-λ equivalente a la expresión 0\*(0 + 1).

**Clase.** AFN-λ: Tiene transiciones λ, por ejemplo δ(q2, λ) ∋ q0. **Archivos.** `automatas/afnd-lambda/lista3-246.jff` (y `.json`, `.xml`).

**Diseño.** Construcción de Thompson: casos básicos y una construcción por cada operador, de dentro hacia fuera.

| δ     | 0    | 1    | λ        |
|-------|------|------|----------|
| → q2  | ∅    | ∅    | {q0, q3} |
| q0    | {q1} | ∅    | ∅        |
| q1    | ∅    | ∅    | {q0, q3} |
| q3    | ∅    | ∅    | {q8}     |
| q8    | ∅    | ∅    | {q4, q6} |
| q4    | {q5} | ∅    | ∅        |
| q5    | ∅    | ∅    | {q9}     |
| q6    | ∅    | {q7} | ∅        |
| q7    | ∅    | ∅    | {q9}     |
| \* q9 | ∅    | ∅    | ∅        |

Tabla de transiciones (→ inicial, \* aceptación, — sin transición).

| Cadena        | Longitud | Esperado | Obtenido | Tipo de caso                 |
|---------------|:--------:|----------|----------|------------------------------|
| `1`           |    1     | acepta   | acepta   | válida                       |
| `00`          |    2     | acepta   | acepta   | válida                       |
| `0000`        |    4     | acepta   | acepta   | válida                       |
| `000000`      |    6     | acepta   | acepta   | válida                       |
| `000000000`   |    9     | acepta   | acepta   | válida                       |
| λ             |    0     | rechaza  | rechaza  | inválida                     |
| `0000011`     |    7     | rechaza  | rechaza  | inválida                     |
| `0000100`     |    7     | rechaza  | rechaza  | inválida                     |
| `1110010101`  |    10    | rechaza  | rechaza  | inválida                     |
| `01010111101` |    11    | rechaza  | rechaza  | inválida                     |
| `0`           |    1     | acepta   | acepta   | frontera: aceptada más corta |

Cadenas de prueba.

## Lista 3 · Ejercicio 247

**Enunciado.** AFN-λ equivalente a la expresión (01)\* + 1\*.

**Clase.** AFN-λ: Tiene transiciones λ, por ejemplo δ(q10, λ) ∋ q4. **Archivos.** `automatas/afnd-lambda/lista3-247.jff` (y `.json`, `.xml`).

**Diseño.** Construcción de Thompson: casos básicos y una construcción por cada operador, de dentro hacia fuera.

| δ      | 0    | 1    | λ        |
|--------|------|------|----------|
| → q10  | ∅    | ∅    | {q4, q8} |
| q4     | ∅    | ∅    | {q0, q5} |
| q0     | {q1} | ∅    | ∅        |
| q1     | ∅    | ∅    | {q2}     |
| q2     | ∅    | {q3} | ∅        |
| q3     | ∅    | ∅    | {q0, q5} |
| q5     | ∅    | ∅    | {q11}    |
| q8     | ∅    | ∅    | {q6, q9} |
| q6     | ∅    | {q7} | ∅        |
| q7     | ∅    | ∅    | {q6, q9} |
| q9     | ∅    | ∅    | {q11}    |
| \* q11 | ∅    | ∅    | ∅        |

Tabla de transiciones (→ inicial, \* aceptación, — sin transición).

| Cadena      | Longitud | Esperado | Obtenido | Tipo de caso |
|-------------|:--------:|----------|----------|--------------|
| λ           |    0     | acepta   | acepta   | válida       |
| `1`         |    1     | acepta   | acepta   | válida       |
| `111`       |    3     | acepta   | acepta   | válida       |
| `11111`     |    5     | acepta   | acepta   | válida       |
| `01010101`  |    8     | acepta   | acepta   | válida       |
| `0`         |    1     | rechaza  | rechaza  | inválida     |
| `00`        |    2     | rechaza  | rechaza  | inválida     |
| `0000`      |    4     | rechaza  | rechaza  | inválida     |
| `101001`    |    6     | rechaza  | rechaza  | inválida     |
| `110001011` |    9     | rechaza  | rechaza  | inválida     |

Cadenas de prueba.

## Lista 3 · Ejercicio 248

**Enunciado.** AFN-λ equivalente a la expresión (0\* + 1)0.

**Clase.** AFN-λ: Tiene transiciones λ, por ejemplo δ(q6, λ) ∋ q2. **Archivos.** `automatas/afnd-lambda/lista3-248.jff` (y `.json`, `.xml`).

**Diseño.** Construcción de Thompson: casos básicos y una construcción por cada operador, de dentro hacia fuera.

| δ     | 0    | 1    | λ        |
|-------|------|------|----------|
| → q6  | ∅    | ∅    | {q2, q4} |
| q2    | ∅    | ∅    | {q0, q3} |
| q0    | {q1} | ∅    | ∅        |
| q1    | ∅    | ∅    | {q0, q3} |
| q3    | ∅    | ∅    | {q7}     |
| q4    | ∅    | {q5} | ∅        |
| q5    | ∅    | ∅    | {q7}     |
| q7    | ∅    | ∅    | {q8}     |
| q8    | {q9} | ∅    | ∅        |
| \* q9 | ∅    | ∅    | ∅        |

Tabla de transiciones (→ inicial, \* aceptación, — sin transición).

| Cadena      | Longitud | Esperado | Obtenido | Tipo de caso |
|-------------|:--------:|----------|----------|--------------|
| `0`         |    1     | acepta   | acepta   | válida       |
| `00`        |    2     | acepta   | acepta   | válida       |
| `0000`      |    4     | acepta   | acepta   | válida       |
| `000000`    |    6     | acepta   | acepta   | válida       |
| `000000000` |    9     | acepta   | acepta   | válida       |
| λ           |    0     | rechaza  | rechaza  | inválida     |
| `1`         |    1     | rechaza  | rechaza  | inválida     |
| `110`       |    3     | rechaza  | rechaza  | inválida     |
| `01011`     |    5     | rechaza  | rechaza  | inválida     |
| `10010000`  |    8     | rechaza  | rechaza  | inválida     |

Cadenas de prueba.

## Lista 3 · Ejercicio 249

**Enunciado.** AFN-λ equivalente a la expresión (0\* + 1)0\*.

**Clase.** AFN-λ: Tiene transiciones λ, por ejemplo δ(q6, λ) ∋ q2. **Archivos.** `automatas/afnd-lambda/lista3-249.jff` (y `.json`, `.xml`).

**Diseño.** Construcción de Thompson: casos básicos y una construcción por cada operador, de dentro hacia fuera.

| δ      | 0    | 1    | λ         |
|--------|------|------|-----------|
| → q6   | ∅    | ∅    | {q2, q4}  |
| q2     | ∅    | ∅    | {q0, q3}  |
| q0     | {q1} | ∅    | ∅         |
| q1     | ∅    | ∅    | {q0, q3}  |
| q3     | ∅    | ∅    | {q7}      |
| q4     | ∅    | {q5} | ∅         |
| q5     | ∅    | ∅    | {q7}      |
| q7     | ∅    | ∅    | {q10}     |
| q10    | ∅    | ∅    | {q8, q11} |
| q8     | {q9} | ∅    | ∅         |
| q9     | ∅    | ∅    | {q8, q11} |
| \* q11 | ∅    | ∅    | ∅         |

Tabla de transiciones (→ inicial, \* aceptación, — sin transición).

| Cadena       | Longitud | Esperado | Obtenido | Tipo de caso |
|--------------|:--------:|----------|----------|--------------|
| λ            |    0     | acepta   | acepta   | válida       |
| `1`          |    1     | acepta   | acepta   | válida       |
| `000`        |    3     | acepta   | acepta   | válida       |
| `00000`      |    5     | acepta   | acepta   | válida       |
| `10000000`   |    8     | acepta   | acepta   | válida       |
| `11`         |    2     | rechaza  | rechaza  | inválida     |
| `110`        |    3     | rechaza  | rechaza  | inválida     |
| `11110`      |    5     | rechaza  | rechaza  | inválida     |
| `1100101`    |    7     | rechaza  | rechaza  | inválida     |
| `0100110101` |    10    | rechaza  | rechaza  | inválida     |

Cadenas de prueba.

## Lista 3 · Ejercicio 250

**Enunciado.** AFN-λ equivalente a la expresión 0*1* + 1\*0.

**Clase.** AFN-λ: Tiene transiciones λ, por ejemplo δ(q14, λ) ∋ q2. **Archivos.** `automatas/afnd-lambda/lista3-250.jff` (y `.json`, `.xml`).

**Diseño.** Construcción de Thompson: casos básicos y una construcción por cada operador, de dentro hacia fuera.

| δ      | 0     | 1    | λ         |
|--------|-------|------|-----------|
| → q14  | ∅     | ∅    | {q2, q10} |
| q2     | ∅     | ∅    | {q0, q3}  |
| q0     | {q1}  | ∅    | ∅         |
| q1     | ∅     | ∅    | {q0, q3}  |
| q3     | ∅     | ∅    | {q6}      |
| q6     | ∅     | ∅    | {q4, q7}  |
| q4     | ∅     | {q5} | ∅         |
| q5     | ∅     | ∅    | {q4, q7}  |
| q7     | ∅     | ∅    | {q15}     |
| q10    | ∅     | ∅    | {q8, q11} |
| q8     | ∅     | {q9} | ∅         |
| q9     | ∅     | ∅    | {q8, q11} |
| q11    | ∅     | ∅    | {q12}     |
| q12    | {q13} | ∅    | ∅         |
| q13    | ∅     | ∅    | {q15}     |
| \* q15 | ∅     | ∅    | ∅         |

Tabla de transiciones (→ inicial, \* aceptación, — sin transición).

| Cadena        | Longitud | Esperado | Obtenido | Tipo de caso |
|---------------|:--------:|----------|----------|--------------|
| λ             |    0     | acepta   | acepta   | válida       |
| `0`           |    1     | acepta   | acepta   | válida       |
| `011`         |    3     | acepta   | acepta   | válida       |
| `00011`       |    5     | acepta   | acepta   | válida       |
| `01111111`    |    8     | acepta   | acepta   | válida       |
| `100`         |    3     | rechaza  | rechaza  | inválida     |
| `1010`        |    4     | rechaza  | rechaza  | inválida     |
| `100000`      |    6     | rechaza  | rechaza  | inválida     |
| `11001110`    |    8     | rechaza  | rechaza  | inválida     |
| `10111100000` |    11    | rechaza  | rechaza  | inválida     |

Cadenas de prueba.

## Lista 3 · Ejercicio 251

**Enunciado.** AFN-λ equivalente a la expresión (0 + 1*)0 + 1*1.

**Clase.** AFN-λ: Tiene transiciones λ, por ejemplo δ(q16, λ) ∋ q6. **Archivos.** `automatas/afnd-lambda/lista3-251.jff` (y `.json`, `.xml`).

**Diseño.** Construcción de Thompson: casos básicos y una construcción por cada operador, de dentro hacia fuera.

| δ      | 0    | 1     | λ          |
|--------|------|-------|------------|
| → q16  | ∅    | ∅     | {q6, q12}  |
| q6     | ∅    | ∅     | {q0, q4}   |
| q0     | {q1} | ∅     | ∅          |
| q1     | ∅    | ∅     | {q7}       |
| q4     | ∅    | ∅     | {q2, q5}   |
| q2     | ∅    | {q3}  | ∅          |
| q3     | ∅    | ∅     | {q2, q5}   |
| q5     | ∅    | ∅     | {q7}       |
| q7     | ∅    | ∅     | {q8}       |
| q8     | {q9} | ∅     | ∅          |
| q9     | ∅    | ∅     | {q17}      |
| q12    | ∅    | ∅     | {q10, q13} |
| q10    | ∅    | {q11} | ∅          |
| q11    | ∅    | ∅     | {q10, q13} |
| q13    | ∅    | ∅     | {q14}      |
| q14    | ∅    | {q15} | ∅          |
| q15    | ∅    | ∅     | {q17}      |
| \* q17 | ∅    | ∅     | ∅          |

Tabla de transiciones (→ inicial, \* aceptación, — sin transición).

| Cadena           | Longitud | Esperado | Obtenido | Tipo de caso |
|------------------|:--------:|----------|----------|--------------|
| `0`              |    1     | acepta   | acepta   | válida       |
| `11`             |    2     | acepta   | acepta   | válida       |
| `1111`           |    4     | acepta   | acepta   | válida       |
| `111111`         |    6     | acepta   | acepta   | válida       |
| `111111110`      |    9     | acepta   | acepta   | válida       |
| λ                |    0     | rechaza  | rechaza  | inválida     |
| `01`             |    2     | rechaza  | rechaza  | inválida     |
| `010111`         |    6     | rechaza  | rechaza  | inválida     |
| `11001100100`    |    11    | rechaza  | rechaza  | inválida     |
| `10110011110010` |    14    | rechaza  | rechaza  | inválida     |

Cadenas de prueba.

## Lista 3 · Ejercicio 252

**Enunciado.** AFN-λ equivalente a la expresión (0 + 1)*(00 + 11) + (00 + 11)(0 + 1)*.

**Clase.** AFN-λ: Tiene transiciones λ, por ejemplo δ(q36, λ) ∋ q6. **Archivos.** `automatas/afnd-lambda/lista3-252.jff` (y `.json`, `.xml`).

**Diseño.** Construcción de Thompson: casos básicos y una construcción por cada operador, de dentro hacia fuera.

| δ      | 0     | 1     | λ          |
|--------|-------|-------|------------|
| → q36  | ∅     | ∅     | {q6, q26}  |
| q6     | ∅     | ∅     | {q4, q7}   |
| q4     | ∅     | ∅     | {q0, q2}   |
| q0     | {q1}  | ∅     | ∅          |
| q1     | ∅     | ∅     | {q5}       |
| q2     | ∅     | {q3}  | ∅          |
| q3     | ∅     | ∅     | {q5}       |
| q5     | ∅     | ∅     | {q4, q7}   |
| q7     | ∅     | ∅     | {q16}      |
| q16    | ∅     | ∅     | {q8, q12}  |
| q8     | {q9}  | ∅     | ∅          |
| q9     | ∅     | ∅     | {q10}      |
| q10    | {q11} | ∅     | ∅          |
| q11    | ∅     | ∅     | {q17}      |
| q12    | ∅     | {q13} | ∅          |
| q13    | ∅     | ∅     | {q14}      |
| q14    | ∅     | {q15} | ∅          |
| q15    | ∅     | ∅     | {q17}      |
| q17    | ∅     | ∅     | {q37}      |
| q26    | ∅     | ∅     | {q18, q22} |
| q18    | {q19} | ∅     | ∅          |
| q19    | ∅     | ∅     | {q20}      |
| q20    | {q21} | ∅     | ∅          |
| q21    | ∅     | ∅     | {q27}      |
| q22    | ∅     | {q23} | ∅          |
| q23    | ∅     | ∅     | {q24}      |
| q24    | ∅     | {q25} | ∅          |
| q25    | ∅     | ∅     | {q27}      |
| q27    | ∅     | ∅     | {q34}      |
| q34    | ∅     | ∅     | {q32, q35} |
| q32    | ∅     | ∅     | {q28, q30} |
| q28    | {q29} | ∅     | ∅          |
| q29    | ∅     | ∅     | {q33}      |
| q30    | ∅     | {q31} | ∅          |
| q31    | ∅     | ∅     | {q33}      |
| q33    | ∅     | ∅     | {q32, q35} |
| q35    | ∅     | ∅     | {q37}      |
| \* q37 | ∅     | ∅     | ∅          |

Tabla de transiciones (→ inicial, \* aceptación, — sin transición).

| Cadena       | Longitud | Esperado | Obtenido | Tipo de caso |
|--------------|:--------:|----------|----------|--------------|
| `00`         |    2     | acepta   | acepta   | válida       |
| `110`        |    3     | acepta   | acepta   | válida       |
| `01111`      |    5     | acepta   | acepta   | válida       |
| `1101100`    |    7     | acepta   | acepta   | válida       |
| `0000100110` |    10    | acepta   | acepta   | válida       |
| λ            |    0     | rechaza  | rechaza  | inválida     |
| `1`          |    1     | rechaza  | rechaza  | inválida     |
| `010`        |    3     | rechaza  | rechaza  | inválida     |
| `01001`      |    5     | rechaza  | rechaza  | inválida     |
| `01110101`   |    8     | rechaza  | rechaza  | inválida     |

Cadenas de prueba.

## Lista 3 · Ejercicio 253

**Enunciado.** AFN-λ equivalente a la expresión (0 + (11 + 00)*)(11 + 10 + 01)*(λ + 110).

**Clase.** AFN-λ: Tiene transiciones λ, por ejemplo δ(q14, λ) ∋ q0. **Archivos.** `automatas/afnd-lambda/lista3-253.jff` (y `.json`, `.xml`).

**Diseño.** Construcción de Thompson: casos básicos y una construcción por cada operador, de dentro hacia fuera.

| δ      | 0     | 1     | λ          |
|--------|-------|-------|------------|
| → q14  | ∅     | ∅     | {q0, q12}  |
| q0     | {q1}  | ∅     | ∅          |
| q1     | ∅     | ∅     | {q15}      |
| q12    | ∅     | ∅     | {q10, q13} |
| q10    | ∅     | ∅     | {q2, q6}   |
| q2     | ∅     | {q3}  | ∅          |
| q3     | ∅     | ∅     | {q4}       |
| q4     | ∅     | {q5}  | ∅          |
| q5     | ∅     | ∅     | {q11}      |
| q6     | {q7}  | ∅     | ∅          |
| q7     | ∅     | ∅     | {q8}       |
| q8     | {q9}  | ∅     | ∅          |
| q9     | ∅     | ∅     | {q11}      |
| q11    | ∅     | ∅     | {q10, q13} |
| q13    | ∅     | ∅     | {q15}      |
| q15    | ∅     | ∅     | {q32}      |
| q32    | ∅     | ∅     | {q30, q33} |
| q30    | ∅     | ∅     | {q24, q26} |
| q24    | ∅     | ∅     | {q16, q20} |
| q16    | ∅     | {q17} | ∅          |
| q17    | ∅     | ∅     | {q18}      |
| q18    | ∅     | {q19} | ∅          |
| q19    | ∅     | ∅     | {q25}      |
| q20    | ∅     | {q21} | ∅          |
| q21    | ∅     | ∅     | {q22}      |
| q22    | {q23} | ∅     | ∅          |
| q23    | ∅     | ∅     | {q25}      |
| q25    | ∅     | ∅     | {q31}      |
| q26    | {q27} | ∅     | ∅          |
| q27    | ∅     | ∅     | {q28}      |
| q28    | ∅     | {q29} | ∅          |
| q29    | ∅     | ∅     | {q31}      |
| q31    | ∅     | ∅     | {q30, q33} |
| q33    | ∅     | ∅     | {q42}      |
| q42    | ∅     | ∅     | {q34, q36} |
| q34    | ∅     | ∅     | {q35}      |
| q35    | ∅     | ∅     | {q43}      |
| q36    | ∅     | {q37} | ∅          |
| q37    | ∅     | ∅     | {q38}      |
| q38    | ∅     | {q39} | ∅          |
| q39    | ∅     | ∅     | {q40}      |
| q40    | {q41} | ∅     | ∅          |
| q41    | ∅     | ∅     | {q43}      |
| \* q43 | ∅     | ∅     | ∅          |

Tabla de transiciones (→ inicial, \* aceptación, — sin transición).

| Cadena           | Longitud | Esperado | Obtenido | Tipo de caso |
|------------------|:--------:|----------|----------|--------------|
| λ                |    0     | acepta   | acepta   | válida       |
| `0`              |    1     | acepta   | acepta   | válida       |
| `010`            |    3     | acepta   | acepta   | válida       |
| `01111`          |    5     | acepta   | acepta   | válida       |
| `00011011`       |    8     | acepta   | acepta   | válida       |
| `1`              |    1     | rechaza  | rechaza  | inválida     |
| `111`            |    3     | rechaza  | rechaza  | inválida     |
| `0111001000`     |    10    | rechaza  | rechaza  | inválida     |
| `0110110000000`  |    13    | rechaza  | rechaza  | inválida     |
| `00101011100000` |    14    | rechaza  | rechaza  | inválida     |

Cadenas de prueba.

## Lista 3 · Ejercicio 254

**Enunciado.** Expresión regular para el autómata de la tabla 254.

**Clase.** AFD: Cada par (estado, símbolo) tiene a lo sumo un destino y no hay transiciones λ. **Archivos.** `automatas/afd/lista3-254.jff` (y `.json`, `.xml`).

**Diseño.** Eliminación de estados sobre el autómata generalizado (inicial S y final F nuevos), en el orden de Q.

| δ    | 0   | 1   |
|------|-----|-----|
| → A  | A   | B   |
| \* B | A   | B   |

Tabla de transiciones (→ inicial, \* aceptación, — sin transición).

| Cadena      | Longitud | Esperado | Obtenido | Tipo de caso |
|-------------|:--------:|----------|----------|--------------|
| `1`         |    1     | acepta   | acepta   | válida       |
| `01`        |    2     | acepta   | acepta   | válida       |
| `0001`      |    4     | acepta   | acepta   | válida       |
| `101001`    |    6     | acepta   | acepta   | válida       |
| `001101101` |    9     | acepta   | acepta   | válida       |
| λ           |    0     | rechaza  | rechaza  | inválida     |
| `0`         |    1     | rechaza  | rechaza  | inválida     |
| `010`       |    3     | rechaza  | rechaza  | inválida     |
| `10000`     |    5     | rechaza  | rechaza  | inválida     |
| `10101000`  |    8     | rechaza  | rechaza  | inválida     |

Cadenas de prueba.

## Lista 3 · Ejercicio 255

**Enunciado.** Expresión regular para el autómata de la tabla 255.

**Clase.** AFD: Cada par (estado, símbolo) tiene a lo sumo un destino y no hay transiciones λ. **Archivos.** `automatas/afd/lista3-255.jff` (y `.json`, `.xml`).

**Diseño.** Eliminación de estados sobre el autómata generalizado (inicial S y final F nuevos), en el orden de Q.

| δ     | 0   | 1   |
|-------|-----|-----|
| →\* A | B   | B   |
| B     | A   | B   |

Tabla de transiciones (→ inicial, \* aceptación, — sin transición).

| Cadena          | Longitud | Esperado | Obtenido | Tipo de caso |
|-----------------|:--------:|----------|----------|--------------|
| λ               |    0     | acepta   | acepta   | válida       |
| `00`            |    2     | acepta   | acepta   | válida       |
| `1111010`       |    7     | acepta   | acepta   | válida       |
| `0100001010`    |    10    | acepta   | acepta   | válida       |
| `0010111110110` |    13    | acepta   | acepta   | válida       |
| `1`             |    1     | rechaza  | rechaza  | inválida     |
| `01`            |    2     | rechaza  | rechaza  | inválida     |
| `1101`          |    4     | rechaza  | rechaza  | inválida     |
| `101111`        |    6     | rechaza  | rechaza  | inválida     |
| `111101101`     |    9     | rechaza  | rechaza  | inválida     |

Cadenas de prueba.

## Lista 3 · Ejercicio 256

**Enunciado.** Expresión regular para el autómata de la tabla 256.

**Clase.** AFD: Cada par (estado, símbolo) tiene a lo sumo un destino y no hay transiciones λ. **Archivos.** `automatas/afd/lista3-256.jff` (y `.json`, `.xml`).

**Diseño.** Eliminación de estados sobre el autómata generalizado (inicial S y final F nuevos), en el orden de Q.

| δ    | 0   | 1   | 2   |
|------|-----|-----|-----|
| → A  | B   | A   | A   |
| \* B | B   | B   | A   |

Tabla de transiciones (→ inicial, \* aceptación, — sin transición).

| Cadena      | Longitud | Esperado | Obtenido | Tipo de caso |
|-------------|:--------:|----------|----------|--------------|
| `0`         |    1     | acepta   | acepta   | válida       |
| `01`        |    2     | acepta   | acepta   | válida       |
| `0000`      |    4     | acepta   | acepta   | válida       |
| `201210`    |    6     | acepta   | acepta   | válida       |
| `121101000` |    9     | acepta   | acepta   | válida       |
| λ           |    0     | rechaza  | rechaza  | inválida     |
| `2`         |    1     | rechaza  | rechaza  | inválida     |
| `202`       |    3     | rechaza  | rechaza  | inválida     |
| `21112`     |    5     | rechaza  | rechaza  | inválida     |
| `01211211`  |    8     | rechaza  | rechaza  | inválida     |

Cadenas de prueba.

## Lista 3 · Ejercicio 257

**Enunciado.** Expresión regular para el autómata de la tabla 257.

**Clase.** AFD: Cada par (estado, símbolo) tiene a lo sumo un destino y no hay transiciones λ. **Archivos.** `automatas/afd/lista3-257.jff` (y `.json`, `.xml`).

**Diseño.** Eliminación de estados sobre el autómata generalizado (inicial S y final F nuevos), en el orden de Q.

| δ    | 0   | 1   |
|------|-----|-----|
| → A  | B   | C   |
| \* B | C   | B   |
| \* C | A   | A   |

Tabla de transiciones (→ inicial, \* aceptación, — sin transición).

| Cadena           | Longitud | Esperado | Obtenido | Tipo de caso |
|------------------|:--------:|----------|----------|--------------|
| `0`              |    1     | acepta   | acepta   | válida       |
| `00`             |    2     | acepta   | acepta   | válida       |
| `1101`           |    4     | acepta   | acepta   | válida       |
| `010001`         |    6     | acepta   | acepta   | válida       |
| `111100101`      |    9     | acepta   | acepta   | válida       |
| λ                |    0     | rechaza  | rechaza  | inválida     |
| `001`            |    3     | rechaza  | rechaza  | inválida     |
| `00010001`       |    8     | rechaza  | rechaza  | inválida     |
| `101101101`      |    9     | rechaza  | rechaza  | inválida     |
| `01010011001101` |    14    | rechaza  | rechaza  | inválida     |

Cadenas de prueba.

## Lista 3 · Ejercicio 258

**Enunciado.** Expresión regular para el autómata de la tabla 258.

**Clase.** AFD: Cada par (estado, símbolo) tiene a lo sumo un destino y no hay transiciones λ. **Archivos.** `automatas/afd/lista3-258.jff` (y `.json`, `.xml`).

**Diseño.** Eliminación de estados sobre el autómata generalizado (inicial S y final F nuevos), en el orden de Q.

| δ    | 0   | 1   |
|------|-----|-----|
| → A  | C   | C   |
| B    | A   | C   |
| \* C | B   | A   |

Tabla de transiciones (→ inicial, \* aceptación, — sin transición).

| Cadena           | Longitud | Esperado | Obtenido | Tipo de caso |
|------------------|:--------:|----------|----------|--------------|
| `1`              |    1     | acepta   | acepta   | válida       |
| `01100011`       |    8     | acepta   | acepta   | válida       |
| `1110100010`     |    10    | acepta   | acepta   | válida       |
| `011001000001`   |    12    | acepta   | acepta   | válida       |
| `11100000100110` |    14    | acepta   | acepta   | válida       |
| λ                |    0     | rechaza  | rechaza  | inválida     |
| `0000101`        |    7     | rechaza  | rechaza  | inválida     |
| `00000100`       |    8     | rechaza  | rechaza  | inválida     |
| `100011011`      |    9     | rechaza  | rechaza  | inválida     |
| `011000000101`   |    12    | rechaza  | rechaza  | inválida     |

Cadenas de prueba.

## Lista 3 · Ejercicio 259

**Enunciado.** Valores R_ij^(k) necesarios para R14^(4) y expresión regular del autómata.

**Clase.** AFD: Cada par (estado, símbolo) tiene a lo sumo un destino y no hay transiciones λ. **Archivos.** `automatas/afd/lista3-259.jff` (y `.json`, `.xml`).

**Diseño.** Recurrencia R_ij^(k) = R_ij^(k−1) + R_ik^((k−1)(R_kk)(k−1))\* R_kj^(k−1).

| δ    | a   | b   |
|------|-----|-----|
| → 1  | 3   | 2   |
| 2    | 1   | 3   |
| 3    | 2   | 3   |
| \* 4 | 1   | 4   |

Tabla de transiciones (→ inicial, \* aceptación, — sin transición).

| Cadena     | Longitud | Esperado | Obtenido | Tipo de caso |
|------------|:--------:|----------|----------|--------------|
| λ          |    0     | rechaza  | rechaza  | inválida     |
| `b`        |    1     | rechaza  | rechaza  | inválida     |
| `aba`      |    3     | rechaza  | rechaza  | inválida     |
| `baaba`    |    5     | rechaza  | rechaza  | inválida     |
| `aabaabbb` |    8     | rechaza  | rechaza  | inválida     |

Cadenas de prueba.

## Lista 3 · Ejercicio 260

**Enunciado.** AFD equivalente al AFN de la tabla 260; describa cómo se obtuvo.

**Clase.** AFN: Hay elección: δ(A, 1) = {B, C}. **Archivos.** `automatas/afnd/lista3-260.jff` (y `.json`, `.xml`).

**Diseño.** Construcción de subconjuntos: se parte de {q0} y, para cada subconjunto nuevo y cada símbolo, se reúnen los destinos; sólo se crean subconjuntos alcanzables.

| δ    | 0         | 1      |
|------|-----------|--------|
| → A  | ∅         | {B, C} |
| B    | {A, B, D} | {C, D} |
| C    | {A, C}    | {A, E} |
| \* D | ∅         | {D, E} |
| E    | {A, E}    | ∅      |

Tabla de transiciones (→ inicial, \* aceptación, — sin transición).

| Cadena       | Longitud | Esperado | Obtenido | Tipo de caso |
|--------------|:--------:|----------|----------|--------------|
| `10`         |    2     | acepta   | acepta   | válida       |
| `101`        |    3     | acepta   | acepta   | válida       |
| `10011`      |    5     | acepta   | acepta   | válida       |
| `1001000`    |    7     | acepta   | acepta   | válida       |
| `1000111101` |    10    | acepta   | acepta   | válida       |
| λ            |    0     | rechaza  | rechaza  | inválida     |
| `1`          |    1     | rechaza  | rechaza  | inválida     |
| `011`        |    3     | rechaza  | rechaza  | inválida     |
| `00101`      |    5     | rechaza  | rechaza  | inválida     |
| `00111110`   |    8     | rechaza  | rechaza  | inválida     |

Cadenas de prueba.

## Lista 3 · Ejercicio 261

**Enunciado.** AFD equivalente al AFN de la figura 261 (transcrito).

**Clase.** AFN: Hay elección: δ(q0, 0) = {q0, q1}. **Archivos.** `automatas/afnd/lista3-261.jff` (y `.json`, `.xml`).

**Diseño.** Construcción de subconjuntos: se parte de {q0} y, para cada subconjunto nuevo y cada símbolo, se reúnen los destinos; sólo se crean subconjuntos alcanzables.

| δ     | 0        | 1        |
|-------|----------|----------|
| → q0  | {q0, q1} | {q0, q3} |
| q1    | {q2}     | ∅        |
| \* q2 | ∅        | ∅        |
| q3    | ∅        | {q4}     |
| q4    | ∅        | ∅        |

Tabla de transiciones (→ inicial, \* aceptación, — sin transición).

| Cadena       | Longitud | Esperado | Obtenido | Tipo de caso |
|--------------|:--------:|----------|----------|--------------|
| `00`         |    2     | acepta   | acepta   | válida       |
| `000`        |    3     | acepta   | acepta   | válida       |
| `01000`      |    5     | acepta   | acepta   | válida       |
| `1010000`    |    7     | acepta   | acepta   | válida       |
| `0010100100` |    10    | acepta   | acepta   | válida       |
| λ            |    0     | rechaza  | rechaza  | inválida     |
| `0`          |    1     | rechaza  | rechaza  | inválida     |
| `010`        |    3     | rechaza  | rechaza  | inválida     |
| `01111`      |    5     | rechaza  | rechaza  | inválida     |
| `01101001`   |    8     | rechaza  | rechaza  | inválida     |

Cadenas de prueba.

## Lista 3 · Ejercicio 262

**Enunciado.** Diseñe un AFN que acepte {ab, ba} y obtenga un AFD.

**Clase.** AFD: Cada par (estado, símbolo) tiene a lo sumo un destino y no hay transiciones λ. **Archivos.** `automatas/afd/lista3-262.jff` (y `.json`, `.xml`).

**Diseño.** Construcción de subconjuntos: se parte de {q0} y, para cada subconjunto nuevo y cada símbolo, se reúnen los destinos; sólo se crean subconjuntos alcanzables. El AFN tiene dos ramas desde q0, una por palabra.

| δ     | a   | b   |
|-------|-----|-----|
| → q0  | q1  | q3  |
| q1    | —   | q2  |
| \* q2 | —   | —   |
| q3    | q4  | —   |
| \* q4 | —   | —   |

Tabla de transiciones (→ inicial, \* aceptación, — sin transición).

| Cadena     | Longitud | Esperado | Obtenido | Tipo de caso                                     |
|------------|:--------:|----------|----------|--------------------------------------------------|
| `ab`       |    2     | acepta   | acepta   | válida                                           |
| `ba`       |    2     | acepta   | acepta   | válida                                           |
| λ          |    0     | rechaza  | rechaza  | inválida                                         |
| `a`        |    1     | rechaza  | rechaza  | inválida                                         |
| `bba`      |    3     | rechaza  | rechaza  | inválida                                         |
| `aaaba`    |    5     | rechaza  | rechaza  | inválida                                         |
| `babbaaaa` |    8     | rechaza  | rechaza  | inválida                                         |
| `b`        |    1     | rechaza  | rechaza  | frontera: justo por debajo de la longitud mínima |

Cadenas de prueba.

## Lista 3 · Ejercicio 263

**Enunciado.** AFD equivalente al AFN de la figura 263 (transcrito).

**Clase.** AFN: Hay elección: δ(q0, 0) = {q0, q1}. **Archivos.** `automatas/afnd/lista3-263.jff` (y `.json`, `.xml`).

**Diseño.** Construcción de subconjuntos: se parte de {q0} y, para cada subconjunto nuevo y cada símbolo, se reúnen los destinos; sólo se crean subconjuntos alcanzables.

| δ     | 0        | 1    |
|-------|----------|------|
| → q0  | {q0, q1} | {q0} |
| q1    | ∅        | {q2} |
| \* q2 | ∅        | ∅    |

Tabla de transiciones (→ inicial, \* aceptación, — sin transición).

| Cadena       | Longitud | Esperado | Obtenido | Tipo de caso |
|--------------|:--------:|----------|----------|--------------|
| `01`         |    2     | acepta   | acepta   | válida       |
| `001`        |    3     | acepta   | acepta   | válida       |
| `00001`      |    5     | acepta   | acepta   | válida       |
| `1000001`    |    7     | acepta   | acepta   | válida       |
| `0100011001` |    10    | acepta   | acepta   | válida       |
| λ            |    0     | rechaza  | rechaza  | inválida     |
| `0`          |    1     | rechaza  | rechaza  | inválida     |
| `100`        |    3     | rechaza  | rechaza  | inválida     |
| `00011`      |    5     | rechaza  | rechaza  | inválida     |
| `01010010`   |    8     | rechaza  | rechaza  | inválida     |

Cadenas de prueba.
