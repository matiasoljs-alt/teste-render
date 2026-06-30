from pydantic import BaseModel, EmailStr

class CreateAdmin(BaseModel):
    name: str
    email: EmailStr
    senha: str


class Loginadmin(BaseModel):
    email: EmailStr
    senha: str