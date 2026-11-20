import pymupdf

from pathlib import Path

from aplicacion.infraestructura.documentos.lector_pdf import (
    LectorPDF
)


class AdaptadorPyMuPDF(LectorPDF):

    def __init__(self):
        self.documento = None

    def abrir(self, ruta):
        """
        Abre un documento PDF utilizando PyMuPDF.
        """

        ruta = Path(ruta)

        if not ruta.exists():
            raise FileNotFoundError(
                f"No se encontró el archivo: {ruta}"
            )

        if not ruta.is_file():
            raise ValueError(
                "La ruta indicada no corresponde a un archivo."
            )

        try:
            self.documento = pymupdf.open(ruta)

        except Exception as error:
            raise ValueError(
                "No fue posible abrir el documento PDF."
            ) from error

        if not self.documento.is_pdf:
            self.cerrar()

            raise ValueError(
                "El archivo indicado no es un PDF válido."
            )

        return self

    def cerrar(self):
        """
        Cierra el documento abierto.
        """

        if self.documento is not None:
            self.documento.close()
            self.documento = None

    def obtener_numero_paginas(self):
        """
        Devuelve el número de páginas del documento.
        """

        self._verificar_documento_abierto()

        return len(self.documento)

    def obtener_texto_pagina(self, numero_pagina):
        """
        Obtiene el texto de una página.
        """

        self._verificar_documento_abierto()

        pagina = self._obtener_pagina(
            numero_pagina
        )

        return pagina.get_text()

    def obtener_metadatos(self):
        """
        Obtiene los metadatos del documento.
        """

        self._verificar_documento_abierto()

        return self.documento.metadata

    def obtener_imagen_pagina(
        self,
        numero_pagina,
        escala=1.5
    ):
        """
        Renderiza una página del PDF y devuelve sus bytes.
        """

        self._verificar_documento_abierto()

        pagina = self._obtener_pagina(
            numero_pagina
        )

        matriz = pymupdf.Matrix(
            escala,
            escala
        )

        pixeles = pagina.get_pixmap(
            matrix=matriz
        )

        return pixeles.tobytes("png")

    def _obtener_pagina(self, numero_pagina):
        """
        Obtiene una página validando su número.
        """

        total_paginas = len(self.documento)

        if numero_pagina < 1 or numero_pagina > total_paginas:
            raise ValueError(
                "El número de página está fuera del rango del documento."
            )

        return self.documento[
            numero_pagina - 1
        ]

    def _verificar_documento_abierto(self):
        """
        Verifica que exista un documento abierto.
        """

        if self.documento is None:
            raise RuntimeError(
                "No hay ningún documento PDF abierto."
            )
