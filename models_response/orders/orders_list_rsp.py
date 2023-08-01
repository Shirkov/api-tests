from typing import List

from pydantic import BaseModel


class Order(BaseModel):
    id: str
    status: str
    ext_status: str


class Data(BaseModel):
    order: Order


class OrdersListRsp(BaseModel):
    data: List[Data]
