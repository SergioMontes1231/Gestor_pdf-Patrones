from aplicacion.repositorios.repositorio_progreso import (
    RepositorioProgreso
)


class ServicioProgreso:

    def __init__(self, repositorio=None):
        self.repositorio = (
            repositorio
            or RepositorioProgreso()
        )

    def guardar_progreso(
        self,
        id_pdf,
        pagina_actual,
        total_paginas
    ):
        """
        Guarda la página actual de lectura.
        """

        if id_pdf <= 0:
            raise ValueError(
                "El ID del PDF no es válido."
            )

        if pagina_actual < 1:
            raise ValueError(
                "La página debe ser mayor o igual a uno."
            )

        if pagina_actual > total_paginas:
            raise ValueError(
                "La página excede el total del documento."
            )

        self.repositorio.guardar_progreso(
            id_pdf,
            pagina_actual
        )

    def obtener_progreso(self, id_pdf):
        """
        Obtiene la página guardada.
        """

        resultado = self.repositorio.obtener_progreso(
            id_pdf
        )

        if resultado is None:
            return 1

        return resultado["pagina_actual"]

    def reiniciar_progreso(self, id_pdf):
        """
        Elimina el progreso guardado de un PDF.
        """

        self.repositorio.eliminar_progreso(
            id_pdf
        )
