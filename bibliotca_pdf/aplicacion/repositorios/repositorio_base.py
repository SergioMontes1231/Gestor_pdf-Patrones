from aplicacion.infraestructura.base_datos.conexion import (
    obtener_conexion
)


class RepositorioBase:

    def ejecutar(self, consulta, parametros=()):
        """
        Ejecuta una consulta SQL que modifica la base de datos.
        """

        with obtener_conexion() as conexion:
            cursor = conexion.execute(
                consulta,
                parametros
            )

            return cursor.lastrowid

    def obtener_uno(self, consulta, parametros=()):
        """
        Obtiene un único registro.
        """

        with obtener_conexion() as conexion:
            resultado = conexion.execute(
                consulta,
                parametros
            ).fetchone()

            return resultado

    def obtener_registros(self, consulta, parametros=()):
        """
        Obtiene todos los registros de una consulta.
        """

        with obtener_conexion() as conexion:
            resultados = conexion.execute(
                consulta,
                parametros
            ).fetchall()

            return resultados
