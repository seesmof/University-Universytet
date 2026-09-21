import pandas as pd
import streamlit as st

import farm_db

ENTITIES = ["Усі", "Посіви", "Тварини", "Завдання", "Інвентар"]
ACTIONS = ["Усі", "Створено", "Оновлено", "Видалено", "Перемкнуто"]

st.title("Журнал оновлень")
st.caption("Хто що змінював: створення, редагування та видалення.")

c1, c2, c3 = st.columns(3)
with c1:
    f_entity = st.selectbox("Сутність", ENTITIES, index=0)
with c2:
    f_action = st.selectbox("Дія", ACTIONS, index=0)
with c3:
    limit = st.selectbox("Показати записів", [50, 100, 200, 500], index=2)

logs = farm_db.list_logs(
    limit=limit,
    entity=None if f_entity == "Усі" else f_entity,
    action=None if f_action == "Усі" else f_action,
)

if not logs:
    st.info("Журнал порожній.")
    st.stop()

df = pd.DataFrame(logs)
df.columns = ["ID", "Дата і час", "Сутність", "Дія", "ID запису", "Деталі"]
st.dataframe(df, hide_index=True, use_container_width=True)

with st.expander("Небезпечна зона", icon=":material/warning:"):
    st.caption("Видалення журналу не можна скасувати.")
    if st.button("Очистити журнал", icon=":material/delete:", type="primary"):
        farm_db.clear_logs()
        st.success("Журнал очищено.")
        st.rerun()
