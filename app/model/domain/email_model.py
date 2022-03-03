import re

from services.constants import REGEX_EMAIL
class EmailModel:
    def __init__(self):
        self.IdEmail: int
        self.Email: str

    # Define a function for validating an Email
    def email_valido(self) -> bool:
        if(re.fullmatch(REGEX_EMAIL, self.Email)):
            return True
        else:
            return False