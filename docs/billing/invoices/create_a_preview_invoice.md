# Create a preview invoice

At any time, you can preview the upcoming invoice for a subscription or subscription schedule. This will show you all the charges that are pending, including subscription renewal charges, invoice item charges, etc. It will also show you any discounts that are applicable to the invoice.

You can also preview the effects of creating or updating a subscription or subscription schedule, including a preview of any prorations that will take place. To ensure that the actual proration is calculated exactly the same as the previewed proration, you should pass the `subscription_details.proration_date` parameter when doing the actual subscription update.

The recommended way to get only the prorations being previewed on the invoice is to consider line items where `parent.subscription_item_details.proration` is `true`.

Note that when you are viewing an upcoming invoice, you are simply viewing a preview – the invoice has not yet been created. As such, the upcoming invoice will not show up in invoice listing calls, and you cannot use the API to pay or edit the invoice. If you want to change the amount that your customer will be billed, you can add, remove, or update pending invoice items, or update the customer’s discount.

Note: Currency conversion calculations use the latest exchange rates. Exchange rates may vary between the time of the preview and the time of the actual invoice creation. [Learn more](https://docs.stripe.com/currencies/conversions.md)

## Returns

Returns an invoice if valid customer information is provided. Raises [an error](https://docs.stripe.com/api/invoices/create_preview.md#errors) otherwise.

## Parameters

- `automatic_tax` (object, optional)
  Settings for automatic tax lookup for this invoice preview.

  - `automatic_tax.enabled` (boolean, required)
    Whether Stripe automatically computes tax on this invoice. Note that incompatible invoice items (invoice items with manually specified [tax rates](https://docs.stripe.com/docs/api/tax_rates.md), negative amounts, or `tax_behavior=unspecified`) cannot be added to automatic tax invoices.

  - `automatic_tax.liability` (object, optional)
    The account that’s liable for tax. If set, the business address and tax registrations required to perform the tax calculation are loaded from this account. The tax transaction is returned in the report of the connected account.

    - `automatic_tax.liability.type` (enum, required)
      Type of the account referenced in the request.
Possible enum values:
      - `account`
        Indicates that the account being referenced is a connected account which is different from the account making the API request but related to it.

      - `self`
        Indicates that the account being referenced is the account making the API request.

    - `automatic_tax.liability.account` (string, required only if type is account)
      The connected account being referenced when `type` is `account`.

- `currency` (enum, optional)
  The currency to preview this invoice in. Defaults to that of `customer` if not specified.

- `customer` (string, optional)
  The identifier of the customer whose upcoming invoice you’re retrieving. If `automatic_tax` is enabled then one of `customer`, `customer_details`, `subscription`, or `schedule` must be set.

- `customer_account` (string, optional)
  The identifier of the account representing the customer whose upcoming invoice you’re retrieving. If `automatic_tax` is enabled then one of `customer`, `customer_account`, `customer_details`, `subscription`, or `schedule` must be set.

- `customer_details` (object, optional)
  Details about the customer you want to invoice or overrides for an existing customer. If `automatic_tax` is enabled then one of `customer`, `customer_details`, `subscription`, or `schedule` must be set.

  - `customer_details.address` (object, required if calculating taxes)
    The customer’s address. Learn about [country-specific requirements for calculating tax](https://docs.stripe.com/invoicing/taxes.md?dashboard-or-api=dashboard#set-up-customer).

    - `customer_details.address.city` (string, optional)
      City, district, suburb, town, or village.

    - `customer_details.address.country` (string, required for calculating taxes)
      Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

    - `customer_details.address.line1` (string, optional)
      Address line 1, such as the street, PO Box, or company name.

    - `customer_details.address.line2` (string, optional)
      Address line 2, such as the apartment, suite, unit, or building.

    - `customer_details.address.postal_code` (string, required for calculating taxes)
      ZIP or postal code.

    - `customer_details.address.state` (string, optional)
      State, county, province, or region ([ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2)).

  - `customer_details.shipping` (object, optional)
    The customer’s shipping information. Appears on invoices emailed to this customer.

    - `customer_details.shipping.address` (object, required)
      Customer shipping address.

      - `customer_details.shipping.address.city` (string, optional)
        City, district, suburb, town, or village.

      - `customer_details.shipping.address.country` (string, optional)
        A freeform text field for the country. However, in order to activate some tax features, the format should be a two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

      - `customer_details.shipping.address.line1` (string, optional)
        Address line 1, such as the street, PO Box, or company name.

      - `customer_details.shipping.address.line2` (string, optional)
        Address line 2, such as the apartment, suite, unit, or building.

      - `customer_details.shipping.address.postal_code` (string, optional)
        ZIP or postal code.

      - `customer_details.shipping.address.state` (string, optional)
        State, county, province, or region ([ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2)).

    - `customer_details.shipping.name` (string, required)
      Customer name.

    - `customer_details.shipping.phone` (string, optional)
      Customer phone (including extension).

  - `customer_details.tax` (object, optional)
    Tax details about the customer.

    - `customer_details.tax.ip_address` (string, optional)
      A recent IP address of the customer used for tax reporting and tax location inference. Stripe recommends updating the IP address when a new PaymentMethod is attached or the address field on the customer is updated. We recommend against updating this field more frequently since it could result in unexpected tax location/reporting outcomes.

  - `customer_details.tax_exempt` (enum, optional)
    The customer’s tax exemption. One of `none`, `exempt`, or `reverse`.
Possible enum values:
    - `exempt`
    - `none`
    - `reverse`

  - `customer_details.tax_ids` (array of objects, optional)
    The customer’s tax IDs.

    - `customer_details.tax_ids.type` (string, required)
      Type of the tax ID, one of `ad_nrt`, `ae_trn`, `al_tin`, `am_tin`, `ao_tin`, `ar_cuit`, `au_abn`, `au_arn`, `aw_tin`, `az_tin`, `ba_tin`, `bb_tin`, `bd_bin`, `bf_ifu`, `bg_uic`, `bh_vat`, `bj_ifu`, `bo_tin`, `br_cnpj`, `br_cpf`, `bs_tin`, `by_tin`, `ca_bn`, `ca_gst_hst`, `ca_pst_bc`, `ca_pst_mb`, `ca_pst_sk`, `ca_qst`, `cd_nif`, `ch_uid`, `ch_vat`, `cl_tin`, `cm_niu`, `cn_tin`, `co_nit`, `cr_tin`, `cv_nif`, `de_stn`, `do_rcn`, `ec_ruc`, `eg_tin`, `es_cif`, `et_tin`, `eu_oss_vat`, `eu_vat`, `gb_vat`, `ge_vat`, `gn_nif`, `hk_br`, `hr_oib`, `hu_tin`, `id_npwp`, `il_vat`, `in_gst`, `is_vat`, `jp_cn`, `jp_rn`, `jp_trn`, `ke_pin`, `kg_tin`, `kh_tin`, `kr_brn`, `kz_bin`, `la_tin`, `li_uid`, `li_vat`, `ma_vat`, `md_vat`, `me_pib`, `mk_vat`, `mr_nif`, `mx_rfc`, `my_frp`, `my_itn`, `my_sst`, `ng_tin`, `no_vat`, `no_voec`, `np_pan`, `nz_gst`, `om_vat`, `pe_ruc`, `ph_tin`, `ro_tin`, `rs_pib`, `ru_inn`, `ru_kpp`, `sa_vat`, `sg_gst`, `sg_uen`, `si_tin`, `sn_ninea`, `sr_fin`, `sv_nit`, `th_vat`, `tj_tin`, `tr_tin`, `tw_vat`, `tz_vat`, `ua_vat`, `ug_tin`, `us_ein`, `uy_ruc`, `uz_tin`, `uz_vat`, `ve_rif`, `vn_tin`, `za_vat`, `zm_tin`, or `zw_tin`

    - `customer_details.tax_ids.value` (string, required)
      Value of the tax ID.

- `discounts` (array of objects, optional)
  The coupons to redeem into discounts for the invoice preview. If not specified, inherits the discount from the subscription or customer. This works for both coupons directly applied to an invoice and coupons applied to a subscription. Pass an empty string to avoid inheriting any discounts.

  - `discounts.coupon` (string, optional)
    ID of the coupon to create a new discount for.

  - `discounts.discount` (string, optional)
    ID of an existing discount on the object (or one of its ancestors) to reuse.

  - `discounts.promotion_code` (string, optional)
    ID of the promotion code to create a new discount for.

- `invoice_items` (array of objects, optional)
  List of invoice items to add or update in the upcoming invoice preview (up to 250).

  - `invoice_items.amount` (integer, optional)
    The integer amount in cents of previewed invoice item.

  - `invoice_items.currency` (enum, optional)
    Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies). Only applicable to new invoice items.

  - `invoice_items.description` (string, optional)
    An arbitrary string which you can attach to the invoice item. The description is displayed in the invoice for easy tracking.

  - `invoice_items.discountable` (boolean, optional)
    Explicitly controls whether discounts apply to this invoice item. Defaults to true, except for negative invoice items.

  - `invoice_items.discounts` (array of objects, optional)
    The coupons to redeem into discounts for the invoice item in the preview.

    - `invoice_items.discounts.coupon` (string, optional)
      ID of the coupon to create a new discount for.

    - `invoice_items.discounts.discount` (string, optional)
      ID of an existing discount on the object (or one of its ancestors) to reuse.

    - `invoice_items.discounts.promotion_code` (string, optional)
      ID of the promotion code to create a new discount for.

  - `invoice_items.invoiceitem` (string, optional)
    The ID of the invoice item to update in preview. If not specified, a new invoice item will be added to the preview of the upcoming invoice.

  - `invoice_items.metadata` (object, optional)
    Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.

  - `invoice_items.period` (object, optional)
    The period associated with this invoice item. When set to different values, the period will be rendered on the invoice. If you have [Stripe Revenue Recognition](https://docs.stripe.com/docs/revenue-recognition.md) enabled, the period will be used to recognize and defer revenue. See the [Revenue Recognition documentation](https://docs.stripe.com/docs/revenue-recognition/methodology/subscriptions-and-invoicing.md) for details.

    - `invoice_items.period.end` (timestamp, required)
      The end of the period, which must be greater than or equal to the start. This value is inclusive.

    - `invoice_items.period.start` (timestamp, required)
      The start of the period. This value is inclusive.

  - `invoice_items.price` (string, optional)
    The ID of the price object. One of `price` or `price_data` is required.

  - `invoice_items.price_data` (object, optional)
    Data used to generate a new [Price](https://docs.stripe.com/docs/api/prices.md) object inline. One of `price` or `price_data` is required.

    - `invoice_items.price_data.currency` (enum, required)
      Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

    - `invoice_items.price_data.product` (string, required)
      The ID of the [Product](https://docs.stripe.com/api/products.md) that this [Price](https://docs.stripe.com/api/prices.md) will belong to.

    - `invoice_items.price_data.tax_behavior` (enum, recommended if calculating taxes)
      Only required if a [default tax behavior](https://docs.stripe.com/docs/tax/products-prices-tax-categories-tax-behavior.md#setting-a-default-tax-behavior-\(recommended\)) was not provided in the Stripe Tax settings. Specifies whether the price is considered inclusive of taxes or exclusive of taxes. One of `inclusive`, `exclusive`, or `unspecified`. Once specified as either `inclusive` or `exclusive`, it cannot be changed.
Possible enum values:
      - `exclusive`
      - `inclusive`
      - `unspecified`

    - `invoice_items.price_data.unit_amount` (integer, optional)
      A positive integer in cents (or 0 for a free price) representing how much to charge.

    - `invoice_items.price_data.unit_amount_decimal` (string, required conditionally)
      Same as `unit_amount`, but accepts a decimal value in cents with at most 12 decimal places. Only one of `unit_amount` and `unit_amount_decimal` can be set.

  - `invoice_items.quantity` (integer, optional)
    Non-negative integer. The quantity of units for the invoice item.

  - `invoice_items.tax_behavior` (enum, recommended if calculating taxes)
    Only required if a [default tax behavior](https://docs.stripe.com/docs/tax/products-prices-tax-categories-tax-behavior.md#setting-a-default-tax-behavior-\(recommended\)) was not provided in the Stripe Tax settings. Specifies whether the price is considered inclusive of taxes or exclusive of taxes. One of `inclusive`, `exclusive`, or `unspecified`. Once specified as either `inclusive` or `exclusive`, it cannot be changed.
Possible enum values:
    - `exclusive`
    - `inclusive`
    - `unspecified`

  - `invoice_items.tax_code` (string, recommended if calculating taxes)
    A [tax code](https://docs.stripe.com/docs/tax/tax-categories.md) ID.

  - `invoice_items.tax_rates` (array of strings, optional)
    The tax rates that apply to the item. When set, any `default_tax_rates` do not apply to this item.

  - `invoice_items.unit_amount` (integer, optional)
    The integer unit amount in cents of the charge to be applied to the upcoming invoice. This unit_amount will be multiplied by the quantity to get the full amount. If you want to apply a credit to the customer’s account, pass a negative unit_amount.

  - `invoice_items.unit_amount_decimal` (string, optional)
    Same as `unit_amount`, but accepts a decimal value in cents with at most 12 decimal places. Only one of `unit_amount` and `unit_amount_decimal` can be set.

- `issuer` (object, optional)
  The connected account that issues the invoice. The invoice is presented with the branding and support information of the specified account.

  - `issuer.type` (enum, required)
    Type of the account referenced in the request.
Possible enum values:
    - `account`
      Indicates that the account being referenced is a connected account which is different from the account making the API request but related to it.

    - `self`
      Indicates that the account being referenced is the account making the API request.

  - `issuer.account` (string, required only if type is account)
    The connected account being referenced when `type` is `account`.

- `on_behalf_of` (string, optional)
  The account (if any) for which the funds of the invoice payment are intended. If set, the invoice will be presented with the branding and support information of the specified account. See the [Invoices with Connect](https://docs.stripe.com/docs/billing/invoices/connect.md) documentation for details.

- `preview_mode` (enum, optional)
  Customizes the types of values to include when calculating the invoice. Defaults to `next` if unspecified.
Possible enum values:
  - `next`
    Will calculate the next invoice for the customer or subscription, factoring in all one-time and recurring items.

  - `recurring`
    Will calculate an invoice that is an estimate of the subscription’s long-term recurring bill. The invoice lines will only include recurring subscription items, taxes, and coupons with `duration=repeating` or `duration=forever`.

    To calculate a recurring estimate, you must provide at least one of `subscription` or `subscription_details.items`. Prorations, subscription cancellations, and trials are not supported with recurring estimates.

- `schedule` (string, optional)
  The identifier of the schedule whose upcoming invoice you’d like to retrieve. Cannot be used with subscription or subscription fields.

- `schedule_details` (object, optional)
  The schedule creation or modification params to apply as a preview. Cannot be used with `subscription` or `subscription_` prefixed fields.

  - `schedule_details.billing_mode` (object, optional)
    Controls how prorations and invoices for subscriptions are calculated and orchestrated.

    - `schedule_details.billing_mode.type` (enum, required)
      Controls the calculation and orchestration of prorations and invoices for subscriptions. If no value is passed, the default is `flexible`.
Possible enum values:
      - `classic`
        Calculations for subscriptions and invoices are based on legacy defaults.

      - `flexible`
        Supports more flexible calculation and orchestration options for subscriptions and invoices.

    - `schedule_details.billing_mode.flexible` (object, optional)
      Configure behavior for flexible billing mode.

      - `schedule_details.billing_mode.flexible.proration_discounts` (enum, optional)
        Controls how invoices and invoice items display proration amounts and discount amounts.
Possible enum values:
        - `included`
          Amounts are net of discounts, and discount amounts are zero.

        - `itemized`
          Amounts are gross of discounts, and discount amounts are accurate.

  - `schedule_details.end_behavior` (enum, optional)
    Behavior of the subscription schedule and underlying subscription when it ends. Possible values are `release` or `cancel` with the default being `release`. `release` will end the subscription schedule and keep the underlying subscription running. `cancel` will end the subscription schedule and cancel the underlying subscription.
Possible enum values:
    - `cancel`
    - `release`

  - `schedule_details.phases` (array of objects, optional)
    List representing phases of the subscription schedule. Each phase can be customized to have different durations, plans, and coupons. If there are multiple phases, the `end_date` of one phase will always equal the `start_date` of the next phase.

    - `schedule_details.phases.items` (array of objects, required)
      List of configuration items, each with an attached price, to apply during this phase of the subscription schedule.

      - `schedule_details.phases.items.billing_thresholds` (object, optional)
        Define thresholds at which an invoice will be sent, and the subscription advanced to a new billing period. Pass an empty string to remove previously-defined thresholds.

        - `schedule_details.phases.items.billing_thresholds.usage_gte` (integer, required)
          Number of units that meets the billing threshold to advance the subscription to a new billing period (e.g., it takes 10 $5 units to meet a $50 [monetary threshold](https://docs.stripe.com/docs/api/subscriptions/update.md#update_subscription-billing_thresholds-amount_gte))

      - `schedule_details.phases.items.discounts` (array of objects, optional)
        The coupons to redeem into discounts for the subscription item.

        - `schedule_details.phases.items.discounts.coupon` (string, optional)
          ID of the coupon to create a new discount for.

        - `schedule_details.phases.items.discounts.discount` (string, optional)
          ID of an existing discount on the object (or one of its ancestors) to reuse.

        - `schedule_details.phases.items.discounts.promotion_code` (string, optional)
          ID of the promotion code to create a new discount for.

      - `schedule_details.phases.items.metadata` (object, optional)
        Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to a configuration item. Metadata on a configuration item will update the underlying subscription item’s `metadata` when the phase is entered, adding new keys and replacing existing keys. Individual keys in the subscription item’s `metadata` can be unset by posting an empty value to them in the configuration item’s `metadata`. To unset all keys in the subscription item’s `metadata`, update the subscription item directly or unset every key individually from the configuration item’s `metadata`.

      - `schedule_details.phases.items.price` (string, optional)
        The ID of the price object.

      - `schedule_details.phases.items.price_data` (object, optional)
        Data used to generate a new [Price](https://docs.stripe.com/docs/api/prices.md) object inline.

        - `schedule_details.phases.items.price_data.currency` (enum, required)
          Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

        - `schedule_details.phases.items.price_data.product` (string, required)
          The ID of the [Product](https://docs.stripe.com/api/products.md) that this [Price](https://docs.stripe.com/api/prices.md) will belong to.

        - `schedule_details.phases.items.price_data.recurring` (object, required)
          The recurring components of a price such as `interval` and `interval_count`.

          - `schedule_details.phases.items.price_data.recurring.interval` (enum, required)
            Specifies billing frequency. Either `day`, `week`, `month` or `year`.
Possible enum values:
            - `day`
            - `month`
            - `week`
            - `year`

          - `schedule_details.phases.items.price_data.recurring.interval_count` (integer, optional)
            The number of intervals between subscription billings. For example, `interval=month` and `interval_count=3` bills every 3 months. Maximum of three years interval allowed (3 years, 36 months, or 156 weeks).

        - `schedule_details.phases.items.price_data.tax_behavior` (enum, recommended if calculating taxes)
          Only required if a [default tax behavior](https://docs.stripe.com/docs/tax/products-prices-tax-categories-tax-behavior.md#setting-a-default-tax-behavior-\(recommended\)) was not provided in the Stripe Tax settings. Specifies whether the price is considered inclusive of taxes or exclusive of taxes. One of `inclusive`, `exclusive`, or `unspecified`. Once specified as either `inclusive` or `exclusive`, it cannot be changed.
Possible enum values:
          - `exclusive`
          - `inclusive`
          - `unspecified`

        - `schedule_details.phases.items.price_data.unit_amount` (integer, optional)
          A positive integer in cents (or 0 for a free price) representing how much to charge.

        - `schedule_details.phases.items.price_data.unit_amount_decimal` (string, required conditionally)
          Same as `unit_amount`, but accepts a decimal value in cents with at most 12 decimal places. Only one of `unit_amount` and `unit_amount_decimal` can be set.

      - `schedule_details.phases.items.quantity` (integer, optional)
        Quantity for the given price. Can be set only if the price’s `usage_type` is `licensed` and not `metered`.

      - `schedule_details.phases.items.tax_rates` (array of strings, optional)
        A list of [Tax Rate](https://docs.stripe.com/docs/api/tax_rates.md) ids. These Tax Rates will override the [`default_tax_rates`](https://docs.stripe.com/docs/api/subscriptions/create.md#create_subscription-default_tax_rates) on the Subscription. When updating, pass an empty string to remove previously-defined tax rates.

    - `schedule_details.phases.add_invoice_items` (array of objects, optional)
      A list of prices and quantities that will generate invoice items appended to the next invoice for this phase. You may pass up to 20 items.

      - `schedule_details.phases.add_invoice_items.discounts` (array of objects, optional)
        The coupons to redeem into discounts for the item.

        - `schedule_details.phases.add_invoice_items.discounts.coupon` (string, optional)
          ID of the coupon to create a new discount for.

        - `schedule_details.phases.add_invoice_items.discounts.discount` (string, optional)
          ID of an existing discount on the object (or one of its ancestors) to reuse.

        - `schedule_details.phases.add_invoice_items.discounts.promotion_code` (string, optional)
          ID of the promotion code to create a new discount for.

      - `schedule_details.phases.add_invoice_items.metadata` (object, optional)
        Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.

      - `schedule_details.phases.add_invoice_items.period` (object, optional)
        The period associated with this invoice item. If not set, `period.start.type` defaults to `max_item_period_start` and `period.end.type` defaults to `min_item_period_end`.

        - `schedule_details.phases.add_invoice_items.period.end` (object, required)
          End of the invoice item period.

          - `schedule_details.phases.add_invoice_items.period.end.type` (enum, required)
            Select how to calculate the end of the invoice item period.
Possible enum values:
            - `min_item_period_end`
              The minimum `current_period_end` of all underlying subscription items whose periods overlap this phase

            - `phase_end`
              End of the phase

            - `timestamp`
              Custom timestamp to use for the end of the invoice item period

          - `schedule_details.phases.add_invoice_items.period.end.timestamp` (timestamp, optional)
            A precise Unix timestamp for the end of the invoice item period. Must be greater than or equal to `period.start`.

        - `schedule_details.phases.add_invoice_items.period.start` (object, required)
          Start of the invoice item period.

          - `schedule_details.phases.add_invoice_items.period.start.type` (enum, required)
            Select how to calculate the start of the invoice item period.
Possible enum values:
            - `max_item_period_start`
              The maximum `current_period_start` of all underlying subscription items whose periods overlap this phase

            - `phase_start`
              Start of the phase

            - `timestamp`
              Custom timestamp to use for the start of the invoice item period

          - `schedule_details.phases.add_invoice_items.period.start.timestamp` (timestamp, optional)
            A precise Unix timestamp for the start of the invoice item period. Must be less than or equal to `period.end`.

      - `schedule_details.phases.add_invoice_items.price` (string, optional)
        The ID of the price object. One of `price` or `price_data` is required.

      - `schedule_details.phases.add_invoice_items.price_data` (object, optional)
        Data used to generate a new [Price](https://docs.stripe.com/docs/api/prices.md) object inline. One of `price` or `price_data` is required.

        - `schedule_details.phases.add_invoice_items.price_data.currency` (enum, required)
          Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

        - `schedule_details.phases.add_invoice_items.price_data.product` (string, required)
          The ID of the [Product](https://docs.stripe.com/api/products.md) that this [Price](https://docs.stripe.com/api/prices.md) will belong to.

        - `schedule_details.phases.add_invoice_items.price_data.tax_behavior` (enum, recommended if calculating taxes)
          Only required if a [default tax behavior](https://docs.stripe.com/docs/tax/products-prices-tax-categories-tax-behavior.md#setting-a-default-tax-behavior-\(recommended\)) was not provided in the Stripe Tax settings. Specifies whether the price is considered inclusive of taxes or exclusive of taxes. One of `inclusive`, `exclusive`, or `unspecified`. Once specified as either `inclusive` or `exclusive`, it cannot be changed.
Possible enum values:
          - `exclusive`
          - `inclusive`
          - `unspecified`

        - `schedule_details.phases.add_invoice_items.price_data.unit_amount` (integer, optional)
          A positive integer in cents (or 0 for a free price) representing how much to charge or a negative integer representing the amount to credit to the customer.

        - `schedule_details.phases.add_invoice_items.price_data.unit_amount_decimal` (string, required conditionally)
          Same as `unit_amount`, but accepts a decimal value in cents with at most 12 decimal places. Only one of `unit_amount` and `unit_amount_decimal` can be set.

      - `schedule_details.phases.add_invoice_items.quantity` (integer, optional)
        Quantity for this item. Defaults to 1.

      - `schedule_details.phases.add_invoice_items.tax_rates` (array of strings, optional)
        The tax rates which apply to the item. When set, the `default_tax_rates` do not apply to this item.

    - `schedule_details.phases.application_fee_percent` (float, optional)
      A non-negative decimal between 0 and 100, with at most two decimal places. This represents the percentage of the subscription invoice total that will be transferred to the application owner’s Stripe account. The request must be made by a platform account on a connected account in order to set an application fee percentage. For more information, see the application fees [documentation](https://stripe.com/docs/connect/subscriptions#collecting-fees-on-subscriptions).

    - `schedule_details.phases.automatic_tax` (object, optional)
      Automatic tax settings for this phase.

      - `schedule_details.phases.automatic_tax.enabled` (boolean, required)
        Enabled automatic tax calculation which will automatically compute tax rates on all invoices generated by the subscription.

      - `schedule_details.phases.automatic_tax.liability` (object, optional)
        The account that’s liable for tax. If set, the business address and tax registrations required to perform the tax calculation are loaded from this account. The tax transaction is returned in the report of the connected account.

        - `schedule_details.phases.automatic_tax.liability.type` (enum, required)
          Type of the account referenced in the request.
Possible enum values:
          - `account`
            Indicates that the account being referenced is a connected account which is different from the account making the API request but related to it.

          - `self`
            Indicates that the account being referenced is the account making the API request.

        - `schedule_details.phases.automatic_tax.liability.account` (string, required only if type is account)
          The connected account being referenced when `type` is `account`.

    - `schedule_details.phases.billing_cycle_anchor` (enum, optional)
      Can be set to `phase_start` to set the anchor to the start of the phase or `automatic` to automatically change it if needed. Cannot be set to `phase_start` if this phase specifies a trial. For more information, see the billing cycle [documentation](https://docs.stripe.com/docs/billing/subscriptions/billing-cycle.md).
Possible enum values:
      - `automatic`
      - `phase_start`

    - `schedule_details.phases.billing_thresholds` (object, optional)
      Define thresholds at which an invoice will be sent, and the subscription advanced to a new billing period. Pass an empty string to remove previously-defined thresholds.

      - `schedule_details.phases.billing_thresholds.amount_gte` (integer, optional)
        Monetary threshold that triggers the subscription to advance to a new billing period

      - `schedule_details.phases.billing_thresholds.reset_billing_cycle_anchor` (boolean, optional)
        Indicates if the `billing_cycle_anchor` should be reset when a threshold is reached. If true, `billing_cycle_anchor` will be updated to the date/time the threshold was last reached; otherwise, the value will remain unchanged.

    - `schedule_details.phases.collection_method` (enum, optional)
      Either `charge_automatically`, or `send_invoice`. When charging automatically, Stripe will attempt to pay the underlying subscription at the end of each billing cycle using the default source attached to the customer. When sending an invoice, Stripe will email your customer an invoice with payment instructions and mark the subscription as `active`. Defaults to `charge_automatically` on creation.
Possible enum values:
      - `charge_automatically`
      - `send_invoice`

    - `schedule_details.phases.default_payment_method` (string, optional)
      ID of the default payment method for the subscription schedule. It must belong to the customer associated with the subscription schedule. If not set, invoices will use the default payment method in the customer’s invoice settings.

    - `schedule_details.phases.default_tax_rates` (array of strings, optional)
      A list of [Tax Rate](https://docs.stripe.com/docs/api/tax_rates.md) ids. These Tax Rates will set the Subscription’s [`default_tax_rates`](https://docs.stripe.com/docs/api/subscriptions/create.md#create_subscription-default_tax_rates), which means they will be the Invoice’s [`default_tax_rates`](https://docs.stripe.com/docs/api/invoices/create.md#create_invoice-default_tax_rates) for any Invoices issued by the Subscription during this Phase.

    - `schedule_details.phases.description` (string, optional)
      Subscription description, meant to be displayable to the customer. Use this field to optionally store an explanation of the subscription for rendering in Stripe surfaces and certain local payment methods UIs.

      The maximum length is 500 characters.

    - `schedule_details.phases.discounts` (array of objects, optional)
      The coupons to redeem into discounts for the schedule phase. If not specified, inherits the discount from the subscription’s customer. Pass an empty string to avoid inheriting any discounts.

      - `schedule_details.phases.discounts.coupon` (string, optional)
        ID of the coupon to create a new discount for.

      - `schedule_details.phases.discounts.discount` (string, optional)
        ID of an existing discount on the object (or one of its ancestors) to reuse.

      - `schedule_details.phases.discounts.promotion_code` (string, optional)
        ID of the promotion code to create a new discount for.

    - `schedule_details.phases.duration` (object, optional)
      The number of intervals the phase should last. If set, `end_date` must not be set.

      - `schedule_details.phases.duration.interval` (enum, required)
        Specifies phase duration. Either `day`, `week`, `month` or `year`.
Possible enum values:
        - `day`
        - `month`
        - `week`
        - `year`

      - `schedule_details.phases.duration.interval_count` (integer, optional)
        The multiplier applied to the interval.

    - `schedule_details.phases.end_date` (timestamp | string, optional)
      The date at which this phase of the subscription schedule ends. If set, `duration` must not be set.

    - `schedule_details.phases.invoice_settings` (object, optional)
      All invoices will be billed using the specified settings.

      - `schedule_details.phases.invoice_settings.account_tax_ids` (array of strings, optional)
        The account tax IDs associated with this phase of the subscription schedule. Will be set on invoices generated by this phase of the subscription schedule.

      - `schedule_details.phases.invoice_settings.days_until_due` (integer, optional)
        Number of days within which a customer must pay invoices generated by this subscription schedule. This value will be `null` for subscription schedules where `billing=charge_automatically`.

      - `schedule_details.phases.invoice_settings.issuer` (object, optional)
        The connected account that issues the invoice. The invoice is presented with the branding and support information of the specified account.

        - `schedule_details.phases.invoice_settings.issuer.type` (enum, required)
          Type of the account referenced in the request.
Possible enum values:
          - `account`
            Indicates that the account being referenced is a connected account which is different from the account making the API request but related to it.

          - `self`
            Indicates that the account being referenced is the account making the API request.

        - `schedule_details.phases.invoice_settings.issuer.account` (string, required only if type is account)
          The connected account being referenced when `type` is `account`.

    - `schedule_details.phases.metadata` (object, optional)
      Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to a phase. Metadata on a schedule’s phase will update the underlying subscription’s `metadata` when the phase is entered, adding new keys and replacing existing keys in the subscription’s `metadata`. Individual keys in the subscription’s `metadata` can be unset by posting an empty value to them in the phase’s `metadata`. To unset all keys in the subscription’s `metadata`, update the subscription directly or unset every key individually from the phase’s `metadata`.

    - `schedule_details.phases.on_behalf_of` (string, optional)
      The account on behalf of which to charge, for each of the associated subscription’s invoices.

    - `schedule_details.phases.proration_behavior` (enum, optional)
      Controls whether the subscription schedule should create [prorations](https://docs.stripe.com/docs/billing/subscriptions/prorations.md) when transitioning to this phase if there is a difference in billing configuration. It’s different from the request-level [proration_behavior](https://docs.stripe.com/docs/api/subscription_schedules/update.md#update_subscription_schedule-proration_behavior) parameter which controls what happens if the update request affects the billing configuration (item price, quantity, etc.) of the current phase.
Possible enum values:
      - `always_invoice`
        Prorate changes, and force an invoice to be immediately created for any prorations.

      - `create_prorations`
        Prorate changes, but leave any prorations as pending invoice items to be picked up on the customer’s next invoice.

      - `none`
        Does not create any prorations.

    - `schedule_details.phases.start_date` (timestamp | string, optional)
      The date at which this phase of the subscription schedule starts or `now`. Must be set on the first phase.

    - `schedule_details.phases.transfer_data` (object, optional)
      The data with which to automatically create a Transfer for each of the associated subscription’s invoices.

      - `schedule_details.phases.transfer_data.destination` (string, required)
        ID of an existing, connected Stripe account.

      - `schedule_details.phases.transfer_data.amount_percent` (float, optional)
        A non-negative decimal between 0 and 100, with at most two decimal places. This represents the percentage of the subscription invoice total that will be transferred to the destination account. By default, the entire amount is transferred to the destination.

    - `schedule_details.phases.trial` (boolean, optional)
      If set to true the entire phase is counted as a trial and the customer will not be charged for any fees.

    - `schedule_details.phases.trial_end` (timestamp | string, optional)
      Sets the phase to trialing from the start date to this date. Must be before the phase end date, can not be combined with `trial`

  - `schedule_details.proration_behavior` (enum, optional)
    In cases where the `schedule_details` params update the currently active phase, specifies if and how to prorate at the time of the request.
Possible enum values:
    - `always_invoice`
      Prorate changes, and force an invoice to be created for those prorations instead of leaving the prorations pending.

    - `create_prorations`
      Prorate changes, but leave any prorations as pending invoice items to be picked up on the customer’s next invoice.

    - `none`
      Does not create any prorations.

- `subscription` (string, optional)
  The identifier of the subscription for which you’d like to retrieve the upcoming invoice. If not provided, but a `subscription_details.items` is provided, you will preview creating a subscription with those items. If neither `subscription` nor `subscription_details.items` is provided, you will retrieve the next upcoming invoice from among the customer’s subscriptions.

- `subscription_details` (object, optional)
  The subscription creation or modification params to apply as a preview. Cannot be used with `schedule` or `schedule_details` fields.

  - `subscription_details.billing_cycle_anchor` (string | timestamp, optional)
    For new subscriptions, a future timestamp to anchor the subscription’s [billing cycle](https://docs.stripe.com/docs/subscriptions/billing-cycle.md). This is used to determine the date of the first full invoice, and, for plans with `month` or `year` intervals, the day of the month for subsequent invoices. For existing subscriptions, the value can only be set to `now` or `unchanged`.

  - `subscription_details.billing_mode` (object, optional)
    Controls how prorations and invoices for subscriptions are calculated and orchestrated.

    - `subscription_details.billing_mode.type` (enum, required)
      Controls the calculation and orchestration of prorations and invoices for subscriptions. If no value is passed, the default is `flexible`.
Possible enum values:
      - `classic`
        Calculations for subscriptions and invoices are based on legacy defaults.

      - `flexible`
        Supports more flexible calculation and orchestration options for subscriptions and invoices.

    - `subscription_details.billing_mode.flexible` (object, optional)
      Configure behavior for flexible billing mode.

      - `subscription_details.billing_mode.flexible.proration_discounts` (enum, optional)
        Controls how invoices and invoice items display proration amounts and discount amounts.
Possible enum values:
        - `included`
          Amounts are net of discounts, and discount amounts are zero.

        - `itemized`
          Amounts are gross of discounts, and discount amounts are accurate.

  - `subscription_details.cancel_at` (timestamp | enum, optional)
    A timestamp at which the subscription should cancel. If set to a date before the current period ends, this will cause a proration if prorations have been enabled using `proration_behavior`. If set during a future period, this will always cause a proration for that period.
Possible enum values:
    - `max_period_end`
      Set subscription to cancel at the latest end date among all subscription items’ current billing periods.

    - `min_period_end`
      Set subscription to cancel at the earliest end date among all subscription items’ current billing periods.

  - `subscription_details.cancel_at_period_end` (boolean, optional)
    Indicate whether this subscription should cancel at the end of the current period (`current_period_end`). Defaults to `false`.

  - `subscription_details.cancel_now` (boolean, optional)
    This simulates the subscription being canceled or expired immediately.

  - `subscription_details.default_tax_rates` (array of strings, optional)
    If provided, the invoice returned will preview updating or creating a subscription with these default tax rates. The default tax rates will apply to any line item that does not have `tax_rates` set.

  - `subscription_details.items` (array of objects, optional)
    A list of up to 20 subscription items, each with an attached price.

    - `subscription_details.items.billing_thresholds` (object, optional)
      Define thresholds at which an invoice will be sent, and the subscription advanced to a new billing period. Pass an empty string to remove previously-defined thresholds.

      - `subscription_details.items.billing_thresholds.usage_gte` (integer, required)
        Number of units that meets the billing threshold to advance the subscription to a new billing period (e.g., it takes 10 $5 units to meet a $50 [monetary threshold](https://docs.stripe.com/docs/api/subscriptions/update.md#update_subscription-billing_thresholds-amount_gte))

    - `subscription_details.items.clear_usage` (boolean, optional)
      Delete all usage for a given subscription item. You must pass this when deleting a usage records subscription item. `clear_usage` has no effect if the plan has a billing meter attached.

    - `subscription_details.items.deleted` (boolean, optional)
      A flag that, if set to `true`, will delete the specified item.

    - `subscription_details.items.discounts` (array of objects, optional)
      The coupons to redeem into discounts for the subscription item.

      - `subscription_details.items.discounts.coupon` (string, optional)
        ID of the coupon to create a new discount for.

      - `subscription_details.items.discounts.discount` (string, optional)
        ID of an existing discount on the object (or one of its ancestors) to reuse.

      - `subscription_details.items.discounts.promotion_code` (string, optional)
        ID of the promotion code to create a new discount for.

    - `subscription_details.items.id` (string, optional)
      Subscription item to update.

    - `subscription_details.items.metadata` (object, optional)
      Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.

    - `subscription_details.items.price` (string, optional)
      The ID of the price object. One of `price` or `price_data` is required. When changing a subscription item’s price, `quantity` is set to 1 unless a `quantity` parameter is provided.

    - `subscription_details.items.price_data` (object, optional)
      Data used to generate a new [Price](https://docs.stripe.com/docs/api/prices.md) object inline. One of `price` or `price_data` is required.

      - `subscription_details.items.price_data.currency` (enum, required)
        Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

      - `subscription_details.items.price_data.product` (string, required)
        The ID of the [Product](https://docs.stripe.com/api/products.md) that this [Price](https://docs.stripe.com/api/prices.md) will belong to.

      - `subscription_details.items.price_data.recurring` (object, required)
        The recurring components of a price such as `interval` and `interval_count`.

        - `subscription_details.items.price_data.recurring.interval` (enum, required)
          Specifies billing frequency. Either `day`, `week`, `month` or `year`.
Possible enum values:
          - `day`
          - `month`
          - `week`
          - `year`

        - `subscription_details.items.price_data.recurring.interval_count` (integer, optional)
          The number of intervals between subscription billings. For example, `interval=month` and `interval_count=3` bills every 3 months. Maximum of three years interval allowed (3 years, 36 months, or 156 weeks).

      - `subscription_details.items.price_data.tax_behavior` (enum, recommended if calculating taxes)
        Only required if a [default tax behavior](https://docs.stripe.com/docs/tax/products-prices-tax-categories-tax-behavior.md#setting-a-default-tax-behavior-\(recommended\)) was not provided in the Stripe Tax settings. Specifies whether the price is considered inclusive of taxes or exclusive of taxes. One of `inclusive`, `exclusive`, or `unspecified`. Once specified as either `inclusive` or `exclusive`, it cannot be changed.
Possible enum values:
        - `exclusive`
        - `inclusive`
        - `unspecified`

      - `subscription_details.items.price_data.unit_amount` (integer, optional)
        A positive integer in cents (or 0 for a free price) representing how much to charge.

      - `subscription_details.items.price_data.unit_amount_decimal` (string, required conditionally)
        Same as `unit_amount`, but accepts a decimal value in cents with at most 12 decimal places. Only one of `unit_amount` and `unit_amount_decimal` can be set.

    - `subscription_details.items.quantity` (integer, optional)
      Quantity for this item.

    - `subscription_details.items.tax_rates` (array of strings, optional)
      A list of [Tax Rate](https://docs.stripe.com/docs/api/tax_rates.md) ids. These Tax Rates will override the [`default_tax_rates`](https://docs.stripe.com/docs/api/subscriptions/create.md#create_subscription-default_tax_rates) on the Subscription. When updating, pass an empty string to remove previously-defined tax rates.

  - `subscription_details.proration_behavior` (enum, optional)
    Determines how to handle [prorations](https://docs.stripe.com/docs/billing/subscriptions/prorations.md) when the billing cycle changes (e.g., when switching plans, resetting `billing_cycle_anchor=now`, or starting a trial), or if an item’s `quantity` changes. The default value is `create_prorations`.
Possible enum values:
    - `always_invoice`
      Always invoice immediately for prorations.

    - `create_prorations`
      Will cause proration invoice items to be created when applicable. These proration items will only be invoiced immediately under [certain conditions](https://docs.stripe.com/docs/subscriptions/upgrading-downgrading.md#immediate-payment).

    - `none`
      Disable creating prorations in this request.

  - `subscription_details.proration_date` (timestamp, optional)
    If previewing an update to a subscription, and doing proration, `subscription_details.proration_date` forces the proration to be calculated as though the update was done at the specified time. The time given must be within the current subscription period and within the current phase of the schedule backing this subscription, if the schedule exists. If set, `subscription`, and one of `subscription_details.items`, or `subscription_details.trial_end` are required. Also, `subscription_details.proration_behavior` cannot be set to ‘none’.

  - `subscription_details.resume_at` (string, optional)
    For paused subscriptions, setting `subscription_details.resume_at` to `now` will preview the invoice that will be generated if the subscription is resumed.

  - `subscription_details.start_date` (timestamp, optional)
    Date a subscription is intended to start (can be future or past).

  - `subscription_details.trial_end` (string | timestamp, optional)
    If provided, the invoice returned will preview updating or creating a subscription with that trial end. If set, one of `subscription_details.items` or `subscription` is required.

```curl
curl https://api.stripe.com/v1/invoices/create_preview \
  -u "<<YOUR_SECRET_KEY>>" \
  -d customer=cus_NeZwdNtLEOXuvB
```

```cli
stripe invoices create_preview  \
  --customer=cus_NeZwdNtLEOXuvB
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

invoice = client.v1.invoices.create_preview({customer: 'cus_NeZwdNtLEOXuvB'})
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

invoice = client.v1.invoices.create_preview({"customer": "cus_NeZwdNtLEOXuvB"})
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$invoice = $stripe->invoices->createPreview(['customer' => 'cus_NeZwdNtLEOXuvB']);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

InvoiceCreatePreviewParams params =
  InvoiceCreatePreviewParams.builder().setCustomer("cus_NeZwdNtLEOXuvB").build();

Invoice invoice = client.v1().invoices().createPreview(params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const invoice = await stripe.invoices.createPreview({
  customer: 'cus_NeZwdNtLEOXuvB',
});
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.InvoiceCreatePreviewParams{
  Customer: stripe.String("cus_NeZwdNtLEOXuvB"),
}
result, err := sc.V1Invoices.CreatePreview(context.TODO(), params)
```

```dotnet
var options = new InvoiceCreatePreviewOptions { Customer = "cus_NeZwdNtLEOXuvB" };
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Invoices;
Invoice invoice = service.CreatePreview(options);
```

### Response

```json
{
  "id": "upcoming_in_1MtHbELkdIwHu7ixl4OzzPMv",
  "object": "invoice",
  "account_country": "US",
  "account_name": "Stripe Docs",
  "account_tax_ids": null,
  "amount_due": 0,
  "amount_paid": 0,
  "amount_overpaid": 0,
  "amount_remaining": 0,
  "amount_shipping": 0,
  "application": null,
  "application_fee_amount": null,
  "attempt_count": 0,
  "attempted": false,
  "auto_advance": false,
  "automatic_tax": {
    "enabled": false,
    "status": null
  },
  "billing_reason": "manual",
  "collection_method": "charge_automatically",
  "created": 1680644467,
  "currency": "usd",
  "custom_fields": null,
  "customer": "cus_NeZwdNtLEOXuvB",
  "customer_address": null,
  "customer_email": "jennyrosen@example.com",
  "customer_name": "Jenny Rosen",
  "customer_phone": null,
  "customer_shipping": null,
  "customer_tax_exempt": "none",
  "customer_tax_ids": [],
  "default_payment_method": null,
  "default_source": null,
  "default_tax_rates": [],
  "description": null,
  "discounts": [],
  "due_date": null,
  "ending_balance": null,
  "footer": null,
  "from_invoice": null,
  "hosted_invoice_url": null,
  "invoice_pdf": null,
  "last_finalization_error": null,
  "latest_revision": null,
  "lines": {
    "object": "list",
    "data": [],
    "has_more": false,
    "total_count": 0,
    "url": "/v1/invoices/in_1MtHbELkdIwHu7ixl4OzzPMv/lines"
  },
  "livemode": false,
  "metadata": {},
  "next_payment_attempt": null,
  "number": null,
  "on_behalf_of": null,
  "parent": null,
  "payment_settings": {
    "default_mandate": null,
    "payment_method_options": null,
    "payment_method_types": null
  },
  "period_end": 1680644467,
  "period_start": 1680644467,
  "post_payment_credit_notes_amount": 0,
  "pre_payment_credit_notes_amount": 0,
  "receipt_number": null,
  "shipping_cost": null,
  "shipping_details": null,
  "starting_balance": 0,
  "statement_descriptor": null,
  "status": "draft",
  "status_transitions": {
    "finalized_at": null,
    "marked_uncollectible_at": null,
    "paid_at": null,
    "voided_at": null
  },
  "subtotal": 0,
  "subtotal_excluding_tax": 0,
  "test_clock": null,
  "total": 0,
  "total_discount_amounts": [],
  "total_excluding_tax": 0,
  "total_taxes": [],
  "webhooks_delivered_at": 1680644467
}
```