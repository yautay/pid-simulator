import numpy as np
import matplotlib.pyplot as plt


class Battery:
    def __init__(self, cells_no, capacity, chemistry):
        self.__cells_no = cells_no
        self.__chemistry = chemistry
        self.__curve = self.__discharge_curve()
        self.__capacity = capacity

    def __discharge_curve(self):
        if self.__chemistry == "lipo":

            return np.array([(0, 3.2),
                             (1, 3.65),
                             (2, 3.68),
                             (3, 3.7),
                             (6, 3.76),
                             (7, 3.82),
                             (8, 3.95),
                             (9, 4.0),
                             (10, 4.2)], dtype="float32")
        if self.__chemistry == "life":
            return np.array([(0, 2.5),
                             (1, 3.1),
                             (2, 3.2),
                             (7, 3.3),
                             (9, 3.3),
                             (10, 3.6)], dtype="float32")

    def voltage(self, state):
        curve = self.__curve
        cells = self.__cells_no
        # get x and y vectors
        curve_x = curve[:, 0]
        curve_y = curve[:, 1]

        # calculate polynomial
        z = np.polyfit(curve_x, curve_y, 3)
        f = np.poly1d(z)

        # calculate new x's and y's & plot
        x_new = np.linspace(curve_x[0], curve_x[-1], 100)
        y_new = f(x_new)
        # plt.plot(x_new, y_new)
        # plt.show()
        if state == 0:
            return y_new[0] * cells
        else:
            return y_new[state - 1] * cells

    def capacity(self, state):
        return self.__capacity / 100 * state
