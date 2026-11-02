from enum import Enum
from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None


class Role(str, Enum):
    NURSE = "Nurse"
    HCA = "HCA"


class User(BaseModel):
    username: str
    email: str | None = None
    full_name : str | None = None
    disabled: bool | None = None
    role : Role


class UserInDB(User):
    hashed_password: str