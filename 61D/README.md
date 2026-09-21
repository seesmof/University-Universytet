# Small farm manager

Streamlit + SQLite (SQLAlchemy ORM) app for crops, livestock and tasks.

Models (`farm_db.py`): `Crop`, `Animal` (table `livestock`), `Task`.

## Run (uv)

```bash
uv sync
uv run streamlit run streamlit_app.py
```

Add dependencies with `uv add <package>`.

Data is stored in `farm.db` (auto-created with sample data).
