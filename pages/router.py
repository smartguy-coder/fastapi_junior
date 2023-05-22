from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter(
    prefix='/web'
)

templates = Jinja2Templates(directory='templates')


@router.get('/')
def get_main_crypto_info(request: Request):
    tags = ['currency', 'crypto', 'money']

    coins = [
        {'name': 'BTC', 'price': 500},
        {'name': 'LC', 'price': 200},
        {'name': 'ETH', 'price': 15},
    ]

    return templates.TemplateResponse(
        name='crypto_main.html',
        context={
            'request': request,
            'tags': tags,
            'coins': coins,
        },
    )
