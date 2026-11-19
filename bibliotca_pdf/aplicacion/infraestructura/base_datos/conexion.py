import sqlite3
from pathlib import Path
from contextlib import contextmanager


# Ubicación principal del proyecto
RUTA_PROYECTO = Path(__file__).resolve().parents[3]

# Ubicación de la base de datos
RUTA_BASE_DATOS = RUTA_PROYECTO / "datos" / "biblioteca.db"


@contextmanager
def obtener_conexion():
    """
    Proporciona una conexión a la base de datos SQLite.

    Administra automáticamente:
    - La apertura de la conexión.
    - La confirmación de cambios.
    - La reversión de cambios si ocurre un error.
    - El cierre de la conexión.
    """

    conexion = sqlite3.connect(RUTA_BASE_DATOS)

    # Permite acceder a las columnas por su nombre.
    conexion.row_factory = sqlite3.Row

    # Habilita las restricciones de claves foráneas.
    conexion.execute("PRAGMA foreign_keys = ON")

    try:
        yield conexion
        conexion.commit()

    except Exception:
        conexion.rollback()
        raise

    finally:
        conexion.close()
