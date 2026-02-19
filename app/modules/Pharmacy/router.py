from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from .schemas import PharmacyCreate, PharmacyOut, PharmacyUpdate
from app.core.database import get_db
from .service import PharmacyService


router = APIRouter(prefix='/pharmacies', tags=['Pharmacies'])


@router.post('/', response_model=PharmacyOut)
def create_pharmacy(data: PharmacyCreate, db: Session = Depends(get_db)):
    service = PharmacyService(db)
    return service.create_pharmacy(data)


@router.get('/', response_model=list[PharmacyOut])
def get_pharmacies(db: Session = Depends(get_db)):
    service = PharmacyService(db)
    return service.list_pharmacies()


@router.get('/{pharmacy_id}', response_model=PharmacyOut)
def get_pharmacy(pharmacy_id: int, db : Session = Depends(get_db)):
    service = PharmacyService(db)
    pharmacy = service.get_pharmacy(pharmacy_id)
    if not pharmacy:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Pharmacy Not Found')
    return pharmacy
    

@router.patch('/{pharmacy_id}', response_model=PharmacyOut)
def update_pharmacy(pharmacy_id: int, data: PharmacyUpdate, db: Session = Depends(get_db)):
    service = PharmacyService(db)
    pharmacy = service.update_pharmacy(pharmacy_id, data)
    if not pharmacy:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Pharmacy Not Found')
    return pharmacy


@router.delete('/{pharmacy_id}', response_model=PharmacyOut)
def delete_pharmacy(pharmacy_id: int, db: Session = Depends(get_db)):
    service = PharmacyService(db)
    pharmacy = service.delete_pharmacy(pharmacy_id)
    if not pharmacy:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Pharmacy Not Found')
    return pharmacy