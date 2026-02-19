from pydantic import BaseModel, EmailStr, ConfigDict
from typing import Optional


class PharmacyBase(BaseModel):
    name: str
    email: EmailStr
    phone: str
    address: Optional[str]


class PharmacyCreate(PharmacyBase):
    pass 


class PharmacyUpdate(BaseModel):
    name: Optional[str]
    email: Optional[EmailStr]
    phone: Optional[str]
    address: Optional[str]
    is_active: Optional[bool]


class PharmacyOut(PharmacyBase):
    id: int
    is_active: bool

    model_config = ConfigDict(from_attributes=True)

