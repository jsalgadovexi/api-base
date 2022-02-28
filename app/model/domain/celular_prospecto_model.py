class CelularProspectoModel:
    def __init__(self):
        self.IdTelefono: int
        self.Telefono: str
        self.IdSolicitud: int

    def celular_valido(self) -> bool:
        if(len(self.Telefono) == 5 and self.Telefono.isdigit()):
            return True
        else:
            return False