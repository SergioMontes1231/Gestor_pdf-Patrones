import pytest
from aplicacion.modelos.grupo import Grupo
from aplicacion.modelos.autor import Autor


def test_crear_grupo():
    grupo = Grupo(
        id_grupo=1,
        nombre_grupo="Anime",
        descripcion_grupo="Libros de anime"
    )

    assert grupo.id_grupo == 1
    assert grupo.nombre_grupo == "Anime"
    assert grupo.descripcion_grupo == "Libros de anime"


def test_crear_autor():
    autor = Autor(
        id_autor=1,
        nombre_autor="Autor de prueba"
    )

    assert autor.id_autor == 1
    assert autor.nombre_autor == "Autor de prueba"
