from cryptonatorAPI import Api
from decimal import Decimal

api = Api(merchant_id='4b8cc73b06e8205f4d232578c0bb6497', secret='b89a02b2802846bfc8d60f65fe724448', language='ru')
amount = Decimal('0.00015')
invoice_id = api.create_invoice(item_name='test_tovar', invoice_amount=amount, invoice_currency='bitcoin')
status = api.check_invoice(invoice_id)
print(status)
