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
        
        self.assertFalse(mt.is_basis(vectors))

    def test_column_space_basis(self):
        # see 18.06 notebook:
        # 18.06_09_independence_basis_and_dimension

        m = [
            [1, 2, 3, 1],
            [1, 1, 2, 1],
            [1, 2, 3, 1]
        ]
        vectors = mt.col_space(m, tolist=True)
        # this is actually the basis of the col space
        self.assertEqual(vectors,
            [[1, 0, 0], [0, 1, 0]])

    def test_column_space_dimension(self):
        m = [
            [1, 2, 3, 1],
            [1, 1, 2, 1],
            [1, 2, 3, 1]
        ]
        vectors = mt.col_space(m, tolist=True)
        self.assertEqual(2, mt.dim(vectors))


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

    def test_nullspace_dimension(self):
        # see 18.06 notebook:
        # 18.06_09_independence_basis_and_dimension
        m = [
            [1, 2, 3, 1],
            [1, 1, 2, 1],
            [1, 2, 3, 1]
        ]
        vectors = mt.null_space(m, tolist=True)

        # dimN(A) = n - r
        # n is 4 (num columns)
        self.assertEqual(2, mt.dim(vectors))

    def test_nullspace(self):
        # see 18.06 notebook
        # 18.06_12_graphs_networks_incidence_matrices
        m = [
            [-1, 1, 0, 0],
            [0, -1, 1, 0],
            [-1, 0, 1, 0],
            [-1, 0, 0, 1],
            [0, 0, -1, 1]
        ]
        vectors = mt.null_space(m, tolist=True)
        self.assertEqual([[1, 1, 1, 1]], vectors)

class TestLeftNullspace(unittest.TestCase):
    def test_left_nullspace_dimension(self):
        # see 18.06 notebook
        # 18.06_12_graphs_networks_incidence_matrices
        m = [
            [-1, 1, 0, 0],
            [0, -1, 1, 0],
            [-1, 0, 1, 0],
            [-1, 0, 0, 1],
            [0, 0, -1, 1]
        ]
        vectors = mt.left_null_space(m, tolist=True)
        self.assertEqual(2, mt.dim(vectors))
        # dimN(AT) = m - r = 5 - 3 = 2


class TestRowspace(unittest.TestCase):
    def test_row_space_dimension(self):
        # see 18.06 notebook
        # 18.06_12_graphs_networks_incidence_matrices
        m = [
            [-1, 1, 0, 0],
            [0, -1, 1, 0],
            [-1, 0, 1, 0],
            [-1, 0, 0, 1],
            [0, 0, -1, 1]
        ]
        vectors = mt.row_space(m, tolist=True)
        self.assertEqual(3, mt.dim(vectors))
        # dimC(AT) = r = 3 (2 free columns)