import requests
import hashlib
from decimal import Decimal



class Api:
    url = 'https://api.cryptonator.com/api/merchant/v1/'

    def __init__(self, merchant_id, secret, language):
        self.merchant_id = merchant_id
        self.secret = secret
        self.language = language
        self.user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
        self.headers = {"User-Agent": self.user_agent}

    def create_invoice(self, item_name, invoice_amount, invoice_currency):
        response = requests.get(url=self.url + 'startpayment', params={
            'merchant_id': self.merchant_id,
            'item_name': item_name,
            'invoice_amount': invoice_amount,
            'invoice_currency': invoice_currency,
        }, headers=self.headers)
        invoice_id = str(response.url).split('/')[-1]
        return invoice_id

    def check_invoice(self, invoice_id):
        hash = hashlib.sha1(f'{self.merchant_id}&{invoice_id}&{self.secret}'.encode())
        response = requests.post(url=self.url + 'getinvoice', headers=self.headers,
                                 data={
                                     'merchant_id': self.merchant_id,
                                     'invoice_id': invoice_id,
                                     'secret_hash': hash.hexdigest()
                                 })
        return response.json()


api = Api(merchant_id='4b8cc73b06e8205f4d232578c0bb6497', secret='b89a02b2802846bfc8d60f65fe724448', language='ru')
amount = Decimal('0.00015')
invoice_id = api.create_invoice(item_name='test_tovar', invoice_amount=amount, invoice_currency='bitcoin')
status = api.check_invoice(invoice_id)
print(status)
