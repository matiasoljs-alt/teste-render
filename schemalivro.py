from pydantic import BaseModel

class CreateLivro(BaseModel):
    name: str
    discription: str
    autor: str
    info: str
    publicate: str