from pydantic import BaseModel, EmailStr

class Createuser(BaseModel):
    name: str
    email:EmailStr
    senha: str

class Loginuser (BaseModel):
    email: EmailStr
    senha: str