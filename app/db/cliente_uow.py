from fastapi.applications import FastAPI
from common.db.unit_of_work import AbstractUnitOfWork, DEFAULT_SESSION_FACTORY
from db.repositories.cliente_repository import ClienteRepository
from db.repositories.direccion_cliente_repository import DireccionClienteRepository
from db.repositories.prospecto_repository import ProspectoRepository

class ClienteUnitOfWork(AbstractUnitOfWork):
    

    def __enter__(self, session_factory = DEFAULT_SESSION_FACTORY):
        self.session = session_factory(expire_on_commit=False)
        self.prospecto_repository = ProspectoRepository(self.session)
        self.cliente_repository = ClienteRepository(self.session)
        self.direccion_repository = DireccionClienteRepository(self.session)
        return self

    def __exit__(self, *args):
        super().__exit__(*args)
        self.session.close()  #(3)

    def commit(self):  #(4)
        self.session.commit()

    def rollback(self):  #(4)
        self.session.rollback()