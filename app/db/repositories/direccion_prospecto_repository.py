from operator import imod
from typing import Any
from sqlalchemy.sql.expression import false, true
from sqlalchemy.sql import select, and_

from common.db.base import BaseRepository
from model.domain.direccion_prospecto_model import DireccionProspectoModel

class DireccionProspectoRepository(BaseRepository):
    def __init__(self, session) -> None:
        super().__init__()
        self.session = session

    def get(self, id: int) -> Any:
        return self.session.query(DireccionProspectoModel).filter_by(Id=id).first()
        
    def add(self, direccion_prospecto_model):
        self.session.add(direccion_prospecto_model)