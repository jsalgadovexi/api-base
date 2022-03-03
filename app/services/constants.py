# GUARDAR LAS CONSTANTES DEL SISTEMA
import re

SOLICITUD_EN_PROCESO = 1
REGEX_EMAIL = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')