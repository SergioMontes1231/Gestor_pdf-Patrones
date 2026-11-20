from flask import Blueprint, render_template

from aplicacion.repositorios.repositorio_grupos import (
    RepositorioGrupos
)


grupos_bp = Blueprint(
    "grupos",
    __name__
)


@grupos_bp.route("/grupos")
def grupos():
    """
    Muestra todos los grupos de la biblioteca.
    """

    repositorio = RepositorioGrupos()

    grupos = repositorio.obtener_todos()

    return render_template(
        "grupos.html",
        grupos=grupos
    )
