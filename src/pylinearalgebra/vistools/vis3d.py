import numpy as np

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

import math


class XYZ:
    def __init__(self):
        self.plt = plt
        self.fig = self.plt.figure()
        self.ax = self.fig.gca(projection='3d')
        self.ax.auto_scale_xyz(1.0, 1.0, 1.0)
        self.ax.set_xlabel('$X$', fontsize=20)
        self.ax.set_ylabel('$Y$', fontsize=20)
        self.ax.set_zlabel('$Z$', fontsize=20)
        self.ax.set_box_aspect([1, 1, 1])

    def plane(self, a, b, c, d=0, alpha=0.4, show_normal=None):
        x = np.linspace(-10, 10, 10)
        y = np.linspace(-10, 10, 10)

        X, Y = np.meshgrid(x, y)
        Z = (d - a * X - b * Y) / c

        self.ax.plot_surface(X, Y, Z, alpha=alpha)

        if show_normal:
            start = (0, 0, 0)
            l = math.sqrt(a * a + b * b + c * c)
            normal_n = [a / l, b / l, c / l]
            sz = 30
            somewhere = [
                x - x_ for x, x_ in zip(start, [n * sz for n in normal_n])
            ]
            self.ax.plot([start[0], somewhere[0]], [start[1], somewhere[1]],
                         [start[2], somewhere[2]], 'r--')

    def vector(self, fr, to):
        soa = np.array([
            list(fr) + list(to)
        ])
        X, Y, Z, U, V, W = zip(*soa)
        self.ax.quiver(X, Y, Z, U, V, W, length=0.4)
    
    def line_seg(self, fr, to, style='K-'):
        self.ax.plot(
            [fr[0], to[0]], [fr[1], to[1]], [fr[2], to[2]], style)


if __name__ == '__main__':
    xyz = XYZ()
    xyz.plane(1, 1, -1, show_normal=True)
    xyz.line_seg((0, 0, 0), (14, 14, 28), 'g--')
    plt.show()