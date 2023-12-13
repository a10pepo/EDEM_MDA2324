#File to define customer class
class Customer:
    nif: str
    name: str
    surname: str
    phone: str
    email: str
    preferent: bool

    def __init__(self, nif, name, surname, phone, email, preferent):
        self.nif = nif
        self.name = name
        self.surname = surname
        self.phone = phone
        self.email = email
        self.preferent = preferent