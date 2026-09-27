# okay starting to copy the code, praise King Jesus! okay it doesnt work again, with some versions problems so yeah, gotta try some different library for working with image classifications, may Jesus Christ our Lord help me.

from imageai.Detection import ObjectDetection
import os

execution_path = os.getcwd()
file_path = os.path.join(execution_path, "data", "resnet50_coco_best_v2.1.0.h5")

detector = ObjectDetection()
detector.setModelTypeAsRetinaNet()
detector.setModelPath(file_path)
detector.loadModel()

face_file_path = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "data", "face.jpg"
)
detections = detector.detectObjectsFromImage(input_image=face_file_path)
output_image_path = os.path.join(execution_path, "image_new.jpg")

for eachObject in detections:
    print(f'{eachObject["name"]}: {eachObject["percentage_probability"]}')
