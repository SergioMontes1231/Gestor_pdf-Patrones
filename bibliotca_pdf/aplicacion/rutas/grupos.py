from flask import Blueprint, render_template, redirect, url_for, request

from aplicacion.modelos.grupo import Grupo
from aplicacion.repositorios.repositorio_grupos import RepositorioGrupos


grupos_bp = Blueprint("grupos", __name__)


@grupos_bp.route("/grupos")
def mostrar_grupos():
    repositorio = RepositorioGrupos()
    grupos = repositorio.obtener_todos()

    return render_template(
        "grupos.html",
        grupos=grupos
    )


@grupos_bp.route("/grupos/crear", methods=["POST"])
def crear_grupo():
    nombre = request.form.get("nombre_grupo", "").strip()
    descripcion = request.form.get("descripcion_grupo", "").strip()

    if not nombre:
        return "El nombre del grupo es obligatorio", 400

    grupo = Grupo(
        nombre_grupo=nombre,
        descripcion_grupo=descripcion
    )

    repositorio = RepositorioGrupos()
    repositorio.guardar(grupo)

    return redirect(url_for("grupos.mostrar_grupos"))


@grupos_bp.route("/grupos/<int:id_grupo>/eliminar", methods=["POST"])
def eliminar_grupo(id_grupo):
    repositorio = RepositorioGrupos()

    repositorio.eliminar(id_grupo)

    return redirect(url_for("grupos.mostrar_grupos"))

@grupos_bp.route("/grupos/<int:id_grupo>")
def detalle_grupo(id_grupo):

    repositorio = RepositorioGrupos()

    grupo = repositorio.obtener_por_id(id_grupo)

    if grupo is None:
        return "Grupo no encontrado", 404

    libros = repositorio.obtener_libros(id_grupo)

    return render_template(
        "detalle_grupo.html",
        grupo=grupo,
        libros=libros
    )
