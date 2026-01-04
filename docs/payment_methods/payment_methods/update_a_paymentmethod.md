# Update a PaymentMethod

Updates a PaymentMethod object. A PaymentMethod must be attached to a customer to be updated.

## Returns

Returns a PaymentMethod object.

## Parameters

- `allow_redisplay` (enum, optional)
  This field indicates whether this payment method can be shown again to its customer in a checkout flow. Stripe products such as Checkout and Elements use this field to determine whether a payment method can be shown as a saved payment method in a checkout flow. The field defaults to `unspecified`.
Possible enum values:
  - `always`
    Use `always` to indicate that this payment method can always be shown to a customer in a checkout flow.

  - `limited`
    Use `limited` to indicate that this payment method can’t always be shown to a customer in a checkout flow. For example, it can only be shown in the context of a specific subscription.

  - `unspecified`
    This is the default value for payment methods where `allow_redisplay` wasn’t set.

- `billing_details` (object, optional)
  Billing information associated with the PaymentMethod that may be used or required by particular types of payment methods.

  - `billing_details.address` (object, optional)
    Billing address.

    - `billing_details.address.city` (string, optional)
      City, district, suburb, town, or village.

    - `billing_details.address.country` (string, optional)
      Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

    - `billing_details.address.line1` (string, optional)
      Address line 1, such as the street, PO Box, or company name.

    - `billing_details.address.line2` (string, optional)
      Address line 2, such as the apartment, suite, unit, or building.

    - `billing_details.address.postal_code` (string, optional)
      ZIP or postal code.

    - `billing_details.address.state` (string, optional)
      State, county, province, or region ([ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2)).

  - `billing_details.email` (string, optional)
    Email address.

    The maximum length is 800 characters.

  - `billing_details.name` (string, optional)
    Full name.

  - `billing_details.phone` (string, optional)
    Billing phone number (including extension).

  - `billing_details.tax_id` (string, optional)
    Taxpayer identification number. Used only for transactions between LATAM buyers and non-LATAM sellers.

- `card` (object, optional)
  If this is a `card` PaymentMethod, this hash contains the user’s card details.

  - `card.exp_month` (integer, optional)
    Two-digit number representing the card’s expiration month.

  - `card.exp_year` (integer, optional)
    Four-digit number representing the card’s expiration year.

  - `card.networks` (object, optional)
    Contains information about card networks used to process the payment.

    - `card.networks.preferred` (enum, optional)
      The customer’s preferred card network for co-branded cards. Supports `cartes_bancaires`, `mastercard`, or `visa`. Selection of a network that does not apply to the card will be stored as `invalid_preference` on the card.

- `metadata` (object, optional)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.

- `payto` (object, optional)
  If this is a `payto` PaymentMethod, this hash contains details about the PayTo payment method.

  - `payto.account_number` (string, optional)
    The account number for the bank account.

  - `payto.bsb_number` (string, optional)
    Bank-State-Branch number of the bank account.

  - `payto.pay_id` (string, optional)
    The PayID alias for the bank account.

- `us_bank_account` (object, optional)
  If this is an `us_bank_account` PaymentMethod, this hash contains details about the US bank account payment method.

  - `us_bank_account.account_holder_type` (enum, optional)
    Bank account holder type.
Possible enum values:
    - `company`
      Account belongs to a company

    - `individual`
      Account belongs to an individual

  - `us_bank_account.account_type` (enum, optional)
    Bank account type.
Possible enum values:
    - `checking`
      Bank account type is checking

    - `savings`
      Bank account type is savings

```curl
curl https://api.stripe.com/v1/payment_methods/pm_1Q0PsIJvEtkwdCNYMSaVuRz6 \
  -u "<<YOUR_SECRET_KEY>>" \
  -d "metadata[order_id]"=6735
```

```cli
stripe payment_methods update pm_1Q0PsIJvEtkwdCNYMSaVuRz6 \
  -d "metadata[order_id]"=6735
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

payment_method = client.v1.payment_methods.update(
  'pm_1Q0PsIJvEtkwdCNYMSaVuRz6',
  {metadata: {order_id: '6735'}},
)
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

payment_method = client.v1.payment_methods.update(
  "pm_1Q0PsIJvEtkwdCNYMSaVuRz6",
  {"metadata": {"order_id": "6735"}},
)
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$paymentMethod = $stripe->paymentMethods->update(
  'pm_1Q0PsIJvEtkwdCNYMSaVuRz6',
  ['metadata' => ['order_id' => '6735']]
);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

PaymentMethodUpdateParams params =
  PaymentMethodUpdateParams.builder().putMetadata("order_id", "6735").build();

PaymentMethod paymentMethod =
  client.v1().paymentMethods().update("pm_1Q0PsIJvEtkwdCNYMSaVuRz6", params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const paymentMethod = await stripe.paymentMethods.update(
  'pm_1Q0PsIJvEtkwdCNYMSaVuRz6',
  {
    metadata: {
      order_id: '6735',
    },
  }
);
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.PaymentMethodUpdateParams{}
params.AddMetadata("order_id", "6735")
result, err := sc.V1PaymentMethods.Update(
  context.TODO(), "pm_1Q0PsIJvEtkwdCNYMSaVuRz6", params)
```

```dotnet
var options = new PaymentMethodUpdateOptions
{
    Metadata = new Dictionary<string, string> { { "order_id", "6735" } },
};
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.PaymentMethods;
PaymentMethod paymentMethod = service.Update("pm_1Q0PsIJvEtkwdCNYMSaVuRz6", options);
```

### Response

```json
{
  "id": "pm_1Q0PsIJvEtkwdCNYMSaVuRz6",
  "object": "payment_method",
  "allow_redisplay": "unspecified",
  "billing_details": {
    "address": {
      "city": null,
      "country": null,
      "line1": null,
      "line2": null,
      "postal_code": null,
      "state": null
    },
    "email": null,
    "name": "John Doe",
    "phone": null
  },
  "created": 1726673582,
  "customer": null,
  "livemode": false,
  "metadata": {
    "order_id": "6735"
  },
  "type": "us_bank_account",
  "us_bank_account": {
    "account_holder_type": "individual",
    "account_type": "checking",
    "bank_name": "STRIPE TEST BANK",
    "financial_connections_account": null,
    "fingerprint": "LstWJFsCK7P349Bg",
    "last4": "6789",
    "networks": {
      "preferred": "ach",
      "supported": [
        "ach"
      ]
    },
    "routing_number": "110000000",
    "status_details": {}
  }
}
```