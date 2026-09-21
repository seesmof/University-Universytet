import pandas as pd
import streamlit as st

import farm_db

st.title("Панель")
st.caption("Огляд посівів, тварин, завдань та інвентарю.")

crops = farm_db.list_crops()
animals = farm_db.list_livestock()
tasks = farm_db.list_tasks()
inventory = farm_db.list_inventory()
recent_logs = farm_db.list_logs(limit=5)

total_area = sum((c.get("area_ha") or 0) for c in crops)
growing = sum(1 for c in crops if c.get("status") == "Зростає")
open_tasks = sum(1 for t in tasks if not t.get("done"))
needs_check = sum(1 for a in animals if a.get("health_status") != "Здорова")
needs_repair = sum(1 for i in inventory if i.get("condition") != "Справний")

with st.container(horizontal=True):
    st.metric("Загальна площа посівів (га)", f"{total_area:.1f}", border=True)
    st.metric("Ділянки посівів", str(len(crops)), f"{growing} ростуть", border=True)
    st.metric("Тварини", str(len(animals)), f"{needs_check} потребують уваги" if needs_check else "Усі здорові", border=True)
    st.metric("Відкриті завдання", str(open_tasks), border=True)
    st.metric("Інвентар", str(len(inventory)), f"{needs_repair} ремонт" if needs_repair else "Все справне", border=True)

col1, col2 = st.columns(2)

with col1:
    with st.container(border=True):
        st.subheader("Площа за культурами")
        if crops:
            df = pd.DataFrame(crops)
            chart_df = df.groupby("name", as_index=False)["area_ha"].sum()
            chart_df.columns = ["Культура", "Площа"]
            st.bar_chart(chart_df, x="Культура", y="Площа", x_label="Культура", y_label="Гектари")
        else:
            st.info("Поки немає посівів.")

with col2:
    with st.container(border=True):
        st.subheader("Тварини за видами")
        if animals:
            df = pd.DataFrame(animals)
            counts = df["animal_type"].value_counts().reset_index()
            counts.columns = ["Вид", "Кількість"]
            st.bar_chart(counts, x="Вид", y="Кількість", x_label="Вид", y_label="Кількість")
        else:
            st.info("Поки немає тварин.")

with st.container(border=True):
    st.subheader("Майбутні врожаї")
    if crops:
        df = pd.DataFrame(crops)
        df = df[["name", "variety", "field", "harvest_date", "status"]].sort_values("harvest_date")
        df.columns = ["Культура", "Сорт", "Поле", "Дата збору", "Статус"]
        st.dataframe(df, hide_index=True)
    else:
        st.info("Поки немає посівів.")

with st.container(border=True):
    st.subheader("Відкриті завдання")
    open_df = [t for t in tasks if not t.get("done")]
    if open_df:
        df = pd.DataFrame(open_df)[["title", "category", "due_date", "priority"]]
        df.columns = ["Назва", "Категорія", "Термін", "Пріоритет"]
        st.dataframe(df, hide_index=True)
    else:
        st.success("Усі завдання виконано.")

with st.container(border=True):
    st.subheader("Останні оновлення")
    if recent_logs:
        df = pd.DataFrame(recent_logs)[["created_at", "entity", "action", "details"]]
        df.columns = ["Дата і час", "Сутність", "Дія", "Деталі"]
        st.dataframe(df, hide_index=True)
    else:
        st.info("Поки немає записів у журналі.")
