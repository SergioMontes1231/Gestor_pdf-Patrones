from dataclasses import dataclass

@dataclass
class Grupo:
    id_grupo: int | None = None
    nombre_grupo: str = ""
    descripcion_grupo: str = ""
    ruta_portada_grupo: str | None = None
