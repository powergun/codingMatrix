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
    return r


def gauss_jordan(mat):
    # assert whether mat is square and invertible

    return rref(mat)


def T(mat):
    pass


def inverse(mat):
    """
    Returns:
        tuple: is_success, inverse matrix
    """
    return False, None
