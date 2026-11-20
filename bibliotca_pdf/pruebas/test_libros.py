import pytest
from aplicacion.modelos.libro import Libro


def test_crear_libro():
    libro = Libro(
        id_pdf=1,
        nombre_pdf="Libro de prueba",
        descripcion_pdf="Descripción del libro",
        total_paginas=100,
        id_estado=1,
        ruta_archivo_pdf="/documentos/libro.pdf",
        ruta_portada_pdf="/documentos/portada.png"
    )

    assert libro.id_pdf == 1
    assert libro.nombre_pdf == "Libro de prueba"
    assert libro.descripcion_pdf == "Descripción del libro"
    assert libro.total_paginas == 100
    assert libro.id_estado == 1


def test_libro_sin_portada():
    libro = Libro(
        id_pdf=2,
        nombre_pdf="Libro sin portada",
        descripcion_pdf="",
        total_paginas=50,
        id_estado=1,
        ruta_archivo_pdf="/documentos/libro.pdf",
        ruta_portada_pdf=None
    )

    assert libro.ruta_portada_pdf is None
    assert libro.nombre_pdf == "Libro sin portada"
