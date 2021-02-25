
import sympy


def _get_shape(mat):
    if isinstance(mat, list):
        return sympy.Matrix(mat).shape
    return mat.shape


def _get_width(x):
    if isinstance(x, float):
        t = f'{x:.02f}'
    else:
        t = str(x)
    return len(t)


def _pprint(x, width=4, pre='', suf='', end='\n'):
    if isinstance(x, float):
        t = f'{x:.02f}'
    else:
        t = str(x)
    print('{}{}{}'.format(pre, t.rjust(width), suf), end=end)


def pprint(mat):
    n_rows, n_cols = _get_shape(mat)
    paren_head = [u'\u23A1', u'\u23A4']
    paren_body = [u'\u23A2', u'\u23A5']
    paren_tail = [u'\u23A3', u'\u23A6']
    parens = []
    if n_rows == 1:
        parens.append(['[', ']'])
    else:
        parens.append(paren_head)
        parens.extend([paren_body] * max(0, n_rows - 2))
        parens.append(paren_tail)
    if n_cols == 1:
        max_width = 0
        for r in mat:
            max_width = max(max_width, _get_width(r))
        for idx, r in enumerate(mat):
            paren = parens[idx]
            _pprint(r, width=max_width + 1, pre=paren[0], suf=paren[1])
    else:
        m = sympy.Matrix(mat)
        max_width = 0
        for i in range(n_rows):
            row = m.row(i)
            for j in range(n_cols):
                max_width = max(max_width, _get_width(row[j]))
        for i in range(n_rows):
            row = m.row(i)
            paren = parens[i]
            _pprint('', width=0, pre=paren[0], end='')
            for j in range(n_cols):
                _pprint(row[j], width =max_width + 1, end=' ')
            _pprint('', width=0, suf=paren[1])
    

if __name__ == '__main__':
    # singleton vector
    pprint([100000])

    # 1d column vector
    pprint([100000, 200000, 30000])

    # 2d matrix
    pprint([
        [100000, 200000, 30000, 1, 1, 1],
        [100000, 200000, 30000, 2, 2, 2],
        [-1, -2, -3, 5, 5, 5]
    ])

    # some 18.06 example
    pprint([
        [-1, 0, 1],
        [0,  1, 1],
        [1, 1, 0]
    ])