from sqlmodel import SQLModel, Field
from typing import Optional

class Usuariodb(SQLModel, table = True):
    id: Optional[int] = Field(
        default = None,
        primary_key = True
    )
    name: str
    email: str
    senha: str
    is_adm:bool = False