import string
import unittest

from pycodingmatrix.chapter0 import caesarCypher


class TestCaesarCypher(unittest.TestCase):
    def setUp(self):
        self.op = caesarCypher.CaesarCypher()

    def test_g(self):
        for i in range(26):
            i_ = self.op.g(i)
            self.assertEqual(i, self.op.g_(i_))

    def test_word(self):
        w = 'THEREISACOW'
        w_ = self.op.do(w)
        self.assertEqual(w, self.op.undo(w_))

    def test_allAlphabeticCharacters(self):
        for C in string.ascii_uppercase:
            C_ = self.op.do(C)
            self.assertEqual(C, self.op.undo(C_))
