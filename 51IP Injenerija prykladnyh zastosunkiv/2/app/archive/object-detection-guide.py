# okay so i copied all the code from the guide but the dependecies dont work together well. so first i added a tensorflow of a specific verison (saw it on a video from tiktok) and it worked but then it stopped, or no it didnt work ever i think. okay so it never worked, but the code is copied and i dont really get it.

from matplotlib import pyplot as plt
import numpy as np
import cv2
import os

current_dir = os.path.dirname(os.path.abspath(__file__))


def main():
    face_file_path = os.path.join(
        current_dir, "data", "haarcascade_frontalface_default.xml"
    )
    eyes_file_path = os.path.join(current_dir, "data", "haarcascade_eye.xml")

    face_cascade = cv2.CascadeClassifier(face_file_path)
    eye_cascade = cv2.CascadeClassifier(eyes_file_path)

    face_photo_file_name = "face.jpg"
    face_photo_path = os.path.join(current_dir, "data", face_photo_file_name)
    image = cv2.imread(face_photo_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for x, y, w, h in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
        roi_gray = gray[y : y + h, x : x + w]
        roi_color = image[y : y + h, x : x + w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for ex, ey, ew, eh in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
    cv2.imshow("img", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
