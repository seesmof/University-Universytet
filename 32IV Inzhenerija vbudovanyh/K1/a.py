# Calculating PPI

from math import sqrt


resolution: str = "3840|2160"
width,height = resolution.split("|")
width,height = int(width), int(height)
size: int = 28

formula=(sqrt(width**2+height**2))/(size)
print(formula)

pixels_per_cm=formula*2.54
print(pixels_per_cm)

line_length_px=50
line_length_mm=pixels_per_cm/line_length_px
line_length_cm=line_length_mm/10
print(line_length_cm)

print(width**2+height,sqrt(width**2+height**2))