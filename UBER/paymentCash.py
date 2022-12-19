from payment import Payment

class PaymentCash(Payment):
    def __init__(self, id, valor, fecha):
        super().__init__(id, valor, fecha)
        