from aplicacion.repositorios.repositorio_base import (
    RepositorioBase
)


class RepositorioProgreso(RepositorioBase):

    def guardar_progreso(self, id_pdf, pagina_actual):
        """
        Guarda o actualiza la página actual de un PDF.
        """

        consulta = """
            INSERT INTO Progreso (
                id_pdf,
                pagina_actual
            )
            VALUES (?, ?)
            ON CONFLICT(id_pdf)
            DO UPDATE SET
                pagina_actual = excluded.pagina_actual,
                fecha_actualizacion = CURRENT_TIMESTAMP
        """

        self.ejecutar(
            consulta,
            (id_pdf, pagina_actual)
        )

    def obtener_progreso(self, id_pdf):
        """
        Obtiene la última página guardada.
        """

        consulta = """
            SELECT *
            FROM Progreso
            WHERE id_pdf = ?
        """

        return self.obtener_uno(
            consulta,
            (id_pdf,)
        )

    def eliminar_progreso(self, id_pdf):
        """
        Elimina el progreso de un PDF.
        """

        consulta = """
            DELETE FROM Progreso
            WHERE id_pdf = ?
        """

        self.ejecutar(
            consulta,
            (id_pdf,)
        )