import datetime
from http.client import HTTPResponse
from operator import ne
import random
from typing import Any, List
from fastapi import HTTPException
from loguru import logger
from starlette import status
from db.login_uow import LoginUnitOfWork
from db.solicitud_uow import EmailUnitOfWork

from datetime import datetime

import requests

from model.domain.login_model import LoginModel
from model.errors import UnauthorizedException

HTTP_SESSION = requests.Session()

number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
ALPHABET = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def validar_email(email: str) -> str:
    with EmailUnitOfWork() as uow:
        return uow.email_repository.get_by_email(email)

def codigo_unico(codigo: str) -> str:
    with LoginUnitOfWork() as uow:
        return uow.login_repository.get_by_codigo(codigo)

def validar_codigo(email, codigo) -> str:
    with LoginUnitOfWork() as uow:
        return uow.login_repository.get_validar_codigo(email, codigo)

def random_captcha_text(char_set = number+alphabet+ALPHABET, captcha_size = 4):
    captcha_text = []
    for i in range(captcha_size):
        c = random.choice(char_set)
        captcha_text.append(c)
    return ''.join(captcha_text)

def registrar_codigo_login(email: str)->int:
    try:
        if validar_email(email) == None:
            raise Exception("El correo " + email + " no esta registrado en base de datos.")
        else:
            email = validar_email(email)
        with LoginUnitOfWork() as uow:
            # import pdb; pdb.set_trace()
            new_model = LoginModel()
            new_model.IdEmail = email.IdEmail
            nuevo_codigo = random_captcha_text()
            if codigo_unico(nuevo_codigo):
                logger.exception("Se repite el código de inicio de sesión... Se va a generar otro código")
                nuevo_codigo = random_captcha_text()
            new_model.Codigo = nuevo_codigo
            new_model.FechaAcceso = datetime.now()
            new_model.VecesLogin = 0
            uow.login_repository.add(new_model)
            uow.commit()
        return new_model.Codigo
    except Exception as exc:
        logger.exception(exc)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(exc),
            headers={"WWW-Authenticate": "Bearer"},
        )

def validar_login(email: str, codigo: str):
    try:
        if validar_codigo(email, codigo) == None:
            raise UnauthorizedException("Los datos ingresados no coinciden")
        else:
            login = validar_codigo(email, codigo)
        with LoginUnitOfWork() as uow:
            # import pdb; pdb.set_trace()
            # uow.login_repository.update(login.IdLogin)
            login.VecesLogin += 1
            login.FechaAcceso = datetime.now()
            uow.login_repository.add(login)

            uow.commit()
        return login.FechaAcceso
    except UnauthorizedException as exc:
        logger.exception(exc)
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
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