from sqlalchemy import (
    Table,
    MetaData,
    Column,
    Integer,
    String,
    Date,
)
from sqlalchemy.orm import mapper, relationship
from sqlalchemy.sql.expression import false
from model.domain.base_model import BaseModel

metadata = MetaData()
################################################################################
### Se debe de realizar el mapeo entre clases de negocio y la base de datos
### el mapeo se hace del modo "tradicional" de SQLAlquemy
################################################################################
tabla_ejemplo = Table(
    "tbc_hawk_alert",
    metadata,
    Column("idHawkAlert", Integer, primary_key=True, autoincrement=True),
    Column("C_FechaReporte", Date, nullable=True),
    Column("C_CodigoClave", Integer, nullable=True),
    Column("C_TipoInstitucion", String(45), nullable=True),
    Column("C_Mensaje", String(60), nullable=True),
    Column("BD_CodigoClave", Integer, nullable=True),
    Column("BD_TipoInstitucion", String(45), nullable=True),
    Column("BD_Mensaje", String(60), nullable=True),
    Column("fbid", String(20), nullable=False),
    Column("idRespuesta", Integer, nullable=True),
)

################################################################################
### Este método se llama al inicio del programa, no se debe de cambiar el
### nombre de la función y debe de contener todos los mapeos
################################################################################
def start_mappers():
    mapper(BaseModel, tabla_ejemplo, properties={
        'Id': tabla_ejemplo.c.idHawkAlert,
        'FechaReporte': tabla_ejemplo.c.C_FechaReporte,
        'CodigoClave': tabla_ejemplo.c.C_CodigoClave,
        'TipoInstitucion': tabla_ejemplo.c.C_TipoInstitucion,
        'Mensaje': tabla_ejemplo.c.C_Mensaje,
        'FacebookId': tabla_ejemplo.c.fbid,
        'Respuesta': tabla_ejemplo.c.idRespuesta,
    })
