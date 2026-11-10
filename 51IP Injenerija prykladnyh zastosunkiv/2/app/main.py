import io
from PIL import Image, ImageEnhance
import streamlit as st

st.set_page_config(layout="centered", page_title="Покращувач зображень", page_icon="🌱")

DEFAULT_VALUE = 1.0

if "new_image" not in st.session_state:
    st.session_state.new_image = None

if "brightness" not in st.session_state:
    st.session_state.brightness = DEFAULT_VALUE

if "contrast" not in st.session_state:
    st.session_state.contrast = DEFAULT_VALUE


def reset_params():
    st.session_state.brightness = DEFAULT_VALUE
    st.session_state.contrast = DEFAULT_VALUE


st.sidebar.header("Параметри покращення")
brightness = st.sidebar.slider("Яскравість", 0.5, 2.0, key="brightness", step=0.1)
contrast = st.sidebar.slider("Контрастність", 0.5, 2.0, key="contrast", step=0.1)
st.sidebar.button(
    "Скинути",
    on_click=reset_params,
    use_container_width=True,
    icon="🔄",
)

uploaded_image = st.file_uploader(
    "Оберіть зображення",
    help="Тут можна завантажити зображення для його покращення",
    type=["jpg", "png", "jpeg"],
)

left, right = st.columns(2)

if not uploaded_image:
    st.write("Чекаю на зображення...")
    st.session_state.new_image = None
else:
    with left:
        st.image(uploaded_image, caption=uploaded_image.name, use_container_width=True)
        if st.button(
            "Покращити",
            icon="🌱",
            help="Застосувати покращення до завантаженого зображення",
            use_container_width=True,
        ):
            img = Image.open(uploaded_image)

            enhancer = ImageEnhance.Brightness(img)
            img = enhancer.enhance(brightness)

            enhancer = ImageEnhance.Contrast(img)
            img = enhancer.enhance(contrast)

            st.session_state.new_image = img

    if st.session_state.new_image is not None:
        with right:
            st.image(
                st.session_state.new_image,
                caption="Покращене зображення",
                use_container_width=True,
            )

            buf = io.BytesIO()
            st.session_state.new_image.save(buf, format="PNG")

            st.download_button(
                label="Завантажити",
                icon="📼",
                data=buf.getvalue(),
                file_name="improved.png",
                mime="image/png",
                use_container_width=True,
            )
