# Biblioteca PDF
aplicacion web local para organizar, administrar y consultar una biblioteca personal de documentos PDF. El poryecto busca facilitar la clasificacion de libros, su consulta y el seguimiento de la estructura, utilizando uan arquitectura modular y patrones de diseño

##Objetivo
Desarrollar una aplicacon web que permita administrar una biblioteca personal de archivos PDF desde una interfaz sencilla.
La aplicacion permitira:
- Registrar archivos PDF en una biblioteca
- Consultar informacion de cada documento, como nombre y numero de paginas
- Organizar libros mediante grupos, autores y etiquetas
- Buscar y consultar documentos registrados
- Leer archivos PDF desde aplicacion
- Guardar el progreso de lectura
- Consultar el historial de documentos abiertos recientemente

## Tecnologias
| Tecnologia | Uso|
|------------|----|
| Python | Lenguaje principal y logica de la aplicacion|
| Flask | Framework para desarrollar la aplicacion web|
| HTML| Estructura de las paginas|
| CSS | Diseño y presentacion visual|
| JavaScript | Interacciones y funcione del lector |
| SQLite | Almacenamiento de informacion |
| PyMuPDF | Lectura de metadatos, extraccion de texto y analisis de PDF |
| PDF.js | Visualizacion de documentos PDF en el navegador |
| pytest | Pruebas del funcionamiento del sistema |

## Patrones de diseño
Los patrones de diseño se utilizaran para organizar el codigo, separar resonsabilidades y facilitar el mantenimiento del proyecto
| Patron | Aplicacion dentro del proyecto |
|-------|------|
| Factory | Centralizar la creacion y configuracion de la aplicacion Flask |
| Repository | Separar las consultas y operaciones de la base de datos de la logica principal |
| Service Layer | Agrupar las operaciones y reglas de negocio de aplicacion |
| Adapter | Adaptar PyMuPDF a una interfaz propia para trabajar con documentos PDF |
| Strategy | Se considerara cuando existan diferentes metodos intercambiables para realizar una misma operacion |

## Estructura del proyecto
biblioteca_pdf/
- ejecutar.py
- configuracion.py
- requisitos.txt
- README.md
- aplicacion/
  - __init__.py
  - rutas/
    - __init__.py
    - libros.py
    - grupos.py
    - biblioteca.py
    - lector.py
  - modelos/
    - __init__.py
    - libro.py
    - grupo.py
    - autor.py
    - progreso.py
  - repositorios/
    - __init__.py
    - repositorio_base.py
    - repositorio_libros.py
    - repositorio_grupos.py
    - repositorio_autores.py
  - servicios/
    - __init__.py
    - servicio_libros.py
    - servicio_pdf.py
    - servicio_busqueda.py
    - servicio_historial.py
    - servicio_progreso.py
  - infraestructura/
    - __init__.py
    - base_datos/
      - _ _ init _ _.py
      - conexion.py
      - esquema.sql
    - documentos/
      - _ _ init _ _.py
      - lector_pdf.py
      - adaptador_pymupdf.py
  - estructuras/
    - _ _ init _ _.py
    - lista_enlazada.py
  - plantillas/
    - base.html
    - inicio.html
    - biblioteca.html
    - detalle_libro.html
    - lector.html
    - grupos.html
  - archivos_estaticos/
    - css/
      - estilo.css
      - biblioteca.css
      - lector.css
    - js/
      - principal.js
      - biblioteca.js
      - lector.js
    - imagenes/
- datos/
  - biblioteca.db
- documentos/
  - libros/
  - portadas/
- pruebas/
  - test_libros.py
  - test_repositorios.py
  - test_pdf.py
  - test_progreso.py

### Responsabilidades de las carpetas

-__ruta:__ recibe las solicitudes del navegador y conecta las paginas con los servicios
- __modelos:__ representa las entidades principales del sistema
- __repositorios:__ administra las operaiones de acceso a la base de datos
- __servicios:__ contiene la logica y las operaciones principales
- __infraestructura:__ contiene los componentes relacionados con tecnologias externas, como SQLite y PyMuPDF
- __estructuras:__ contiene estructuras de datos implmentadas para el proyecto
- __plantillas:__ almacena las paginas HTML
- __archivos_estaticos:__ contiene los estilos, scripts e imagenes
- __datos:__ lamacena la base de datos
- __documentos:__ almacena los PDF y sus portadas
- __prueba:__ contiene las pruebas automatizadas

__Nota:__ Se debe crear un entorno virtual, para ejecutar el archivo, ya que asi se pueden descargar las librerias necesarias que se contienen en "requerimientos.txt"

## Convenciones para commints, pullrequest y merges

### Para commints
- __Formato:__ tipo(area): descripcion breve

#### Tipos principales
| Tipo | Uso |
|----|---|
| feat | Agregar una funcionalidad |
| fix | Corregir un error |
| docs | Modificar documentacion |
| style | Cambios de formato o presentacion sin modificar la logica |
| refactor | Mejorar la estructura del codigo sin cambiar su comportamiento |
| test | Agregar o modificar pruebas |
| chore | Tareas de mantenimiento o configuracion |

__Ejemplos:__
  - feat(database): crear esquema inicial de SQLite
  - feat(libros): agregar registro de documentos PDF
  - fix(repositorios): corregir consulta de libros
  - docs(readme): documentar estructura del proyecto
  - refactor(servicios): separar operaciones de biblioteca
  - test(libros): agregar pruebas de registro
  - chore(config): actualizar dependencias

### Para pull request
- __Formato del titulo:__ tipo(area): descripcion del cambio

__ejemplo:__ feat(database): implementar conexion y esquema inicial

- __Descripcion recomendada:__

Descripcion: Explicacion breve que se agrego o modifico

Cambios realizados:
- cambio 1
- cambio 2
- cambio 3

Pruebas
- Se verifico el funcionamiento
- Se ejecutaron las pruebas correspondientes

Observaciones

Indica errores conocidos o detalles importantes

### Ramas y merges
Se utiliza la siguiente organizacion:

| Rama | Proposito |
|-|-|
| main | Contiene la version estable del proyecto |
| develop | Integra los cambios antes de incorporarlos a la version estable|
| feature/nombre | Desarrolla una funcionalidad nueva |
| fix/nombre | Corrige un problema existente |
