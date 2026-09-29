import os
import cv2
from matplotlib import pyplot as plt
from ultralytics import YOLO

model = YOLO("yolov8n.pt")

# Load an image
current_dir = os.path.dirname(os.path.abspath(__file__))
image_file_name = "face.jpg"
image_file_path = os.path.join(current_dir, "data", image_file_name)
img = cv2.imread(image_file_path)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Show the loaded image
plt.imshow(img)
plt.title("Original Image")
plt.show()


# Code taken from https://github.com/pranayrishi/YOLO-ObjectDetection/blob/main/main.py
def detect_objects(frame):
    results = model(frame)
    detected_objects = list()

    for r in results:
        for box in r.boxes:
            class_id = int(box.cls[0])
            confidence = box.conf[0].item()

            if confidence > 0.5:
                label = model.names[class_id]
                detected_objects.append(label)

                # Draw a box
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(
                    frame,
                    label,
                    (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.5,
                    (0, 255, 0),
                    2,
                )
                cv2.putText(
                    frame,
                    str(confidence),
                    (x2 - 30, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.5,
                    (0, 255, 0),
                    2,
                )
    return frame, detected_objects


# Show the detected objects
frame, detected_objects = detect_objects(img)
plt.imshow(frame)
plt.title("Detected Objects")
plt.show()
