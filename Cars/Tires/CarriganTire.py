import numpy as np

from Cars.Tires.Tire import Tire


class CarriganTire(Tire):
    def __init__(self, frontR: float, frontL: float, backR: float, backL: float):
        self.wear_array = [frontR, frontL, backR, backL]

    def needs_service(self):
        for tire in self.wear_array:
            if tire >= 0.9:
                return True
        return False
