import pytest
from aplicacion.modelos.progreso import Progreso


def test_crear_progreso():
    progreso = Progreso(
        id_pdf=1,
        pagina_actual=5
    )

    assert progreso.id_pdf == 1
    assert progreso.pagina_actual == 5


def test_progreso_pagina_inicial():
    progreso = Progreso(
        id_pdf=1,
        pagina_actual=0
    )

    assert progreso.pagina_actual == 0


def test_progreso_actualizado():
    progreso = Progreso(
        id_pdf=1,
        pagina_actual=10
    )

    progreso.pagina_actual = 25

    assert progreso.pagina_actual == 25
