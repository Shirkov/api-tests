from pydantic import BaseModel


class AddressesSuggestRsp(BaseModel):
    city_fias_id: str
    fias_id: str
    address: str
