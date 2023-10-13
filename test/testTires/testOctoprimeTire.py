import unittest
from datetime import date

from Cars.Tires.OctoprimeTire import OctoprimeTire


class TestOctoprimeTire(unittest.TestCase):
    def test_needs_service_true(self):
        frontR = 0.75
        frontL = 0.75
        backR = 0.75
        backL = 0.75
        tire = OctoprimeTire(frontR, frontL, backR, backL)
        self.assertTrue(tire.needs_service())

    def test_needs_service_false(self):
        frontR = 0.74
        frontL = 0.75
        backR = 0.75
        backL = 0.75
        tire = OctoprimeTire(frontR, frontL, backR, backL)
        self.assertFalse(tire.needs_service())
