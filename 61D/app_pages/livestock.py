from datetime import date

import pandas as pd
import streamlit as st

import farm_db

ANIMAL_TYPES = ["Корова", "Вівця", "Коза", "Свиня", "Курка", "Кінь", "Інше"]
HEALTH_STATUSES = ["Здорова", "Хвора", "Потребує огляду", "На лікуванні"]

st.title("Тварини")
st.caption("Облік тварин, порід і здоров’я.")

with st.expander("Додати тварину", icon=":material/add:"):
    with st.form("add_animal", border=False):
        c1, c2 = st.columns(2)
        with c1:
            animal_type = st.selectbox("Вид", ANIMAL_TYPES)
            tag_id = st.text_input("Номер бирки")
            breed = st.text_input("Порода", value="")
        with c2:
            birth_date = st.date_input("Дата народження", value=date.today())
            health = st.selectbox("Стан здоров’я", HEALTH_STATUSES)
            notes = st.text_area("Нотатки", value="")
        if st.form_submit_button("Зберегти тварину", type="primary", icon=":material/save:"):
            if not tag_id.strip() and animal_type != "Курка":
                st.error("Номер бирки обов’язковий (крім груп курей).")
            else:
                farm_db.add_animal(animal_type, tag_id.strip(), breed, birth_date, health, notes)
                st.success("Збережено.")
                st.rerun()

animals = farm_db.list_livestock()
if not animals:
    st.info("Поки немає тварин.")
    st.stop()

df = pd.DataFrame(animals)
df.columns = ["ID", "Вид", "Номер бирки", "Порода", "Дата народження", "Стан здоров’я", "Нотатки"]
st.dataframe(df, hide_index=True)

labels = {f"{a['id']} — {a['animal_type']} {a['tag_id']}": a["id"] for a in animals}
selected_label = st.selectbox("Виберіть тварину для редагування або видалення", list(labels.keys()), key="animal_select")
selected = next(a for a in animals if a["id"] == labels[selected_label])

with st.form("edit_animal"):
    st.subheader(f"Редагувати #{selected['id']}")
    c1, c2 = st.columns(2)
    with c1:
        e_type = st.selectbox(
            "Вид",
            ANIMAL_TYPES,
            index=ANIMAL_TYPES.index(selected["animal_type"]) if selected["animal_type"] in ANIMAL_TYPES else 0,
        )
        e_tag = st.text_input("Номер бирки", value=selected.get("tag_id") or "")
        e_breed = st.text_input("Порода", value=selected.get("breed") or "")
    with c2:
        e_health = st.selectbox(
            "Стан здоров’я",
            HEALTH_STATUSES,
            index=HEALTH_STATUSES.index(selected.get("health_status") or "Здорова") if selected.get("health_status") in HEALTH_STATUSES else 0,
        )
        e_notes = st.text_area("Нотатки", value=selected.get("notes") or "")
    with st.container(horizontal=True):
        save = st.form_submit_button("Оновити", type="primary", icon=":material/save:")
        delete = st.form_submit_button("Видалити", icon=":material/delete:")
    if save:
        farm_db.update_animal(
            selected["id"], e_type, e_tag, e_breed,
            selected.get("birth_date"), e_health, e_notes,
        )
        st.success("Оновлено.")
        st.rerun()
    if delete:
        farm_db.delete_animal(selected["id"])
        st.success("Видалено.")
        st.rerun()
