from sklearn.cluster import KMeans
import matplotlib.image as img
from nicegui import ui, app
import numpy as np 
import os

class Color:
    def __init__(
        self,
        r: int,
        g: int,
        b: int,
    ):
        self.red=r
        self.green=g
        self.blue=b

    def __str__(self):
        return f'{self.red} {self.green} {self.blue}'

    def __repr__(self):
        return f'{self.red} {self.green} {self.blue}'

    def get_html_rgb_value(self):
        return f'rgb({self.red},{self.green},{self.blue})'

def get_n_most_common_colors(
    image_path:str,
    colors_count:int,
):
    '''
    < image_path: str
        full image path as string 
    < colors_count: int 
        number of most common colors to return for a given image 

    > palette: list[list[int]]
        has length of colors_count
        each element is a color in RGB format:
            red_value, green_value, blue_value
    '''

    image=img.imread(image_path)
    w,h,d=tuple(image.shape)
    pixel=np.reshape(image,(w*h,d))

    model=KMeans(n_clusters=colors_count,random_state=40).fit(pixel)
    palette=np.uint8(model.cluster_centers_)

    res=[]
    for c in palette:
        r,g,b=c
        res.append(Color(r,g,b))
    print(res)

    return res

image_file=r'E:\Universytet\31RP Rozrobka Prykladnyh-program\5\images\duck_nature_pond_bird.jpg'
r=get_n_most_common_colors(image_file,3)
print(r)