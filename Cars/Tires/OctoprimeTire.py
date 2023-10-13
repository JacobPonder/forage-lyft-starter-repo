import numpy as np

from Cars.Tires.Tire import Tire


class OctoprimeTire(Tire):
    def __init__(self, frontR: float, frontL: float, backR: float, backL: float):
        self.wear_array = [frontR, frontL, backR, backL]

    def needs_service(self):
        total = 0.0
        for tire in self.wear_array:
            total += tire
        if total >= 3:
            return True
        else:
            return False
