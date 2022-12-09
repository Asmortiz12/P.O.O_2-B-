from account import Account

class User(Account):
    def __init__(self, id, nombre, genero, telefono, edad):
        super().__init__(id, nombre, genero, telefono, edad)