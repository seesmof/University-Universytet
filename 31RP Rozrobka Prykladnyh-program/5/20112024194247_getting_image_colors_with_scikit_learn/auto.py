from sklearn.cluster import KMeans
import numpy as np 
import matplotlib.pyplot as plt 
import matplotlib.image as img

image_path=r'E:\Universytet\31RP Rozrobka Prykladnyh-program\5\landscape_red_thurm_schwyz.jpg'
image=img.imread(image_path)

w,h,d=tuple(image.shape)
pixel=np.reshape(image,(w*h,d))

n_colors=3
model=KMeans(n_clusters=n_colors,random_state=40).fit(pixel)
palette=np.uint8(model.cluster_centers_)
print(palette)

plt.imshow([palette])
plt.show()