from accountDriver import Driver

class Car(Driver):
    placa   = str
    modelo  = str
    color   = str
    año     = int

    def __init__(self, placa, modelo, color, año, Driver):
        super().__init__(Driver)
        self.placa      = placa
        self.modelo     = modelo
        self.color      = color
        self.año        = año