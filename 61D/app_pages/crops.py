from datetime import date

import pandas as pd
import streamlit as st

import farm_db

STATUSES = ["Зростає", "Зібрано", "Заплановано", "Втрачено"]

st.title("Посіви")
st.caption("Облік посадок, полів і врожаїв.")

with st.expander("Додати посів", icon=":material/add:"):
    with st.form("add_crop", border=False):
        c1, c2 = st.columns(2)
        with c1:
            name = st.text_input("Назва культури")
            variety = st.text_input("Сорт", value="")
            field = st.text_input("Поле", value="")
            area = st.number_input("Площа (га)", min_value=0.0, step=0.1)
        with c2:
            plant_date = st.date_input("Дата посіву", value=date.today())
            harvest_date = st.date_input("Дата збору", value=date.today())
            status = st.selectbox("Статус", STATUSES)
            notes = st.text_area("Нотатки", value="")
        if st.form_submit_button("Зберегти посів", type="primary", icon=":material/save:"):
            if not name.strip():
                st.error("Назва культури обов’язкова.")
            else:
                farm_db.add_crop(name.strip(), variety, field, area, plant_date, harvest_date, status, notes)
                st.success(f"Збережено {name}.")
                st.rerun()

crops = farm_db.list_crops()
if not crops:
    st.info("Поки немає посівів. Додайте вище.")
    st.stop()

df = pd.DataFrame(crops)
df.columns = ["ID", "Назва", "Сорт", "Поле", "Площа (га)", "Дата посіву", "Дата збору", "Статус", "Нотатки"]
st.dataframe(df, hide_index=True)

labels = {f"{c['id']} — {c['name']} ({c['field']})": c["id"] for c in crops}
selected_label = st.selectbox("Виберіть посів для редагування або видалення", list(labels.keys()), key="crop_select")
selected = next(c for c in crops if c["id"] == labels[selected_label])

with st.form("edit_crop"):
    st.subheader(f"Редагувати #{selected['id']}")
    c1, c2 = st.columns(2)
    with c1:
        e_name = st.text_input("Назва культури", value=selected["name"])
        e_variety = st.text_input("Сорт", value=selected.get("variety") or "")
        e_field = st.text_input("Поле", value=selected.get("field") or "")
        e_area = st.number_input("Площа (га)", min_value=0.0, step=0.1, value=float(selected.get("area_ha") or 0))
    with c2:
        e_status = st.selectbox(
            "Статус",
            STATUSES,
            index=STATUSES.index(selected.get("status") or "Зростає") if selected.get("status") in STATUSES else 0,
        )
        e_notes = st.text_area("Нотатки", value=selected.get("notes") or "")
    with st.container(horizontal=True):
        save = st.form_submit_button("Оновити", type="primary", icon=":material/save:")
        delete = st.form_submit_button("Видалити", icon=":material/delete:")

    if save:
        farm_db.update_crop(
            selected["id"], e_name, e_variety, e_field, e_area,
            selected.get("plant_date"), selected.get("harvest_date"), e_status, e_notes,
        )
        st.success("Оновлено.")
        st.rerun()
    if delete:
        farm_db.delete_crop(selected["id"])
        st.success("Видалено.")
        st.rerun()
