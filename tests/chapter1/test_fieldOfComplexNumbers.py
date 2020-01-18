import numbers
import math
import cmath

import unittest


class TestComplexNumberArithmatics(unittest.TestCase):
    def test_multiply(self):
        a = 1 + 3j
        b = -2 + 6j
        self.assertEqual(-20, a * b)  # 1 * -2 + 1 * 6j + 3j * -2 + 3j * 6j

    def test_eulersFormula(self):
        self.assertAlmostEqual(0,
                               cmath.exp(1j * math.pi) +
                               1)  # e ^ (i.pi) + 1 = 0
