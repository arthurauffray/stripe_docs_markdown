# The Tax Setting object

## Attributes

- `object` (string)
  String representing the object’s type. Objects of the same type share the same value.

- `defaults` (object)
  Default configuration to be used on Stripe Tax calculations.

  - `defaults.provider` (enum)
    The tax calculation provider this account uses. Defaults to `stripe` when not using a [third-party provider](https://docs.stripe.com/tax/third-party-apps.md).

  - `defaults.tax_behavior` (enum, nullable)
    Default [tax behavior](https://stripe.com/docs/tax/products-prices-tax-categories-tax-behavior#tax-behavior) used to specify whether the price is considered inclusive of taxes or exclusive of taxes. If the item’s price has a tax behavior set, it will take precedence over the default tax behavior.
Possible enum values:
    - `exclusive`
      Taxes are calculated on top of the line item amount.

    - `inclusive`
      Taxes are included in the line item amount.

    - `inferred_by_currency`
      Stripe will use the price currency to define whether the tax should be added on top of the price (excluded) or included in the price.

  - `defaults.tax_code` (string, nullable)
    Default [tax code](https://stripe.com/docs/tax/tax-categories) used to classify your products and prices.

- `head_office` (object, nullable)
  The place where your business is located.

  - `head_office.address` (object)
    The location of the business for tax purposes.

    - `head_office.address.city` (string, nullable)
      City, district, suburb, town, or village.

    - `head_office.address.country` (string, nullable)
      Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

    - `head_office.address.line1` (string, nullable)
      Address line 1, such as the street, PO Box, or company name.

    - `head_office.address.line2` (string, nullable)
      Address line 2, such as the apartment, suite, unit, or building.

    - `head_office.address.postal_code` (string, nullable)
      ZIP or postal code.

    - `head_office.address.state` (string, nullable)
      State, county, province, or region ([ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2)).

- `livemode` (boolean)
  Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.

- `status` (enum)
  The status of the Tax `Settings`.
Possible enum values:
  - `active`
    Tax `Settings` have the required information and ready for tax calculations.

  - `pending`
    Tax `Settings` missing some required information and not ready for tax calculations. Check `status_details` field for more.

- `status_details` (object)
  Information about the status.

  - `status_details.active` (object, nullable)
    If status is `active`, this hash contains further details about the Settings.

  - `status_details.pending` (object, nullable)
    If status is `pending`, this hash contains further details about the Settings.

    - `status_details.pending.missing_fields` (array of strings, nullable)
      The list of missing fields that are required to perform calculations. It includes the entry `head_office` when the status is `pending`. It is recommended to set the optional values even if they aren’t listed as required for calculating taxes. Calculations can fail if missing fields aren’t explicitly provided on every call.

### The Tax Setting object

```json
{
  "object": "tax.settings",
  "defaults": {
    "tax_behavior": null,
    "tax_code": "txcd_10000000"
  },
  "head_office": {
    "address": {
      "city": null,
      "country": "US",
      "line1": null,
      "line2": null,
      "postal_code": null,
      "state": "CA"
    }
  },
  "livemode": false,
  "status": "active",
  "status_details": {
    "active": {}
  }
}
```