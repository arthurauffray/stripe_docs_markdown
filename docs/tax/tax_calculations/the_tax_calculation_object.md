# The Tax Calculation object

## Attributes

- `id` (string, nullable)
  Unique identifier for the calculation.

- `object` (string)
  String representing the object’s type. Objects of the same type share the same value.

- `amount_total` (integer)
  Total amount after taxes in the [smallest currency unit](https://docs.stripe.com/docs/currencies.md#zero-decimal).

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

- `expires_at` (timestamp, nullable)
  Timestamp of date at which the tax calculation will expire.

- `line_items` (object, nullable)
  The list of items the customer is purchasing.

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
      A custom identifier for this line item.

    - `line_items.data.tax_behavior` (enum)
      Specifies whether the `amount` includes taxes. If `tax_behavior=inclusive`, then the amount includes taxes.
Possible enum values:
      - `exclusive`
        Taxes are calculated on top of the line item amount (default).

      - `inclusive`
        Taxes are included in the line item amount.

    - `line_items.data.tax_breakdown` (array of objects, nullable)
      Detailed account of taxes relevant to this line item.

      - `line_items.data.tax_breakdown.amount` (integer)
        The amount of tax, in the [smallest currency unit](https://docs.stripe.com/docs/currencies.md#zero-decimal).

      - `line_items.data.tax_breakdown.jurisdiction` (object)
        The jurisdiction in which tax is imposed.

        - `line_items.data.tax_breakdown.jurisdiction.country` (string)
          Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

        - `line_items.data.tax_breakdown.jurisdiction.display_name` (string)
          A human-readable name for the jurisdiction imposing the tax.

        - `line_items.data.tax_breakdown.jurisdiction.level` (enum)
          Indicates the level of the jurisdiction imposing the tax.
Possible enum values:
          - `city`
            Level pertaining to city (e.g. Chicago)

          - `country`
            Level pertaining to country (e.g. United States, Ireland, etc.)

          - `county`
            Level pertaining to county (e.g. Cook)

          - `district`
            Level pertaining to district (e.g. Roseland)

          - `state`
            Level pertaining to state (e.g. Illinois)

        - `line_items.data.tax_breakdown.jurisdiction.state` (string, nullable)
          [ISO 3166-2 subdivision code](https://en.wikipedia.org/wiki/ISO_3166-2), without country prefix. For example, “NY” for New York, United States.

      - `line_items.data.tax_breakdown.sourcing` (enum)
        Indicates whether the jurisdiction was determined by the origin (merchant’s address) or destination (customer’s address).
Possible enum values:
        - `destination`
          The tax is calculated at the customer’s address.

        - `origin`
          The tax is calculated at one of your addresses, for example the main establishment.

      - `line_items.data.tax_breakdown.tax_rate_details` (object, nullable)
        Details regarding the rate for this tax. This field will be `null` when the tax is not imposed, for example if the product is exempt from tax.

        - `line_items.data.tax_breakdown.tax_rate_details.display_name` (string)
          A localized display name for tax type, intended to be human-readable. For example, “Local Sales and Use Tax”, “Value-added tax (VAT)”, or “Umsatzsteuer (USt.)”.

        - `line_items.data.tax_breakdown.tax_rate_details.percentage_decimal` (string)
          The tax rate percentage as a string. For example, 8.5% is represented as “8.5”.

        - `line_items.data.tax_breakdown.tax_rate_details.tax_type` (enum)
          The tax type, such as `vat` or `sales_tax`.
Possible enum values:
          - `amusement_tax`
            Amusement Tax

          - `communications_tax`
            Communications Tax

          - `gst`
            Goods and Services Tax

          - `hst`
            Harmonized Sales Tax

          - `igst`
            Integrated Goods and Services Tax

          - `jct`
            Japanese Consumption Tax

          - `lease_tax`
            Chicago Lease Tax

          - `pst`
            Provincial Sales Tax

          - `qst`
            Quebec Sales Tax

          - `retail_delivery_fee`
            Retail Delivery Fee

          - `rst`
            Retail Sales Tax

          - `sales_tax`
            Sales Tax

          - `service_tax`
            Service Tax

          - `vat`
            Value-Added Tax

      - `line_items.data.tax_breakdown.taxability_reason` (enum)
        The reasoning behind this tax, for example, if the product is tax exempt. The possible values for this field may be extended as new tax rules are supported.
Possible enum values:
        - `customer_exempt`
          No tax is applied as the customer is exempt from tax.

        - `not_collecting`
          No tax is collected either because you are not registered to collect tax in this jurisdiction, or because the non-taxable product tax code (`txcd_00000000`) was used.

        - `not_subject_to_tax`
          No tax is imposed on this transaction.

        - `not_supported`
          No tax applied. Stripe doesn’t support this jurisdiction, territory, or product.

        - `portion_product_exempt`
          A portion of the price is exempt from tax.

        - `portion_reduced_rated`
          A portion of the price is taxed at a reduced rate.

        - `portion_standard_rated`
          A portion of the price is taxed at the standard rate.

        - `product_exempt`
          The product or service is nontaxable or exempt from tax.

        - `product_exempt_holiday`
          The product or service is not taxed due to a sales tax holiday.

        - `proportionally_rated`
          The shipping cost tax rate is calculated as a weighted average of the other line items’ rates, weighted by their amounts.

        - `reduced_rated`
          Taxed at a reduced rate.

        - `reverse_charge`
          No tax is applied as it is the responsibility of the buyer to account for tax in this case.

        - `standard_rated`
          Taxed at the standard rate.

        - `taxable_basis_reduced`
          A reduced amount of the price is subject to tax.

        - `zero_rated`
          The transaction is taxed at a special rate of 0% or the transaction is exempt (but these exempt transactions still let you deduct the “input VAT” paid on your business purchases).

      - `line_items.data.tax_breakdown.taxable_amount` (integer)
        The amount on which tax is calculated, in the [smallest currency unit](https://docs.stripe.com/docs/currencies.md#zero-decimal).

    - `line_items.data.tax_code` (string)
      The [tax code](https://docs.stripe.com/docs/tax/tax-categories.md) ID used for this resource.

  - `line_items.has_more` (boolean)
    True if this list has another page of items after this one that can be fetched.

  - `line_items.url` (string)
    The URL where this list can be accessed.

- `livemode` (boolean)
  Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.

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
  The shipping cost details for the calculation.

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

  - `shipping_cost.tax_breakdown` (array of objects, nullable)
    Detailed account of taxes relevant to shipping cost.

    - `shipping_cost.tax_breakdown.amount` (integer)
      The amount of tax, in the [smallest currency unit](https://docs.stripe.com/docs/currencies.md#zero-decimal).

    - `shipping_cost.tax_breakdown.jurisdiction` (object)
      The jurisdiction in which tax is imposed.

      - `shipping_cost.tax_breakdown.jurisdiction.country` (string)
        Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

      - `shipping_cost.tax_breakdown.jurisdiction.display_name` (string)
        A human-readable name for the jurisdiction imposing the tax.

      - `shipping_cost.tax_breakdown.jurisdiction.level` (enum)
        Indicates the level of the jurisdiction imposing the tax.
Possible enum values:
        - `city`
          Level pertaining to city (e.g. Chicago)

        - `country`
          Level pertaining to country (e.g. United States, Ireland, etc.)

        - `county`
          Level pertaining to county (e.g. Cook)

        - `district`
          Level pertaining to district (e.g. Roseland)

        - `state`
          Level pertaining to state (e.g. Illinois)

      - `shipping_cost.tax_breakdown.jurisdiction.state` (string, nullable)
        [ISO 3166-2 subdivision code](https://en.wikipedia.org/wiki/ISO_3166-2), without country prefix. For example, “NY” for New York, United States.

    - `shipping_cost.tax_breakdown.sourcing` (enum)
      Indicates whether the jurisdiction was determined by the origin (merchant’s address) or destination (customer’s address).
Possible enum values:
      - `destination`
        The tax is calculated at the customer’s address.

      - `origin`
        The tax is calculated at one of your addresses, for example the main establishment.

    - `shipping_cost.tax_breakdown.tax_rate_details` (object, nullable)
      Details regarding the rate for this tax. This field will be `null` when the tax is not imposed, for example if the product is exempt from tax.

      - `shipping_cost.tax_breakdown.tax_rate_details.display_name` (string)
        A localized display name for tax type, intended to be human-readable. For example, “Local Sales and Use Tax”, “Value-added tax (VAT)”, or “Umsatzsteuer (USt.)”.

      - `shipping_cost.tax_breakdown.tax_rate_details.percentage_decimal` (string)
        The tax rate percentage as a string. For example, 8.5% is represented as “8.5”.

      - `shipping_cost.tax_breakdown.tax_rate_details.tax_type` (enum)
        The tax type, such as `vat` or `sales_tax`.
Possible enum values:
        - `amusement_tax`
          Amusement Tax

        - `communications_tax`
          Communications Tax

        - `gst`
          Goods and Services Tax

        - `hst`
          Harmonized Sales Tax

        - `igst`
          Integrated Goods and Services Tax

        - `jct`
          Japanese Consumption Tax

        - `lease_tax`
          Chicago Lease Tax

        - `pst`
          Provincial Sales Tax

        - `qst`
          Quebec Sales Tax

        - `retail_delivery_fee`
          Retail Delivery Fee

        - `rst`
          Retail Sales Tax

        - `sales_tax`
          Sales Tax

        - `service_tax`
          Service Tax

        - `vat`
          Value-Added Tax

    - `shipping_cost.tax_breakdown.taxability_reason` (enum)
      The reasoning behind this tax, for example, if the product is tax exempt. The possible values for this field may be extended as new tax rules are supported.
Possible enum values:
      - `customer_exempt`
        No tax is applied as the customer is exempt from tax.

      - `not_collecting`
        No tax is collected either because you are not registered to collect tax in this jurisdiction, or because the non-taxable product tax code (`txcd_00000000`) was used.

      - `not_subject_to_tax`
        No tax is imposed on this transaction.

      - `not_supported`
        No tax applied. Stripe doesn’t support this jurisdiction, territory, or product.

      - `portion_product_exempt`
        A portion of the price is exempt from tax.

      - `portion_reduced_rated`
        A portion of the price is taxed at a reduced rate.

      - `portion_standard_rated`
        A portion of the price is taxed at the standard rate.

      - `product_exempt`
        The product or service is nontaxable or exempt from tax.

      - `product_exempt_holiday`
        The product or service is not taxed due to a sales tax holiday.

      - `proportionally_rated`
        The shipping cost tax rate is calculated as a weighted average of the other line items’ rates, weighted by their amounts.

      - `reduced_rated`
        Taxed at a reduced rate.

      - `reverse_charge`
        No tax is applied as it is the responsibility of the buyer to account for tax in this case.

      - `standard_rated`
        Taxed at the standard rate.

      - `taxable_basis_reduced`
        A reduced amount of the price is subject to tax.

      - `zero_rated`
        The transaction is taxed at a special rate of 0% or the transaction is exempt (but these exempt transactions still let you deduct the “input VAT” paid on your business purchases).

    - `shipping_cost.tax_breakdown.taxable_amount` (integer)
      The amount on which tax is calculated, in the [smallest currency unit](https://docs.stripe.com/docs/currencies.md#zero-decimal).

  - `shipping_cost.tax_code` (string)
    The [tax code](https://docs.stripe.com/docs/tax/tax-categories.md) ID used for shipping.

- `tax_amount_exclusive` (integer)
  The amount of tax to be collected on top of the line item prices.

- `tax_amount_inclusive` (integer)
  The amount of tax already included in the line item prices.

- `tax_breakdown` (array of objects)
  Breakdown of individual tax amounts that add up to the total.

  - `tax_breakdown.amount` (integer)
    The amount of tax, in the [smallest currency unit](https://docs.stripe.com/docs/currencies.md#zero-decimal).

  - `tax_breakdown.inclusive` (boolean)
    Specifies whether the tax amount is included in the line item amount.

  - `tax_breakdown.tax_rate_details` (object)
    Details of the applied tax rate, such as type, percentage, state and country.

    - `tax_breakdown.tax_rate_details.country` (string, nullable)
      Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

    - `tax_breakdown.tax_rate_details.flat_amount` (object, nullable)
      The amount of the tax rate when the `rate_type` is `flat_amount`. Tax rates with `rate_type` `percentage` can vary based on the transaction, resulting in this field being `null`. This field exposes the amount and currency of the flat tax rate.

      - `tax_breakdown.tax_rate_details.flat_amount.amount` (integer)
        Amount of the tax when the `rate_type` is `flat_amount`. This positive integer represents how much to charge in the smallest currency unit (e.g., 100 cents to charge $1.00 or 100 to charge ¥100, a zero-decimal currency). The amount value supports up to eight digits (e.g., a value of 99999999 for a USD charge of $999,999.99).

      - `tax_breakdown.tax_rate_details.flat_amount.currency` (string)
        Three-letter ISO currency code, in lowercase.

    - `tax_breakdown.tax_rate_details.percentage_decimal` (string)
      The tax rate percentage as a string. For example, 8.5% is represented as `"8.5"`.

    - `tax_breakdown.tax_rate_details.rate_type` (enum, nullable)
      Indicates the type of tax rate applied to the taxable amount. This value can be `null` when no tax applies to the location. This field is only present for TaxRates created by Stripe Tax.
Possible enum values:
      - `flat_amount`
        A fixed amount applied as tax, regardless of the taxable amount, such as a retail delivery fee.

      - `percentage`
        A tax rate expressed as a percentage of the taxable amount, such as the sales tax rate in California.

    - `tax_breakdown.tax_rate_details.state` (string, nullable)
      State, county, province, or region ([ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2)).

    - `tax_breakdown.tax_rate_details.tax_type` (enum, nullable)
      The tax type, such as `vat` or `sales_tax`.
Possible enum values:
      - `amusement_tax`
        Amusement Tax

      - `communications_tax`
        Communications Tax

      - `gst`
        Goods and Services Tax

      - `hst`
        Harmonized Sales Tax

      - `igst`
        Integrated Goods and Services Tax

      - `jct`
        Japanese Consumption Tax

      - `lease_tax`
        Chicago Lease Tax

      - `pst`
        Provincial Sales Tax

      - `qst`
        Quebec Sales Tax

      - `retail_delivery_fee`
        Retail Delivery Fee

      - `rst`
        Retail Sales Tax

      - `sales_tax`
        Sales Tax

      - `service_tax`
        Service Tax

      - `vat`
        Value-Added Tax

  - `tax_breakdown.taxability_reason` (enum)
    The reasoning behind this tax, for example, if the product is tax exempt. We might extend the possible values for this field to support new tax rules.
Possible enum values:
    - `customer_exempt`
      No tax is applied as the customer is exempt from tax.

    - `not_collecting`
      No tax is collected either because you are not registered to collect tax in this jurisdiction, or because the non-taxable product tax code (`txcd_00000000`) was used.

    - `not_subject_to_tax`
      No tax is imposed on this transaction.

    - `not_supported`
      No tax applied. Stripe doesn’t support this jurisdiction, territory, or product.

    - `portion_product_exempt`
      A portion of the price is exempt from tax.

    - `portion_reduced_rated`
      A portion of the price is taxed at a reduced rate.

    - `portion_standard_rated`
      A portion of the price is taxed at the standard rate.

    - `product_exempt`
      The product or service is nontaxable or exempt from tax.

    - `product_exempt_holiday`
      The product or service is not taxed due to a sales tax holiday.

    - `proportionally_rated`
      The shipping cost tax rate is calculated as a weighted average of the other line items’ rates, weighted by their amounts.

    - `reduced_rated`
      Taxed at a reduced rate.

    - `reverse_charge`
      No tax is applied as it is the responsibility of the buyer to account for tax in this case.

    - `standard_rated`
      Taxed at the standard rate.

    - `taxable_basis_reduced`
      A reduced amount of the price is subject to tax.

    - `zero_rated`
      The transaction is taxed at a special rate of 0% or the transaction is exempt (but these exempt transactions still let you deduct the “input VAT” paid on your business purchases).

  - `tax_breakdown.taxable_amount` (integer)
    The amount on which tax is calculated, in the [smallest currency unit](https://docs.stripe.com/docs/currencies.md#zero-decimal).

- `tax_date` (timestamp)
  Timestamp of date at which the tax rules and rates in effect applies for the calculation.

### The Tax Calculation object

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