# Finalize a test-mode authorization's amount

Finalize the amount on an Authorization prior to capture, when the initial authorization was for an estimated amount.

## Returns

An Authorization object

## Parameters

- `final_amount` (integer, required)
  The final authorization amount that will be captured by the merchant. This amount is in the authorization currency and in the [smallest currency unit](https://docs.stripe.com/docs/currencies.md#zero-decimal).

- `fleet` (object, optional)
  Fleet-specific information for authorizations using Fleet cards.

  - `fleet.cardholder_prompt_data` (object, optional)
    Answers to prompts presented to the cardholder at the point of sale. Prompted fields vary depending on the configuration of your physical fleet cards. Typical points of sale support only numeric entry.

    - `fleet.cardholder_prompt_data.driver_id` (string, optional)
      Driver ID.

    - `fleet.cardholder_prompt_data.odometer` (integer, optional)
      Odometer reading.

    - `fleet.cardholder_prompt_data.unspecified_id` (string, optional)
      An alphanumeric ID. This field is used when a vehicle ID, driver ID, or generic ID is entered by the cardholder, but the merchant or card network did not specify the prompt type.

    - `fleet.cardholder_prompt_data.user_id` (string, optional)
      User ID.

    - `fleet.cardholder_prompt_data.vehicle_number` (string, optional)
      Vehicle number.

  - `fleet.purchase_type` (string, optional)
    The type of purchase. One of `fuel_purchase`, `non_fuel_purchase`, or `fuel_and_non_fuel_purchase`.

  - `fleet.reported_breakdown` (object, optional)
    More information about the total amount. This information is not guaranteed to be accurate as some merchants may provide unreliable data.

    - `fleet.reported_breakdown.fuel` (object, optional)
      Breakdown of fuel portion of the purchase.

      - `fleet.reported_breakdown.fuel.gross_amount_decimal` (string, optional)
        Gross fuel amount that should equal Fuel Volume multipled by Fuel Unit Cost, inclusive of taxes.

    - `fleet.reported_breakdown.non_fuel` (object, optional)
      Breakdown of non-fuel portion of the purchase.

      - `fleet.reported_breakdown.non_fuel.gross_amount_decimal` (string, optional)
        Gross non-fuel amount that should equal the sum of the line items, inclusive of taxes.

    - `fleet.reported_breakdown.tax` (object, optional)
      Information about tax included in this transaction.

      - `fleet.reported_breakdown.tax.local_amount_decimal` (string, optional)
        Amount of state or provincial Sales Tax included in the transaction amount. Null if not reported by merchant or not subject to tax.

      - `fleet.reported_breakdown.tax.national_amount_decimal` (string, optional)
        Amount of national Sales Tax or VAT included in the transaction amount. Null if not reported by merchant or not subject to tax.

  - `fleet.service_type` (string, optional)
    The type of fuel service. One of `non_fuel_transaction`, `full_service`, or `self_service`.

- `fuel` (object, optional)
  Information about fuel that was purchased with this transaction.

  - `fuel.industry_product_code` (string, optional)
    [Conexxus Payment System Product Code](https://www.conexxus.org/conexxus-payment-system-product-codes) identifying the primary fuel product purchased.

  - `fuel.quantity_decimal` (string, optional)
    The quantity of `unit`s of fuel that was dispensed, represented as a decimal string with at most 12 decimal places.

  - `fuel.type` (string, optional)
    The type of fuel that was purchased. One of `diesel`, `unleaded_plus`, `unleaded_regular`, `unleaded_super`, or `other`.

  - `fuel.unit` (string, optional)
    The units for `quantity_decimal`. One of `charging_minute`, `imperial_gallon`, `kilogram`, `kilowatt_hour`, `liter`, `pound`, `us_gallon`, or `other`.

  - `fuel.unit_cost_decimal` (string, optional)
    The cost in cents per each unit of fuel, represented as a decimal string with at most 12 decimal places.

```curl
curl https://api.stripe.com/v1/test_helpers/issuing/authorizations/iauth_1DPc772eZvKYlo2C6avLyZ25/finalize_amount \
  -u "<<YOUR_SECRET_KEY>>" \
  -d final_amount=1000
```

```cli
stripe test_helpers issuing authorizations finalize_amount iauth_1DPc772eZvKYlo2C6avLyZ25 \
  --final-amount=1000
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

authorization = client.v1.test_helpers.issuing.authorizations.finalize_amount(
  'iauth_1DPc772eZvKYlo2C6avLyZ25',
  {final_amount: 1000},
)
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

authorization = client.v1.test_helpers.issuing.authorizations.finalize_amount(
  "iauth_1DPc772eZvKYlo2C6avLyZ25",
  {"final_amount": 1000},
)
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$authorization = $stripe->testHelpers->issuing->authorizations->finalizeAmount(
  'iauth_1DPc772eZvKYlo2C6avLyZ25',
  ['final_amount' => 1000]
);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

AuthorizationFinalizeAmountParams params =
  AuthorizationFinalizeAmountParams.builder().setFinalAmount(1000L).build();

Authorization authorization =
  client.v1().testHelpers().issuing().authorizations().finalizeAmount(
    "iauth_1DPc772eZvKYlo2C6avLyZ25",
    params
  );
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const authorization = await stripe.testHelpers.issuing.authorizations.finalizeAmount(
  'iauth_1DPc772eZvKYlo2C6avLyZ25',
  {
    final_amount: 1000,
  }
);
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.TestHelpersIssuingAuthorizationFinalizeAmountParams{
  FinalAmount: stripe.Int64(1000),
}
result, err := sc.V1TestHelpersIssuingAuthorizations.FinalizeAmount(
  context.TODO(), "iauth_1DPc772eZvKYlo2C6avLyZ25", params)
```

```dotnet
var options = new Stripe.TestHelpers.Issuing.AuthorizationFinalizeAmountOptions
{
    FinalAmount = 1000,
};
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.TestHelpers.Issuing.Authorizations;
Stripe.Issuing.Authorization authorization = service.FinalizeAmount(
    "iauth_1DPc772eZvKYlo2C6avLyZ25",
    options);
```

### Response

```json
{
  "id": "iauth_1DPc772eZvKYlo2C6avLyZ25",
  "object": "issuing.authorization",
  "amount": 1000,
  "amount_details": {
    "atm_fee": null,
    "cashback_amount": null
  },
  "approved": true,
  "authorization_method": "chip",
  "balance_transactions": [],
  "card": "ic_1Nsse72eZvKYlo2CWBGm2WQ5",
  "cardholder": "ich_1Ccy6F2eZvKYlo2ClnIm9bs4",
  "created": 1540586461,
  "currency": "usd",
  "livemode": false,
  "merchant_amount": 1000,
  "merchant_currency": "usd",
  "merchant_data": {
    "category": "automated_fuel_dispensers",
    "category_code": "5542",
    "city": "San Francisco",
    "country": "US",
    "name": "Rocket Rides",
    "network_id": "1234567890",
    "postal_code": "94107",
    "state": "CA",
    "terminal_id": null
  },
  "metadata": {},
  "network_data": null,
  "pending_request": null,
  "redaction": null,
  "request_history": [],
  "status": "reversed",
  "transactions": [],
  "verification_data": {
    "address_line1_check": "not_provided",
    "address_postal_code_check": "match",
    "cvc_check": "match",
    "expiry_check": "match"
  },
  "wallet": null
}
```