# cryptonatorAPI

Все для вас, HashBotted

Installation using pip
-----------------------------------
`pip install cryptonator-API`


Import
-----------------------------------

```python
cryptonator_API import cryptonatorAPI
from decimal import Decimal
```


Сreate Invoice
-----------------------------------
```python
api = cryptonatorAPI(
      merchant_id='4b8cc73b06e8205f4d212a7a8c0bb6497', 
      secret='b89a02b2801231fc8d60f65fe724448', 
      language='ru')
      
amount = Decimal('0.00015')

invoice_id = api.create_invoice(
      item_name='test_tovar', 
      invoice_amount=amount, 
      invoice_currency='bitcoin') 
      
#returns invoice_id
```

Check Invoice
-----------------------------------
```python
status = api.check_invoice(invoice_id)
print(status)

#{'order_id': '2636351', 'amount': '0.00015000', 'currency': 'bitcoin', 'status': 'unpaid'}
```
