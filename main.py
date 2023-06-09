import shutil

from fastapi import FastAPI, UploadFile, File
from fastapi.staticfiles import StaticFiles
import sentry_sdk

from pages.router import router
import schemas
# import library


sentry_sdk.init(
    dsn="https://ce2a4e37e7eb425181834b68194dfbe9@o4505229726318592.ingest.sentry.io/4505250941698048",
    traces_sample_rate=1.0,
)

app = FastAPI(title='CryptoData', version='1.0')

app.mount('/static', StaticFiles(directory='static'), name='static')
app.include_router(router)


# @app.on_event('startup')
# def startup():
#     library.send_telegram_message('API app started')
#
#
# @app.on_event('shutdown')
# def shutdown():
#     library.send_telegram_message('API app closed')


@app.post('/{name}/{age}', response_model=schemas.Coin)
def index(name: str, age: int, coin: schemas.Coin):
    message = 'root endpoint'

    return {'message': coin}


@app.get('/new/data')
def new():
    return {'new': True}


@app.get('/{number}')
def number_decreaser(number: int, query: int = None):
    if query is not None:
        result = number / query
    else:
        result = number / 2

    return {
        'message': 'ok',
        'result': result,
    }


@app.post('/file')
def file_upload(file: UploadFile = File(...)):
    with open(f'downloads/{file.filename}', 'wb') as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {}
