from sklearn.cluster import KMeans
import matplotlib.image as img
from nicegui import ui, app
import numpy as np 
import os

'''
get an image from user 
get a number of colors from user 
get a list of N colors for the image: select the most common colors (maybe a slider between 1 and 3)
show images with same colors 
'''

def get_colors(
    image_path:str,
    colors_count:int,
):
    image=img.imread(image_path)
    w,h,d=tuple(image.shape)
    pixel=np.reshape(image,(w*h,d))

    model=KMeans(n_clusters=colors_count,random_state=40).fit(pixel)
    palette=np.uint8(model.cluster_centers_)
    return palette

root=os.path.dirname(os.path.abspath(__file__))
images_folder=os.path.join(root,'images')
app.add_media_files('/images',images_folder)
image_files=os.listdir(images_folder)

def update_image():
    print(image_file)
    ui.update(image)
image_file=image_files[0]
image=ui.image(f'/images/{image_file}')
image_file=ui.input(
    label='File name here...',
    value=image_files[0],
    autocomplete=image_files,
    on_change=update_image()
).classes('w-full')

ui.label('Number of colors').classes('mt-7')
colors_count_slider=ui.slider(min=1,max=3,value=3)
with ui.row().classes('flex justify-between w-full'):
    ui.label(1)
    ui.label(2)
    ui.label(3)

ui.run(favicon='🖼️',title='Image Colors')