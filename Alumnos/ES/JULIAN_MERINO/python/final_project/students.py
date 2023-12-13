#File to define customer class
class Student:
    nif: str
    name: str
    surname: str
    phone: str
    email: str
    passed: bool

    def __init__(self, nif, name, surname, phone, email, passed):
        self.nif = nif
        self.name = name
        self.surname = surname
        self.phone = phone
        self.email = email
        self.passed = passed