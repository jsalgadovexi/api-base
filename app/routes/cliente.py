from fastapi import APIRouter, Body, Depends
from routes.validator import ValidateEmail
from services import cliente_handler as handler
from common.api.responses import responses as HTTP_RESPONSES

################################################################################
### En app/model/rest.py se definen los modelos que servirán para comunicarse
### con el front end (tanto los que se reciben como los que se devuelven)
################################################################################

from model.rest import (
    ClienteRequest,
    ClienteResponse
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

@router.post("/registrar_cliente", response_model=ClienteResponse)
async def registrar_prospecto(cliente: ClienteRequest) -> ClienteResponse:
    id_cliente, id_direccion = handler.registrar_cliente(cliente)
    # import pdb; pdb.set_trace()
    return ClienteResponse(
        estatus = 200,
        mensaje = '¡Cliente registrado exitosamente!, se le notifico por correo su incorporación a Vexi',
        id_cliente = id_cliente,
        id_direccion = id_direccion
    )