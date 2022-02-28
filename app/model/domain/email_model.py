import re
# Make a regular expression for validating an Email
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

class EmailModel:
    def __init__(self):
        self.IdEmail: int
        self.Email: str

    # Define a function for validating an Email
    def email_valido(self) -> bool:
        if(re.fullmatch(regex, self.Email)):
            return True
        else:
            return False