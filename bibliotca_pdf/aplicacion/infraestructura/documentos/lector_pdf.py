from abc import ABC, abstractmethod


class LectorPDF(ABC):

    @abstractmethod
    def abrir(self, ruta):
        """
        Abre un documento PDF.
        """
        pass

    @abstractmethod
    def cerrar(self):
        """
        Cierra el documento PDF.
        """
        pass

    @abstractmethod
    def obtener_numero_paginas(self):
        """
        Devuelve el número total de páginas.
        """
        pass

    @abstractmethod
    def obtener_texto_pagina(self, numero_pagina):
        """
        Obtiene el texto de una página.
        """
        pass

    @abstractmethod
    def obtener_metadatos(self):
        """
        Obtiene los metadatos del documento.
        """
        pass

    @abstractmethod
    def obtener_imagen_pagina(self, numero_pagina, escala=1.5):
        """
        Renderiza una página como imagen.
        """
        pass
