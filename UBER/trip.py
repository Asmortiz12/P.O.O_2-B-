from car import Car
from accountDriver import Driver
from accountUser   import User
from route import Route
from payment import Payment

class Trip(Car, Driver, User, Route, Payment):
    idTrip  = int
    car     = Car("", "", "", "", "")
    driver  = Driver("", "", "", "", "", "")
    user    = User("", "", "", "", "")
    route   = Route("", "", "", "")
    payment = Payment("", "", "")

    def __init__(self, idTrip, user, driver, car, route, payment):
       self.idTrip  = idTrip
       self.car     = car
       self.driver  = driver
       self.user    = user
       self.route   = route
       self.payment = payment

