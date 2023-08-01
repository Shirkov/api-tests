from pydantic import BaseModel


class CartRsp(BaseModel):
    id: str
    quantity: int
