from aplicacion.repositorios.repositorio_libros import (
    RepositorioLibros
)
from aplicacion.servicios.servicio_pdf import (
    ServicioPDF
)


class ServicioLibros:

    def __init__(
        self,
        repositorio=None,
        servicio_pdf=None
    ):

        self.repositorio = (
            repositorio
            or RepositorioLibros()
        )

        self.servicio_pdf = (
            servicio_pdf
            or ServicioPDF()
        )

    def registrar_libro(self, libro):
        """
        Registra un libro validando previamente su PDF.
        """

        if not libro.nombre_pdf.strip():
            raise ValueError(
                "El nombre del libro no puede estar vacío."
            )

        if not libro.ruta_archivo_pdf:
            raise ValueError(
                "El libro debe tener una ruta de archivo."
            )

        # Validar el PDF
        self.servicio_pdf.validar_pdf(
            libro.ruta_archivo_pdf
        )

        # Obtener automáticamente el número de páginas
        libro.total_paginas = (
            self.servicio_pdf.obtener_numero_paginas(
                libro.ruta_archivo_pdf
            )
        )

        # Guardar el libro en la base de datos
        return self.repositorio.guardar(
            libro
        )

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
