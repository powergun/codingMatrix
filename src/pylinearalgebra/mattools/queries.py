import numpy as np
import scipy.linalg as la
import sympy

from pylinearalgebra.mattools import list_utils

def rank(mat):
    m = sympy.Matrix(mat)
    return m.rank()


def dim(space):
    rows = list(zip(*space))
    m = sympy.Matrix(rows)
    r, i_pivots = m.rref()
    return len(i_pivots)


# NOTE:
# this is not right,
# another way to compute the dim but not the basis is to
# use AT
# put these vector into AT and turn them into columns,
# do elimination (I can use rref), calculate the number
# of (column) pivots
# HOWEVER this method does not give me the basis of the
# space these original vectors span!!!
# because while doing elimination on AT, I have changed
# the column space (which IS THE SPACE spanned by the
# original vectors)
# I need to take i_pivots and the columns from AT as
# the basis of the given space
def bases(space):
    """
    Params:
        space: a list of vectors
    """
    AT = sympy.Matrix(space).transpose()
    _, i_pivots = AT.rref()
    return [list_utils.flatten(AT.col(i).tolist()) for i in i_pivots]


# NOTE: the condition for some vectors {v1...vn} to
# form a basis for Rn is different to whether {v1...vn}
# form a basis of C(A) (if A consists of and only of these v)
def is_basis_rn(vectors):
    n_cols = len(vectors)
    n_rows = len(vectors[0]) if vectors else 0
    if n_cols != n_rows:
        return False

    # ok, it is a square matrix
    rows = list(zip(*vectors))
    m = sympy.Matrix(rows)
    try:
        m.inv()
    except:
        return False
    return True


def check_independence(vectors):
    # are these vectors independent?
    # see:
    # https://math.stackexchange.com/questions/421574/how-to-check-if-a-set-of-vectors-is-a-basis
    
    # NOTE: to check whether these vectors form a basis
    #       I need to test whether they are invertible (or
    #       compute their determinant)
    rows = list(zip(*vectors))
    m = sympy.Matrix(rows)

    # if r = n, N(A) must be {Z}
    if rank(m) == len(vectors):
        return len(null_space(m, tolist=True)) == 0
    
    # if r < n, there will be free variables, which produce
    # non-zero solutions in N(A)
    return False


# NOTE: this function actually returns the basis of C(AT)
def row_space(mat, tolist=False):
    m = sympy.Matrix(mat)
    space = m.rref()[0].rowspace()
    if tolist:
        return [list(v) for v in space]
    return space

# it returns the basis of C(A)
def col_space(mat, tolist=False):
    m = sympy.Matrix(mat)
    space = m.rref()[0].columnspace()
    if tolist:
        return [list(v) for v in space]
    return space

def null_space(mat, tolist=False):
    m = sympy.Matrix(mat)
    space = m.nullspace()
    if tolist:
        return [list(v) for v in space]
    return space

def left_null_space(mat, tolist=False):
    m = sympy.Matrix(mat)
    r, _ = m.rref()
    space = r.transpose().nullspace()
    if tolist:
        return [list(v) for v in space]
    return space