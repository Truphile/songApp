from pydantic import BaseModel, EmailStr


class userRegister(BaseModel):
    full_name: str
    email: EmailStr
    password: str

class userLogin(BaseModel):
    email: EmailStr
    password: str