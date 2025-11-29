import os
import matplotlib.image as img 
import matplotlib.pyplot as plt 
from scipy.cluster.vq import whiten, kmeans
import pandas as pd

image_path=r'E:\Universytet\31RP Rozrobka Prykladnyh-program\5\landscape_red_thurm_schwyz.jpg'
image=img.imread(image_path)

red,green,blue=[],[],[]
for row in image:
    for current_red,current_green,current_blue in row:
        red.append(current_red)
        green.append(current_green)
        blue.append(current_blue)

df=pd.DataFrame({'red':red,'green':green,'blue':blue})
df['scaled_red']=whiten(df['red'])
df['scaled_green']=whiten(df['green'])
df['scaled_blue']=whiten(df['blue'])

cluster_centers,_=kmeans(df[['scaled_red','scaled_blue','scaled_green']],3)
red_std,green_std,blue_std=df[['red','green','blue']].std()

colors=[]
for red_scaled,green_scaled,blue_scaled in cluster_centers:
    colors.append((red_scaled*red_std/255,green_scaled*green_std/255,blue_scaled*blue_std/255))

# limit number of colors here by selected value from slider
colors_number=3

colors=colors[:3]
plt.imshow([colors])
plt.show()