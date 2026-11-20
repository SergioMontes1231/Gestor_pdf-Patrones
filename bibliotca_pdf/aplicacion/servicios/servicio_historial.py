from aplicacion.repositorios.repositorio_historial import (
    RepositorioHistorial
)


class ServicioHistorial:

    def __init__(self, repositorio=None):
        self.repositorio = (
            repositorio
            or RepositorioHistorial()
        )

    def registrar_apertura(self, id_pdf):
        """
        Registra que se abrió un PDF.
        """

        if id_pdf <= 0:
            raise ValueError(
                "El ID del PDF no es válido."
            )

        return self.repositorio.registrar_apertura(
            id_pdf
        )

    def obtener_historial(self, limite=50):
        """
        Obtiene el historial de lectura.
        """

        if limite <= 0:
            raise ValueError(
                "El límite debe ser mayor que cero."
            )

        return self.repositorio.obtener_historial(
            limite
        )

    def obtener_historial_libro(self, id_pdf):
        """
        Obtiene el historial de un PDF.
        """

        return self.repositorio.obtener_historial_libro(
            id_pdf
        )

    def limpiar_historial(self):
        """
        Elimina todos los registros del historial.
        """

        self.repositorio.eliminar_historial()
