# Create a Tax Calculation

Calculates tax based on the input and returns a Tax `Calculation` object.

## Returns

A Tax `Calculation` object containing the first 100 input `line_items` if the calculation succeeds. Otherwise, an error (for example, indicating that the customer address was invalid).

## Parameters

- `currency` (enum, required)
  Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

- `line_items` (array of objects, required)
  A list of items the customer is purchasing.

  - `line_items.amount` (integer, required)
    A positive integer representing the line item’s total price in the [smallest currency unit](https://docs.stripe.com/docs/currencies.md#zero-decimal). If `tax_behavior=inclusive`, then this amount includes taxes. Otherwise, taxes are calculated on top of this amount.

  - `line_items.metadata` (object, optional)
    Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

  - `line_items.product` (string, optional)
    If provided, the product’s `tax_code` will be used as the line item’s `tax_code`.

  - `line_items.quantity` (integer, optional)
    The number of units of the item being purchased. Used to calculate the per-unit price from the total `amount` for the line. For example, if `amount=100` and `quantity=4`, the calculated unit price is 25.

  - `line_items.reference` (string, required)
    A custom identifier for this line item, which must be unique across the line items in the calculation. The reference helps identify each line item in exported [tax reports](https://docs.stripe.com/docs/tax/reports.md).

    The maximum length is 500 characters.

  - `line_items.tax_behavior` (enum, optional)
    Specifies whether the `amount` includes taxes. Defaults to `exclusive`.
Possible enum values:
    - `exclusive`
      Taxes are calculated on top of the line item amount (default).

    - `inclusive`
      Taxes are included in the line item amount.

  - `line_items.tax_code` (string, optional)
    A [tax code](https://docs.stripe.com/docs/tax/tax-categories.md) ID to use for this line item. If not provided, we will use the tax code from the provided `product` param. If neither `tax_code` nor `product` is provided, we will use the default tax code from your Tax Settings.

- `customer` (string, required unless customer_details provided)
  The ID of an existing customer to use for this calculation. If provided, the customer’s address and tax IDs are copied to `customer_details`.

- `customer_details` (object, required unless customer provided)
  Details about the customer, including address and tax IDs.

  - `customer_details.address` (object, required unless ip_address provided)
    The customer’s postal address (for example, home or business location).

    - `customer_details.address.country` (string, required)
      Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

    - `customer_details.address.city` (string, optional)
      City, district, suburb, town, or village.

    - `customer_details.address.line1` (string, optional)
      Address line 1, such as the street, PO Box, or company name.

    - `customer_details.address.line2` (string, optional)
      Address line 2, such as the apartment, suite, unit, or building.

    - `customer_details.address.postal_code` (string, required for US addresses)
      ZIP or postal code.

    - `customer_details.address.state` (string, optional)
      State, county, province, or region. We recommend sending [ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2) subdivision code value when possible.

  - `customer_details.address_source` (enum, Required when using address)
    The type of customer address provided.
Possible enum values:
    - `billing`
      Denotes the address as billing address.

    - `shipping`
      Denotes the address as shipping address.

  - `customer_details.ip_address` (string, required unless address provided)
    The customer’s IP address (IPv4 or IPv6).

  - `customer_details.tax_ids` (array of objects, optional)
    The customer’s tax IDs. Stripe Tax might consider a transaction with applicable tax IDs to be B2B, which might affect the tax calculation result. Stripe Tax doesn’t validate tax IDs for correctness.

    - `customer_details.tax_ids.type` (string, required)
      Type of the tax ID, one of `ad_nrt`, `ae_trn`, `al_tin`, `am_tin`, `ao_tin`, `ar_cuit`, `au_abn`, `au_arn`, `aw_tin`, `az_tin`, `ba_tin`, `bb_tin`, `bd_bin`, `bf_ifu`, `bg_uic`, `bh_vat`, `bj_ifu`, `bo_tin`, `br_cnpj`, `br_cpf`, `bs_tin`, `by_tin`, `ca_bn`, `ca_gst_hst`, `ca_pst_bc`, `ca_pst_mb`, `ca_pst_sk`, `ca_qst`, `cd_nif`, `ch_uid`, `ch_vat`, `cl_tin`, `cm_niu`, `cn_tin`, `co_nit`, `cr_tin`, `cv_nif`, `de_stn`, `do_rcn`, `ec_ruc`, `eg_tin`, `es_cif`, `et_tin`, `eu_oss_vat`, `eu_vat`, `gb_vat`, `ge_vat`, `gn_nif`, `hk_br`, `hr_oib`, `hu_tin`, `id_npwp`, `il_vat`, `in_gst`, `is_vat`, `jp_cn`, `jp_rn`, `jp_trn`, `ke_pin`, `kg_tin`, `kh_tin`, `kr_brn`, `kz_bin`, `la_tin`, `li_uid`, `li_vat`, `ma_vat`, `md_vat`, `me_pib`, `mk_vat`, `mr_nif`, `mx_rfc`, `my_frp`, `my_itn`, `my_sst`, `ng_tin`, `no_vat`, `no_voec`, `np_pan`, `nz_gst`, `om_vat`, `pe_ruc`, `ph_tin`, `ro_tin`, `rs_pib`, `ru_inn`, `ru_kpp`, `sa_vat`, `sg_gst`, `sg_uen`, `si_tin`, `sn_ninea`, `sr_fin`, `sv_nit`, `th_vat`, `tj_tin`, `tr_tin`, `tw_vat`, `tz_vat`, `ua_vat`, `ug_tin`, `us_ein`, `uy_ruc`, `uz_tin`, `uz_vat`, `ve_rif`, `vn_tin`, `za_vat`, `zm_tin`, or `zw_tin`

    - `customer_details.tax_ids.value` (string, required)
      Value of the tax ID.

  - `customer_details.taxability_override` (enum, optional)
    Overrides the tax calculation result to allow you to not collect tax from your customer. Use this if you’ve manually checked your customer’s tax exemptions. Prefer providing the customer’s `tax_ids` where possible, which automatically determines whether `reverse_charge` applies.
Possible enum values:
    - `customer_exempt`
      The customer is exempt of tax.

    - `none`
      No taxability override (default).

    - `reverse_charge`
      The customer is entitled to reverse charge tax treatment.

- `ship_from_details` (object, optional)
  Details about the address from which the goods are being shipped.

  - `ship_from_details.address` (object, required)
    The address from which the goods are being shipped from.

    - `ship_from_details.address.country` (string, required)
      Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

    - `ship_from_details.address.city` (string, optional)
      City, district, suburb, town, or village.

    - `ship_from_details.address.line1` (string, optional)
      Address line 1, such as the street, PO Box, or company name.

    - `ship_from_details.address.line2` (string, optional)
      Address line 2, such as the apartment, suite, unit, or building.

    - `ship_from_details.address.postal_code` (string, required for US addresses)
      ZIP or postal code.

    - `ship_from_details.address.state` (string, optional)
      State/province as an [ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2) subdivision code, without country prefix, such as “NY” or “TX”.

- `shipping_cost` (object, optional)
  Shipping cost details to be used for the calculation.

  - `shipping_cost.amount` (integer, required unless shipping_rate provided)
    A positive integer in the [smallest currency unit](https://docs.stripe.com/docs/currencies.md#zero-decimal) representing the shipping charge. If `tax_behavior=inclusive`, then this amount includes taxes. Otherwise, taxes are calculated on top of this amount.

  - `shipping_cost.shipping_rate` (string, required unless amount provided)
    If provided, the [shipping rate](https://docs.stripe.com/docs/api/shipping_rates/object.md)’s `amount`, `tax_code` and `tax_behavior` are used. If you provide a shipping rate, then you cannot pass the `amount`, `tax_code`, or `tax_behavior` parameters.

  - `shipping_cost.tax_behavior` (enum, optional)
    Specifies whether the `amount` includes taxes. If `tax_behavior=inclusive`, then the amount includes taxes. Defaults to `exclusive`.
Possible enum values:
    - `exclusive`
      Taxes are calculated on top of the line item amount (default).

    - `inclusive`
      Taxes are included in the line item amount.

  - `shipping_cost.tax_code` (string, optional)
    The [tax code](https://docs.stripe.com/docs/tax/tax-categories.md) used to calculate tax on shipping. If not provided, the default shipping tax code from your [Tax Settings](https://dashboard.stripe.com/settings/tax) is used.

- `tax_date` (integer, optional)
  Timestamp of date at which the tax rules and rates in effect applies for the calculation. Measured in seconds since the Unix epoch. Can be up to 48 hours in the past, and up to 48 hours in the future.

```curl
curl https://api.stripe.com/v1/tax/calculations \
  -u "<<YOUR_SECRET_KEY>>" \
  -d currency=usd \
  -d "customer_details[address][line1]"="920 5th Ave" \
  -d "customer_details[address][city]"=Seattle \
  -d "customer_details[address][state]"=WA \
  -d "customer_details[address][postal_code]"=98104 \
  -d "customer_details[address][country]"=US \
  -d "customer_details[address_source]"=shipping \
  -d "line_items[0][amount]"=1499 \
  -d "line_items[0][tax_code]"=txcd_10000000 \
  -d "line_items[0][reference]"="Music Streaming Coupon" \
  -d "shipping_cost[amount]"=300 \
  -d "expand[0]"=line_items
```

```cli
stripe tax calculations create  \
  --currency=usd \
  -d "customer_details[address][line1]"="920 5th Ave" \
  -d "customer_details[address][city]"=Seattle \
  -d "customer_details[address][state]"=WA \
  -d "customer_details[address][postal_code]"=98104 \
  -d "customer_details[address][country]"=US \
  -d "customer_details[address_source]"=shipping \
  -d "line_items[0][amount]"=1499 \
  -d "line_items[0][tax_code]"=txcd_10000000 \
  -d "line_items[0][reference]"="Music Streaming Coupon" \
  -d "shipping_cost[amount]"=300 \
  -d "expand[0]"=line_items
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

calculation = client.v1.tax.calculations.create({
  currency: 'usd',
  customer_details: {
    address: {
      line1: '920 5th Ave',
      city: 'Seattle',
      state: 'WA',
      postal_code: '98104',
      country: 'US',
    },
    address_source: 'shipping',
  },
  line_items: [
    {
      amount: 1499,
      tax_code: 'txcd_10000000',
      reference: 'Music Streaming Coupon',
    },
  ],
  shipping_cost: {amount: 300},
  expand: ['line_items'],
})
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

calculation = client.v1.tax.calculations.create({
  "currency": "usd",
  "customer_details": {
    "address": {
      "line1": "920 5th Ave",
      "city": "Seattle",
      "state": "WA",
      "postal_code": "98104",
      "country": "US",
    },
    "address_source": "shipping",
  },
  "line_items": [
    {
      "amount": 1499,
      "tax_code": "txcd_10000000",
      "reference": "Music Streaming Coupon",
    },
  ],
  "shipping_cost": {"amount": 300},
  "expand": ["line_items"],
})
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$calculation = $stripe->tax->calculations->create([
  'currency' => 'usd',
  'customer_details' => [
    'address' => [
      'line1' => '920 5th Ave',
      'city' => 'Seattle',
      'state' => 'WA',
      'postal_code' => '98104',
      'country' => 'US',
    ],
    'address_source' => 'shipping',
  ],
  'line_items' => [
    [
      'amount' => 1499,
      'tax_code' => 'txcd_10000000',
      'reference' => 'Music Streaming Coupon',
    ],
  ],
  'shipping_cost' => ['amount' => 300],
  'expand' => ['line_items'],
]);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

CalculationCreateParams params =
  CalculationCreateParams.builder()
    .setCurrency("usd")
    .setCustomerDetails(
      CalculationCreateParams.CustomerDetails.builder()
        .setAddress(
          CalculationCreateParams.CustomerDetails.Address.builder()
            .setLine1("920 5th Ave")
            .setCity("Seattle")
            .setState("WA")
            .setPostalCode("98104")
            .setCountry("US")
            .build()
        )
        .setAddressSource(
          CalculationCreateParams.CustomerDetails.AddressSource.SHIPPING
        )
        .build()
    )
    .addLineItem(
      CalculationCreateParams.LineItem.builder()
        .setAmount(1499L)
        .setTaxCode("txcd_10000000")
        .setReference("Music Streaming Coupon")
        .build()
    )
    .setShippingCost(
      CalculationCreateParams.ShippingCost.builder().setAmount(300L).build()
    )
    .addExpand("line_items")
    .build();

Calculation calculation = client.v1().tax().calculations().create(params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const calculation = await stripe.tax.calculations.create({
  currency: 'usd',
  customer_details: {
    address: {
      line1: '920 5th Ave',
      city: 'Seattle',
      state: 'WA',
      postal_code: '98104',
      country: 'US',
    },
    address_source: 'shipping',
  },
  line_items: [
    {
      amount: 1499,
      tax_code: 'txcd_10000000',
      reference: 'Music Streaming Coupon',
    },
  ],
  shipping_cost: {
    amount: 300,
  },
  expand: ['line_items'],
});
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.TaxCalculationCreateParams{
  Currency: stripe.String(stripe.CurrencyUSD),
  CustomerDetails: &stripe.TaxCalculationCreateCustomerDetailsParams{
    Address: &stripe.AddressParams{
      Line1: stripe.String("920 5th Ave"),
      City: stripe.String("Seattle"),
      State: stripe.String("WA"),
      PostalCode: stripe.String("98104"),
      Country: stripe.String("US"),
    },
    AddressSource: stripe.String(stripe.TaxCalculationCustomerDetailsAddressSourceShipping),
  },
  LineItems: []*stripe.TaxCalculationCreateLineItemParams{
    &stripe.TaxCalculationCreateLineItemParams{
      Amount: stripe.Int64(1499),
      TaxCode: stripe.String("txcd_10000000"),
      Reference: stripe.String("Music Streaming Coupon"),
    },
  },
  ShippingCost: &stripe.TaxCalculationCreateShippingCostParams{
    Amount: stripe.Int64(300),
  },
}
params.AddExpand("line_items")
result, err := sc.V1TaxCalculations.Create(context.TODO(), params)
```

```dotnet
var options = new Stripe.Tax.CalculationCreateOptions
{
    Currency = "usd",
    CustomerDetails = new Stripe.Tax.CalculationCustomerDetailsOptions
    {
        Address = new AddressOptions
        {
            Line1 = "920 5th Ave",
            City = "Seattle",
            State = "WA",
            PostalCode = "98104",
            Country = "US",
        },
        AddressSource = "shipping",
    },
    LineItems = new List<Stripe.Tax.CalculationLineItemOptions>
    {
        new Stripe.Tax.CalculationLineItemOptions
        {
            Amount = 1499,
            TaxCode = "txcd_10000000",
            Reference = "Music Streaming Coupon",
        },
    },
    ShippingCost = new Stripe.Tax.CalculationShippingCostOptions { Amount = 300 },
    Expand = new List<string> { "line_items" },
};
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Tax.Calculations;
Stripe.Tax.Calculation calculation = service.Create(options);
```

### Response

```json
{
  "id": "taxcalc_1OduxkBUZ691iUZ4iWvpMApI",
  "object": "tax.calculation",
  "amount_total": 1953,
  "currency": "usd",
  "customer": null,
  "customer_details": {
    "address": {
      "city": "Seattle",
      "country": "US",
      "line1": "920 5th Ave",
      "line2": null,
      "postal_code": "98104",
      "state": "WA"
    },
    "address_source": "shipping",
    "ip_address": null,
    "tax_ids": [],
    "taxability_override": "none"
  },
  "expires_at": 1706708005,
  "line_items": {
    "object": "list",
    "data": [
      {
        "id": "tax_li_PSqf3RMNZa23H4",
        "object": "tax.calculation_line_item",
        "amount": 1499,
        "amount_tax": 154,
        "livemode": false,
        "product": null,
        "quantity": 1,
        "reference": "Music Streaming Coupon",
        "tax_behavior": "exclusive",
        "tax_code": "txcd_10000000"
      }
    ],
    "has_more": false,
    "total_count": 1,
    "url": "/v1/tax/calculations/taxcalc_1OduxkBUZ691iUZ4iWvpMApI/line_items"
  },
  "livemode": false,
  "ship_from_details": null,
  "shipping_cost": {
    "amount": 300,
    "amount_tax": 0,
    "tax_behavior": "exclusive",
    "tax_code": "txcd_92010001"
  },
  "tax_amount_exclusive": 154,
  "tax_amount_inclusive": 0,
  "tax_breakdown": [
    {
      "amount": 154,
      "inclusive": false,
      "tax_rate_details": {
        "country": "US",
        "percentage_decimal": "10.25",
        "state": "WA",
        "tax_type": "sales_tax"
      },
      "taxability_reason": "standard_rated",
      "taxable_amount": 1499
    },
    {
      "amount": 0,
      "inclusive": false,
      "tax_rate_details": {
        "country": "DE",
        "percentage_decimal": "0.0",
        "state": null,
        "tax_type": "vat"
      },
      "taxability_reason": "zero_rated",
      "taxable_amount": 300
    }
  ],
  "tax_date": 1706535204
}
```