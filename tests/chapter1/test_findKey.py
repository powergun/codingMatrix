import unittest
import string

data = [
    '10101', '00100', '10101', '01011', '11001', '00011', '01011', '10101',
    '00100', '11001', '11010'
]


def to_binary(w):
    return eval('0b{}'.format(w))


class Pad(object):
    def __init__(self, mask):
        self._mask = mask

    def __call__(self, binary):
        return (binary ^ self._mask) % 27


class TestCrackOneTimePad(unittest.TestCase):
    """
    P93 Problem 1.5.1

    eve is evil

    the one-time pad function is f(x) = (x ^ 17) % 27
    """
    def test_(self):
        """
        Uses a brutal force method
        """
        results = list()
        for i in range(31):
            results.append(''.join([
                (string.ascii_lowercase + ' ')[Pad(i)(to_binary(d))]
                for d in data
            ]))
        self.assertTrue('eve is evil' in results)
