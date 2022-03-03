
import re
from fastapi import HTTPException, Request
from loguru import logger
from model.errors import FormatException
from starlette import status

from services.constants import REGEX_EMAIL

class ValidateEmail:
    
    def __init__(self, param_name: str = None):
        '''
        Inicializa el validador
        @param_name: es el nombre del parámetro que viene en la ruta
        '''
        self.param_name: str = param_name
    
    def __call__(self, request: Request):
        '''
        Se validara que el correo contenga un formato de correo electronico valido
        @request: Obtiene el valor del parametro.
        '''
        try:
            #import pdb; pdb.set_trace()
            req_correo = str(request.path_params[self.param_name])
            
            if re.fullmatch(REGEX_EMAIL, req_correo):
                logger.info("El correo es valido ")
            else:    
                raise FormatException(description= "El correo {} no tiene formato valido".format(req_correo))            
            
        except FormatException as exc:
            raise HTTPException(
                status_code= status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail= str(exc.description)
            )