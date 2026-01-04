# The Tax Transaction object

## Attributes

- `id` (string)
  Unique identifier for the transaction.

- `object` (string)
  String representing the object’s type. Objects of the same type share the same value.

- `created` (timestamp)
  Time at which the object was created. Measured in seconds since the Unix epoch.

- `currency` (string)
  Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

- `customer` (string, nullable)
  The ID of an existing [Customer](https://docs.stripe.com/docs/api/customers/object.md) used for the resource.

- `customer_details` (object)
  The customer’s details, such as address and tax IDs.

  - `customer_details.address` (object, nullable)
    The customer’s postal address (for example, home or business location).

    - `customer_details.address.city` (string, nullable)
      City, district, suburb, town, or village.

    - `customer_details.address.country` (string)
      Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

    - `customer_details.address.line1` (string, nullable)
      Address line 1, such as the street, PO Box, or company name.

    - `customer_details.address.line2` (string, nullable)
      Address line 2, such as the apartment, suite, unit, or building.

    - `customer_details.address.postal_code` (string, nullable)
      ZIP or postal code.

    - `customer_details.address.state` (string, nullable)
      State/province as an [ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2) subdivision code, without country prefix, such as “NY” or “TX”.

  - `customer_details.address_source` (enum, nullable)
    The type of customer address provided.
Possible enum values:
    - `billing`
      Denotes the address as billing address.

    - `shipping`
      Denotes the address as shipping address.

  - `customer_details.ip_address` (string, nullable)
    The customer’s IP address (IPv4 or IPv6).

  - `customer_details.tax_ids` (array of objects)
    The customer’s tax IDs (for example, EU VAT numbers).

    - `customer_details.tax_ids.type` (enum)
      The type of the tax ID, one of `ad_nrt`, `ar_cuit`, `eu_vat`, `bo_tin`, `br_cnpj`, `br_cpf`, `cn_tin`, `co_nit`, `cr_tin`, `do_rcn`, `ec_ruc`, `eu_oss_vat`, `hr_oib`, `pe_ruc`, `ro_tin`, `rs_pib`, `sv_nit`, `uy_ruc`, `ve_rif`, `vn_tin`, `gb_vat`, `nz_gst`, `au_abn`, `au_arn`, `in_gst`, `no_vat`, `no_voec`, `za_vat`, `ch_vat`, `mx_rfc`, `sg_uen`, `ru_inn`, `ru_kpp`, `ca_bn`, `hk_br`, `es_cif`, `tw_vat`, `th_vat`, `jp_cn`, `jp_rn`, `jp_trn`, `li_uid`, `li_vat`, `my_itn`, `us_ein`, `kr_brn`, `ca_qst`, `ca_gst_hst`, `ca_pst_bc`, `ca_pst_mb`, `ca_pst_sk`, `my_sst`, `sg_gst`, `ae_trn`, `cl_tin`, `sa_vat`, `id_npwp`, `my_frp`, `il_vat`, `ge_vat`, `ua_vat`, `is_vat`, `bg_uic`, `hu_tin`, `si_tin`, `ke_pin`, `tr_tin`, `eg_tin`, `ph_tin`, `al_tin`, `bh_vat`, `kz_bin`, `ng_tin`, `om_vat`, `de_stn`, `ch_uid`, `tz_vat`, `uz_vat`, `uz_tin`, `md_vat`, `ma_vat`, `by_tin`, `ao_tin`, `bs_tin`, `bb_tin`, `cd_nif`, `mr_nif`, `me_pib`, `zw_tin`, `ba_tin`, `gn_nif`, `mk_vat`, `sr_fin`, `sn_ninea`, `am_tin`, `np_pan`, `tj_tin`, `ug_tin`, `zm_tin`, `kh_tin`, `aw_tin`, `az_tin`, `bd_bin`, `bj_ifu`, `et_tin`, `kg_tin`, `la_tin`, `cm_niu`, `cv_nif`, `bf_ifu`, or `unknown`
Possible enum values:
      - `ad_nrt`
      - `ae_trn`
      - `al_tin`
      - `am_tin`
      - `ao_tin`
      - `ar_cuit`
      - `au_abn`
      - `au_arn`
      - `aw_tin`
      - `az_tin`
      - `ba_tin`
      - `bb_tin`
      - `bd_bin`
      - `bf_ifu`
      - `bg_uic`
      - `bh_vat`
      - `bj_ifu`
      - `bo_tin`
      - `br_cnpj`
      - `br_cpf`
      - `bs_tin`
      - `by_tin`
      - `ca_bn`
      - `ca_gst_hst`
      - `ca_pst_bc`
      - `ca_pst_mb`
      - `ca_pst_sk`
      - `ca_qst`
      - `cd_nif`
      - `ch_uid`
      - `ch_vat`
      - `cl_tin`
      - `cm_niu`
      - `cn_tin`
      - `co_nit`
      - `cr_tin`
      - `cv_nif`
      - `de_stn`
      - `do_rcn`
      - `ec_ruc`
      - `eg_tin`
      - `es_cif`
      - `et_tin`
      - `eu_oss_vat`
      - `eu_vat`
      - `gb_vat`
      - `ge_vat`
      - `gn_nif`
      - `hk_br`
      - `hr_oib`
      - `hu_tin`
      - `id_npwp`
      - `il_vat`
      - `in_gst`
      - `is_vat`
      - `jp_cn`
      - `jp_rn`
      - `jp_trn`
      - `ke_pin`
      - `kg_tin`
      - `kh_tin`
      - `kr_brn`
      - `kz_bin`
      - `la_tin`
      - `li_uid`
      - `li_vat`
      - `ma_vat`
      - `md_vat`
      - `me_pib`
      - `mk_vat`
      - `mr_nif`
      - `mx_rfc`
      - `my_frp`
      - `my_itn`
      - `my_sst`
      - `ng_tin`
      - `no_vat`
      - `no_voec`
      - `np_pan`
      - `nz_gst`
      - `om_vat`
      - `pe_ruc`
      - `ph_tin`
      - `ro_tin`
      - `rs_pib`
      - `ru_inn`
      - `ru_kpp`
      - `sa_vat`
      - `sg_gst`
      - `sg_uen`
      - `si_tin`
      - `sn_ninea`
      - `sr_fin`
      - `sv_nit`
      - `th_vat`
      - `tj_tin`
      - `tr_tin`
      - `tw_vat`
      - `tz_vat`
      - `ua_vat`
      - `ug_tin`
      - `unknown`
      - `us_ein`
      - `uy_ruc`
      - `uz_tin`
      - `uz_vat`
      - `ve_rif`
      - `vn_tin`
      - `za_vat`
      - `zm_tin`
      - `zw_tin`

    - `customer_details.tax_ids.value` (string)
      The value of the tax ID.

  - `customer_details.taxability_override` (enum)
    The taxability override used for taxation.
Possible enum values:
    - `customer_exempt`
      The customer is exempt of tax.

    - `none`
      No taxability override (default).

    - `reverse_charge`
      The customer is entitled to reverse charge tax treatment.

- `line_items` (object, nullable)
  The tax collected or refunded, by line item.

  - `line_items.object` (string)
    String representing the object’s type. Objects of the same type share the same value. Always has the value `list`.

  - `line_items.data` (array of objects)
    Details about each object.

    - `line_items.data.id` (string)
      Unique identifier for the object.

    - `line_items.data.object` (string)
      String representing the object’s type. Objects of the same type share the same value.

    - `line_items.data.amount` (integer)
      The line item amount in the [smallest currency unit](https://docs.stripe.com/docs/currencies.md#zero-decimal). If `tax_behavior=inclusive`, then this amount includes taxes. Otherwise, taxes were calculated on top of this amount.

    - `line_items.data.amount_tax` (integer)
      The amount of tax calculated for this line item, in the [smallest currency unit](https://docs.stripe.com/docs/currencies.md#zero-decimal).

    - `line_items.data.livemode` (boolean)
      Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.

    - `line_items.data.metadata` (object, nullable)
      Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

    - `line_items.data.product` (string, nullable)
      The ID of an existing [Product](https://docs.stripe.com/docs/api/products/object.md).

    - `line_items.data.quantity` (integer)
      The number of units of the item being purchased. For reversals, this is the quantity reversed.

    - `line_items.data.reference` (string)
      A custom identifier for this line item in the transaction.

    - `line_items.data.reversal` (object, nullable)
      If `type=reversal`, contains information about what was reversed.

      - `line_items.data.reversal.original_line_item` (string)
        The `id` of the line item to reverse in the original transaction.

    - `line_items.data.tax_behavior` (enum)
      Specifies whether the `amount` includes taxes. If `tax_behavior=inclusive`, then the amount includes taxes.
Possible enum values:
      - `exclusive`
        Taxes are calculated on top of the line item amount (default).

      - `inclusive`
        Taxes are included in the line item amount.

    - `line_items.data.tax_code` (string)
      The [tax code](https://docs.stripe.com/docs/tax/tax-categories.md) ID used for this resource.

    - `line_items.data.type` (enum)
      If `reversal`, this line item reverses an earlier transaction.
Possible enum values:
      - `reversal`
        Represents a partial or full reversal of an earlier transaction.

      - `transaction`
        Represents a customer sale or order.

  - `line_items.has_more` (boolean)
    True if this list has another page of items after this one that can be fetched.

  - `line_items.url` (string)
    The URL where this list can be accessed.

- `livemode` (boolean)
  Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.

- `metadata` (object, nullable)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

- `posted_at` (timestamp)
  The Unix timestamp representing when the tax liability is assumed or reduced.

- `reference` (string)
  A custom unique identifier, such as ‘myOrder_123’.

- `reversal` (object, nullable)
  If `type=reversal`, contains information about what was reversed.

  - `reversal.original_transaction` (string, nullable)
    The `id` of the reversed `Transaction` object.

- `ship_from_details` (object, nullable)
  The details of the ship from location, such as the address.

  - `ship_from_details.address` (object)
    The address from which the goods in the transaction are shipped from.

    - `ship_from_details.address.city` (string, nullable)
      City, district, suburb, town, or village.

    - `ship_from_details.address.country` (string)
      Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

    - `ship_from_details.address.line1` (string, nullable)
      Address line 1, such as the street, PO Box, or company name.

    - `ship_from_details.address.line2` (string, nullable)
      Address line 2, such as the apartment, suite, unit, or building.

    - `ship_from_details.address.postal_code` (string, nullable)
      ZIP or postal code.

    - `ship_from_details.address.state` (string, nullable)
      State/province as an [ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2) subdivision code, without country prefix, such as “NY” or “TX”.

- `shipping_cost` (object, nullable)
  The shipping cost details for the transaction.

  - `shipping_cost.amount` (integer)
    The shipping amount in the [smallest currency unit](https://docs.stripe.com/docs/currencies.md#zero-decimal). If `tax_behavior=inclusive`, then this amount includes taxes. Otherwise, taxes were calculated on top of this amount.

  - `shipping_cost.amount_tax` (integer)
    The amount of tax calculated for shipping, in the [smallest currency unit](https://docs.stripe.com/docs/currencies.md#zero-decimal).

  - `shipping_cost.shipping_rate` (string, nullable)
    The ID of an existing [ShippingRate](https://docs.stripe.com/docs/api/shipping_rates/object.md).

  - `shipping_cost.tax_behavior` (enum)
    Specifies whether the `amount` includes taxes. If `tax_behavior=inclusive`, then the amount includes taxes.
Possible enum values:
    - `exclusive`
      Taxes are calculated on top of the shipping cost amount (default).

    - `inclusive`
      Taxes are included in the shipping cost amount.

  - `shipping_cost.tax_code` (string)
    The [tax code](https://docs.stripe.com/docs/tax/tax-categories.md) ID used for shipping.

- `tax_date` (timestamp)
  Timestamp of date at which the tax rules and rates in effect applies for the calculation.

- `type` (enum)
  If `reversal`, this transaction reverses an earlier transaction.
Possible enum values:
  - `reversal`
    Represents a partial or full reversal of an earlier transaction.

  - `transaction`
    Represents a customer sale or order.

### The Tax Transaction object

```json
{
  "id": "tax_1NaS0I2eZvKYlo2CRuMhUcmz",
  "object": "tax.transaction",
  "created": 1690932566,
  "currency": "usd",
  "customer": null,
  "customer_details": {
    "address": {
      "city": "South San Francisco",
      "country": "US",
      "line1": "354 Oyster Point Blvd",
      "line2": "",
      "postal_code": "94080",
      "state": "CA"
    },
    "address_source": "shipping",
    "ip_address": null,
    "tax_ids": [],
    "taxability_override": "none"
  },
  "line_items": {
    "object": "list",
    "data": [
      {
        "id": "tax_li_ONCP443tgfS8I1",
        "object": "tax.transaction_line_item",
        "amount": 1499,
        "amount_tax": 148,
        "livemode": false,
        "metadata": null,
        "product": null,
        "quantity": 1,
        "reference": "Pepperoni Pizza",
        "reversal": null,
        "tax_behavior": "exclusive",
        "tax_code": "txcd_40060003",
        "type": "transaction"
      }
    ],
    "has_more": false,
    "url": "/v1/tax/transactions/tax_1NaS0I2eZvKYlo2CRuMhUcmz/line_items"
  },
  "livemode": false,
  "metadata": null,
  "posted_at": 1690932566,
  "reference": "myOrder_123",
  "reversal": null,
  "shipping_cost": {
    "amount": 300,
    "amount_tax": 0,
    "tax_behavior": "exclusive",
    "tax_code": "txcd_92010001"
  },
  "ship_from_details": {
    "address": {
      "postal_code": "75001",
      "state": "TX",
      "country": "US"
    }
  },
  "tax_date": 1690932566,
  "type": "transaction"
}
```