class Account():
    id       = int
    nombre   = str
    genero   = str
    telefono = int
    edad     = int

    def __init__(self, id, nombre, genero, telefono, edad):
        self.id         = id
        self.nombre     = nombre
        self.genero     = genero
        self.telefono   = telefono
        self.edad       = edad