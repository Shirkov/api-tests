from pydantic import BaseModel


class Address(BaseModel):
    city: str
    region: str
    area: str
    zip_code: str
    street: str
    building: str
    suite: str
    entrance: str
    floor: str
    enter_code: str
    comments: str
    frontend_metadata: str
