import requests
import json
from config import keys
class ConvertionException(Exception):
    pass

class CryptoConverter:
    @staticmethod
    def convert(quote: str, base: str, amount: str):

        if quote == base:
            raise ConvertionException(f'Невозможно перевести одинаковые валюты {base}.')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertionException(f'не удалось обработать валюту {quote}')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {base}')

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(f'Не удалось обработать количество {amount}')

        r = requests.get(f"http://api.exchangeratesapi.io/v1/latest?access_key=03cafa375e7f4d865e4c3a9e90268431&format=1?base={base_ticker}&symbols={quote_ticker}")
        resp = json.loads(r.content)
        get_price = resp['rates'][quote_ticker] * amount
        get_price = round(get_price, 3)
        message =  f"Цена {amount} {base} в {quote}  : {get_price}"
        return message
