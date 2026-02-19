from fastapi import FastAPI
from app.core.database import engine, Base
from app.modules.pharmacy.models import Pharmacy
from app.modules.pharmacy.router import router as pharmacy_router
from app.modules.medicine.router import router as medicine_router
from app.modules.batch.router import router as batch_router


app = FastAPI(title='PharmaCore')

Base.metadata.create_all(bind=engine)

app.include_router(pharmacy_router)
app.include_router(medicine_router)
app.include_router(batch_router)


@app.get('/')
def root():
    return {'message': 'PharmaCore API Running'}
