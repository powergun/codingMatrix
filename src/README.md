# Source Tree

## Structure

### pycodingmatrix 

source code for Coding the Matrix book exercises

### symbolic

demo and helpers for expressing linear alegbra mathematic concepts
in Latex and Markdown

### vistools

helpers that simplify drawing matrix and graph related elements
with matplotlib, such as `vector(from, to)`; **primarily used by 18.06 notebooks**.

### mattools

helpers that implement various query or transformer functions such as
`rank(), bases(), dim(), rref()`. Most of them wrap one or more
existing functions from scipy, numpy or sympy.

sources:

```text
https://scipy-cookbook.readthedocs.io/items/RankNullspace.html
https://stackoverflow.com/questions/27176453/scipy-find-bases-of-column-space-of-matrix
https://docs.scipy.org/doc/numpy-1.10.0/reference/generated/numpy.linalg.qr.html
https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.null_space.html
https://numpy.org/doc/stable/reference/generated/numpy.linalg.matrix_rank.html

https://en.wikipedia.org/wiki/Singular_value_decomposition
```
