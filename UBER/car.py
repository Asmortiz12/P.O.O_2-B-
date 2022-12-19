from accountDriver import Driver

class Car(Driver):
    placa   = str
    modelo  = str
    color   = str
    año     = int
    driver  = Driver("", "", "", "", "", "")

    def __init__(self, placa, modelo, color, año, driver):
        self.driver     = driver
        self.placa      = placa
        self.modelo     = modelo
        self.color      = color
        self.año        = año