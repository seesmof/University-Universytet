import math
import pandas as pd
import numpy as np

MX, MY = 10.0, 20.0
sigma_x, sigma_y = 0.7, 0.9
r1, r2 = -0.7, -0.9
X_vals = [12.1, 11.4, 10.0, 8.6]


def joint_density(x, y, mu_x=MX, mu_y=MY, sx=sigma_x, sy=sigma_y, rho=r1):
    denom = 2 * math.pi * sx * sy * math.sqrt(1 - rho**2)
    z = (
        ((x - mu_x) / sx) ** 2
        - 2 * rho * ((x - mu_x) / sx) * ((y - mu_y) / sy)
        + ((y - mu_y) / sy) ** 2
    )
    exponent = -z / (2 * (1 - rho**2))
    return math.exp(exponent) / denom


def normal_pdf(y, mu, sigma):
    return (1 / (sigma * math.sqrt(2 * math.pi))) * math.exp(
        -0.5 * ((y - mu) / sigma) ** 2
    )


def conditional_params(x, rho):
    mu_cond = MY + rho * (sigma_y / sigma_x) * (x - MX)
    var_cond = sigma_y**2 * (1 - rho**2)
    sigma_cond = math.sqrt(var_cond)
    return mu_cond, sigma_cond


# 2.3.3: D[Δy] = D[y](1 - r^2)
rs = np.round(np.arange(0, 1.01, 0.1), 2)
Dy = sigma_y**2
Dy_factors = [Dy, 2 * Dy, 4 * Dy]
rows = []
for Dy_factor in Dy_factors:
    for r in rs:
        error_var = Dy_factor * (1 - r**2)
        rows.append({"Dy_factor": Dy_factor, "r": r, "D_error": error_var})

table_2_3_3 = pd.DataFrame(rows)
