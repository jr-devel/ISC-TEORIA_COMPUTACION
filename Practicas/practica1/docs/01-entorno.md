# Ejercicio 1. Entorno de trabajo: control de versiones y contenedores

## Parte A. Investigación

### Control de versiones

Un sistema de control de versiones registra cada estado de un conjunto de archivos junto con su autor, su fecha y una explicación del cambio, de modo que cualquier versión anterior puede recuperarse o compararse con la actual (Chacon & Straub, 2014, 1). En un equipo resuelve tres problemas que aparecen en cuanto dos personas tocan el mismo proyecto: saber quién cambió qué y por qué, trabajar en paralelo sin sobrescribir el trabajo ajeno y volver atrás cuando un cambio introduce un error. Git es *distribuido*: cada copia del repositorio contiene la historia completa, por lo que se puede confirmar, crear ramas y consultar el historial sin conexión.

**Git y GitHub.** Git es el programa que administra la historia en la computadora de cada persona. GitHub es un servicio en la nube que aloja repositorios Git y añade lo que Git no trae: Pull Requests con revisión, integración continua (GitHub Actions), control de acceso e incidencias. Se puede usar Git sin GitHub, pero GitHub no tiene sentido sin Git.

| Concepto                | Definición                                                                                                                                                   | Ejemplo en esta práctica                                                   |
|-------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------|
| Repositorio             | Carpeta cuya historia completa guarda Git en el subdirectorio oculto `.git`.                                                                                 | `practica1-tc`, con `src/`, `tests/`, `docs/` y `entorno/`.                |
| Confirmación (*commit*) | Fotografía de los archivos preparados, con un mensaje y un identificador único (hash SHA-1).                                                                 | `Agrega el enumerador de Σⁿ con límite de cadenas`.                        |
| Rama (*branch*)         | Puntero móvil a una confirmación; permite desarrollar sin afectar la rama principal.                                                                         | `feature/interfaz`, para la interfaz Flet.                                 |
| Fusión (*merge*)        | Integra en una rama los cambios de otra; si ambas avanzaron, crea una confirmación con dos padres.                                                           | `feature/interfaz` se fusionó en `main`.                                   |
| Conflicto de fusión     | Ocurre cuando las dos ramas modificaron las mismas líneas; Git no elige y marca el archivo con `<<<<<<<`, `=======` y `>>>>>>>` para que una persona decida. | Dos versiones distintas del mensaje de error del límite en `lenguajes.py`. |
| Pull Request            | Solicitud en GitHub para fusionar una rama, con descripción, revisión, comentarios y resultado de las pruebas (GitHub Inc., 2026).                           | «Interfaz con menú lateral y ayuda por sección».                           |
| `.gitignore`            | Lista de patrones de archivos que Git no debe rastrear, normalmente porque se regeneran.                                                                     | `venv/`, `__pycache__/`, `*.pyc`, `salidas/`.                              |
| `README`                | Documento de entrada del repositorio; GitHub lo muestra en la página principal.                                                                              | Portada con datos del alumno, índice e instrucciones.                      |

Términos de control de versiones.

### Contenedores

Un contenedor es un proceso aislado del sistema operativo anfitrión que ve su propio sistema de archivos, su propia red y sus propios procesos, pero **comparte el núcleo** del anfitrión. Una máquina virtual, en cambio, emula hardware completo y arranca su propio sistema operativo sobre un hipervisor. De ahí las tres diferencias que pide la práctica (Felter et al., 2015):

- **Arranque.** Un contenedor inicia en fracciones de segundo, porque sólo lanza un proceso; una máquina virtual tarda lo que tarda en arrancar un sistema operativo.
- **Tamaño.** Una imagen de contenedor contiene únicamente la aplicación y sus bibliotecas (decenas o cientos de MB); una máquina virtual incluye un sistema operativo completo (varios GB).
- **Aislamiento.** La máquina virtual aísla más, porque cada una tiene su propio núcleo; en el contenedor el aislamiento se logra con *namespaces* y *cgroups* del mismo núcleo, que es una frontera más delgada.

Los cuatro términos de Docker que se usan en el ejercicio son (Docker Inc., 2026b): la **imagen**, plantilla de sólo lectura formada por capas (por ejemplo, `python:3.12-slim` más las dependencias); el **contenedor**, una instancia en ejecución de una imagen, con una capa escribible propia; el **volumen**, almacenamiento que vive fuera del ciclo de vida del contenedor y que aquí monta la carpeta del proyecto en `/app` para que los cambios al código se vean sin reconstruir; y el **puerto publicado**, que conecta un puerto del equipo con uno del contenedor (`8550:8550`), necesario para abrir la interfaz desde el navegador.

**Entorno virtual de Python.** Es una carpeta con su propio `site-packages` y enlaces al intérprete que lo creó; aísla las *bibliotecas* de cada proyecto, no el intérprete (Python Software Foundation, 2026b). Por eso un entorno virtual no cambia la versión de Python: `python -m venv` con Python 3.12 siempre produce un entorno 3.12. Para probar tres versiones hacen falta tres intérpretes, y cada contenedor aporta el suyo.

