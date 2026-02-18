from fastapi import FastAPI
from app.core.database import engine, Base


app = FastAPI(title='PharmaCore')


@app.get('/')
def root():
    return {'message': 'PharmaCore API Running'}