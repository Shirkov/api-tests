from pydantic import BaseModel
from datetime import datetime


class AuthSysLoginRsp(BaseModel):
    username: str
    email: str
    full_name: str
    created: datetime
    settings: dict
    permissions: list


class AuthLoginRsp(BaseModel):
    username: str
    email: str
    full_name: str
    created: datetime
    settings: dict
    permissions: list
