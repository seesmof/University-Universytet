import os
import matplotlib.image as img 
import matplotlib.pyplot as plt 
from scipy.cluster.vq import whiten, kmeans
import pandas as pd

image_path=r'E:\Universytet\31RP Rozrobka Prykladnyh-program\5\landscape_red_thurm_schwyz.jpg'
image=img.imread(image_path)
print(image)

r,g,b=[],[],[]
for row in image:
    for tr,tg,tb,t in row:
        r.append(tr)
        g.append(tg)
        b.append(tb)

print(r,g,b)