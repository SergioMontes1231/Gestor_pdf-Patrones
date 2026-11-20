from aplicacion.repositorios.repositorio_libros import (
    RepositorioLibros
)


class ServicioLibros:

    def __init__(self, repositorio=None):
        self.repositorio = (
            repositorio
            or RepositorioLibros()
        )

    def registrar_libro(self, libro):
        """
        Registra un libro en la biblioteca.
        """

        if not libro.nombre_pdf.strip():
            raise ValueError(
                "El nombre del libro no puede estar vacío."
            )

        if libro.total_paginas <= 0:
            raise ValueError(
                "El libro debe tener al menos una página."
            )

        if not libro.ruta_archivo_pdf:
            raise ValueError(
                "El libro debe tener una ruta de archivo."
            )

        return self.repositorio.guardar(libro)

    def obtener_libro(self, id_pdf):
        """
        Obtiene un libro mediante su ID.
        """

        return self.repositorio.obtener_por_id(
            id_pdf
        )

    def obtener_libros(self):
        """
        Obtiene todos los libros de la biblioteca.
        """

        return self.repositorio.obtener_todos()

    def actualizar_libro(self, libro):
        """
        Actualiza los datos de un libro.
        """

        if libro.id_pdf is None:
            raise ValueError(
                "El libro no tiene un ID válido."
            )

        if not libro.nombre_pdf.strip():
            raise ValueError(
                "El nombre del libro no puede estar vacío."
            )

        self.repositorio.actualizar(libro)

    def eliminar_libro(self, id_pdf):
        """
        Elimina un libro de la biblioteca.
        """

        libro = self.repositorio.obtener_por_id(
            id_pdf
        )

        if libro is None:
            raise ValueError(
                "El libro no existe."
            )

        self.repositorio.eliminar(id_pdf)

    def asociar_grupo(self, id_pdf, id_grupo):
        """
        Asocia un libro con un grupo.
        """

        self.repositorio.asociar_grupo(
            id_pdf,
            id_grupo
        )

    def quitar_grupo(self, id_pdf, id_grupo):
        """
        Quita un libro de un grupo.
        """

        self.repositorio.quitar_grupo(
            id_pdf,
            id_grupo
        )

    def asociar_autor(self, id_pdf, id_autor):
        """
        Asocia un autor con un libro.
        """

        self.repositorio.asociar_autor(
            id_pdf,
            id_autor
        )

    def quitar_autor(self, id_pdf, id_autor):
        """
        Quita la asociación de un autor con un libro.
        """

        self.repositorio.quitar_autor(
            id_pdf,
            id_autor
        )
