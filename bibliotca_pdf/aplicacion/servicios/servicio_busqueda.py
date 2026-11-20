from aplicacion.repositorios.repositorio_libros import (
    RepositorioLibros
)

from aplicacion.repositorios.repositorio_autores import (
    RepositorioAutores
)

from aplicacion.repositorios.repositorio_grupos import (
    RepositorioGrupos
)


class ServicioBusqueda:

    def __init__(
        self,
        repositorio_libros=None,
        repositorio_autores=None,
        repositorio_grupos=None
    ):

        self.repositorio_libros = (
            repositorio_libros
            or RepositorioLibros()
        )

        self.repositorio_autores = (
            repositorio_autores
            or RepositorioAutores()
        )

        self.repositorio_grupos = (
            repositorio_grupos
            or RepositorioGrupos()
        )

    def buscar_libros(self, texto):
        """
        Busca libros por nombre.
        """

        if not texto.strip():
            return []

        return self.repositorio_libros.buscar_por_nombre(
            texto
        )

    def buscar_autores(self, texto):
        """
        Busca autores por nombre.
        """

        if not texto.strip():
            return []

        return self.repositorio_autores.buscar_por_nombre(
            texto
        )

    def obtener_libros_de_grupo(self, id_grupo):
        """
        Obtiene los libros de un grupo.
        """

        return self.repositorio_grupos.obtener_libros(
            id_grupo
        )

    def obtener_libros_de_autor(self, id_autor):
        """
        Obtiene los libros de un autor.
        """

        return self.repositorio_autores.obtener_libros(
            id_autor
        )
