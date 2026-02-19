from fastapi import FastAPI
from app.core.database import engine, Base
from app.modules.pharmacy.models import Pharmacy


app = FastAPI(title='PharmaCore')

Base.metadata.create_all(bind=engine)


@app.get('/')
def root():
    return {'message': 'PharmaCore API Running'}
