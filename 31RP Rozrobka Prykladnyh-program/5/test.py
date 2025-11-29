from nicegui import ui 

from sklearn.cluster import KMeans
import numpy as np 
import matplotlib.pyplot as plt 
import matplotlib.image as img

def get_colors(
    image_path:str,
):
    image=img.imread(image_path)
    w,h,d=tuple(image.shape)
    pixel=np.reshape(image,(w*h,d))

    n_colors=3
    model=KMeans(n_clusters=n_colors,random_state=40).fit(pixel)
    palette=np.uint8(model.cluster_centers_)
    return palette

image_path=r'E:\Universytet\31RP Rozrobka Prykladnyh-program\5\images\mountains_landscape_mountain_nature.jpg'
palette=get_colors(image_path)
print(palette,round(palette.mean()))
plt.imshow([palette])
plt.show()

for color in palette:
    r,g,b=color
    print(r,g,b)