from operator import imod
from typing import Any
from sqlalchemy.sql.expression import false, true
from sqlalchemy.sql import select, and_

from common.db.base import BaseRepository
from model.domain.cat_estatus_sol_model import CatEstatusSolicitudModel

class EstatusSolicitudRepository(BaseRepository):
    def __init__(self, session) -> None:
        super().__init__()
        self.session = session

    def get(self, id: int) -> Any:
        return self.session.query(CatEstatusSolicitudModel).filter_by(Id=id).first()
        
    def add(self, estatus_solicitud_model):
        self.session.add(estatus_solicitud_model)
        self.session.flush()
        self.session.refresh(estatus_solicitud_model)