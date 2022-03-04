from http.client import HTTPResponse
from operator import ne
import random
from typing import Any, List
from fastapi import HTTPException
from loguru import logger
from starlette import status
from db.cliente_uow import ClienteUnitOfWork

import requests
from model.domain.cliente_model import ClienteModel
from model.domain.direccion_cliente_model import DireccionClienteModel
from model.errors import RulesBussinessException

from model.rest import ClienteRequest

HTTP_SESSION = requests.Session()

number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
ALPHABET = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def random_numero_cliente(char_set = number+ALPHABET, captcha_size = 7):
    text = []
    for i in range(captcha_size):
        c = random.choice(char_set)
        text.append(c)
    return ''.join(text)

def registrar_cliente(cliente: ClienteRequest)->List[int]:
    try:
        with ClienteUnitOfWork() as uow:
            new_model_cliente = ClienteModel()
            new_model_direccion = DireccionClienteModel()

            new_model_cliente.NumeroCliente = random_numero_cliente()
            new_model_cliente.Email = cliente.email
            new_model_cliente.PrimerNombre = cliente.primer_nombre
            new_model_cliente.SegundoNombre = cliente.segundo_nombre
            new_model_cliente.ApellidoPaterno = cliente.apellido_paterno
            new_model_cliente.ApellidoMaterno = cliente.apellido_materno
            new_model_cliente.CURP = cliente.CURP
            new_model_cliente.FechaNacimiento = cliente.fecha_nacimiento
            if not new_model_cliente.validar_edad():
                raise RulesBussinessException("El cliente no cumple con la edad permitida")
            new_model_cliente.Celular = cliente.celular
            new_model_cliente.RFC = cliente.RFC

            if uow.prospecto_repository.get_by_cliente(cliente) == None:
                raise RulesBussinessException("No hay un prospecto registrado con esos datos")

            uow.cliente_repository.add(new_model_cliente)

            new_model_direccion.Calle = cliente.direccion
            new_model_direccion.IdCliente = new_model_cliente.IdCliente

            uow.direccion_repository.add(new_model_direccion)

            uow.commit()
        return [new_model_cliente.IdCliente, new_model_direccion.IdDireccion]
    except RulesBussinessException as exc:
        # logger.exception(exc)
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=str(exc),
            headers={"WWW-Authenticate": "Bearer"},
        )
    except Exception as exc:
        logger.exception(exc)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(exc),
            headers={"WWW-Authenticate": "Bearer"},
        )