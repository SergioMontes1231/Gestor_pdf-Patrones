from flask import Blueprint, render_template, redirect, url_for

from aplicacion.servicios.servicio_libros import (
    ServicioLibros
)


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

    if libro is None:
        return "Libro no encontrado", 404

    return render_template(
        "detalle_libro.html",
        libro=libro
    )


@libros_bp.route(
    "/libro/<int:id_pdf>/eliminar",
    methods=["POST"]
)
def eliminar_libro(id_pdf):
    """
    Elimina un libro de la biblioteca.
    """

    servicio = ServicioLibros()

    try:
        servicio.eliminar_libro(
            id_pdf
        )

    except ValueError:
        return "Libro no encontrado", 404

    return redirect(
        url_for("biblioteca.biblioteca")
    )
