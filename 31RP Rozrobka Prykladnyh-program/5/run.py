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

def get_colors_dataset(
    images_folder:str,
    image_files:list[str],
):
    colors_dataset=dict()
    for image_file_name in image_files:
        image_path=os.path.join(images_folder,image_file_name)
        image_colors=get_colors(
            image_path=image_path,
            colors_count=colors_count
        )
        colors_dataset[image_file_name]=image_colors
    return colors_dataset

def get_average_colors(
    colors_dataset:dict,
):
    return {name:round(colors.mean()) for name,colors in colors_dataset.items()}

ROOT_FOLDER=os.path.dirname(os.path.abspath(__file__))
LABEL_CLASSES='font-medium text-lg'

images_folder=os.path.join(ROOT_FOLDER,'images')
app.add_media_files('/images',images_folder)
image_files=os.listdir(images_folder)
colors_count=3
image_colors=get_colors_dataset(
    images_folder=images_folder,
    image_files=image_files
)
average_image_colors=get_average_colors(image_colors)

ui.label('Image to process').classes(LABEL_CLASSES)
selected_image_file=ui.select(
    options=image_files,
    value=image_files[0],
    with_input=True
).classes('w-full')

ui.label('Number of colors').classes('mt-7 '+LABEL_CLASSES)
ui.slider(min=1,max=3,value=colors_count).bind_value(globals(),'colors_count')

with ui.dialog() as result, ui.card():
    ui.label('Results here')
    ui.label(str(average_image_colors))
    ui.label(colors_count)
    ui.button('AMEN',on_click=result.close)

ui.button('AMEN',on_click=result.open)

ui.run(favicon='🖼️',title='Image Colors')