import cv2
import numpy as np
import streamlit as st
from PIL import Image

st.title("RGB до монохрому")

left, right = st.columns(2)

with left:
    uploaded = st.file_uploader("Оберіть зображення", type=["jpg", "jped", "png"])
    if uploaded:
        image = Image.open(uploaded).convert("RGB")
        st.image(image, caption="Початкове зображення у RGB", width="stretch")

if uploaded:
    img_array = np.array(image)
    gray = cv2.cvtColor(img_array, cv2.COLOR_RGB2GRAY)

    with right:
        st.image(gray, caption="Монохром", width="stretch", channels="gray")
else:
    with right:
        st.info("Завантажте зображення аби побачити його монохромну версію.і")
