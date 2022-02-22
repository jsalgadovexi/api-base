from operator import ne
from typing import Any
from fastapi import HTTPException
from loguru import logger
from starlette import status

from db.solicitud_uow import EmailUnitOfWork

from model.domain.email_model import EmailModel

import requests

HTTP_SESSION = requests.Session()

def registrar_email_prospecto(email: str)->int:
    with EmailUnitOfWork() as uow:
        new_model = EmailModel()
        new_model.Email = email
        uow.email_repository.add(new_model)
        uow.commit()
    return new_model.IdEmail