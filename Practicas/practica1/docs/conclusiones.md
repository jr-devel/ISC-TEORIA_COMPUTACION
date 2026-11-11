# Conclusiones

El entorno de trabajo quedó resuelto antes de escribir la primera línea de lógica: un repositorio con historia, ramas y Pull Requests, y tres contenedores construidos con un único `Dockerfile` que difieren sólo en la versión del intérprete. Fijar la imagen y las dependencias tuvo un efecto concreto: la incompatibilidad entre `flet-web` y las versiones nuevas de FastAPI apareció una sola vez, se resolvió con una línea en `requirements.txt` y no volvió a afectar a ninguno de los tres entornos.

La investigación mostró que las definiciones de la unidad no son convenciones arbitrarias. Que Σ⁰ sea {λ} y no ∅ es lo que hace funcionar las leyes de las potencias, y la diferencia entre Σ\* y Σ⁺ se reduce a λ. La lectura de Turing explicó por qué la tesis de Church-Turing no puede demostrarse, y los artículos recientes, por qué la distinción entre la expresión regular de la teoría y la de los lenguajes de programación tiene consecuencias de seguridad.

En JFLAP, preguntarse qué hay que recordar del prefijo leído redujo casi todos los enunciados a cuatro familias de diseño (conteo modular, búsqueda de patrones, producto y extremos), y comparar cada autómata contra la definición del lenguaje sobre todas las cadenas cortas detectó errores que tres cadenas de prueba no habrían mostrado.

En la aplicación, separar el núcleo de la interfaz permitió probar toda la lógica con 34 pruebas en tres versiones de Python sin abrir una ventana, y calcular el número de cadenas con la fórmula antes de generarlas convirtió el crecimiento exponencial de \|Σ\|ⁿ en un aviso que el usuario ve mientras elige la longitud.
