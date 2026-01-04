# Create a test-mode force capture

Allows the user to capture an arbitrary amount, also known as a forced capture.

## Returns

A Transaction object

## Parameters

- `amount` (integer, required)
  The total amount to attempt to capture. This amount is in the provided currency, or defaults to the cards currency, and in the [smallest currency unit](https://docs.stripe.com/docs/currencies.md#zero-decimal).

- `card` (string, required)
  Card associated with this transaction.

- `currency` (enum, optional)
  The currency of the capture. If not provided, defaults to the currency of the card. Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

- `merchant_data` (object, optional)
  Details about the seller (grocery store, e-commerce website, etc.) where the card authorization happened.

  - `merchant_data.category` (string, optional)
    A categorization of the seller’s type of business. See our [merchant categories guide](https://docs.stripe.com/docs/issuing/merchant-categories.md) for a list of possible values.

  - `merchant_data.city` (string, optional)
    City where the seller is located

  - `merchant_data.country` (string, optional)
    Country where the seller is located

  - `merchant_data.name` (string, optional)
    Name of the seller

  - `merchant_data.network_id` (string, optional)
    Identifier assigned to the seller by the card network. Different card networks may assign different network_id fields to the same merchant.

  - `merchant_data.postal_code` (string, optional)
    Postal code where the seller is located

  - `merchant_data.state` (string, optional)
    State where the seller is located

  - `merchant_data.terminal_id` (string, optional)
    An ID assigned by the seller to the location of the sale.

  - `merchant_data.url` (string, optional)
    URL provided by the merchant on a 3DS request

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
curl https://api.stripe.com/v1/test_helpers/issuing/transactions/create_force_capture \
  -u "<<YOUR_SECRET_KEY>>" \
  -d amount=1000 \
  -d card=ic_1Gswa82eZvKYlo2CP2jveFil
```

```cli
stripe test_helpers issuing transactions create_force_capture  \
  --amount=1000 \
  --card=ic_1Gswa82eZvKYlo2CP2jveFil
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

transaction = client.v1.test_helpers.issuing.transactions.create_force_capture({
  amount: 1000,
  card: 'ic_1Gswa82eZvKYlo2CP2jveFil',
})
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

transaction = client.v1.test_helpers.issuing.transactions.create_force_capture({
  "amount": 1000,
  "card": "ic_1Gswa82eZvKYlo2CP2jveFil",
})
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$transaction = $stripe->testHelpers->issuing->transactions->createForceCapture([
  'amount' => 1000,
  'card' => 'ic_1Gswa82eZvKYlo2CP2jveFil',
]);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

TransactionCreateForceCaptureParams params =
  TransactionCreateForceCaptureParams.builder()
    .setAmount(1000L)
    .setCard("ic_1Gswa82eZvKYlo2CP2jveFil")
    .build();

Transaction transaction =
  client.v1().testHelpers().issuing().transactions().createForceCapture(params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const transaction = await stripe
  .testHelpers
  .issuing
  .transactions
  .createForceCapture({
  amount: 1000,
  card: 'ic_1Gswa82eZvKYlo2CP2jveFil',
});
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.TestHelpersIssuingTransactionCreateForceCaptureParams{
  Amount: stripe.Int64(1000),
  Card: stripe.String("ic_1Gswa82eZvKYlo2CP2jveFil"),
}
result, err := sc.V1TestHelpersIssuingTransactions.CreateForceCapture(
  context.TODO(), params)
```

```dotnet
var options = new Stripe.TestHelpers.Issuing.TransactionCreateForceCaptureOptions
{
    Amount = 1000,
    Card = "ic_1Gswa82eZvKYlo2CP2jveFil",
};
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.TestHelpers.Issuing.Transactions;
Stripe.Issuing.Transaction transaction = service.CreateForceCapture(options);
```

### Response

```json
{
  "id": "ipi_1GswaK2eZvKYlo2Co7wmNJhD",
  "object": "issuing.transaction",
  "amount": -1000,
  "amount_details": {
    "atm_fee": null,
    "cashback_amount": null
  },
  "authorization": "iauth_1GswaJ2eZvKYlo2Ct9mFMJ4S",
  "balance_transaction": "txn_1GswaK2eZvKYlo2CJAFFIuHg",
  "card": "ic_1Gswa82eZvKYlo2CP2jveFil",
  "cardholder": "ich_1Gswa82eZvKYlo2CvobneLSo",
  "created": 1591905672,
  "currency": "usd",
  "dispute": null,
  "livemode": false,
  "merchant_amount": -1000,
  "merchant_currency": "usd",
  "merchant_data": {
    "category": "computer_software_stores",
    "category_code": "5734",
    "city": "SAN FRANCISCO",
    "country": "US",
    "name": "STRIPE.COM",
    "network_id": "1234567890",
    "postal_code": "94103",
    "state": "CA",
    "terminal_id": null
  },
  "metadata": {
    "order_id": "6735"
  },
  "redaction": null,
  "type": "capture",
  "wallet": null
}
```