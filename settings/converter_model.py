from pydantic import BaseModel


class Cms(BaseModel):
    cms_url: str
    cms_login: str
    cms_password: str
    cms_sys_login: str
    cms_sys_password: str


class Search(BaseModel):
    search_url: str
    engine: str


class Telegram(BaseModel):
    bot_url: str
    token: str
    chat_id: str


class Converter(BaseModel):
    cms: Cms
    search: Search
    telegram: Telegram
