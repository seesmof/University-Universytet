from rich.console import Console
from rich.traceback import install

install()
console = Console()


from scipy import integrate
import numpy as np

x = np.arange(10, 14.25, 0.25)
y = np.arange(3, 12)
console.print(integrate.romb(y))

y = np.sin(np.power(x, 2.5))
console.print(integrate.romb(y))

console.print(integrate.romb(y, show=True))
