from sqlmodel import SQLModel, create_engine, Session

DATABASE_URL = "sqlite:///./chat.db"
engine = create_engine(DATABASE_URL, echo=False)


def init_db() -> None:
    SQLModel.metadata.create_all(engine, checkfirst=True)


def get_session():
    with Session(engine) as session:
        yield session
