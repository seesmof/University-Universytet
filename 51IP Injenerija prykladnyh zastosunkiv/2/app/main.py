from PIL import Image
import streamlit as st

st.set_page_config(layout="wide", page_title="Покращувач зображень", page_icon="🌱")

uploaded_file = st.file_uploader(
    "Оберіть зображення для покращення",
    type=["jpg", "png", "jpeg"],
)
left, right = st.columns(2)

with left:
    if not uploaded_file:
        st.write("Чекаю на зображення...")
    else:
        image = Image.open(uploaded_file)
        st.image(image, caption=uploaded_file.name)
        st.button(
            "Покращити",
            icon="🌱",
            help="Застосувати покращення до завантаженого зображення",
            use_container_width=True,
        )
