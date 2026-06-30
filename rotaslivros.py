from models.livros import LivrosDB
from fastapi import HTTPException, APIRouter,  Depends
from database import get_session, verify_master_password
from sqlmodel import select, Session


livro_router = APIRouter(prefix="/livross")

@livro_router.get("/todos_-livros")
def all_books(session: Session = Depends(get_session)):

    verify = session.exec(
        select(
            LivrosDB
        )
    ).all()

    if not verify:
        raise HTTPException(
            404,
            "sem livros disponiveis"
        )

    return verify

@livro_router.post("/ler-livro/{livro_id}")
def ler(livro_id: int, session: Session = Depends(get_session)):
    
    livro = session.exec(
        select(
            LivrosDB
        ).where(
            LivrosDB.id == livro_id
        )
    ).first()

    if livro is None:
        raise HTTPException(
            404,
            "livro n encntrado"
        )

    return livro.info    