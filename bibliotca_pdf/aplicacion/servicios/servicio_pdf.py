from pathlib import Path

from aplicacion.infraestructura.documentos.adaptador_pymupdf import (
    AdaptadorPyMuPDF
)


class ServicioPDF:

    def __init__(self, lector=None):
        self.lector = (
            lector
            or AdaptadorPyMuPDF()
        )

    def validar_pdf(self, ruta):
        """
        Verifica que un archivo sea un PDF válido.
        """

        ruta = Path(ruta)

        if not ruta.exists():
            raise FileNotFoundError(
                "El archivo PDF no existe."
            )

        if not ruta.is_file():
            raise ValueError(
                "La ruta no corresponde a un archivo."
            )

        if ruta.suffix.lower() != ".pdf":
            raise ValueError(
                "El archivo no tiene extensión PDF."
            )

        try:
            self.lector.abrir(ruta)

            paginas = self.lector.obtener_numero_paginas()

            if paginas <= 0:
                raise ValueError(
                    "El documento no contiene páginas."
                )

            return True

        finally:
            self.lector.cerrar()

    def obtener_numero_paginas(self, ruta):
        """
        Obtiene el número de páginas de un PDF.
        """

        try:
            self.lector.abrir(ruta)

            return self.lector.obtener_numero_paginas()

        finally:
            self.lector.cerrar()

    def obtener_metadatos(self, ruta):
        """
        Obtiene los metadatos de un PDF.
        """

        try:
            self.lector.abrir(ruta)

            return self.lector.obtener_metadatos()

        finally:
            self.lector.cerrar()

    def obtener_texto_pagina(
        self,
        ruta,
        numero_pagina
    ):
        """
        Obtiene el texto de una página.
        """

        try:
            self.lector.abrir(ruta)

            return self.lector.obtener_texto_pagina(
                numero_pagina
            )

        finally:
            self.lector.cerrar()

    def obtener_imagen_pagina(
        self,
        ruta,
        numero_pagina,
        escala=1.5
    ):
        """
        Obtiene la imagen de una página.
        """

        try:
            self.lector.abrir(ruta)

            return self.lector.obtener_imagen_pagina(
                numero_pagina,
                escala
            )

        finally:
            self.lector.cerrar()
