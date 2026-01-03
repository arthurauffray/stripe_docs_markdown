# Create a customer

## Returns

Returns the Customer object after successful customer creation. Raises [an error](https://docs.stripe.com/api/customers/create.md#errors) if create parameters are invalid (for example, specifying an invalid coupon or an invalid source).

## Parameters

- `address` (object, required if calculating taxes)
  The customer’s address. Learn about [country-specific requirements for calculating tax](https://docs.stripe.com/invoicing/taxes.md?dashboard-or-api=dashboard#set-up-customer).

  - `address.city` (string, optional)
    City, district, suburb, town, or village.

  - `address.country` (string, optional)
    A freeform text field for the country. However, in order to activate some tax features, the format should be a two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

  - `address.line1` (string, optional)
    Address line 1, such as the street, PO Box, or company name.

  - `address.line2` (string, optional)
    Address line 2, such as the apartment, suite, unit, or building.

  - `address.postal_code` (string, optional)
    ZIP or postal code.

  - `address.state` (string, optional)
    State, county, province, or region ([ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2)).

- `balance` (integer, optional)
  An integer amount in cents that represents the customer’s current balance, which affect the customer’s future invoices. A negative amount represents a credit that decreases the amount due on an invoice; a positive amount increases the amount due on an invoice.

- `business_name` (string, optional)
  The customer’s business name. This may be up to *150 characters*.

  The maximum length is 150 characters.

- `cash_balance` (object, optional)
  Balance information and default balance settings for this customer.

  - `cash_balance.settings` (object, optional)
    Settings controlling the behavior of the customer’s cash balance, such as reconciliation of funds received.

    - `cash_balance.settings.reconciliation_mode` (enum, optional)
      Controls how funds transferred by the customer are applied to payment intents and invoices. Valid options are `automatic`, `manual`, or `merchant_default`. For more information about these reconciliation modes, see [Reconciliation](https://docs.stripe.com/docs/payments/customer-balance/reconciliation.md).
Possible enum values:
      - `automatic`
      - `manual`
      - `merchant_default`

- `description` (string, optional)
  An arbitrary string that you can attach to a customer object. It is displayed alongside the customer in the dashboard.

- `email` (string, optional)
  Customer’s email address. It’s displayed alongside the customer in your dashboard and can be useful for searching and tracking. This may be up to *512 characters*.

  The maximum length is 512 characters.

- `individual_name` (string, optional)
  The customer’s full name. This may be up to *150 characters*.

  The maximum length is 150 characters.

- `invoice_prefix` (string, optional)
  The prefix for the customer used to generate unique invoice numbers. Must be 3–12 uppercase letters or numbers.

- `invoice_settings` (object, optional)
  Default invoice settings for this customer.

  - `invoice_settings.custom_fields` (array of objects, optional)
    The list of up to 4 default custom fields to be displayed on invoices for this customer. When updating, pass an empty string to remove previously-defined fields.

    - `invoice_settings.custom_fields.name` (string, required)
      The name of the custom field. This may be up to 40 characters.

      The maximum length is 40 characters.

    - `invoice_settings.custom_fields.value` (string, required)
      The value of the custom field. This may be up to 140 characters.

      The maximum length is 140 characters.

  - `invoice_settings.default_payment_method` (string, optional)
    ID of a payment method that’s attached to the customer, to be used as the customer’s default payment method for subscriptions and invoices.

  - `invoice_settings.footer` (string, optional)
    Default footer to be displayed on invoices for this customer.

  - `invoice_settings.rendering_options` (object, optional)
    Default options for invoice PDF rendering for this customer.

    - `invoice_settings.rendering_options.amount_tax_display` (enum, optional)
      How line-item prices and amounts will be displayed with respect to tax on invoice PDFs. One of `exclude_tax` or `include_inclusive_tax`. `include_inclusive_tax` will include inclusive tax (and exclude exclusive tax) in invoice PDF amounts. `exclude_tax` will exclude all tax (inclusive and exclusive alike) from invoice PDF amounts.
Possible enum values:
      - `exclude_tax`
      - `include_inclusive_tax`

    - `invoice_settings.rendering_options.template` (string, optional)
      ID of the invoice rendering template to use for future invoices.

- `metadata` (object, optional)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.

- `name` (string, optional)
  The customer’s full name or business name.

  The maximum length is 256 characters.

- `next_invoice_sequence` (integer, optional)
  The sequence to be used on the customer’s next invoice. Defaults to 1.

- `payment_method` (string, optional)
  The ID of the PaymentMethod to attach to the customer.

- `phone` (string, optional)
  The customer’s phone number.

  The maximum length is 20 characters.

- `preferred_locales` (array of strings, optional)
  Customer’s preferred languages, ordered by preference.

- `shipping` (object, optional)
  The customer’s shipping information. Appears on invoices emailed to this customer.

  - `shipping.address` (object, required)
    Customer shipping address.

    - `shipping.address.city` (string, optional)
      City, district, suburb, town, or village.

    - `shipping.address.country` (string, optional)
      A freeform text field for the country. However, in order to activate some tax features, the format should be a two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

    - `shipping.address.line1` (string, optional)
      Address line 1, such as the street, PO Box, or company name.

    - `shipping.address.line2` (string, optional)
      Address line 2, such as the apartment, suite, unit, or building.

    - `shipping.address.postal_code` (string, optional)
      ZIP or postal code.

    - `shipping.address.state` (string, optional)
      State, county, province, or region ([ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2)).

  - `shipping.name` (string, required)
    Customer name.

  - `shipping.phone` (string, optional)
    Customer phone (including extension).

- `source` (string, optional)
  When using payment sources created via the Token or Sources APIs, passing `source` will create a new source object, make it the new customer default source, and delete the old customer default if one exists. If you want to add additional sources instead of replacing the existing default, use the [card creation API](https://docs.stripe.com/docs/api.md#create_card). Whenever you attach a card to a customer, Stripe will automatically validate the card.

- `tax` (object, recommended if calculating taxes)
  Tax details about the customer.

  - `tax.ip_address` (string, optional)
    A recent IP address of the customer used for tax reporting and tax location inference. Stripe recommends updating the IP address when a new PaymentMethod is attached or the address field on the customer is updated. We recommend against updating this field more frequently since it could result in unexpected tax location/reporting outcomes.

  - `tax.validate_location` (enum, optional)
    A flag that indicates when Stripe should validate the customer tax location. Defaults to `deferred`.
Possible enum values:
    - `deferred`
      Defer the validation of the customer’s tax location until needed, such as when Stripe Tax is calculating taxes on an Invoice. **Default.**

    - `immediately`
      Validate the customer’s tax location immediately. An error is returned and the customer is not created/updated if the tax location is invalid. **Recommended if calculating taxes.**

- `tax_exempt` (enum, optional)
  The customer’s tax exemption. One of `none`, `exempt`, or `reverse`.
Possible enum values:
  - `exempt`
  - `none`
  - `reverse`

- `tax_id_data` (array of objects, optional)
  The customer’s tax IDs.

  - `tax_id_data.type` (string, required)
    Type of the tax ID, one of `ad_nrt`, `ae_trn`, `al_tin`, `am_tin`, `ao_tin`, `ar_cuit`, `au_abn`, `au_arn`, `aw_tin`, `az_tin`, `ba_tin`, `bb_tin`, `bd_bin`, `bf_ifu`, `bg_uic`, `bh_vat`, `bj_ifu`, `bo_tin`, `br_cnpj`, `br_cpf`, `bs_tin`, `by_tin`, `ca_bn`, `ca_gst_hst`, `ca_pst_bc`, `ca_pst_mb`, `ca_pst_sk`, `ca_qst`, `cd_nif`, `ch_uid`, `ch_vat`, `cl_tin`, `cm_niu`, `cn_tin`, `co_nit`, `cr_tin`, `cv_nif`, `de_stn`, `do_rcn`, `ec_ruc`, `eg_tin`, `es_cif`, `et_tin`, `eu_oss_vat`, `eu_vat`, `gb_vat`, `ge_vat`, `gn_nif`, `hk_br`, `hr_oib`, `hu_tin`, `id_npwp`, `il_vat`, `in_gst`, `is_vat`, `jp_cn`, `jp_rn`, `jp_trn`, `ke_pin`, `kg_tin`, `kh_tin`, `kr_brn`, `kz_bin`, `la_tin`, `li_uid`, `li_vat`, `ma_vat`, `md_vat`, `me_pib`, `mk_vat`, `mr_nif`, `mx_rfc`, `my_frp`, `my_itn`, `my_sst`, `ng_tin`, `no_vat`, `no_voec`, `np_pan`, `nz_gst`, `om_vat`, `pe_ruc`, `ph_tin`, `ro_tin`, `rs_pib`, `ru_inn`, `ru_kpp`, `sa_vat`, `sg_gst`, `sg_uen`, `si_tin`, `sn_ninea`, `sr_fin`, `sv_nit`, `th_vat`, `tj_tin`, `tr_tin`, `tw_vat`, `tz_vat`, `ua_vat`, `ug_tin`, `us_ein`, `uy_ruc`, `uz_tin`, `uz_vat`, `ve_rif`, `vn_tin`, `za_vat`, `zm_tin`, or `zw_tin`

  - `tax_id_data.value` (string, required)
    Value of the tax ID.

- `test_clock` (string, optional)
  ID of the test clock to attach to the customer.

```curl
curl https://api.stripe.com/v1/customers \
  -u "<<YOUR_SECRET_KEY>>" \
  -d name="Jenny Rosen" \
  --data-urlencode email="jennyrosen@example.com"
```

```cli
stripe customers create  \
  --name="Jenny Rosen" \
  --email="jennyrosen@example.com"
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

customer = client.v1.customers.create({
  name: 'Jenny Rosen',
  email: 'jennyrosen@example.com',
})
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

customer = client.v1.customers.create({
  "name": "Jenny Rosen",
  "email": "jennyrosen@example.com",
})
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$customer = $stripe->customers->create([
  'name' => 'Jenny Rosen',
  'email' => 'jennyrosen@example.com',
]);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

CustomerCreateParams params =
  CustomerCreateParams.builder()
    .setName("Jenny Rosen")
    .setEmail("jennyrosen@example.com")
    .build();

Customer customer = client.v1().customers().create(params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const customer = await stripe.customers.create({
  name: 'Jenny Rosen',
  email: 'jennyrosen@example.com',
});
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.CustomerCreateParams{
  Name: stripe.String("Jenny Rosen"),
  Email: stripe.String("jennyrosen@example.com"),
}
result, err := sc.V1Customers.Create(context.TODO(), params)
```

```dotnet
var options = new CustomerCreateOptions
{
    Name = "Jenny Rosen",
    Email = "jennyrosen@example.com",
};
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Customers;
Customer customer = service.Create(options);
```

### Response

```json
{
  "id": "cus_NffrFeUfNV2Hib",
  "object": "customer",
  "address": null,
  "balance": 0,
  "created": 1680893993,
  "currency": null,
  "default_source": null,
  "delinquent": false,
  "description": null,
  "email": "jennyrosen@example.com",
  "invoice_prefix": "0759376C",
  "invoice_settings": {
    "custom_fields": null,
    "default_payment_method": null,
    "footer": null,
    "rendering_options": null
  },
  "livemode": false,
  "metadata": {},
  "name": "Jenny Rosen",
  "next_invoice_sequence": 1,
  "phone": null,
  "preferred_locales": [],
  "shipping": null,
  "tax_exempt": "none",
  "test_clock": null
}
```