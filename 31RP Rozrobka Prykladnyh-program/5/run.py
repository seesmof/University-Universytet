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
colors_count=3

images_folder=os.path.join(ROOT_FOLDER,'images')
app.add_media_files('/images',images_folder)
image_files=os.listdir(images_folder)
image_file=image_files[0]
image_colors=get_colors_dataset(
    images_folder=images_folder,
    image_files=image_files
)
average_image_colors=get_average_colors(image_colors)

def update_image_output():
    results_image.source=os.path.join(images_folder,image_file)
    results_image.update()

ui.label('Image to process').classes(LABEL_CLASSES)
ui.select(
    options=image_files,
    with_input=True,
    value=image_file,
    on_change=update_image_output,
).classes('w-full').bind_value(globals(),'image_file')

ui.label('Number of colors').classes('mt-7 '+LABEL_CLASSES)
ui.slider(
    min=1,
    max=3,
    value=colors_count
).bind_value(globals(),'colors_count')

image_average_color=average_image_colors[image_file]
closest_colors=sorted(
    ((image_name,color_value) for image_name,color_value in average_image_colors.items() if color_value<=image_average_color and image_name!=image_file),
    key=lambda color: color[1],
    reverse=True
)

ui.label(f'Results for {image_file}').classes(LABEL_CLASSES)
results_image=ui.image(os.path.join(images_folder,image_file))

ui.label(f'Most common colors ({colors_count})').classes('mt-7 '+LABEL_CLASSES)
with ui.row().classes('w-full flex gap-3'):
    ui.element('span').classes('flex-1 py-5 rounded-md').style('background: #37bf37;')
    ui.element('span').classes('flex-1 py-5 rounded-md').style('background: #7359eb;') if colors_count>=2 else None
    ui.element('span').classes('flex-1 py-5 rounded-md').style('background: #779bef;') if colors_count>=3 else None

closest_color_image_paths=[
    os.path.join(images_folder,this_file_name) for this_file_name,this_color_value in closest_colors[:3]
]
ui.label(f'Images with similar colors').classes('mt-7 '+LABEL_CLASSES)
with ui.row().classes('w-full flex gap-3'):
    ui.image(closest_color_image_paths[0]).classes('flex-1 rounded-md h-full display-cover')
    ui.image(closest_color_image_paths[1]).classes('flex-1 rounded-md h-full display-cover')
    ui.image(closest_color_image_paths[2]).classes('flex-1 rounded-md h-full display-cover')

ui.run(favicon='🖼️',title='Image Colors')