from operator import imod
from typing import Any
from loguru import logger
from sqlalchemy.sql.expression import false, true
from sqlalchemy.sql import select, and_

from common.db.base import BaseRepository
from model.domain.email_model import EmailModel
from model.domain.prospecto_model import ProspectoModel
from model.rest import ClienteRequest

class ProspectoRepository(BaseRepository):
    def __init__(self, session) -> None:
        super().__init__()
        self.session = session

    def get(self, id: int) -> Any:
        return self.session.query(ProspectoModel).filter_by(Id=id).first()

    def get_by_cliente(self, cliente: ClienteRequest) -> Any:
        try:
            id_email = self.session.query(EmailModel).filter_by(Email=cliente.email).first().IdEmail
            return self.session.query(ProspectoModel).filter_by(IdEmail=id_email, CURP=cliente.CURP, RFC=cliente.RFC).first()
        except Exception as exc:
            logger.exception(exc)
        
    def add(self, prospecto_model):
        self.session.add(prospecto_model)
        self.session.flush()
        self.session.refresh(prospecto_model)