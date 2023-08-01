from pydantic import BaseModel


class PickupsRsp(BaseModel):
    id: str
    originalId: str
    name: str
    type: str
    city: str
    cityId: str
    subwayStation: str
    address: str
    workingHours: str
    coordinates: dict

