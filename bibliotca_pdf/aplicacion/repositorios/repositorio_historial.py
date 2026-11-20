from aplicacion.repositorios.repositorio_base import (
    RepositorioBase
)


class RepositorioHistorial(RepositorioBase):

    def registrar_apertura(self, id_pdf):
        """
        Registra la apertura de un PDF.
        """

        consulta = """
            INSERT INTO Historial (
                id_pdf
            )
            VALUES (?)
        """

        return self.ejecutar(
            consulta,
            (id_pdf,)
        )

    def obtener_historial(self, limite=50):
        """
        Obtiene las últimas aperturas registradas.
        """

        consulta = """
            SELECT
                Historial.id_historial,
                Historial.id_pdf,
                Historial.fecha_apertura,
                PDFs.nombre_pdf
            FROM Historial
            INNER JOIN PDFs
                ON Historial.id_pdf = PDFs.id_pdf
            ORDER BY Historial.fecha_apertura DESC
            LIMIT ?
        """

        return self.obtener_registros(
            consulta,
            (limite,)
        )

    def obtener_historial_libro(self, id_pdf):
        """
        Obtiene las aperturas de un PDF específico.
        """

        consulta = """
            SELECT *
            FROM Historial
            WHERE id_pdf = ?
            ORDER BY fecha_apertura DESC
        """

        return self.obtener_registros(
            consulta,
            (id_pdf,)
        )

    def eliminar_historial(self):
        """
        Elimina todos los registros del historial.
        """

        consulta = """
            DELETE FROM Historial
        """

        self.ejecutar(consulta)