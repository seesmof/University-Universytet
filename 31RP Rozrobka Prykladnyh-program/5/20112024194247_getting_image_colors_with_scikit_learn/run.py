import os
import matplotlib.image as img 
import matplotlib.pyplot as plt 
from scipy.cluster.vq import whiten, kmeans
import pandas as pd

image_path=r'E:\Universytet\31RP Rozrobka Prykladnyh-program\5\landscape_red_thurm_schwyz.jpg'
image=img.imread(image_path)

r,g,b=[],[],[]
for row in image:
    for current_red,current_green,current_blue in row:
        r.append(current_red)
        g.append(current_green)
        b.append(current_blue)

print(len(r),len(g),len(b))

df=pd.DataFrame({'red':r,'green':g,'blue':b})
df['scaled_color_red']=whiten(df['red'])
df['scaled_color_blue']=whiten(df['blue'])
df['scaled_color_green']=whiten(df['green'])

cluster_centers,_=kmeans(df[['scaled_color_red','scaled_color_blue','scaled_color_green']],3)
dominant_colors=[]
red_std,green_std,blue_std=df[['red','green','blue']].std()
for center in cluster_centers:
    red_scaled,green_scaled,blue_scaled=center
    dominant_colors.append((red_scaled*red_std/255,green_scaled*green_std/255,blue_scaled*blue_std/255))

# limit number of colors here by selected value from slider
colors_number=3
dominant_colors=dominant_colors[:3]
plt.imshow([dominant_colors])
plt.show()