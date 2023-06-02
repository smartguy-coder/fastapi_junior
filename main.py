from fastapi import FastAPI
import sentry_sdk

from pages.router import router
# import library


sentry_sdk.init(
    dsn="https://ce2a4e37e7eb425181834b68194dfbe9@o4505229726318592.ingest.sentry.io/4505250941698048",
    traces_sample_rate=1.0,
)

app = FastAPI(title='CryptoData', version='1.0')
app.include_router(router)


# @app.on_event('startup')
# def startup():
#     library.send_telegram_message('API app started')
#
#
# @app.on_event('shutdown')
# def shutdown():
#     library.send_telegram_message('API app closed')


@app.get('/')
def index():
    message = 'root endpoint'
    # library.send_telegram_message(message)
    return {'message': message}


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
