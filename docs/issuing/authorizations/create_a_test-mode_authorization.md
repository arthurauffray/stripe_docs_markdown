# Create a test-mode authorization

Create a test-mode authorization.

## Returns

An Authorization object

## Parameters

- `card` (string, required)
  Card associated with this authorization.

- `amount` (integer, optional)
  The total amount to attempt to authorize. This amount is in the provided currency, or defaults to the card’s currency, and in the [smallest currency unit](https://docs.stripe.com/docs/currencies.md#zero-decimal).

- `amount_details` (object, optional)
  Detailed breakdown of amount components. These amounts are denominated in `currency` and in the [smallest currency unit](https://docs.stripe.com/docs/currencies.md#zero-decimal).

  - `amount_details.atm_fee` (integer, optional)
    The ATM withdrawal fee.

  - `amount_details.cashback_amount` (integer, optional)
    The amount of cash requested by the cardholder.

- `authorization_method` (enum, optional)
  How the card details were provided. Defaults to online.
Possible enum values:
  - `chip`
    The card was physically present and inserted into a chip-enabled terminal. The transaction is cryptographically secured.

  - `contactless`
    The card was tapped on a contactless-enabled terminal. If a digital wallet copy of the card was used, the `wallet` field will be present.

  - `keyed_in`
    The card number was manually entered into a terminal.

  - `online`
    The card was used in a card-not-present scenario, such as a transaction initiated at an online e-commerce checkout.

  - `swipe`
    The card was physically swiped in a terminal.

- `currency` (enum, optional)
  The currency of the authorization. If not provided, defaults to the currency of the card. Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

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

- `is_amount_controllable` (boolean, optional)
  If set `true`, you may provide [amount](https://docs.stripe.com/docs/api/issuing/authorizations/approve.md#approve_issuing_authorization-amount) to control how much to hold for the authorization.

- `merchant_amount` (integer, optional)
  The total amount to attempt to authorize. This amount is in the provided merchant currency, and in the [smallest currency unit](https://docs.stripe.com/docs/currencies.md#zero-decimal).

- `merchant_currency` (enum, optional)
  The currency of the authorization. If not provided, defaults to the currency of the card. Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

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

- `network_data` (object, optional)
  Details about the authorization, such as identifiers, set by the card network.

  - `network_data.acquiring_institution_id` (string, optional)
    Identifier assigned to the acquirer by the card network.

- `verification_data` (object, optional)
  Verifications that Stripe performed on information that the cardholder provided to the merchant.

  - `verification_data.address_line1_check` (enum, optional)
    Whether the cardholder provided an address first line and if it matched the cardholder’s `billing.address.line1`.
Possible enum values:
    - `match`
      Verification succeeded, values matched.

    - `mismatch`
      Verification failed, values didn’t match.

    - `not_provided`
      Verification was not performed because no value was provided.

  - `verification_data.address_postal_code_check` (enum, optional)
    Whether the cardholder provided a postal code and if it matched the cardholder’s `billing.address.postal_code`.
Possible enum values:
    - `match`
      Verification succeeded, values matched.

    - `mismatch`
      Verification failed, values didn’t match.

    - `not_provided`
      Verification was not performed because no value was provided.

  - `verification_data.authentication_exemption` (object, optional)
    The exemption applied to this authorization.

    - `verification_data.authentication_exemption.claimed_by` (enum, required)
      The entity that requested the exemption, either the acquiring merchant or the Issuing user.
Possible enum values:
      - `acquirer`
        Acquiring merchant.

      - `issuer`
        Issuing user.

    - `verification_data.authentication_exemption.type` (enum, required)
      The specific exemption claimed for this authorization.
Possible enum values:
      - `low_value_transaction`
        Specifies an exemption for some low-value authorizations.

      - `transaction_risk_analysis`
        Specifies an exemption for low-risk authorizations, determined using real-time risk analysis.

      - `unknown`
        Specifies an unknown exemption type.

  - `verification_data.cvc_check` (enum, optional)
    Whether the cardholder provided a CVC and if it matched Stripe’s record.
Possible enum values:
    - `match`
      Verification succeeded, values matched.

    - `mismatch`
      Verification failed, values didn’t match.

    - `not_provided`
      Verification was not performed because no value was provided.

  - `verification_data.expiry_check` (enum, optional)
    Whether the cardholder provided an expiry date and if it matched Stripe’s record.
Possible enum values:
    - `match`
      Verification succeeded, values matched.

    - `mismatch`
      Verification failed, values didn’t match.

    - `not_provided`
      Verification was not performed because no value was provided.

  - `verification_data.three_d_secure` (object, optional)
    3D Secure details.

    - `verification_data.three_d_secure.result` (enum, required)
      The outcome of the 3D Secure authentication request.
Possible enum values:
      - `attempt_acknowledged`
        The merchant attempted to authenticate the authorization, but the cardholder is not enrolled or was unable to reach Stripe.

      - `authenticated`
        Authentication successful.

      - `failed`
        Authentication failed.

      - `required`
        The authorization was declined because regulatory requirements mandated an authentication for this transaction but it wasn’t submitted correctly by the merchant, and they didn’t claim an applicable exemption. Check out our [3DS documentation](https://stripe.com/docs/issuing/3d-secure#prevent-fraud) if you want to learn more.

- `wallet` (enum, optional)
  The digital wallet used for this transaction. One of `apple_pay`, `google_pay`, or `samsung_pay`. Will populate as `null` when no digital wallet was utilized.

```curl
curl https://api.stripe.com/v1/test_helpers/issuing/authorizations \
  -u "<<YOUR_SECRET_KEY>>" \
  -d amount=1000 \
  -d card=ic_1Nsse72eZvKYlo2CWBGm2WQ5
```

```cli
stripe test_helpers issuing authorizations create  \
  --amount=1000 \
  --card=ic_1Nsse72eZvKYlo2CWBGm2WQ5
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

authorization = client.v1.test_helpers.issuing.authorizations.create({
  amount: 1000,
  card: 'ic_1Nsse72eZvKYlo2CWBGm2WQ5',
})
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

authorization = client.v1.test_helpers.issuing.authorizations.create({
  "amount": 1000,
  "card": "ic_1Nsse72eZvKYlo2CWBGm2WQ5",
})
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$authorization = $stripe->testHelpers->issuing->authorizations->create([
  'amount' => 1000,
  'card' => 'ic_1Nsse72eZvKYlo2CWBGm2WQ5',
]);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

AuthorizationCreateParams params =
  AuthorizationCreateParams.builder()
    .setAmount(1000L)
    .setCard("ic_1Nsse72eZvKYlo2CWBGm2WQ5")
    .build();

Authorization authorization =
  client.v1().testHelpers().issuing().authorizations().create(params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const authorization = await stripe.testHelpers.issuing.authorizations.create({
  amount: 1000,
  card: 'ic_1Nsse72eZvKYlo2CWBGm2WQ5',
});
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.TestHelpersIssuingAuthorizationCreateParams{
  Amount: stripe.Int64(1000),
  Card: stripe.String("ic_1Nsse72eZvKYlo2CWBGm2WQ5"),
}
result, err := sc.V1TestHelpersIssuingAuthorizations.Create(context.TODO(), params)
```

```dotnet
var options = new Stripe.TestHelpers.Issuing.AuthorizationCreateOptions
{
    Amount = 1000,
    Card = "ic_1Nsse72eZvKYlo2CWBGm2WQ5",
};
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.TestHelpers.Issuing.Authorizations;
Stripe.Issuing.Authorization authorization = service.Create(options);
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
  "authorization_method": "keyed_in",
  "balance_transactions": [],
  "card": "ic_1Nsse72eZvKYlo2CWBGm2WQ5",
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