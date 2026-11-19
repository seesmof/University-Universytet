import streamlit as st
import whisper

st.set_page_config(page_title="Класифікація звуку", layout="centered")
st.title("Класифікація звуку")

model = whisper.load_model("base")

uploaded = st.file_uploader(
    "Завантажити аудіо", type=["wav", "mp3", "ogg", "flac", "m4a"]
)

if uploaded is not None:
    audio = uploaded.read()
    st.audio(audio)
    tmp = "tmp_audio.wav"
    with open(tmp, "wb") as f:
        f.write(audio)
    with st.spinner("Розпізнаю..."):
        result = model.transcribe(tmp)
    st.subheader("Результат")
    text = result["text"].strip()
    if not text:
        st.warning("У наданому файлі мовлення не виявлено.")
    else:
        st.write(text)
        st.write("Мова:", result["language"])
