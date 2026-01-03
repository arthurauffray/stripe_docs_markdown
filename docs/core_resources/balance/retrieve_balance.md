# Retrieve balance

Retrieves the current account balance, based on the authentication that was used to make the request. For a sample request, see [Accounting for negative balances](https://docs.stripe.com/docs/connect/account-balances.md#accounting-for-negative-balances).

## Returns

Returns a balance object for the account that was authenticated in the request.

```curl
curl https://api.stripe.com/v1/balance \
  -u "<<YOUR_SECRET_KEY>>"
```

```cli
stripe balance retrieve
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

balance = client.v1.balance.retrieve()
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

balance = client.v1.balance.retrieve()
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$balance = $stripe->balance->retrieve([]);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

BalanceRetrieveParams params = BalanceRetrieveParams.builder().build();

Balance balance = client.v1().balance().retrieve(params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const balance = await stripe.balance.retrieve();
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.BalanceRetrieveParams{}
result, err := sc.V1Balance.Retrieve(context.TODO(), params)
```

```dotnet
var options = new BalanceGetOptions();
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Balance;
Balance balance = service.Get(options);
```

### Response

```json
{
  "object": "balance",
  "available": [
    {
      "amount": 666670,
      "currency": "usd",
      "source_types": {
        "card": 666670
      }
    }
  ],
  "connect_reserved": [
    {
      "amount": 0,
      "currency": "usd"
    }
  ],
  "livemode": false,
  "pending": [
    {
      "amount": 61414,
      "currency": "usd",
      "source_types": {
        "card": 61414
      }
    }
  ]
}
```