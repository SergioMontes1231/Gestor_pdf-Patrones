from aplicacion.repositorios.repositorio_base import (
    RepositorioBase
)

from aplicacion.modelos.grupo import Grupo


class RepositorioGrupos(RepositorioBase):

    def guardar(self, grupo):
        """
        Guarda un grupo nuevo.
        """

        consulta = """
            INSERT INTO Grupos (
                nombre_grupo,
                descripcion_grupo,
                ruta_portada_grupo
            )
            VALUES (?, ?, ?)
        """

        parametros = (
            grupo.nombre_grupo,
            grupo.descripcion_grupo,
            grupo.ruta_portada_grupo
        )

        grupo.id_grupo = self.ejecutar(
            consulta,
            parametros
        )

        return grupo

    def obtener_por_id(self, id_grupo):
        """
        Obtiene un grupo mediante su ID.
        """

        consulta = """
            SELECT *
            FROM Grupos
            WHERE id_grupo = ?
        """

        resultado = self.obtener_uno(
            consulta,
            (id_grupo,)
        )

        if resultado is None:
            return None

        return self._convertir_a_grupo(resultado)

    def obtener_todos(self):
        """
        Obtiene todos los grupos.
        """

        consulta = """
            SELECT *
            FROM Grupos
            ORDER BY nombre_grupo
        """

        resultados = self.obtener_registros(
            consulta
        )

        return [
            self._convertir_a_grupo(resultado)
            for resultado in resultados
        ]

    def actualizar(self, grupo):
        """
        Actualiza la información de un grupo.
        """

        consulta = """
            UPDATE Grupos
            SET nombre_grupo = ?,
                descripcion_grupo = ?,
                ruta_portada_grupo = ?
            WHERE id_grupo = ?
        """

        parametros = (
            grupo.nombre_grupo,
            grupo.descripcion_grupo,
            grupo.ruta_portada_grupo,
            grupo.id_grupo
        )

        self.ejecutar(
            consulta,
            parametros
        )

    def eliminar(self, id_grupo):
        """
        Elimina un grupo.
        """

        consulta = """
            DELETE FROM Grupos
            WHERE id_grupo = ?
        """

        self.ejecutar(
            consulta,
            (id_grupo,)
        )

    def obtener_libros(self, id_grupo):
        """
        Obtiene los libros pertenecientes a un grupo.
        """

        consulta = """
            SELECT PDFs.*
            FROM PDFs
            INNER JOIN Agrupar
                ON PDFs.id_pdf = Agrupar.id_pdf
            WHERE Agrupar.id_grupo = ?
            ORDER BY PDFs.nombre_pdf
        """

        return self.obtener_registros(
            consulta,
            (id_grupo,)
        )

    @staticmethod
    def _convertir_a_grupo(resultado):
        """
        Convierte un registro de SQLite en un objeto Grupo.
        """

        return Grupo(
            id_grupo=resultado["id_grupo"],
            nombre_grupo=resultado["nombre_grupo"],
            descripcion_grupo=resultado["descripcion_grupo"],
            ruta_portada_grupo=resultado["ruta_portada_grupo"]
        )
