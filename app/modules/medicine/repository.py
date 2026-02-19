from sqlalchemy.orm import Session
from .models import Medicine
from .schemas import MedicineCreate, MedicineUpdate


class MedicineRepository:

    def __init__(self, db: Session):
        self.db = db

    def create(self, medicine_data: MedicineCreate):
        medicine = Medicine(**medicine_data.model_dump())
        self.db.add(medicine)
        self.db.commit()
        self.db.refresh(medicine)
        return medicine
    
    def get_all(self):
        return self.db.query(Medicine).all()
    
    def get_by_id(self, medicine_id: int):
        return self.db.get(Medicine, medicine_id)
    
    def update(self, medicine_id: int, medicine_data: MedicineUpdate):
        medicine = self.get_by_id(medicine_id)
        if not medicine:
            return None
        for key, value in medicine_data.model_dump().items():
            setattr(medicine, key, value)
        self.db.commit()
        self.db.refresh(medicine)
        return medicine
    
    def delete(self, medicine_id: int):
        medicine = self.get_by_id(medicine_id)
        if not medicine:
            return None
        self.db.delete(medicine)
        self.db.commit()
        return medicine