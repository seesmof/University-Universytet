import numpy as np
import scipy as sp

VARIANT = 19

MX = 10.0
MY = 20.0
SIGMA_X = 0.7
SIGMA_Y = 0.9
R1 = -0.7
R2 = -0.9
X_1 = 12.1
X_2 = 11.4
X_3 = 10.0
X_4 = 8.6
Xs = [X_1, X_2, X_3, X_4]


def w_x_y(x: int, y: int) -> float:
    first_part = 1 / (2 * np.pi * SIGMA_X * SIGMA_Y * np.sqrt(1 - R2))
    exponent_outer = -1 * (2 * (1 - R2))
    exponent_inner = (
        (x - MX / SIGMA_X**2)
        - ((2 * R1 * (x - MX) * (x - MY)) / (SIGMA_X * SIGMA_Y))
        + ((y - MY) ** 2) / SIGMA_Y**2
    )
    return first_part * np.exp(exponent_outer * exponent_inner)


def w_x(x: int) -> float:
    w_x_y(x, y)
    sp.integrate.quad()


def w_y(y: int) -> float: ...
