from car import Car

class UberXL(Car):
    asientos  =  int

    def __init__(self, placa, modelo, color, año, Driver, asientos):
        super().__init__(placa, modelo, color, año, Driver)
        self.asientos = asientos