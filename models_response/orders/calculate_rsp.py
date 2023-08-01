from typing import List

from pydantic import BaseModel


class Item(BaseModel):
    id: str
    quantity: int
    price: int
    price_old: int
    total: int
    offers: list


class CalculateRsp(BaseModel):
    total: int
    discount: int
    price: int
    price_old: int
    items: List[Item]
