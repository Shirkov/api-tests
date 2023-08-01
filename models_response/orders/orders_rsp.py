from pydantic import BaseModel


class OrdersRsp(BaseModel):
    id: str
    status: str
    ext_status: str