from pydantic import BaseModel


class Store(BaseModel):
    warehouseId: str
    name: str
    city: str
    cityId: str
    address: str
    workingHours: dict


class StoresRsp(BaseModel):
    pickupStore: Store
