from flask import (Blueprint, render_template, redirect, url_for, request, flash)

from pathlib import Path
from werkzeug.utils import secure_filename

from aplicacion.modelos.libro import Libro

from aplicacion.servicios.servicio_libros import (ServicioLibros)

from aplicacion.repositorios.repositorio_grupos import RepositorioGrupos

from aplicacion.modelos.autor import Autor
from aplicacion.repositorios.repositorio_autores import RepositorioAutores


libros_bp = Blueprint(
    "libros",
    __name__
)


@libros_bp.route("/libro/<int:id_pdf>")
def detalle_libro(id_pdf):
    """
    Muestra los detalles de un libro.
    """

    servicio = ServicioLibros()

    libro = servicio.obtener_libro(
        id_pdf
    )

    repositorio_grupos = RepositorioGrupos()

    grupos = repositorio_grupos.obtener_todos()

    grupos_libro = []

    for grupo in grupos:

        libros_grupo = repositorio_grupos.obtener_libros(
            grupo.id_grupo
        )

        for libro_grupo in libros_grupo:

            if libro_grupo["id_pdf"] == libro.id_pdf:

                grupos_libro.append(grupo)

                break

    if libro is None:
        return "Libro no encontrado", 404

    repositorio_autores = RepositorioAutores()

    autores = repositorio_autores.obtener_todos()

    autores_libro = []

    for autor in autores:

        libros_autor = repositorio_autores.obtener_libros(
            autor.id_autor
        )

        for libro_autor in libros_autor:

            if libro_autor["id_pdf"] == libro.id_pdf:

                autores_libro.append(autor)

                break

    return render_template(
        "detalle_libro.html",
        libro=libro,
        grupos=grupos,
        grupos_libro=grupos_libro,
        autores = autores,
        autores_libro = autores_libro
    )


@libros_bp.route("/libro/<int:id_pdf>/eliminar", methods=["POST"])
def eliminar_libro(id_pdf):

    servicio = ServicioLibros()

    libro = servicio.obtener_libro(id_pdf)

    if libro is None:
        return "Libro no encontrado", 404

    # Eliminar el archivo PDF del almacenamiento
    import os

    if os.path.exists(libro.ruta_archivo_pdf):
        os.remove(libro.ruta_archivo_pdf)

    # Eliminar portada si existe
    if (
        libro.ruta_portada_pdf
        and os.path.exists(libro.ruta_portada_pdf)
    ):
        os.remove(libro.ruta_portada_pdf)

    servicio.eliminar_libro(id_pdf)

    return redirect(
        url_for("biblioteca.biblioteca")
    )

@libros_bp.route(
    "/importar",
    methods=["POST"]
)
def importar_pdf():

    archivo = request.files.get(
        "archivo_pdf"
    )

    descripcion = request.form.get(
        "descripcion_pdf",
        ""
    )

    # Verificar que se seleccionó un archivo
    if archivo is None or archivo.filename == "":
        return "No se seleccionó ningún archivo.", 400

    # Verificar extensión
    if not archivo.filename.lower().endswith(".pdf"):
        return "El archivo debe ser un PDF.", 400

    # Preparar nombre seguro
    nombre_archivo = secure_filename(
        archivo.filename
    )

    # Ubicación del proyecto
    ruta_proyecto = Path(__file__).resolve().parents[2]

    # Carpeta de documentos
    carpeta_documentos = (
        ruta_proyecto
        / "documentos"
        / "libros"
    )

    carpeta_documentos.mkdir(
        parents=True,
        exist_ok=True
    )

    # Ruta del archivo
    ruta_archivo = (
        carpeta_documentos
        / nombre_archivo
    )

    # Evitar sobrescribir archivos existentes
    if ruta_archivo.exists():

        nombre_archivo = (
            f"{ruta_archivo.stem}_"
            f"{int(__import__('time').time())}"
            f"{ruta_archivo.suffix}"
        )

        ruta_archivo = (
            carpeta_documentos
            / nombre_archivo
        )

    # Guardar archivo
    archivo.save(
        ruta_archivo
    )

    # Crear modelo
    libro = Libro(
        nombre_pdf=Path(nombre_archivo).stem,
        descripcion_pdf=descripcion,
        ruta_archivo_pdf=str(ruta_archivo)
    )

    # Registrar libro mediante el servicio
    servicio = ServicioLibros()

    try:

        servicio.registrar_libro(
            libro
        )

    except Exception as error:

        # Si el registro falla, eliminar archivo
        if ruta_archivo.exists():
            ruta_archivo.unlink()

        return str(error), 400

    # Regresar a la biblioteca
    return redirect(
        url_for("biblioteca.biblioteca")
    )

@libros_bp.route(
    "/libro/<int:id_pdf>/grupo",
    methods=["POST"]
)
def asignar_grupo(id_pdf):

    id_grupo = request.form.get("id_grupo")

    if not id_grupo:
        return "Debes seleccionar un grupo", 400

    servicio = ServicioLibros()

    servicio.asociar_grupo(
        id_pdf,
        int(id_grupo)
    )

    return redirect(
        url_for(
            "libros.detalle_libro",
            id_pdf=id_pdf
        )
    )

@libros_bp.route(
    "/libro/<int:id_pdf>/grupo/<int:id_grupo>/eliminar",
    methods=["POST"]
)
def quitar_grupo(id_pdf, id_grupo):

    servicio = ServicioLibros()

    servicio.quitar_grupo(
        id_pdf,
        id_grupo
    )

    return redirect(
        url_for(
            "libros.detalle_libro",
            id_pdf=id_pdf
        )
    )

@libros_bp.route(
    "/libro/<int:id_pdf>/autor",
    methods=["POST"]
)
def asignar_autor(id_pdf):

    id_autor = request.form.get("id_autor")

    if not id_autor:
        return "Debes seleccionar un autor", 400

    servicio = ServicioLibros()

    servicio.asociar_autor(
        id_pdf,
        int(id_autor)
    )

    return redirect(
        url_for(
            "libros.detalle_libro",
            id_pdf=id_pdf
        )
    )


@libros_bp.route(
    "/libro/<int:id_pdf>/autor/<int:id_autor>/eliminar",
    methods=["POST"]
)
def quitar_autor(id_pdf, id_autor):

    servicio = ServicioLibros()

    servicio.quitar_autor(
        id_pdf,
        id_autor
    )

    return redirect(
        url_for(
            "libros.detalle_libro",
            id_pdf=id_pdf
        )
    )

@libros_bp.route("/libro/<int:id_pdf>/autor/crear", methods=["POST"])
def crear_autor(id_pdf):

    nombre = request.form.get(
        "nombre_autor",
        ""
    ).strip()

    if not nombre:
        return redirect(
            url_for(
                "libros.detalle_libro",
                id_pdf=id_pdf
            )
        )

    repositorio = RepositorioAutores()

    # Buscar si el autor ya existe
    autores_existentes = repositorio.buscar_por_nombre(nombre)

    autor_existente = next(
        (
            autor
            for autor in autores_existentes
            if autor.nombre_autor.lower() == nombre.lower()
        ),
        None
    )

    if autor_existente:
        autor = autor_existente

    else:
        autor = Autor(
            nombre_autor=nombre
        )

        autor = repositorio.guardar(autor)

    servicio = ServicioLibros()

    servicio.asociar_autor(
        id_pdf,
        autor.id_autor
    )

    return redirect(
        url_for(
            "libros.detalle_libro",
            id_pdf=id_pdf
        )
    )
