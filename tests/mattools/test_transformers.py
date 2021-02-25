import unittest

import numpy as np
import sympy

from pylinearalgebra.mattools.transformers import T, inverse, rref


class TestInverse(unittest.TestCase):
    def test_invertible(self):
        self.assertTrue(inverse([1])[0])
        self.assertTrue(inverse([
            [1, 0, 0],
            [0, 1, 0],
            [0, 0, 1]
        ])[0])

    def test_non_invertible(self):
        self.assertFalse(inverse([0])[0])
        self.assertFalse(inverse([
            [1, 0, 0],
            [0, 1, 0],
            [0, 0, 0]
        ])[0])


class TestTranspose(unittest.TestCase):
    def test_1d_transpose(self):
        arr = [1, 0, 3]
        t = T(arr)
        self.assertEqual(t, [[1, 0, 3]])

        t2 = T([[1], [0], [3]])
        self.assertEqual(t2, [[1, 0, 3]])

    def test_2d_transpose(self):
        arr = [
            [1, 3],
            [5, 9]
        ]
        t = T(arr)
        self.assertEqual(t, [[1, 5], [3, 9]])


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

    def test_with_identity_expect_rref_augmented(self):
        arr = [
            [1, 2, 1,  2],
            [3, 4, 5,  3],
            [1, 1, -1, -1],
        ]
        I = [
            [1, 0, 0],
            [0, 1, 0],
            [0, 0, 1]
        ]
        r, i_pivots = rref(arr, I=I)
        self.assertTrue(r)
        self.assertEqual(i_pivots, [0, 1, 2])
