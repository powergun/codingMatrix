import itertools
import random

import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

class XY:
    def __init__(self, x_lim=None, y_lim=None, names=None):
        random.seed(42)

        # matplotlib color names:
        # https://matplotlib.org/3.1.0/gallery/color/named_colors.html

        if not names:
            names = list(mcolors.BASE_COLORS) + \
                list(mcolors.TABLEAU_COLORS)
            self._colors = names
            random.shuffle(self._colors)
        else:
            self._colors = names

        self._color_it = itertools.cycle(self._colors)
        self._x_lim = x_lim or (-4, 4)
        self._y_lim = y_lim or (-4, 4)

        ax = plt.gca()
        ax.set_aspect(1.0)

        plt.axhline(0, color='black', alpha=0.3)
        plt.axvline(0, color='black', alpha=0.3)

        plt.xlim(self._x_lim[0], self._x_lim[1])
        plt.ylim(self._y_lim[0], self._y_lim[1])

    def color(self):
        return next(self._color_it)

    def line(self,
            #
            fr,
            to,
            alpha=None,
            color=None,
            ):
        if not color:
            color = self.color()
        plt.plot(
            [fr[0], to[0]],
            [fr[1], to[1]],
            color=color,
            alpha=alpha,
        )

    def fx(self,
            #
            xs,
            f,
            color=None,
            alpha=None,
        ):
        if not color:
            color = self.color()
        plt.plot(
            xs,
            [f(x) for x in xs],
            color=color,
            alpha=alpha,
        )

    def vector(
            #
            self,
            fr,
            to,
            fr_text=None,
            to_text=None,
            shaft_text=None,
            alpha=None,
            text_alpha=0.65,
            shaft_arrow=False,
            color=None,
            ):
        vert = [fr[0], fr[1], to[0] - fr[0], to[1] - fr[1]]
        half = [vert[0], vert[1], vert[2] / 2.0, vert[3] / 2.0]
        c = color or self.color()
        if shaft_arrow:
            plt.arrow(
                *half,
                head_width=0.15,
                head_length=0.4,
                overhang=1.0,
                color=c,
                alpha=alpha,
            )
            plt.arrow(
                *vert,
                head_width=0,
                head_length=0,
                length_includes_head=True,
                overhang=1.0,
                color=c,
                alpha=alpha,
            )
        else:
            plt.arrow(
                *vert,
                head_width=0.15,
                head_length=0.4,
                length_includes_head=True,
                overhang=1.0,
                color=c,
                alpha=alpha,
            )
        if fr_text is None and len(fr) > 2 and isinstance(fr[2], str):
            fr_text = fr[2]

        if fr_text:
            plt.annotate(
                fr_text,
                [fr[0], fr[1]],
                size=20,
                alpha=text_alpha)

        if shaft_text:
            plt.annotate(
                shaft_text,
                [half[0] + half[2], half[1] + half[3]],
                size=20,
                alpha=text_alpha)

        return self


if __name__ == '__main__':
    xy = XY(x_lim=(-0.5, 4), y_lim=(-0.5, 2))
    node1 = [1, 1, '1']
    node2 = [0, 0, '2']
    node3 = [2, 0, '3']
    node4 = [3.3, 0.4, '4']
    xy.vector(node1, node2, shaft_text='(1)')
    xy.vector(node1, node3, shaft_text='(3)')
    xy.vector(node2, node3, shaft_text='(2)')
    xy.vector(node3, node4, shaft_text='(5)')
    xy.vector(node1, node4, shaft_text='(4)')
    plt.show()