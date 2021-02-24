import unittest

import numpy

from pyLinearAlgebra.pycodingmatrix.chapter2 import vectorUtils


class TestCrossProduct(unittest.TestCase):
    def _sequenceAlmostEqual(self, s1, s2, places=7):
        self.assertEqual(len(s1), len(s2), msg='{} != {}'.format(s1, s2))
        for idx in range(len(s1)):
            self.assertAlmostEqual(s1[idx],
                                   s2[idx],
                                   places=places,
                                   msg='idx {}, v1 {} != v2 {}'.format(
                                       idx, s1[idx], s2[idx]))

    def test_expectResultPerpendicular(self):
        actual = vectorUtils.cross_product_f3([1.5, 0, -13],
                                              [-31.2, 0.4, 1.31413])
        expected = numpy.cross([1.5, 0, -13], [-31.2, 0.4, 1.31413])
        self._sequenceAlmostEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
