from datetime import datetime
from operator import imod
from typing import Any
from loguru import logger
from sqlalchemy.sql.expression import false, true
from sqlalchemy.sql import select, and_

from common.db.base import BaseRepository
from model.domain.email_model import EmailModel
from model.domain.login_model import LoginModel

class LoginRepository(BaseRepository):
    def __init__(self, session) -> None:
        super().__init__()
        self.session = session

    def get(self, id: int) -> Any:
        return self.session.query(LoginModel).filter_by(Id=id).first()

    def get_by_codigo(self, codigo: str) -> Any:
        return self.session.query(LoginModel).filter_by(Codigo=codigo).first()

    def get_validar_codigo(self, email: str, codigo: str) -> Any:
        try:
            id_email = self.session.query(EmailModel).filter_by(Email=email).first().IdEmail
            return self.session.query(LoginModel).filter_by(IdEmail = id_email, Codigo=codigo).first()
        except Exception as exc:
            logger.exception(exc)
        
    def add(self, login_model):
        self.session.add(login_model)
        self.session.flush()
        self.session.refresh(login_model)

    def update(self, id_login):
        return self.session.query(LoginModel).filter_by(IdLogin = id_login).update({LoginModel.FechaAcceso: datetime.now(), LoginModel.VecesLogin: LoginModel.VecesLogin + 1})