class Payment():
    id     = str
    valor  = float
    fecha  = int

    def __init__(self, id, valor, fecha):
        self.id    = id
        self.valor = valor
        self.fecha = fecha