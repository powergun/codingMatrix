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


class TestIsBasis(unittest.TestCase):
    def test_vectors_do_not_form_basis(self):
        # see 18.06 notebook:
        # 18.06_09_independence_basis_and_dimension

        # Note, this example came from a "mistake" Gilbert
        # made
        A = [
            [1, 2, 3],
            [1, 2, 3],
            [3, 4, 8],
        ]
        column_vectors = mt.T(A)
        self.assertFalse(mt.is_basis_rn(column_vectors))
        ok, _ = mt.inverse(A)
        # this A is not invertible (two equal rows)
        self.assertFalse(ok)

    def test_vectors_form_basis(self):
        # Gilbert fixed the above mistake with this A
        A = [
            [1, 2, 3],
            [1, 2, 4],
            [3, 4, 8],
        ]
        column_vectors = mt.T(A)
        self.assertTrue(mt.is_basis_rn(column_vectors))


class TestCheckDependence(unittest.TestCase):
    def test_independent(self):
        # see 18.06 notebook:
        # 18.06_09_independence_basis_and_dimension
        m = [
            [11, 1, 2],
            [2, 1, 3],
            [3, 1, 4],
            [4, 1, 5],
        ]
        column_vectors = mt.T(m)
        vectors = mt.null_space(m)
        # nullspace is {Z}
        self.assertFalse(vectors)
        self.assertTrue(mt.check_independence(column_vectors))


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

        # are the original column vectors form a basis ??
        # of C(A) - no, the column space consists of 2
        # vectors only (whereas A has 3 columns)
        self.assertTrue(mt.check_independence(vectors))

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
        vectors = mt.col_space(m, tolist=True)

        # dimN(A) = n - r
        # n is 4 (num columns)
        self.assertEqual(2, 4 - mt.dim(vectors))

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


class TestGetBasesFromSpace(unittest.TestCase):
    def test_given_dependent_vectors_expect_independent_ones(self):
        v1 = np.array([1, 2, 3])
        v2 = np.array([-11, 13, -2])
        space = [
            v1.tolist(), 
            v2.tolist(),
            (v1 + v2).tolist(),
            (v1 * 3).tolist(),
            (v1 * 3 + v2 * -3).tolist(),
        ]
        bases = mt.bases(space)
        self.assertSequenceEqual(bases, [v1.tolist(), v2.tolist()])


if __name__ == '__main__':
    unittest.main()
