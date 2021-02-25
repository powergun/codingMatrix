import unittest

import numpy as np
import sympy

import pylinearalgebra.mattools as mt


class TestRank(unittest.TestCase):
    def test_rank_is_n_pivots(self):
        # see 18.06 notebook:
        # 18.06_07_pivot_variables_and_special_solutions

        m = [
            [1, 2, 2, 2],
            [2, 4, 6, 8],
            [3, 6, 8, 10]
        ]
        self.assertEqual(2, mt.rank(m))
        r, i_pivots = mt.rref(m)
        self.assertEqual(2, len(i_pivots))

        # recall that the rank of A-T is the rank of A
        m_t = mt.T(m)
        self.assertEqual(2, mt.rank(m_t))


class TestNullspace(unittest.TestCase):
    def test_vectors_in_null_space(self):
        m = [
            [1, 1, 2],
            [2, 1, 3],
            [3, 1, 4],
            [4, 1, 5]
        ]
        vectors = mt.null_space(m, tolist=True)
        self.assertEqual(
            vectors,
            [[-1, -1, 1]]
        )


class TestColumnspace(unittest.TestCase):
    def test_vectors_in_column_space(self):
        # see 18.06 notebook:
        # 18.06_06_column_space_and_nullspace
        m = [
            [1, 1, 2],
            [2, 1, 3],
            [3, 1, 4],
            [4, 1, 5],
        ]
        vectors = mt.col_space(m, tolist=True)
        self.assertEqual(vectors[0], [1, 0, 0, 0])
        self.assertEqual(vectors[1], [0, 1, 0, 0])
        self.assertTrue(mt.check_independence(vectors))
        self.assertTrue(mt.is_basis(vectors))
