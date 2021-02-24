import numpy as np
import sympy

"""all these functions should return the same data type as the
input's: 

numpy.array -> numpy.array
sympy.Matrix -> sympy.Matrix
list -> list
"""


def rref(mat, I=None):
    # if I is produced, create an augmented matrix and then
    # transform it to the reduced row echelon form

    m = sympy.Matrix(mat)
    r, i_pivots = m.rref()

    # may convert m back the type of mat for convenience
    def to_list(m):
        return [m.row(i) for i in range(m.rows())]

    if isinstance(mat, list):
        return to_list(r), list(i_pivots)
    if isinstance(mat, np.ndarray):
        return np.array(to_list(r)), np.array(list(i_pivots))
    return r, i_pivots


def gauss_jordan(mat):
    # assert whether mat is square and invertible

    r, i_pivots = rref(mat)
    return r


def T(mat):
    pass


def inverse(mat):
    """
    Returns:
        tuple: is_success, inverse matrix
    """
    return False, None
