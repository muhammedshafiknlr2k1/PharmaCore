from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from .schemas import MedicineCreate, MedicineUpdate, MedicineOut
from .service import MedicineService
from app.core.database import get_db
from typing import List


router = APIRouter(prefix='/medicines', tags=['Medicines'])


@router.post('/', response_model=MedicineOut)
def create_medicine(data: MedicineCreate, db: Session = Depends(get_db)):
    service = MedicineService(db)
    return service.create_medicine(data)


@router.get('/', response_model=List[MedicineOut])
def list_medicines(db: Session = Depends(get_db)):
    service = MedicineService(db)
    return service.list_medicines()


@router.get('/{medicine_id}', response_model=MedicineOut)
def get_medicine(medicine_id: int, db: Session = Depends(get_db)):
    service = MedicineService(db)
    try:
        return service.get_medicine(medicine_id)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    

@router.patch('/medicine_id', response_model=MedicineOut)
def update_medicine(medicine_id: int, data: MedicineUpdate, db: Session = Depends(get_db)):
    service = MedicineService(db)
    try:
        return service.update_medicine(medicine_id, data)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    

@router.delete('/{medicine_id}', response_model=MedicineOut)
def delete_medicine(medicine_id: int, db: Session = Depends(get_db)):
    service = MedicineService(db)
    try:
        return service.delete_medicine(medicine_id)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    
    