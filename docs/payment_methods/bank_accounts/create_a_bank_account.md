# Create a bank account

When you create a new bank account, you must specify a `Customer` object on which to create it.

## Returns

Returns the bank account object.

## Parameters

- `source` (object | string, required)
  Either a token, like the ones returned by [Stripe.js](https://docs.stripe.com/docs/js.md), or a dictionary containing a user’s bank account details (with the options shown below).

  - `source.account_number` (string, required)
    The account number for the bank account, in string form. Must be a checking account.

  - `source.country` (string, required)
    The country in which the bank account is located.

  - `source.currency` (string, required)
    The currency the bank account is in. This must be a country/currency pairing that [Stripe supports](https://docs.stripe.com/docs/payouts.md).

  - `source.object` (string, required)
    The type of external account. Should be `bank_account`

  - `source.account_holder_name` (string, optional)
    The name of the person or business that owns the bank account. This field is required when attaching the bank account to a `Customer` object.

  - `source.account_holder_type` (enum, optional)
    The type of entity that holds the account. This field is required when attaching the bank account to a `Customer` object.
Possible enum values:
    - `company`
    - `individual`

  - `source.routing_number` (string, optional)
    The routing number, sort code, or other country-appropriate institution number for the bank account. For US bank accounts, this is required and should be the ACH routing number, not the wire routing number. If you are providing an IBAN for `account_number`, this field is not required.

- `metadata` (object, optional)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.

```curl
curl https://api.stripe.com/v1/customers/cus_9s6XI9OFIdpjIg/sources \
  -u "<<YOUR_SECRET_KEY>>" \
  -d source=btok_1MvoS32eZvKYlo2CDhGTErAe
```

```cli
stripe payment_sources create cus_9s6XI9OFIdpjIg \
  --source=btok_1MvoS32eZvKYlo2CDhGTErAe
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

result = client.v1.customers.payment_sources.create(
  'cus_9s6XI9OFIdpjIg',
  {source: 'btok_1MvoS32eZvKYlo2CDhGTErAe'},
)
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

payment_source = client.v1.customers.payment_sources.create(
  "cus_9s6XI9OFIdpjIg",
  {"source": "btok_1MvoS32eZvKYlo2CDhGTErAe"},
)
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$paymentSource = $stripe->customers->createSource(
  'cus_9s6XI9OFIdpjIg',
  ['source' => 'btok_1MvoS32eZvKYlo2CDhGTErAe']
);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

CustomerPaymentSourceCreateParams params =
  CustomerPaymentSourceCreateParams.builder()
    .setSource("btok_1MvoS32eZvKYlo2CDhGTErAe")
    .build();

PaymentSource paymentSource =
  client.v1().customers().paymentSources().create("cus_9s6XI9OFIdpjIg", params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const customerSource = await stripe.customers.createSource(
  'cus_9s6XI9OFIdpjIg',
  {
    source: 'btok_1MvoS32eZvKYlo2CDhGTErAe',
  }
);
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.PaymentSourceCreateParams{
  Source: stripe.String("btok_1MvoS32eZvKYlo2CDhGTErAe"),
  Customer: stripe.String("cus_9s6XI9OFIdpjIg"),
}
result, err := sc.V1PaymentSources.Create(context.TODO(), params)
```

```dotnet
var options = new CustomerPaymentSourceCreateOptions
{
    Source = "btok_1MvoS32eZvKYlo2CDhGTErAe",
};
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Customers.PaymentSources;
IPaymentSource iPaymentSource = service.Create("cus_9s6XI9OFIdpjIg", options);
```

### Response

```json
{
  "id": "ba_1MvoIJ2eZvKYlo2CO9f0MabO",
  "object": "bank_account",
  "account_holder_name": "Jane Austen",
  "account_holder_type": "company",
  "account_type": null,
  "bank_name": "STRIPE TEST BANK",
  "country": "US",
  "currency": "usd",
  "customer": "cus_9s6XI9OFIdpjIg",
  "fingerprint": "1JWtPxqbdX5Gamtc",
  "last4": "6789",
  "metadata": {},
  "routing_number": "110000000",
  "status": "new"
}
```