# The Quote object

## Attributes

- `id` (string)
  Unique identifier for the object.

- `object` (string)
  String representing the object’s type. Objects of the same type share the same value.

- `amount_subtotal` (integer)
  Total before any discounts or taxes are applied.

- `amount_total` (integer)
  Total after discounts and taxes are applied.

- `application` (string, nullable)
  ID of the Connect Application that created the quote.

- `application_fee_amount` (integer, nullable)
  The amount of the application fee (if any) that will be requested to be applied to the payment and transferred to the application owner’s Stripe account. Only applicable if there are no line items with recurring prices on the quote.

- `application_fee_percent` (float, nullable)
  A non-negative decimal between 0 and 100, with at most two decimal places. This represents the percentage of the subscription invoice total that will be transferred to the application owner’s Stripe account. Only applicable if there are line items with recurring prices on the quote.

- `automatic_tax` (object)
  Settings for automatic tax lookup for this quote and resulting invoices and subscriptions.

  - `automatic_tax.enabled` (boolean)
    Automatically calculate taxes

  - `automatic_tax.liability` (object, nullable)
    The account that’s liable for tax. If set, the business address and tax registrations required to perform the tax calculation are loaded from this account. The tax transaction is returned in the report of the connected account.

    - `automatic_tax.liability.account` (string, nullable)
      The connected account being referenced when `type` is `account`.

    - `automatic_tax.liability.type` (enum)
      Type of the account referenced.
Possible enum values:
      - `account`
        Indicates that the account being referenced is a connected account which is different from the account making the API request but related to it.

      - `self`
        Indicates that the account being referenced is the account making the API request.

  - `automatic_tax.provider` (string, nullable)
    The tax provider powering automatic tax.

  - `automatic_tax.status` (enum, nullable)
    The status of the most recent automated tax calculation for this quote.
Possible enum values:
    - `complete`
      The automatic tax calculation was successful.

    - `failed`
      The tax calculation failed, please try again later.

    - `requires_location_inputs`
      The location details supplied on the customer aren’t valid or don’t provide enough location information to accurately determine tax rates for the customer.

- `collection_method` (enum)
  Either `charge_automatically`, or `send_invoice`. When charging automatically, Stripe will attempt to pay invoices at the end of the subscription cycle or on finalization using the default payment method attached to the subscription or customer. When sending an invoice, Stripe will email your customer an invoice with payment instructions and mark the subscription as `active`. Defaults to `charge_automatically`.
Possible enum values:
  - `charge_automatically`
  - `send_invoice`

- `computed` (object)
  The definitive totals and line items for the quote, computed based on your inputted line items as well as other configuration such as trials. Used for rendering the quote to your customer.

  - `computed.recurring` (object, nullable)
    The definitive totals and line items the customer will be charged on a recurring basis. Takes into account the line items with recurring prices and discounts with `duration=forever` coupons only. Defaults to `null` if no inputted line items with recurring prices.

    - `computed.recurring.amount_subtotal` (integer)
      Total before any discounts or taxes are applied.

    - `computed.recurring.amount_total` (integer)
      Total after discounts and taxes are applied.

    - `computed.recurring.interval` (enum)
      The frequency at which a subscription is billed. One of `day`, `week`, `month` or `year`.
Possible enum values:
      - `day`
      - `month`
      - `week`
      - `year`

    - `computed.recurring.interval_count` (integer)
      The number of intervals (specified in the `interval` attribute) between subscription billings. For example, `interval=month` and `interval_count=3` bills every 3 months.

    - `computed.recurring.total_details` (object)
      Tax and discount details for the computed total amount.

      - `computed.recurring.total_details.amount_discount` (integer)
        This is the sum of all the discounts.

      - `computed.recurring.total_details.amount_shipping` (integer, nullable)
        This is the sum of all the shipping amounts.

      - `computed.recurring.total_details.amount_tax` (integer)
        This is the sum of all the tax amounts.

      - `computed.recurring.total_details.breakdown` (object, nullable)
        Breakdown of individual tax and discount amounts that add up to the totals.

        - `computed.recurring.total_details.breakdown.discounts` (array of objects)
          The aggregated discounts.

          - `computed.recurring.total_details.breakdown.discounts.amount` (integer)
            The amount discounted.

          - `computed.recurring.total_details.breakdown.discounts.discount` (object)
            The discount applied.

            - `computed.recurring.total_details.breakdown.discounts.discount.id` (string)
              The ID of the discount object. Discounts cannot be fetched by ID. Use `expand[]=discounts` in API calls to expand discount IDs in an array.

            - `computed.recurring.total_details.breakdown.discounts.discount.object` (string)
              String representing the object’s type. Objects of the same type share the same value.

            - `computed.recurring.total_details.breakdown.discounts.discount.checkout_session` (string, nullable)
              The Checkout session that this coupon is applied to, if it is applied to a particular session in payment mode. Will not be present for subscription mode.

            - `computed.recurring.total_details.breakdown.discounts.discount.customer` (string, nullable)
              The ID of the customer associated with this discount.

            - `computed.recurring.total_details.breakdown.discounts.discount.customer_account` (string, nullable)
              The ID of the account representing the customer associated with this discount.

            - `computed.recurring.total_details.breakdown.discounts.discount.end` (timestamp, nullable)
              If the coupon has a duration of `repeating`, the date that this discount will end. If the coupon has a duration of `once` or `forever`, this attribute will be null.

            - `computed.recurring.total_details.breakdown.discounts.discount.invoice` (string, nullable)
              The invoice that the discount’s coupon was applied to, if it was applied directly to a particular invoice.

            - `computed.recurring.total_details.breakdown.discounts.discount.invoice_item` (string, nullable)
              The invoice item `id` (or invoice line item `id` for invoice line items of type=‘subscription’) that the discount’s coupon was applied to, if it was applied directly to a particular invoice item or invoice line item.

            - `computed.recurring.total_details.breakdown.discounts.discount.promotion_code` (string, nullable)
              The promotion code applied to create this discount.

            - `computed.recurring.total_details.breakdown.discounts.discount.source` (object)
              The source of the discount.

              - `computed.recurring.total_details.breakdown.discounts.discount.source.coupon` (string, nullable)
                The coupon that was redeemed to create this discount.

              - `computed.recurring.total_details.breakdown.discounts.discount.source.type` (enum)
                The source type of the discount.
Possible enum values:
                - `coupon`
                  Coupon source type

            - `computed.recurring.total_details.breakdown.discounts.discount.start` (timestamp)
              Date that the coupon was applied.

            - `computed.recurring.total_details.breakdown.discounts.discount.subscription` (string, nullable)
              The subscription that this coupon is applied to, if it is applied to a particular subscription.

            - `computed.recurring.total_details.breakdown.discounts.discount.subscription_item` (string, nullable)
              The subscription item that this coupon is applied to, if it is applied to a particular subscription item.

        - `computed.recurring.total_details.breakdown.taxes` (array of objects)
          The aggregated tax amounts by rate.

          - `computed.recurring.total_details.breakdown.taxes.amount` (integer)
            Amount of tax applied for this rate.

          - `computed.recurring.total_details.breakdown.taxes.rate` (object)
            The tax rate applied.

            - `computed.recurring.total_details.breakdown.taxes.rate.id` (string)
              Unique identifier for the object.

            - `computed.recurring.total_details.breakdown.taxes.rate.object` (string)
              String representing the object’s type. Objects of the same type share the same value.

            - `computed.recurring.total_details.breakdown.taxes.rate.active` (boolean)
              Defaults to `true`. When set to `false`, this tax rate cannot be used with new applications or Checkout Sessions, but will still work for subscriptions and invoices that already have it set.

            - `computed.recurring.total_details.breakdown.taxes.rate.country` (string, nullable)
              Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

            - `computed.recurring.total_details.breakdown.taxes.rate.created` (timestamp)
              Time at which the object was created. Measured in seconds since the Unix epoch.

            - `computed.recurring.total_details.breakdown.taxes.rate.description` (string, nullable)
              An arbitrary string attached to the tax rate for your internal use only. It will not be visible to your customers.

            - `computed.recurring.total_details.breakdown.taxes.rate.display_name` (string)
              The display name of the tax rates as it will appear to your customer on their receipt email, PDF, and the hosted invoice page.

            - `computed.recurring.total_details.breakdown.taxes.rate.effective_percentage` (float, nullable)
              Actual/effective tax rate percentage out of 100. For tax calculations with automatic_tax[enabled]=true, this percentage reflects the rate actually used to calculate tax based on the product’s taxability and whether the user is registered to collect taxes in the corresponding jurisdiction.

            - `computed.recurring.total_details.breakdown.taxes.rate.flat_amount` (object, nullable)
              The amount of the tax rate when the `rate_type` is `flat_amount`. Tax rates with `rate_type` `percentage` can vary based on the transaction, resulting in this field being `null`. This field exposes the amount and currency of the flat tax rate.

              - `computed.recurring.total_details.breakdown.taxes.rate.flat_amount.amount` (integer)
                Amount of the tax when the `rate_type` is `flat_amount`. This positive integer represents how much to charge in the smallest currency unit (e.g., 100 cents to charge $1.00 or 100 to charge ¥100, a zero-decimal currency). The amount value supports up to eight digits (e.g., a value of 99999999 for a USD charge of $999,999.99).

              - `computed.recurring.total_details.breakdown.taxes.rate.flat_amount.currency` (string)
                Three-letter ISO currency code, in lowercase.

            - `computed.recurring.total_details.breakdown.taxes.rate.inclusive` (boolean)
              This specifies if the tax rate is inclusive or exclusive.

            - `computed.recurring.total_details.breakdown.taxes.rate.jurisdiction` (string, nullable)
              The jurisdiction for the tax rate. You can use this label field for tax reporting purposes. It also appears on your customer’s invoice.

            - `computed.recurring.total_details.breakdown.taxes.rate.jurisdiction_level` (enum, nullable)
              The level of the jurisdiction that imposes this tax rate. Will be `null` for manually defined tax rates.
