from pydantic import BaseModel


class AddressesCreateRsp(BaseModel):
    id: str
    ext_id: str
    customer_id: str
    zip_code: str
    region: str
    area: str
    city: str
    city_id: str
    street: str
    building: str
    suite: str
    longitude: float
    latitude: float
    entrance: str
    floor: str
    enter_code: str
    comments: str
    ext_data: dict
