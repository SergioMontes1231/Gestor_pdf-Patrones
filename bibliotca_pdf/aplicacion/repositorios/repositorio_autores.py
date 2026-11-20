from aplicacion.repositorios.repositorio_base import (
    RepositorioBase
)

from aplicacion.modelos.autor import Autor


class RepositorioAutores(RepositorioBase):

    def guardar(self, autor):
        """
        Guarda un autor nuevo.
        """

        consulta = """
            INSERT INTO Autor (
                nombre_autor
            )
            VALUES (?)
        """

        parametros = (
            autor.nombre_autor,
        )

        autor.id_autor = self.ejecutar(
            consulta,
            parametros
        )

        return autor

    def obtener_por_id(self, id_autor):
        """
        Obtiene un autor mediante su ID.
        """

        consulta = """
            SELECT *
            FROM Autor
            WHERE id_autor = ?
        """

        resultado = self.obtener_uno(
            consulta,
            (id_autor,)
        )

        if resultado is None:
            return None

        return self._convertir_a_autor(resultado)

    def obtener_todos(self):
        """
        Obtiene todos los autores registrados.
        """

        consulta = """
            SELECT *
            FROM Autor
            ORDER BY nombre_autor
        """

        resultados = self.obtener_registros(
            consulta
        )

        return [
            self._convertir_a_autor(resultado)
            for resultado in resultados
        ]

    def buscar_por_nombre(self, nombre):
        """
        Busca autores por nombre.
        """

        consulta = """
            SELECT *
            FROM Autor
            WHERE nombre_autor LIKE ?
            ORDER BY nombre_autor
        """

        resultados = self.obtener_registros(
            consulta,
            (f"%{nombre}%",)
        )

        return [
            self._convertir_a_autor(resultado)
            for resultado in resultados
        ]

    def actualizar(self, autor):
        """
        Actualiza el nombre de un autor.
        """

        consulta = """
            UPDATE Autor
            SET nombre_autor = ?
            WHERE id_autor = ?
        """

        parametros = (
            autor.nombre_autor,
            autor.id_autor
        )

        self.ejecutar(
            consulta,
            parametros
        )

    def eliminar(self, id_autor):
        """
        Elimina un autor.
        """

        consulta = """
            DELETE FROM Autor
            WHERE id_autor = ?
        """

        self.ejecutar(
            consulta,
            (id_autor,)
        )

    def obtener_libros(self, id_autor):
        """
        Obtiene los PDFs asociados a un autor.
        """

        consulta = """
            SELECT PDFs.*
            FROM PDFs
            INNER JOIN Crea
                ON PDFs.id_pdf = Crea.id_pdf
            WHERE Crea.id_autor = ?
            ORDER BY PDFs.nombre_pdf
        """

        return self.obtener_registros(
            consulta,
            (id_autor,)
        )

    @staticmethod
    def _convertir_a_autor(resultado):
        """
        Convierte un registro de SQLite en un objeto Autor.
        """

        return Autor(
            id_autor=resultado["id_autor"],
            nombre_autor=resultado["nombre_autor"]
        )
