from flask import Flask

from aplicacion.infraestructura.base_datos.inicializar import (
    inicializar_base_datos
)


def crear_aplicacion():
    """
    Crea y configura la aplicación Flask.
    """

    app = Flask(
        __name__,
        template_folder="plantillas",
        static_folder="archivos_estaticos"
    )


    # Configuración básica
    app.config["SECRET_KEY"] = "clave-desarrollo"

    # Inicializar la base de datos
    inicializar_base_datos()

    # Registrar rutas
    from aplicacion.rutas.libros import libros_bp
    from aplicacion.rutas.grupos import grupos_bp
    from aplicacion.rutas.biblioteca import biblioteca_bp
    from aplicacion.rutas.lector import lector_bp

    app.register_blueprint(libros_bp)
    app.register_blueprint(grupos_bp)
    app.register_blueprint(biblioteca_bp)
    app.register_blueprint(lector_bp)

    return app