Possible enum values:
              - `city`
              - `country`
              - `county`
              - `district`
              - `multiple`
              - `state`

            - `computed.recurring.total_details.breakdown.taxes.rate.livemode` (boolean)
              Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.

            - `computed.recurring.total_details.breakdown.taxes.rate.metadata` (object, nullable)
              Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

            - `computed.recurring.total_details.breakdown.taxes.rate.percentage` (float)
              Tax rate percentage out of 100. For tax calculations with automatic_tax[enabled]=true, this percentage includes the statutory tax rate of non-taxable jurisdictions.

            - `computed.recurring.total_details.breakdown.taxes.rate.rate_type` (enum, nullable)
              Indicates the type of tax rate applied to the taxable amount. This value can be `null` when no tax applies to the location. This field is only present for TaxRates created by Stripe Tax.
Possible enum values:
              - `flat_amount`
                A fixed amount applied as tax, regardless of the taxable amount, such as a retail delivery fee.

              - `percentage`
                A tax rate expressed as a percentage of the taxable amount, such as the sales tax rate in California.

            - `computed.recurring.total_details.breakdown.taxes.rate.state` (string, nullable)
              [ISO 3166-2 subdivision code](https://en.wikipedia.org/wiki/ISO_3166-2), without country prefix. For example, “NY” for New York, United States.

            - `computed.recurring.total_details.breakdown.taxes.rate.tax_type` (enum, nullable)
              The high-level tax type, such as `vat` or `sales_tax`.
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

          - `computed.recurring.total_details.breakdown.taxes.taxability_reason` (enum, nullable)
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

          - `computed.recurring.total_details.breakdown.taxes.taxable_amount` (integer, nullable)
            The amount on which tax is calculated, in cents.

  - `computed.upfront` (object)
    The definitive upfront totals and line items the customer will be charged on the first invoice.

    - `computed.upfront.amount_subtotal` (integer)
      Total before any discounts or taxes are applied.

    - `computed.upfront.amount_total` (integer)
      Total after discounts and taxes are applied.

    - `computed.upfront.line_items` (object)
      The line items that will appear on the next invoice after this quote is accepted. This does not include pending invoice items that exist on the customer but may still be included in the next invoice.

      - `computed.upfront.line_items.object` (string)
        String representing the object’s type. Objects of the same type share the same value. Always has the value `list`.

      - `computed.upfront.line_items.data` (array of objects)
        Details about each object.

        - `computed.upfront.line_items.data.id` (string)
          Unique identifier for the object.

        - `computed.upfront.line_items.data.object` (string)
          String representing the object’s type. Objects of the same type share the same value.

        - `computed.upfront.line_items.data.amount_discount` (integer)
          Total discount amount applied. If no discounts were applied, defaults to 0.

        - `computed.upfront.line_items.data.amount_subtotal` (integer)
          Total before any discounts or taxes are applied.

        - `computed.upfront.line_items.data.amount_tax` (integer)
          Total tax amount applied. If no tax was applied, defaults to 0.

        - `computed.upfront.line_items.data.amount_total` (integer)
          Total after discounts and taxes.

        - `computed.upfront.line_items.data.currency` (enum)
          Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

        - `computed.upfront.line_items.data.description` (string, nullable)
          An arbitrary string attached to the object. Often useful for displaying to users. Defaults to product name.

        - `computed.upfront.line_items.data.discounts` (array of objects, nullable)
          The discounts applied to the line item.

          - `computed.upfront.line_items.data.discounts.amount` (integer)
            The amount discounted.

          - `computed.upfront.line_items.data.discounts.discount` (object)
            The discount applied.

            - `computed.upfront.line_items.data.discounts.discount.id` (string)
              The ID of the discount object. Discounts cannot be fetched by ID. Use `expand[]=discounts` in API calls to expand discount IDs in an array.

            - `computed.upfront.line_items.data.discounts.discount.object` (string)
              String representing the object’s type. Objects of the same type share the same value.

            - `computed.upfront.line_items.data.discounts.discount.checkout_session` (string, nullable)
              The Checkout session that this coupon is applied to, if it is applied to a particular session in payment mode. Will not be present for subscription mode.

            - `computed.upfront.line_items.data.discounts.discount.customer` (string, nullable)
              The ID of the customer associated with this discount.

            - `computed.upfront.line_items.data.discounts.discount.customer_account` (string, nullable)
              The ID of the account representing the customer associated with this discount.

            - `computed.upfront.line_items.data.discounts.discount.end` (timestamp, nullable)
              If the coupon has a duration of `repeating`, the date that this discount will end. If the coupon has a duration of `once` or `forever`, this attribute will be null.

            - `computed.upfront.line_items.data.discounts.discount.invoice` (string, nullable)
              The invoice that the discount’s coupon was applied to, if it was applied directly to a particular invoice.

            - `computed.upfront.line_items.data.discounts.discount.invoice_item` (string, nullable)
              The invoice item `id` (or invoice line item `id` for invoice line items of type=‘subscription’) that the discount’s coupon was applied to, if it was applied directly to a particular invoice item or invoice line item.

            - `computed.upfront.line_items.data.discounts.discount.promotion_code` (string, nullable)
              The promotion code applied to create this discount.

            - `computed.upfront.line_items.data.discounts.discount.source` (object)
              The source of the discount.

              - `computed.upfront.line_items.data.discounts.discount.source.coupon` (string, nullable)
                The coupon that was redeemed to create this discount.

              - `computed.upfront.line_items.data.discounts.discount.source.type` (enum)
                The source type of the discount.
Possible enum values:
                - `coupon`
                  Coupon source type

            - `computed.upfront.line_items.data.discounts.discount.start` (timestamp)
              Date that the coupon was applied.

            - `computed.upfront.line_items.data.discounts.discount.subscription` (string, nullable)
              The subscription that this coupon is applied to, if it is applied to a particular subscription.

            - `computed.upfront.line_items.data.discounts.discount.subscription_item` (string, nullable)
              The subscription item that this coupon is applied to, if it is applied to a particular subscription item.

        - `computed.upfront.line_items.data.metadata` (object, nullable)
          Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

        - `computed.upfront.line_items.data.price` (object, nullable)
          The price used to generate the line item.

          - `computed.upfront.line_items.data.price.id` (string)
            Unique identifier for the object.

          - `computed.upfront.line_items.data.price.object` (string)
            String representing the object’s type. Objects of the same type share the same value.

          - `computed.upfront.line_items.data.price.active` (boolean)
            Whether the price can be used for new purchases.

          - `computed.upfront.line_items.data.price.billing_scheme` (enum)
            Describes how to compute the price per period. Either `per_unit` or `tiered`. `per_unit` indicates that the fixed amount (specified in `unit_amount` or `unit_amount_decimal`) will be charged per unit in `quantity` (for prices with `usage_type=licensed`), or per unit of total usage (for prices with `usage_type=metered`). `tiered` indicates that the unit pricing will be computed using a tiering strategy as defined using the `tiers` and `tiers_mode` attributes.
Possible enum values:
            - `per_unit`
            - `tiered`

          - `computed.upfront.line_items.data.price.created` (timestamp)
            Time at which the object was created. Measured in seconds since the Unix epoch.

          - `computed.upfront.line_items.data.price.currency` (enum)
            Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

          - `computed.upfront.line_items.data.price.currency_options` (object, nullable)
            Prices defined in each available currency option. Each key must be a three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html) and a [supported currency](https://stripe.com/docs/currencies).

            - `computed.upfront.line_items.data.price.currency_options.<currency>.custom_unit_amount` (object, nullable)
              When set, provides configuration for the amount to be adjusted by the customer during Checkout Sessions and Payment Links.

              - `computed.upfront.line_items.data.price.currency_options.<currency>.custom_unit_amount.maximum` (integer, nullable)
                The maximum unit amount the customer can specify for this item.

              - `computed.upfront.line_items.data.price.currency_options.<currency>.custom_unit_amount.minimum` (integer, nullable)
                The minimum unit amount the customer can specify for this item. Must be at least the minimum charge amount.

              - `computed.upfront.line_items.data.price.currency_options.<currency>.custom_unit_amount.preset` (integer, nullable)
                The starting unit amount which can be updated by the customer.

            - `computed.upfront.line_items.data.price.currency_options.<currency>.tax_behavior` (enum, nullable)
              Only required if a [default tax behavior](https://docs.stripe.com/docs/tax/products-prices-tax-categories-tax-behavior.md#setting-a-default-tax-behavior-\(recommended\)) was not provided in the Stripe Tax settings. Specifies whether the price is considered inclusive of taxes or exclusive of taxes. One of `inclusive`, `exclusive`, or `unspecified`. Once specified as either `inclusive` or `exclusive`, it cannot be changed.
Possible enum values:
              - `exclusive`
              - `inclusive`
              - `unspecified`

            - `computed.upfront.line_items.data.price.currency_options.<currency>.tiers` (array of objects, nullable)
              Each element represents a pricing tier. This parameter requires `billing_scheme` to be set to `tiered`. See also the documentation for `billing_scheme`.

              - `computed.upfront.line_items.data.price.currency_options.<currency>.tiers.flat_amount` (integer, nullable)
                Price for the entire tier.

              - `computed.upfront.line_items.data.price.currency_options.<currency>.tiers.flat_amount_decimal` (decimal string, nullable)
                Same as `flat_amount`, but contains a decimal value with at most 12 decimal places.

              - `computed.upfront.line_items.data.price.currency_options.<currency>.tiers.unit_amount` (integer, nullable)
                Per unit price for units relevant to the tier.

              - `computed.upfront.line_items.data.price.currency_options.<currency>.tiers.unit_amount_decimal` (decimal string, nullable)
                Same as `unit_amount`, but contains a decimal value with at most 12 decimal places.

              - `computed.upfront.line_items.data.price.currency_options.<currency>.tiers.up_to` (integer, nullable)
                Up to and including to this quantity will be contained in the tier.

            - `computed.upfront.line_items.data.price.currency_options.<currency>.unit_amount` (integer, nullable)
              The unit amount in cents to be charged, represented as a whole integer if possible. Only set if `billing_scheme=per_unit`.

            - `computed.upfront.line_items.data.price.currency_options.<currency>.unit_amount_decimal` (decimal string, nullable)
              The unit amount in cents to be charged, represented as a decimal string with at most 12 decimal places. Only set if `billing_scheme=per_unit`.

          - `computed.upfront.line_items.data.price.custom_unit_amount` (object, nullable)
            When set, provides configuration for the amount to be adjusted by the customer during Checkout Sessions and Payment Links.

            - `computed.upfront.line_items.data.price.custom_unit_amount.maximum` (integer, nullable)
              The maximum unit amount the customer can specify for this item.

            - `computed.upfront.line_items.data.price.custom_unit_amount.minimum` (integer, nullable)
              The minimum unit amount the customer can specify for this item. Must be at least the minimum charge amount.

            - `computed.upfront.line_items.data.price.custom_unit_amount.preset` (integer, nullable)
              The starting unit amount which can be updated by the customer.

          - `computed.upfront.line_items.data.price.livemode` (boolean)
            Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.

          - `computed.upfront.line_items.data.price.lookup_key` (string, nullable)
            A lookup key used to retrieve prices dynamically from a static string. This may be up to 200 characters.

          - `computed.upfront.line_items.data.price.metadata` (object)
            Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

          - `computed.upfront.line_items.data.price.nickname` (string, nullable)
            A brief description of the price, hidden from customers.

          - `computed.upfront.line_items.data.price.product` (string)
            The ID of the product this price is associated with.

          - `computed.upfront.line_items.data.price.recurring` (object, nullable)
            The recurring components of a price such as `interval` and `usage_type`.

            - `computed.upfront.line_items.data.price.recurring.interval` (enum)
              The frequency at which a subscription is billed. One of `day`, `week`, `month` or `year`.

            - `computed.upfront.line_items.data.price.recurring.interval_count` (integer)
              The number of intervals (specified in the `interval` attribute) between subscription billings. For example, `interval=month` and `interval_count=3` bills every 3 months.

            - `computed.upfront.line_items.data.price.recurring.meter` (string, nullable)
              The meter tracking the usage of a metered price

            - `computed.upfront.line_items.data.price.recurring.usage_type` (enum)
              Configures how the quantity per period should be determined. Can be either `metered` or `licensed`. `licensed` automatically bills the `quantity` set when adding it to a subscription. `metered` aggregates the total usage based on usage records. Defaults to `licensed`.

          - `computed.upfront.line_items.data.price.tax_behavior` (enum, nullable)
            Only required if a [default tax behavior](https://docs.stripe.com/docs/tax/products-prices-tax-categories-tax-behavior.md#setting-a-default-tax-behavior-\(recommended\)) was not provided in the Stripe Tax settings. Specifies whether the price is considered inclusive of taxes or exclusive of taxes. One of `inclusive`, `exclusive`, or `unspecified`. Once specified as either `inclusive` or `exclusive`, it cannot be changed.
Possible enum values:
            - `exclusive`
            - `inclusive`
            - `unspecified`

          - `computed.upfront.line_items.data.price.tiers` (array of objects, nullable)
            Each element represents a pricing tier. This parameter requires `billing_scheme` to be set to `tiered`. See also the documentation for `billing_scheme`.

            - `computed.upfront.line_items.data.price.tiers.flat_amount` (integer, nullable)
              Price for the entire tier.

            - `computed.upfront.line_items.data.price.tiers.flat_amount_decimal` (decimal string, nullable)
              Same as `flat_amount`, but contains a decimal value with at most 12 decimal places.

            - `computed.upfront.line_items.data.price.tiers.unit_amount` (integer, nullable)
              Per unit price for units relevant to the tier.

            - `computed.upfront.line_items.data.price.tiers.unit_amount_decimal` (decimal string, nullable)
              Same as `unit_amount`, but contains a decimal value with at most 12 decimal places.

            - `computed.upfront.line_items.data.price.tiers.up_to` (integer, nullable)
              Up to and including to this quantity will be contained in the tier.

          - `computed.upfront.line_items.data.price.tiers_mode` (enum, nullable)
            Defines if the tiering price should be `graduated` or `volume` based. In `volume`-based tiering, the maximum quantity within a period determines the per unit price. In `graduated` tiering, pricing can change as the quantity grows.
Possible enum values:
            - `graduated`
            - `volume`

          - `computed.upfront.line_items.data.price.transform_quantity` (object, nullable)
            Apply a transformation to the reported usage or set quantity before computing the amount billed. Cannot be combined with `tiers`.

            - `computed.upfront.line_items.data.price.transform_quantity.divide_by` (integer)
              Divide usage by this number.

            - `computed.upfront.line_items.data.price.transform_quantity.round` (enum)
              After division, either round the result `up` or `down`.

          - `computed.upfront.line_items.data.price.type` (enum)
            One of `one_time` or `recurring` depending on whether the price is for a one-time purchase or a recurring (subscription) purchase.
Possible enum values:
            - `one_time`
            - `recurring`

          - `computed.upfront.line_items.data.price.unit_amount` (integer, nullable)
            The unit amount in cents to be charged, represented as a whole integer if possible. Only set if `billing_scheme=per_unit`.

          - `computed.upfront.line_items.data.price.unit_amount_decimal` (decimal string, nullable)
            The unit amount in cents to be charged, represented as a decimal string with at most 12 decimal places. Only set if `billing_scheme=per_unit`.

        - `computed.upfront.line_items.data.quantity` (integer, nullable)
          The quantity of products being purchased.

        - `computed.upfront.line_items.data.taxes` (array of objects, nullable)
          The taxes applied to the line item.

          - `computed.upfront.line_items.data.taxes.amount` (integer)
            Amount of tax applied for this rate.

          - `computed.upfront.line_items.data.taxes.rate` (object)
            The tax rate applied.

            - `computed.upfront.line_items.data.taxes.rate.id` (string)
              Unique identifier for the object.

            - `computed.upfront.line_items.data.taxes.rate.object` (string)
              String representing the object’s type. Objects of the same type share the same value.

            - `computed.upfront.line_items.data.taxes.rate.active` (boolean)
              Defaults to `true`. When set to `false`, this tax rate cannot be used with new applications or Checkout Sessions, but will still work for subscriptions and invoices that already have it set.

            - `computed.upfront.line_items.data.taxes.rate.country` (string, nullable)
              Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

            - `computed.upfront.line_items.data.taxes.rate.created` (timestamp)
              Time at which the object was created. Measured in seconds since the Unix epoch.

            - `computed.upfront.line_items.data.taxes.rate.description` (string, nullable)
              An arbitrary string attached to the tax rate for your internal use only. It will not be visible to your customers.

            - `computed.upfront.line_items.data.taxes.rate.display_name` (string)
              The display name of the tax rates as it will appear to your customer on their receipt email, PDF, and the hosted invoice page.

            - `computed.upfront.line_items.data.taxes.rate.effective_percentage` (float, nullable)
              Actual/effective tax rate percentage out of 100. For tax calculations with automatic_tax[enabled]=true, this percentage reflects the rate actually used to calculate tax based on the product’s taxability and whether the user is registered to collect taxes in the corresponding jurisdiction.

            - `computed.upfront.line_items.data.taxes.rate.flat_amount` (object, nullable)
              The amount of the tax rate when the `rate_type` is `flat_amount`. Tax rates with `rate_type` `percentage` can vary based on the transaction, resulting in this field being `null`. This field exposes the amount and currency of the flat tax rate.

              - `computed.upfront.line_items.data.taxes.rate.flat_amount.amount` (integer)
                Amount of the tax when the `rate_type` is `flat_amount`. This positive integer represents how much to charge in the smallest currency unit (e.g., 100 cents to charge $1.00 or 100 to charge ¥100, a zero-decimal currency). The amount value supports up to eight digits (e.g., a value of 99999999 for a USD charge of $999,999.99).

              - `computed.upfront.line_items.data.taxes.rate.flat_amount.currency` (string)
                Three-letter ISO currency code, in lowercase.

            - `computed.upfront.line_items.data.taxes.rate.inclusive` (boolean)
              This specifies if the tax rate is inclusive or exclusive.

            - `computed.upfront.line_items.data.taxes.rate.jurisdiction` (string, nullable)
              The jurisdiction for the tax rate. You can use this label field for tax reporting purposes. It also appears on your customer’s invoice.

            - `computed.upfront.line_items.data.taxes.rate.jurisdiction_level` (enum, nullable)
              The level of the jurisdiction that imposes this tax rate. Will be `null` for manually defined tax rates.
Possible enum values:
              - `city`
              - `country`
              - `county`
              - `district`
              - `multiple`
              - `state`

            - `computed.upfront.line_items.data.taxes.rate.livemode` (boolean)
              Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.

            - `computed.upfront.line_items.data.taxes.rate.metadata` (object, nullable)
              Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

            - `computed.upfront.line_items.data.taxes.rate.percentage` (float)
              Tax rate percentage out of 100. For tax calculations with automatic_tax[enabled]=true, this percentage includes the statutory tax rate of non-taxable jurisdictions.

            - `computed.upfront.line_items.data.taxes.rate.rate_type` (enum, nullable)
              Indicates the type of tax rate applied to the taxable amount. This value can be `null` when no tax applies to the location. This field is only present for TaxRates created by Stripe Tax.
Possible enum values:
              - `flat_amount`
                A fixed amount applied as tax, regardless of the taxable amount, such as a retail delivery fee.

              - `percentage`
                A tax rate expressed as a percentage of the taxable amount, such as the sales tax rate in California.

            - `computed.upfront.line_items.data.taxes.rate.state` (string, nullable)
              [ISO 3166-2 subdivision code](https://en.wikipedia.org/wiki/ISO_3166-2), without country prefix. For example, “NY” for New York, United States.

            - `computed.upfront.line_items.data.taxes.rate.tax_type` (enum, nullable)
              The high-level tax type, such as `vat` or `sales_tax`.
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

          - `computed.upfront.line_items.data.taxes.taxability_reason` (enum, nullable)
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

          - `computed.upfront.line_items.data.taxes.taxable_amount` (integer, nullable)
            The amount on which tax is calculated, in cents.

      - `computed.upfront.line_items.has_more` (boolean)
        True if this list has another page of items after this one that can be fetched.

      - `computed.upfront.line_items.url` (string)
        The URL where this list can be accessed.

    - `computed.upfront.total_details` (object)
      Tax and discount details for the computed total amount.

      - `computed.upfront.total_details.amount_discount` (integer)
        This is the sum of all the discounts.

      - `computed.upfront.total_details.amount_shipping` (integer, nullable)
        This is the sum of all the shipping amounts.

      - `computed.upfront.total_details.amount_tax` (integer)
        This is the sum of all the tax amounts.

      - `computed.upfront.total_details.breakdown` (object, nullable)
        Breakdown of individual tax and discount amounts that add up to the totals.

        - `computed.upfront.total_details.breakdown.discounts` (array of objects)
          The aggregated discounts.

          - `computed.upfront.total_details.breakdown.discounts.amount` (integer)
            The amount discounted.

          - `computed.upfront.total_details.breakdown.discounts.discount` (object)
            The discount applied.

            - `computed.upfront.total_details.breakdown.discounts.discount.id` (string)
              The ID of the discount object. Discounts cannot be fetched by ID. Use `expand[]=discounts` in API calls to expand discount IDs in an array.

            - `computed.upfront.total_details.breakdown.discounts.discount.object` (string)
              String representing the object’s type. Objects of the same type share the same value.

            - `computed.upfront.total_details.breakdown.discounts.discount.checkout_session` (string, nullable)
              The Checkout session that this coupon is applied to, if it is applied to a particular session in payment mode. Will not be present for subscription mode.

            - `computed.upfront.total_details.breakdown.discounts.discount.customer` (string, nullable)
              The ID of the customer associated with this discount.

            - `computed.upfront.total_details.breakdown.discounts.discount.customer_account` (string, nullable)
              The ID of the account representing the customer associated with this discount.

            - `computed.upfront.total_details.breakdown.discounts.discount.end` (timestamp, nullable)
              If the coupon has a duration of `repeating`, the date that this discount will end. If the coupon has a duration of `once` or `forever`, this attribute will be null.

            - `computed.upfront.total_details.breakdown.discounts.discount.invoice` (string, nullable)
              The invoice that the discount’s coupon was applied to, if it was applied directly to a particular invoice.

            - `computed.upfront.total_details.breakdown.discounts.discount.invoice_item` (string, nullable)
              The invoice item `id` (or invoice line item `id` for invoice line items of type=‘subscription’) that the discount’s coupon was applied to, if it was applied directly to a particular invoice item or invoice line item.

            - `computed.upfront.total_details.breakdown.discounts.discount.promotion_code` (string, nullable)
              The promotion code applied to create this discount.

            - `computed.upfront.total_details.breakdown.discounts.discount.source` (object)
              The source of the discount.

              - `computed.upfront.total_details.breakdown.discounts.discount.source.coupon` (string, nullable)
                The coupon that was redeemed to create this discount.

              - `computed.upfront.total_details.breakdown.discounts.discount.source.type` (enum)
                The source type of the discount.
Possible enum values:
                - `coupon`
                  Coupon source type

            - `computed.upfront.total_details.breakdown.discounts.discount.start` (timestamp)
              Date that the coupon was applied.

            - `computed.upfront.total_details.breakdown.discounts.discount.subscription` (string, nullable)
              The subscription that this coupon is applied to, if it is applied to a particular subscription.

            - `computed.upfront.total_details.breakdown.discounts.discount.subscription_item` (string, nullable)
              The subscription item that this coupon is applied to, if it is applied to a particular subscription item.

        - `computed.upfront.total_details.breakdown.taxes` (array of objects)
          The aggregated tax amounts by rate.

          - `computed.upfront.total_details.breakdown.taxes.amount` (integer)
            Amount of tax applied for this rate.

          - `computed.upfront.total_details.breakdown.taxes.rate` (object)
            The tax rate applied.

            - `computed.upfront.total_details.breakdown.taxes.rate.id` (string)
              Unique identifier for the object.

            - `computed.upfront.total_details.breakdown.taxes.rate.object` (string)
              String representing the object’s type. Objects of the same type share the same value.

            - `computed.upfront.total_details.breakdown.taxes.rate.active` (boolean)
              Defaults to `true`. When set to `false`, this tax rate cannot be used with new applications or Checkout Sessions, but will still work for subscriptions and invoices that already have it set.

            - `computed.upfront.total_details.breakdown.taxes.rate.country` (string, nullable)
              Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

            - `computed.upfront.total_details.breakdown.taxes.rate.created` (timestamp)
              Time at which the object was created. Measured in seconds since the Unix epoch.

            - `computed.upfront.total_details.breakdown.taxes.rate.description` (string, nullable)
              An arbitrary string attached to the tax rate for your internal use only. It will not be visible to your customers.

            - `computed.upfront.total_details.breakdown.taxes.rate.display_name` (string)
              The display name of the tax rates as it will appear to your customer on their receipt email, PDF, and the hosted invoice page.

            - `computed.upfront.total_details.breakdown.taxes.rate.effective_percentage` (float, nullable)
              Actual/effective tax rate percentage out of 100. For tax calculations with automatic_tax[enabled]=true, this percentage reflects the rate actually used to calculate tax based on the product’s taxability and whether the user is registered to collect taxes in the corresponding jurisdiction.

            - `computed.upfront.total_details.breakdown.taxes.rate.flat_amount` (object, nullable)
              The amount of the tax rate when the `rate_type` is `flat_amount`. Tax rates with `rate_type` `percentage` can vary based on the transaction, resulting in this field being `null`. This field exposes the amount and currency of the flat tax rate.

              - `computed.upfront.total_details.breakdown.taxes.rate.flat_amount.amount` (integer)
                Amount of the tax when the `rate_type` is `flat_amount`. This positive integer represents how much to charge in the smallest currency unit (e.g., 100 cents to charge $1.00 or 100 to charge ¥100, a zero-decimal currency). The amount value supports up to eight digits (e.g., a value of 99999999 for a USD charge of $999,999.99).

              - `computed.upfront.total_details.breakdown.taxes.rate.flat_amount.currency` (string)
                Three-letter ISO currency code, in lowercase.

            - `computed.upfront.total_details.breakdown.taxes.rate.inclusive` (boolean)
              This specifies if the tax rate is inclusive or exclusive.

            - `computed.upfront.total_details.breakdown.taxes.rate.jurisdiction` (string, nullable)
              The jurisdiction for the tax rate. You can use this label field for tax reporting purposes. It also appears on your customer’s invoice.

            - `computed.upfront.total_details.breakdown.taxes.rate.jurisdiction_level` (enum, nullable)
              The level of the jurisdiction that imposes this tax rate. Will be `null` for manually defined tax rates.
Possible enum values:
              - `city`
              - `country`
              - `county`
              - `district`
              - `multiple`
              - `state`

            - `computed.upfront.total_details.breakdown.taxes.rate.livemode` (boolean)
              Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.

            - `computed.upfront.total_details.breakdown.taxes.rate.metadata` (object, nullable)
              Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

            - `computed.upfront.total_details.breakdown.taxes.rate.percentage` (float)
              Tax rate percentage out of 100. For tax calculations with automatic_tax[enabled]=true, this percentage includes the statutory tax rate of non-taxable jurisdictions.

            - `computed.upfront.total_details.breakdown.taxes.rate.rate_type` (enum, nullable)
              Indicates the type of tax rate applied to the taxable amount. This value can be `null` when no tax applies to the location. This field is only present for TaxRates created by Stripe Tax.
Possible enum values:
              - `flat_amount`
                A fixed amount applied as tax, regardless of the taxable amount, such as a retail delivery fee.

              - `percentage`
                A tax rate expressed as a percentage of the taxable amount, such as the sales tax rate in California.

            - `computed.upfront.total_details.breakdown.taxes.rate.state` (string, nullable)
              [ISO 3166-2 subdivision code](https://en.wikipedia.org/wiki/ISO_3166-2), without country prefix. For example, “NY” for New York, United States.

            - `computed.upfront.total_details.breakdown.taxes.rate.tax_type` (enum, nullable)
              The high-level tax type, such as `vat` or `sales_tax`.
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

          - `computed.upfront.total_details.breakdown.taxes.taxability_reason` (enum, nullable)
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

          - `computed.upfront.total_details.breakdown.taxes.taxable_amount` (integer, nullable)
            The amount on which tax is calculated, in cents.

- `created` (timestamp)
  Time at which the object was created. Measured in seconds since the Unix epoch.

- `currency` (string, nullable)
  Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

- `customer` (string, nullable)
  The customer who received this quote. A customer is required to finalize the quote. Once specified, you can’t change it.

- `customer_account` (string, nullable)
  The account representing the customer who received this quote. A customer or account is required to finalize the quote. Once specified, you can’t change it.

- `default_tax_rates` (array of strings)
  The tax rates applied to this quote.

- `description` (string, nullable)
  A description that will be displayed on the quote PDF.

- `discounts` (array of strings)
  The discounts applied to this quote.

- `expires_at` (timestamp)
  The date on which the quote will be canceled if in `open` or `draft` status. Measured in seconds since the Unix epoch.

- `footer` (string, nullable)
  A footer that will be displayed on the quote PDF.

- `from_quote` (object, nullable)
  Details of the quote that was cloned. See the [cloning documentation](https://docs.stripe.com/docs/quotes/clone.md) for more details.

  - `from_quote.is_revision` (boolean)
    Whether this quote is a revision of a different quote.

  - `from_quote.quote` (string)
    The quote that was cloned.

- `header` (string, nullable)
  A header that will be displayed on the quote PDF.

- `invoice` (string, nullable)
  The invoice that was created from this quote.

- `invoice_settings` (object)
  All invoices will be billed using the specified settings.

  - `invoice_settings.days_until_due` (integer, nullable)
    Number of days within which a customer must pay invoices generated by this quote. This value will be `null` for quotes where `collection_method=charge_automatically`.

  - `invoice_settings.issuer` (object)
    The connected account that issues the invoice. The invoice is presented with the branding and support information of the specified account.

    - `invoice_settings.issuer.account` (string, nullable)
      The connected account being referenced when `type` is `account`.

    - `invoice_settings.issuer.type` (enum)
      Type of the account referenced.
Possible enum values:
      - `account`
        Indicates that the account being referenced is a connected account which is different from the account making the API request but related to it.

      - `self`
        Indicates that the account being referenced is the account making the API request.

- `line_items` (object)
  A list of items the customer is being quoted for.

  - `line_items.object` (string)
    String representing the object’s type. Objects of the same type share the same value. Always has the value `list`.

  - `line_items.data` (array of objects)
    Details about each object.

    - `line_items.data.id` (string)
      Unique identifier for the object.

    - `line_items.data.object` (string)
      String representing the object’s type. Objects of the same type share the same value.

    - `line_items.data.amount_discount` (integer)
      Total discount amount applied. If no discounts were applied, defaults to 0.

    - `line_items.data.amount_subtotal` (integer)
      Total before any discounts or taxes are applied.

    - `line_items.data.amount_tax` (integer)
      Total tax amount applied. If no tax was applied, defaults to 0.

    - `line_items.data.amount_total` (integer)
      Total after discounts and taxes.

    - `line_items.data.currency` (enum)
      Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

    - `line_items.data.description` (string, nullable)
      An arbitrary string attached to the object. Often useful for displaying to users. Defaults to product name.

    - `line_items.data.discounts` (array of objects, nullable)
      The discounts applied to the line item.

      - `line_items.data.discounts.amount` (integer)
        The amount discounted.

      - `line_items.data.discounts.discount` (object)
        The discount applied.

        - `line_items.data.discounts.discount.id` (string)
          The ID of the discount object. Discounts cannot be fetched by ID. Use `expand[]=discounts` in API calls to expand discount IDs in an array.

        - `line_items.data.discounts.discount.object` (string)
          String representing the object’s type. Objects of the same type share the same value.

        - `line_items.data.discounts.discount.checkout_session` (string, nullable)
          The Checkout session that this coupon is applied to, if it is applied to a particular session in payment mode. Will not be present for subscription mode.

        - `line_items.data.discounts.discount.customer` (string, nullable)
          The ID of the customer associated with this discount.

        - `line_items.data.discounts.discount.customer_account` (string, nullable)
          The ID of the account representing the customer associated with this discount.

        - `line_items.data.discounts.discount.end` (timestamp, nullable)
          If the coupon has a duration of `repeating`, the date that this discount will end. If the coupon has a duration of `once` or `forever`, this attribute will be null.

        - `line_items.data.discounts.discount.invoice` (string, nullable)
          The invoice that the discount’s coupon was applied to, if it was applied directly to a particular invoice.

        - `line_items.data.discounts.discount.invoice_item` (string, nullable)
          The invoice item `id` (or invoice line item `id` for invoice line items of type=‘subscription’) that the discount’s coupon was applied to, if it was applied directly to a particular invoice item or invoice line item.

        - `line_items.data.discounts.discount.promotion_code` (string, nullable)
          The promotion code applied to create this discount.

        - `line_items.data.discounts.discount.source` (object)
          The source of the discount.

          - `line_items.data.discounts.discount.source.coupon` (string, nullable)
            The coupon that was redeemed to create this discount.

          - `line_items.data.discounts.discount.source.type` (enum)
            The source type of the discount.
Possible enum values:
            - `coupon`
              Coupon source type

        - `line_items.data.discounts.discount.start` (timestamp)
          Date that the coupon was applied.

        - `line_items.data.discounts.discount.subscription` (string, nullable)
          The subscription that this coupon is applied to, if it is applied to a particular subscription.

        - `line_items.data.discounts.discount.subscription_item` (string, nullable)
          The subscription item that this coupon is applied to, if it is applied to a particular subscription item.

    - `line_items.data.metadata` (object, nullable)
      Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

    - `line_items.data.price` (object, nullable)
      The price used to generate the line item.

      - `line_items.data.price.id` (string)
        Unique identifier for the object.

      - `line_items.data.price.object` (string)
        String representing the object’s type. Objects of the same type share the same value.

      - `line_items.data.price.active` (boolean)
        Whether the price can be used for new purchases.

      - `line_items.data.price.billing_scheme` (enum)
        Describes how to compute the price per period. Either `per_unit` or `tiered`. `per_unit` indicates that the fixed amount (specified in `unit_amount` or `unit_amount_decimal`) will be charged per unit in `quantity` (for prices with `usage_type=licensed`), or per unit of total usage (for prices with `usage_type=metered`). `tiered` indicates that the unit pricing will be computed using a tiering strategy as defined using the `tiers` and `tiers_mode` attributes.
Possible enum values:
        - `per_unit`
        - `tiered`

      - `line_items.data.price.created` (timestamp)
        Time at which the object was created. Measured in seconds since the Unix epoch.

      - `line_items.data.price.currency` (enum)
        Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

      - `line_items.data.price.currency_options` (object, nullable)
        Prices defined in each available currency option. Each key must be a three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html) and a [supported currency](https://stripe.com/docs/currencies).

        - `line_items.data.price.currency_options.<currency>.custom_unit_amount` (object, nullable)
          When set, provides configuration for the amount to be adjusted by the customer during Checkout Sessions and Payment Links.

          - `line_items.data.price.currency_options.<currency>.custom_unit_amount.maximum` (integer, nullable)
            The maximum unit amount the customer can specify for this item.

          - `line_items.data.price.currency_options.<currency>.custom_unit_amount.minimum` (integer, nullable)
            The minimum unit amount the customer can specify for this item. Must be at least the minimum charge amount.

          - `line_items.data.price.currency_options.<currency>.custom_unit_amount.preset` (integer, nullable)
            The starting unit amount which can be updated by the customer.

        - `line_items.data.price.currency_options.<currency>.tax_behavior` (enum, nullable)
          Only required if a [default tax behavior](https://docs.stripe.com/docs/tax/products-prices-tax-categories-tax-behavior.md#setting-a-default-tax-behavior-\(recommended\)) was not provided in the Stripe Tax settings. Specifies whether the price is considered inclusive of taxes or exclusive of taxes. One of `inclusive`, `exclusive`, or `unspecified`. Once specified as either `inclusive` or `exclusive`, it cannot be changed.
Possible enum values:
          - `exclusive`
          - `inclusive`
          - `unspecified`

        - `line_items.data.price.currency_options.<currency>.tiers` (array of objects, nullable)
          Each element represents a pricing tier. This parameter requires `billing_scheme` to be set to `tiered`. See also the documentation for `billing_scheme`.

          - `line_items.data.price.currency_options.<currency>.tiers.flat_amount` (integer, nullable)
            Price for the entire tier.

          - `line_items.data.price.currency_options.<currency>.tiers.flat_amount_decimal` (decimal string, nullable)
            Same as `flat_amount`, but contains a decimal value with at most 12 decimal places.

          - `line_items.data.price.currency_options.<currency>.tiers.unit_amount` (integer, nullable)
            Per unit price for units relevant to the tier.

          - `line_items.data.price.currency_options.<currency>.tiers.unit_amount_decimal` (decimal string, nullable)
            Same as `unit_amount`, but contains a decimal value with at most 12 decimal places.

          - `line_items.data.price.currency_options.<currency>.tiers.up_to` (integer, nullable)
            Up to and including to this quantity will be contained in the tier.

        - `line_items.data.price.currency_options.<currency>.unit_amount` (integer, nullable)
          The unit amount in cents to be charged, represented as a whole integer if possible. Only set if `billing_scheme=per_unit`.

        - `line_items.data.price.currency_options.<currency>.unit_amount_decimal` (decimal string, nullable)
          The unit amount in cents to be charged, represented as a decimal string with at most 12 decimal places. Only set if `billing_scheme=per_unit`.

      - `line_items.data.price.custom_unit_amount` (object, nullable)
        When set, provides configuration for the amount to be adjusted by the customer during Checkout Sessions and Payment Links.

        - `line_items.data.price.custom_unit_amount.maximum` (integer, nullable)
          The maximum unit amount the customer can specify for this item.

        - `line_items.data.price.custom_unit_amount.minimum` (integer, nullable)
          The minimum unit amount the customer can specify for this item. Must be at least the minimum charge amount.

        - `line_items.data.price.custom_unit_amount.preset` (integer, nullable)
          The starting unit amount which can be updated by the customer.

      - `line_items.data.price.livemode` (boolean)
        Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.

      - `line_items.data.price.lookup_key` (string, nullable)
        A lookup key used to retrieve prices dynamically from a static string. This may be up to 200 characters.

      - `line_items.data.price.metadata` (object)
        Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

      - `line_items.data.price.nickname` (string, nullable)
        A brief description of the price, hidden from customers.

      - `line_items.data.price.product` (string)
        The ID of the product this price is associated with.

      - `line_items.data.price.recurring` (object, nullable)
        The recurring components of a price such as `interval` and `usage_type`.

        - `line_items.data.price.recurring.interval` (enum)
          The frequency at which a subscription is billed. One of `day`, `week`, `month` or `year`.

        - `line_items.data.price.recurring.interval_count` (integer)
          The number of intervals (specified in the `interval` attribute) between subscription billings. For example, `interval=month` and `interval_count=3` bills every 3 months.

        - `line_items.data.price.recurring.meter` (string, nullable)
          The meter tracking the usage of a metered price

        - `line_items.data.price.recurring.usage_type` (enum)
          Configures how the quantity per period should be determined. Can be either `metered` or `licensed`. `licensed` automatically bills the `quantity` set when adding it to a subscription. `metered` aggregates the total usage based on usage records. Defaults to `licensed`.

      - `line_items.data.price.tax_behavior` (enum, nullable)
        Only required if a [default tax behavior](https://docs.stripe.com/docs/tax/products-prices-tax-categories-tax-behavior.md#setting-a-default-tax-behavior-\(recommended\)) was not provided in the Stripe Tax settings. Specifies whether the price is considered inclusive of taxes or exclusive of taxes. One of `inclusive`, `exclusive`, or `unspecified`. Once specified as either `inclusive` or `exclusive`, it cannot be changed.
Possible enum values:
        - `exclusive`
        - `inclusive`
        - `unspecified`

      - `line_items.data.price.tiers` (array of objects, nullable)
        Each element represents a pricing tier. This parameter requires `billing_scheme` to be set to `tiered`. See also the documentation for `billing_scheme`.

        - `line_items.data.price.tiers.flat_amount` (integer, nullable)
          Price for the entire tier.

        - `line_items.data.price.tiers.flat_amount_decimal` (decimal string, nullable)
          Same as `flat_amount`, but contains a decimal value with at most 12 decimal places.

        - `line_items.data.price.tiers.unit_amount` (integer, nullable)
          Per unit price for units relevant to the tier.

        - `line_items.data.price.tiers.unit_amount_decimal` (decimal string, nullable)
          Same as `unit_amount`, but contains a decimal value with at most 12 decimal places.

        - `line_items.data.price.tiers.up_to` (integer, nullable)
          Up to and including to this quantity will be contained in the tier.

      - `line_items.data.price.tiers_mode` (enum, nullable)
        Defines if the tiering price should be `graduated` or `volume` based. In `volume`-based tiering, the maximum quantity within a period determines the per unit price. In `graduated` tiering, pricing can change as the quantity grows.
Possible enum values:
        - `graduated`
        - `volume`

      - `line_items.data.price.transform_quantity` (object, nullable)
        Apply a transformation to the reported usage or set quantity before computing the amount billed. Cannot be combined with `tiers`.

        - `line_items.data.price.transform_quantity.divide_by` (integer)
          Divide usage by this number.

        - `line_items.data.price.transform_quantity.round` (enum)
          After division, either round the result `up` or `down`.

      - `line_items.data.price.type` (enum)
        One of `one_time` or `recurring` depending on whether the price is for a one-time purchase or a recurring (subscription) purchase.
Possible enum values:
        - `one_time`
        - `recurring`

      - `line_items.data.price.unit_amount` (integer, nullable)
        The unit amount in cents to be charged, represented as a whole integer if possible. Only set if `billing_scheme=per_unit`.

      - `line_items.data.price.unit_amount_decimal` (decimal string, nullable)
        The unit amount in cents to be charged, represented as a decimal string with at most 12 decimal places. Only set if `billing_scheme=per_unit`.

    - `line_items.data.quantity` (integer, nullable)
      The quantity of products being purchased.

    - `line_items.data.taxes` (array of objects, nullable)
      The taxes applied to the line item.

      - `line_items.data.taxes.amount` (integer)
        Amount of tax applied for this rate.

      - `line_items.data.taxes.rate` (object)
        The tax rate applied.

        - `line_items.data.taxes.rate.id` (string)
          Unique identifier for the object.

        - `line_items.data.taxes.rate.object` (string)
          String representing the object’s type. Objects of the same type share the same value.

        - `line_items.data.taxes.rate.active` (boolean)
          Defaults to `true`. When set to `false`, this tax rate cannot be used with new applications or Checkout Sessions, but will still work for subscriptions and invoices that already have it set.

        - `line_items.data.taxes.rate.country` (string, nullable)
          Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

        - `line_items.data.taxes.rate.created` (timestamp)
          Time at which the object was created. Measured in seconds since the Unix epoch.

        - `line_items.data.taxes.rate.description` (string, nullable)
          An arbitrary string attached to the tax rate for your internal use only. It will not be visible to your customers.

        - `line_items.data.taxes.rate.display_name` (string)
          The display name of the tax rates as it will appear to your customer on their receipt email, PDF, and the hosted invoice page.

        - `line_items.data.taxes.rate.effective_percentage` (float, nullable)
          Actual/effective tax rate percentage out of 100. For tax calculations with automatic_tax[enabled]=true, this percentage reflects the rate actually used to calculate tax based on the product’s taxability and whether the user is registered to collect taxes in the corresponding jurisdiction.

        - `line_items.data.taxes.rate.flat_amount` (object, nullable)
          The amount of the tax rate when the `rate_type` is `flat_amount`. Tax rates with `rate_type` `percentage` can vary based on the transaction, resulting in this field being `null`. This field exposes the amount and currency of the flat tax rate.

          - `line_items.data.taxes.rate.flat_amount.amount` (integer)
            Amount of the tax when the `rate_type` is `flat_amount`. This positive integer represents how much to charge in the smallest currency unit (e.g., 100 cents to charge $1.00 or 100 to charge ¥100, a zero-decimal currency). The amount value supports up to eight digits (e.g., a value of 99999999 for a USD charge of $999,999.99).

          - `line_items.data.taxes.rate.flat_amount.currency` (string)
            Three-letter ISO currency code, in lowercase.

        - `line_items.data.taxes.rate.inclusive` (boolean)
          This specifies if the tax rate is inclusive or exclusive.

        - `line_items.data.taxes.rate.jurisdiction` (string, nullable)
          The jurisdiction for the tax rate. You can use this label field for tax reporting purposes. It also appears on your customer’s invoice.

        - `line_items.data.taxes.rate.jurisdiction_level` (enum, nullable)
          The level of the jurisdiction that imposes this tax rate. Will be `null` for manually defined tax rates.
Possible enum values:
          - `city`
          - `country`
          - `county`
          - `district`
          - `multiple`
          - `state`

        - `line_items.data.taxes.rate.livemode` (boolean)
          Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.

        - `line_items.data.taxes.rate.metadata` (object, nullable)
          Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

        - `line_items.data.taxes.rate.percentage` (float)
          Tax rate percentage out of 100. For tax calculations with automatic_tax[enabled]=true, this percentage includes the statutory tax rate of non-taxable jurisdictions.

        - `line_items.data.taxes.rate.rate_type` (enum, nullable)
          Indicates the type of tax rate applied to the taxable amount. This value can be `null` when no tax applies to the location. This field is only present for TaxRates created by Stripe Tax.
Possible enum values:
          - `flat_amount`
            A fixed amount applied as tax, regardless of the taxable amount, such as a retail delivery fee.

          - `percentage`
            A tax rate expressed as a percentage of the taxable amount, such as the sales tax rate in California.

        - `line_items.data.taxes.rate.state` (string, nullable)
          [ISO 3166-2 subdivision code](https://en.wikipedia.org/wiki/ISO_3166-2), without country prefix. For example, “NY” for New York, United States.

        - `line_items.data.taxes.rate.tax_type` (enum, nullable)
          The high-level tax type, such as `vat` or `sales_tax`.
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

      - `line_items.data.taxes.taxability_reason` (enum, nullable)
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

      - `line_items.data.taxes.taxable_amount` (integer, nullable)
        The amount on which tax is calculated, in cents.

  - `line_items.has_more` (boolean)
    True if this list has another page of items after this one that can be fetched.

  - `line_items.url` (string)
    The URL where this list can be accessed.

- `livemode` (boolean)
  Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.

- `metadata` (object)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

- `number` (string, nullable)
  A unique number that identifies this particular quote. This number is assigned once the quote is [finalized](https://docs.stripe.com/docs/quotes/overview.md#finalize).

- `on_behalf_of` (string, nullable)
  The account on behalf of which to charge. See the [Connect documentation](https://support.stripe.com/questions/sending-invoices-on-behalf-of-connected-accounts) for details.

- `status` (enum)
  The status of the quote.
Possible enum values:
  - `accepted`
    The customer has accepted the quote and invoice, subscription or subscription schedule has been created.

  - `canceled`
    The quote has been canceled and is no longer valid.

  - `draft`
    The quote can be edited while in this status and has not been sent to the customer.

  - `open`
    The quote has been finalized and is awaiting action from the customer.

- `status_transitions` (object)
  The timestamps of which the quote transitioned to a new status.

  - `status_transitions.accepted_at` (timestamp, nullable)
    The time that the quote was accepted. Measured in seconds since Unix epoch.

  - `status_transitions.canceled_at` (timestamp, nullable)
    The time that the quote was canceled. Measured in seconds since Unix epoch.

  - `status_transitions.finalized_at` (timestamp, nullable)
    The time that the quote was finalized. Measured in seconds since Unix epoch.

- `subscription` (string, nullable)
  The subscription that was created or updated from this quote.

- `subscription_data` (object)
  When creating a subscription or subscription schedule, the specified configuration data will be used. There must be at least one line item with a recurring price for a subscription or subscription schedule to be created.

  - `subscription_data.billing_mode` (object)
    The [billing mode](https://docs.stripe.com/api/subscriptions/create.md#create_subscription-billing_mode) that will be set on the subscription once the quote is accepted.

    - `subscription_data.billing_mode.flexible` (object, nullable)
      Configure behavior for flexible billing mode

      - `subscription_data.billing_mode.flexible.proration_discounts` (enum)
        Controls how invoices and invoice items display proration amounts and discount amounts.
Possible enum values:
        - `included`
          Amounts are net of discounts, and discount amounts are zero.

        - `itemized`
          Amounts are gross of discounts, and discount amounts are accurate.

    - `subscription_data.billing_mode.type` (enum)
      Controls how prorations and invoices for subscriptions are calculated and orchestrated.
Possible enum values:
      - `classic`
        Calculations for subscriptions and invoices are based on legacy defaults.

      - `flexible`
        Supports more flexible calculation and orchestration options for subscriptions and invoices.

  - `subscription_data.description` (string, nullable)
    The subscription’s description, meant to be displayable to the customer. Use this field to optionally store an explanation of the subscription for rendering in Stripe surfaces and certain local payment methods UIs.

  - `subscription_data.effective_date` (timestamp, nullable)
    When creating a new subscription, the date of which the subscription schedule will start after the quote is accepted. This date is ignored if it is in the past when the quote is accepted. Measured in seconds since the Unix epoch.

  - `subscription_data.metadata` (object, nullable)
    Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that will set metadata on the subscription or subscription schedule when the quote is accepted. If a recurring price is included in `line_items`, this field will be passed to the resulting subscription’s `metadata` field. If `subscription_data.effective_date` is used, this field will be passed to the resulting subscription schedule’s `phases.metadata` field. Unlike object-level metadata, this field is declarative. Updates will clear prior values.

  - `subscription_data.trial_period_days` (integer, nullable)
    Integer representing the number of trial period days before the customer is charged for the first time.

- `subscription_schedule` (string, nullable)
  The subscription schedule that was created or updated from this quote.

- `test_clock` (string, nullable)
  ID of the test clock this quote belongs to.

- `total_details` (object)
  Tax and discount details for the computed total amount.

  - `total_details.amount_discount` (integer)
    This is the sum of all the discounts.

  - `total_details.amount_shipping` (integer, nullable)
    This is the sum of all the shipping amounts.

  - `total_details.amount_tax` (integer)
    This is the sum of all the tax amounts.

  - `total_details.breakdown` (object, nullable)
    Breakdown of individual tax and discount amounts that add up to the totals.

    - `total_details.breakdown.discounts` (array of objects)
      The aggregated discounts.

      - `total_details.breakdown.discounts.amount` (integer)
        The amount discounted.

      - `total_details.breakdown.discounts.discount` (object)
        The discount applied.

        - `total_details.breakdown.discounts.discount.id` (string)
          The ID of the discount object. Discounts cannot be fetched by ID. Use `expand[]=discounts` in API calls to expand discount IDs in an array.

        - `total_details.breakdown.discounts.discount.object` (string)
          String representing the object’s type. Objects of the same type share the same value.

        - `total_details.breakdown.discounts.discount.checkout_session` (string, nullable)
          The Checkout session that this coupon is applied to, if it is applied to a particular session in payment mode. Will not be present for subscription mode.

        - `total_details.breakdown.discounts.discount.customer` (string, nullable)
          The ID of the customer associated with this discount.

        - `total_details.breakdown.discounts.discount.customer_account` (string, nullable)
          The ID of the account representing the customer associated with this discount.

        - `total_details.breakdown.discounts.discount.end` (timestamp, nullable)
          If the coupon has a duration of `repeating`, the date that this discount will end. If the coupon has a duration of `once` or `forever`, this attribute will be null.

        - `total_details.breakdown.discounts.discount.invoice` (string, nullable)
          The invoice that the discount’s coupon was applied to, if it was applied directly to a particular invoice.

        - `total_details.breakdown.discounts.discount.invoice_item` (string, nullable)
          The invoice item `id` (or invoice line item `id` for invoice line items of type=‘subscription’) that the discount’s coupon was applied to, if it was applied directly to a particular invoice item or invoice line item.

        - `total_details.breakdown.discounts.discount.promotion_code` (string, nullable)
          The promotion code applied to create this discount.

        - `total_details.breakdown.discounts.discount.source` (object)
          The source of the discount.

          - `total_details.breakdown.discounts.discount.source.coupon` (string, nullable)
            The coupon that was redeemed to create this discount.

          - `total_details.breakdown.discounts.discount.source.type` (enum)
            The source type of the discount.
Possible enum values:
            - `coupon`
              Coupon source type

        - `total_details.breakdown.discounts.discount.start` (timestamp)
          Date that the coupon was applied.

        - `total_details.breakdown.discounts.discount.subscription` (string, nullable)
          The subscription that this coupon is applied to, if it is applied to a particular subscription.

        - `total_details.breakdown.discounts.discount.subscription_item` (string, nullable)
          The subscription item that this coupon is applied to, if it is applied to a particular subscription item.

    - `total_details.breakdown.taxes` (array of objects)
      The aggregated tax amounts by rate.

      - `total_details.breakdown.taxes.amount` (integer)
        Amount of tax applied for this rate.

      - `total_details.breakdown.taxes.rate` (object)
        The tax rate applied.

        - `total_details.breakdown.taxes.rate.id` (string)
          Unique identifier for the object.

        - `total_details.breakdown.taxes.rate.object` (string)
          String representing the object’s type. Objects of the same type share the same value.

        - `total_details.breakdown.taxes.rate.active` (boolean)
          Defaults to `true`. When set to `false`, this tax rate cannot be used with new applications or Checkout Sessions, but will still work for subscriptions and invoices that already have it set.

        - `total_details.breakdown.taxes.rate.country` (string, nullable)
          Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

        - `total_details.breakdown.taxes.rate.created` (timestamp)
          Time at which the object was created. Measured in seconds since the Unix epoch.

        - `total_details.breakdown.taxes.rate.description` (string, nullable)
          An arbitrary string attached to the tax rate for your internal use only. It will not be visible to your customers.

        - `total_details.breakdown.taxes.rate.display_name` (string)
          The display name of the tax rates as it will appear to your customer on their receipt email, PDF, and the hosted invoice page.

        - `total_details.breakdown.taxes.rate.effective_percentage` (float, nullable)
          Actual/effective tax rate percentage out of 100. For tax calculations with automatic_tax[enabled]=true, this percentage reflects the rate actually used to calculate tax based on the product’s taxability and whether the user is registered to collect taxes in the corresponding jurisdiction.

        - `total_details.breakdown.taxes.rate.flat_amount` (object, nullable)
          The amount of the tax rate when the `rate_type` is `flat_amount`. Tax rates with `rate_type` `percentage` can vary based on the transaction, resulting in this field being `null`. This field exposes the amount and currency of the flat tax rate.

          - `total_details.breakdown.taxes.rate.flat_amount.amount` (integer)
            Amount of the tax when the `rate_type` is `flat_amount`. This positive integer represents how much to charge in the smallest currency unit (e.g., 100 cents to charge $1.00 or 100 to charge ¥100, a zero-decimal currency). The amount value supports up to eight digits (e.g., a value of 99999999 for a USD charge of $999,999.99).

          - `total_details.breakdown.taxes.rate.flat_amount.currency` (string)
            Three-letter ISO currency code, in lowercase.

        - `total_details.breakdown.taxes.rate.inclusive` (boolean)
          This specifies if the tax rate is inclusive or exclusive.

        - `total_details.breakdown.taxes.rate.jurisdiction` (string, nullable)
          The jurisdiction for the tax rate. You can use this label field for tax reporting purposes. It also appears on your customer’s invoice.

        - `total_details.breakdown.taxes.rate.jurisdiction_level` (enum, nullable)
          The level of the jurisdiction that imposes this tax rate. Will be `null` for manually defined tax rates.
Possible enum values:
          - `city`
          - `country`
          - `county`
          - `district`
          - `multiple`
          - `state`

        - `total_details.breakdown.taxes.rate.livemode` (boolean)
          Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.

        - `total_details.breakdown.taxes.rate.metadata` (object, nullable)
          Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

        - `total_details.breakdown.taxes.rate.percentage` (float)
          Tax rate percentage out of 100. For tax calculations with automatic_tax[enabled]=true, this percentage includes the statutory tax rate of non-taxable jurisdictions.

        - `total_details.breakdown.taxes.rate.rate_type` (enum, nullable)
          Indicates the type of tax rate applied to the taxable amount. This value can be `null` when no tax applies to the location. This field is only present for TaxRates created by Stripe Tax.
Possible enum values:
          - `flat_amount`
            A fixed amount applied as tax, regardless of the taxable amount, such as a retail delivery fee.

          - `percentage`
            A tax rate expressed as a percentage of the taxable amount, such as the sales tax rate in California.

        - `total_details.breakdown.taxes.rate.state` (string, nullable)
          [ISO 3166-2 subdivision code](https://en.wikipedia.org/wiki/ISO_3166-2), without country prefix. For example, “NY” for New York, United States.

        - `total_details.breakdown.taxes.rate.tax_type` (enum, nullable)
          The high-level tax type, such as `vat` or `sales_tax`.
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

      - `total_details.breakdown.taxes.taxability_reason` (enum, nullable)
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

      - `total_details.breakdown.taxes.taxable_amount` (integer, nullable)
        The amount on which tax is calculated, in cents.

- `transfer_data` (object, nullable)
  The account (if any) the payments will be attributed to for tax reporting, and where funds from each payment will be transferred to for each of the invoices.

  - `transfer_data.amount` (integer, nullable)
    The amount in cents that will be transferred to the destination account when the invoice is paid. By default, the entire amount is transferred to the destination.

  - `transfer_data.amount_percent` (float, nullable)
    A non-negative decimal between 0 and 100, with at most two decimal places. This represents the percentage of the subscription invoice total that will be transferred to the destination account. By default, the entire amount will be transferred to the destination.

  - `transfer_data.destination` (string)
    The account where funds from the payment will be transferred to upon payment success.

### The Quote object

```json
{
  "id": "qt_1Mr7wVLkdIwHu7ixJYSiPTGq",
  "object": "quote",
  "amount_subtotal": 2198,
  "amount_total": 2198,
  "application": null,
  "application_fee_amount": null,
  "application_fee_percent": null,
  "automatic_tax": {
    "enabled": false,
    "liability": null,
    "status": null
  },
  "collection_method": "charge_automatically",
  "computed": {
    "recurring": null,
    "upfront": {
      "amount_subtotal": 2198,
      "amount_total": 2198,
      "total_details": {
        "amount_discount": 0,
        "amount_shipping": 0,
        "amount_tax": 0
      }
    }
  },
  "created": 1680130691,
  "currency": "usd",
  "customer": "cus_NcMfB0SSFHINCV",
  "default_tax_rates": [],
  "description": null,
  "discounts": [],
  "expires_at": 1682722691,
  "footer": null,
  "from_quote": null,
  "header": null,
  "invoice": null,
  "invoice_settings": {
    "days_until_due": null,
    "issuer": {
      "type": "self"
    }
  },
  "livemode": false,
  "metadata": {},
  "number": null,
  "on_behalf_of": null,
  "status": "draft",
  "status_transitions": {
    "accepted_at": null,
    "canceled_at": null,
    "finalized_at": null
  },
  "subscription": null,
  "subscription_data": {
    "description": null,
    "effective_date": null,
    "trial_period_days": null
  },
  "subscription_schedule": null,
  "test_clock": null,
  "total_details": {
    "amount_discount": 0,
    "amount_shipping": 0,
    "amount_tax": 0
  },
  "transfer_data": null
}
```