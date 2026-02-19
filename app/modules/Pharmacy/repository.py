from sqlalchemy.orm import Session
from app.modules.pharmacy.models import Pharmacy
from app.modules.pharmacy.schemas import PharmacyCreate, PharmacyUpdate


class PharmacyRepository:

    def __init__(self, db: Session):
        self.db = db


    def create(self, pharmacy_data: PharmacyCreate):
        pharmacy = Pharmacy(**pharmacy_data.model_dump())
        self.db.add(pharmacy)
        self.db.commit()
        self.db.refresh(pharmacy)
        return pharmacy
    

    def get_all(self):
        return self.db.query(Pharmacy).all()
    

    def get_by_id(self, pharmacy_id: int):
        return self.db.query(Pharmacy).filter(Pharmacy.id == pharmacy_id).first()
    

    def update(self, pharmacy_id: int, pharmacy_data: PharmacyUpdate):
        pharmacy = self.get_by_id(pharmacy_id)
        if not pharmacy:
            return None
        
        for key, value in pharmacy_data.model_dump(exclude_unset=True).items():
            setattr(pharmacy, key, value)
        self.db.commit()
        self.db.refresh(pharmacy)
        return pharmacy
        

    def delete(self, pharmacy_id: int):
        pharmacy = self.get_by_id(pharmacy_id)
        if not pharmacy:
            return None
        self.db.delete(pharmacy)
        self.db.commit()
        return pharmacy

