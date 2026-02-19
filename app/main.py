from fastapi import FastAPI
from app.core.database import engine, Base
from app.modules.pharmacy.models import Pharmacy
from app.modules.pharmacy.router import router as pharmacy_router


app = FastAPI(title='PharmaCore')

Base.metadata.create_all(bind=engine)

app.include_router(pharmacy_router)


@app.get('/')
def root():
    return {'message': 'PharmaCore API Running'}
