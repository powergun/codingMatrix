
import string


class CaesarCypher(object):

    def __init__(self):
        self._Atoi = dict((__, _) for _, __ in
                          enumerate(string.ascii_uppercase))

    def f(self, A):
        return self._Atoi[A]

    def g(self, i):
        return (i + 3) % 26

    def g_(self, i):
        return (i - 3) % 26

    def h(self, i):
        return string.ascii_uppercase[i]

    def do(self, word):
        tokens = []
        for c in word.upper():
            c_ = self.h(self.g(self.f(c)))
            tokens.append(c_)
        return ''.join(tokens)

    def undo(self, word):
        tokens = []
        for c in word.upper():
            c_ = self.h(self.g_(self.f(c)))
            tokens.append(c_)
        return ''.join(tokens)
