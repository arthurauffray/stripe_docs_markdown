# Create or retrieve funding instructions for a customer cash balance

Retrieve funding instructions for a customer cash balance. If funding instructions do not yet exist for the customer, new funding instructions will be created. If funding instructions have already been created for a given customer, the same funding instructions will be retrieved. In other words, we will return the same funding instructions each time.

## Returns

Returns funding instructions for a customer cash balance

## Parameters

- `bank_transfer` (object, required)
  Additional parameters for `bank_transfer` funding types

  - `bank_transfer.type` (enum, required)
    The type of the `bank_transfer`
Possible enum values:
    - `eu_bank_transfer`
      A bank transfer to a `eu_bank_transfer`

    - `gb_bank_transfer`
      A bank transfer to a `gb_bank_transfer`

    - `jp_bank_transfer`
      A bank transfer to a `jp_bank_transfer`

    - `mx_bank_transfer`
      A bank transfer to a `mx_bank_transfer`

    - `us_bank_transfer`
      A bank transfer to a `us_bank_transfer`

  - `bank_transfer.eu_bank_transfer` (object, optional)
    Configuration for eu_bank_transfer funding type.

    - `bank_transfer.eu_bank_transfer.country` (string, required)
      The desired country code of the bank account information. Permitted values include: `BE`, `DE`, `ES`, `FR`, `IE`, or `NL`.

  - `bank_transfer.requested_address_types` (array of enums, optional)
    List of address types that should be returned in the financial_addresses response. If not specified, all valid types will be returned.

    Permitted values include: `sort_code`, `zengin`, `iban`, or `spei`.
Possible enum values:
    - `iban`
      An IBAN financial address

    - `sort_code`
      A SortCode financial address

    - `spei`
      A Spei financial address

    - `zengin`
      A Zengin financial address

- `currency` (enum, required)
  Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

- `funding_type` (enum, required)
  The `funding_type` to get the instructions for.
Possible enum values:
  - `bank_transfer`
    Use a bank_transfer hash to define the bank transfer type

```curl
curl https://api.stripe.com/v1/customers/cus_9s6XKzkNRiz8i3/funding_instructions \
  -u "<<YOUR_SECRET_KEY>>" \
  -d funding_type=bank_transfer \
  -d currency=eur \
  -d "bank_transfer[type]"=eu_bank_transfer \
  -d "bank_transfer[eu_bank_transfer][country]"=DE
```

```cli
stripe customers create_funding_instructions cus_9s6XKzkNRiz8i3 \
  --funding-type=bank_transfer \
  --currency=eur \
  -d "bank_transfer[type]"=eu_bank_transfer \
  -d "bank_transfer[eu_bank_transfer][country]"=DE
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

funding_instructions = client.v1.customers.funding_instructions.create(
  'cus_9s6XKzkNRiz8i3',
  {
    funding_type: 'bank_transfer',
    currency: 'eur',
    bank_transfer: {
      type: 'eu_bank_transfer',
      eu_bank_transfer: {country: 'DE'},
    },
  },
)
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

funding_instructions = client.v1.customers.funding_instructions.create(
  "cus_9s6XKzkNRiz8i3",
  {
    "funding_type": "bank_transfer",
    "currency": "eur",
    "bank_transfer": {
      "type": "eu_bank_transfer",
      "eu_bank_transfer": {"country": "DE"},
    },
  },
)
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$fundingInstructions = $stripe->customers->createFundingInstructions(
  'cus_9s6XKzkNRiz8i3',
  [
    'funding_type' => 'bank_transfer',
    'currency' => 'eur',
    'bank_transfer' => [
      'type' => 'eu_bank_transfer',
      'eu_bank_transfer' => ['country' => 'DE'],
    ],
  ]
);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

CustomerFundingInstructionsCreateParams params =
  CustomerFundingInstructionsCreateParams.builder()
    .setFundingType(
      CustomerFundingInstructionsCreateParams.FundingType.BANK_TRANSFER
    )
    .setCurrency("eur")
    .setBankTransfer(
      CustomerFundingInstructionsCreateParams.BankTransfer.builder()
        .setType(
          CustomerFundingInstructionsCreateParams.BankTransfer.Type.EU_BANK_TRANSFER
        )
        .setEuBankTransfer(
          CustomerFundingInstructionsCreateParams.BankTransfer.EuBankTransfer.builder()
            .setCountry("DE")
            .build()
        )
        .build()
    )
    .build();

FundingInstructions fundingInstructions =
  client.v1().customers().fundingInstructions().create("cus_9s6XKzkNRiz8i3", params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const fundingInstructions = await stripe.customers.createFundingInstructions(
  'cus_9s6XKzkNRiz8i3',
  {
    funding_type: 'bank_transfer',
    currency: 'eur',
    bank_transfer: {
      type: 'eu_bank_transfer',
      eu_bank_transfer: {
        country: 'DE',
      },
    },
  }
);
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.CustomerCreateFundingInstructionsParams{
  FundingType: stripe.String("bank_transfer"),
  Currency: stripe.String(stripe.CurrencyEUR),
  BankTransfer: &stripe.CustomerCreateFundingInstructionsBankTransferParams{
    Type: stripe.String("eu_bank_transfer"),
    EUBankTransfer: &stripe.CustomerCreateFundingInstructionsBankTransferEUBankTransferParams{
      Country: stripe.String("DE"),
    },
  },
}
result, err := sc.V1Customers.CreateFundingInstructions(
  context.TODO(), "cus_9s6XKzkNRiz8i3", params)
```

```dotnet
var options = new CustomerFundingInstructionsCreateOptions
{
    FundingType = "bank_transfer",
    Currency = "eur",
    BankTransfer = new CustomerFundingInstructionsBankTransferOptions
    {
        Type = "eu_bank_transfer",
        EuBankTransfer = new CustomerFundingInstructionsBankTransferEuBankTransferOptions
        {
            Country = "DE",
        },
    },
};
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Customers.FundingInstructions;
FundingInstructions fundingInstructions = service.Create(
    "cus_9s6XKzkNRiz8i3",
    options);
```

### Response

```json
{
  "object": "funding_instructions",
  "bank_transfer": {
    "country": "DE",
    "financial_addresses": [
      {
        "iban": {
          "account_holder_address": {
            "city": "Dublin",
            "country": "IE",
            "line1": "Some address",
            "line2": null,
            "postal_code": "D01H104",
            "state": "Dublin 1"
          },
          "account_holder_name": "Merchant name",
          "bank_address": {
            "city": "Dublin",
            "country": "IE",
            "line1": "1 North Wall Quay",
            "line2": null,
            "postal_code": "D01 T8Y1",
            "state": "Dublin"
          },
          "bic": "SOGEDEFFXXX",
          "country": "DE",
          "iban": "DE006847740991234567890"
        },
        "supported_networks": [
          "sepa",
          "swift"
        ],
        "type": "iban"
      }
    ],
    "type": "eu_bank_transfer"
  },
  "currency": "eur",
  "funding_type": "bank_transfer",
  "livemode": false
}
```