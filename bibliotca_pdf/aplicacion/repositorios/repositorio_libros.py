from aplicacion.repositorios.repositorio_base import (
    RepositorioBase
)

from aplicacion.modelos.libro import Libro


class RepositorioLibros(RepositorioBase):

    def guardar(self, libro):
        """
        Guarda un libro nuevo en la base de datos.
        """

        consulta = """
            INSERT INTO PDFs (
                nombre_pdf,
                descripcion_pdf,
                total_paginas,
                id_estado,
                ruta_archivo_pdf,
                ruta_portada_pdf
            )
            VALUES (?, ?, ?, ?, ?, ?)
        """

        parametros = (
            libro.nombre_pdf,
            libro.descripcion_pdf,
            libro.total_paginas,
            libro.id_estado,
            libro.ruta_archivo_pdf,
            libro.ruta_portada_pdf
        )

        libro.id_pdf = self.ejecutar(
            consulta,
            parametros
        )

        return libro

    def obtener_por_id(self, id_pdf):
        """
        Obtiene un libro mediante su identificador.
        """

        consulta = """
            SELECT *
            FROM PDFs
            WHERE id_pdf = ?
        """

        resultado = self.obtener_uno(
            consulta,
            (id_pdf,)
        )

        if resultado is None:
            return None

        return Libro(
            id_pdf=resultado["id_pdf"],
            nombre_pdf=resultado["nombre_pdf"],
            descripcion_pdf=resultado["descripcion_pdf"],
            total_paginas=resultado["total_paginas"],
            id_estado=resultado["id_estado"],
            ruta_archivo_pdf=resultado["ruta_archivo_pdf"],
            ruta_portada_pdf=resultado["ruta_portada_pdf"]
        )

    def obtener_todos(self):
        """
        Obtiene todos los libros registrados.
        """

        consulta = """
            SELECT *
            FROM PDFs
            ORDER BY nombre_pdf
        """

        resultados = self.obtener_registros(
            consulta
        )

        return [
            self._convertir_a_libro(resultado)
            for resultado in resultados
        ]


    def buscar_por_nombre(self, nombre):
        """
        Busca libros cuyo nombre contenga el texto indicado.
        """

        consulta = """
            SELECT *
            FROM PDFs
            WHERE nombre_pdf LIKE ?
            ORDER BY nombre_pdf
        """

        resultados = self.obtener_registros(
            consulta,
            (f"%{nombre}%",)
        )

        return [
            self._convertir_a_libro(resultado)
            for resultado in resultados
        ]

    def actualizar(self, libro):
        """
        Actualiza la información de un libro.
        """

        consulta = """
            UPDATE PDFs
            SET nombre_pdf = ?,
                descripcion_pdf = ?,
                total_paginas = ?,
                id_estado = ?,
                ruta_archivo_pdf = ?,
                ruta_portada_pdf = ?
            WHERE id_pdf = ?
        """

        parametros = (
            libro.nombre_pdf,
            libro.descripcion_pdf,
            libro.total_paginas,
            libro.id_estado,
            libro.ruta_archivo_pdf,
            libro.ruta_portada_pdf,
            libro.id_pdf
        )

        self.ejecutar(
            consulta,
            parametros
        )

    def eliminar(self, id_pdf):
        """
        Elimina un libro de la base de datos.
        """

        consulta = """
            DELETE FROM PDFs
            WHERE id_pdf = ?
        """

        self.ejecutar(
            consulta,
            (id_pdf,)
        )

    def asociar_grupo(self, id_pdf, id_grupo):
        """
        Relaciona un libro con un grupo.
        """

        consulta = """
            INSERT OR IGNORE INTO Agrupar (
                id_pdf,
                id_grupo
            )
            VALUES (?, ?)
        """

        self.ejecutar(
            consulta,
            (id_pdf, id_grupo)
        )

    def quitar_grupo(self, id_pdf, id_grupo):
        """
        Elimina la relación entre un libro y un grupo.
        """

        consulta = """
            DELETE FROM Agrupar
            WHERE id_pdf = ?
              AND id_grupo = ?
        """

        self.ejecutar(
            consulta,
            (id_pdf, id_grupo)
        )

    def asociar_autor(self, id_pdf, id_autor):
        self.ejecutar(
            """
            INSERT OR IGNORE INTO Crea (id_pdf, id_autor)
            VALUES (?, ?)
            """,
            (id_pdf, id_autor)
    )

    def quitar_autor(self, id_pdf, id_autor):
        """
        Elimina la relación entre un libro y un autor.
        """

        consulta = """
            DELETE FROM Crea
            WHERE id_pdf = ?
              AND id_autor = ?
        """

        self.ejecutar(
            consulta,
            (id_pdf, id_autor)
        )

    @staticmethod
    def _convertir_a_libro(resultado):
        """
        Convierte un registro de SQLite en un objeto Libro.
        """

        return Libro(
            id_pdf=resultado["id_pdf"],
            nombre_pdf=resultado["nombre_pdf"],
            descripcion_pdf=resultado["descripcion_pdf"],
            total_paginas=resultado["total_paginas"],
            id_estado=resultado["id_estado"],
            ruta_archivo_pdf=resultado["ruta_archivo_pdf"],
            ruta_portada_pdf=resultado["ruta_portada_pdf"]
        )
