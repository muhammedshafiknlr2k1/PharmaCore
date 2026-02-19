from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import date


class BatchBase(BaseModel):
    medicine_id: int
    pharmacy_id: int
    batch_number: str
    quantity: int
    expiry_date: date

    model_config = ConfigDict(from_attributes=True)


class BatchCreate(BatchBase):
    pass


class BatchUpdate(BaseModel):
    quantity: Optional[int]
    expiry_date: Optional[date]

    model_config = ConfigDict(from_attributes=True)


class BatchOut(BatchBase):
    id: int

    model_config = ConfigDict(from_attributes=True)