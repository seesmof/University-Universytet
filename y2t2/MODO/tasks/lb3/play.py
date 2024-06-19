import numpy as np
import matplotlib.pyplot as plt
from rich.console import Console
from rich.traceback import install
from scipy.optimize import minimize_scalar

install()
console = Console()


def quadraticApproximation(p1, p2, p3, f):
    v1, v2, v3 = f(p1), f(p2), f(p3)
    return (
        0.5
        * ((v2 - v1) * (p3**2 - p1**2) - (v3 - v1) * (p2**2 - p1**2))
        / ((v2 - v1) * (p3 - p1) - (v3 - v1) * (p2 - p1))
    )


def searchPowell(p1, step, epsilon, f):
    points = [p1]
    while True:
        p2 = p1 + step
        v1, v2 = f(p1), f(p2)
        p3 = p1 + 2 * step if v1 > v2 else p1 - step
        v3 = f(p3)
        vMin, pMin = min((v1, p1), (v2, p2), (v3, p3))
        pPrime = quadraticApproximation(p1, p2, p3, f)
        points.append(pPrime)
        if abs(vMin - f(pPrime)) < epsilon and abs(pMin - pPrime) < epsilon:
            return pMin, vMin, points
        p1, p2, p3 = sorted(
            [
                pMin,
                pPrime,
                pMin + step if pMin == pPrime else pMin - step,
            ]
        )


def getResults(f, start=-1, end=3, step=0.1, epsilon=1e-6):
    pMin, vMin, points = searchPowell(start, step, epsilon, f)

    def drawResults():
        x = np.linspace(start, end, 100)
        plt.figure(figsize=(10, 6))
        plt.plot(x, f(x), label="f(x)")
        plt.plot(points, [f(p) for p in points], "ro-", label="Powell's Method")
        plt.plot(pMin, vMin, "go", label="Powell's Minimum")
        plt.title("Visualization of Powell's Method")
        plt.xlabel("x")
        plt.ylabel("f(x)")
        plt.legend()
        plt.show()

    scalar = f"{minimize_scalar(f, (start, end)).x:.2f}"
    powell = f"{pMin:.2f}"
    console.print(f"{start = }, {end = }, {scalar = }, {powell = }, {powell==scalar}")
    drawResults()


def runTests():
    def HALLELUJAH_HALLELUJAH_HALLELUJAH(x):
        return (2 * x + 1) ** 2 * (x - 4)

    def GLORY_TO_JESUS_CHRIST(x):
        return (x - 2) ** 2

    data = [
        (GLORY_TO_JESUS_CHRIST, -1, 3),
        (HALLELUJAH_HALLELUJAH_HALLELUJAH, -1, 5),
        (lambda x: x**4 - 12 * x + 3, -4, 4),
        (lambda x: x * np.cos(x) * np.sin(x), 0.5, 2),
        (lambda x: np.sqrt(x**2 - x + np.exp(x)), -2, 2),
        (lambda x: 3 * x**4 + (x - 1) ** 2, -1, 4),
    ]
    for f, start, end in data:
        console.print(start, end)
        getResults(f, start, end)
        console.print()


def main():
    runTests()


if __name__ == "__main__":
    main()
