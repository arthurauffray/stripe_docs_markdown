# The Transaction object

## Attributes

- `id` (string)
  Unique identifier for the object.

- `object` (string)
  String representing the object’s type. Objects of the same type share the same value.

- `amount` (integer)
  The transaction amount, which will be reflected in your balance. This amount is in your currency and in the [smallest currency unit](https://docs.stripe.com/docs/currencies.md#zero-decimal).

- `amount_details` (object, nullable)
  Detailed breakdown of amount components. These amounts are denominated in `currency` and in the [smallest currency unit](https://docs.stripe.com/docs/currencies.md#zero-decimal).

  - `amount_details.atm_fee` (integer, nullable)
    The fee charged by the ATM for the cash withdrawal.

  - `amount_details.cashback_amount` (integer, nullable)
    The amount of cash requested by the cardholder.

- `authorization` (string, nullable)
  The `Authorization` object that led to this transaction.

- `balance_transaction` (string, nullable)
  ID of the [balance transaction](https://docs.stripe.com/docs/api/balance_transactions.md) associated with this transaction.

- `card` (string)
  The card used to make this transaction.

- `cardholder` (string, nullable)
  The cardholder to whom this transaction belongs.

- `created` (timestamp)
  Time at which the object was created. Measured in seconds since the Unix epoch.

- `currency` (enum)
  Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

- `dispute` (string, nullable)
  If you’ve disputed the transaction, the ID of the dispute.

- `livemode` (boolean)
  Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.

- `merchant_amount` (integer)
  The amount that the merchant will receive, denominated in `merchant_currency` and in the [smallest currency unit](https://docs.stripe.com/docs/currencies.md#zero-decimal). It will be different from `amount` if the merchant is taking payment in a different currency.

- `merchant_currency` (enum)
  The currency with which the merchant is taking payment.

- `merchant_data` (object)
  Details about the seller (grocery store, e-commerce website, etc.) involved in this transaction.

  - `merchant_data.category` (string)
    A categorization of the seller’s type of business. See our [merchant categories guide](https://docs.stripe.com/docs/issuing/merchant-categories.md) for a list of possible values.

  - `merchant_data.category_code` (string)
    The merchant category code for the seller’s business

  - `merchant_data.city` (string, nullable)
    City where the seller is located

  - `merchant_data.country` (string, nullable)
    Country where the seller is located

  - `merchant_data.name` (string, nullable)
    Name of the seller

  - `merchant_data.network_id` (string)
    Identifier assigned to the seller by the card network. Different card networks may assign different network_id fields to the same merchant.

  - `merchant_data.postal_code` (string, nullable)
    Postal code where the seller is located

  - `merchant_data.state` (string, nullable)
    State where the seller is located

  - `merchant_data.tax_id` (string, nullable)
    The seller’s tax identification number. Currently populated for French merchants only.

  - `merchant_data.terminal_id` (string, nullable)
    An ID assigned by the seller to the location of the sale.

  - `merchant_data.url` (string, nullable)
    URL provided by the merchant on a 3DS request

- `metadata` (object)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

- `network_data` (object, nullable)
  Details about the transaction, such as processing dates, set by the card network.

  - `network_data.authorization_code` (string, nullable)
    A code created by Stripe which is shared with the merchant to validate the authorization. This field will be populated if the authorization message was approved. The code typically starts with the letter “S”, followed by a six-digit number. For example, “S498162”. Please note that the code is not guaranteed to be unique across authorizations.

  - `network_data.processing_date` (string, nullable)
    The date the transaction was processed by the card network. This can be different from the date the seller recorded the transaction depending on when the acquirer submits the transaction to the network.

  - `network_data.transaction_id` (string, nullable)
    Unique identifier for the authorization assigned by the card network used to match subsequent messages, disputes, and transactions.

- `purchase_details` (object, nullable)
  Additional purchase information that is optionally provided by the merchant.

  - `purchase_details.fleet` (object, nullable)
    Fleet-specific information for transactions using Fleet cards.

    - `purchase_details.fleet.cardholder_prompt_data` (object, nullable)
      Answers to prompts presented to cardholder at point of sale.

      - `purchase_details.fleet.cardholder_prompt_data.driver_id` (string, nullable)
        Driver ID.

      - `purchase_details.fleet.cardholder_prompt_data.odometer` (integer, nullable)
        Odometer reading.

      - `purchase_details.fleet.cardholder_prompt_data.unspecified_id` (string, nullable)
        An alphanumeric ID. This field is used when a vehicle ID, driver ID, or generic ID is entered by the cardholder, but the merchant or card network did not specify the prompt type.

      - `purchase_details.fleet.cardholder_prompt_data.user_id` (string, nullable)
        User ID.

      - `purchase_details.fleet.cardholder_prompt_data.vehicle_number` (string, nullable)
        Vehicle number.

    - `purchase_details.fleet.purchase_type` (string, nullable)
      The type of purchase. One of `fuel_purchase`, `non_fuel_purchase`, or `fuel_and_non_fuel_purchase`.

    - `purchase_details.fleet.reported_breakdown` (object, nullable)
      More information about the total amount. This information is not guaranteed to be accurate as some merchants may provide unreliable data.

      - `purchase_details.fleet.reported_breakdown.fuel` (object, nullable)
        Breakdown of fuel portion of the purchase.

        - `purchase_details.fleet.reported_breakdown.fuel.gross_amount_decimal` (decimal string, nullable)
          Gross fuel amount that should equal Fuel Volume multipled by Fuel Unit Cost, inclusive of taxes.

      - `purchase_details.fleet.reported_breakdown.non_fuel` (object, nullable)
        Breakdown of non-fuel portion of the purchase.

        - `purchase_details.fleet.reported_breakdown.non_fuel.gross_amount_decimal` (decimal string, nullable)
          Gross non-fuel amount that should equal the sum of the line items, inclusive of taxes.

      - `purchase_details.fleet.reported_breakdown.tax` (object, nullable)
        Information about tax included in this transaction.

        - `purchase_details.fleet.reported_breakdown.tax.local_amount_decimal` (decimal string, nullable)
          Amount of state or provincial Sales Tax included in the transaction amount. Null if not reported by merchant or not subject to tax.

        - `purchase_details.fleet.reported_breakdown.tax.national_amount_decimal` (decimal string, nullable)
          Amount of national Sales Tax or VAT included in the transaction amount. Null if not reported by merchant or not subject to tax.

    - `purchase_details.fleet.service_type` (string, nullable)
      The type of fuel service. One of `non_fuel_transaction`, `full_service`, or `self_service`.

  - `purchase_details.flight` (object, nullable)
    Information about the flight that was purchased with this transaction.

    - `purchase_details.flight.departure_at` (integer, nullable)
      The time that the flight departed.

    - `purchase_details.flight.passenger_name` (string, nullable)
      The name of the passenger.

    - `purchase_details.flight.refundable` (boolean, nullable)
      Whether the ticket is refundable.

    - `purchase_details.flight.segments` (array of objects, nullable)
      The legs of the trip.

      - `purchase_details.flight.segments.arrival_airport_code` (string, nullable)
        The three-letter IATA airport code of the flight’s destination.

      - `purchase_details.flight.segments.carrier` (string, nullable)
        The airline carrier code.

      - `purchase_details.flight.segments.departure_airport_code` (string, nullable)
        The three-letter IATA airport code that the flight departed from.

      - `purchase_details.flight.segments.flight_number` (string, nullable)
        The flight number.

      - `purchase_details.flight.segments.service_class` (string, nullable)
        The flight’s service class.

      - `purchase_details.flight.segments.stopover_allowed` (boolean, nullable)
        Whether a stopover is allowed on this flight.

    - `purchase_details.flight.travel_agency` (string, nullable)
      The travel agency that issued the ticket.

  - `purchase_details.fuel` (object, nullable)
    Information about fuel that was purchased with this transaction.

    - `purchase_details.fuel.industry_product_code` (string, nullable)
      [Conexxus Payment System Product Code](https://www.conexxus.org/conexxus-payment-system-product-codes) identifying the primary fuel product purchased.

    - `purchase_details.fuel.quantity_decimal` (decimal string, nullable)
      The quantity of `unit`s of fuel that was dispensed, represented as a decimal string with at most 12 decimal places.

    - `purchase_details.fuel.type` (string)
      The type of fuel that was purchased. One of `diesel`, `unleaded_plus`, `unleaded_regular`, `unleaded_super`, or `other`.

    - `purchase_details.fuel.unit` (string)
      The units for `quantity_decimal`. One of `charging_minute`, `imperial_gallon`, `kilogram`, `kilowatt_hour`, `liter`, `pound`, `us_gallon`, or `other`.

    - `purchase_details.fuel.unit_cost_decimal` (decimal string)
      The cost in cents per each unit of fuel, represented as a decimal string with at most 12 decimal places.

  - `purchase_details.lodging` (object, nullable)
    Information about lodging that was purchased with this transaction.

    - `purchase_details.lodging.check_in_at` (integer, nullable)
      The time of checking into the lodging.

    - `purchase_details.lodging.nights` (integer, nullable)
      The number of nights stayed at the lodging.

  - `purchase_details.receipt` (array of objects, nullable)
    The line items in the purchase.

    - `purchase_details.receipt.description` (string, nullable)
      The description of the item. The maximum length of this field is 26 characters.

    - `purchase_details.receipt.quantity` (float, nullable)
      The quantity of the item.

    - `purchase_details.receipt.total` (integer, nullable)
      The total for this line item in cents.

    - `purchase_details.receipt.unit_cost` (integer, nullable)
      The unit cost of the item in cents.

  - `purchase_details.reference` (string, nullable)
    A merchant-specific order number.

- `token` (string, nullable)
  [Token](https://docs.stripe.com/docs/api/issuing/tokens/object.md) object used for this transaction. If a network token was not used for this transaction, this field will be null.

- `type` (enum)
  The nature of the transaction.
Possible enum values:
  - `capture`
    Funds were captured by the acquirer. `amount` will be negative because funds are moving out of your balance. Not all captures will be linked to an authorization, as acquirers [can force capture in some cases](https://stripe.com/docs/issuing/purchases/transactions).

  - `refund`
    An acquirer initiated a refund. This transaction might not be linked to an original capture, for example credits are original transactions. `amount` will be positive for refunds and negative for refund reversals (very rare).

- `wallet` (enum, nullable)
  The digital wallet used for this transaction. One of `apple_pay`, `google_pay`, or `samsung_pay`.

### The Transaction object

```json
{
  "id": "ipi_1MzFN1K8F4fqH0lBmFq8CjbU",
  "object": "issuing.transaction",
  "amount": -100,
  "amount_details": {
    "atm_fee": null
  },
  "authorization": "iauth_1MzFMzK8F4fqH0lBc9VdaZUp",
  "balance_transaction": "txn_1MzFN1K8F4fqH0lBQPtqUmJN",
  "card": "ic_1MzFMxK8F4fqH0lBjIUITRYi",
  "cardholder": "ich_1MzFMxK8F4fqH0lBXnFW0ROG",
  "created": 1682065867,
  "currency": "usd",
  "dispute": null,
  "livemode": false,
  "merchant_amount": -100,
  "merchant_currency": "usd",
  "merchant_data": {
    "category": "computer_software_stores",
    "category_code": "5734",
    "city": "SAN FRANCISCO",
    "country": "US",
    "name": "WWWW.BROWSEBUG.BIZ",
    "network_id": "1234567890",
    "postal_code": "94103",
    "state": "CA"
  },
  "metadata": {},
  "type": "capture",
  "wallet": null
}
```