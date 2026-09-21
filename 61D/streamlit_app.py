import streamlit as st

import farm_db

st.set_page_config(
    page_title="Менеджер ферми", page_icon=":material/agriculture:", layout="wide"
)

farm_db.init_db()

pages = [
    st.Page("app_pages/dashboard.py", title="Панель", icon=":material/dashboard:"),
    st.Page("app_pages/crops.py", title="Посіви", icon=":material/grass:"),
    st.Page("app_pages/livestock.py", title="Тварини", icon=":material/pets:"),
    st.Page("app_pages/tasks.py", title="Завдання", icon=":material/checklist:"),
    st.Page("app_pages/inventory.py", title="Інвентар", icon=":material/handyman:"),
    st.Page("app_pages/logs.py", title="Журнал", icon=":material/history:"),
]

nav = st.navigation(pages)
nav.run()
