# code taken from https://github.com/pranayrishi/YOLO-ObjectDetection/blob/main/main.py

import cv2
from ultralytics import YOLO

model = YOLO("yolov8s.pt")


def detect_objects(frame):
    results = model(frame)
    detected_objects = []

    for result in results:
        for box in result.boxes:
            class_id = int(box.cls[0])
            confidence = box.conf[0].item()

            if confidence > 0.5:
                label = model.names[class_id]
                detected_objects.append(label)

                x1, y1, x2, y2 = map(int, box.xyxy[0])
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(
                    frame,
                    label,
                    (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.6,
                    (0, 255, 0),
                    2,
                )
    return frame, detected_objects


cap = cv2.VideoCapture(0)
while 1:
    ret, frame = cap.read()
    if not ret:
        break

    frame, detected_objects = detect_objects(frame)
    cv2.imshow("Vision", frame)
    if detected_objects:
        print(f"Detected objects: {detected_objects}")
    key = cv2.waitKey(1)

cap.release()
cv2.destroyAllWindows()
