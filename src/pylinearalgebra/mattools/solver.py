import numpy as np
import sympy


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


def solve_rn(mat):
    A = sympy.Matrix(mat)

    # Return reduced row-echelon form of matrix and
    # indices of pivot vars.
    R, i_pivots = A.rref()
    I = np.identity(len(i_pivots))
    F_rows = []
    for row_idx in range(R.rows):
        row = R.row(row_idx)
        if sum(row) == 0:
            continue
        cols = [
            x for col_idx, x in enumerate(row)
            if col_idx not in i_pivots
        ]
        F_rows.append(cols)
    F = sympy.Matrix(F_rows)
    F_neg = F * -1

    # N
    # each column of N holds a solution {x1, x2, x3, x4}

    # it's good to iterate over the shape of F-inv
    # I've added another example below when F-inv has less columns
    # than I;
    # Gilbert also shows that example in the video
    return [
        [
            F_neg.row(0)[col_idx],
            F_neg.row(1)[col_idx],
            I[0][col_idx],
            I[1][col_idx],
        ]
        for col_idx in range(F_neg.cols)
    ]
