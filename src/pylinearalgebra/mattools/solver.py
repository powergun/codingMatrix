import numpy as np
import sympy
import scipy.linalg as la

from pylinearalgebra.mattools.list_utils import flatten
from pylinearalgebra.mattools.transformers import rref_IFZ


def can_solve(A, b):
    A = np.array(A)
    b = np.array(b)
    Aaug = sympy.Matrix([np.append(A[i], x) for i, x in enumerate(b)])
    R, i_pivots = Aaug.rref()
    # test the condition:
    for i in range(A.shape[0]):
        lhs = sum(R.row(i)[:-1])
        rhs = R.row(i)[-1]
        if lhs == 0 and rhs != 0:
            return False
    return True


# this is still buggy!
def solve_rn(mat):
    I, F, _ = rref_IFZ(mat)
    F_neg = F * -1
    # N
    # each column of N holds a solution {x1, x2, x3, x4}

    # it's good to iterate over the shape of F-inv
    # I've added another example below when F-inv has less columns
    # than I;
    # Gilbert also shows that example in the video
    solutions = []
    for col_idx in range(F_neg.cols):
        solution = []
        for row_idx in range(F_neg.rows):
            row = F_neg.row(row_idx)
            solution.append(row[col_idx])
        for row_idx in range(I.shape[0]):
            row = I.row(row_idx)
            solution.append(row[col_idx])
        solutions.append(solution)
    return solutions


def lu(mat):
    A = np.array(mat)
    pl, u = la.lu(A, permute_l=True)
    return pl, u


def plu(mat):
    A = np.array(mat)
    p, l, u = la.lu(A, permute_l=False)
    return p, l, u


if __name__ == '__main__':
    A = [
        [1, 4, 7],
        [2, 5, 8],
        [3, 6, 9]
    ]
    print(solve_rn(A))