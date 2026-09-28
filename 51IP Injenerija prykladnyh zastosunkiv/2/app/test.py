import os
import cv2

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

current_dir = os.path.dirname(os.path.abspath(__file__))
image_file_name = "face.jpg"
image_file_path = os.path.join(current_dir, "data", image_file_name)
img = cv2.imread(image_file_path)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(
    gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30)
)

for x, y, w, h in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
cv2.imshow("Faces", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
