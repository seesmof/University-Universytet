import numpy as np
import scipy as sp

VARIANT = 19

M_X = 10.0
M_Y = 20.0
SIGMA_X = 0.7
D_X = SIGMA_X**2
SIGMA_Y = 0.9
D_Y = SIGMA_Y**2
R1 = -0.7
R2 = -0.9
Rs = [R1, R2]
rs = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
X_1 = 12.1
X_2 = 11.4
X_3 = 10.0
X_4 = 8.6
Xs = [X_1, X_2, X_3, X_4]


def w_x_y(x: int, y: int) -> float:
    first_part = 1 / (2 * np.pi * SIGMA_X * SIGMA_Y * np.sqrt(1 - R1**2))
    exponent_outer = -1 * (2 * (1 - R1**2))
    exponent_inner = (
        (x - M_X / SIGMA_X**2)
        - ((2 * R1 * (x - M_X) * (x - M_Y)) / (SIGMA_X * SIGMA_Y))
        + ((y - M_Y) ** 2) / SIGMA_Y**2
    )
    return first_part * np.exp(exponent_outer * exponent_inner)


def w_x(x: int) -> float:
    lower_up = 1
    lower_low = SIGMA_X * np.sqrt(2 * np.pi)

    upper_up = (x - M_X) ** 2
    upper_low = 2 * SIGMA_X**2

    return lower_up / lower_low * np.e ** -(upper_up / upper_low)


def w_y(y: int) -> float:
    lower_up = 1
    lower_low = SIGMA_Y * np.sqrt(2 * np.pi)

    upper_up = (y - M_Y) ** 2
    upper_low = 2 * SIGMA_Y**2

    return lower_up / lower_low * np.e ** -(upper_up / upper_low)


def w_y_from_x(x: int, y: int) -> float:
    first_low = SIGMA_X * np.sqrt(1 - R1**2) * np.sqrt(2 * np.pi)

    second_up = y - (SIGMA_X * M_Y + SIGMA_Y * R1 * (x - M_X)) / SIGMA_X
    second_low = 2 * (SIGMA_X**2) * (1 - R1**2)

    return 1 / first_low * np.exp(-(second_up / second_low))


def m_y_from_x(x: int):
    up = SIGMA_X * M_Y + SIGMA_Y * R1 * (x - M_X)
    return up / SIGMA_X


def d_y_from_x():
    return (SIGMA_X**2) * (1 - R1**2)


def w_y_from_x_j(y: int, x_j: int):
    first_low = SIGMA_Y * np.sqrt(1 - R1**2) * np.sqrt(2 * np.pi)

    second_up = y - m_y_from_x_j(x_j) ** 2
    second_low = 2 * d_y_from_x(x_j)

    return 1 / first_low * np.exp(-(second_up / second_low))


def m_y_from_x_j(x_j: int):
    return M_X + R1 * (SIGMA_Y / SIGMA_X) * (x_j - M_X)


def d_delta_y(delta_y: int | float) -> float:
    return SIGMA_Y**2 * (1 - R1**2)
