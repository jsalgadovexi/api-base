from datetime import date
from pydantic import BaseModel
from typing import Optional

################################################################################
### Clases que se reciben
################################################################################

class TestRequest(BaseModel):
    primer_campo: str
    segundo_campo: str
    tercer_campo: Optional[str] = None

class DatosAlta(BaseModel):
    nombre:str
    comentarios:str

class EmailRequest(BaseModel):
    email: str

class ProspectoRequest(BaseModel):
    email: str
    primer_nombre: str
    segundo_nombre: str
    ap_paterno: str
    ap_materno: str
    CURP: str
    fecha_nac: date
    RFC: str
    telefono: str
    calle: str

################################################################################
### Clases que se envían
################################################################################

class TestData(BaseModel):
    valor1: int
    valor2: str

class TestResponse(BaseModel):
    estatus: int
    mensaje: str
    datos: TestData

class EmailResponse(BaseModel):
    estatus: int
    mensaje: str
    id_nuevo_email: int

class ProspectoResponse(BaseModel):
    estatus: int
    mensaje: str
    id_prospecto: int
    id_email: int
    id_celular: int
    id_direccion: int