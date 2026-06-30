from sqlmodel import SQLModel, create_engine, Session

DATABASE_URL = "sqlite:///bamquinho.db"

engine = create_engine(
    DATABASE_URL,
    echo = True,
    connect_args = {"check_same_thread": False}
    
)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session

from fastapi import Header, HTTPException

ADMIN_SECRET = "**1155**"


def verify_master_password(
    senha: str = Header(...)
):
    if senha != ADMIN_SECRET:
        raise HTTPException(
            status_code=401,
            detail="senha incorreta"
        )

    return True        