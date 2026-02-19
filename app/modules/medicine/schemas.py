from pydantic import BaseModel, ConfigDict
from typing import Optional


class MedicineBase(BaseModel):
    name: str
    description: Optional[str] = None
    category: Optional[str] = None
    is_active: Optional[bool] = True

    model_config = ConfigDict(from_attributes=True)


class MedicineCreate(MedicineBase):
    pass


class MedicineUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    category: Optional[str] = None
    is_active: Optional[bool] = None 

    model_config = ConfigDict(from_attributes=True)


class MedicineOut(MedicineBase):
    id: int

    model_config = ConfigDict(from_attributes=True)

    