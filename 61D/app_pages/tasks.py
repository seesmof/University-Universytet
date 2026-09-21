from datetime import date

import streamlit as st

import farm_db

CATEGORIES = ["Загальне", "Посіви", "Тварини", "Запаси", "Обслуговування"]
PRIORITIES = ["Низький", "Середній", "Високий"]

st.title("Завдання")
st.caption("Щоденні справи ферми.")

with st.expander("Додати завдання", icon=":material/add:"):
    with st.form("add_task", border=False):
        title = st.text_input("Назва")
        c1, c2 = st.columns(2)
        with c1:
            category = st.selectbox("Категорія", CATEGORIES)
            due = st.date_input("Термін", value=date.today())
        with c2:
            priority = st.segmented_control("Пріоритет", PRIORITIES, default="Середній")
            notes = st.text_input("Нотатки", value="")
        if st.form_submit_button("Додати завдання", type="primary", icon=":material/add_task:"):
            if not title.strip():
                st.error("Назва обов’язкова.")
            else:
                farm_db.add_task(title.strip(), category, due, priority, notes)
                st.success("Завдання додано.")
                st.rerun()

tasks = farm_db.list_tasks()
if not tasks:
    st.info("Поки немає завдань.")
    st.stop()

filter_open = st.checkbox("Показати лише відкриті завдання", value=True)
shown = [t for t in tasks if not t["done"]] if filter_open else tasks

if not shown:
    st.success("Немає справ. Усі завдання виконано.")

for t in shown:
    with st.container(border=True):
        c1, c2, c3 = st.columns([0.08, 0.72, 0.2])
        with c1:
            checked = st.checkbox(
                "Виконано",
                value=bool(t["done"]),
                key=f"task_{t['id']}",
                label_visibility="collapsed",
            )
            if checked != bool(t["done"]):
                farm_db.toggle_task(t["id"], checked)
                st.rerun()
        with c2:
            title = f"~~{t['title']}~~" if t["done"] else t["title"]
            st.markdown(f"**{title}**")
            st.caption(f"{t['category']} · термін {t['due_date']} · {t['priority']}")
        with c3:
            if st.button("Видалити", key=f"del_{t['id']}", icon=":material/delete:"):
                farm_db.delete_task(t["id"])
                st.rerun()
