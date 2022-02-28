from operator import imod
from typing import Any
from sqlalchemy.sql.expression import false, true
from sqlalchemy.sql import select, and_

from common.db.base import BaseRepository
from model.domain.cliente_model import ClienteModel

class ClienteRepository(BaseRepository):
    def __init__(self, session) -> None:
        super().__init__()
        self.session = session

    def get(self, id: int) -> Any:
        return self.session.query(ClienteModel).filter_by(Id=id).first()
        
    def add(self, cliente_model):
        self.session.add(cliente_model)
        self.session.flush()
        self.session.refresh(cliente_model)