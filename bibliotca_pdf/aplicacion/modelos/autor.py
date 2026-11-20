from dataclasses import dataclass

@dataclass
class Autor:
    id_autor: int | None = None
    nombre_autor: str = ""
