
from dataclasses import dataclass, asdict

@dataclass
class RespuestaOperacion():
    contenido: any = ""
    error: bool = False
    mensaje: str = ""
