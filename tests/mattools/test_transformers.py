
import unittest

import numpy as np
import sympy

from pylinearalgebra.mattools.transformers import rref


class TestRREF(unittest.TestCase):

    def test_return_numpy_array(self):
        arr = [[1, 1], [0, 0]]
        np_arr = np.array(arr)
        r, i_pivots = rref(np_arr)
        self.assertEqual(i_pivots.shape, (1, ))
        self.assertEqual(r.shape, (2, 2))   
    
    def test_return_python_list(self):
        arr = [[1, 1], [0, 0]]
        r, i_pivots = rref(arr)
        self.assertEqual(i_pivots, [0])
        self.assertEqual(r, arr)  

    def test_return_sympy_matrix(self):
        arr = [[1, 1], [0, 0]]
        m = sympy.Matrix(arr)
        r, i_pivots = rref(m)
        self.assertEqual(r.rows, 2)
        self.assertEqual(i_pivots, (0, ))
