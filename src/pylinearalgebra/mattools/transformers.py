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

    
    if I is not None:
        assert len(mat) == len(I), 'I must have the same shape as the source matrix!'
        mat = [row + irow for row, irow in zip(mat, I)]
    
    m = sympy.Matrix(mat)
    r, i_pivots = m.rref()

    # may convert m back the type of mat for convenience

    if isinstance(mat, list):
        return r.tolist(), list(i_pivots)
    if isinstance(mat, np.ndarray):
        return np.array(r), np.array(i_pivots)
    return r, i_pivots


def T(mat):
    if isinstance(mat, list):
        return sympy.Matrix(mat).transpose().tolist()
    if isinstance(mat, np.ndarray):
        return mat.transpose()
    if isinstance(mat, sympy.Matrix):
        return mat.transpose()
    raise ValueError('unsupported format')


def inverse(mat):
    """
    Returns:
        tuple: is_success, inverse matrix
    """
    def _sympy_inv(m):
        try:
            m_inv = m.inv()
        except sympy.matrices.common.NonInvertibleMatrixError:
            return False, None
        return True, m_inv
    
    if isinstance(mat, list):
        ok, m_inv = _sympy_inv(sympy.Matrix(mat))
        if ok:
            return ok, m_inv.tolist()
        return False, None

    if isinstance(mat, np.ndarray):
        ok, m_inv = _sympy_inv(sympy.Matrix(mat))
        if ok:
            return ok, np.array(m_inv)
        return False, None

    if isinstance(mat, sympy.Matrix):
        return _sympy_inv(mat)

    raise ValueError('unsupported format')
