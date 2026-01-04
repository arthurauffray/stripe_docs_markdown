# List credit grants

Retrieve a list of credit grants.

## Returns

Returns a list of credit grants.

## Parameters

- `customer` (string, optional)
  Only return credit grants for this customer.

- `customer_account` (string, optional)
  Only return credit grants for this account representing the customer.

- `ending_before` (string, optional)
  A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.

- `limit` (integer, optional)
  A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.

- `starting_after` (string, optional)
  A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.

```curl
curl https://api.stripe.com/v1/billing/credit_grants \
  -u "<<YOUR_SECRET_KEY>>"
```

```cli
stripe billing credit_grants list
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

credit_grants = client.v1.billing.credit_grants.list()
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

credit_grants = client.v1.billing.credit_grants.list()
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$creditGrants = $stripe->billing->creditGrants->all([]);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

CreditGrantListParams params = CreditGrantListParams.builder().build();

StripeCollection<CreditGrant> stripeCollection =
  client.v1().billing().creditGrants().list(params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const creditGrants = await stripe.billing.creditGrants.list();
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.BillingCreditGrantListParams{}
result := sc.V1BillingCreditGrants.List(context.TODO(), params)
```

```dotnet
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Billing.CreditGrants;
StripeList<Stripe.Billing.CreditGrant> creditGrants = service.List();
```

### Response

```json
{
  "object": "list",
  "data": [
    {
      "id": "credgr_test_61R9a6NUWsRmOW3RM41L6nFOS1ekDGHo",
      "object": "billing.credit_grant",
      "amount": {
        "monetary": {
          "currency": "usd",
          "value": 1000
        },
        "type": "monetary"
      },
      "applicability_config": {
        "scope": {
          "price_type": "metered"
        }
      },
      "category": "paid",
      "created": 1726620803,
      "customer": "cus_QrvQguzkIK8zTj",
      "effective_at": 1729297860,
      "expires_at": null,
      "livemode": false,
      "metadata": {},
      "name": "Purchased Credits",
      "priority": 50,
      "test_clock": null,
      "updated": 1726620803,
      "voided_at": null
    }
  ],
  "has_more": false,
  "url": "/v1/billing/credit_grants"
}
```