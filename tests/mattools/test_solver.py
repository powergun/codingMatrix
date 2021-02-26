import unittest
import numpy as np
import pylinearalgebra.mattools as mt


class TestCanSolve(unittest.TestCase):
    def test_can_solve_Ab(self):
        # a solvable system (b3 - b2 - b1 = 0)
        A = [
          [1, 2, 2, 2],
          [2, 4, 6, 8],
          [3, 6, 8, 10],
        ]
        b = [1, 5, 6]
        self.assertTrue(mt.can_solve(A, b))
    
    def test_can_not_solve_Ab(self):
        # a non-solvable system (b3 - b2 - b1 != 0)
        A = [
          [1, 2, 2, 2],
          [2, 4, 6, 8],
          [3, 6, 8, 10],
        ]
        b = [0, 5, 6]
        self.assertFalse(mt.can_solve(A, b))


class TestFindNullspaceSolutions(unittest.TestCase):
    def test_expect_number_of_solutions(self):
        A = [
            [1, 2, 2, 2],
            [2, 4, 6, 8],
            [3, 6, 8, 10]
        ]
        solutions = mt.solve_rn(A)
        self.assertEqual(2, len(solutions))

    def test_expect_solution_vectors(self):
        A = [
            [1, 2, 2, 2],
            [2, 4, 6, 8],
            [3, 6, 8, 10]
        ]
        solutions = mt.solve_rn(A)
        self.assertEqual([[-2, 0, 1, 0], [2, -2, 0, 1]], solutions)

    def test_transpose_expect_solution_vectors(self):
        A = [
            [1, 2, 2, 2],
            [2, 4, 6, 8],
            [3, 6, 8, 10]
        ]
        AT = mt.T(A)
        solutions = mt.solve_rn(AT)
        self.assertEqual([[-1, -1, 1, 0]], solutions)

    def test_chapter1_problem1(self):
        # source:
        # MIT18_06SCF11_Ses1.1prob_The_Geometry_of_Linear_Equations

        A = [
            [1, 4, 7],
            [2, 5, 8],
            [3, 6, 9]
        ]
        solutions = mt.solve_rn(A)
        self.assertEqual(solutions, [[1, -2, 1, 0]])


if __name__ == '__main__':
    unittest.main()