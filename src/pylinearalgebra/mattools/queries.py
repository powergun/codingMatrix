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
    m = sympy.Matrix(zip(*vectors))
    r, i_pivots = m.rref()
    return r.columns() == len(i_pivots)


def row_space(mat):
    m = sympy.Matrix(mat)
    return m.rref()[0].rowspace()


def col_space(mat):
    m = sympy.Matrix(mat)
    return m.rref()[0].columnspace()


def null_space(mat):
    m = sympy.Matrix(mat)
    return m.rref()[0].nullspace()


def left_null_space(mat):
    m = sympy.Matrix(mat)
    r, _ = m.rref()
    return r.transpose().nullspace()
