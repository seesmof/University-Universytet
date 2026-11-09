import streamlit as st

st.set_page_config(layout="centered", page_title="Покращувач зображень", page_icon="🌱")

uploaded_image = st.file_uploader(
    "Оберіть зображення",
    help="Тут можна завантажити зображення для його покращення",
    type=["jpg", "png", "jpeg"],
)
left, right = st.columns(2)

if not uploaded_image:
    st.write("Чекаю на зображення...")
else:
    with left:
        st.image(uploaded_image, caption=uploaded_image.name, use_container_width=True)
        if st.button(
            "Покращити",
            icon="🌱",
            help="Застосувати покращення до завантаженого зображення",
            use_container_width=True,
        ):
            # enhanced_image = upscale_image(uploaded_image)
            enhanced_image = uploaded_image
            with right:
                st.image(
                    enhanced_image,
                    caption="Покращене зображення",
                    use_container_width=True,
                )
                st.download_button(
                    label="Завантажити",
                    icon="📼",
                    # data=buffer.tobytes(),
                    data="Jesus is LORD",
                    file_name="upscaled.png",
                    mime="image/png",
                    use_container_width=True,
                )
