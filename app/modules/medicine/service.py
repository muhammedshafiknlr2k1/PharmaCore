from sqlalchemy.orm import Session
from .repository import MedicineRepository
from .schemas import MedicineCreate, MedicineUpdate
from typing import List


class MedicineService:

    def __init__(self, db: Session):
        self.repo = MedicineRepository(db)


    def create_medicine(self, data: MedicineCreate):
        return self.repo.create(data)
    

    def list_medicines(self):
        return self.repo.get_all()


    def get_medicine(self, medicine_id: int):
        medicine = self.repo.get_by_id(medicine_id)
        if not medicine:
            raise ValueError('Medicine Not Found')
        return medicine    
    

    def update_medicine(self, medicine_id: int, data: MedicineUpdate):
        medicine = self.repo.update(medicine_id, data)
        if not medicine:
            raise ValueError('Medicine Not Found')
        return medicine
    

    def delete_medicine(self, medicine_id: int):
        medicine = self.repo.delete(medicine_id)
        if not medicine:
            raise ValueError('Medicine Not Found')
        return medicine
    