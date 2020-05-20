# cryptonatorAPI
Сreate Invoice
-----------------------------------
```
api = Api(
      merchant_id='4b8cc73b06e8205f4d212a7a8c0bb6497', 
      secret='b89a02b2801231fc8d60f65fe724448', 
      language='ru')
      
amount = Decimal('0.00015')
invoice_id = api.create_invoice(
      item_name='test_tovar', 
      invoice_amount=amount, 
      invoice_currency='bitcoin') #returns invoice_id
```

Check Invoice
-----------------------------------
```
status = api.check_invoice(invoice_id)
print(status)
```
