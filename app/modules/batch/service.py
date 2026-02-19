from sqlalchemy.orm import Session
from typing import List
from .repository import BatchRepository
from .schemas import BatchCreate, BatchUpdate


class BatchService:

    def __init__(self, db: Session):
        self.repo = BatchRepository(db)

    def create_batch(self, data: BatchCreate):
        existing_batch = self.repo.get_by_batch(
            data.medicine_id,
            data.pharmacy_id,
            data.batch_number
        )

        # 🔥 Business logic: merge quantity if same batch
        if existing_batch:
            existing_batch.quantity += data.quantity
            return self.repo.save(existing_batch)

        return self.repo.create(data)
    
    def list_batches(self):
        return self.repo.get_all()
    
    def get_batch(self, batch_id: int):
        batch = self.repo.get_by_id(batch_id)
        if not batch:
            raise ValueError('Batch Not Found')
        return batch
    
    def list_batches_by_medicine(self, medicine_id: int):
        return self.repo.get_by_medicine(medicine_id)
    
    def list_batches_by_pharmacy(self, pharmacy_id: int):
        return self.repo.get_by_pharmacy(pharmacy_id)
    
    def update_batch(self, batch_id: int, data: BatchUpdate):
        batch = self.repo.update(batch_id, data)
        if not batch:
            raise ValueError('Batch Not Found')
        return batch
    
    def delete_batch(self, batch_id: int):
        batch = self.repo.delete(batch_id)
        if not batch:
            raise ValueError('Batch Not Found')
        return batch
    