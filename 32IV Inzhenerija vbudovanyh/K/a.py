# Calculating PPI

from math import sqrt


resolution: str = "3840|2160"
width,height = resolution.split("|")
width,height = int(width), int(height)
size: int = 28

formula=(sqrt(width**2+height**2))/(size)
print(formula)

PPI=157.3505121487356