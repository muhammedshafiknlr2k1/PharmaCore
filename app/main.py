from fastapi import FastAPI


app = FastAPI(title='PharmaCore')


@app.get('/')
def root():
    return {'message': 'PharmaCore API Running'}