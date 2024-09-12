var = 19
n = var * 10
mu = var
sigma = var / 10

print(
    f"N: {n} - number of runs\nM: {mu} - mathematical expectation\nS: {sigma} - dispersion"
)

""" 
description: mean, dispersion, standard deviation, excess, assymmetry, range, median, mode

- use `Rnormal(N, mu, sigma)`
- save to `data.txt`
- build histogram, frequencies table, description
- save to `data.rtf`
- build histogra, frequencies table, description with R internal functions
"""

with open("l1/task_data.yml", "w", encoding="utf-8") as f:
    f.write(f"- N: {n}\n- M: {mu}\n- S: {sigma}")
