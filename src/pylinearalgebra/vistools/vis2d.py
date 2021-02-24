import itertools
import random

import matplotlib.pyplot as plt


class XY:
    def __init__(self, x_lim=None, y_lim=None, is_matplotlib_inline=True):
        random.seed(42)
        self._colors = random.shuffle('rgb')
        self._color_it = itertools.cycle(self._colors)

    def color(self):
        return next(self._color_it)

    def point(self, p, p_text=None):
        pass

    def line(self, fr, to, fr_text=None, to_text=None, shaft_text=None):
        pass

    def vector(self, fr, to, fr_text=None, to_text=None, shaft_text=None):
        pass
