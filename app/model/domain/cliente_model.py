from sqlalchemy.sql.sqltypes import Date
from datetime import date
from datetime import datetime

class ClienteModel:
    def __init__(self):
        self.IdCliente: int
        self.NumeroCliente: str
        self.Email: str
        self.PrimerNombre: str
        self.SegundoNombre: str
        self.ApellidoPaterno: str
        self.ApellidoMaterno: str
        self.CURP: str
        self.FechaNacimiento: Date
        self.Celular: str
        self.RFC: str

    def validar_edad(self) -> bool:
        today = date.today()
        nacimiento = datetime.strptime(self.FechaNacimiento, '%Y-%m-%d').date()
        age = today.year - nacimiento.year - ((today.month, today.day) < (nacimiento.month, nacimiento.day))

        if age >= 18 and age <= 75:
            return True
        else:
            return False