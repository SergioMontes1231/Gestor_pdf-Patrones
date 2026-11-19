from pathlib import Path

from aplicacion.infraestructura.base_datos.conexion import (
    obtener_conexion,
    RUTA_BASE_DATOS
)


# Ubicación del archivo esquema.sql
RUTA_ESQUEMA = Path(__file__).parent / "esquema.sql"


def inicializar_base_datos():
    """
    Crea las tablas de la base de datos
    utilizando el esquema SQL definido.
    """

    # Leer el archivo SQL
    with open(RUTA_ESQUEMA, "r", encoding="utf-8") as archivo:
        esquema = archivo.read()

    # Ejecutar el esquema en la base de datos
    with obtener_conexion() as conexion:
        conexion.executescript(esquema)

    print("Base de datos inicializada correctamente.")
    print(f"Ubicación: {RUTA_BASE_DATOS}")


if __name__ == "__main__":
    inicializar_base_datos()