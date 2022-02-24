from datetime import datetime


class LoginModel:
    def __init__(self):
        self.IdLogin: int
        self.IdEmail: int
        self.Codigo: str
        self.FechaAcceso: datetime
        self.VecesLogin: int