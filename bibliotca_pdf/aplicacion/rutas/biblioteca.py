from flask import Blueprint, render_template

from aplicacion.servicios.servicio_libros import (
    ServicioLibros
)

from aplicacion.servicios.servicio_busqueda import (
    ServicioBusqueda
)


biblioteca_bp = Blueprint(
    "biblioteca",
    __name__
)


@biblioteca_bp.route("/")
def inicio():
    """
    Página principal.
    """

    return render_template(
        "inicio.html"
    )


@biblioteca_bp.route("/biblioteca")
def biblioteca():
    """
    Muestra todos los libros registrados.
    """

    servicio = ServicioLibros()

    libros = servicio.obtener_libros()

    return render_template(
        "biblioteca.html",
        libros=libros
    )


@biblioteca_bp.route("/buscar")
def buscar():
    """
    Busca libros en la biblioteca.
    """

    from flask import request

    texto = request.args.get(
        "q",
        ""
    )

    servicio = ServicioBusqueda()

    resultados = servicio.buscar_libros(
        texto
    )

    return render_template(
        "biblioteca.html",
        libros=resultados,
        busqueda=texto
    )
