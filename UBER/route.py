class Route():
    start        =[int, int]
    end          =[int, int]
    distanciaKm  = int
    timeAprox    = int
    def __init__(self, start, end, distanciaKm, timeAprox):
        self.start         = start
        self.end           = end
        self.distanciaKm   = distanciaKm
        self.timeAprox     = timeAprox
 