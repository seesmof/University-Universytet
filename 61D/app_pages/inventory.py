import pandas as pd
import streamlit as st

import farm_db

CATEGORIES = ["Ручні інструменти", "Електроінструменти", "Техніка", "Запчастини", "Паливо", "Добрива", "Насіння", "Корми", "Інше"]
CONDITIONS = ["Справний", "Потребує ремонту", "Зламаний"]
UNITS = ["шт", "кг", "л", "м", "компл."]

st.title("Інвентар")
st.caption("Облік інструментів, техніки та запасів.")

with st.expander("Додати позицію", icon=":material/add:"):
    with st.form("add_item", border=False):
        c1, c2 = st.columns(2)
        with c1:
            name = st.text_input("Назва")
            category = st.selectbox("Категорія", CATEGORIES)
            quantity = st.number_input("Кількість", min_value=0.0, step=1.0)
            unit = st.selectbox("Одиниця", UNITS)
        with c2:
            condition = st.selectbox("Стан", CONDITIONS)
            location = st.text_input("Місце зберігання", value="")
            notes = st.text_area("Нотатки", value="")
        if st.form_submit_button("Зберегти", type="primary", icon=":material/save:"):
            if not name.strip():
                st.error("Назва обов’язкова.")
            else:
                farm_db.add_inventory_item(name.strip(), category, quantity, unit, condition, location, notes)
                st.success(f"Збережено {name}.")
                st.rerun()

items = farm_db.list_inventory()
if not items:
    st.info("Поки немає інвентарю. Додайте вище.")
    st.stop()

filter_cat = st.selectbox("Фільтр за категорією", ["Усі"] + CATEGORIES, index=0)
shown = items if filter_cat == "Усі" else [i for i in items if i["category"] == filter_cat]

needs_repair = sum(1 for i in items if i.get("condition") != "Справний")
with st.container(horizontal=True):
    st.metric("Позицій", str(len(items)), border=True)
    st.metric("Потребують ремонту", str(needs_repair), border=True)

if not shown:
    st.info("Немає позицій у цій категорії.")
    st.stop()

df = pd.DataFrame(shown)
df.columns = ["ID", "Назва", "Категорія", "Кількість", "Одиниця", "Стан", "Місце", "Нотатки"]
st.dataframe(df, hide_index=True)

labels = {f"{i['id']} — {i['name']} ({i['quantity']} {i['unit']})": i["id"] for i in shown}
selected_label = st.selectbox("Виберіть позицію для редагування або видалення", list(labels.keys()), key="inv_select")
selected = next(i for i in shown if i["id"] == labels[selected_label])

with st.form("edit_item"):
    st.subheader(f"Редагувати #{selected['id']}")
    c1, c2 = st.columns(2)
    with c1:
        e_name = st.text_input("Назва", value=selected["name"])
        e_cat = st.selectbox(
            "Категорія", CATEGORIES,
            index=CATEGORIES.index(selected.get("category")) if selected.get("category") in CATEGORIES else len(CATEGORIES) - 1,
        )
        e_qty = st.number_input("Кількість", min_value=0.0, step=1.0, value=float(selected.get("quantity") or 0))
        e_unit = st.selectbox(
            "Одиниця", UNITS,
            index=UNITS.index(selected.get("unit")) if selected.get("unit") in UNITS else 0,
        )
    with c2:
        e_cond = st.selectbox(
            "Стан", CONDITIONS,
            index=CONDITIONS.index(selected.get("condition")) if selected.get("condition") in CONDITIONS else 0,
        )
        e_loc = st.text_input("Місце зберігання", value=selected.get("location") or "")
        e_notes = st.text_area("Нотатки", value=selected.get("notes") or "")
    with st.container(horizontal=True):
        save = st.form_submit_button("Оновити", type="primary", icon=":material/save:")
        delete = st.form_submit_button("Видалити", icon=":material/delete:")
    if save:
        farm_db.update_inventory_item(selected["id"], e_name, e_cat, e_qty, e_unit, e_cond, e_loc, e_notes)
        st.success("Оновлено.")
        st.rerun()
    if delete:
        farm_db.delete_inventory_item(selected["id"])
        st.success("Видалено.")
        st.rerun()
