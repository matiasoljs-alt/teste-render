from fastapi import FastAPI
from rotas import rotaadmin, rotasusuario, rotaslivros
from database import create_db_and_tables

app = FastAPI()

create_db_and_tables()

app.include_router(rotaslivros.livro_router)
app.include_router(rotaadmin.adm_router)
app.include_router(rotasusuario.router_usuer)


@app.get("/")
def home():
    return {"msg": "API funcionando"}