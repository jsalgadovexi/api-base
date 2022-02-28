from operator import imod
from typing import Any
from sqlalchemy.sql.expression import false, true
from sqlalchemy.sql import select, and_

from common.db.base import BaseRepository
from model.domain.direccion_cliente_model import DireccionClienteModel

class DireccionClienteRepository(BaseRepository):
    def __init__(self, session) -> None:
        super().__init__()
        self.session = session

    def get(self, id: int) -> Any:
        return self.session.query(DireccionClienteModel).filter_by(Id=id).first()
        
    def add(self, direccion_cliente_model):
        self.session.add(direccion_cliente_model)
        self.session.flush()
        self.session.refresh(direccion_cliente_model)