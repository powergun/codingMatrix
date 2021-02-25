import numpy as np
import scipy.linalg as la
import sympy


def rank(mat):
    m = sympy.Matrix(mat)
    return m.rank()


def dim(space):
    pass


def bases(space):
    return []


def is_basis(space, vec):
    return False


def row_space(mat):
    m = sympy.Matrix(mat)
    return m.rowspace()


def col_space(mat):
    m = sympy.Matrix(mat)
    return m.columnspace()


def null_space(mat):
    m = sympy.Matrix(mat)
    return m.nullspace()


def left_null_space(mat):
    m = sympy.Matrix(mat)
    return m.transpose().nullspace()
