# Create a card

When you create a new debit card, you must specify a [connected account](https://docs.stripe.com/api/external_account_cards/create.md#accounts) to create it on. You can only specify connected accounts where [account.controller.requirement_collection](https://docs.stripe.com/api/accounts/object.md#account_object-controller-requirement_collection) is `application` (includes [Custom accounts](https://docs.stripe.com/connect/custom-accounts.md)).

If the account has no default destination card, then the new card will become the default. However, if the owner already has a default then it will not change. To change the default, you should set `default_for_currency` to `true`.

## Returns

Returns the card object

## Parameters

- `external_account` (object | string, required)
  A token, like the ones returned by [Stripe.js](https://docs.stripe.com/docs/js.md) or a dictionary containing a user’s card details (with the options shown below). Stripe will automatically validate the card.

  - `external_account.exp_month` (integer, required)
    Two-digit number representing the card’s expiration month.

  - `external_account.exp_year` (integer, required)
    Two- or -four-digit number representing the card’s expiration year.

  - `external_account.number` (string, required)
    The card number, as a string without any separators.

  - `external_account.object` (string, required)
    The type of payment source. It should be `card`.

  - `external_account.address_city` (string, optional)
    City / District / Suburb / Town / Village.

  - `external_account.address_country` (string, optional)
    Billing address country, if provided.

  - `external_account.address_line1` (string, optional)
    Address line 1 (Street address / PO Box / Company name).

  - `external_account.address_line2` (string, optional)
    Address line 2 (Apartment / Suite / Unit / Building).

  - `external_account.address_state` (string, optional)
    State / County / Province / Region.

  - `external_account.address_zip` (string, optional)
    ZIP or postal code.

  - `external_account.currency` (string, optional)
    Required when adding a card to an account (not applicable to customers or recipients). The card (which must be a debit card) can be used as a transfer destination for funds in this currency.

  - `external_account.cvc` (string, optional)
    Card security code. Highly recommended to always include this value, but it’s required only for accounts based in European countries.

  - `external_account.default_for_currency` (boolean, optional)
    Applicable only on accounts (not customers or recipients). If you set this to `true` (or if this is the first external account being added in this currency), this card will become the default external account for its currency.

  - `external_account.metadata` (object, optional)
    A set of key-value pairs that you can attach to a card object. This can be useful for storing additional information about the card in a structured format.

  - `external_account.name` (string, optional)
    Cardholder’s full name.

- `default_for_currency` (boolean, optional)
  When set to true, or if this is the first external account added in this currency, this account becomes the default external account for its currency.

- `metadata` (object, optional)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.

```curl
curl https://api.stripe.com/v1/accounts/acct_1032D82eZvKYlo2C/external_accounts \
  -u "<<YOUR_SECRET_KEY>>" \
  -d external_account=tok_visa_debit
```

```cli
stripe external_accounts create acct_1032D82eZvKYlo2C \
  --external-account=tok_visa_debit
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

result = client.v1.accounts.external_accounts.create(
  'acct_1032D82eZvKYlo2C',
  {external_account: 'tok_visa_debit'},
)
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

external_account = client.v1.accounts.external_accounts.create(
  "acct_1032D82eZvKYlo2C",
  {"external_account": "tok_visa_debit"},
)
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$externalAccount = $stripe->accounts->createExternalAccount(
  'acct_1032D82eZvKYlo2C',
  ['external_account' => 'tok_visa_debit']
);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

AccountExternalAccountCreateParams params =
  AccountExternalAccountCreateParams.builder()
    .setExternalAccount("tok_visa_debit")
    .build();

ExternalAccount externalAccount =
  client.v1().accounts().externalAccounts().create("acct_1032D82eZvKYlo2C", params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const externalAccount = await stripe.accounts.createExternalAccount(
  'acct_1032D82eZvKYlo2C',
  {
    external_account: 'tok_visa_debit',
  }
);
```

```go
stripe.Key = "<<YOUR_SECRET_KEY>>"

params := &stripe.BankAccountParams{
	Account: stripe.String("acct_1032D82eZvKYlo2C"),
	Token: stripe.String("tok_visa_debit"),
}
result, _ := bankaccount.New(params)
```

```dotnet
var options = new AccountExternalAccountCreateOptions
{
    ExternalAccount = "tok_visa_debit",
};
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Accounts.ExternalAccounts;
IExternalAccount iExternalAccount = service.Create("acct_1032D82eZvKYlo2C", options);
```

### Response

```json
{
  "id": "card_1NAiaG2eZvKYlo2CDXvcMb6m",
  "object": "card",
  "account": "acct_1032D82eZvKYlo2C",
  "address_city": null,
  "address_country": null,
  "address_line1": null,
  "address_line1_check": null,
  "address_line2": null,
  "address_state": null,
  "address_zip": null,
  "address_zip_check": null,
  "brand": "Visa",
  "country": "US",
  "cvc_check": "pass",
  "dynamic_last4": null,
  "exp_month": 8,
  "exp_year": 2024,
  "fingerprint": "Xt5EWLLDS7FJjR1c",
  "funding": "credit",
  "last4": "4242",
  "metadata": {},
  "name": null,
  "redaction": null,
  "tokenization_method": null,
  "wallet": null
}
```