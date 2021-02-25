import numpy as np
import scipy.linalg as la
import sympy


def rank(mat):
    m = sympy.Matrix(mat)
    return m.rank()


def dim(space):
    return len(bases(space))


def bases(space):
    """
    Params:
        space: a list of column vectors
    """
    m = sympy.Matrix(zip(*space))
    r, i_pivots = m.rref()
    return [r[pivot] for pivot in i_pivots]


def is_basis(vectors):
    # are these vectors independent?
    # see:
    # https://math.stackexchange.com/questions/421574/how-to-check-if-a-set-of-vectors-is-a-basis
    rows = list(zip(*vectors))
    m = sympy.Matrix(rows)
    r, i_pivots = m.rref()
    return r.cols == len(i_pivots)


def check_independence(vectors):
    return is_basis(vectors)


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