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
    print(colors_dataset)
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

LABEL_CLASSES='font-medium text-lg'
COLOR_CLASSES='flex-1 py-7 rounded-md'

colors_count=3

app.add_media_files('/images',IMAGE_FOLDER_PATH)
image_files=os.listdir(IMAGE_FOLDER_PATH)
image_file=image_files[0]
image_colors=get_colors_dataset(
    images_folder=IMAGE_FOLDER_PATH,
    image_files=image_files
)
average_image_colors=get_average_colors(image_colors)

def update_image_output():
    results_image.source=os.path.join(IMAGE_FOLDER_PATH,image_file)
    results_image.update()

def update_colors():
    colors_count_label.text=f'Most common colors ({colors_count})'
    colors_count_label.update()

    image_average_color=average_image_colors[image_file]
    colors_list=list(set((image_name,color_value) for image_name,color_value in average_image_colors.items() if color_value<=image_average_color and image_name!=image_file))
    print(colors_list)
    closest_colors=sorted(
        colors_list,
        key=lambda color: color[1],
        reverse=True
    )

    closest_color_image_paths=[
        os.path.join(IMAGE_FOLDER_PATH,this_file_name) for this_file_name,this_color_value in closest_colors
    ]
    similar_image_one.source=closest_color_image_paths[0]
    similar_image_one.update()
    similar_image_two.source=closest_color_image_paths[1]
    similar_image_two.update()
    similar_image_three.source=closest_color_image_paths[2]
    similar_image_three.update()

def update_ui():
    update_image_output()
    update_colors()

ui.label('Image to process').classes(LABEL_CLASSES)
ui.select(
    options=image_files,
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
results_image=ui.image(os.path.join(IMAGE_FOLDER_PATH,image_file)).classes('max-h-96 rounded-md object-center')

colors_count_label=ui.label(f'Most common colors ({colors_count})').classes('mt-7 '+LABEL_CLASSES)
with ui.row().classes('w-full flex gap-3'):
    closest_color_one=ui.element('span').classes(COLOR_CLASSES).style('background: #37bf37;')
    closest_color_two=ui.element('span').classes(COLOR_CLASSES).style('background: #7359eb;') if colors_count>=2 else None
    closest_color_three=ui.element('span').classes(COLOR_CLASSES).style('background: #779bef;') if colors_count>=3 else None

ui.label(f'Images with similar colors').classes('mt-7 '+LABEL_CLASSES)
with ui.row().classes('w-full flex gap-3'):
    similar_image_one=ui.image().classes('flex-1 rounded-md max-h-60 display-cover')
    similar_image_two=ui.image().classes('flex-1 rounded-md max-h-60 display-cover')
    similar_image_three=ui.image().classes('flex-1 rounded-md max-h-60 display-cover')

update_ui()
ui.run(favicon='🖼️',title='Image Colors')