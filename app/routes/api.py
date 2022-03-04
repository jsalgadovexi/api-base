from fastapi import APIRouter

from routes import controller, solicitud, login, cliente

api_router = APIRouter()
api_router.include_router(controller.router, tags=["pruebas"], prefix="/base")
api_router.include_router(solicitud.router, tags=["originación"], prefix="/solicitud")
api_router.include_router(login.router, tags=["login"], prefix="/auth")
api_router.include_router(cliente.router, tags=["clientes"], prefix="/clientes")