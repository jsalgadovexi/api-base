from fastapi.applications import FastAPI
from common.db.unit_of_work import AbstractUnitOfWork, DEFAULT_SESSION_FACTORY
from db.repositories import demo_repository as repository


################################################################################
### Esta clase funciona como un agregado (agreggate) que se encarga de 
### manejar un conjunto de repositorios. Siempre se debe de acceder a los
### repositorios por medio de un agregado, aunque solo sea uno
################################################################################
class SqlAlchemyUnitOfWork(AbstractUnitOfWork):
    

    def __enter__(self, session_factory = DEFAULT_SESSION_FACTORY):
        self.session = session_factory(expire_on_commit=False)
        self.base_repository = repository.DemoRepository(self.session)
        return self

    def __exit__(self, *args):
        super().__exit__(*args)
        self.session.close()  #(3)

    def commit(self):  #(4)
        self.session.commit()

    def rollback(self):  #(4)
        self.session.rollback()
