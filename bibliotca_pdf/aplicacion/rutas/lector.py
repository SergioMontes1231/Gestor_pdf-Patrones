from flask import (
    Blueprint,
    render_template,
    Response,
    request
)

from aplicacion.servicios.servicio_libros import (
    ServicioLibros
)

from aplicacion.servicios.servicio_pdf import (
    ServicioPDF
)

from aplicacion.servicios.servicio_historial import (
    ServicioHistorial
)

from aplicacion.servicios.servicio_progreso import (
    ServicioProgreso
)


lector_bp = Blueprint(
    "lector",
    __name__
)


@lector_bp.route("/leer/<int:id_pdf>")
def leer_pdf(id_pdf):
    """
    Abre el lector de un PDF.
    """

    servicio_libros = ServicioLibros()

    servicio_progreso = ServicioProgreso()

    servicio_historial = ServicioHistorial()

    libro = servicio_libros.obtener_libro(
        id_pdf
    )

    if libro is None:
        return "Libro no encontrado", 404

    pagina_actual = servicio_progreso.obtener_progreso(
        id_pdf
    )

    servicio_historial.registrar_apertura(
        id_pdf
    )

    return render_template(
        "lector.html",
        libro=libro,
        pagina_actual=pagina_actual
    )


@lector_bp.route(
    "/leer/<int:id_pdf>/pagina/<int:numero_pagina>"
)
def obtener_pagina(id_pdf, numero_pagina):
    """
    Devuelve una página del PDF como imagen.
    """

    servicio_libros = ServicioLibros()

    servicio_pdf = ServicioPDF()

    libro = servicio_libros.obtener_libro(
        id_pdf
    )

    if libro is None:
        return "Libro no encontrado", 404

    try:
        imagen = servicio_pdf.obtener_imagen_pagina(
            libro.ruta_archivo_pdf,
            numero_pagina
        )

    except ValueError as error:
        return str(error), 400

    return Response(
        imagen,
        mimetype="image/png"
    )


@lector_bp.route(
    "/leer/<int:id_pdf>/progreso",
    methods=["POST"]
)
def guardar_progreso(id_pdf):
    """
    Guarda la página actual de lectura.
    """

    servicio_libros = ServicioLibros()

    servicio_pdf = ServicioPDF()

    servicio_progreso = ServicioProgreso()

    libro = servicio_libros.obtener_libro(
        id_pdf
    )

    if libro is None:
        return "Libro no encontrado", 404

    pagina_actual = request.form.get(
        "pagina",
        type=int
    )

    if pagina_actual is None:
        return "Página no válida", 400

    servicio_progreso.guardar_progreso(
        id_pdf,
        pagina_actual,
        libro.total_paginas
    )

    return "Progreso guardado", 200
