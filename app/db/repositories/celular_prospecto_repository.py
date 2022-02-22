from operator import imod
from typing import Any
from sqlalchemy.sql.expression import false, true
from sqlalchemy.sql import select, and_

from common.db.base import BaseRepository
from model.domain.celular_prospecto_model import CelularProspectoModel

class CelularProspectoRepository(BaseRepository):
    def __init__(self, session) -> None:
        super().__init__()
        self.session = session

    def get(self, id: int) -> Any:
        return self.session.query(CelularProspectoModel).filter_by(Id=id).first()
        
    def add(self, celular_prospecto_model):
        self.session.add(celular_prospecto_model)