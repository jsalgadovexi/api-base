from datetime import date
import re
from turtle import title
from fastapi import HTTPException
from pydantic import BaseModel, Field
from typing import Optional
from pydantic import BaseModel, ValidationError, validator
from model.errors import FormatException
from starlette import status

from services.constants import REGEX_CODIGO, REGEX_CURP, REGEX_EMAIL, REGEX_LETTERS, REGEX_RFC

################################################################################
### Clases que se reciben
################################################################################

class TestRequest(BaseModel):
    primer_campo: str
    segundo_campo: str
    tercer_campo: Optional[str] = None
    estatus: Optional[int] = Field(1, title = "Estatus de la solicitud", description= "Estatus en la que se encuentra la solicitud del prospecto.")

class EstatusRequest(BaseModel):
    estatus: Optional[int] = Field(1, title = "Estatus de la solicitud", description= "Estatus en la que se encuentra la solicitud del prospecto.")

class DatosAlta(BaseModel):
    nombre:str
    comentarios:str

class EmailRequest(BaseModel):
    email: str
    @validator ('email')
    def email_validator(cls, email):
        try:
            if not re.fullmatch(REGEX_EMAIL, email):
                raise FormatException('El correo {} no tiene un formato de correo electrónico válido'.format(email))
            return email
        except FormatException as exc:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail=str(exc),
                headers={"WWW-Authenticate": "Bearer"},
            )

class ProspectoRequest(BaseModel):
    email: str
    @validator ('email')
    def email_validator(cls, email):
        try:
            if not re.fullmatch(REGEX_EMAIL, email):
                raise FormatException('El correo {} no tiene un formato de correo electrónico válido'.format(email))
            return email
        except FormatException as exc:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail=str(exc),
                headers={"WWW-Authenticate": "Bearer"},
            )
    primer_nombre: str
    segundo_nombre: str
    ap_paterno: str
    ap_materno: str
    CURP: str
    @validator ('CURP')
    def curp_validator(cls, CURP):
        try:
            if not re.fullmatch(REGEX_CURP, CURP):
                raise FormatException('El CURP {} no tiene un formato válido'.format(CURP))
            return CURP
        except FormatException as exc:
            raise HTTPException(
                status_code=status.HTTP_406_NOT_ACCEPTABLE,
                detail=str(exc),
                headers={"WWW-Authenticate": "Bearer"},
            )
    fecha_nac: date
    RFC: str
    @validator ('RFC')
    def rfc_validator(cls, RFC):
        try:
            if not re.fullmatch(REGEX_RFC, RFC):
                raise FormatException('El RFC {} no tiene un formato válido'.format(RFC))
            return RFC
        except FormatException as exc:
            raise HTTPException(
                status_code=status.HTTP_406_NOT_ACCEPTABLE,
                detail=str(exc),
                headers={"WWW-Authenticate": "Bearer"},
            )
    telefono: str
    @validator ('telefono')
    def telefono_validator(cls, telefono):
        try:
            if not (len(telefono) == 10 and telefono.isdigit()):
                raise FormatException('El celular {} debe tener únicamente números y un máximo de 10 dígitos'.format(telefono))
            return telefono
        except FormatException as exc:
            raise HTTPException(
                status_code=status.HTTP_406_NOT_ACCEPTABLE,
                detail=str(exc),
                headers={"WWW-Authenticate": "Bearer"},
            )
    calle: str

class LoginRequest(BaseModel):
    codigo: str
    @validator ('codigo')
    def codigo_validator(cls, codigo):
        try:
            if not re.match(REGEX_CODIGO, codigo):
                raise FormatException('El código no es válido')
            return codigo
        except FormatException as exc:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail=str(exc),
                headers={"WWW-Authenticate": "Bearer"},
            )

class ClienteRequest(BaseModel):
    email: str = Field(title="Correo electrónico", description="Correo electrónico del cliente")
    @validator ('email')
    def email_validator(cls, email):
        try:
            if not re.fullmatch(REGEX_EMAIL, email):
                raise FormatException('El correo {} no tiene un formato de correo electrónico válido'.format(email))
            return email
        except FormatException as exc:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail=str(exc),
                headers={"WWW-Authenticate": "Bearer"},
            )
    primer_nombre: str = Field(title="Primer nombre", max_length=30, description="Primer nombre del cliente")
    @validator ('primer_nombre')
    def nombre_validator(cls, primer_nombre):
        try:
            if len(primer_nombre) > 30 or not re.fullmatch(REGEX_LETTERS, primer_nombre):
                raise FormatException('El nombre {} tiene más caracteres de los permitidos y solo debe tener letras'.format(primer_nombre))
            return primer_nombre
        except FormatException as exc:
            raise HTTPException(
                status_code=status.HTTP_406_NOT_ACCEPTABLE,
                detail=str(exc),
                headers={"WWW-Authenticate": "Bearer"},
            )
    segundo_nombre: Optional[str] = Field('', title="Segundo nombre", max_length=30, description="Segundo nombre del cliente, puede o no tenerlo")
    apellido_paterno: str = Field(title="Apellido paterno", max_length=50, description="Apellido paterno del cliente")
    apellido_materno: Optional[str] = Field('', title="Apellido paterno", max_length=50, description="Apellido paterno del cliente, puede o no tenerlo")
    CURP: str = Field(title="CURP", description="CURP registrada del cliente, debe tener una longitud de 18 caracteres")
    @validator ('CURP')
    def curp_validator(cls, CURP):
        try:
            if not re.fullmatch(REGEX_CURP, CURP):
                raise FormatException('El CURP {} no tiene un formato válido'.format(CURP))
            return CURP
        except FormatException as exc:
            raise HTTPException(
                status_code=status.HTTP_406_NOT_ACCEPTABLE,
                detail=str(exc),
                headers={"WWW-Authenticate": "Bearer"},
            )
    fecha_nacimiento: date = Field(title="Fecha de nacimiento", description="La fecha de nacimiento con formato aaaa-mm-dd")
    celular: str = Field(title="Celular", description="Celular del cliente, debe tener una longitud obligatoria de 10 dígitos")
    @validator ('celular')
    def celular_validator(cls, celular):
        try:
            if not (len(celular) == 10 and celular.isdigit()):
                raise FormatException('El celular {} debe tener únicamente números y un máximo de 10 dígitos'.format(celular))
            return celular
        except FormatException as exc:
            raise HTTPException(
                status_code=status.HTTP_406_NOT_ACCEPTABLE,
                detail=str(exc),
                headers={"WWW-Authenticate": "Bearer"},
            )
    RFC: str = Field(title="RFC", description="RFC registrado del cliente, debe tener una longitud de 13 caracteres")
    @validator ('RFC')
    def rfc_validator(cls, RFC):
        try:
            if not re.fullmatch(REGEX_RFC, RFC):
                raise FormatException('El RFC {} no tiene un formato válido'.format(RFC))
            return RFC
        except FormatException as exc:
            raise HTTPException(
                status_code=status.HTTP_406_NOT_ACCEPTABLE,
                detail=str(exc),
                headers={"WWW-Authenticate": "Bearer"},
            )
    direccion: str = Field(title="Dirección", description="Calle del domicilio del cliente")

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

class CodigoResponse(BaseModel):
    estatus: int
    mensaje: str
    codigo: str

class LoginResponse(BaseModel):
    estatus: int
    mensaje: str
    prospecto: int

class ClienteResponse(BaseModel):
    estatus: int
    mensaje: str
    id_cliente: int
    id_direccion: int