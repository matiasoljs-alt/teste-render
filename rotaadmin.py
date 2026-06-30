from fastapi import APIRouter,  HTTPException, Depends
from sqlmodel import select, Session
from database import get_session, verify_master_password
from schemas.schemaadmin import Loginadmin, CreateAdmin
from models.admmodels import AdmDB
from models.livros import LivrosDB
from schemas.schemalivro import CreateLivro
from models.usuarios import Usuariodb

adm_router = APIRouter(prefix="/admin")

@adm_router.post("/create--admn")
def create_admin(adm: CreateAdmin, session: Session = Depends(get_session), autorizado: bool = Depends(verify_master_password)):

    new_adm = AdmDB(
        name=adm.name,
        email=adm.email,
        senha=adm.senha
    )

    verify_adm = session.exec(
        select(
            AdmDB
        ).where(
            AdmDB.email == adm.email
        )
    ).first()

    if verify_adm:
        raise HTTPException (
            400,
            "impossivel de criar com essas credenciais"
        )

    session.add(new_adm)
    session.commit()
    session.refresh(new_adm)

    return {"msg": f"admin criado bem vindo a equipe {new_adm.name}"}


@adm_router.delete("/deletar_adm/{adm_id}")
def deletar_adm(adm_id: int, session: Session = Depends(get_session), autorizado: bool = Depends(verify_master_password)):

    adm = session.get(AdmDB, adm_id)

    if not adm:
        raise HTTPException(
            404,
            "admin nao encontrado"
        )

    session.delete(adm) 
    session.commit()

    return {"msg" "admin deletado"}   




@adm_router.post("/login-_adm")
def login_admin(adm: Loginadmin, session: Session = Depends(get_session)):
    
    verify_adm = session.exec(
        select(
            AdmDB
        ).where(
            AdmDB.email == adm.email,
            AdmDB.senha == adm.senha
        )
    )

    if verify_adm is None:
        raise HTTPException (
            404,
            "adm nao encontrado "
        )


    return {"msg": f"bem vindo(a) adm "}


@adm_router.get("/todos-adm")    
def all_admin(session: Session = Depends(get_session)):

    all_adms = session.exec(
        select(
            AdmDB
        )
    ).all()

    if not all_adms:
        raise HTTPException(
            404,
            "nenhum adm"
        )

    return all_adms    

@adm_router.post("/create_livro")
def criar_livro(livro: CreateLivro, session: Session = Depends(get_session)):
    
    new_book = LivrosDB(
        name=livro.name,
        discription=livro.discription,
        autor=livro.autor,
        info=livro.info,
        publicate=livro.publicate
    )

    exist_book = session.exec(
        select(LivrosDB).where(
            LivrosDB.name == livro.name,
            LivrosDB.info == livro.info
        )
    ).first()

    if exist_book:
        raise HTTPException(
            400,
            "livro ja existe"
        )

    session.add(new_book)
    session.commit()
    session.refresh(new_book)

    return new_book


@adm_router.get("/all_users")
def all_users(session: Session = Depends(get_session)):

    users = session.exec(
        select(
            Usuariodb
        )
    ).all()

    if not users:
        raise HTTPException(
            404,
            "nenhum usuario no banco"
        )

    return users


@adm_router.delete("/delete/{user_id}")
def deletar_user(user_id: int, session: Session = Depends(get_session), autorizado: bool = Depends(verify_master_password)):

    user = session.get(Usuariodb, user_id)

    if not user:
        raise HTTPException(
            404,
            "usuario n encontrado"
        )

    session.delete(user)
    session.commit()

    return {"msg": "usuario deletado vapo"}

