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
        self.red=int(r)
        self.green=int(g)
        self.blue=int(b)

    def __str__(self):
        return f'{self.red} {self.green} {self.blue}'

    def __repr__(self):
        return f'{self.red} {self.green} {self.blue}'

    def get_html_rgb_value(self):
        return f'rgb({self.red},{self.green},{self.blue})'
    
    def get_average(self):
        return (self.red+self.green+self.blue)//3

def get_n_most_common_colors(
    image_path:str,
    colors_count:int,
):
    '''
    < image_path: str
        full image path as string 
    < colors_count: int 
        number of most common colors to return for a given image 

    > palette: list[Color]
        has length of colors_count
        each element is a Color object with values for red, green and blue as ints
    '''

    # Read an image, get it into an object to work with
    image=img.imread(image_path)
    # Read image's width, height, depth
    w,h,d=tuple(image.shape)
    # Get a pixel size by reshaping the image into rows
    pixel=np.reshape(image,(w*h,d))
    # Make a K-Means algorithm model, fit it into a pixel
    model=KMeans(n_clusters=colors_count,random_state=40).fit(pixel)
    # Make a colors palette by extracting cluster centers from the model
    palette=np.uint8(model.cluster_centers_)
    # Make a list for storing Colors data
    res=[]
    # Go through each color in palette, colors_count times
    for c in palette:
        # Extract the red, green and blue values for each color
        r,g,b=c
        # Make and add a Color object for the colors
        res.append(Color(r,g,b))
    # Return the produced list of Colors
    return res

def get_colors_dataset(
    images_folder:str,
    image_files:list[str],
):
    colors_dataset=dict()
    for image_file_name in image_files:
        image_path=os.path.join(images_folder,image_file_name)
        this_image_colors=get_n_most_common_colors(
            image_path=image_path,
            colors_count=colors_count
        )
        colors_dataset[image_file_name]=this_image_colors
    return colors_dataset

def get_average_colors(
    colors_dataset:dict,
):
    def get_average_color(
        colors:list[Color]
    ):
        return round(sum([c.get_average() for c in colors])/len(colors))

    return {name:get_average_color(colors) for name,colors in colors_dataset.items()}

ROOT_FOLDER=os.path.dirname(os.path.abspath(__file__))
IMAGE_FOLDER_PATH=os.path.join(ROOT_FOLDER,'images')
IMAGE_FILE_NAMES=os.listdir(IMAGE_FOLDER_PATH)

LABEL_CLASSES='font-medium text-lg'
COLOR_CLASSES='flex-1 py-7 rounded-md'

app.add_media_files('/images',IMAGE_FOLDER_PATH)
image_file=IMAGE_FILE_NAMES[0]
colors_count=3

image_colors=get_colors_dataset(IMAGE_FOLDER_PATH,IMAGE_FILE_NAMES)
average_image_colors=get_average_colors(image_colors)

def update_image_output():
    results_image.source=os.path.join(IMAGE_FOLDER_PATH,image_file)

def update_colors():
    colors_count_label.text=f'The image has {colors_count} most common color{"s" if colors_count>1 else ""}'

    image_average_color=average_image_colors[image_file]
    colors_list=list(set((image_name,color_value) for image_name,color_value in average_image_colors.items() if color_value<=image_average_color and image_name!=image_file))
    closest_colors=sorted(
        colors_list,
        key=lambda color: color[1],
        reverse=True
    )

    this_image_colors:list[Color]=image_colors[image_file]
    closest_color_one.style(f'background: {this_image_colors[0].get_html_rgb_value()};')
    closest_color_two.style(f'background: {this_image_colors[1].get_html_rgb_value()};')
    closest_color_two.visible=colors_count>=2
    closest_color_three.style(f'background: {this_image_colors[2].get_html_rgb_value()};')
    closest_color_three.visible=colors_count>=3

    closest_color_image_paths=[
        os.path.join(IMAGE_FOLDER_PATH,this_file_name) for this_file_name,this_color_value in closest_colors
    ]
    similar_image_one.source=closest_color_image_paths[0]
    similar_image_two.source=closest_color_image_paths[1]
    similar_image_three.source=closest_color_image_paths[2]

def update_ui():
    update_image_output()
    update_colors()

ui.label('Image to process').classes(LABEL_CLASSES)
ui.select(
    options=IMAGE_FILE_NAMES,
    with_input=True,
    value=image_file,
    on_change=update_ui,
).classes('w-full').bind_value(globals(),'image_file')

ui.label('Number of colors').classes('mt-7 '+LABEL_CLASSES)
ui.slider(
    min=1,
    max=3,
    value=colors_count,
    on_change=update_ui,
).bind_value(globals(),'colors_count')
with ui.row().classes('flex justify-between w-full'):
    ui.label(1)
    ui.label(2)
    ui.label(3)

ui.label(f'Results for {image_file}').classes('mt-12 '+LABEL_CLASSES)
results_image=ui.image(os.path.join(IMAGE_FOLDER_PATH,image_file)).classes('rounded-md object-center').style('max-height: 37vh;')

colors_count_label=ui.label(f'Most common colors ({colors_count})').classes('mt-7 '+LABEL_CLASSES)
with ui.row().classes('w-full flex gap-3'):
    closest_color_one=ui.element('span').classes(COLOR_CLASSES)
    closest_color_two=ui.element('span').classes(COLOR_CLASSES)
    closest_color_three=ui.element('span').classes(COLOR_CLASSES)

ui.label(f'Images with similar colors').classes('mt-7 '+LABEL_CLASSES)
with ui.row().classes('w-full flex gap-3'):
    similar_image_one=ui.image().classes('flex-1 rounded-md max-h-60 display-cover')
    similar_image_two=ui.image().classes('flex-1 rounded-md max-h-60 display-cover')
    similar_image_three=ui.image().classes('flex-1 rounded-md max-h-60 display-cover')

update_ui()
ui.run(favicon='🖼️',title='Image Colors')