from dataclasses import dataclass

@dataclass
class Libro:
    id_pdf: int | None = None
    nombre_pdf: str = ""
    descripcion_pdf: str = ""
    total_paginas: int = 0
    id_estado: int = 1
    ruta_archivo_pdf: str = ""
    ruta_portada_pdf: str | None = None
