from sqlalchemy.orm import Session
from typing import List
from .models import Batch
from .schemas import BatchCreate, BatchUpdate


class BatchRepository:

    def __init__(self, db: Session):
        self.db = db

    def get_by_batch(self, medicine_id: int, pharmacy_id: int, batch_number: str):
        return (
            self.db.query(Batch)
            .filter(
                Batch.medicine_id == medicine_id,
                Batch.pharmacy_id == pharmacy_id,
                Batch.batch_number == batch_number
            )
            .first()
        )

    def create(self, data: BatchCreate):
        batch = Batch(**data.model_dump())
        self.db.add(batch)
        self.db.commit()
        self.db.refresh(batch)
        return batch
    
    def get_all(self):
        return self.db.query(Batch).all()
    
    def get_by_id(self, batch_id: int):
        return self.db.get(Batch, batch_id)
    
    def get_by_medicine(self, medicine_id: int):
        return self.db.query(Batch).filter(Batch.medicine_id == medicine_id).all()
    
    def get_by_pharmacy(self, pharmacy_id: int):
        return self.db.query(Batch).filter(Batch.pharmacy_id == pharmacy_id).all()
    
    def save(self, batch: Batch):
        self.db.commit()
        self.db.refresh(batch)
        return batch
    
    def update(self, batch_id: int, data: BatchUpdate):
        batch = self.get_by_id(batch_id)
        if not batch:
            return None
        
        for key, value in data.model_dump().items():
            setattr(batch, key, value)

        self.db.commit()
        self.db.refresh(batch)
        return batch
    
    def delete(self, batch_id: int):
        batch = self.get_by_id(batch_id)
        if not batch:
            return None
        
        self.db.delete(batch)
        self.db.commit()
        return batch