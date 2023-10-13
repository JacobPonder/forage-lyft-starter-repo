import unittest
from datetime import date

from Cars.Tires.CarriganTire import CarriganTire


class TestCarriganTire(unittest.TestCase):
    def test_needs_service_true(self):
        frontR = 0.9
        frontL = 0.0
        backR = 0.0
        backL = 0.0
        tire = CarriganTire(frontR, frontL, backR, backL)
        self.assertTrue(tire.needs_service())

    def test_needs_service_false(self):
        frontR = 0.89
        frontL = 0
        backR = 0
        backL = 0
        tire = CarriganTire(frontR, frontL, backR, backL)
        self.assertFalse(tire.needs_service())