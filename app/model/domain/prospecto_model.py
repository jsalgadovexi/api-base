from sqlalchemy.sql.sqltypes import Date
from datetime import date

class ProspectoModel:
    def __init__(self):
        self.IdProspecto: int
        self.IdEmail: int
        self.IdEstatusSolicitud: int
        self.PrimerNombre: str
        self.SegundoNombre: str
        self.ApellidoPaterno: str
        self.ApellidoMaterno: str
        self.CURP: str
        self.FechaNacimiento: Date
        self.RFC: str

    def validar_edad(self) -> bool:
        today = date.today()
        age = today.year - self.FechaNacimiento.year - ((today.month, today.day) < (self.FechaNacimiento.month, self.FechaNacimiento.day))

        if age >= 18 and age <= 75:
            return True
        else:
            return False