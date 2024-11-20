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

folder_path=r'E:\Universytet\31RP Rozrobka Prykladnyh-program\5'
images='landscape_red_thurm_schwyz.jpg,landscape_moor_nature_reserve.jpg,nature_reserve_moor_forest_0.jpg'.split(',')
for image in images:
    palette=get_colors(rf'{folder_path}\{image}')
    plt.imshow([palette])
    plt.show()