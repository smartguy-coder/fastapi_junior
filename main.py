from fastapi import FastAPI

from pages.router import router

app = FastAPI(title='CryptoData', version='1.0')
app.include_router(router)


@app.get('/')
def index():
    return {'message': 'we are here'}


@app.get('/{number}')
def number_increaser(number: int, query: int = None):
    if query:
        result = number * query
    else:
        result = number * 2

    return {
        'message': 'ok',
        'result': result,
    }
