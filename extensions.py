import requests
import json
from config import keys, payload, headers

class ConversionException(Exception):
    pass

class Converter:

    @staticmethod
    def get_price(quote: str, base: str, amount: str):
        if quote == base:
            raise (ConversionException("Валюты должны быть разные"))

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise (ConversionException(f"Не удалось обработать валюту {quote}"))

        try:
            base_ticker = keys[base]
        except KeyError:
            raise (ConversionException(f"Не удалось обработать валюту {base}"))

        try:
            amount_val = float(amount)
        except ValueError:
            raise (ConversionException(f"Не удалось обработать количество валюты {amount}"))

        url = f"https://api.apilayer.com/fixer/convert?to={base_ticker}&from={quote_ticker}&amount={amount_val}"
        response = requests.request("GET", url, headers=headers, data=payload)

        result_json = json.loads(response.content)

        return result_json['result']