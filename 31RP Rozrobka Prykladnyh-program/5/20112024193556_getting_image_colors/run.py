import os
from PIL import Image

current_dir=os.path.dirname(os.path.abspath(__file__))
root=os.path.join(current_dir,'..')
image_name='landscape_red_thurm_schwyz.jpg'
image_path=os.path.join(root,image_name)
img = Image.open(image_path)
colors=img.convert('RGB').getcolors()
print(colors)