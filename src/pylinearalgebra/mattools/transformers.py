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

def rref_IFZ(mat):
    # decompose R to [I,   F]
    #                [*0, *0]
    # F can be empty if mat is full column rank
    # the zero row(s) are optional
    A = sympy.Matrix(mat)
    R, i_pivots = A.rref()
    
    R_cleaned = []
    Z = []
    for row_idx in range(R.rows):
        row = R.row(row_idx)
        is_zero_row = all([x == 0 for x in row])
        if is_zero_row:
            Z.append(row)
        else:
            R_cleaned.append(row)

    I = []
    F = []
    for row in R_cleaned:
        I_row = []
        F_row = []
        for col_idx in range(R.cols):
            x = row[col_idx]
            if col_idx in i_pivots:
                I_row.append(x)
            else:
                F_row.append(x)
        I.append(I_row)
        F.append(F_row)
    return sympy.Matrix(I), sympy.Matrix(F), sympy.Matrix(Z)
        


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


if __name__ == '__main__':
    A = [
        [1, 4, 7],
        [2, 5, 8],
        [3, 6, 9]
    ]
    I, F, Z = rref_IFZ(A)
    print(I)
    print(F)
    print(Z)
