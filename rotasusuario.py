from fastapi import APIRouter,  HTTPException, Depends
from sqlmodel import Session, select
from database import get_session
from schemas.sechemausuario import Createuser, Loginuser
from models.usuarios import Usuariodb

router_usuer = APIRouter(prefix="/Users")

@router_usuer.post("/create_user")
def createi_user(user: Createuser, session: Session = Depends(get_session)):
    new_user = Usuariodb(
        name=user.name,
        email=user.email,
        senha=user.senha
    )

    verify_user = session.exec(
        select(Usuariodb).where(
            Usuariodb.email == user.email
        )
    ).first()

    if verify_user:
        raise HTTPException(
            400,
            "esse email ja estar sendo usado"
        )

    session.add(new_user)
    session.commit()
    session.refresh(new_user)    

    return {"msg": f"usuario {user.name} cadastrado com sucesso"}



@router_usuer.post("/login_pag")
def logins_users(user: Loginuser, session: Session = Depends(get_session)):

    verify_login = session.exec(
        select(
            Usuariodb
        ).where(
            Usuariodb.email == user.email,
            Usuariodb.senha == user.senha
        )
    ).first()

    if verify_login is None:
        raise HTTPException(
            404,
            "usuario ou senha estão incorreta"
        )

    return {"msg": f"bem vindo de volta {user.name}"} 

    