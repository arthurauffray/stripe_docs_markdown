# Capture a test-mode authorization

Capture a test-mode authorization.

## Returns

An Authorization object.

## Parameters

- `capture_amount` (integer, optional)
  The amount to capture from the authorization. If not provided, the full amount of the authorization will be captured. This amount is in the authorization currency and in the [smallest currency unit](https://docs.stripe.com/docs/currencies.md#zero-decimal).

- `close_authorization` (boolean, optional)
  Whether to close the authorization after capture. Defaults to true. Set to false to enable multi-capture flows.

- `purchase_details` (object, optional)
  Additional purchase information that is optionally provided by the merchant.

  - `purchase_details.fleet` (object, optional)
    Fleet-specific information for transactions using Fleet cards.

    - `purchase_details.fleet.cardholder_prompt_data` (object, optional)
      Answers to prompts presented to the cardholder at the point of sale. Prompted fields vary depending on the configuration of your physical fleet cards. Typical points of sale support only numeric entry.

      - `purchase_details.fleet.cardholder_prompt_data.driver_id` (string, optional)
        Driver ID.

      - `purchase_details.fleet.cardholder_prompt_data.odometer` (integer, optional)
        Odometer reading.

      - `purchase_details.fleet.cardholder_prompt_data.unspecified_id` (string, optional)
        An alphanumeric ID. This field is used when a vehicle ID, driver ID, or generic ID is entered by the cardholder, but the merchant or card network did not specify the prompt type.

      - `purchase_details.fleet.cardholder_prompt_data.user_id` (string, optional)
        User ID.

      - `purchase_details.fleet.cardholder_prompt_data.vehicle_number` (string, optional)
        Vehicle number.

    - `purchase_details.fleet.purchase_type` (string, optional)
      The type of purchase. One of `fuel_purchase`, `non_fuel_purchase`, or `fuel_and_non_fuel_purchase`.

    - `purchase_details.fleet.reported_breakdown` (object, optional)
      More information about the total amount. This information is not guaranteed to be accurate as some merchants may provide unreliable data.

      - `purchase_details.fleet.reported_breakdown.fuel` (object, optional)
        Breakdown of fuel portion of the purchase.

        - `purchase_details.fleet.reported_breakdown.fuel.gross_amount_decimal` (string, optional)
          Gross fuel amount that should equal Fuel Volume multipled by Fuel Unit Cost, inclusive of taxes.

      - `purchase_details.fleet.reported_breakdown.non_fuel` (object, optional)
        Breakdown of non-fuel portion of the purchase.

        - `purchase_details.fleet.reported_breakdown.non_fuel.gross_amount_decimal` (string, optional)
          Gross non-fuel amount that should equal the sum of the line items, inclusive of taxes.

      - `purchase_details.fleet.reported_breakdown.tax` (object, optional)
        Information about tax included in this transaction.

        - `purchase_details.fleet.reported_breakdown.tax.local_amount_decimal` (string, optional)
          Amount of state or provincial Sales Tax included in the transaction amount. Null if not reported by merchant or not subject to tax.

        - `purchase_details.fleet.reported_breakdown.tax.national_amount_decimal` (string, optional)
          Amount of national Sales Tax or VAT included in the transaction amount. Null if not reported by merchant or not subject to tax.

    - `purchase_details.fleet.service_type` (string, optional)
      The type of fuel service. One of `non_fuel_transaction`, `full_service`, or `self_service`.

  - `purchase_details.flight` (object, optional)
    Information about the flight that was purchased with this transaction.

    - `purchase_details.flight.departure_at` (timestamp, optional)
      The time that the flight departed.

    - `purchase_details.flight.passenger_name` (string, optional)
      The name of the passenger.

    - `purchase_details.flight.refundable` (boolean, optional)
      Whether the ticket is refundable.

    - `purchase_details.flight.segments` (array of objects, optional)
      The legs of the trip.

      - `purchase_details.flight.segments.arrival_airport_code` (string, optional)
        The three-letter IATA airport code of the flight’s destination.

        The maximum length is 3 characters.

      - `purchase_details.flight.segments.carrier` (string, optional)
        The airline carrier code.

      - `purchase_details.flight.segments.departure_airport_code` (string, optional)
        The three-letter IATA airport code that the flight departed from.

        The maximum length is 3 characters.

      - `purchase_details.flight.segments.flight_number` (string, optional)
        The flight number.

      - `purchase_details.flight.segments.service_class` (string, optional)
        The flight’s service class.

      - `purchase_details.flight.segments.stopover_allowed` (boolean, optional)
        Whether a stopover is allowed on this flight.

    - `purchase_details.flight.travel_agency` (string, optional)
      The travel agency that issued the ticket.

  - `purchase_details.fuel` (object, optional)
    Information about fuel that was purchased with this transaction.

    - `purchase_details.fuel.industry_product_code` (string, optional)
      [Conexxus Payment System Product Code](https://www.conexxus.org/conexxus-payment-system-product-codes) identifying the primary fuel product purchased.

    - `purchase_details.fuel.quantity_decimal` (string, optional)
      The quantity of `unit`s of fuel that was dispensed, represented as a decimal string with at most 12 decimal places.

    - `purchase_details.fuel.type` (string, optional)
      The type of fuel that was purchased. One of `diesel`, `unleaded_plus`, `unleaded_regular`, `unleaded_super`, or `other`.

    - `purchase_details.fuel.unit` (string, optional)
      The units for `quantity_decimal`. One of `charging_minute`, `imperial_gallon`, `kilogram`, `kilowatt_hour`, `liter`, `pound`, `us_gallon`, or `other`.

    - `purchase_details.fuel.unit_cost_decimal` (string, optional)
      The cost in cents per each unit of fuel, represented as a decimal string with at most 12 decimal places.

  - `purchase_details.lodging` (object, optional)
    Information about lodging that was purchased with this transaction.

    - `purchase_details.lodging.check_in_at` (timestamp, optional)
      The time of checking into the lodging.

    - `purchase_details.lodging.nights` (integer, optional)
      The number of nights stayed at the lodging.

  - `purchase_details.receipt` (array of objects, optional)
    The line items in the purchase.

  - `purchase_details.reference` (string, optional)
    A merchant-specific order number.

```curl
curl -X POST https://api.stripe.com/v1/test_helpers/issuing/authorizations/iauth_1DPc772eZvKYlo2C6avLyZ25/capture \
  -u "<<YOUR_SECRET_KEY>>"
```

```cli
stripe test_helpers issuing authorizations capture iauth_1DPc772eZvKYlo2C6avLyZ25
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

authorization = client.v1.test_helpers.issuing.authorizations.capture('iauth_1DPc772eZvKYlo2C6avLyZ25')
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

authorization = client.v1.test_helpers.issuing.authorizations.capture(
  "iauth_1DPc772eZvKYlo2C6avLyZ25",
)
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$authorization = $stripe->testHelpers->issuing->authorizations->capture(
  'iauth_1DPc772eZvKYlo2C6avLyZ25',
  []
);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

AuthorizationCaptureParams params = AuthorizationCaptureParams.builder().build();

Authorization authorization =
  client.v1().testHelpers().issuing().authorizations().capture(
    "iauth_1DPc772eZvKYlo2C6avLyZ25",
    params
  );
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const authorization = await stripe.testHelpers.issuing.authorizations.capture(
  'iauth_1DPc772eZvKYlo2C6avLyZ25'
);
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.TestHelpersIssuingAuthorizationCaptureParams{}
result, err := sc.V1TestHelpersIssuingAuthorizations.Capture(
  context.TODO(), "iauth_1DPc772eZvKYlo2C6avLyZ25", params)
```

```dotnet
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.TestHelpers.Issuing.Authorizations;
Stripe.Issuing.Authorization authorization = service.Capture(
    "iauth_1DPc772eZvKYlo2C6avLyZ25");
```

### Response

```json
{
  "id": "iauth_1DPc772eZvKYlo2C6avLyZ25",
  "object": "issuing.authorization",
  "amount": 0,
  "amount_details": {
    "atm_fee": null,
    "cashback_amount": null
  },
  "approved": true,
  "authorization_method": "keyed_in",
  "balance_transactions": [],
  "card": {
    "id": "ic_1FEiQC2eZvKYlo2CtahKepKy",
    "object": "issuing.card",
    "brand": "Visa",
    "cancellation_reason": null,
    "cardholder": {
      "id": "ich_1Ccy6F2eZvKYlo2ClnIm9bs4",
      "object": "issuing.cardholder",
      "billing": {
        "address": {
          "city": "Beverly Hills",
          "country": "US",
          "line1": "123 Fake St",
          "line2": "Apt 3",
          "postal_code": "90210",
          "state": "CA"
        }
      },
      "company": null,
      "created": 1528992903,
      "email": "jenny@example.com",
      "individual": null,
      "livemode": false,
      "metadata": {},
      "name": "Jenny Rosen",
      "phone_number": "+18008675309",
      "preferred_locales": [],
      "redaction": null,
      "requirements": {
        "disabled_reason": null,
        "past_due": []
      },
      "spending_controls": {
        "allowed_categories": [],
        "blocked_categories": [],
        "spending_limits": [],
        "spending_limits_currency": null
      },
      "status": "active",
      "type": "individual"
    },
    "created": 1567541772,
    "currency": "usd",
    "exp_month": 12,
    "exp_year": 2020,
    "last4": "4242",
    "livemode": false,
    "metadata": {
      "status": "canceled"
    },
    "redaction": null,
    "replaced_by": null,
    "replacement_for": null,
    "replacement_reason": null,
    "shipping": null,
    "spending_controls": {
      "allowed_categories": null,
      "blocked_categories": null,
      "spending_limits": [],
      "spending_limits_currency": null
    },
    "status": "canceled",
    "type": "physical",
    "wallets": {
      "apple_pay": {
        "eligible": true,
        "ineligible_reason": null
      },
      "google_pay": {
        "eligible": false,
        "ineligible_reason": "missing_agreement"
      },
      "primary_account_identifier": null
    }
  },
  "cardholder": "ich_1Ccy6F2eZvKYlo2ClnIm9bs4",
  "created": 1540586461,
  "currency": "usd",
  "livemode": false,
  "merchant_amount": 0,
  "merchant_currency": "usd",
  "merchant_data": {
    "category": "taxicabs_limousines",
    "category_code": "4121",
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