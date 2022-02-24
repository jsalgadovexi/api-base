from operator import ne
from typing import Any, List
from fastapi import HTTPException
from loguru import logger
from starlette import status

from db.solicitud_uow import EmailUnitOfWork, ProspectoUnitOfWork
from model.domain.celular_prospecto_model import CelularProspectoModel
from model.domain.direccion_prospecto_model import DireccionProspectoModel

from model.domain.email_model import EmailModel

import requests
from model.domain.prospecto_model import ProspectoModel

from model.rest import ProspectoRequest

HTTP_SESSION = requests.Session()

def registrar_email_prospecto(email: str)->int:
    try:
        with EmailUnitOfWork() as uow:
            # import pdb; pdb.set_trace()
            new_model = EmailModel()
            new_model.Email = email
            uow.email_repository.add(new_model)
            uow.commit()
        return new_model.IdEmail
    except Exception as exc:
        logger.exception(exc)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(exc),
            headers={"WWW-Authenticate": "Bearer"},
        )

def registrar_prospecto(prospecto: ProspectoRequest)->List[int]:
    try:
        with ProspectoUnitOfWork() as uow:
            # import pdb; pdb.set_trace()
            new_model_email = EmailModel()
            new_model_prospecto = ProspectoModel()
            new_model_celular = CelularProspectoModel()
            new_model_direccion = DireccionProspectoModel()

            SOLICITUD_EN_PROCESO = 1

            new_model_email.Email = prospecto.email

            new_model_prospecto.PrimerNombre = prospecto.primer_nombre
            new_model_prospecto.SegundoNombre = prospecto.segundo_nombre
            new_model_prospecto.ApellidoPaterno = prospecto.ap_paterno
            new_model_prospecto.ApellidoMaterno = prospecto.ap_materno
            new_model_prospecto.FechaNacimiento = prospecto.fecha_nac
            new_model_prospecto.RFC = prospecto.RFC
            new_model_prospecto.CURP = prospecto.CURP
            new_model_prospecto.IdEstatusSolicitud = SOLICITUD_EN_PROCESO

            uow.email_repository.add(new_model_email)
            
            new_model_prospecto.IdEmail = new_model_email.IdEmail
            uow.prospecto_repository.add(new_model_prospecto)

            new_model_celular.Telefono = prospecto.telefono
            new_model_celular.IdSolicitud = new_model_prospecto.IdProspecto
            uow.celular_repository.add(new_model_celular)

            new_model_direccion.Calle = prospecto.calle
            new_model_direccion.IdSolicitud = new_model_prospecto.IdProspecto
            uow.direccion_repository.add(new_model_direccion)

            uow.commit()
        return [new_model_email.IdEmail, new_model_prospecto.IdProspecto, new_model_celular.IdTelefono, new_model_direccion.IdDireccion]
    except Exception as exc:
        logger.exception(exc)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(exc),
            headers={"WWW-Authenticate": "Bearer"},
        )