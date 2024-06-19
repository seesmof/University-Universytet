"""
Cubic approximation method

FIRST WAY:
w_1 - starting point of the interval
start by creating a new w_2 point, such as:
f'(w_1) and f'(w_2) have different signs
IN OTHER WORDS
put a stationary point w* at which f'(w) = 0 in the interval between w_1 and w_2
approximating cubic function is as follows:
f*(w_1)=a_0+a_1(w-w_1)+a_2(w-w_1)(w-w_2)+a_3(w-w_1)^2(w-w_2)
parameters of this function need to be chosen in such a way that f*(w) and its derivatives in w_1 and w_2 would be equal to the values of f(w) and f'(w) at those points

MORE FORMALIZED VIEW:
w_0 - starting point of the interval
step - positive value of the step
epsilon - accuracy of the approximation

STEP 1:
calculate f'(w_0)
if f'(w_0) < 0, calculate w_k+1=w_k+2^k*step for values k from 0 to infinity
if f'(w_0) > 0, calculate x_k+1=w_k-2^k*step for values k from 0 to infinity

STEP 2:
calculate f'(w) in points w_k+1 for k from 0 to point w
where f'(w_M-1)/f'(w)<0
then set w_1=w_M-1, and w_2=w
calculate values of f(w_1), f(w_2), f'(w_1), f'(w_2)

STEP 3:
find stationary point w* of approximating cubic polynomial
w*=w_2 if u<0 else w_2-u(w_2-w_1) if 0<=u<=1 else w_1 if u>1
u=(f'(w_2)+B-z)/(f'(w_z)-f'(w_1)+2B)
z=(3(f'(w_1)-f'(w_2))))/(w_2-w_1)+f'(w_1)+f'(w_2)
B=(z^2-f'(w_1)f'(w_2)^{1/2}) if w_1<w_2 else -(z^2-f'(w_1)f'(w_2)^{1/2}) if w_1>w_2

STEP 4:
if f(w*)<f(w_1), go to STEP 5
else calculate w* using formula w*=w*+0.5*(w*-w_1) until f(w*)<=f(w_1)

STEP 5:
if |f(w*)|<=epsilon, stop the search
else set w_2=w_1 and w_1=w* if f(w*)f'(w_1)<0 else w_1=w* if f'(w*)f'(w_2)<0
go to STEP 3

---

SECOND WAY:
x0 - starting point of the interval
step - positive value of the step
epsilon - accuracy of the approximation

STEP 1:
calculate f'(x0)
if f'(x0) < 0, calculate x_k+1=x_k+2^k*step for values k from 0 to infinity
if f'(x0) > 0, calculate x_k+1=x_k-2^k*step for values k from 0 to infinity

STEP 2:
calculate f'(x) in points x_k+1 for k from 0 to point x_m, where f'(x_m-1)/f'(x_m)<0
then x1=x_m-1, and x1=x_m
calculate values of f1, f2, f'1, f'2

STEP 3:
find stationary point x' approximating cubic polynomial, using formulas:
x'=x1 if u<0 else x1-u(x1-x1) if 0<=u<=1 else x1 if u>1
u=(f'2+w-z)/(f'2-f'1+2w')
z=(3(f1-f2))/(x1-x1)+f'1+f'2
w=(z^2-f'1f'2)^{1/2} if x1<x1 else -(z^2-f'1f'2)^{1/2} if x1>x1

STEP 4:
if f(x')<f(x1), go to STEP 5
else calculate x' using formula x'=x'+(1/(2(x'-x1))) while f(x')<=f(x1)

STEP 5:
if |f'(x')|<=epsilon, stop the search
else set x2=x1 and x1=x' if f'(x')f'(x1)<0 else x1=x' if f'(x')f'(x2)<0
go to STEP 3
"""


def cube(f, start=-1, end=3, step=0.1, epsilon=1e-6):
    import numpy as np

    x_values = np.arange(start, end, step)
    y_values = [f(x) for x in x_values]

    # Fit a cubic polynomial to the data
    coeffs = np.polyfit(x_values, y_values, 3)

    # Find the zero of the polynomial
    roots = np.roots(coeffs)
    real_roots = [
        r
        for r in roots
        if np.imag(r) == 0 and np.real(r) >= start and np.real(r) <= end
    ]
    x_n = min(real_roots, key=abs)

    # Convergence check
    while abs(f(x_n)) > epsilon:
        x_n1 = x_n - np.polyval(coeffs, x_n)
        if abs(x_n1 - x_n) < epsilon:
            break
        x_n = x_n1

    return x_n


def cube(f, start=-1, end=3, step=0.1, epsilon=1e-6):
    import math

    def derivative(f, x, h=1e-6):
        return (f(x + h) - f(x - h)) / (2 * h)

    x0 = start
    f_prime_x0 = derivative(f, x0)

    k = 0
    while True:
        x_k_plus_1 = x0 + 2**k * step if f_prime_x0 < 0 else x0 - 2**k * step
        f_prime_x_k_plus_1 = derivative(f, x_k_plus_1)

        if f_prime_x0 * f_prime_x_k_plus_1 < 0:
            x1, x2 = x0, x_k_plus_1
            f1, f2 = f(x1), f(x2)
            f_prime_1, f_prime_2 = f_prime_x0, f_prime_x_k_plus_1
            break

        x0 = x_k_plus_1
        f_prime_x0 = f_prime_x_k_plus_1
        k += 1

    while True:
        z = 3 * (f1 - f2) / (x1 - x2) + f_prime_1 + f_prime_2
        w = (
            math.sqrt(z**2 - f_prime_1 * f_prime_2)
            if x1 < x2
            else -math.sqrt(z**2 - f_prime_1 * f_prime_2)
        )
        u = (f_prime_2 + w - z) / (f_prime_2 - f_prime_1 + 2 * w)
        x_prime = x1 if u < 0 else x1 - u * (x1 - x2) if 0 <= u <= 1 else x2

        while f(x_prime) > f1:
            x_prime = x_prime + 1 / (2 * (x_prime - x1))

        f_prime_x_prime = derivative(f, x_prime)

        if abs(f_prime_x_prime) <= epsilon:
            return x_prime

        if f_prime_x_prime * f_prime_1 < 0:
            x2 = x1
            x1 = x_prime
        else:
            x1 = x_prime

        f1, f2 = f(x1), f(x2)
        f_prime_1, f_prime_2 = derivative(f, x1), derivative(f, x2)


def cube(f=f, start=-1, end=3, step=0.1, epsilon=1e-6):
    x = start
    while abs(f(x)) > epsilon and x < end:
        x += step
    return x if abs(f(x)) <= epsilon else None


def cube(f=f, start=-1, end=3, step=0.1, epsilon=1e-6):
    """
    Cubic approximation method
    """
    import numpy as np

    x_values = np.arange(start, end, step)
    y_values = [f(x) for x in x_values]

    coeffs = np.polyfit(x_values, y_values, 3)

    roots = np.roots(coeffs)
    real_roots = [r for r in roots if np.imag(r) == 0 and start <= np.real(r) <= end]
    x_star = min(real_roots, key=abs)

    while abs(f(x_star)) > epsilon:
        x_star_new = np.polyval(coeffs, x_star)
        if abs(x_star_new - x_star) < epsilon:
            break
        x_star = x_star - x_star_new

    return x_star
