import pytest
from aplicacion.modelos.libro import Libro


def test_libro_tiene_ruta_pdf():
    libro = Libro(
        id_pdf=1,
        nombre_pdf="Documento",
        descripcion_pdf="Prueba",
        total_paginas=10,
        id_estado=1,
        ruta_archivo_pdf="/documentos/prueba.pdf",
        ruta_portada_pdf=None
    )

    assert libro.ruta_archivo_pdf.endswith(".pdf")


def test_libro_tiene_paginas():
    libro = Libro(
        id_pdf=1,
        nombre_pdf="Documento",
        descripcion_pdf="Prueba",
        total_paginas=10,
        id_estado=1,
        ruta_archivo_pdf="/documentos/prueba.pdf",
        ruta_portada_pdf=None
    )

    assert libro.total_paginas > 0
    assert libro.total_paginas == 10
