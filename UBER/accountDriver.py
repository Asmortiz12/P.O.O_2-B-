from account import Account

class Driver(Account):
    licencia : str
    
    def __init__(self, id, nombre, genero, telefono, edad, licencia):
        super().__init__(id, nombre, genero, telefono, edad)
        self.licencia = licencia