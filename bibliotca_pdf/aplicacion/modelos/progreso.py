from dataclasses import dataclass

@dataclass
class Progreso:
    id_pdf: int
    pagina_actual: int = 1
    porcentaje: float = 0.0
