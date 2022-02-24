from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.exceptions import RequestValidationError
from pydantic import errors
from pydantic.error_wrappers import ValidationError
from starlette.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from model.errors import EntityNotFoundException
from model.errors import NotFoundMessage
from services import solicitud_handler as handler
from fastapi import Request
from fastapi_jwt_auth import AuthJWT
from common.api.responses import responses as HTTP_RESPONSES
import time

################################################################################
### En app/model/rest.py se definen los modelos que servirán para comunicarse
### con el front end (tanto los que se reciben como los que se devuelven)
################################################################################

from model.rest import (
    EmailRequest,
    EmailResponse,
    ProspectoRequest,
    ProspectoResponse
)

################################################################################
### Se pueden definir errores personalizados (ver la implementación en el
### archivo EntityNotFoundException) 
################################################################################
router = APIRouter(responses=HTTP_RESPONSES)


################################################################################
### Se definen los parámetros que se reciben y los que se devuelven con base 
### en el modelo
################################################################################



@router.post("/registrar_email", response_model=EmailResponse)
async def registrar_email(data: EmailRequest) -> EmailResponse:
    id_email = handler.registrar_email_prospecto(data.email)

    return EmailResponse(
        estatus = 200,
        mensaje = "El email se registro con éxito",
        id_nuevo_email = id_email
    )

@router.post("/registrar_prospecto", response_model=ProspectoResponse)
async def registrar_prospecto(prospecto: ProspectoRequest) -> ProspectoResponse:
    id_email, id_prospecto = handler.registrar_prospecto(prospecto)
    # import pdb; pdb.set_trace()
    return ProspectoResponse(
        estatus = 200,
        mensaje = 'Prospecto registrado exitosamente',
        id_email = id_email,
        id_prospecto = id_prospecto
    )