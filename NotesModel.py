from pydantic import BaseModel, EmailStr

class User(BaseModel):
    email: EmailStr
    note: str
    date: str




