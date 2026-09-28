import os
import cv2
import random
from ultralytics import YOLO
from PIL import Image

current_dir = os.path.dirname(os.path.abspath(__file__))
face_image_path = os.path.join(current_dir, "data", "face.jpg")

# img = Image.open(face_image_path).convert("RGB")
img = cv2.imread(face_image_path)
cv2.imshow(img)

yolo = YOLO("yolov8s.pt")
