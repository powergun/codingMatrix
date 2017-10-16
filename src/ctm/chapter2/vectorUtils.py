

def cross_product_f3(p, q):
    """
    computes the cross product of two float-3 vectors

    | i   j   k  |
    | p.x p.y p.z|
    | q.x q.y q.z|

    i * p.y * q.z, j * p.z * q.x, k * p.x * q.y - i * p.z * q.y, j * p.x * q.z, k * p.y * q.x

    Args:
        p (list):
        q (list):

    Returns:
        list:
    """
    class _Vector(object):

        def __init__(self, x, y, z):
            self.x = x
            self.y = y
            self.z = z

        def to_list(self):
            return [self.x, self.y, self.z]

        def __str__(self):
            return str(self.to_list())

        def sub(self, other):
            return _Vector(*(self.x - other.x, self.y - other.y, self.z - other.z))

    p = _Vector(*p)
    q = _Vector(*q)
    i = 1
    j = 1
    k = 1
    lhs = _Vector(*(i * p.y * q.z, j * p.z * q.x, k * p.x * q.y))
    rhs = _Vector(*(i * p.z * q.y, j * p.x * q.z, k * p.y * q.x))
    return lhs.sub(rhs).to_list()
