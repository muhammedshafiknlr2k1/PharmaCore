from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.core.database import get_db
from .schemas import BatchCreate, BatchUpdate, BatchOut
from .service import BatchService


router = APIRouter(prefix='/batches', tags=['Batches'])


@router.post('/', response_model=BatchOut)
def create_batch(data: BatchCreate, db: Session = Depends(get_db)):
    service = BatchService(db)
    return service.create_batch(data)


@router.get('/', response_model=List[BatchOut])
def list_batches(db: Session = Depends(get_db)):
    service = BatchService(db)
    return service.list_batches()


@router.get('/{batch_id}', response_model=BatchOut)
def get_batch(batch_id: int, db: Session = Depends(get_db)):
    service = BatchService(db)
    try:
        return service.get_batch(batch_id)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    

@router.get('/medicine/{medicine_id}', response_model=List[BatchOut])
def get_batches_by_medicine(medicine_id: int, db: Session = Depends(get_db)):
    service = BatchService(db)
    return service.list_batches_by_medicine(medicine_id)


@router.get('/pharmacy/{pharmacy_id}', response_model=List[BatchOut])
def get_batches_by_pharmacy(pharmacy_id: int, db: Session = Depends(get_db)):
    service = BatchService(db)
    return service.list_batches_by_pharmacy(pharmacy_id)


@router.patch('/{batch_id}', response_model=BatchOut)
def update_batch(batch_id: int, data: BatchUpdate, db: Session = Depends(get_db)):
    service = BatchService(db)
    try:
        return service.update_batch(batch_id, data)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    

@router.delete('/{batch_id}', response_model=BatchOut)
def delete_batch(batch_id: int, db: Session = Depends(get_db)):
    service = BatchService(db)
    try:
        return service.delete_batch(batch_id)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    