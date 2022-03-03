from fastapi import APIRouter, Body, Depends, HTTPException
from services import login_handler as handler
from common.api.responses import responses as HTTP_RESPONSES

from model.rest import (
    CodigoResponse,
    EmailRequest,
    LoginRequest,
    LoginResponse
)

################################################################################
### Se pueden definir errores personalizados (ver la implementación en el
### archivo EntityNotFoundException) 
################################################################################
router = APIRouter(responses=HTTP_RESPONSES)

@router.post("/codigo_verificacion/{email}", response_model=CodigoResponse)
async def registrar_email(email: str) -> CodigoResponse:
    codigo = handler.registrar_codigo_login(email)

    return CodigoResponse(
        estatus = 200,
        mensaje = "Se envió un código de verificación a tu correo electrónico registrado",
        codigo = codigo
    )

@router.post("/login/{email}", response_model=LoginResponse)
async def registrar_email(email: str, data: LoginRequest) -> LoginResponse:
    handler.validar_login(email, data.codigo)

    return LoginResponse(
        estatus = 200,
        mensaje = "Acceso correcto",
        prospecto = 1
    )