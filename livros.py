from sqlmodel import Field, SQLModel
from typing import Optional

class LivrosDB(SQLModel, table = True):
    id: Optional[int] = Field(
        default = None,
        primary_key=True
    )

    name: str
    discription: str
    autor: str
    info: str
    publicate: str