**Por qué fijar la imagen.** `python:latest` apunta a la versión más reciente en el momento de construir; un día es 3.13 y al siguiente 3.14, con lo que la misma receta produce entornos distintos y un fallo puede aparecer sin que nadie haya cambiado el código. `python:3.12-slim` fija la versión menor (y la variante ligera), de modo que la construcción es reproducible; las correcciones de la versión de parche siguen llegando.

## Parte B. Repositorio

El repositorio `practica1-tc` contiene `README.md` (portada con nombre, boleta, grupo, carrera, unidad de aprendizaje, profesor y fecha, índice enlazado e instrucciones), un `.gitignore` que excluye `venv/`, `.venv/`, `__pycache__/`, `*.pyc`, `.pytest_cache/`, `salidas/` y los auxiliares de LaTeX, y que **no** excluye los `.jff`, y la historia de confirmaciones. Se hicieron más de cinco confirmaciones con mensajes en imperativo que dicen qué cambia; la interfaz se desarrolló en la rama `feature/interfaz` y entró a `main` mediante un Pull Request descrito y fusionado.

![Salida de `git log --oneline --graph --all`.](../evidencias/git/git-log-graph.png)

![Pull Request de `feature/interfaz` fusionado en `main`.](../evidencias/git/pull-request.png)

## Parte C. Los tres entornos de Python

### Archivos versionados

El `Dockerfile` (carpeta `entorno/`) es único y recibe la versión como argumento. La tabla explica cada instrucción.

| Instrucción                                                | Función                                                                                                                                            |
|------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| `ARG PYTHON_VERSION=3.12`                                  | Declara el argumento de construcción; `compose.yml` le da 3.11, 3.12 o 3.13. El valor por omisión permite construir la imagen sin Compose.         |
| `FROM python:${PYTHON_VERSION}-slim`                       | Imagen base oficial en su variante ligera, con la versión elegida.                                                                                 |
| `RUN python -m venv /opt/venv`                             | Crea el entorno virtual fuera de `/app`, porque el volumen de Compose reemplaza `/app` con la carpeta del equipo y borraría un entorno creado ahí. |
| `ENV PATH="/opt/venv/bin:$PATH"`                           | Antepone el `bin/` del entorno al `PATH`; equivale a activarlo para todas las órdenes siguientes.                                                  |
| `WORKDIR /app`                                             | Carpeta de trabajo dentro del contenedor.                                                                                                          |
| `COPY requirements.txt .`                                  | Copia sólo la lista de dependencias, para que la capa siguiente se reutilice mientras esa lista no cambie.                                         |
| `RUN pip install … -r requirements.txt`                    | Actualiza pip e instala las versiones fijadas; `--no-cache-dir` evita guardar los paquetes descargados en la imagen.                               |
| `COPY . .`                                                 | Copia el proyecto (útil si se ejecuta sin volumen).                                                                                                |
| `ENV FLET_FORCE_WEB_SERVER=true` y `FLET_SERVER_PORT=8550` | Sin escritorio, Flet se sirve como aplicación web en el puerto 8550.                                                                               |
| `CMD ["python", "src/app.py"]`                             | Orden por omisión: abrir la interfaz.                                                                                                              |

Instrucciones del `Dockerfile`.

`compose.yml` declara los servicios `py311`, `py312` y `py313` con el mismo `Dockerfile` (Docker Inc., 2026a) y distinto `PYTHON_VERSION`; los tres montan la carpeta del proyecto en `/app`, `py311` y `py313` ejecutan `pytest -q` por omisión y sólo `py312` publica el puerto 8550 para la interfaz. `requirements.txt` fija `flet[web]==0.86.5`, `fastapi==0.115.12` y `pytest==8.3.4`. FastAPI se fija porque `flet-web` lo requiere sin acotar su versión y las publicaciones de FastAPI posteriores a la 0.115 eliminaron un parámetro que `flet-web` 0.86.5 todavía usa; sin esa línea la interfaz no arranca en un entorno nuevo.

### Justificación de las versiones

| Servicio | Versión | Motivo                                                                                                                                                                                                                                                          |
|----------|---------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `py311`  | 3.11    | Flet 0.86.5 exige Python ≥ 3.10 (Appveyor Systems Inc., 2026), pero 3.10 llegó al fin de su soporte en octubre de 2026 (Python Software Foundation, 2026a); 3.11 es la más antigua que conserva parches de seguridad (hasta octubre de 2027) y que Flet admite. |
| `py312`  | 3.12    | Versión de referencia del curso; recibe parches de seguridad hasta octubre de 2028. Sirve la interfaz.                                                                                                                                                          |
| `py313`  | 3.13    | Versión estable reciente (soporte hasta octubre de 2029); detecta dependencias de comportamientos que cambiaron.                                                                                                                                                |

Elección de versiones.

### Verificación

Cada contenedor se construye con `docker compose build` y se comprueba con `docker compose run --rm py311 python --version` y sus equivalentes; las salidas son `Python 3.11.x`, `Python 3.12.x` y `Python 3.13.x`.

![`python --version` en los contenedores `py311`, `py312` y `py313`.](../evidencias/docker/python-version.png)
