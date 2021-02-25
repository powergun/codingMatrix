import numpy as np
import scipy.linalg as la
import sympy


def rank(mat):
    m = sympy.Matrix(mat)
    return m.rank()


def dim(space):
    rows = list(zip(*space))
    m = sympy.Matrix(rows)
    r, i_pivots = m.rref()
    return len(i_pivots)


def bases(space):
    """
    Params:
        space: a list of column vectors
    """
    rows = list(zip(*space))
    m = sympy.Matrix(rows)
    r, i_pivots = m.rref()
    return [r[pivot] for pivot in i_pivots]


def is_basis(vectors):
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
    r, i_pivots = m.rref()
    return r.cols == len(i_pivots) 


def row_space(mat, tolist=False):
    m = sympy.Matrix(mat)
    space = m.rref()[0].rowspace()
    if tolist:
        return [list(v) for v in space]
    return space

def col_space(mat, tolist=False):
    m = sympy.Matrix(mat)
    space = m.rref()[0].columnspace()
    if tolist:
        return [list(v) for v in space]
    return space

def null_space(mat, tolist=False):
    m = sympy.Matrix(mat)
    space = m.rref()[0].nullspace()
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