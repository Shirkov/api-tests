from pydantic import BaseModel


class CourierRsp(BaseModel):
    id: str
    date: str
    date: str
    carrierId: str
    tariffId: str
    type: str

