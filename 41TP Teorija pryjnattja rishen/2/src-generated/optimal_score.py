import math

MX, MY = 10.0, 20.0
sigma_x, sigma_y = 0.7, 0.9
r1, r2 = -0.7, -0.9
X_vals = [12.1, 11.4, 10.0, 8.6]


def conditional_params(x, rho):
    mu_cond = MY + rho * (sigma_y / sigma_x) * (x - MX)
    sigma_cond = math.sqrt(sigma_y**2 * (1 - rho**2))
    return mu_cond, sigma_cond


def newton_raphson_mode(start, mu, sigma, tol=1e-6, max_iter=10):
    y = start
    path = [y]
    for _ in range(max_iter):
        diff = y - mu
        denom = diff**2 - sigma**2
        if abs(denom) < 1e-9:
            break
        step = diff / denom
        y -= step
        path.append(y)
        if abs(step) < tol:
            break
    return y, path


def bisection_mode(low, high, mu, sigma, tol=1e-6, max_iter=50):
    left, right = low, high
    path = []
    for _ in range(max_iter):
        mid = 0.5 * (left + right)
        deriv = -(mid - mu) / sigma**2
        path.append(mid)
        if abs(deriv) < tol:
            break
        if deriv > 0:
            right = mid
        else:
            left = mid
    return mid, path


x_target = X_vals[1]  # 11.4
mu_c, sigma_c = conditional_params(x_target, r1)

# Newton–Raphson
start = mu_c + sigma_c
opt_newton, path_nr = newton_raphson_mode(start, mu_c, sigma_c)

# Bisection on derivative (exact for normal)
opt_bisection, path_bi = bisection_mode(
    mu_c - 2 * sigma_c, mu_c + 2 * sigma_c, mu_c, sigma_c
)

print("Умовне середнє:", mu_c)
print("Newton–Raphson:", opt_newton, path_nr)
print("Bisection:", opt_bisection, path_bi)
