import numpy as np
import matplotlib.pyplot as plt
from rich.console import Console
from rich.traceback import install
from scipy.optimize import minimize_scalar

install()
console = Console()


def f(x):
    return (x - 2) ** 2


def quadraticApproximation(p1, p2, p3):
    v1, v2, v3 = f(p1), f(p2), f(p3)
    return (
        0.5
        * ((v2 - v1) * (p3**2 - p1**2) - (v3 - v1) * (p2**2 - p1**2))
        / ((v2 - v1) * (p3 - p1) - (v3 - v1) * (p2 - p1))
    )


def searchPowell(p1, step, epsilon):
    points = [p1]
    while True:
        p2 = p1 + step
        v1, v2 = f(p1), f(p2)
        p3 = p1 + 2 * step if v1 > v2 else p1 - step
        v3 = f(p3)
        vMin, pMin = min((v1, p1), (v2, p2), (v3, p3))
        pPrime = quadraticApproximation(p1, p2, p3)

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


def main() -> None:
    bounds: tuple[float, float] = (-1, 3)

    with console.status("Optimizing...", spinner="point"):
        pMin, vMin, points = searchPowell(-1, 0.1, 1e-6)
        resPowell = f"{pMin:.2f}"
        resScalar: float = f"{minimize_scalar(f, bounds).x:.2f}"

    console.print(f"Powell's Method: {resPowell}")
    console.print(f"Scalar Method: {resScalar}")
    console.print()
    console.print(
        "[green bold]Correct answer found![/green bold]"
        if resPowell == resScalar
        else "[red bold]Doesn't match![/red bold]"
    )

    def drawResults():
        x = np.linspace(-1, 3, 100)
        plt.figure(figsize=(10, 6))
        plt.plot(x, f(x), label="f(x) = (x-2)^2")
        plt.plot(points, [f(p) for p in points], "ro-", label="Powell's Method")
        plt.plot(pMin, vMin, "go", label="Powell's Minimum")
        plt.title("Visualization of Powell's Method for function (x-2)^2")
        plt.xlabel("x")
        plt.ylabel("f(x)")
        plt.legend()
        plt.show()

    drawResults()


if __name__ == "__main__":
    main()
