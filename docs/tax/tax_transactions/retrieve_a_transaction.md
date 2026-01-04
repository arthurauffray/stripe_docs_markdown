# Retrieve a transaction

Retrieves a Tax `Transaction` object.

## Returns

A Tax `Transaction` object.

```curl
curl https://api.stripe.com/v1/tax/transactions/tax_1NaS0I2eZvKYlo2CRuMhUcmz \
  -u "<<YOUR_SECRET_KEY>>"
```

```cli
stripe tax transactions retrieve tax_1NaS0I2eZvKYlo2CRuMhUcmz
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

transaction = client.v1.tax.transactions.retrieve('tax_1NaS0I2eZvKYlo2CRuMhUcmz')
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

transaction = client.v1.tax.transactions.retrieve("tax_1NaS0I2eZvKYlo2CRuMhUcmz")
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$transaction = $stripe->tax->transactions->retrieve(
  'tax_1NaS0I2eZvKYlo2CRuMhUcmz',
  []
);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

TransactionRetrieveParams params = TransactionRetrieveParams.builder().build();

Transaction transaction =
  client.v1().tax().transactions().retrieve("tax_1NaS0I2eZvKYlo2CRuMhUcmz", params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const transaction = await stripe.tax.transactions.retrieve(
  'tax_1NaS0I2eZvKYlo2CRuMhUcmz'
);
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.TaxTransactionRetrieveParams{}
result, err := sc.V1TaxTransactions.Retrieve(
  context.TODO(), "tax_1NaS0I2eZvKYlo2CRuMhUcmz", params)
```

```dotnet
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Tax.Transactions;
Stripe.Tax.Transaction transaction = service.Get("tax_1NaS0I2eZvKYlo2CRuMhUcmz");
```

### Response

```json
{
  "id": "tax_1NaS0I2eZvKYlo2CRuMhUcmz",
  "object": "tax.transaction",
  "created": 1690932566,
  "currency": "usd",
  "customer": null,
  "customer_details": {
    "address": {
      "city": "South San Francisco",
      "country": "US",
      "line1": "354 Oyster Point Blvd",
      "line2": "",
      "postal_code": "94080",
      "state": "CA"
    },
    "address_source": "shipping",
    "ip_address": null,
    "tax_ids": [],
    "taxability_override": "none"
  },
  "line_items": {
    "object": "list",
    "data": [
      {
        "id": "tax_li_ONCP443tgfS8I1",
        "object": "tax.transaction_line_item",
        "amount": 1499,
        "amount_tax": 148,
        "livemode": false,
        "metadata": null,
        "product": null,
        "quantity": 1,
        "reference": "Pepperoni Pizza",
        "reversal": null,
        "tax_behavior": "exclusive",
        "tax_code": "txcd_40060003",
        "type": "transaction"
      }
    ],
    "has_more": false,
    "url": "/v1/tax/transactions/tax_1NaS0I2eZvKYlo2CRuMhUcmz/line_items"
  },
  "livemode": false,
  "metadata": null,
  "posted_at": 1690932566,
  "reference": "myOrder_123",
  "reversal": null,
  "shipping_cost": {
    "amount": 300,
    "amount_tax": 0,
    "tax_behavior": "exclusive",
    "tax_code": "txcd_92010001"
  },
  "ship_from_details": {
    "address": {
      "postal_code": "75001",
      "state": "TX",
      "country": "US"
    }
  },
  "tax_date": 1690932566,
  "type": "transaction"
}
```