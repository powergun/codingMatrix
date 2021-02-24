import unittest

import pyLinearAlgebra.pycodingmatrix.chapter2.three_TAs as sut


class TestThreeTAs(unittest.TestCase):
    def test_split(self):
        plaintext = 'there is a cow'
        code = sut.str_to_code(plaintext)
        a, b, c = sut.do_split(code)
        code_ = sut.do_merge(a, b, c)
        text_ = sut.code_to_str(code_)
        self.assertEqual(code, code_)
