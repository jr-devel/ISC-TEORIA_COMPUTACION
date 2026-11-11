# Propuesta de trabajo

**Título tentativo.** Validación de datos de formularios con autómatas mínimos: tiempo lineal garantizado y la misma semántica en el cliente y en el servidor.

**Problema.** Los sistemas web validan los datos (correos, CURP, teléfonos, fechas) con expresiones regulares escritas una vez y copiadas entre lenguajes: JavaScript en el navegador y Python o Java en el servidor. Davis et al. (2019) mostraron que cerca del 15 % de las expresiones cambia de significado al pasar de un lenguaje a otro y que muchas tardan un tiempo superlineal en algún motor; un validador que acepta un dato en el navegador y lo rechaza en el servidor, o que se congela con una entrada maliciosa, es un error real. Los formatos de esos campos son, casi siempre, **lenguajes regulares**, así que admiten un modelo formal único: un AFD.

**Clase de máquina.** Con lo visto hasta ahora basta el autómata finito: se escribe la expresión en la notación del curso (sin referencias hacia atrás), se convierte en AFN-λ, se determiniza y se minimiza, y el AFD mínimo se usa como especificación ejecutable en ambos lados. Prevé requerir **autómatas de pila** para los datos con anidamiento, como un objeto JSON o una expresión aritmética en un campo de fórmula, que no son regulares; no prevé máquinas de Turing.

**Sustento.**

- Davis et al. (2019) cuantifican el problema de portabilidad y de rendimiento de las expresiones regulares.
- Moseley et al. (2023) muestran que un motor basado en autómatas puede reemplazar a uno de retroceso en un producto de uso masivo sin perder rendimiento.

**Qué se construiría.** Un generador que reciba un catálogo de formatos en la notación del curso y produzca, para cada uno, el AFD mínimo y su código en JavaScript y en Python (una tabla de transiciones y un ciclo de lectura), más un informe con el número de estados.

**Cómo se comprobaría.** (1) Equivalencia: para cada formato, comparar el AFD con `re.fullmatch` y con el motor de JavaScript sobre miles de cadenas generadas y mutadas, como en las pruebas de esta práctica; cualquier diferencia indica un error de traducción. (2) Tiempo: medir el tiempo de validación contra la longitud de entradas diseñadas para provocar retroceso y comprobar que crece linealmente. (3) Uso: integrarlo en un formulario de prueba y verificar que cliente y servidor dan el mismo veredicto.
