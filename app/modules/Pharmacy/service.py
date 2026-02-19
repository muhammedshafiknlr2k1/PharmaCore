from sqlalchemy.orm import Session
from .schemas import PharmacyCreate, PharmacyUpdate
from .repository import PharmacyRepository


class PharmacyService:

    def __init__(self, db: Session):
        self.repo = PharmacyRepository(db)

    def create_pharmacy(self, data: PharmacyCreate):
        return self.repo.create(data)

    def list_pharmacies(self):
        return self.repo.get_all()

    def get_pharmacy(self, pharmacy_id: int):
        return self.repo.get_by_id(pharmacy_id)

    def update_pharmacy(self, pharmacy_id: int, data: PharmacyUpdate):
        return self.repo.update(pharmacy_id, data)

    def delete_pharmacy(self, pharmacy_id: int):
        return self.repo.delete(pharmacy_id)