# List accounts

Returns a list of Accounts.

## Parameters

- `applied_configurations` (array of enums, optional)
  Filter only accounts that have all of the configurations specified. If omitted, returns all accounts regardless of which configurations they have.
Possible enum values:
  - `customer`
    The Account can be used as a customer.

  - `merchant`
    The Account can be used as a merchant.

  - `recipient`
    The Account can be used as a recipient.

- `closed` (boolean, optional)
  Filter by whether the account is closed. If omitted, returns only Accounts that are not closed.

- `limit` (integer, optional)
  The upper limit on the number of accounts returned by the List Account request.

- `page` (string, optional)
  The page token to navigate to next or previous batch of accounts given by the list request.

## Returns

## Response attributes

- `data` (array of objects)
  A list of retrieved Account objects.

  - `data.id` (string)
    Unique identifier for the Account.

  - `data.object` (string, value is "v2.core.account")
    String representing the object’s type. Objects of the same type share the same value of the object field.

  - `data.applied_configurations` (array of enums)
    The configurations that have been applied to this account.
Possible enum values:
    - `customer`
      The Account can be used as a customer.

    - `merchant`
      The Account can be used as a merchant.

    - `recipient`
      The Account can be used as a recipient.

  - `data.closed` (boolean, nullable)
    Indicates whether the account has been closed.

  - `data.configuration` (object, nullable)
    An Account represents a company, individual, or other entity that a user interacts with. Accounts store identity information and one or more configurations that enable product-specific capabilities. You can assign configurations at creation or add them later.

    - `data.configuration.customer` (object, nullable)
      The Customer Configuration allows the Account to be used in inbound payment flows.

      - `data.configuration.customer.applied` (boolean)
        Indicates whether the customer configuration is active. You can deactivate or reactivate the customer configuration by updating this property. Deactivating the configuration by setting this value to false will unrequest all capabilities within the configuration. It will not delete any of the configuration’s other properties.

      - `data.configuration.customer.automatic_indirect_tax` (object, nullable)
        Settings for automatic indirect tax calculation on the customer’s invoices, subscriptions, Checkout Sessions, and Payment Links. Available when automatic tax calculation is available for the customer account’s location.

        - `data.configuration.customer.automatic_indirect_tax.exempt` (enum, nullable)
          The customer account’s tax exemption status: `none`, `exempt`, or `reverse`. When `reverse`, invoice and receipt PDFs include “Reverse charge”.
Possible enum values:
          - `exempt`
            The customer is tax-exempt.

          - `none`
            The customer is not tax-exempt.

          - `reverse`
            Reverse charge applies.

        - `data.configuration.customer.automatic_indirect_tax.ip_address` (string, nullable)
          A recent IP address of the customer used for tax reporting and tax location inference.

        - `data.configuration.customer.automatic_indirect_tax.location` (object, nullable)
          The customer account’s identified tax location, derived from `location_source`. Only rendered if the `automatic_indirect_tax` feature is requested and `active`.

          - `data.configuration.customer.automatic_indirect_tax.location.country` (enum, nullable)
            The identified tax country of the customer.

          - `data.configuration.customer.automatic_indirect_tax.location.state` (string, nullable)
            The identified tax state, county, province, or region of the customer.

        - `data.configuration.customer.automatic_indirect_tax.location_source` (enum, nullable)
          Data source used to identify the customer account’s tax location. Defaults to `identity_address`. Used for automatic indirect tax calculation.
Possible enum values:
          - `identity_address`
            Identity address (`identity.business_details.address` or `identity.individual.address`).

          - `ip_address`
            IP address.

          - `payment_method`
            The customer’s default payment method, unless a default payment method is set on the subscription or invoice.

          - `shipping_address`
            Shipping address.

      - `data.configuration.customer.billing` (object, nullable)
        Default Billing settings for the customer account, used in Invoices and Subscriptions.

        - `data.configuration.customer.billing.default_payment_method` (string, nullable)
          ID of a PaymentMethod attached to the customer account to use as the default for invoices and subscriptions.

        - `data.configuration.customer.billing.invoice` (object, nullable)
          Default invoice settings for the customer account.

          - `data.configuration.customer.billing.invoice.custom_fields` (array of objects)
            The list of up to 4 default custom fields to be displayed on invoices for this customer. When updating, pass an empty string to remove previously-defined fields.

            - `data.configuration.customer.billing.invoice.custom_fields.name` (string)
              The name of the custom field. This may be up to 40 characters.

            - `data.configuration.customer.billing.invoice.custom_fields.value` (string)
              The value of the custom field. This may be up to 140 characters. When updating, pass an empty string to remove previously-defined values.

          - `data.configuration.customer.billing.invoice.footer` (string, nullable)
            Default invoice footer.

          - `data.configuration.customer.billing.invoice.next_sequence` (integer, nullable)
            Sequence number to use on the customer account’s next invoice. Defaults to 1.

          - `data.configuration.customer.billing.invoice.prefix` (string, nullable)
            Prefix used to generate unique invoice numbers. Must be 3-12 uppercase letters or numbers.

          - `data.configuration.customer.billing.invoice.rendering` (object, nullable)
            Default invoice PDF rendering options.

            - `data.configuration.customer.billing.invoice.rendering.amount_tax_display` (enum, nullable)
              Indicates whether displayed line item prices and amounts on invoice PDFs include inclusive tax amounts. Must be either `include_inclusive_tax` or `exclude_tax`.
Possible enum values:
              - `exclude_tax`
                Exclude tax.

              - `include_inclusive_tax`
                Include inclusive tax.

            - `data.configuration.customer.billing.invoice.rendering.template` (string, nullable)
              ID of the invoice rendering template to use for future invoices.

      - `data.configuration.customer.capabilities` (object, nullable)
        Capabilities that have been requested on the Customer Configuration.

        - `data.configuration.customer.capabilities.automatic_indirect_tax` (object, nullable)
          Generates requirements for enabling automatic indirect tax calculation on this customer’s invoices or subscriptions. Recommended to request this capability if planning to enable automatic tax calculation on this customer’s invoices or subscriptions.

          - `data.configuration.customer.capabilities.automatic_indirect_tax.status` (enum)
            The status of the Capability.
Possible enum values:
            - `active`
              The Capability is active.

            - `pending`
              Stripe is carrying out an action prior to activating the Capability. No further action is required at this time.

            - `restricted`
              The Capability requires further action before it can be activated, check the `status_details` for information on why.

            - `unsupported`
              The Capability is unsupported. Check `status_details` for information on why.

          - `data.configuration.customer.capabilities.automatic_indirect_tax.status_details` (array of objects)
            Additional details about the capability’s status. This value is empty when `status` is `active`.

            - `data.configuration.customer.capabilities.automatic_indirect_tax.status_details.code` (enum)
              Machine-readable code explaining the reason for the Capability to be in its current status.
Possible enum values:
              - `determining_status`
                Stripe is in the process of determining the capability’s status.

              - `requirements_past_due`
                Some required information is past due.

              - `requirements_pending_verification`
                Stripe is currently verifying information that was supplied about the Account.

              - `restricted_other`
                Capability is restricted for unspecified reasons.

              - `unsupported_business`
                Capability is not supported for the Account’s business as expressed by the MCC in the Merchant Configuration.

              - `unsupported_country`
                Capability is not supported for the Account’s Legal Entity country.

              - `unsupported_entity_type`
                Capability is not supported for the given Identity entity type (i.e. individual).

            - `data.configuration.customer.capabilities.automatic_indirect_tax.status_details.resolution` (enum)
              Machine-readable code explaining how to make the Capability active.
Possible enum values:
              - `contact_stripe`
                Contact Stripe support to find more information about why this Capability is restricted.

              - `no_resolution`
                No action is required from the user.

              - `provide_info`
                Provide outstanding information about the Account to enable this Capability. Check the Requirements resource for more details.

      - `data.configuration.customer.shipping` (object, nullable)
        The customer’s shipping information. Appears on invoices emailed to this customer.

        - `data.configuration.customer.shipping.address` (object, nullable)
          Customer shipping address.

          - `data.configuration.customer.shipping.address.city` (string, nullable)
            City, district, suburb, town, or village.

          - `data.configuration.customer.shipping.address.country` (enum, nullable)
            Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

          - `data.configuration.customer.shipping.address.line1` (string, nullable)
            Address line 1 (e.g., street, PO Box, or company name).

          - `data.configuration.customer.shipping.address.line2` (string, nullable)
            Address line 2 (e.g., apartment, suite, unit, or building).

          - `data.configuration.customer.shipping.address.postal_code` (string, nullable)
            ZIP or postal code.

          - `data.configuration.customer.shipping.address.state` (string, nullable)
            State, county, province, or region.

        - `data.configuration.customer.shipping.name` (string, nullable)
          Customer name.

        - `data.configuration.customer.shipping.phone` (string, nullable)
          Customer phone (including extension).

      - `data.configuration.customer.test_clock` (string, nullable)
        ID of the test clock to attach to the customer. Can only be set on testmode Accounts, and when the Customer Configuration is first set on an Account.

    - `data.configuration.merchant` (object, nullable)
      Enables the Account to act as a connected account and collect payments facilitated by a Connect platform. You must onboard your platform to Connect before you can add this configuration to your connected accounts. Utilize this configuration when the Account will be the Merchant of Record, like with Direct charges or Destination Charges with on_behalf_of set.

      - `data.configuration.merchant.applied` (boolean)
        Indicates whether the merchant configuration is active. You can deactivate or reactivate the merchant configuration by updating this property. Deactivating the configuration by setting this value to false doesn’t delete the configuration’s properties.

      - `data.configuration.merchant.bacs_debit_payments` (object, nullable)
        Settings for Bacs Direct Debit payments.

        - `data.configuration.merchant.bacs_debit_payments.display_name` (string, nullable)
          Display name for Bacs Direct Debit payments.

        - `data.configuration.merchant.bacs_debit_payments.service_user_number` (string, nullable)
          Service User Number (SUN) for Bacs Direct Debit payments.

      - `data.configuration.merchant.branding` (object, nullable)
        Settings used to apply the merchant’s branding to email receipts, invoices, Checkout, and other products.

        - `data.configuration.merchant.branding.icon` (string, nullable)
          ID of a [file upload](https://docs.stripe.com/api/persons/update.md#create_file): An icon for the merchant. Must be square and at least 128px x 128px.

        - `data.configuration.merchant.branding.logo` (string, nullable)
          ID of a [file upload](https://docs.stripe.com/api/persons/update.md#create_file): A logo for the merchant that will be used in Checkout instead of the icon and without the merchant’s name next to it if provided. Must be at least 128px x 128px.

        - `data.configuration.merchant.branding.primary_color` (string, nullable)
          A CSS hex color value representing the primary branding color for the merchant.

        - `data.configuration.merchant.branding.secondary_color` (string, nullable)
          A CSS hex color value representing the secondary branding color for the merchant.

      - `data.configuration.merchant.capabilities` (object, nullable)
        Capabilities that have been requested on the Merchant Configuration.

        - `data.configuration.merchant.capabilities.ach_debit_payments` (object, nullable)
          Allow the merchant to process ACH debit payments.

          - `data.configuration.merchant.capabilities.ach_debit_payments.status` (enum)
            The status of the Capability.
Possible enum values:
            - `active`
              The Capability is active.

            - `pending`
              Stripe is carrying out an action prior to activating the Capability. No further action is required at this time.

            - `restricted`
              The Capability requires further action before it can be activated, check the `status_details` for information on why.

            - `unsupported`
              The Capability is unsupported. Check `status_details` for information on why.

          - `data.configuration.merchant.capabilities.ach_debit_payments.status_details` (array of objects)
            Additional details about the capability’s status. This value is empty when `status` is `active`.

            - `data.configuration.merchant.capabilities.ach_debit_payments.status_details.code` (enum)
              Machine-readable code explaining the reason for the Capability to be in its current status.
Possible enum values:
              - `determining_status`
                Stripe is in the process of determining the capability’s status.

              - `requirements_past_due`
                Some required information is past due.

              - `requirements_pending_verification`
                Stripe is currently verifying information that was supplied about the Account.

              - `restricted_other`
                Capability is restricted for unspecified reasons.

              - `unsupported_business`
                Capability is not supported for the Account’s business as expressed by the MCC in the Merchant Configuration.

              - `unsupported_country`
                Capability is not supported for the Account’s Legal Entity country.

              - `unsupported_entity_type`
                Capability is not supported for the given Identity entity type (i.e. individual).

            - `data.configuration.merchant.capabilities.ach_debit_payments.status_details.resolution` (enum)
              Machine-readable code explaining how to make the Capability active.
Possible enum values:
              - `contact_stripe`
                Contact Stripe support to find more information about why this Capability is restricted.

              - `no_resolution`
                No action is required from the user.

              - `provide_info`
                Provide outstanding information about the Account to enable this Capability. Check the Requirements resource for more details.

        - `data.configuration.merchant.capabilities.acss_debit_payments` (object, nullable)
          Allow the merchant to process ACSS debit payments.

          - `data.configuration.merchant.capabilities.acss_debit_payments.status` (enum)
            The status of the Capability.
Possible enum values:
            - `active`
              The Capability is active.

            - `pending`
              Stripe is carrying out an action prior to activating the Capability. No further action is required at this time.

            - `restricted`
              The Capability requires further action before it can be activated, check the `status_details` for information on why.

            - `unsupported`
              The Capability is unsupported. Check `status_details` for information on why.

          - `data.configuration.merchant.capabilities.acss_debit_payments.status_details` (array of objects)
            Additional details about the capability’s status. This value is empty when `status` is `active`.

            - `data.configuration.merchant.capabilities.acss_debit_payments.status_details.code` (enum)
              Machine-readable code explaining the reason for the Capability to be in its current status.
Possible enum values:
              - `determining_status`
                Stripe is in the process of determining the capability’s status.

              - `requirements_past_due`
                Some required information is past due.

              - `requirements_pending_verification`
                Stripe is currently verifying information that was supplied about the Account.

              - `restricted_other`
                Capability is restricted for unspecified reasons.

              - `unsupported_business`
                Capability is not supported for the Account’s business as expressed by the MCC in the Merchant Configuration.

              - `unsupported_country`
                Capability is not supported for the Account’s Legal Entity country.

              - `unsupported_entity_type`
                Capability is not supported for the given Identity entity type (i.e. individual).

            - `data.configuration.merchant.capabilities.acss_debit_payments.status_details.resolution` (enum)
              Machine-readable code explaining how to make the Capability active.
Possible enum values:
              - `contact_stripe`
                Contact Stripe support to find more information about why this Capability is restricted.

              - `no_resolution`
                No action is required from the user.

              - `provide_info`
                Provide outstanding information about the Account to enable this Capability. Check the Requirements resource for more details.

        - `data.configuration.merchant.capabilities.affirm_payments` (object, nullable)
          Allow the merchant to process Affirm payments.

          - `data.configuration.merchant.capabilities.affirm_payments.status` (enum)
            The status of the Capability.
Possible enum values:
            - `active`
              The Capability is active.

            - `pending`
              Stripe is carrying out an action prior to activating the Capability. No further action is required at this time.

            - `restricted`
              The Capability requires further action before it can be activated, check the `status_details` for information on why.

            - `unsupported`
              The Capability is unsupported. Check `status_details` for information on why.

          - `data.configuration.merchant.capabilities.affirm_payments.status_details` (array of objects)
            Additional details about the capability’s status. This value is empty when `status` is `active`.

            - `data.configuration.merchant.capabilities.affirm_payments.status_details.code` (enum)
              Machine-readable code explaining the reason for the Capability to be in its current status.
Possible enum values:
              - `determining_status`
                Stripe is in the process of determining the capability’s status.

              - `requirements_past_due`
                Some required information is past due.

              - `requirements_pending_verification`
                Stripe is currently verifying information that was supplied about the Account.

              - `restricted_other`
                Capability is restricted for unspecified reasons.

              - `unsupported_business`
                Capability is not supported for the Account’s business as expressed by the MCC in the Merchant Configuration.

              - `unsupported_country`
                Capability is not supported for the Account’s Legal Entity country.

              - `unsupported_entity_type`
                Capability is not supported for the given Identity entity type (i.e. individual).

            - `data.configuration.merchant.capabilities.affirm_payments.status_details.resolution` (enum)
              Machine-readable code explaining how to make the Capability active.
Possible enum values:
              - `contact_stripe`
                Contact Stripe support to find more information about why this Capability is restricted.

              - `no_resolution`
                No action is required from the user.

              - `provide_info`
                Provide outstanding information about the Account to enable this Capability. Check the Requirements resource for more details.

        - `data.configuration.merchant.capabilities.afterpay_clearpay_payments` (object, nullable)
          Allow the merchant to process Afterpay/Clearpay payments.

          - `data.configuration.merchant.capabilities.afterpay_clearpay_payments.status` (enum)
            The status of the Capability.
Possible enum values:
            - `active`
              The Capability is active.

            - `pending`
              Stripe is carrying out an action prior to activating the Capability. No further action is required at this time.

            - `restricted`
              The Capability requires further action before it can be activated, check the `status_details` for information on why.

            - `unsupported`
              The Capability is unsupported. Check `status_details` for information on why.

          - `data.configuration.merchant.capabilities.afterpay_clearpay_payments.status_details` (array of objects)
            Additional details about the capability’s status. This value is empty when `status` is `active`.

            - `data.configuration.merchant.capabilities.afterpay_clearpay_payments.status_details.code` (enum)
              Machine-readable code explaining the reason for the Capability to be in its current status.
Possible enum values:
              - `determining_status`
                Stripe is in the process of determining the capability’s status.

              - `requirements_past_due`
                Some required information is past due.

              - `requirements_pending_verification`
                Stripe is currently verifying information that was supplied about the Account.

              - `restricted_other`
                Capability is restricted for unspecified reasons.

              - `unsupported_business`
                Capability is not supported for the Account’s business as expressed by the MCC in the Merchant Configuration.

              - `unsupported_country`
                Capability is not supported for the Account’s Legal Entity country.

              - `unsupported_entity_type`
                Capability is not supported for the given Identity entity type (i.e. individual).

            - `data.configuration.merchant.capabilities.afterpay_clearpay_payments.status_details.resolution` (enum)
              Machine-readable code explaining how to make the Capability active.
Possible enum values:
              - `contact_stripe`
                Contact Stripe support to find more information about why this Capability is restricted.

              - `no_resolution`
                No action is required from the user.

              - `provide_info`
                Provide outstanding information about the Account to enable this Capability. Check the Requirements resource for more details.

        - `data.configuration.merchant.capabilities.alma_payments` (object, nullable)
          Allow the merchant to process Alma payments.

          - `data.configuration.merchant.capabilities.alma_payments.status` (enum)
            The status of the Capability.
Possible enum values:
            - `active`
              The Capability is active.

            - `pending`
              Stripe is carrying out an action prior to activating the Capability. No further action is required at this time.

            - `restricted`
              The Capability requires further action before it can be activated, check the `status_details` for information on why.

            - `unsupported`
              The Capability is unsupported. Check `status_details` for information on why.

          - `data.configuration.merchant.capabilities.alma_payments.status_details` (array of objects)
            Additional details about the capability’s status. This value is empty when `status` is `active`.

            - `data.configuration.merchant.capabilities.alma_payments.status_details.code` (enum)
              Machine-readable code explaining the reason for the Capability to be in its current status.
Possible enum values:
              - `determining_status`
                Stripe is in the process of determining the capability’s status.

              - `requirements_past_due`
                Some required information is past due.

              - `requirements_pending_verification`
                Stripe is currently verifying information that was supplied about the Account.

              - `restricted_other`
                Capability is restricted for unspecified reasons.

              - `unsupported_business`
                Capability is not supported for the Account’s business as expressed by the MCC in the Merchant Configuration.

              - `unsupported_country`
                Capability is not supported for the Account’s Legal Entity country.

              - `unsupported_entity_type`
                Capability is not supported for the given Identity entity type (i.e. individual).

            - `data.configuration.merchant.capabilities.alma_payments.status_details.resolution` (enum)
              Machine-readable code explaining how to make the Capability active.
Possible enum values:
              - `contact_stripe`
                Contact Stripe support to find more information about why this Capability is restricted.

              - `no_resolution`
                No action is required from the user.

              - `provide_info`
                Provide outstanding information about the Account to enable this Capability. Check the Requirements resource for more details.

        - `data.configuration.merchant.capabilities.amazon_pay_payments` (object, nullable)
          Allow the merchant to process Amazon Pay payments.

          - `data.configuration.merchant.capabilities.amazon_pay_payments.status` (enum)
            The status of the Capability.
Possible enum values:
            - `active`
              The Capability is active.

            - `pending`
              Stripe is carrying out an action prior to activating the Capability. No further action is required at this time.

            - `restricted`
              The Capability requires further action before it can be activated, check the `status_details` for information on why.

            - `unsupported`
              The Capability is unsupported. Check `status_details` for information on why.

          - `data.configuration.merchant.capabilities.amazon_pay_payments.status_details` (array of objects)
            Additional details about the capability’s status. This value is empty when `status` is `active`.

            - `data.configuration.merchant.capabilities.amazon_pay_payments.status_details.code` (enum)
              Machine-readable code explaining the reason for the Capability to be in its current status.
Possible enum values:
              - `determining_status`
                Stripe is in the process of determining the capability’s status.

              - `requirements_past_due`
                Some required information is past due.

              - `requirements_pending_verification`
                Stripe is currently verifying information that was supplied about the Account.

              - `restricted_other`
                Capability is restricted for unspecified reasons.

              - `unsupported_business`
                Capability is not supported for the Account’s business as expressed by the MCC in the Merchant Configuration.

              - `unsupported_country`
                Capability is not supported for the Account’s Legal Entity country.

              - `unsupported_entity_type`
                Capability is not supported for the given Identity entity type (i.e. individual).

            - `data.configuration.merchant.capabilities.amazon_pay_payments.status_details.resolution` (enum)
              Machine-readable code explaining how to make the Capability active.
Possible enum values:
              - `contact_stripe`
                Contact Stripe support to find more information about why this Capability is restricted.

              - `no_resolution`
                No action is required from the user.

              - `provide_info`
                Provide outstanding information about the Account to enable this Capability. Check the Requirements resource for more details.

        - `data.configuration.merchant.capabilities.au_becs_debit_payments` (object, nullable)
          Allow the merchant to process Australian BECS Direct Debit payments.

          - `data.configuration.merchant.capabilities.au_becs_debit_payments.status` (enum)
            The status of the Capability.
Possible enum values:
            - `active`
              The Capability is active.

            - `pending`
              Stripe is carrying out an action prior to activating the Capability. No further action is required at this time.

            - `restricted`
              The Capability requires further action before it can be activated, check the `status_details` for information on why.

            - `unsupported`
              The Capability is unsupported. Check `status_details` for information on why.

          - `data.configuration.merchant.capabilities.au_becs_debit_payments.status_details` (array of objects)
            Additional details about the capability’s status. This value is empty when `status` is `active`.

            - `data.configuration.merchant.capabilities.au_becs_debit_payments.status_details.code` (enum)
              Machine-readable code explaining the reason for the Capability to be in its current status.
Possible enum values:
              - `determining_status`
                Stripe is in the process of determining the capability’s status.

              - `requirements_past_due`
                Some required information is past due.

              - `requirements_pending_verification`
                Stripe is currently verifying information that was supplied about the Account.

              - `restricted_other`
                Capability is restricted for unspecified reasons.

              - `unsupported_business`
                Capability is not supported for the Account’s business as expressed by the MCC in the Merchant Configuration.

              - `unsupported_country`
                Capability is not supported for the Account’s Legal Entity country.

              - `unsupported_entity_type`
                Capability is not supported for the given Identity entity type (i.e. individual).

            - `data.configuration.merchant.capabilities.au_becs_debit_payments.status_details.resolution` (enum)
              Machine-readable code explaining how to make the Capability active.
Possible enum values:
              - `contact_stripe`
                Contact Stripe support to find more information about why this Capability is restricted.

              - `no_resolution`
                No action is required from the user.

              - `provide_info`
                Provide outstanding information about the Account to enable this Capability. Check the Requirements resource for more details.

        - `data.configuration.merchant.capabilities.bacs_debit_payments` (object, nullable)
          Allow the merchant to process BACS Direct Debit payments.

          - `data.configuration.merchant.capabilities.bacs_debit_payments.status` (enum)
            The status of the Capability.
Possible enum values:
            - `active`
              The Capability is active.

            - `pending`
              Stripe is carrying out an action prior to activating the Capability. No further action is required at this time.

            - `restricted`
              The Capability requires further action before it can be activated, check the `status_details` for information on why.

            - `unsupported`
              The Capability is unsupported. Check `status_details` for information on why.

          - `data.configuration.merchant.capabilities.bacs_debit_payments.status_details` (array of objects)
            Additional details about the capability’s status. This value is empty when `status` is `active`.

            - `data.configuration.merchant.capabilities.bacs_debit_payments.status_details.code` (enum)
              Machine-readable code explaining the reason for the Capability to be in its current status.
Possible enum values:
              - `determining_status`
                Stripe is in the process of determining the capability’s status.

              - `requirements_past_due`
                Some required information is past due.

              - `requirements_pending_verification`
                Stripe is currently verifying information that was supplied about the Account.

              - `restricted_other`
                Capability is restricted for unspecified reasons.

              - `unsupported_business`
                Capability is not supported for the Account’s business as expressed by the MCC in the Merchant Configuration.

              - `unsupported_country`
                Capability is not supported for the Account’s Legal Entity country.

              - `unsupported_entity_type`
                Capability is not supported for the given Identity entity type (i.e. individual).

            - `data.configuration.merchant.capabilities.bacs_debit_payments.status_details.resolution` (enum)
              Machine-readable code explaining how to make the Capability active.
Possible enum values:
              - `contact_stripe`
                Contact Stripe support to find more information about why this Capability is restricted.

              - `no_resolution`
                No action is required from the user.

              - `provide_info`
                Provide outstanding information about the Account to enable this Capability. Check the Requirements resource for more details.

        - `data.configuration.merchant.capabilities.bancontact_payments` (object, nullable)
          Allow the merchant to process Bancontact payments.

          - `data.configuration.merchant.capabilities.bancontact_payments.status` (enum)
            The status of the Capability.
Possible enum values:
            - `active`
              The Capability is active.

            - `pending`
              Stripe is carrying out an action prior to activating the Capability. No further action is required at this time.

            - `restricted`
              The Capability requires further action before it can be activated, check the `status_details` for information on why.

            - `unsupported`
              The Capability is unsupported. Check `status_details` for information on why.

          - `data.configuration.merchant.capabilities.bancontact_payments.status_details` (array of objects)
            Additional details about the capability’s status. This value is empty when `status` is `active`.

            - `data.configuration.merchant.capabilities.bancontact_payments.status_details.code` (enum)
              Machine-readable code explaining the reason for the Capability to be in its current status.
Possible enum values:
              - `determining_status`
                Stripe is in the process of determining the capability’s status.

              - `requirements_past_due`
                Some required information is past due.

              - `requirements_pending_verification`
                Stripe is currently verifying information that was supplied about the Account.

              - `restricted_other`
                Capability is restricted for unspecified reasons.

              - `unsupported_business`
                Capability is not supported for the Account’s business as expressed by the MCC in the Merchant Configuration.

              - `unsupported_country`
                Capability is not supported for the Account’s Legal Entity country.

              - `unsupported_entity_type`
                Capability is not supported for the given Identity entity type (i.e. individual).

            - `data.configuration.merchant.capabilities.bancontact_payments.status_details.resolution` (enum)
              Machine-readable code explaining how to make the Capability active.
Possible enum values:
              - `contact_stripe`
                Contact Stripe support to find more information about why this Capability is restricted.

              - `no_resolution`
                No action is required from the user.

              - `provide_info`
                Provide outstanding information about the Account to enable this Capability. Check the Requirements resource for more details.

        - `data.configuration.merchant.capabilities.blik_payments` (object, nullable)
          Allow the merchant to process BLIK payments.

          - `data.configuration.merchant.capabilities.blik_payments.status` (enum)
            The status of the Capability.
Possible enum values:
            - `active`
              The Capability is active.

            - `pending`
              Stripe is carrying out an action prior to activating the Capability. No further action is required at this time.

            - `restricted`
              The Capability requires further action before it can be activated, check the `status_details` for information on why.

            - `unsupported`
              The Capability is unsupported. Check `status_details` for information on why.

          - `data.configuration.merchant.capabilities.blik_payments.status_details` (array of objects)
            Additional details about the capability’s status. This value is empty when `status` is `active`.

            - `data.configuration.merchant.capabilities.blik_payments.status_details.code` (enum)
              Machine-readable code explaining the reason for the Capability to be in its current status.
Possible enum values:
              - `determining_status`
                Stripe is in the process of determining the capability’s status.

              - `requirements_past_due`
                Some required information is past due.

              - `requirements_pending_verification`
                Stripe is currently verifying information that was supplied about the Account.

              - `restricted_other`
                Capability is restricted for unspecified reasons.

              - `unsupported_business`
                Capability is not supported for the Account’s business as expressed by the MCC in the Merchant Configuration.

              - `unsupported_country`
                Capability is not supported for the Account’s Legal Entity country.

              - `unsupported_entity_type`
                Capability is not supported for the given Identity entity type (i.e. individual).

            - `data.configuration.merchant.capabilities.blik_payments.status_details.resolution` (enum)
              Machine-readable code explaining how to make the Capability active.
Possible enum values:
              - `contact_stripe`
                Contact Stripe support to find more information about why this Capability is restricted.

              - `no_resolution`
                No action is required from the user.

              - `provide_info`
                Provide outstanding information about the Account to enable this Capability. Check the Requirements resource for more details.

        - `data.configuration.merchant.capabilities.boleto_payments` (object, nullable)
          Allow the merchant to process Boleto payments.

          - `data.configuration.merchant.capabilities.boleto_payments.status` (enum)
            The status of the Capability.
Possible enum values:
            - `active`
              The Capability is active.

            - `pending`
              Stripe is carrying out an action prior to activating the Capability. No further action is required at this time.

            - `restricted`
              The Capability requires further action before it can be activated, check the `status_details` for information on why.

            - `unsupported`
              The Capability is unsupported. Check `status_details` for information on why.

          - `data.configuration.merchant.capabilities.boleto_payments.status_details` (array of objects)
            Additional details about the capability’s status. This value is empty when `status` is `active`.

            - `data.configuration.merchant.capabilities.boleto_payments.status_details.code` (enum)
              Machine-readable code explaining the reason for the Capability to be in its current status.
Possible enum values:
              - `determining_status`
                Stripe is in the process of determining the capability’s status.

              - `requirements_past_due`
                Some required information is past due.

              - `requirements_pending_verification`
                Stripe is currently verifying information that was supplied about the Account.

              - `restricted_other`
                Capability is restricted for unspecified reasons.

              - `unsupported_business`
                Capability is not supported for the Account’s business as expressed by the MCC in the Merchant Configuration.

              - `unsupported_country`
                Capability is not supported for the Account’s Legal Entity country.

              - `unsupported_entity_type`
                Capability is not supported for the given Identity entity type (i.e. individual).

            - `data.configuration.merchant.capabilities.boleto_payments.status_details.resolution` (enum)
              Machine-readable code explaining how to make the Capability active.
Possible enum values:
              - `contact_stripe`
                Contact Stripe support to find more information about why this Capability is restricted.

              - `no_resolution`
                No action is required from the user.

              - `provide_info`
                Provide outstanding information about the Account to enable this Capability. Check the Requirements resource for more details.

        - `data.configuration.merchant.capabilities.card_payments` (object, nullable)
          Allow the merchant to collect card payments.

          - `data.configuration.merchant.capabilities.card_payments.status` (enum)
            The status of the Capability.
Possible enum values:
            - `active`
              The Capability is active.

            - `pending`
              Stripe is carrying out an action prior to activating the Capability. No further action is required at this time.

            - `restricted`
              The Capability requires further action before it can be activated, check the `status_details` for information on why.

            - `unsupported`
              The Capability is unsupported. Check `status_details` for information on why.

          - `data.configuration.merchant.capabilities.card_payments.status_details` (array of objects)
            Additional details about the capability’s status. This value is empty when `status` is `active`.

            - `data.configuration.merchant.capabilities.card_payments.status_details.code` (enum)
              Machine-readable code explaining the reason for the Capability to be in its current status.
Possible enum values:
              - `determining_status`
                Stripe is in the process of determining the capability’s status.

              - `requirements_past_due`
                Some required information is past due.

              - `requirements_pending_verification`
                Stripe is currently verifying information that was supplied about the Account.

              - `restricted_other`
                Capability is restricted for unspecified reasons.

              - `unsupported_business`
                Capability is not supported for the Account’s business as expressed by the MCC in the Merchant Configuration.

              - `unsupported_country`
                Capability is not supported for the Account’s Legal Entity country.

              - `unsupported_entity_type`
                Capability is not supported for the given Identity entity type (i.e. individual).

            - `data.configuration.merchant.capabilities.card_payments.status_details.resolution` (enum)
              Machine-readable code explaining how to make the Capability active.
Possible enum values:
              - `contact_stripe`
                Contact Stripe support to find more information about why this Capability is restricted.

              - `no_resolution`
                No action is required from the user.

              - `provide_info`
                Provide outstanding information about the Account to enable this Capability. Check the Requirements resource for more details.

        - `data.configuration.merchant.capabilities.cartes_bancaires_payments` (object, nullable)
          Allow the merchant to process Cartes Bancaires payments.

          - `data.configuration.merchant.capabilities.cartes_bancaires_payments.status` (enum)
            The status of the Capability.
Possible enum values:
            - `active`
              The Capability is active.

            - `pending`
              Stripe is carrying out an action prior to activating the Capability. No further action is required at this time.

            - `restricted`
              The Capability requires further action before it can be activated, check the `status_details` for information on why.

            - `unsupported`
              The Capability is unsupported. Check `status_details` for information on why.

          - `data.configuration.merchant.capabilities.cartes_bancaires_payments.status_details` (array of objects)
            Additional details about the capability’s status. This value is empty when `status` is `active`.

            - `data.configuration.merchant.capabilities.cartes_bancaires_payments.status_details.code` (enum)
              Machine-readable code explaining the reason for the Capability to be in its current status.
Possible enum values:
              - `determining_status`
                Stripe is in the process of determining the capability’s status.

              - `requirements_past_due`
                Some required information is past due.

              - `requirements_pending_verification`
                Stripe is currently verifying information that was supplied about the Account.

              - `restricted_other`
                Capability is restricted for unspecified reasons.

              - `unsupported_business`
                Capability is not supported for the Account’s business as expressed by the MCC in the Merchant Configuration.

              - `unsupported_country`
                Capability is not supported for the Account’s Legal Entity country.

              - `unsupported_entity_type`
                Capability is not supported for the given Identity entity type (i.e. individual).

            - `data.configuration.merchant.capabilities.cartes_bancaires_payments.status_details.resolution` (enum)
              Machine-readable code explaining how to make the Capability active.
Possible enum values:
              - `contact_stripe`
                Contact Stripe support to find more information about why this Capability is restricted.

              - `no_resolution`
                No action is required from the user.

              - `provide_info`
                Provide outstanding information about the Account to enable this Capability. Check the Requirements resource for more details.

        - `data.configuration.merchant.capabilities.cashapp_payments` (object, nullable)
          Allow the merchant to process Cash App payments.

          - `data.configuration.merchant.capabilities.cashapp_payments.status` (enum)
            The status of the Capability.
Possible enum values:
            - `active`
              The Capability is active.

            - `pending`
              Stripe is carrying out an action prior to activating the Capability. No further action is required at this time.

            - `restricted`
              The Capability requires further action before it can be activated, check the `status_details` for information on why.

            - `unsupported`
              The Capability is unsupported. Check `status_details` for information on why.

          - `data.configuration.merchant.capabilities.cashapp_payments.status_details` (array of objects)
            Additional details about the capability’s status. This value is empty when `status` is `active`.

            - `data.configuration.merchant.capabilities.cashapp_payments.status_details.code` (enum)
              Machine-readable code explaining the reason for the Capability to be in its current status.
Possible enum values:
              - `determining_status`
                Stripe is in the process of determining the capability’s status.

              - `requirements_past_due`
                Some required information is past due.

              - `requirements_pending_verification`
                Stripe is currently verifying information that was supplied about the Account.

              - `restricted_other`
                Capability is restricted for unspecified reasons.

              - `unsupported_business`
                Capability is not supported for the Account’s business as expressed by the MCC in the Merchant Configuration.

              - `unsupported_country`
                Capability is not supported for the Account’s Legal Entity country.

              - `unsupported_entity_type`
                Capability is not supported for the given Identity entity type (i.e. individual).

            - `data.configuration.merchant.capabilities.cashapp_payments.status_details.resolution` (enum)
              Machine-readable code explaining how to make the Capability active.
Possible enum values:
              - `contact_stripe`
                Contact Stripe support to find more information about why this Capability is restricted.

              - `no_resolution`
                No action is required from the user.

              - `provide_info`
                Provide outstanding information about the Account to enable this Capability. Check the Requirements resource for more details.

        - `data.configuration.merchant.capabilities.eps_payments` (object, nullable)
          Allow the merchant to process EPS payments.

          - `data.configuration.merchant.capabilities.eps_payments.status` (enum)
            The status of the Capability.
Possible enum values:
            - `active`
              The Capability is active.

            - `pending`
              Stripe is carrying out an action prior to activating the Capability. No further action is required at this time.

            - `restricted`
              The Capability requires further action before it can be activated, check the `status_details` for information on why.

            - `unsupported`
              The Capability is unsupported. Check `status_details` for information on why.

          - `data.configuration.merchant.capabilities.eps_payments.status_details` (array of objects)
            Additional details about the capability’s status. This value is empty when `status` is `active`.

            - `data.configuration.merchant.capabilities.eps_payments.status_details.code` (enum)
              Machine-readable code explaining the reason for the Capability to be in its current status.
Possible enum values:
              - `determining_status`
                Stripe is in the process of determining the capability’s status.

              - `requirements_past_due`
                Some required information is past due.

              - `requirements_pending_verification`
                Stripe is currently verifying information that was supplied about the Account.

              - `restricted_other`
                Capability is restricted for unspecified reasons.

              - `unsupported_business`
                Capability is not supported for the Account’s business as expressed by the MCC in the Merchant Configuration.

              - `unsupported_country`
                Capability is not supported for the Account’s Legal Entity country.

              - `unsupported_entity_type`
                Capability is not supported for the given Identity entity type (i.e. individual).

            - `data.configuration.merchant.capabilities.eps_payments.status_details.resolution` (enum)
              Machine-readable code explaining how to make the Capability active.
Possible enum values:
              - `contact_stripe`
                Contact Stripe support to find more information about why this Capability is restricted.

              - `no_resolution`
                No action is required from the user.

              - `provide_info`
                Provide outstanding information about the Account to enable this Capability. Check the Requirements resource for more details.

        - `data.configuration.merchant.capabilities.fpx_payments` (object, nullable)
          Allow the merchant to process FPX payments.

          - `data.configuration.merchant.capabilities.fpx_payments.status` (enum)
            The status of the Capability.
Possible enum values:
            - `active`
              The Capability is active.

            - `pending`
              Stripe is carrying out an action prior to activating the Capability. No further action is required at this time.

            - `restricted`
              The Capability requires further action before it can be activated, check the `status_details` for information on why.

            - `unsupported`
              The Capability is unsupported. Check `status_details` for information on why.

          - `data.configuration.merchant.capabilities.fpx_payments.status_details` (array of objects)
            Additional details about the capability’s status. This value is empty when `status` is `active`.

            - `data.configuration.merchant.capabilities.fpx_payments.status_details.code` (enum)
              Machine-readable code explaining the reason for the Capability to be in its current status.
Possible enum values:
              - `determining_status`
                Stripe is in the process of determining the capability’s status.

              - `requirements_past_due`
                Some required information is past due.

              - `requirements_pending_verification`
                Stripe is currently verifying information that was supplied about the Account.

              - `restricted_other`
                Capability is restricted for unspecified reasons.

              - `unsupported_business`
                Capability is not supported for the Account’s business as expressed by the MCC in the Merchant Configuration.

              - `unsupported_country`
                Capability is not supported for the Account’s Legal Entity country.

              - `unsupported_entity_type`
                Capability is not supported for the given Identity entity type (i.e. individual).

            - `data.configuration.merchant.capabilities.fpx_payments.status_details.resolution` (enum)
              Machine-readable code explaining how to make the Capability active.
Possible enum values:
              - `contact_stripe`
                Contact Stripe support to find more information about why this Capability is restricted.

              - `no_resolution`
                No action is required from the user.

              - `provide_info`
                Provide outstanding information about the Account to enable this Capability. Check the Requirements resource for more details.

        - `data.configuration.merchant.capabilities.gb_bank_transfer_payments` (object, nullable)
          Allow the merchant to process UK bank transfer payments.

          - `data.configuration.merchant.capabilities.gb_bank_transfer_payments.status` (enum)
            The status of the Capability.
Possible enum values:
            - `active`
              The Capability is active.

            - `pending`
              Stripe is carrying out an action prior to activating the Capability. No further action is required at this time.

            - `restricted`
              The Capability requires further action before it can be activated, check the `status_details` for information on why.

            - `unsupported`
              The Capability is unsupported. Check `status_details` for information on why.

          - `data.configuration.merchant.capabilities.gb_bank_transfer_payments.status_details` (array of objects)
            Additional details about the capability’s status. This value is empty when `status` is `active`.

            - `data.configuration.merchant.capabilities.gb_bank_transfer_payments.status_details.code` (enum)
              Machine-readable code explaining the reason for the Capability to be in its current status.
Possible enum values:
              - `determining_status`
                Stripe is in the process of determining the capability’s status.

              - `requirements_past_due`
                Some required information is past due.

              - `requirements_pending_verification`
                Stripe is currently verifying information that was supplied about the Account.

              - `restricted_other`
                Capability is restricted for unspecified reasons.

              - `unsupported_business`
                Capability is not supported for the Account’s business as expressed by the MCC in the Merchant Configuration.

              - `unsupported_country`
                Capability is not supported for the Account’s Legal Entity country.

              - `unsupported_entity_type`
                Capability is not supported for the given Identity entity type (i.e. individual).

            - `data.configuration.merchant.capabilities.gb_bank_transfer_payments.status_details.resolution` (enum)
              Machine-readable code explaining how to make the Capability active.
Possible enum values:
              - `contact_stripe`
                Contact Stripe support to find more information about why this Capability is restricted.

              - `no_resolution`
                No action is required from the user.

              - `provide_info`
                Provide outstanding information about the Account to enable this Capability. Check the Requirements resource for more details.

        - `data.configuration.merchant.capabilities.grabpay_payments` (object, nullable)
          Allow the merchant to process GrabPay payments.

          - `data.configuration.merchant.capabilities.grabpay_payments.status` (enum)
            The status of the Capability.
Possible enum values:
            - `active`
              The Capability is active.

            - `pending`
              Stripe is carrying out an action prior to activating the Capability. No further action is required at this time.

            - `restricted`
              The Capability requires further action before it can be activated, check the `status_details` for information on why.

            - `unsupported`
              The Capability is unsupported. Check `status_details` for information on why.

          - `data.configuration.merchant.capabilities.grabpay_payments.status_details` (array of objects)
            Additional details about the capability’s status. This value is empty when `status` is `active`.

            - `data.configuration.merchant.capabilities.grabpay_payments.status_details.code` (enum)
              Machine-readable code explaining the reason for the Capability to be in its current status.
Possible enum values:
              - `determining_status`
                Stripe is in the process of determining the capability’s status.

              - `requirements_past_due`
                Some required information is past due.

              - `requirements_pending_verification`
                Stripe is currently verifying information that was supplied about the Account.

              - `restricted_other`
                Capability is restricted for unspecified reasons.

              - `unsupported_business`
                Capability is not supported for the Account’s business as expressed by the MCC in the Merchant Configuration.

              - `unsupported_country`
                Capability is not supported for the Account’s Legal Entity country.

              - `unsupported_entity_type`
                Capability is not supported for the given Identity entity type (i.e. individual).

            - `data.configuration.merchant.capabilities.grabpay_payments.status_details.resolution` (enum)
              Machine-readable code explaining how to make the Capability active.
Possible enum values:
              - `contact_stripe`
                Contact Stripe support to find more information about why this Capability is restricted.

              - `no_resolution`
                No action is required from the user.

              - `provide_info`
                Provide outstanding information about the Account to enable this Capability. Check the Requirements resource for more details.

        - `data.configuration.merchant.capabilities.ideal_payments` (object, nullable)
          Allow the merchant to process iDEAL payments.

          - `data.configuration.merchant.capabilities.ideal_payments.status` (enum)
            The status of the Capability.
Possible enum values:
            - `active`
              The Capability is active.

            - `pending`
              Stripe is carrying out an action prior to activating the Capability. No further action is required at this time.

            - `restricted`
              The Capability requires further action before it can be activated, check the `status_details` for information on why.

            - `unsupported`
              The Capability is unsupported. Check `status_details` for information on why.

          - `data.configuration.merchant.capabilities.ideal_payments.status_details` (array of objects)
            Additional details about the capability’s status. This value is empty when `status` is `active`.

            - `data.configuration.merchant.capabilities.ideal_payments.status_details.code` (enum)
              Machine-readable code explaining the reason for the Capability to be in its current status.
Possible enum values:
              - `determining_status`
                Stripe is in the process of determining the capability’s status.

              - `requirements_past_due`
                Some required information is past due.

              - `requirements_pending_verification`
                Stripe is currently verifying information that was supplied about the Account.

              - `restricted_other`
                Capability is restricted for unspecified reasons.

              - `unsupported_business`
                Capability is not supported for the Account’s business as expressed by the MCC in the Merchant Configuration.

              - `unsupported_country`
                Capability is not supported for the Account’s Legal Entity country.

              - `unsupported_entity_type`
                Capability is not supported for the given Identity entity type (i.e. individual).

            - `data.configuration.merchant.capabilities.ideal_payments.status_details.resolution` (enum)
              Machine-readable code explaining how to make the Capability active.
Possible enum values:
              - `contact_stripe`
                Contact Stripe support to find more information about why this Capability is restricted.

              - `no_resolution`
                No action is required from the user.

              - `provide_info`
                Provide outstanding information about the Account to enable this Capability. Check the Requirements resource for more details.

        - `data.configuration.merchant.capabilities.jcb_payments` (object, nullable)
          Allow the merchant to process JCB card payments.

          - `data.configuration.merchant.capabilities.jcb_payments.status` (enum)
            The status of the Capability.
Possible enum values:
            - `active`
              The Capability is active.

            - `pending`
              Stripe is carrying out an action prior to activating the Capability. No further action is required at this time.

            - `restricted`
              The Capability requires further action before it can be activated, check the `status_details` for information on why.

            - `unsupported`
              The Capability is unsupported. Check `status_details` for information on why.

          - `data.configuration.merchant.capabilities.jcb_payments.status_details` (array of objects)
            Additional details about the capability’s status. This value is empty when `status` is `active`.

            - `data.configuration.merchant.capabilities.jcb_payments.status_details.code` (enum)
              Machine-readable code explaining the reason for the Capability to be in its current status.
Possible enum values:
              - `determining_status`
                Stripe is in the process of determining the capability’s status.

              - `requirements_past_due`
                Some required information is past due.

              - `requirements_pending_verification`
                Stripe is currently verifying information that was supplied about the Account.

              - `restricted_other`
                Capability is restricted for unspecified reasons.

              - `unsupported_business`
                Capability is not supported for the Account’s business as expressed by the MCC in the Merchant Configuration.

              - `unsupported_country`
                Capability is not supported for the Account’s Legal Entity country.

              - `unsupported_entity_type`
                Capability is not supported for the given Identity entity type (i.e. individual).

            - `data.configuration.merchant.capabilities.jcb_payments.status_details.resolution` (enum)
              Machine-readable code explaining how to make the Capability active.
Possible enum values:
              - `contact_stripe`
                Contact Stripe support to find more information about why this Capability is restricted.

              - `no_resolution`
                No action is required from the user.

              - `provide_info`
                Provide outstanding information about the Account to enable this Capability. Check the Requirements resource for more details.

        - `data.configuration.merchant.capabilities.jp_bank_transfer_payments` (object, nullable)
          Allow the merchant to process Japanese bank transfer payments.

          - `data.configuration.merchant.capabilities.jp_bank_transfer_payments.status` (enum)
            The status of the Capability.
Possible enum values:
            - `active`
              The Capability is active.

            - `pending`
              Stripe is carrying out an action prior to activating the Capability. No further action is required at this time.

            - `restricted`
              The Capability requires further action before it can be activated, check the `status_details` for information on why.

            - `unsupported`
              The Capability is unsupported. Check `status_details` for information on why.

          - `data.configuration.merchant.capabilities.jp_bank_transfer_payments.status_details` (array of objects)
            Additional details about the capability’s status. This value is empty when `status` is `active`.

            - `data.configuration.merchant.capabilities.jp_bank_transfer_payments.status_details.code` (enum)
              Machine-readable code explaining the reason for the Capability to be in its current status.
Possible enum values:
              - `determining_status`
                Stripe is in the process of determining the capability’s status.

              - `requirements_past_due`
                Some required information is past due.

              - `requirements_pending_verification`
                Stripe is currently verifying information that was supplied about the Account.

              - `restricted_other`
                Capability is restricted for unspecified reasons.

              - `unsupported_business`
                Capability is not supported for the Account’s business as expressed by the MCC in the Merchant Configuration.

              - `unsupported_country`
                Capability is not supported for the Account’s Legal Entity country.

              - `unsupported_entity_type`
                Capability is not supported for the given Identity entity type (i.e. individual).

            - `data.configuration.merchant.capabilities.jp_bank_transfer_payments.status_details.resolution` (enum)
              Machine-readable code explaining how to make the Capability active.
Possible enum values:
              - `contact_stripe`
                Contact Stripe support to find more information about why this Capability is restricted.

              - `no_resolution`
                No action is required from the user.

              - `provide_info`
                Provide outstanding information about the Account to enable this Capability. Check the Requirements resource for more details.

        - `data.configuration.merchant.capabilities.kakao_pay_payments` (object, nullable)
          Allow the merchant to process Kakao Pay payments.

          - `data.configuration.merchant.capabilities.kakao_pay_payments.status` (enum)
            The status of the Capability.
Possible enum values:
            - `active`
              The Capability is active.

            - `pending`
              Stripe is carrying out an action prior to activating the Capability. No further action is required at this time.

            - `restricted`
              The Capability requires further action before it can be activated, check the `status_details` for information on why.

            - `unsupported`
              The Capability is unsupported. Check `status_details` for information on why.

          - `data.configuration.merchant.capabilities.kakao_pay_payments.status_details` (array of objects)
            Additional details about the capability’s status. This value is empty when `status` is `active`.

            - `data.configuration.merchant.capabilities.kakao_pay_payments.status_details.code` (enum)
              Machine-readable code explaining the reason for the Capability to be in its current status.
Possible enum values:
              - `determining_status`
                Stripe is in the process of determining the capability’s status.

              - `requirements_past_due`
                Some required information is past due.

              - `requirements_pending_verification`
                Stripe is currently verifying information that was supplied about the Account.

              - `restricted_other`
                Capability is restricted for unspecified reasons.

              - `unsupported_business`
                Capability is not supported for the Account’s business as expressed by the MCC in the Merchant Configuration.

              - `unsupported_country`
                Capability is not supported for the Account’s Legal Entity country.

              - `unsupported_entity_type`
                Capability is not supported for the given Identity entity type (i.e. individual).

            - `data.configuration.merchant.capabilities.kakao_pay_payments.status_details.resolution` (enum)
              Machine-readable code explaining how to make the Capability active.
Possible enum values:
              - `contact_stripe`
                Contact Stripe support to find more information about why this Capability is restricted.

              - `no_resolution`
                No action is required from the user.

              - `provide_info`
                Provide outstanding information about the Account to enable this Capability. Check the Requirements resource for more details.

        - `data.configuration.merchant.capabilities.klarna_payments` (object, nullable)
          Allow the merchant to process Klarna payments.

          - `data.configuration.merchant.capabilities.klarna_payments.status` (enum)
            The status of the Capability.
Possible enum values:
            - `active`
              The Capability is active.

            - `pending`
              Stripe is carrying out an action prior to activating the Capability. No further action is required at this time.

            - `restricted`
              The Capability requires further action before it can be activated, check the `status_details` for information on why.

            - `unsupported`
              The Capability is unsupported. Check `status_details` for information on why.

          - `data.configuration.merchant.capabilities.klarna_payments.status_details` (array of objects)
            Additional details about the capability’s status. This value is empty when `status` is `active`.

            - `data.configuration.merchant.capabilities.klarna_payments.status_details.code` (enum)
              Machine-readable code explaining the reason for the Capability to be in its current status.
Possible enum values:
              - `determining_status`
                Stripe is in the process of determining the capability’s status.

              - `requirements_past_due`
                Some required information is past due.

              - `requirements_pending_verification`
                Stripe is currently verifying information that was supplied about the Account.

              - `restricted_other`
                Capability is restricted for unspecified reasons.

              - `unsupported_business`
                Capability is not supported for the Account’s business as expressed by the MCC in the Merchant Configuration.

              - `unsupported_country`
                Capability is not supported for the Account’s Legal Entity country.

              - `unsupported_entity_type`
                Capability is not supported for the given Identity entity type (i.e. individual).

            - `data.configuration.merchant.capabilities.klarna_payments.status_details.resolution` (enum)
              Machine-readable code explaining how to make the Capability active.
Possible enum values:
              - `contact_stripe`
                Contact Stripe support to find more information about why this Capability is restricted.

              - `no_resolution`
                No action is required from the user.

              - `provide_info`
                Provide outstanding information about the Account to enable this Capability. Check the Requirements resource for more details.

        - `data.configuration.merchant.capabilities.konbini_payments` (object, nullable)
          Allow the merchant to process Konbini convenience store payments.

          - `data.configuration.merchant.capabilities.konbini_payments.status` (enum)
            The status of the Capability.
Possible enum values:
            - `active`
              The Capability is active.

            - `pending`
              Stripe is carrying out an action prior to activating the Capability. No further action is required at this time.

            - `restricted`
              The Capability requires further action before it can be activated, check the `status_details` for information on why.

            - `unsupported`
              The Capability is unsupported. Check `status_details` for information on why.

          - `data.configuration.merchant.capabilities.konbini_payments.status_details` (array of objects)
            Additional details about the capability’s status. This value is empty when `status` is `active`.

            - `data.configuration.merchant.capabilities.konbini_payments.status_details.code` (enum)
              Machine-readable code explaining the reason for the Capability to be in its current status.
Possible enum values:
              - `determining_status`
                Stripe is in the process of determining the capability’s status.

              - `requirements_past_due`
                Some required information is past due.

              - `requirements_pending_verification`
                Stripe is currently verifying information that was supplied about the Account.

              - `restricted_other`
                Capability is restricted for unspecified reasons.

              - `unsupported_business`
                Capability is not supported for the Account’s business as expressed by the MCC in the Merchant Configuration.

              - `unsupported_country`
                Capability is not supported for the Account’s Legal Entity country.

              - `unsupported_entity_type`
                Capability is not supported for the given Identity entity type (i.e. individual).

            - `data.configuration.merchant.capabilities.konbini_payments.status_details.resolution` (enum)
              Machine-readable code explaining how to make the Capability active.
Possible enum values:
              - `contact_stripe`
                Contact Stripe support to find more information about why this Capability is restricted.

              - `no_resolution`
                No action is required from the user.

              - `provide_info`
                Provide outstanding information about the Account to enable this Capability. Check the Requirements resource for more details.

        - `data.configuration.merchant.capabilities.kr_card_payments` (object, nullable)
          Allow the merchant to process Korean card payments.

          - `data.configuration.merchant.capabilities.kr_card_payments.status` (enum)
            The status of the Capability.
Possible enum values:
            - `active`
              The Capability is active.

            - `pending`
              Stripe is carrying out an action prior to activating the Capability. No further action is required at this time.

            - `restricted`
              The Capability requires further action before it can be activated, check the `status_details` for information on why.

            - `unsupported`
              The Capability is unsupported. Check `status_details` for information on why.

          - `data.configuration.merchant.capabilities.kr_card_payments.status_details` (array of objects)
            Additional details about the capability’s status. This value is empty when `status` is `active`.

            - `data.configuration.merchant.capabilities.kr_card_payments.status_details.code` (enum)
              Machine-readable code explaining the reason for the Capability to be in its current status.
Possible enum values:
              - `determining_status`
                Stripe is in the process of determining the capability’s status.

              - `requirements_past_due`
                Some required information is past due.

              - `requirements_pending_verification`
                Stripe is currently verifying information that was supplied about the Account.

              - `restricted_other`
                Capability is restricted for unspecified reasons.

              - `unsupported_business`
                Capability is not supported for the Account’s business as expressed by the MCC in the Merchant Configuration.

              - `unsupported_country`
                Capability is not supported for the Account’s Legal Entity country.

              - `unsupported_entity_type`
                Capability is not supported for the given Identity entity type (i.e. individual).

            - `data.configuration.merchant.capabilities.kr_card_payments.status_details.resolution` (enum)
              Machine-readable code explaining how to make the Capability active.
Possible enum values:
              - `contact_stripe`
                Contact Stripe support to find more information about why this Capability is restricted.

              - `no_resolution`
                No action is required from the user.

              - `provide_info`
                Provide outstanding information about the Account to enable this Capability. Check the Requirements resource for more details.

        - `data.configuration.merchant.capabilities.link_payments` (object, nullable)
          Allow the merchant to process Link payments.

          - `data.configuration.merchant.capabilities.link_payments.status` (enum)
            The status of the Capability.
Possible enum values:
            - `active`
              The Capability is active.

            - `pending`
              Stripe is carrying out an action prior to activating the Capability. No further action is required at this time.

            - `restricted`
              The Capability requires further action before it can be activated, check the `status_details` for information on why.

            - `unsupported`
              The Capability is unsupported. Check `status_details` for information on why.

          - `data.configuration.merchant.capabilities.link_payments.status_details` (array of objects)
            Additional details about the capability’s status. This value is empty when `status` is `active`.

            - `data.configuration.merchant.capabilities.link_payments.status_details.code` (enum)
              Machine-readable code explaining the reason for the Capability to be in its current status.
Possible enum values:
              - `determining_status`
                Stripe is in the process of determining the capability’s status.

              - `requirements_past_due`
                Some required information is past due.

              - `requirements_pending_verification`
                Stripe is currently verifying information that was supplied about the Account.

              - `restricted_other`
                Capability is restricted for unspecified reasons.

              - `unsupported_business`
                Capability is not supported for the Account’s business as expressed by the MCC in the Merchant Configuration.

              - `unsupported_country`
                Capability is not supported for the Account’s Legal Entity country.

              - `unsupported_entity_type`
                Capability is not supported for the given Identity entity type (i.e. individual).

            - `data.configuration.merchant.capabilities.link_payments.status_details.resolution` (enum)
              Machine-readable code explaining how to make the Capability active.
Possible enum values:
              - `contact_stripe`
                Contact Stripe support to find more information about why this Capability is restricted.

              - `no_resolution`
                No action is required from the user.

              - `provide_info`
                Provide outstanding information about the Account to enable this Capability. Check the Requirements resource for more details.

        - `data.configuration.merchant.capabilities.mobilepay_payments` (object, nullable)
          Allow the merchant to process MobilePay payments.

          - `data.configuration.merchant.capabilities.mobilepay_payments.status` (enum)
            The status of the Capability.
Possible enum values:
            - `active`
              The Capability is active.

            - `pending`
              Stripe is carrying out an action prior to activating the Capability. No further action is required at this time.

            - `restricted`
              The Capability requires further action before it can be activated, check the `status_details` for information on why.

            - `unsupported`
              The Capability is unsupported. Check `status_details` for information on why.

          - `data.configuration.merchant.capabilities.mobilepay_payments.status_details` (array of objects)
            Additional details about the capability’s status. This value is empty when `status` is `active`.

            - `data.configuration.merchant.capabilities.mobilepay_payments.status_details.code` (enum)
              Machine-readable code explaining the reason for the Capability to be in its current status.
Possible enum values:
              - `determining_status`
                Stripe is in the process of determining the capability’s status.

              - `requirements_past_due`
                Some required information is past due.

              - `requirements_pending_verification`
                Stripe is currently verifying information that was supplied about the Account.

              - `restricted_other`
                Capability is restricted for unspecified reasons.

              - `unsupported_business`
                Capability is not supported for the Account’s business as expressed by the MCC in the Merchant Configuration.

              - `unsupported_country`
                Capability is not supported for the Account’s Legal Entity country.

              - `unsupported_entity_type`
                Capability is not supported for the given Identity entity type (i.e. individual).

            - `data.configuration.merchant.capabilities.mobilepay_payments.status_details.resolution` (enum)
              Machine-readable code explaining how to make the Capability active.
Possible enum values:
              - `contact_stripe`
                Contact Stripe support to find more information about why this Capability is restricted.

              - `no_resolution`
                No action is required from the user.

              - `provide_info`
                Provide outstanding information about the Account to enable this Capability. Check the Requirements resource for more details.

        - `data.configuration.merchant.capabilities.multibanco_payments` (object, nullable)
          Allow the merchant to process Multibanco payments.

          - `data.configuration.merchant.capabilities.multibanco_payments.status` (enum)
            The status of the Capability.
Possible enum values:
            - `active`
              The Capability is active.

            - `pending`
              Stripe is carrying out an action prior to activating the Capability. No further action is required at this time.

            - `restricted`
              The Capability requires further action before it can be activated, check the `status_details` for information on why.

            - `unsupported`
              The Capability is unsupported. Check `status_details` for information on why.

          - `data.configuration.merchant.capabilities.multibanco_payments.status_details` (array of objects)
            Additional details about the capability’s status. This value is empty when `status` is `active`.

            - `data.configuration.merchant.capabilities.multibanco_payments.status_details.code` (enum)
              Machine-readable code explaining the reason for the Capability to be in its current status.
Possible enum values:
              - `determining_status`
                Stripe is in the process of determining the capability’s status.

              - `requirements_past_due`
                Some required information is past due.

              - `requirements_pending_verification`
                Stripe is currently verifying information that was supplied about the Account.

              - `restricted_other`
                Capability is restricted for unspecified reasons.

              - `unsupported_business`
                Capability is not supported for the Account’s business as expressed by the MCC in the Merchant Configuration.

              - `unsupported_country`
                Capability is not supported for the Account’s Legal Entity country.

              - `unsupported_entity_type`
                Capability is not supported for the given Identity entity type (i.e. individual).

            - `data.configuration.merchant.capabilities.multibanco_payments.status_details.resolution` (enum)
              Machine-readable code explaining how to make the Capability active.
Possible enum values:
              - `contact_stripe`
                Contact Stripe support to find more information about why this Capability is restricted.

              - `no_resolution`
                No action is required from the user.

              - `provide_info`
                Provide outstanding information about the Account to enable this Capability. Check the Requirements resource for more details.

        - `data.configuration.merchant.capabilities.mx_bank_transfer_payments` (object, nullable)
          Allow the merchant to process Mexican bank transfer payments.

          - `data.configuration.merchant.capabilities.mx_bank_transfer_payments.status` (enum)
            The status of the Capability.
Possible enum values:
            - `active`
              The Capability is active.

            - `pending`
              Stripe is carrying out an action prior to activating the Capability. No further action is required at this time.

            - `restricted`
              The Capability requires further action before it can be activated, check the `status_details` for information on why.

            - `unsupported`
              The Capability is unsupported. Check `status_details` for information on why.

          - `data.configuration.merchant.capabilities.mx_bank_transfer_payments.status_details` (array of objects)
            Additional details about the capability’s status. This value is empty when `status` is `active`.

            - `data.configuration.merchant.capabilities.mx_bank_transfer_payments.status_details.code` (enum)
              Machine-readable code explaining the reason for the Capability to be in its current status.
Possible enum values:
              - `determining_status`
                Stripe is in the process of determining the capability’s status.

              - `requirements_past_due`
                Some required information is past due.

              - `requirements_pending_verification`
                Stripe is currently verifying information that was supplied about the Account.

              - `restricted_other`
                Capability is restricted for unspecified reasons.

              - `unsupported_business`
                Capability is not supported for the Account’s business as expressed by the MCC in the Merchant Configuration.

              - `unsupported_country`
                Capability is not supported for the Account’s Legal Entity country.

              - `unsupported_entity_type`
                Capability is not supported for the given Identity entity type (i.e. individual).

            - `data.configuration.merchant.capabilities.mx_bank_transfer_payments.status_details.resolution` (enum)
              Machine-readable code explaining how to make the Capability active.
Possible enum values:
              - `contact_stripe`
                Contact Stripe support to find more information about why this Capability is restricted.

              - `no_resolution`
                No action is required from the user.

              - `provide_info`
                Provide outstanding information about the Account to enable this Capability. Check the Requirements resource for more details.

        - `data.configuration.merchant.capabilities.naver_pay_payments` (object, nullable)
          Allow the merchant to process Naver Pay payments.

          - `data.configuration.merchant.capabilities.naver_pay_payments.status` (enum)
            The status of the Capability.
Possible enum values:
            - `active`
              The Capability is active.

            - `pending`
              Stripe is carrying out an action prior to activating the Capability. No further action is required at this time.

            - `restricted`
              The Capability requires further action before it can be activated, check the `status_details` for information on why.

            - `unsupported`
              The Capability is unsupported. Check `status_details` for information on why.

          - `data.configuration.merchant.capabilities.naver_pay_payments.status_details` (array of objects)
            Additional details about the capability’s status. This value is empty when `status` is `active`.

            - `data.configuration.merchant.capabilities.naver_pay_payments.status_details.code` (enum)
              Machine-readable code explaining the reason for the Capability to be in its current status.
Possible enum values:
              - `determining_status`
                Stripe is in the process of determining the capability’s status.

              - `requirements_past_due`
                Some required information is past due.

              - `requirements_pending_verification`
                Stripe is currently verifying information that was supplied about the Account.

              - `restricted_other`
                Capability is restricted for unspecified reasons.

              - `unsupported_business`
                Capability is not supported for the Account’s business as expressed by the MCC in the Merchant Configuration.

              - `unsupported_country`
                Capability is not supported for the Account’s Legal Entity country.

              - `unsupported_entity_type`
                Capability is not supported for the given Identity entity type (i.e. individual).

            - `data.configuration.merchant.capabilities.naver_pay_payments.status_details.resolution` (enum)
              Machine-readable code explaining how to make the Capability active.
Possible enum values:
              - `contact_stripe`
                Contact Stripe support to find more information about why this Capability is restricted.

              - `no_resolution`
                No action is required from the user.

              - `provide_info`
                Provide outstanding information about the Account to enable this Capability. Check the Requirements resource for more details.

        - `data.configuration.merchant.capabilities.oxxo_payments` (object, nullable)
          Allow the merchant to process OXXO payments.

          - `data.configuration.merchant.capabilities.oxxo_payments.status` (enum)
            The status of the Capability.
Possible enum values:
            - `active`
              The Capability is active.

            - `pending`
              Stripe is carrying out an action prior to activating the Capability. No further action is required at this time.

            - `restricted`
              The Capability requires further action before it can be activated, check the `status_details` for information on why.

            - `unsupported`
              The Capability is unsupported. Check `status_details` for information on why.

          - `data.configuration.merchant.capabilities.oxxo_payments.status_details` (array of objects)
            Additional details about the capability’s status. This value is empty when `status` is `active`.

            - `data.configuration.merchant.capabilities.oxxo_payments.status_details.code` (enum)
              Machine-readable code explaining the reason for the Capability to be in its current status.
Possible enum values:
              - `determining_status`
                Stripe is in the process of determining the capability’s status.

              - `requirements_past_due`
                Some required information is past due.

              - `requirements_pending_verification`
                Stripe is currently verifying information that was supplied about the Account.

              - `restricted_other`
                Capability is restricted for unspecified reasons.

              - `unsupported_business`
                Capability is not supported for the Account’s business as expressed by the MCC in the Merchant Configuration.

              - `unsupported_country`
                Capability is not supported for the Account’s Legal Entity country.

              - `unsupported_entity_type`
                Capability is not supported for the given Identity entity type (i.e. individual).

            - `data.configuration.merchant.capabilities.oxxo_payments.status_details.resolution` (enum)
              Machine-readable code explaining how to make the Capability active.
Possible enum values:
              - `contact_stripe`
                Contact Stripe support to find more information about why this Capability is restricted.

              - `no_resolution`
                No action is required from the user.

              - `provide_info`
                Provide outstanding information about the Account to enable this Capability. Check the Requirements resource for more details.

        - `data.configuration.merchant.capabilities.p24_payments` (object, nullable)
          Allow the merchant to process Przelewy24 (P24) payments.

          - `data.configuration.merchant.capabilities.p24_payments.status` (enum)
            The status of the Capability.
Possible enum values:
            - `active`
              The Capability is active.

            - `pending`
              Stripe is carrying out an action prior to activating the Capability. No further action is required at this time.

            - `restricted`
              The Capability requires further action before it can be activated, check the `status_details` for information on why.

            - `unsupported`
              The Capability is unsupported. Check `status_details` for information on why.

          - `data.configuration.merchant.capabilities.p24_payments.status_details` (array of objects)
            Additional details about the capability’s status. This value is empty when `status` is `active`.

            - `data.configuration.merchant.capabilities.p24_payments.status_details.code` (enum)
              Machine-readable code explaining the reason for the Capability to be in its current status.
Possible enum values:
              - `determining_status`
                Stripe is in the process of determining the capability’s status.

              - `requirements_past_due`
                Some required information is past due.

              - `requirements_pending_verification`
                Stripe is currently verifying information that was supplied about the Account.

              - `restricted_other`
                Capability is restricted for unspecified reasons.

              - `unsupported_business`
                Capability is not supported for the Account’s business as expressed by the MCC in the Merchant Configuration.

              - `unsupported_country`
                Capability is not supported for the Account’s Legal Entity country.

              - `unsupported_entity_type`
                Capability is not supported for the given Identity entity type (i.e. individual).

            - `data.configuration.merchant.capabilities.p24_payments.status_details.resolution` (enum)
              Machine-readable code explaining how to make the Capability active.
Possible enum values:
              - `contact_stripe`
                Contact Stripe support to find more information about why this Capability is restricted.

              - `no_resolution`
                No action is required from the user.

              - `provide_info`
                Provide outstanding information about the Account to enable this Capability. Check the Requirements resource for more details.

        - `data.configuration.merchant.capabilities.pay_by_bank_payments` (object, nullable)
          Allow the merchant to process Pay by Bank payments.

          - `data.configuration.merchant.capabilities.pay_by_bank_payments.status` (enum)
            The status of the Capability.
Possible enum values:
            - `active`
              The Capability is active.

            - `pending`
              Stripe is carrying out an action prior to activating the Capability. No further action is required at this time.

            - `restricted`
              The Capability requires further action before it can be activated, check the `status_details` for information on why.

            - `unsupported`
              The Capability is unsupported. Check `status_details` for information on why.

          - `data.configuration.merchant.capabilities.pay_by_bank_payments.status_details` (array of objects)
            Additional details about the capability’s status. This value is empty when `status` is `active`.

            - `data.configuration.merchant.capabilities.pay_by_bank_payments.status_details.code` (enum)
              Machine-readable code explaining the reason for the Capability to be in its current status.
Possible enum values:
              - `determining_status`
                Stripe is in the process of determining the capability’s status.

              - `requirements_past_due`
                Some required information is past due.

              - `requirements_pending_verification`
                Stripe is currently verifying information that was supplied about the Account.

              - `restricted_other`
                Capability is restricted for unspecified reasons.

              - `unsupported_business`
                Capability is not supported for the Account’s business as expressed by the MCC in the Merchant Configuration.

              - `unsupported_country`
                Capability is not supported for the Account’s Legal Entity country.

              - `unsupported_entity_type`
                Capability is not supported for the given Identity entity type (i.e. individual).

            - `data.configuration.merchant.capabilities.pay_by_bank_payments.status_details.resolution` (enum)
              Machine-readable code explaining how to make the Capability active.
Possible enum values:
              - `contact_stripe`
                Contact Stripe support to find more information about why this Capability is restricted.

              - `no_resolution`
                No action is required from the user.

              - `provide_info`
                Provide outstanding information about the Account to enable this Capability. Check the Requirements resource for more details.

        - `data.configuration.merchant.capabilities.payco_payments` (object, nullable)
          Allow the merchant to process PAYCO payments.

          - `data.configuration.merchant.capabilities.payco_payments.status` (enum)
            The status of the Capability.
Possible enum values:
            - `active`
              The Capability is active.

            - `pending`
              Stripe is carrying out an action prior to activating the Capability. No further action is required at this time.

            - `restricted`
              The Capability requires further action before it can be activated, check the `status_details` for information on why.

            - `unsupported`
              The Capability is unsupported. Check `status_details` for information on why.

          - `data.configuration.merchant.capabilities.payco_payments.status_details` (array of objects)
            Additional details about the capability’s status. This value is empty when `status` is `active`.

            - `data.configuration.merchant.capabilities.payco_payments.status_details.code` (enum)
              Machine-readable code explaining the reason for the Capability to be in its current status.
Possible enum values:
              - `determining_status`
                Stripe is in the process of determining the capability’s status.

              - `requirements_past_due`
                Some required information is past due.

              - `requirements_pending_verification`
                Stripe is currently verifying information that was supplied about the Account.

              - `restricted_other`
                Capability is restricted for unspecified reasons.

              - `unsupported_business`
                Capability is not supported for the Account’s business as expressed by the MCC in the Merchant Configuration.

              - `unsupported_country`
                Capability is not supported for the Account’s Legal Entity country.

              - `unsupported_entity_type`
                Capability is not supported for the given Identity entity type (i.e. individual).

            - `data.configuration.merchant.capabilities.payco_payments.status_details.resolution` (enum)
              Machine-readable code explaining how to make the Capability active.
Possible enum values:
              - `contact_stripe`
                Contact Stripe support to find more information about why this Capability is restricted.

              - `no_resolution`
                No action is required from the user.

              - `provide_info`
                Provide outstanding information about the Account to enable this Capability. Check the Requirements resource for more details.

        - `data.configuration.merchant.capabilities.paynow_payments` (object, nullable)
          Allow the merchant to process PayNow payments.

          - `data.configuration.merchant.capabilities.paynow_payments.status` (enum)
            The status of the Capability.
Possible enum values:
            - `active`
              The Capability is active.

            - `pending`
              Stripe is carrying out an action prior to activating the Capability. No further action is required at this time.

            - `restricted`
              The Capability requires further action before it can be activated, check the `status_details` for information on why.

            - `unsupported`
              The Capability is unsupported. Check `status_details` for information on why.

          - `data.configuration.merchant.capabilities.paynow_payments.status_details` (array of objects)
            Additional details about the capability’s status. This value is empty when `status` is `active`.

            - `data.configuration.merchant.capabilities.paynow_payments.status_details.code` (enum)
              Machine-readable code explaining the reason for the Capability to be in its current status.
Possible enum values:
              - `determining_status`
                Stripe is in the process of determining the capability’s status.

              - `requirements_past_due`
                Some required information is past due.

              - `requirements_pending_verification`
                Stripe is currently verifying information that was supplied about the Account.

              - `restricted_other`
                Capability is restricted for unspecified reasons.

              - `unsupported_business`
                Capability is not supported for the Account’s business as expressed by the MCC in the Merchant Configuration.

              - `unsupported_country`
                Capability is not supported for the Account’s Legal Entity country.

              - `unsupported_entity_type`
                Capability is not supported for the given Identity entity type (i.e. individual).

            - `data.configuration.merchant.capabilities.paynow_payments.status_details.resolution` (enum)
              Machine-readable code explaining how to make the Capability active.
Possible enum values:
              - `contact_stripe`
                Contact Stripe support to find more information about why this Capability is restricted.

              - `no_resolution`
                No action is required from the user.

              - `provide_info`
                Provide outstanding information about the Account to enable this Capability. Check the Requirements resource for more details.

        - `data.configuration.merchant.capabilities.promptpay_payments` (object, nullable)
          Allow the merchant to process PromptPay payments.

          - `data.configuration.merchant.capabilities.promptpay_payments.status` (enum)
            The status of the Capability.
Possible enum values:
            - `active`
              The Capability is active.

            - `pending`
              Stripe is carrying out an action prior to activating the Capability. No further action is required at this time.

            - `restricted`
              The Capability requires further action before it can be activated, check the `status_details` for information on why.

            - `unsupported`
              The Capability is unsupported. Check `status_details` for information on why.

          - `data.configuration.merchant.capabilities.promptpay_payments.status_details` (array of objects)
            Additional details about the capability’s status. This value is empty when `status` is `active`.

            - `data.configuration.merchant.capabilities.promptpay_payments.status_details.code` (enum)
              Machine-readable code explaining the reason for the Capability to be in its current status.
Possible enum values:
              - `determining_status`
                Stripe is in the process of determining the capability’s status.

              - `requirements_past_due`
                Some required information is past due.

              - `requirements_pending_verification`
                Stripe is currently verifying information that was supplied about the Account.

              - `restricted_other`
                Capability is restricted for unspecified reasons.

              - `unsupported_business`
                Capability is not supported for the Account’s business as expressed by the MCC in the Merchant Configuration.

              - `unsupported_country`
                Capability is not supported for the Account’s Legal Entity country.

              - `unsupported_entity_type`
                Capability is not supported for the given Identity entity type (i.e. individual).

            - `data.configuration.merchant.capabilities.promptpay_payments.status_details.resolution` (enum)
              Machine-readable code explaining how to make the Capability active.
Possible enum values:
              - `contact_stripe`
                Contact Stripe support to find more information about why this Capability is restricted.

              - `no_resolution`
                No action is required from the user.

              - `provide_info`
                Provide outstanding information about the Account to enable this Capability. Check the Requirements resource for more details.

        - `data.configuration.merchant.capabilities.revolut_pay_payments` (object, nullable)
          Allow the merchant to process Revolut Pay payments.

          - `data.configuration.merchant.capabilities.revolut_pay_payments.status` (enum)
            The status of the Capability.
Possible enum values:
            - `active`
              The Capability is active.

            - `pending`
              Stripe is carrying out an action prior to activating the Capability. No further action is required at this time.

            - `restricted`
              The Capability requires further action before it can be activated, check the `status_details` for information on why.

            - `unsupported`
              The Capability is unsupported. Check `status_details` for information on why.

          - `data.configuration.merchant.capabilities.revolut_pay_payments.status_details` (array of objects)
            Additional details about the capability’s status. This value is empty when `status` is `active`.

            - `data.configuration.merchant.capabilities.revolut_pay_payments.status_details.code` (enum)
              Machine-readable code explaining the reason for the Capability to be in its current status.
Possible enum values:
              - `determining_status`
                Stripe is in the process of determining the capability’s status.

              - `requirements_past_due`
                Some required information is past due.

              - `requirements_pending_verification`
                Stripe is currently verifying information that was supplied about the Account.

              - `restricted_other`
                Capability is restricted for unspecified reasons.

              - `unsupported_business`
                Capability is not supported for the Account’s business as expressed by the MCC in the Merchant Configuration.

              - `unsupported_country`
                Capability is not supported for the Account’s Legal Entity country.

              - `unsupported_entity_type`
                Capability is not supported for the given Identity entity type (i.e. individual).

            - `data.configuration.merchant.capabilities.revolut_pay_payments.status_details.resolution` (enum)
              Machine-readable code explaining how to make the Capability active.
Possible enum values:
              - `contact_stripe`
                Contact Stripe support to find more information about why this Capability is restricted.

              - `no_resolution`
                No action is required from the user.

              - `provide_info`
                Provide outstanding information about the Account to enable this Capability. Check the Requirements resource for more details.

        - `data.configuration.merchant.capabilities.samsung_pay_payments` (object, nullable)
          Allow the merchant to process Samsung Pay payments.

          - `data.configuration.merchant.capabilities.samsung_pay_payments.status` (enum)
            The status of the Capability.
Possible enum values:
            - `active`
              The Capability is active.

            - `pending`
              Stripe is carrying out an action prior to activating the Capability. No further action is required at this time.

            - `restricted`
              The Capability requires further action before it can be activated, check the `status_details` for information on why.

            - `unsupported`
              The Capability is unsupported. Check `status_details` for information on why.

          - `data.configuration.merchant.capabilities.samsung_pay_payments.status_details` (array of objects)
            Additional details about the capability’s status. This value is empty when `status` is `active`.

            - `data.configuration.merchant.capabilities.samsung_pay_payments.status_details.code` (enum)
              Machine-readable code explaining the reason for the Capability to be in its current status.
Possible enum values:
              - `determining_status`
                Stripe is in the process of determining the capability’s status.

              - `requirements_past_due`
                Some required information is past due.

              - `requirements_pending_verification`
                Stripe is currently verifying information that was supplied about the Account.

              - `restricted_other`
                Capability is restricted for unspecified reasons.

              - `unsupported_business`
                Capability is not supported for the Account’s business as expressed by the MCC in the Merchant Configuration.

              - `unsupported_country`
                Capability is not supported for the Account’s Legal Entity country.

              - `unsupported_entity_type`
                Capability is not supported for the given Identity entity type (i.e. individual).

            - `data.configuration.merchant.capabilities.samsung_pay_payments.status_details.resolution` (enum)
              Machine-readable code explaining how to make the Capability active.
Possible enum values:
              - `contact_stripe`
                Contact Stripe support to find more information about why this Capability is restricted.

              - `no_resolution`
                No action is required from the user.

              - `provide_info`
                Provide outstanding information about the Account to enable this Capability. Check the Requirements resource for more details.

        - `data.configuration.merchant.capabilities.sepa_bank_transfer_payments` (object, nullable)
          Allow the merchant to process SEPA bank transfer payments.

          - `data.configuration.merchant.capabilities.sepa_bank_transfer_payments.status` (enum)
            The status of the Capability.
Possible enum values:
            - `active`
              The Capability is active.

            - `pending`
              Stripe is carrying out an action prior to activating the Capability. No further action is required at this time.

            - `restricted`
              The Capability requires further action before it can be activated, check the `status_details` for information on why.

            - `unsupported`
              The Capability is unsupported. Check `status_details` for information on why.

          - `data.configuration.merchant.capabilities.sepa_bank_transfer_payments.status_details` (array of objects)
            Additional details about the capability’s status. This value is empty when `status` is `active`.

            - `data.configuration.merchant.capabilities.sepa_bank_transfer_payments.status_details.code` (enum)
              Machine-readable code explaining the reason for the Capability to be in its current status.
Possible enum values:
              - `determining_status`
                Stripe is in the process of determining the capability’s status.

              - `requirements_past_due`
                Some required information is past due.

              - `requirements_pending_verification`
                Stripe is currently verifying information that was supplied about the Account.

              - `restricted_other`
                Capability is restricted for unspecified reasons.

              - `unsupported_business`
                Capability is not supported for the Account’s business as expressed by the MCC in the Merchant Configuration.

              - `unsupported_country`
                Capability is not supported for the Account’s Legal Entity country.

              - `unsupported_entity_type`
                Capability is not supported for the given Identity entity type (i.e. individual).

            - `data.configuration.merchant.capabilities.sepa_bank_transfer_payments.status_details.resolution` (enum)
              Machine-readable code explaining how to make the Capability active.
Possible enum values:
              - `contact_stripe`
                Contact Stripe support to find more information about why this Capability is restricted.

              - `no_resolution`
                No action is required from the user.

              - `provide_info`
                Provide outstanding information about the Account to enable this Capability. Check the Requirements resource for more details.

        - `data.configuration.merchant.capabilities.sepa_debit_payments` (object, nullable)
          Allow the merchant to process SEPA Direct Debit payments.

          - `data.configuration.merchant.capabilities.sepa_debit_payments.status` (enum)
            The status of the Capability.
Possible enum values:
            - `active`
              The Capability is active.

            - `pending`
              Stripe is carrying out an action prior to activating the Capability. No further action is required at this time.

            - `restricted`
              The Capability requires further action before it can be activated, check the `status_details` for information on why.

            - `unsupported`
              The Capability is unsupported. Check `status_details` for information on why.

          - `data.configuration.merchant.capabilities.sepa_debit_payments.status_details` (array of objects)
            Additional details about the capability’s status. This value is empty when `status` is `active`.

            - `data.configuration.merchant.capabilities.sepa_debit_payments.status_details.code` (enum)
              Machine-readable code explaining the reason for the Capability to be in its current status.
Possible enum values:
              - `determining_status`
                Stripe is in the process of determining the capability’s status.

              - `requirements_past_due`
                Some required information is past due.

              - `requirements_pending_verification`
                Stripe is currently verifying information that was supplied about the Account.

              - `restricted_other`
                Capability is restricted for unspecified reasons.

              - `unsupported_business`
                Capability is not supported for the Account’s business as expressed by the MCC in the Merchant Configuration.

              - `unsupported_country`
                Capability is not supported for the Account’s Legal Entity country.

              - `unsupported_entity_type`
                Capability is not supported for the given Identity entity type (i.e. individual).

            - `data.configuration.merchant.capabilities.sepa_debit_payments.status_details.resolution` (enum)
              Machine-readable code explaining how to make the Capability active.
Possible enum values:
              - `contact_stripe`
                Contact Stripe support to find more information about why this Capability is restricted.

              - `no_resolution`
                No action is required from the user.

              - `provide_info`
                Provide outstanding information about the Account to enable this Capability. Check the Requirements resource for more details.

        - `data.configuration.merchant.capabilities.stripe_balance` (object, nullable)
          Capabilities that enable the merchant to manage their Stripe Balance (/v1/balance).

          - `data.configuration.merchant.capabilities.stripe_balance.payouts` (object, nullable)
            Enables this Account to complete payouts from their Stripe Balance (/v1/balance).

            - `data.configuration.merchant.capabilities.stripe_balance.payouts.status` (enum)
              The status of the Capability.
Possible enum values:
              - `active`
                The Capability is active.

              - `pending`
                Stripe is carrying out an action prior to activating the Capability. No further action is required at this time.

              - `restricted`
                The Capability requires further action before it can be activated, check the `status_details` for information on why.

              - `unsupported`
                The Capability is unsupported. Check `status_details` for information on why.

            - `data.configuration.merchant.capabilities.stripe_balance.payouts.status_details` (array of objects)
              Additional details about the capability’s status. This value is empty when `status` is `active`.

              - `data.configuration.merchant.capabilities.stripe_balance.payouts.status_details.code` (enum)
                Machine-readable code explaining the reason for the Capability to be in its current status.
Possible enum values:
                - `determining_status`
                  Stripe is in the process of determining the capability’s status.

                - `requirements_past_due`
                  Some required information is past due.

                - `requirements_pending_verification`
                  Stripe is currently verifying information that was supplied about the Account.

                - `restricted_other`
                  Capability is restricted for unspecified reasons.

                - `unsupported_business`
                  Capability is not supported for the Account’s business as expressed by the MCC in the Merchant Configuration.

                - `unsupported_country`
                  Capability is not supported for the Account’s Legal Entity country.

                - `unsupported_entity_type`
                  Capability is not supported for the given Identity entity type (i.e. individual).

              - `data.configuration.merchant.capabilities.stripe_balance.payouts.status_details.resolution` (enum)
                Machine-readable code explaining how to make the Capability active.
Possible enum values:
                - `contact_stripe`
                  Contact Stripe support to find more information about why this Capability is restricted.

                - `no_resolution`
                  No action is required from the user.

                - `provide_info`
                  Provide outstanding information about the Account to enable this Capability. Check the Requirements resource for more details.

        - `data.configuration.merchant.capabilities.swish_payments` (object, nullable)
          Allow the merchant to process Swish payments.

          - `data.configuration.merchant.capabilities.swish_payments.status` (enum)
            The status of the Capability.
Possible enum values:
            - `active`
              The Capability is active.

            - `pending`
              Stripe is carrying out an action prior to activating the Capability. No further action is required at this time.

            - `restricted`
              The Capability requires further action before it can be activated, check the `status_details` for information on why.

            - `unsupported`
              The Capability is unsupported. Check `status_details` for information on why.

          - `data.configuration.merchant.capabilities.swish_payments.status_details` (array of objects)
            Additional details about the capability’s status. This value is empty when `status` is `active`.

            - `data.configuration.merchant.capabilities.swish_payments.status_details.code` (enum)
              Machine-readable code explaining the reason for the Capability to be in its current status.
Possible enum values:
              - `determining_status`
                Stripe is in the process of determining the capability’s status.

              - `requirements_past_due`
                Some required information is past due.

              - `requirements_pending_verification`
                Stripe is currently verifying information that was supplied about the Account.

              - `restricted_other`
                Capability is restricted for unspecified reasons.

              - `unsupported_business`
                Capability is not supported for the Account’s business as expressed by the MCC in the Merchant Configuration.

              - `unsupported_country`
                Capability is not supported for the Account’s Legal Entity country.

              - `unsupported_entity_type`
                Capability is not supported for the given Identity entity type (i.e. individual).

            - `data.configuration.merchant.capabilities.swish_payments.status_details.resolution` (enum)
              Machine-readable code explaining how to make the Capability active.
Possible enum values:
              - `contact_stripe`
                Contact Stripe support to find more information about why this Capability is restricted.

              - `no_resolution`
                No action is required from the user.

              - `provide_info`
                Provide outstanding information about the Account to enable this Capability. Check the Requirements resource for more details.

        - `data.configuration.merchant.capabilities.twint_payments` (object, nullable)
          Allow the merchant to process TWINT payments.

          - `data.configuration.merchant.capabilities.twint_payments.status` (enum)
            The status of the Capability.
Possible enum values:
            - `active`
              The Capability is active.

            - `pending`
              Stripe is carrying out an action prior to activating the Capability. No further action is required at this time.

            - `restricted`
              The Capability requires further action before it can be activated, check the `status_details` for information on why.

            - `unsupported`
              The Capability is unsupported. Check `status_details` for information on why.

          - `data.configuration.merchant.capabilities.twint_payments.status_details` (array of objects)
            Additional details about the capability’s status. This value is empty when `status` is `active`.

            - `data.configuration.merchant.capabilities.twint_payments.status_details.code` (enum)
              Machine-readable code explaining the reason for the Capability to be in its current status.
Possible enum values:
              - `determining_status`
                Stripe is in the process of determining the capability’s status.

              - `requirements_past_due`
                Some required information is past due.

              - `requirements_pending_verification`
                Stripe is currently verifying information that was supplied about the Account.

              - `restricted_other`
                Capability is restricted for unspecified reasons.

              - `unsupported_business`
                Capability is not supported for the Account’s business as expressed by the MCC in the Merchant Configuration.

              - `unsupported_country`
                Capability is not supported for the Account’s Legal Entity country.

              - `unsupported_entity_type`
                Capability is not supported for the given Identity entity type (i.e. individual).

            - `data.configuration.merchant.capabilities.twint_payments.status_details.resolution` (enum)
              Machine-readable code explaining how to make the Capability active.
Possible enum values:
              - `contact_stripe`
                Contact Stripe support to find more information about why this Capability is restricted.

              - `no_resolution`
                No action is required from the user.

              - `provide_info`
                Provide outstanding information about the Account to enable this Capability. Check the Requirements resource for more details.

        - `data.configuration.merchant.capabilities.us_bank_transfer_payments` (object, nullable)
          Allow the merchant to process US bank transfer payments.

          - `data.configuration.merchant.capabilities.us_bank_transfer_payments.status` (enum)
            The status of the Capability.
Possible enum values:
            - `active`
              The Capability is active.

            - `pending`
              Stripe is carrying out an action prior to activating the Capability. No further action is required at this time.

            - `restricted`
              The Capability requires further action before it can be activated, check the `status_details` for information on why.

            - `unsupported`
              The Capability is unsupported. Check `status_details` for information on why.

          - `data.configuration.merchant.capabilities.us_bank_transfer_payments.status_details` (array of objects)
            Additional details about the capability’s status. This value is empty when `status` is `active`.

            - `data.configuration.merchant.capabilities.us_bank_transfer_payments.status_details.code` (enum)
              Machine-readable code explaining the reason for the Capability to be in its current status.
Possible enum values:
              - `determining_status`
                Stripe is in the process of determining the capability’s status.

              - `requirements_past_due`
                Some required information is past due.

              - `requirements_pending_verification`
                Stripe is currently verifying information that was supplied about the Account.

              - `restricted_other`
                Capability is restricted for unspecified reasons.

              - `unsupported_business`
                Capability is not supported for the Account’s business as expressed by the MCC in the Merchant Configuration.

              - `unsupported_country`
                Capability is not supported for the Account’s Legal Entity country.

              - `unsupported_entity_type`
                Capability is not supported for the given Identity entity type (i.e. individual).

            - `data.configuration.merchant.capabilities.us_bank_transfer_payments.status_details.resolution` (enum)
              Machine-readable code explaining how to make the Capability active.
Possible enum values:
              - `contact_stripe`
                Contact Stripe support to find more information about why this Capability is restricted.

              - `no_resolution`
                No action is required from the user.

              - `provide_info`
                Provide outstanding information about the Account to enable this Capability. Check the Requirements resource for more details.

        - `data.configuration.merchant.capabilities.zip_payments` (object, nullable)
          Allow the merchant to process Zip payments.

          - `data.configuration.merchant.capabilities.zip_payments.status` (enum)
            The status of the Capability.
Possible enum values:
            - `active`
              The Capability is active.

            - `pending`
              Stripe is carrying out an action prior to activating the Capability. No further action is required at this time.

            - `restricted`
              The Capability requires further action before it can be activated, check the `status_details` for information on why.

            - `unsupported`
              The Capability is unsupported. Check `status_details` for information on why.

          - `data.configuration.merchant.capabilities.zip_payments.status_details` (array of objects)
            Additional details about the capability’s status. This value is empty when `status` is `active`.

            - `data.configuration.merchant.capabilities.zip_payments.status_details.code` (enum)
              Machine-readable code explaining the reason for the Capability to be in its current status.
Possible enum values:
              - `determining_status`
                Stripe is in the process of determining the capability’s status.

              - `requirements_past_due`
                Some required information is past due.

              - `requirements_pending_verification`
                Stripe is currently verifying information that was supplied about the Account.

              - `restricted_other`
                Capability is restricted for unspecified reasons.

              - `unsupported_business`
                Capability is not supported for the Account’s business as expressed by the MCC in the Merchant Configuration.

              - `unsupported_country`
                Capability is not supported for the Account’s Legal Entity country.

              - `unsupported_entity_type`
                Capability is not supported for the given Identity entity type (i.e. individual).

            - `data.configuration.merchant.capabilities.zip_payments.status_details.resolution` (enum)
              Machine-readable code explaining how to make the Capability active.
Possible enum values:
              - `contact_stripe`
                Contact Stripe support to find more information about why this Capability is restricted.

              - `no_resolution`
                No action is required from the user.

              - `provide_info`
                Provide outstanding information about the Account to enable this Capability. Check the Requirements resource for more details.

      - `data.configuration.merchant.card_payments` (object, nullable)
        Card payments settings.

        - `data.configuration.merchant.card_payments.decline_on` (object, nullable)
          Automatically declines certain charge types regardless of whether the card issuer accepted or declined the charge.

          - `data.configuration.merchant.card_payments.decline_on.avs_failure` (boolean, nullable)
            Whether Stripe automatically declines charges with an incorrect ZIP or postal code. This setting only applies when a ZIP or postal code is provided and they fail bank verification.

          - `data.configuration.merchant.card_payments.decline_on.cvc_failure` (boolean, nullable)
            Whether Stripe automatically declines charges with an incorrect CVC. This setting only applies when a CVC is provided and it fails bank verification.

      - `data.configuration.merchant.konbini_payments` (object, nullable)
        Settings specific to Konbini payments on the account.

        - `data.configuration.merchant.konbini_payments.support` (object, nullable)
          Support for Konbini payments.

          - `data.configuration.merchant.konbini_payments.support.email` (string, nullable)
            Support email address for Konbini payments.

          - `data.configuration.merchant.konbini_payments.support.hours` (object, nullable)
            Support hours for Konbini payments.

            - `data.configuration.merchant.konbini_payments.support.hours.end_time` (string, nullable)
              Support hours end time (JST time of day) for in `HH:MM` format.

            - `data.configuration.merchant.konbini_payments.support.hours.start_time` (string, nullable)
              Support hours start time (JST time of day) for in `HH:MM` format.

          - `data.configuration.merchant.konbini_payments.support.phone` (string, nullable)
            Support phone number for Konbini payments.

      - `data.configuration.merchant.mcc` (string, nullable)
        The Merchant Category Code (MCC) for the merchant. MCCs classify businesses based on the goods or services they provide.

      - `data.configuration.merchant.script_statement_descriptor` (object, nullable)
        Settings for the default text that appears on statements for language variations.

        - `data.configuration.merchant.script_statement_descriptor.kana` (object, nullable)
          The Kana variation of statement_descriptor used for charges in Japan. Japanese statement descriptors have [special requirements](https://docs.stripe.com/get-started/account/statement-descriptors.md#set-japanese-statement-descriptors).

          - `data.configuration.merchant.script_statement_descriptor.kana.descriptor` (string, nullable)
            The default text that appears on statements for non-card charges outside of Japan. For card charges, if you don’t set a statement_descriptor_prefix, this text is also used as the statement descriptor prefix. In that case, if concatenating the statement descriptor suffix causes the combined statement descriptor to exceed 22 characters, we truncate the statement_descriptor text to limit the full descriptor to 22 characters. For more information about statement descriptors and their requirements, see the Merchant Configuration settings documentation.

          - `data.configuration.merchant.script_statement_descriptor.kana.prefix` (string, nullable)
            Default text that appears on statements for card charges outside of Japan, prefixing any dynamic statement_descriptor_suffix specified on the charge. To maximize space for the dynamic part of the descriptor, keep this text short. If you don’t specify this value, statement_descriptor is used as the prefix. For more information about statement descriptors and their requirements, see the Merchant Configuration settings documentation.

        - `data.configuration.merchant.script_statement_descriptor.kanji` (object, nullable)
          The Kanji variation of statement_descriptor used for charges in Japan. Japanese statement descriptors have [special requirements](https://docs.stripe.com/get-started/account/statement-descriptors.md#set-japanese-statement-descriptors).

          - `data.configuration.merchant.script_statement_descriptor.kanji.descriptor` (string, nullable)
            The default text that appears on statements for non-card charges outside of Japan. For card charges, if you don’t set a statement_descriptor_prefix, this text is also used as the statement descriptor prefix. In that case, if concatenating the statement descriptor suffix causes the combined statement descriptor to exceed 22 characters, we truncate the statement_descriptor text to limit the full descriptor to 22 characters. For more information about statement descriptors and their requirements, see the Merchant Configuration settings documentation.

          - `data.configuration.merchant.script_statement_descriptor.kanji.prefix` (string, nullable)
            Default text that appears on statements for card charges outside of Japan, prefixing any dynamic statement_descriptor_suffix specified on the charge. To maximize space for the dynamic part of the descriptor, keep this text short. If you don’t specify this value, statement_descriptor is used as the prefix. For more information about statement descriptors and their requirements, see the Merchant Configuration settings documentation.

      - `data.configuration.merchant.sepa_debit_payments` (object, nullable)
        Settings for SEPA Direct Debit payments.

        - `data.configuration.merchant.sepa_debit_payments.creditor_id` (string, nullable)
          Creditor ID for SEPA Direct Debit payments.

      - `data.configuration.merchant.statement_descriptor` (object, nullable)
        Statement descriptor.

        - `data.configuration.merchant.statement_descriptor.descriptor` (string, nullable)
          The default text that appears on statements for non-card charges outside of Japan. For card charges, if you don’t set a statement_descriptor_prefix, this text is also used as the statement descriptor prefix. In that case, if concatenating the statement descriptor suffix causes the combined statement descriptor to exceed 22 characters, we truncate the statement_descriptor text to limit the full descriptor to 22 characters. For more information about statement descriptors and their requirements, see the Merchant Configuration settings documentation.

        - `data.configuration.merchant.statement_descriptor.prefix` (string, nullable)
          Default text that appears on statements for card charges outside of Japan, prefixing any dynamic statement_descriptor_suffix specified on the charge. To maximize space for the dynamic part of the descriptor, keep this text short. If you don’t specify this value, statement_descriptor is used as the prefix. For more information about statement descriptors and their requirements, see the Merchant Configuration settings documentation.

      - `data.configuration.merchant.support` (object, nullable)
        Publicly available contact information for sending support issues to.

        - `data.configuration.merchant.support.address` (object, nullable)
          A publicly available mailing address for sending support issues to.

          - `data.configuration.merchant.support.address.city` (string, nullable)
            City, district, suburb, town, or village.

          - `data.configuration.merchant.support.address.country` (enum, nullable)
            Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

          - `data.configuration.merchant.support.address.line1` (string, nullable)
            Address line 1 (e.g., street, PO Box, or company name).

          - `data.configuration.merchant.support.address.line2` (string, nullable)
            Address line 2 (e.g., apartment, suite, unit, or building).

          - `data.configuration.merchant.support.address.postal_code` (string, nullable)
            ZIP or postal code.

          - `data.configuration.merchant.support.address.state` (string, nullable)
            State, county, province, or region.

          - `data.configuration.merchant.support.address.town` (string, nullable)
            Town or district.

        - `data.configuration.merchant.support.email` (string, nullable)
          A publicly available email address for sending support issues to.

        - `data.configuration.merchant.support.phone` (string, nullable)
          A publicly available phone number to call with support issues.

        - `data.configuration.merchant.support.url` (string, nullable)
          A publicly available website for handling support issues.

    - `data.configuration.recipient` (object, nullable)
      The Recipient Configuration allows the Account to receive funds. Utilize this configuration if the Account will not be the Merchant of Record, like with Separate Charges & Transfers, or Destination Charges without on_behalf_of set.

      - `data.configuration.recipient.applied` (boolean)
        Indicates whether the recipient configuration is active. You can deactivate or reactivate the recipient configuration by updating this property. Deactivating the configuration by setting this value to false  unrequest all capabilities within the configuration. It will not delete any of the configuration’s other properties.

      - `data.configuration.recipient.capabilities` (object, nullable)
        Capabilities that have been requested on the Recipient Configuration.

        - `data.configuration.recipient.capabilities.stripe_balance` (object, nullable)
          Capabilities that enable the recipient to manage their Stripe Balance (/v1/balance).

          - `data.configuration.recipient.capabilities.stripe_balance.payouts` (object, nullable)
            Enables this Account to complete payouts from their Stripe Balance (/v1/balance).

            - `data.configuration.recipient.capabilities.stripe_balance.payouts.status` (enum)
              The status of the Capability.
Possible enum values:
              - `active`
                The Capability is active.

              - `pending`
                Stripe is carrying out an action prior to activating the Capability. No further action is required at this time.

              - `restricted`
                The Capability requires further action before it can be activated, check the `status_details` for information on why.

              - `unsupported`
                The Capability is unsupported. Check `status_details` for information on why.

            - `data.configuration.recipient.capabilities.stripe_balance.payouts.status_details` (array of objects)
              Additional details about the capability’s status. This value is empty when `status` is `active`.

              - `data.configuration.recipient.capabilities.stripe_balance.payouts.status_details.code` (enum)
                Machine-readable code explaining the reason for the Capability to be in its current status.
Possible enum values:
                - `determining_status`
                  Stripe is in the process of determining the capability’s status.

                - `requirements_past_due`
                  Some required information is past due.

                - `requirements_pending_verification`
                  Stripe is currently verifying information that was supplied about the Account.

                - `restricted_other`
                  Capability is restricted for unspecified reasons.

                - `unsupported_business`
                  Capability is not supported for the Account’s business as expressed by the MCC in the Merchant Configuration.

                - `unsupported_country`
                  Capability is not supported for the Account’s Legal Entity country.

                - `unsupported_entity_type`
                  Capability is not supported for the given Identity entity type (i.e. individual).

              - `data.configuration.recipient.capabilities.stripe_balance.payouts.status_details.resolution` (enum)
                Machine-readable code explaining how to make the Capability active.
Possible enum values:
                - `contact_stripe`
                  Contact Stripe support to find more information about why this Capability is restricted.

                - `no_resolution`
                  No action is required from the user.

                - `provide_info`
                  Provide outstanding information about the Account to enable this Capability. Check the Requirements resource for more details.

          - `data.configuration.recipient.capabilities.stripe_balance.stripe_transfers` (object, nullable)
            Enables this Account to receive /v1/transfers into their Stripe Balance (/v1/balance).

            - `data.configuration.recipient.capabilities.stripe_balance.stripe_transfers.status` (enum)
              The status of the Capability.
Possible enum values:
              - `active`
                The Capability is active.

              - `pending`
                Stripe is carrying out an action prior to activating the Capability. No further action is required at this time.

              - `restricted`
                The Capability requires further action before it can be activated, check the `status_details` for information on why.

              - `unsupported`
                The Capability is unsupported. Check `status_details` for information on why.

            - `data.configuration.recipient.capabilities.stripe_balance.stripe_transfers.status_details` (array of objects)
              Additional details about the capability’s status. This value is empty when `status` is `active`.

              - `data.configuration.recipient.capabilities.stripe_balance.stripe_transfers.status_details.code` (enum)
                Machine-readable code explaining the reason for the Capability to be in its current status.
Possible enum values:
                - `determining_status`
                  Stripe is in the process of determining the capability’s status.

                - `requirements_past_due`
                  Some required information is past due.

                - `requirements_pending_verification`
                  Stripe is currently verifying information that was supplied about the Account.

                - `restricted_other`
                  Capability is restricted for unspecified reasons.

                - `unsupported_business`
                  Capability is not supported for the Account’s business as expressed by the MCC in the Merchant Configuration.

                - `unsupported_country`
                  Capability is not supported for the Account’s Legal Entity country.

                - `unsupported_entity_type`
                  Capability is not supported for the given Identity entity type (i.e. individual).

              - `data.configuration.recipient.capabilities.stripe_balance.stripe_transfers.status_details.resolution` (enum)
                Machine-readable code explaining how to make the Capability active.
Possible enum values:
                - `contact_stripe`
                  Contact Stripe support to find more information about why this Capability is restricted.

                - `no_resolution`
                  No action is required from the user.

                - `provide_info`
                  Provide outstanding information about the Account to enable this Capability. Check the Requirements resource for more details.

  - `data.contact_email` (string, nullable)
    The default contact email address for the Account. Required when configuring the account as a merchant or recipient.

  - `data.created` (timestamp)
    Time at which the object was created. Represented as a RFC 3339 date & time UTC value in millisecond precision, for example: 2022-09-18T13:22:18.123Z.

  - `data.dashboard` (enum, nullable)
    A value indicating the Stripe dashboard this Account has access to. This will depend on which configurations are enabled for this account.
Possible enum values:
    - `express`
      The Account has access to the Express hosted dashboard.

    - `full`
      The Account has access to the full Stripe hosted dashboard.

    - `none`
      The Account does not have access to any Stripe hosted dashboard.

  - `data.defaults` (object, nullable)
    Default values for settings shared across Account configurations.

    - `data.defaults.currency` (enum, nullable)
      Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

    - `data.defaults.locales` (array of enums, nullable)
      The Account’s preferred locales (languages), ordered by preference.
Possible enum values:
      - `ar-SA`
        IETF Locale.

      - `bg`
        IETF Locale.

      - `bg-BG`
        IETF Locale.

      - `cs`
        IETF Locale.

      - `cs-CZ`
        IETF Locale.

      - `da`
        IETF Locale.

      - `da-DK`
        IETF Locale.

      - `de`
        IETF Locale.

      - `de-DE`
        IETF Locale.

      - `el`
        IETF Locale.

      - `el-GR`
        IETF Locale.

      - `en`
        IETF Locale.

      - `en-AU`
        IETF Locale.

      - `en-CA`
        IETF Locale.

      - `en-GB`
        IETF Locale.

      - `en-IE`
        IETF Locale.

      - `en-IN`
        IETF Locale.

      - `en-NZ`
        IETF Locale.

      - `en-SG`
        IETF Locale.

      - `en-US`
        IETF Locale.

      - `es`
        IETF Locale.

      - `es-419`
        IETF  Locale.

      - `es-ES`
        IETF Locale.

      - `et`
        IETF Locale.

      - `et-EE`
        IETF Locale.

      - `fi`
        IETF Locale.

      - `fi-FI`
        IETF Locale.

      - `fil`
        IETF Locale.

      - `fil-PH`
        IETF Locale.

      - `fr`
        IETF Locale.

      - `fr-CA`
        IETF Locale.

      - `fr-FR`
        IETF Locale.

      - `he-IL`
        IETF Locale.

      - `hr`
        IETF Locale.

      - `hr-HR`
        IETF Locale.

      - `hu`
        IETF Locale.

      - `hu-HU`
        IETF Locale.

      - `id`
        IETF Locale.

      - `id-ID`
        IETF Locale.

      - `it`
        IETF Locale.

      - `it-IT`
        IETF Locale.

      - `ja`
        IETF Locale.

      - `ja-JP`
        IETF Locale.

      - `ko`
        IETF Locale.

      - `ko-KR`
        IETF Locale.

      - `lt`
        IETF Locale.

      - `lt-LT`
        IETF Locale.

      - `lv`
        IETF Locale.

      - `lv-LV`
        IETF Locale.

      - `ms`
        IETF Locale.

      - `ms-MY`
        IETF Locale.

      - `mt`
        IETF Locale.

      - `mt-MT`
        IETF Locale.

      - `nb`
        IETF Locale.

      - `nb-NO`
        IETF Locale.

      - `nl`
        IETF Locale.

      - `nl-NL`
        IETF Locale.

      - `pl`
        IETF Locale.

      - `pl-PL`
        IETF Locale.

      - `pt`
        IETF Locale.

      - `pt-BR`
        IETF Locale.

      - `pt-PT`
        IETF Locale.

      - `ro`
        IETF Locale.

      - `ro-RO`
        IETF Locale.

      - `ru`
        IETF Locale.

      - `ru-RU`
        IETF Locale.

      - `sk`
        IETF Locale.

      - `sk-SK`
        IETF Locale.

      - `sl`
        IETF Locale.

      - `sl-SI`
        IETF Locale.

      - `sv`
        IETF Locale.

      - `sv-SE`
        IETF Locale.

      - `th`
        IETF Locale.

      - `th-TH`
        IETF Locale.

      - `tr`
        IETF Locale.

      - `tr-TR`
        IETF Locale.

      - `vi`
        IETF Locale.

      - `vi-VN`
        IETF Locale.

      - `zh`
        IETF Locale.

      - `zh-HK`
        IETF Locale.

      - `zh-Hans`
        IETF Locale.

      - `zh-Hant-HK`
        IETF Locale.

      - `zh-Hant-TW`
        IETF Locale.

      - `zh-TW`
        IETF Locale.

    - `data.defaults.profile` (object, nullable)
      Account profile information.

      - `data.defaults.profile.business_url` (string, nullable)
        The business’s publicly-available website.

      - `data.defaults.profile.doing_business_as` (string, nullable)
        The customer-facing business name.

      - `data.defaults.profile.product_description` (string, nullable)
        Internal-only description of the product sold or service provided by the business. It’s used by Stripe for risk and underwriting purposes.

    - `data.defaults.responsibilities` (object)
      Default responsibilities held by either Stripe or the platform.

      - `data.defaults.responsibilities.fees_collector` (enum, nullable)
        Indicates whether the platform or connected account is responsible for paying Stripe fees for pricing-control-eligible products.
Possible enum values:
        - `application`
          The platform is responsible for collecting fees from the Account.

        - `application_custom`
          Direct charge fee behavior is the same as for Custom accounts. See [documentation](https://docs.stripe.com/connect/direct-charges-fee-payer-behavior.md).

        - `application_express`
          Direct charge fee behavior is the same as for Express accounts. See [documentation](https://docs.stripe.com/connect/direct-charges-fee-payer-behavior.md).

        - `stripe`
          Stripe is responsible for collecting fees from the Account.

      - `data.defaults.responsibilities.losses_collector` (enum, nullable)
        A value indicating responsibility for collecting requirements on this account.
Possible enum values:
        - `application`
          The platform is responsible for negative balances on the Account.

        - `stripe`
          Stripe is responsible for negative balances on this Account.

      - `data.defaults.responsibilities.requirements_collector` (enum)
        A value indicating responsibility for collecting requirements on this account.
Possible enum values:
        - `application`
          The platform is responsible for collecting outstanding and updated requirements on the Account.

        - `stripe`
          Stripe is responsible for collecting outstanding and updated requirements on the Account.

  - `data.display_name` (string, nullable)
    A descriptive name for the Account. This name will be surfaced in the Stripe Dashboard and on any invoices sent to the Account.

  - `data.future_requirements` (object, nullable)
    Information about the future requirements for the Account that will eventually come into effect, including what information needs to be collected, and by when.

    - `data.future_requirements.entries` (array of objects, nullable)
      A list of requirements for the Account.

      - `data.future_requirements.entries.awaiting_action_from` (enum)
        Indicates whether the platform or Stripe is currently responsible for taking action on the requirement. Value can be `user` or `stripe`.
Possible enum values:
        - `stripe`
          Integrator should do nothing.

        - `user`
          Integrator should take action.

      - `data.future_requirements.entries.description` (string)
        Machine-readable string describing the requirement.

      - `data.future_requirements.entries.errors` (array of objects)
        Descriptions of why the requirement must be collected, or why the collected information isn’t satisfactory to Stripe.

        - `data.future_requirements.entries.errors.code` (enum)
          Machine-readable code describing the error.
Possible enum values:
          - `invalid_address_city_state_postal_code`
            The combination of the city, state, and postal code in the provided address could not be validated.

          - `invalid_address_highway_contract_box`
            Invalid address. Your business address must be a valid physical address from which you conduct business and cannot be a Highway Contract Box.

          - `invalid_address_private_mailbox`
            Invalid address. Your business address must be a valid physical address from which you conduct business and cannot be a private mailbox.

          - `invalid_business_profile_name`
            Business profile names must consist of recognizable words.

          - `invalid_business_profile_name_denylisted`
            Generic or well-known business names aren’t supported.

          - `invalid_company_name_denylisted`
            Generic or well-known business names aren’t supported.

          - `invalid_dob_age_over_maximum`
            Date of birth must be within the past 120 years.

          - `invalid_dob_age_under_18`
            Underage. Age must be at least 18.

          - `invalid_dob_age_under_minimum`
            Person must be at least 13 years old.

          - `invalid_product_description_length`
            Your product description must be at least 10 characters.

          - `invalid_product_description_url_match`
            Your product description must be different from your URL.

          - `invalid_representative_country`
            The representative must have an address in the same country as the company.

          - `invalid_statement_descriptor_business_mismatch`
            The statement descriptor must be similar to your business name, legal entity name, or URL.

          - `invalid_statement_descriptor_denylisted`
            Generic or well-known statement descriptors aren’t supported.

          - `invalid_statement_descriptor_length`
            The statement descriptor must be at least 5 characters.

          - `invalid_statement_descriptor_prefix_denylisted`
            Generic or well-known statement descriptor prefixes aren’t supported.

          - `invalid_statement_descriptor_prefix_mismatch`
            The statement descriptor prefix must be similar to your statement descriptor, business name, legal entity name, or URL.

          - `invalid_street_address`
            The street name and/or number for the provided address could not be validated.

          - `invalid_tax_id`
            The provided tax ID must have 9 digits.

          - `invalid_tax_id_format`
            Tax IDs must be a unique set of 9 numbers without dashes or other special characters.

          - `invalid_tos_acceptance`
            The existing terms of service signature has been invalidated because the account’s tax ID has changed. The account needs to accept the terms of service again. For more information, see [this documentation](https://docs.stripe.com/connect/update-verified-information.md).

          - `invalid_url_denylisted`
            Generic business URLs aren’t supported.

          - `invalid_url_format`
            URL must be formatted as https://example.com.

          - `invalid_url_web_presence_detected`
            Because you use a website, app, social media page, or online profile to sell products or services, you must provide a URL for your business.

          - `invalid_url_website_business_information_mismatch`
            The business information on your website must match the details you provided to Stripe.

          - `invalid_url_website_empty`
            Your provided website appears to be empty.

          - `invalid_url_website_inaccessible`
            This URL couldn’t be reached. Make sure it’s available and entered correctly or provide another.

          - `invalid_url_website_inaccessible_geoblocked`
            Your provided website appears to be geographically blocked.

          - `invalid_url_website_inaccessible_password_protected`
            Your provided website appears to be password protected.

          - `invalid_url_website_incomplete`
            Your website seems to be missing some required information. [Learn about the requirements](https://support.stripe.com/questions/information-required-on-your-business-website-to-use-stripe).

          - `invalid_url_website_incomplete_cancellation_policy`
            Your provided website appears to have an incomplete cancellation policy.

          - `invalid_url_website_incomplete_customer_service_details`
            Your provided website appears to have incomplete customer service details.

          - `invalid_url_website_incomplete_legal_restrictions`
            Your provided website appears to have incomplete legal restrictions.

          - `invalid_url_website_incomplete_refund_policy`
            Your provided website appears to have an incomplete refund policy.

          - `invalid_url_website_incomplete_return_policy`
            Your provided website appears to have an incomplete refund policy.

          - `invalid_url_website_incomplete_terms_and_conditions`
            Your provided website appears to have incomplete terms and conditions.

          - `invalid_url_website_incomplete_under_construction`
            Your provided website appears to be incomplete or under construction.

          - `invalid_url_website_other`
            We weren’t able to verify your business using the URL you provided. Make sure it’s entered correctly or provide another URL.

          - `invalid_value_other`
            An invalid value was provided for the related field. This is a general error code.

          - `unresolvable_ip_address`
            IP address did not resolve to a valid tax location.

          - `unresolvable_postal_code`
            Postal code did not resolve to a valid tax location.

          - `verification_directors_mismatch`
            Directors on the account don’t match government records. Update the account and upload a directorship document with current directors.

          - `verification_document_address_mismatch`
            Address on the account doesn’t match the verification document. Update the account and upload the document again.

          - `verification_document_address_missing`
            The company address was missing on the document. Upload a document that includes the address.

          - `verification_document_corrupt`
            File seems to be corrupted or damaged. Provide a different file.

          - `verification_document_country_not_supported`
            Document isn’t supported in this person’s country or region. Provide a supported verification document.

          - `verification_document_directors_mismatch`
            Directors on the account don’t match the document provided. Update the account to match the registration document and upload it again.

          - `verification_document_dob_mismatch`
            The date of birth (DOB) on the document did not match the DOB on the account. Upload a document with a matching DOB or update the DOB on the account.

          - `verification_document_duplicate_type`
            The same type of document was used twice. Two unique types of documents are required for verification.

          - `verification_document_expired`
            The document could not be used for verification because it has expired. If it’s an identity document, its expiration date must be after the date the document was submitted. If it’s an address document, the issue date must be within the last six months.

          - `verification_document_failed_copy`
            Document is a photo or screenshot. Upload the original document.

          - `verification_document_failed_greyscale`
            Document seems to be in grayscale or black and white. Provide a full color photo of the document for verification.

          - `verification_document_failed_other`
            The document could not be verified for an unknown reason. Ensure that the document follows the [guidelines for document uploads](https://docs.stripe.com/acceptable-verification-documents.md).

          - `verification_document_failed_test_mode`
            A test data helper was supplied to simulate verification failure. Refer to the documentation for [test file tokens](https://docs.stripe.com/connect/testing.md#test-file-tokens).

          - `verification_document_fraudulent`
            Document seems to be altered. This could be because it’s fraudulent.

          - `verification_document_id_number_mismatch`
            Tax ID number on the account doesn’t match the verification document. Update the account to match the verification document and upload it again.

          - `verification_document_id_number_missing`
            The company ID number was missing on the document. Upload a document that includes the ID number.

          - `verification_document_incomplete`
            Document doesn’t include required information. Make sure all pages and sections are complete.

          - `verification_document_invalid`
            Document isn’t an acceptable form of identification in this account’s country or region. Ensure that the document follows the [guidelines for document uploads](https://docs.stripe.com/acceptable-verification-documents.md).

          - `verification_document_issue_or_expiry_date_missing`
            Document is missing an expiration date. Provide a document with an expiration date.

          - `verification_document_manipulated`
            Document seems to be altered. This could be because it’s fraudulent.

          - `verification_document_missing_back`
            The back of the document is missing. Provide both sides of the document for verification.

          - `verification_document_missing_front`
            The front of the document is missing. Provide both sides of the document for verification.

          - `verification_document_name_mismatch`
            The name on the account does not match the name on the document. Update the account to match the document and upload it again.

          - `verification_document_name_missing`
            The company name was missing on the document. Upload a document that includes the company name.

          - `verification_document_nationality_mismatch`
            The nationality on the document did not match the person’s stated nationality. Update the person’s stated nationality, or upload a document that matches it.

          - `verification_document_not_readable`
            Document isn’t readable. This could be because it’s blurry or dark, or because the document was obstructed.

          - `verification_document_not_signed`
            Document doesn’t seem to be signed. Provide a signed document.

          - `verification_document_not_uploaded`
            Document didn’t upload because of a problem with the file.

          - `verification_document_photo_mismatch`
            ID photo on the document doesn’t match the selfie provided by this account.

          - `verification_document_too_large`
            Document file is too large. Upload one that’s 10MB or less.

          - `verification_document_type_not_supported`
            The provided document type is not accepted. Ensure that the document follows the [guidelines for document uploads](https://docs.stripe.com/acceptable-verification-documents.md).

          - `verification_extraneous_directors`
            Extraneous directors have been added to the account. Update the account and upload a registration document with current directors.

          - `verification_failed_address_match`
            The address on the account could not be verified. Correct any errors in the address field or upload a document that includes the address.

          - `verification_failed_business_iec_number`
            The Importer Exporter Code (IEC) number on your account could not be verified. Either correct any possible errors in the company name or IEC number. Refer to the support article for [accepting international payments in India](https://support.stripe.com/questions/accepting-international-payments-from-stripe-accounts-in-india).

          - `verification_failed_document_match`
            The document could not be verified. Upload a document that includes the company name, ID number, and address fields.

          - `verification_failed_id_number_match`
            ID number on the document doesn’t match the ID number provided by this account.

          - `verification_failed_keyed_identity`
            The person’s keyed-in identity information could not be verified. Correct any errors or upload a document that matches the identity fields (e.g., name and date of birth) entered.

          - `verification_failed_keyed_match`
            The keyed-in information on the account could not be verified. Correct any errors in the company name, ID number, or address fields. You can also upload a document that includes those fields.

          - `verification_failed_name_match`
            The company name on the account could not be verified. Correct any errors in the company name field or upload a document that includes the company name.

          - `verification_failed_other`
            Verification failed for an unknown reason. Correct any errors and resubmit the required fields.

          - `verification_failed_representative_authority`
            The authority of the account representative could not be verified. Please change the account representative to a person who is registered as an authorized representative. Please refer to [this support article](https://support.stripe.com/questions/representative-authority-verification).

          - `verification_failed_residential_address`
            We could not verify that the person resides at the provided address. The address must be a valid physical address where the individual resides and cannot be a P.O. Box.

          - `verification_failed_tax_id_match`
            The tax ID on the account cannot be verified by the IRS. Either correct any possible errors in the company name or tax ID, or upload a document that contains those fields.

          - `verification_failed_tax_id_not_issued`
            The tax ID on the account was not recognized by the IRS. Refer to the support article for [newly-issued tax ID numbers](https://support.stripe.com/questions/newly-issued-us-tax-id-number-tin-not-verifying).

          - `verification_missing_directors`
            Directors are missing from the account. Update the account and upload a registration document with current directors.

          - `verification_missing_executives`
            We have identified executives that haven’t been added on the account. Add any missing executives to the account.

          - `verification_missing_owners`
            We have identified owners that haven’t been added on the account. Add any missing owners to the account.

          - `verification_requires_additional_memorandum_of_associations`
            We have identified holding companies with significant percentage ownership. Upload a Memorandum of Association for each of the holding companies.

          - `verification_requires_additional_proof_of_registration`
            The uploaded document contains holding companies with significant percentage ownership. Upload a proof of registration for each of the holding companies.

          - `verification_selfie_document_missing_photo`
            Photo is missing from the document. Provide a document with a photo.

          - `verification_selfie_face_mismatch`
            Selfie doesn’t match the photo on the document. Provide a clear, well-lit, and unobstructed selfie.

          - `verification_selfie_manipulated`
            Selfie seems to be altered. This could be because it’s fraudulent.

          - `verification_selfie_unverified_other`
            Selfie couldn’t be verified. Provide a clear, well-lit, and unobstructed selfie that matches the photo on the identity document.

          - `verification_supportability`
            We can’t accept payments for this business under the Stripe Services Agreement without additional verification, as mentioned in the [prohibited and restricted businesses list](https://stripe.com/legal/restricted-businesses).

          - `verification_token_stale`
            The eID token submitted for liveness verification must be submitted within 5 minutes of obtaining it from the partner.

        - `data.future_requirements.entries.errors.description` (string)
          Human-readable description of the error.

      - `data.future_requirements.entries.impact` (object)
        A hash describing the impact of not collecting the requirement, or Stripe not being able to verify the collected information.

        - `data.future_requirements.entries.impact.restricts_capabilities` (array of objects, nullable)
          The Capabilities that will be restricted if the requirement is not collected and satisfactory to Stripe.

          - `data.future_requirements.entries.impact.restricts_capabilities.capability` (enum)
            The name of the Capability which will be restricted.
Possible enum values:
            - `ach_debit_payments`
              Capability to use ACH Debit payments.

            - `acss_debit_payments`
              Capability to use ACSS Debit payments.

            - `affirm_payments`
              Capability to use Affirm payments.

            - `afterpay_clearpay_payments`
              Capability to use Afterpay Clearpay payments.

            - `alma_payments`
              Capability to use Alma payments.

            - `amazon_pay_payments`
              Capability to use Amazon Pay payments.

            - `au_becs_debit_payments`
              Capability to use AU BECS Debit payments.

            - `automatic_indirect_tax`
              Capability to have taxes automatically corrected.

            - `bacs_debit_payments`
              Capability to use BACS Direct Debit payments.

            - `bancontact_payments`
              Capability to use Bancontact payments.

            - `bank_accounts.local`
              Capability to use Bank Accounts Local payouts.

            - `bank_accounts.wire`
              Capability to use Bank Accounts Wire payouts.

            - `blik_payments`
              Capability to use BLIK payments.

            - `boleto_payments`
              Capability to use Boleto payments.

            - `card_payments`
              Capability to collect card payments.

            - `cards`
              Capability to use Card payouts.

            - `cartes_bancaires_payments`
              Capability to use Cartes Bancaires payments.

            - `cashapp_payments`
              Capability to use CashApp payments.

            - `eps_payments`
              Capability to use EPS payments.

            - `fpx_payments`
              Capability to use FPX payments.

            - `gb_bank_transfer_payments`
              Capability to use GB bank transfer payments.

            - `grabpay_payments`
              Capability to use GrabPay payments.

            - `ideal_payments`
              Capability to use IDEAL payments.

            - `jcb_payments`
              Capability to use JCB payments.

            - `jp_bank_transfer_payments`
              Capability to use JP bank transfer payments.

            - `kakao_pay_payments`
              Capability to use Kakao Pay payments.

            - `klarna_payments`
              Capability to use Klarna payments.

            - `konbini_payments`
              Capability to use Konbini payments.

            - `kr_card_payments`
              Capability to use KR card payments.

            - `link_payments`
              Capability to use Link payments.

            - `mobilepay_payments`
              Capability to use MobilePay payments.

            - `multibanco_payments`
              Capability to use Multibanco payments.

            - `mx_bank_transfer_payments`
              Capability to use MX bank transfer payments.

            - `naver_pay_payments`
              Capability to use Naver Pay payments.

            - `oxxo_payments`
              Capability to use OXXO payments.

            - `p24_payments`
              Capability to use P24 payments.

            - `pay_by_bank_payments`
              Capability to use Pay by Bank payments.

            - `payco_payments`
              Capability to use Payco payments.

            - `paynow_payments`
              Capability to use PayNow payments.

            - `promptpay_payments`
              Capability to use PromptPay payments.

            - `revolut_pay_payments`
              Capability to use Revolut Pay payments.

            - `samsung_pay_payments`
              Capability to use Samsung Pay payments.

            - `sepa_bank_transfer_payments`
              Capability to use SEPA bank transfer payments.

            - `sepa_debit_payments`
              Capability to use SEPA Debit payments.

            - `stripe_balance.payouts`
              Capability to do payouts from the user’s Stripe balance.

            - `stripe_balance.stripe_transfers`
              Capability to receive transfers to the user’s Stripe balance.

            - `swish_payments`
              Capability to use Swish payments.

            - `twint_payments`
              Capability to use Twint payments.

            - `us_bank_transfer_payments`
              Capability to use US bank transfer payments.

            - `zip_payments`
              Capability to use Zip payments.

          - `data.future_requirements.entries.impact.restricts_capabilities.configuration` (enum)
            The configuration which specifies the Capability which will be restricted.
Possible enum values:
            - `customer`
              Customer configuration.

            - `merchant`
              Merchant configuration.

            - `recipient`
              Recipient configuration.

          - `data.future_requirements.entries.impact.restricts_capabilities.deadline` (object)
            Details about when in the account lifecycle the requirement must be collected by the avoid the Capability restriction.

            - `data.future_requirements.entries.impact.restricts_capabilities.deadline.status` (enum)
              The current status of the requirement’s impact.
Possible enum values:
              - `currently_due`
                The requirement needs to be collected to keep the account enabled.

              - `eventually_due`
                The requirement needs to be collected assuming all volume thresholds are met.

              - `past_due`
                The requirement needs to be collected to enable the account.

      - `data.future_requirements.entries.minimum_deadline` (object)
        The soonest point when the account will be impacted by not providing the requirement.

        - `data.future_requirements.entries.minimum_deadline.status` (enum)
          The current status of the requirement’s impact.
Possible enum values:
          - `currently_due`
            The requirement needs to be collected to keep the account enabled.

          - `eventually_due`
            The requirement needs to be collected assuming all volume thresholds are met.

          - `past_due`
            The requirement needs to be collected to enable the account.

      - `data.future_requirements.entries.reference` (object, nullable)
        A reference to the location of the requirement.

        - `data.future_requirements.entries.reference.inquiry` (string, nullable)
          If `inquiry` is the type, the inquiry token.

        - `data.future_requirements.entries.reference.resource` (string, nullable)
          If `resource` is the type, the resource token.

        - `data.future_requirements.entries.reference.type` (enum)
          The type of the reference. If the type is “inquiry”, the inquiry token can be found in the “inquiry” field. Otherwise the type is an API resource, the token for which can be found in the “resource” field.
Possible enum values:
          - `inquiry`
            An inquiry from Stripe.

          - `payment_method`
            A payment method.

          - `person`
            A person resource.

      - `data.future_requirements.entries.requested_reasons` (array of objects)
        A list of reasons why Stripe is collecting the requirement.

        - `data.future_requirements.entries.requested_reasons.code` (enum)
          Machine-readable description of Stripe’s reason for collecting the requirement.
Possible enum values:
          - `routine_onboarding`
            Stripe needs a basic set of information.

          - `routine_verification`
            Stripe needs to review provided information.

    - `data.future_requirements.minimum_transition_date` (timestamp, nullable)
      The time at which the future requirements become effective.

    - `data.future_requirements.summary` (object, nullable)
      An object containing an overview of requirements for the Account.

      - `data.future_requirements.summary.minimum_deadline` (object, nullable)
        The soonest date and time a requirement on the Account will become `past due`. Represented as a RFC 3339 date & time UTC value in millisecond precision, for example: `2022-09-18T13:22:18.123Z`.

        - `data.future_requirements.summary.minimum_deadline.status` (enum)
          The current strictest status of all requirements on the Account.
Possible enum values:
          - `currently_due`
            The requirement needs to be collected to keep the account enabled.

          - `eventually_due`
            The requirement needs to be collected assuming all volume thresholds are met.

          - `past_due`
            The requirement needs to be collected to enable the account.

        - `data.future_requirements.summary.minimum_deadline.time` (timestamp, nullable)
          The soonest RFC3339 date & time UTC value a requirement can impact the Account.

  - `data.identity` (object, nullable)
    Information about the company, individual, and business represented by the Account.

    - `data.identity.attestations` (object, nullable)
      Attestations from the identity’s key people, e.g. owners, executives, directors, representatives.

      - `data.identity.attestations.directorship_declaration` (object, nullable)
        This hash is used to attest that the directors information provided to Stripe is both current and correct.

        - `data.identity.attestations.directorship_declaration.date` (timestamp, nullable)
          The time marking when the director attestation was made. Represented as a RFC 3339 date & time UTC value in millisecond precision, for example: 2022-09-18T13:22:18.123Z.

        - `data.identity.attestations.directorship_declaration.ip` (string, nullable)
          The IP address from which the director attestation was made.

        - `data.identity.attestations.directorship_declaration.user_agent` (string, nullable)
          The user agent of the browser from which the director attestation was made.

      - `data.identity.attestations.ownership_declaration` (object, nullable)
        This hash is used to attest that the beneficial owner information provided to Stripe is both current and correct.

        - `data.identity.attestations.ownership_declaration.date` (timestamp, nullable)
          The time marking when the beneficial owner attestation was made. Represented as a RFC 3339 date & time UTC value in millisecond precision, for example: 2022-09-18T13:22:18.123Z.

        - `data.identity.attestations.ownership_declaration.ip` (string, nullable)
          The IP address from which the beneficial owner attestation was made.

        - `data.identity.attestations.ownership_declaration.user_agent` (string, nullable)
          The user agent of the browser from which the beneficial owner attestation was made.

      - `data.identity.attestations.persons_provided` (object, nullable)
        Attestation that all Persons with a specific Relationship value have been provided.

        - `data.identity.attestations.persons_provided.directors` (boolean, nullable)
          Whether the company’s directors have been provided. Set this Boolean to true after creating all the company’s directors with the [Persons API](https://docs.stripe.com/api/v2/core/accounts/createperson.md).

        - `data.identity.attestations.persons_provided.executives` (boolean, nullable)
          Whether the company’s executives have been provided. Set this Boolean to true after creating all the company’s executives with the [Persons API](https://docs.stripe.com/api/v2/core/accounts/createperson.md).

        - `data.identity.attestations.persons_provided.owners` (boolean, nullable)
          Whether the company’s owners have been provided. Set this Boolean to true after creating all the company’s owners with the [Persons API](https://docs.stripe.com/api/v2/core/accounts/createperson.md).

        - `data.identity.attestations.persons_provided.ownership_exemption_reason` (enum, nullable)
          Reason for why the company is exempt from providing ownership information.
Possible enum values:
          - `qualified_entity_exceeds_ownership_threshold`
            A qualifying entity or group of qualifying entities own a significant enough share of the merchant’s business that they are exempt from providing ownership information based on regulatory guidelines in the merchant’s country.

          - `qualifies_as_financial_institution`
            A merchant is a financial institution.

      - `data.identity.attestations.representative_declaration` (object, nullable)
        This hash is used to attest that the representative is authorized to act as the representative of their legal entity.

        - `data.identity.attestations.representative_declaration.date` (timestamp, nullable)
          The time marking when the representative attestation was made. Represented as a RFC 3339 date & time UTC value in millisecond precision, for example: 2022-09-18T13:22:18.123Z.

        - `data.identity.attestations.representative_declaration.ip` (string, nullable)
          The IP address from which the representative attestation was made.

        - `data.identity.attestations.representative_declaration.user_agent` (string, nullable)
          The user agent of the browser from which the representative attestation was made.

      - `data.identity.attestations.terms_of_service` (object, nullable)
        Attestations of accepted terms of service agreements.

        - `data.identity.attestations.terms_of_service.account` (object, nullable)
          Details on the Account’s acceptance of the [Stripe Services Agreement](https://docs.stripe.com/connect/updating-accounts.md#tos-acceptance).

          - `data.identity.attestations.terms_of_service.account.date` (timestamp, nullable)
            The time when the Account’s representative accepted the terms of service. Represented as a RFC 3339 date & time UTC value in millisecond precision, for example: 2022-09-18T13:22:18.123Z.

          - `data.identity.attestations.terms_of_service.account.ip` (string, nullable)
            The IP address from which the Account’s representative accepted the terms of service.

          - `data.identity.attestations.terms_of_service.account.user_agent` (string, nullable)
            The user agent of the browser from which the Account’s representative accepted the terms of service.

    - `data.identity.business_details` (object, nullable)
      Information about the company or business.

      - `data.identity.business_details.address` (object, nullable)
        The company’s primary address.

        - `data.identity.business_details.address.city` (string, nullable)
          City, district, suburb, town, or village.

        - `data.identity.business_details.address.country` (enum, nullable)
          Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

        - `data.identity.business_details.address.line1` (string, nullable)
          Address line 1 (e.g., street, PO Box, or company name).

        - `data.identity.business_details.address.line2` (string, nullable)
          Address line 2 (e.g., apartment, suite, unit, or building).

        - `data.identity.business_details.address.postal_code` (string, nullable)
          ZIP or postal code.

        - `data.identity.business_details.address.state` (string, nullable)
          State, county, province, or region.

        - `data.identity.business_details.address.town` (string, nullable)
          Town or district.

      - `data.identity.business_details.annual_revenue` (object, nullable)
        The business gross annual revenue for its preceding fiscal year.

        - `data.identity.business_details.annual_revenue.amount` (object, nullable)
          Annual revenue amount in minor currency units (for example, ‘123’ for 1.23 USD).

          - `data.identity.business_details.annual_revenue.amount.currency` (string)
            A lowercase alpha3 currency code like “usd”.

          - `data.identity.business_details.annual_revenue.amount.value` (integer)
            In minor units like 123 for 1.23 USD.

        - `data.identity.business_details.annual_revenue.fiscal_year_end` (string, nullable)
          The close-out date of the preceding fiscal year in ISO 8601 format. E.g. 2023-12-31 for the 31st of December, 2023.

      - `data.identity.business_details.documents` (object, nullable)
        Documents that may be submitted to satisfy various informational requests.

        - `data.identity.business_details.documents.bank_account_ownership_verification` (object, nullable)
          One or more documents that support the Bank account ownership verification requirement. Must be a document associated with the account’s primary active bank account that displays the last 4 digits of the account number, either a statement or a check.

          - `data.identity.business_details.documents.bank_account_ownership_verification.files` (array of strings)
            One or more document IDs returned by a [file upload](https://docs.stripe.com/api/persons/update.md#create_file) with a purpose value of `account_requirement`.

          - `data.identity.business_details.documents.bank_account_ownership_verification.type` (enum)
            The format of the document. Currently supports `files` only.
Possible enum values:
            - `files`
              Document type with multiple files.

        - `data.identity.business_details.documents.company_license` (object, nullable)
          One or more documents that demonstrate proof of a company’s license to operate.

          - `data.identity.business_details.documents.company_license.files` (array of strings)
            One or more document IDs returned by a [file upload](https://docs.stripe.com/api/persons/update.md#create_file) with a purpose value of `account_requirement`.

          - `data.identity.business_details.documents.company_license.type` (enum)
            The format of the document. Currently supports `files` only.
Possible enum values:
            - `files`
              Document type with multiple files.

        - `data.identity.business_details.documents.company_memorandum_of_association` (object, nullable)
          One or more documents showing the company’s Memorandum of Association.

          - `data.identity.business_details.documents.company_memorandum_of_association.files` (array of strings)
            One or more document IDs returned by a [file upload](https://docs.stripe.com/api/persons/update.md#create_file) with a purpose value of `account_requirement`.

          - `data.identity.business_details.documents.company_memorandum_of_association.type` (enum)
            The format of the document. Currently supports `files` only.
Possible enum values:
            - `files`
              Document type with multiple files.

        - `data.identity.business_details.documents.company_ministerial_decree` (object, nullable)
          Certain countries only: One or more documents showing the ministerial decree legalizing the company’s establishment.

          - `data.identity.business_details.documents.company_ministerial_decree.files` (array of strings)
            One or more document IDs returned by a [file upload](https://docs.stripe.com/api/persons/update.md#create_file) with a purpose value of `account_requirement`.

          - `data.identity.business_details.documents.company_ministerial_decree.type` (enum)
            The format of the document. Currently supports `files` only.
Possible enum values:
            - `files`
              Document type with multiple files.

        - `data.identity.business_details.documents.company_registration_verification` (object, nullable)
          One or more documents that demonstrate proof of a company’s registration with the appropriate local authorities.

          - `data.identity.business_details.documents.company_registration_verification.files` (array of strings)
            One or more document IDs returned by a [file upload](https://docs.stripe.com/api/persons/update.md#create_file) with a purpose value of `account_requirement`.

          - `data.identity.business_details.documents.company_registration_verification.type` (enum)
            The format of the document. Currently supports `files` only.
Possible enum values:
            - `files`
              Document type with multiple files.

        - `data.identity.business_details.documents.company_tax_id_verification` (object, nullable)
          One or more documents that demonstrate proof of a company’s tax ID.

          - `data.identity.business_details.documents.company_tax_id_verification.files` (array of strings)
            One or more document IDs returned by a [file upload](https://docs.stripe.com/api/persons/update.md#create_file) with a purpose value of `account_requirement`.

          - `data.identity.business_details.documents.company_tax_id_verification.type` (enum)
            The format of the document. Currently supports `files` only.
Possible enum values:
            - `files`
              Document type with multiple files.

        - `data.identity.business_details.documents.primary_verification` (object, nullable)
          A document verifying the business.

          - `data.identity.business_details.documents.primary_verification.front_back` (object)
            The [file upload](https://docs.stripe.com/api/persons/update.md#create_file) tokens for the front and back of the verification document.

            - `data.identity.business_details.documents.primary_verification.front_back.back` (string, nullable)
              A [file upload](https://docs.stripe.com/api/persons/update.md#create_file) token representing the back of the verification document. The purpose of the uploaded file should be ‘identity_document’. The uploaded file needs to be a color image (smaller than 8,000px by 8,000px), in JPG, PNG, or PDF format, and less than 10 MB in size.

            - `data.identity.business_details.documents.primary_verification.front_back.front` (string)
              A [file upload](https://docs.stripe.com/api/persons/update.md#create_file) token representing the front of the verification document. The purpose of the uploaded file should be ‘identity_document’. The uploaded file needs to be a color image (smaller than 8,000px by 8,000px), in JPG, PNG, or PDF format, and less than 10 MB in size.

          - `data.identity.business_details.documents.primary_verification.type` (enum)
            The format of the verification document. Currently supports `front_back` only.
Possible enum values:
            - `front_back`
              Document type with both front and back sides.

        - `data.identity.business_details.documents.proof_of_address` (object, nullable)
          One or more documents that demonstrate proof of address.

          - `data.identity.business_details.documents.proof_of_address.files` (array of strings)
            One or more document IDs returned by a [file upload](https://docs.stripe.com/api/persons/update.md#create_file) with a purpose value of `account_requirement`.

          - `data.identity.business_details.documents.proof_of_address.type` (enum)
            The format of the document. Currently supports `files` only.
Possible enum values:
            - `files`
              Document type with multiple files.

        - `data.identity.business_details.documents.proof_of_registration` (object, nullable)
          One or more documents showing the company’s proof of registration with the national business registry.

          - `data.identity.business_details.documents.proof_of_registration.files` (array of strings)
            One or more document IDs returned by a [file upload](https://docs.stripe.com/api/persons/update.md#create_file) with a purpose value of `account_requirement`.

          - `data.identity.business_details.documents.proof_of_registration.type` (enum)
            The format of the document. Currently supports `files` only.
Possible enum values:
            - `files`
              Document type with multiple files.

        - `data.identity.business_details.documents.proof_of_ultimate_beneficial_ownership` (object, nullable)
          One or more documents that demonstrate proof of ultimate beneficial ownership.

          - `data.identity.business_details.documents.proof_of_ultimate_beneficial_ownership.files` (array of strings)
            One or more document IDs returned by a [file upload](https://docs.stripe.com/api/persons/update.md#create_file) with a purpose value of `account_requirement`.

          - `data.identity.business_details.documents.proof_of_ultimate_beneficial_ownership.type` (enum)
            The format of the document. Currently supports `files` only.
Possible enum values:
            - `files`
              Document type with multiple files.

      - `data.identity.business_details.estimated_worker_count` (integer, nullable)
        Estimated maximum number of workers currently engaged by the business (including employees, contractors, and vendors).

      - `data.identity.business_details.id_numbers` (array of objects, nullable)
        The provided ID numbers of a business entity.

        - `data.identity.business_details.id_numbers.registrar` (string, nullable)
          The registrar of the ID number (Only valid for DE ID number types).

        - `data.identity.business_details.id_numbers.type` (enum)
          The ID number type of a business entity.
Possible enum values:
          - `ae_crn`
            Company registration number - United Arab Emirates.

          - `ae_vat`
            Business VAT ID - United Arab Emirates.

          - `ao_nif`
            Número de Identificação Fiscal (NIF) - Angola.

          - `ar_cuit`
            Clave Única de Identificación Tributaria - Argentina.

          - `at_fn`
            Firmenbuchnummer - Austria.

          - `at_stn`
            Steuernummer (StNr.) - Austria.

          - `at_vat`
            VAT Number (UID) - Austria.

          - `au_abn`
            Australian Business Number - Australia.

          - `au_acn`
            Australian Company Number - Australia.

          - `au_in`
            Incorporation Number - Australia.

          - `az_tin`
            Tax Identification Number - Azerbaijan.

          - `bd_etin`
            Electronic Tax Identification Number (ETIN) - Bangladesh.

          - `be_cbe`
            Enterprise number - Belgium.

          - `be_vat`
            VAT Number (n° TVA/BTW-nr) - Belgium.

          - `bg_uic`
            Unique Identification Code - Bulgaria.

          - `bg_vat`
            VAT Number (ДДС номер) - Bulgaria.

          - `br_cnpj`
            Cadastro Nacional da Pessoa Jurídica - Brazil.

          - `ca_cn`
            Corporation Number - Canada.

          - `ca_crarr`
            CRA registered charity program account number - Canada.

          - `ca_gst_hst`
            GST/HST Number - Canada.

          - `ca_neq`
            Québec Enterprise Number - Canada.

          - `ca_rid`
            Registry ID - Canada.

          - `ch_chid`
            Handelsregisternummer - Switzerland.

          - `ch_uid`
            Business Identification Number (UID) - Switzerland.

          - `cr_cpj`
            Cédula de Persona Jurídica (CPJ) - Costa Rica.

          - `cr_nite`
            Número de Indetificación Tributario Especial (NITE) - Costa Rica.

          - `cy_he`
            Αριθμός Εγγραφής Εταιρείας - Cyprus.

          - `cy_tic`
            Tax Identification Code - Cyprus.

          - `cy_vat`
            VAT Number (ΦΠΑ) - Cyprus.

          - `cz_ico`
            Identifikační číslo osoby - Czech Republic.

          - `cz_vat`
            VAT Number (DIČ) - Czech Republic.

          - `de_hrn`
            Handelsregisternummer - Germany.

          - `de_stn`
            Steuernummer (StNr.) - Germany.

          - `de_vat`
            VAT Number (USt-IdNr.) - Germany.

          - `dk_cvr`
            Centrale Virksomhedsregister - Denmark.

          - `dk_vat`
            VAT Number (CVR) - Denmark.

          - `do_rcn`
            Registro Nacional del Contribuyente (RNC) - Dominican Republic.

          - `ee_rk`
            Registrikood - Estonia.

          - `ee_vat`
            VAT Number (KMKR) - Estonia.

          - `es_cif`
            Número de Identificación Fiscal - Spain.

          - `es_vat`
            VAT Number (NIF-IVA) - Spain.

          - `fi_vat`
            VAT Number (ALV nro Momsnummer) - Finland.

          - `fi_yt`
            Y-tunnus - Finland.

          - `fr_rna`
            Numéro RNA - France.

          - `fr_siren`
            SIREN - France.

          - `fr_vat`
            VAT Number (n° TVA) - France.

          - `gb_crn`
            Companies House Registration Number - United Kingdom.

          - `gi_crn`
            Company Registration Number (CRN) - Gibraltar.

          - `gr_afm`
            Αριθμός Φορολογικού Μητρώου (ΑΦΜ) - Greece.

          - `gr_gemi`
            General Commercial Register (G.E.M.I.) - Greece.

          - `gr_vat`
            VAT Number (ΦΠΑ) - Greece.

          - `gt_nit`
            Número de Identificación Tributaria (NIT) - Guatemala.

          - `hk_br`
            Business Registration Number - Hong Kong.

          - `hk_cr`
            Company Registration Number - Hong Kong.

          - `hr_mbs`
            MBS (matični broj poslovnog subjekta) - Croatia.

          - `hr_oib`
            Osobni identifikacijski broj (OIB) - Croatia.

          - `hr_vat`
            VAT ID (PDV identifikacijski broj) - Croatia.

          - `hu_cjs`
            Company registration number (Cégjegyzékszám) - Hungary.

          - `hu_tin`
            Adószám - Hungary.

          - `hu_vat`
            VAT Number (ANUM) - Hungary.

          - `ie_crn`
            Company Registration Number (CRN) - Ireland.

          - `ie_trn`
            Tax registration number (TRN) - Ireland.

          - `ie_vat`
            VAT Number - Ireland.

          - `it_rea`
            Numero Repertorio Economico e Amministrativo (REA) - Italy.

          - `it_vat`
            Partita IVA - Italy.

          - `jp_cn`
            Corporate number (Corporate “My Number”) - Japan.

          - `kz_bin`
            Business Identification Number (BIN) - Kazakhstan.

          - `li_uid`
            Handelsregisternummer - Liechtenstein.

          - `lt_ccrn`
            Central Commercial Registry Number / Certificate Number - Lithuania.

          - `lt_vat`
            VAT Number (PVM kodas) - Lithuania.

          - `lu_nif`
            Numéro d’identification fiscale (NIF) - Luxembourg.

          - `lu_rcs`
            Registre de commerce et des sociétés (RCS) number - Luxembourg.

          - `lu_vat`
            VAT Number (No. TVA) - Luxembourg.

          - `lv_urn`
            Uzņēmumu reģistrs number - Latvia.

          - `lv_vat`
            VAT Number (PVN) - Latvia.

          - `mt_crn`
            Company Registration Number - Malta.

          - `mt_tin`
            Tax identification number - Malta.

          - `mt_vat`
            VAT Registration Number - Malta.

          - `mx_rfc`
            Registro Federal de Contribuyentes (RFC) - Mexico.

          - `my_brn`
            Malaysia Business Registration Number (BRN) - Malaysia.

          - `my_coid`
            Corporate Identity Number (MyCoID) - Malaysia.

          - `my_itn`
            Tax Identification Number (TIN) - Malaysia.

          - `my_sst`
            Malaysia Sales and Service Tax Number (SST) - Malaysia.

          - `mz_nuit`
            Mozambique Taxpayer Single ID Number (NUIT) - Mozambique.

          - `nl_kvk`
            Chamber of Commerce (KVK) Number - Netherlands.

          - `nl_rsin`
            Tax Identification Number (RSIN) - Netherlands.

          - `nl_vat`
            VAT Number (Btw-nr.) - Netherlands.

          - `no_orgnr`
            Organisasjonsnummer - Norway.

          - `nz_bn`
            New Zealand Business Number (NZBN) - New Zealand.

          - `nz_ird`
            Inland Revenue Department (IRD) Number - New Zealand.

          - `pe_ruc`
            Registro Único de Contribuyentes (RUC) - Peru.

          - `pk_ntn`
            National Tax Number (NTN) - Pakistan.

          - `pl_nip`
            Numer Identyfikacji Podatkowej (NIP) - Poland.

          - `pl_regon`
            REGON number - Poland.

          - `pl_vat`
            VAT Number (NIP) - Poland.

          - `pt_vat`
            VAT number (Número de Identificação Fiscal (NIF)) - Portugal.

          - `ro_cui`
            Codul de identificare fiscală (CIF/CUI) - Romania.

          - `ro_orc`
            Număr de ordine în registrul comerțului (Nr. ORC) - Romania.

          - `ro_vat`
            VAT Number (CIF) - Romania.

          - `sa_crn`
            Commercial Registration Number - Saudi Arabia.

          - `sa_tin`
            ZATCA-Issued Tax Identification Number - Saudi Arabia.

          - `se_orgnr`
            Organisationsnummer - Sweden.

          - `se_vat`
            VAT Number (Momsnr.) - Sweden.

          - `sg_uen`
            Unique Entity Number (UEN) - Singapore.

          - `si_msp`
            Company Identification Number (Matična številka podjetja) - Slovenia.

          - `si_tin`
            Davčna številka - Slovenia.

          - `si_vat`
            VAT Number (ID za DDV) - Slovenia.

          - `sk_dic`
            Daňové identifikačné číslo (DIČ) - Slovakia.

          - `sk_ico`
            Organization identification number (ICO) - Slovakia.

          - `sk_vat`
            VAT Number (IČ DPH) - Slovakia.

          - `th_crn`
            Company registration number (CRN) - Thailand.

          - `th_prn`
            Partnership registration number (PRN) - Thailand.

          - `th_tin`
            Taxpayer Identification Number (TIN) (หมายเลขประจำตัวผู้เสียภาษี) - Thailand.

          - `us_ein`
            Employer Identification Number (EIN) - United States.

      - `data.identity.business_details.monthly_estimated_revenue` (object, nullable)
        An estimate of the monthly revenue of the business. Only accepted for accounts in Brazil and India.

        - `data.identity.business_details.monthly_estimated_revenue.amount` (object, nullable)
          Estimated monthly revenue amount in minor currency units (for example, ‘123’ for 1.23 USD).

          - `data.identity.business_details.monthly_estimated_revenue.amount.currency` (string)
            A lowercase alpha3 currency code like “usd”.

          - `data.identity.business_details.monthly_estimated_revenue.amount.value` (integer)
            In minor units like 123 for 1.23 USD.

      - `data.identity.business_details.phone` (string, nullable)
        The company’s phone number (used for verification).

      - `data.identity.business_details.registered_name` (string, nullable)
        The business legal name.

      - `data.identity.business_details.script_addresses` (object, nullable)
        The business registration address of the business entity in non latin script.

        - `data.identity.business_details.script_addresses.kana` (object, nullable)
          Kana Address.

          - `data.identity.business_details.script_addresses.kana.city` (string, nullable)
            City, district, suburb, town, or village.

          - `data.identity.business_details.script_addresses.kana.country` (enum, nullable)
            Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

          - `data.identity.business_details.script_addresses.kana.line1` (string, nullable)
            Address line 1 (e.g., street, PO Box, or company name).

          - `data.identity.business_details.script_addresses.kana.line2` (string, nullable)
            Address line 2 (e.g., apartment, suite, unit, or building).

          - `data.identity.business_details.script_addresses.kana.postal_code` (string, nullable)
            ZIP or postal code.

          - `data.identity.business_details.script_addresses.kana.state` (string, nullable)
            State, county, province, or region.

          - `data.identity.business_details.script_addresses.kana.town` (string, nullable)
            Town or district.

        - `data.identity.business_details.script_addresses.kanji` (object, nullable)
          Kanji Address.

          - `data.identity.business_details.script_addresses.kanji.city` (string, nullable)
            City, district, suburb, town, or village.

          - `data.identity.business_details.script_addresses.kanji.country` (enum, nullable)
            Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

          - `data.identity.business_details.script_addresses.kanji.line1` (string, nullable)
            Address line 1 (e.g., street, PO Box, or company name).

          - `data.identity.business_details.script_addresses.kanji.line2` (string, nullable)
            Address line 2 (e.g., apartment, suite, unit, or building).

          - `data.identity.business_details.script_addresses.kanji.postal_code` (string, nullable)
            ZIP or postal code.

          - `data.identity.business_details.script_addresses.kanji.state` (string, nullable)
            State, county, province, or region.

          - `data.identity.business_details.script_addresses.kanji.town` (string, nullable)
            Town or district.

      - `data.identity.business_details.script_names` (object, nullable)
        The business legal name in non latin script.

        - `data.identity.business_details.script_names.kana` (object, nullable)
          Kana name.

          - `data.identity.business_details.script_names.kana.registered_name` (string, nullable)
            Registered name of the business.

        - `data.identity.business_details.script_names.kanji` (object, nullable)
          Kanji name.

          - `data.identity.business_details.script_names.kanji.registered_name` (string, nullable)
            Registered name of the business.

      - `data.identity.business_details.structure` (enum, nullable)
        The category identifying the legal structure of the business.
Possible enum values:
        - `cooperative`
          A cooperative organization.

        - `free_zone_establishment`
          A free zone establishment.

        - `free_zone_llc`
          A free zone LLC.

        - `government_instrumentality`
          An organization formed by statute or by a government body in the US to perform a function, but not part of the government itself.

        - `governmental_unit`
          A branch of the state, local, or federal government of the US.

        - `incorporated_association`
          An incorporated association.

        - `incorporated_non_profit`
          An organization incorporated under US state law with tax-exempt status as a nonprofit (for example, 501©(3)).

        - `incorporated_partnership`
          Also called ‘Limited Partnerships’ or ‘Registered Ordinary Partnerships’, these are businesses registered in Thailand owned by two or more people. The business’ legal entity and its legal personality is separated and distinct from the individual partners.

        - `limited_liability_partnership`
          A limited liability partnership.

        - `llc`
          An LLC.

        - `multi_member_llc`
          A business with multiple owners or members that’s registered in a US state as a Limited Liability Company (LLC).

        - `private_company`
          A private company.

        - `private_corporation`
          A business incorporated in a US state that’s privately owned. It doesn’t have shares that are traded on a public stock exchange. It’s also called a closely-held corporation. If you’re a single-member LLC that has elected to be treated as a corporation for tax purposes, use this classification.

        - `private_partnership`
          A business jointly owned by two or more people that’s created through a partnership agreement.

        - `public_company`
          A public company.

        - `public_corporation`
          A business incorporated under the laws of a US state. Ownership shares of this corporation are traded on a public stock exchange.

        - `public_listed_corporation`
          A public corporation that is specifically listed.

        - `public_partnership`
          A business formed by a partnership agreement with one or more people, but has shares that are publicly traded on a stock exchange.

        - `registered_charity`
          A charitable organization, public foundation, or private foundation registered with the Canada Revenue Agency.

        - `single_member_llc`
          A business entity registered with a US state as a limited liability company (LLC) and that has only one member or owner.

        - `sole_establishment`
          A sole establishment.

        - `sole_proprietorship`
          A business that isn’t a separate legal entity from its individual owner.

        - `tax_exempt_government_instrumentality`
          A tax exempt government instrumentality.

        - `trust`
          A trust.

        - `unincorporated_association`
          A business venture of two or more people that doesn’t have a formal corporate or entity structure.

        - `unincorporated_non_profit`
          An unincorporated nonprofit.

        - `unincorporated_partnership`
          An unincorporated partnership.

    - `data.identity.country` (enum, nullable)
      The country in which the account holder resides, or in which the business is legally established. This should be an [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country code.

    - `data.identity.entity_type` (enum, nullable)
      The entity type.
Possible enum values:
      - `company`
        A registered business.

      - `government_entity`
        A government entity.

      - `individual`
        An individual that is not registered as a business.

      - `non_profit`
        A nonprofit organization.

    - `data.identity.individual` (object, nullable)
      Information about the individual represented by the Account. This property is `null` unless `entity_type` is set to `individual`.

      - `data.identity.individual.id` (string)
        Unique identifier for the object.

      - `data.identity.individual.object` (string)
        String representing the object’s type. Objects of the same type share the same value.

      - `data.identity.individual.account` (string)
        The account ID which the individual belongs to.

      - `data.identity.individual.additional_addresses` (array of objects, nullable)
        Additional addresses associated with the individual.

        - `data.identity.individual.additional_addresses.city` (string, nullable)
          City, district, suburb, town, or village.

        - `data.identity.individual.additional_addresses.country` (enum, nullable)
          Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

        - `data.identity.individual.additional_addresses.line1` (string, nullable)
          Address line 1 (e.g., street, PO Box, or company name).

        - `data.identity.individual.additional_addresses.line2` (string, nullable)
          Address line 2 (e.g., apartment, suite, unit, or building).

        - `data.identity.individual.additional_addresses.postal_code` (string, nullable)
          ZIP or postal code.

        - `data.identity.individual.additional_addresses.purpose` (enum)
          Purpose of additional address.
Possible enum values:
          - `registered`
            The registered address.

        - `data.identity.individual.additional_addresses.state` (string, nullable)
          State, county, province, or region.

        - `data.identity.individual.additional_addresses.town` (string, nullable)
          Town or district.

      - `data.identity.individual.additional_names` (array of objects, nullable)
        Additional names (e.g. aliases) associated with the individual.

        - `data.identity.individual.additional_names.full_name` (string, nullable)
          The individual’s full name.

        - `data.identity.individual.additional_names.given_name` (string, nullable)
          The individual’s first or given name.

        - `data.identity.individual.additional_names.purpose` (enum)
          The purpose or type of the additional name.
Possible enum values:
          - `alias`
            An alias for the individual’s name.

          - `maiden`
            The maiden name of the individual.

        - `data.identity.individual.additional_names.surname` (string, nullable)
          The individual’s last or family name.

      - `data.identity.individual.additional_terms_of_service` (object, nullable)
        Terms of service acceptances.

        - `data.identity.individual.additional_terms_of_service.account` (object, nullable)
          Stripe terms of service agreement.

          - `data.identity.individual.additional_terms_of_service.account.date` (timestamp, nullable)
            The time when the Account’s representative accepted the terms of service. Represented as a RFC 3339 date & time UTC value in millisecond precision, for example: 2022-09-18T13:22:18.123Z.

          - `data.identity.individual.additional_terms_of_service.account.ip` (string, nullable)
            The IP address from which the Account’s representative accepted the terms of service.

          - `data.identity.individual.additional_terms_of_service.account.user_agent` (string, nullable)
            The user agent of the browser from which the Account’s representative accepted the terms of service.

      - `data.identity.individual.address` (object, nullable)
        The individual’s residential address.

        - `data.identity.individual.address.city` (string, nullable)
          City, district, suburb, town, or village.

        - `data.identity.individual.address.country` (enum, nullable)
          Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

        - `data.identity.individual.address.line1` (string, nullable)
          Address line 1 (e.g., street, PO Box, or company name).

        - `data.identity.individual.address.line2` (string, nullable)
          Address line 2 (e.g., apartment, suite, unit, or building).

        - `data.identity.individual.address.postal_code` (string, nullable)
          ZIP or postal code.

        - `data.identity.individual.address.state` (string, nullable)
          State, county, province, or region.

        - `data.identity.individual.address.town` (string, nullable)
          Town or district.

      - `data.identity.individual.created` (timestamp)
        Time at which the object was created. Represented as a RFC 3339 date & time UTC value in millisecond precision, for example: 2022-09-18T13:22:18.123Z.

      - `data.identity.individual.date_of_birth` (object, nullable)
        The individual’s date of birth.

        - `data.identity.individual.date_of_birth.day` (integer)
          The day of birth, between 1 and 31.

        - `data.identity.individual.date_of_birth.month` (integer)
          The month of birth, between 1 and 12.

        - `data.identity.individual.date_of_birth.year` (integer)
          The four-digit year of birth.

      - `data.identity.individual.documents` (object, nullable)
        Documents that may be submitted to satisfy various informational requests.

        - `data.identity.individual.documents.company_authorization` (object, nullable)
          One or more documents that demonstrate proof that this person is authorized to represent the company.

          - `data.identity.individual.documents.company_authorization.files` (array of strings)
            One or more document IDs returned by a [file upload](https://docs.stripe.com/api/persons/update.md#create_file) with a purpose value of `account_requirement`.

          - `data.identity.individual.documents.company_authorization.type` (enum)
            The format of the document. Currently supports `files` only.
Possible enum values:
            - `files`
              Document type with multiple files.

        - `data.identity.individual.documents.passport` (object, nullable)
          One or more documents showing the person’s passport page with photo and personal data.

          - `data.identity.individual.documents.passport.files` (array of strings)
            One or more document IDs returned by a [file upload](https://docs.stripe.com/api/persons/update.md#create_file) with a purpose value of `account_requirement`.

          - `data.identity.individual.documents.passport.type` (enum)
            The format of the document. Currently supports `files` only.
Possible enum values:
            - `files`
              Document type with multiple files.

        - `data.identity.individual.documents.primary_verification` (object, nullable)
          An identifying document showing the person’s name, either a passport or local ID card.

          - `data.identity.individual.documents.primary_verification.front_back` (object)
            The [file upload](https://docs.stripe.com/api/persons/update.md#create_file) tokens for the front and back of the verification document.

            - `data.identity.individual.documents.primary_verification.front_back.back` (string, nullable)
              A [file upload](https://docs.stripe.com/api/persons/update.md#create_file) token representing the back of the verification document. The purpose of the uploaded file should be ‘identity_document’. The uploaded file needs to be a color image (smaller than 8,000px by 8,000px), in JPG, PNG, or PDF format, and less than 10 MB in size.

            - `data.identity.individual.documents.primary_verification.front_back.front` (string)
              A [file upload](https://docs.stripe.com/api/persons/update.md#create_file) token representing the front of the verification document. The purpose of the uploaded file should be ‘identity_document’. The uploaded file needs to be a color image (smaller than 8,000px by 8,000px), in JPG, PNG, or PDF format, and less than 10 MB in size.

          - `data.identity.individual.documents.primary_verification.type` (enum)
            The format of the verification document. Currently supports `front_back` only.
Possible enum values:
            - `front_back`
              Document type with both front and back sides.

        - `data.identity.individual.documents.secondary_verification` (object, nullable)
          A document showing address, either a passport, local ID card, or utility bill from a well-known utility company.

          - `data.identity.individual.documents.secondary_verification.front_back` (object)
            The [file upload](https://docs.stripe.com/api/persons/update.md#create_file) tokens for the front and back of the verification document.

            - `data.identity.individual.documents.secondary_verification.front_back.back` (string, nullable)
              A [file upload](https://docs.stripe.com/api/persons/update.md#create_file) token representing the back of the verification document. The purpose of the uploaded file should be ‘identity_document’. The uploaded file needs to be a color image (smaller than 8,000px by 8,000px), in JPG, PNG, or PDF format, and less than 10 MB in size.

            - `data.identity.individual.documents.secondary_verification.front_back.front` (string)
              A [file upload](https://docs.stripe.com/api/persons/update.md#create_file) token representing the front of the verification document. The purpose of the uploaded file should be ‘identity_document’. The uploaded file needs to be a color image (smaller than 8,000px by 8,000px), in JPG, PNG, or PDF format, and less than 10 MB in size.

          - `data.identity.individual.documents.secondary_verification.type` (enum)
            The format of the verification document. Currently supports `front_back` only.
Possible enum values:
            - `front_back`
              Document type with both front and back sides.

        - `data.identity.individual.documents.visa` (object, nullable)
          One or more documents showing the person’s visa required for living in the country where they are residing.

          - `data.identity.individual.documents.visa.files` (array of strings)
            One or more document IDs returned by a [file upload](https://docs.stripe.com/api/persons/update.md#create_file) with a purpose value of `account_requirement`.

          - `data.identity.individual.documents.visa.type` (enum)
            The format of the document. Currently supports `files` only.
Possible enum values:
            - `files`
              Document type with multiple files.

      - `data.identity.individual.email` (string, nullable)
        The individual’s email address.

      - `data.identity.individual.given_name` (string, nullable)
        The individual’s first name.

      - `data.identity.individual.id_numbers` (array of objects, nullable)
        The identification numbers (e.g., SSN) associated with the individual.

        - `data.identity.individual.id_numbers.type` (enum)
          The ID number type of an individual.
Possible enum values:
          - `ae_eid`
            Emirates ID - United Arab Emirates.

          - `ao_nif`
            Número de Identificação Fiscal (Tax Identification Number) - Angola.

          - `ar_cuil`
            Código Único de Identificación Laboral (CUIL) - Argentina.

          - `ar_dni`
            Documento Nacional de Identidad (DNI) - Argentina.

          - `at_stn`
            Steuernummer - Austria.

          - `az_tin`
            Tax Identification Number - Azerbaijan.

          - `bd_brc`
            Birth Registration Certificate (BRC) - Bangladesh.

          - `bd_etin`
            Electronic Tax Identification Number (ETIN) - Bangladesh.

          - `bd_nid`
            National Identification Number (NID) - Bangladesh.

          - `be_nrn`
            National Registration Number (NRN) - Belgium.

          - `bg_ucn`
            Unified Civil Number (Единен граждански номер) - Bulgaria.

          - `bn_nric`
            National Registration Identity Card number (NRIC) - Brunei Darussalam.

          - `br_cpf`
            Cadastro de Pessoas Físicas - Brazil.

          - `ca_sin`
            Social Insurance Number (SIN) - Canada.

          - `ch_oasi`
            OASI / AHV / AVS - Switzerland.

          - `cl_rut`
            Rol Único Tributario (RUT) - Chile.

          - `cn_pp`
            Passport number (护照号码) - China.

          - `co_nuip`
            Número Único de Identificación Personal (NUIP) - Colombia.

          - `cr_ci`
            Número de cédula de identidad - Costa Rica.

          - `cr_cpf`
            Cédula de Persona Fisica (CPF) - Costa Rica.

          - `cr_dimex`
            Documento de Identidad Migratorio para Extranjeros (DIMEX) - Costa Rica.

          - `cr_nite`
            Número de Indetificación Tributario Especial (NITE) - Costa Rica.

          - `cy_tic`
            Tax Identification Code (TIC) - Cyprus.

          - `cz_rc`
            Rodné číslo - Czech Republic.

          - `de_stn`
            Tax Identification Number (Steuer-ID) - Germany.

          - `dk_cpr`
            Personnummer (CPR) - Denmark.

          - `do_cie`
            Número de cédula de identidad y electoral - Dominican Republic.

          - `do_rcn`
            Registro Nacional del Contribuyente (RNC) - Dominican Republic.

          - `ec_ci`
            Número de Cédula de Identidad - Ecuador.

          - `ee_ik`
            Isikukood (PIC) - Estonia.

          - `es_nif`
            Número de Identificación Fiscal (NIF) - Spain.

          - `fi_hetu`
            Henkilötunnus (HETU) - Finland.

          - `fr_nir`
            Numéro d’inscription au répertoire (NIR) - France.

          - `gb_nino`
            National Insurance Number (NINO) - United Kingdom.

          - `gr_afm`
            Tax Identification Number (ΑΦΜ) - Greece.

          - `gt_nit`
            Número de Identificación Tributaria (NIT) - Guatemala.

          - `hk_id`
            Hong Kong Identity Card Number - Hong Kong.

          - `hr_oib`
            Osobni identifikacijski broj (OIB) - Croatia.

          - `hu_ad`
            Adóazonosító - Hungary.

          - `id_nik`
            Nomor Induk Kependudukan (NIK) - Indonesia.

          - `ie_ppsn`
            Personal Public Service Number (PPSN) - Ireland.

          - `is_kt`
            Kennitala - Iceland.

          - `it_cf`
            Codice fiscale - Italy.

          - `jp_inc`
            Individual Number Card (個人番号) - Japan.

          - `ke_pin`
            Kenya Revenue Authority PIN - Kenya.

          - `kz_iin`
            Identification Number (IIN) - Kazakhstan.

          - `li_peid`
            Personenidentifikationsnummer (PEID) - Liechtenstein.

          - `lt_ak`
            Asmens kodas - Lithuania.

          - `lu_nif`
            Numéro d’Identification Personnelle (NIF) - Luxembourg.

          - `lv_pk`
            Personas kods - Latvia.

          - `mx_rfc`
            Personal RFC - Mexico.

          - `my_nric`
            National Registration Identity Card Number - Malaysia.

          - `mz_nuit`
            Mozambique Taxpayer Single ID Number (NUIT) - Mozambique.

          - `ng_nin`
            National Identity Number (NIN) - Nigeria.

          - `nl_bsn`
            Citizen Service Number (BSN) - Netherlands.

          - `no_nin`
            Fødselsnummer (NIN) - Norway.

          - `nz_ird`
            IRD number - New Zealand.

          - `pe_dni`
            Documento Nacional de Identidad (DNI) - Peru.

          - `pk_cnic`
            Computerized National Identity Card Number (CNIC) - Pakistan.

          - `pk_snic`
            Smart National Identity Card Number (SNIC) - Pakistan.

          - `pl_pesel`
            PESEL number - Poland.

          - `pt_nif`
            Número de Identificação Fiscal (NIF) - Portugal.

          - `ro_cnp`
            Codul Numeric Personal (CNP) - Romania.

          - `sa_tin`
            ZATCA-Issued Tax Identification Number - Saudi Arabia.

          - `se_pin`
            Personnummer (PIN) - Sweden.

          - `sg_fin`
            Foreign Identification Number - Singapore.

          - `sg_nric`
            National Registration Identity Card - Singapore.

          - `sk_dic`
            Daňové Identifikačné Číslo (DIC) - Slovakia.

          - `th_lc`
            Laser Code (เลเซอร์ ไอดี) - Thailand.

          - `th_pin`
            Personal Identification Number (เลขประจำตัวประชาชน) - Thailand.

          - `tr_tin`
            Tax Identification Number (TIN) - Turkey.

          - `us_itin`
            Individual Taxpayer Identification Number - United States.

          - `us_itin_last_4`
            Last 4 digits of Individual Taxpayer Identification Number - United States.

          - `us_ssn`
            Social Security Number - United States. If the us_ssn_last_4 is verified, this value populates automatically.

          - `us_ssn_last_4`
            Last 4 digits of Social Security Number - United States.

          - `uy_dni`
            Número de Documento Nacional de Identidad - Uruguay.

          - `za_id`
            South African ID Number - South Africa.

      - `data.identity.individual.legal_gender` (enum, nullable)
        The individual’s gender (International regulations require either "male” or “female”).
Possible enum values:
        - `female`
          Female gender person.

        - `male`
          Male gender person.

      - `data.identity.individual.metadata` (map, nullable)
        Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

      - `data.identity.individual.nationalities` (array of enums, nullable)
        The countries where the individual is a national. Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

      - `data.identity.individual.phone` (string, nullable)
        The individual’s phone number.

      - `data.identity.individual.political_exposure` (enum, nullable)
        Indicates if the individual or any of their representatives, family members, or other closely related persons, declares that they hold or have held an important public job or function, in any jurisdiction.
Possible enum values:
        - `existing`
          The person has disclosed that they do have political exposure.

        - `none`
          The person has disclosed that they have no political exposure.

      - `data.identity.individual.relationship` (object, nullable)
        The relationship that this individual has with the Account’s identity.

        - `data.identity.individual.relationship.authorizer` (boolean, nullable)
          Whether the individual is an authorizer of the Account’s identity.

        - `data.identity.individual.relationship.director` (boolean, nullable)
          Whether the individual is a director of the Account’s identity. Directors are typically members of the governing board of the company or are responsible for making sure that the company meets its regulatory obligations.

        - `data.identity.individual.relationship.executive` (boolean, nullable)
          Whether the individual has significant responsibility to control, manage, or direct the organization.

        - `data.identity.individual.relationship.legal_guardian` (boolean, nullable)
          Whether the individual is the legal guardian of the Account’s representative.

        - `data.identity.individual.relationship.owner` (boolean, nullable)
          Whether the individual is an owner of the Account’s identity.

        - `data.identity.individual.relationship.percent_ownership` (decimal, nullable)
          The percentage of the Account’s identity that the individual owns.

        - `data.identity.individual.relationship.representative` (boolean, nullable)
          Whether the individual is authorized as the primary representative of the Account. This is the person nominated by the business to provide information about themselves, and general information about the account. There can only be one representative at any given time. At the time the account is created, this person should be set to the person responsible for opening the account.

        - `data.identity.individual.relationship.title` (string, nullable)
          The individual’s title (e.g., CEO, Support Engineer).

      - `data.identity.individual.script_addresses` (object, nullable)
        The script addresses (e.g., non-Latin characters) associated with the individual.

        - `data.identity.individual.script_addresses.kana` (object, nullable)
          Kana Address.

          - `data.identity.individual.script_addresses.kana.city` (string, nullable)
            City, district, suburb, town, or village.

          - `data.identity.individual.script_addresses.kana.country` (enum, nullable)
            Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

          - `data.identity.individual.script_addresses.kana.line1` (string, nullable)
            Address line 1 (e.g., street, PO Box, or company name).

          - `data.identity.individual.script_addresses.kana.line2` (string, nullable)
            Address line 2 (e.g., apartment, suite, unit, or building).

          - `data.identity.individual.script_addresses.kana.postal_code` (string, nullable)
            ZIP or postal code.

          - `data.identity.individual.script_addresses.kana.state` (string, nullable)
            State, county, province, or region.

          - `data.identity.individual.script_addresses.kana.town` (string, nullable)
            Town or district.

        - `data.identity.individual.script_addresses.kanji` (object, nullable)
          Kanji Address.

          - `data.identity.individual.script_addresses.kanji.city` (string, nullable)
            City, district, suburb, town, or village.

          - `data.identity.individual.script_addresses.kanji.country` (enum, nullable)
            Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

          - `data.identity.individual.script_addresses.kanji.line1` (string, nullable)
            Address line 1 (e.g., street, PO Box, or company name).

          - `data.identity.individual.script_addresses.kanji.line2` (string, nullable)
            Address line 2 (e.g., apartment, suite, unit, or building).

          - `data.identity.individual.script_addresses.kanji.postal_code` (string, nullable)
            ZIP or postal code.

          - `data.identity.individual.script_addresses.kanji.state` (string, nullable)
            State, county, province, or region.

          - `data.identity.individual.script_addresses.kanji.town` (string, nullable)
            Town or district.

      - `data.identity.individual.script_names` (object, nullable)
        The script names (e.g. non-Latin characters) associated with the individual.

        - `data.identity.individual.script_names.kana` (object, nullable)
          Persons name in kana script.

          - `data.identity.individual.script_names.kana.given_name` (string, nullable)
            The person’s first or given name.

          - `data.identity.individual.script_names.kana.surname` (string, nullable)
            The person’s last or family name.

        - `data.identity.individual.script_names.kanji` (object, nullable)
          Persons name in kanji script.

          - `data.identity.individual.script_names.kanji.given_name` (string, nullable)
            The person’s first or given name.

          - `data.identity.individual.script_names.kanji.surname` (string, nullable)
            The person’s last or family name.

      - `data.identity.individual.surname` (string, nullable)
        The individual’s last name.

      - `data.identity.individual.updated` (timestamp)
        Time at which the object was last updated.

  - `data.livemode` (boolean)
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.

  - `data.metadata` (map, nullable)
    Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

  - `data.requirements` (object, nullable)
    Information about the active requirements for the Account, including what information needs to be collected, and by when.

    - `data.requirements.entries` (array of objects, nullable)
      A list of requirements for the Account.

      - `data.requirements.entries.awaiting_action_from` (enum)
        Indicates whether the platform or Stripe is currently responsible for taking action on the requirement. Value can be `user` or `stripe`.
Possible enum values:
        - `stripe`
          Integrator should do nothing.

        - `user`
          Integrator should take action.

      - `data.requirements.entries.description` (string)
        Machine-readable string describing the requirement.

      - `data.requirements.entries.errors` (array of objects)
        Descriptions of why the requirement must be collected, or why the collected information isn’t satisfactory to Stripe.

        - `data.requirements.entries.errors.code` (enum)
          Machine-readable code describing the error.
Possible enum values:
          - `invalid_address_city_state_postal_code`
            The combination of the city, state, and postal code in the provided address could not be validated.

          - `invalid_address_highway_contract_box`
            Invalid address. Your business address must be a valid physical address from which you conduct business and cannot be a Highway Contract Box.

          - `invalid_address_private_mailbox`
            Invalid address. Your business address must be a valid physical address from which you conduct business and cannot be a private mailbox.

          - `invalid_business_profile_name`
            Business profile names must consist of recognizable words.

          - `invalid_business_profile_name_denylisted`
            Generic or well-known business names aren’t supported.

          - `invalid_company_name_denylisted`
            Generic or well-known business names aren’t supported.

          - `invalid_dob_age_over_maximum`
            Date of birth must be within the past 120 years.

          - `invalid_dob_age_under_18`
            Underage. Age must be at least 18.

          - `invalid_dob_age_under_minimum`
            Person must be at least 13 years old.

          - `invalid_product_description_length`
            Your product description must be at least 10 characters.

          - `invalid_product_description_url_match`
            Your product description must be different from your URL.

          - `invalid_representative_country`
            The representative must have an address in the same country as the company.

          - `invalid_statement_descriptor_business_mismatch`
            The statement descriptor must be similar to your business name, legal entity name, or URL.

          - `invalid_statement_descriptor_denylisted`
            Generic or well-known statement descriptors aren’t supported.

          - `invalid_statement_descriptor_length`
            The statement descriptor must be at least 5 characters.

          - `invalid_statement_descriptor_prefix_denylisted`
            Generic or well-known statement descriptor prefixes aren’t supported.

          - `invalid_statement_descriptor_prefix_mismatch`
            The statement descriptor prefix must be similar to your statement descriptor, business name, legal entity name, or URL.

          - `invalid_street_address`
            The street name and/or number for the provided address could not be validated.

          - `invalid_tax_id`
            The provided tax ID must have 9 digits.

          - `invalid_tax_id_format`
            Tax IDs must be a unique set of 9 numbers without dashes or other special characters.

          - `invalid_tos_acceptance`
            The existing terms of service signature has been invalidated because the account’s tax ID has changed. The account needs to accept the terms of service again. For more information, see [this documentation](https://docs.stripe.com/connect/update-verified-information.md).

          - `invalid_url_denylisted`
            Generic business URLs aren’t supported.

          - `invalid_url_format`
            URL must be formatted as https://example.com.

          - `invalid_url_web_presence_detected`
            Because you use a website, app, social media page, or online profile to sell products or services, you must provide a URL for your business.

          - `invalid_url_website_business_information_mismatch`
            The business information on your website must match the details you provided to Stripe.

          - `invalid_url_website_empty`
            Your provided website appears to be empty.

          - `invalid_url_website_inaccessible`
            This URL couldn’t be reached. Make sure it’s available and entered correctly or provide another.

          - `invalid_url_website_inaccessible_geoblocked`
            Your provided website appears to be geographically blocked.

          - `invalid_url_website_inaccessible_password_protected`
            Your provided website appears to be password protected.

          - `invalid_url_website_incomplete`
            Your website seems to be missing some required information. [Learn about the requirements](https://support.stripe.com/questions/information-required-on-your-business-website-to-use-stripe).

          - `invalid_url_website_incomplete_cancellation_policy`
            Your provided website appears to have an incomplete cancellation policy.

          - `invalid_url_website_incomplete_customer_service_details`
            Your provided website appears to have incomplete customer service details.

          - `invalid_url_website_incomplete_legal_restrictions`
            Your provided website appears to have incomplete legal restrictions.

          - `invalid_url_website_incomplete_refund_policy`
            Your provided website appears to have an incomplete refund policy.

          - `invalid_url_website_incomplete_return_policy`
            Your provided website appears to have an incomplete refund policy.

          - `invalid_url_website_incomplete_terms_and_conditions`
            Your provided website appears to have incomplete terms and conditions.

          - `invalid_url_website_incomplete_under_construction`
            Your provided website appears to be incomplete or under construction.

          - `invalid_url_website_other`
            We weren’t able to verify your business using the URL you provided. Make sure it’s entered correctly or provide another URL.

          - `invalid_value_other`
            An invalid value was provided for the related field. This is a general error code.

          - `unresolvable_ip_address`
            IP address did not resolve to a valid tax location.

          - `unresolvable_postal_code`
            Postal code did not resolve to a valid tax location.

          - `verification_directors_mismatch`
            Directors on the account don’t match government records. Update the account and upload a directorship document with current directors.

          - `verification_document_address_mismatch`
            Address on the account doesn’t match the verification document. Update the account and upload the document again.

          - `verification_document_address_missing`
            The company address was missing on the document. Upload a document that includes the address.

          - `verification_document_corrupt`
            File seems to be corrupted or damaged. Provide a different file.

          - `verification_document_country_not_supported`
            Document isn’t supported in this person’s country or region. Provide a supported verification document.

          - `verification_document_directors_mismatch`
            Directors on the account don’t match the document provided. Update the account to match the registration document and upload it again.

          - `verification_document_dob_mismatch`
            The date of birth (DOB) on the document did not match the DOB on the account. Upload a document with a matching DOB or update the DOB on the account.

          - `verification_document_duplicate_type`
            The same type of document was used twice. Two unique types of documents are required for verification.

          - `verification_document_expired`
            The document could not be used for verification because it has expired. If it’s an identity document, its expiration date must be after the date the document was submitted. If it’s an address document, the issue date must be within the last six months.

          - `verification_document_failed_copy`
            Document is a photo or screenshot. Upload the original document.

          - `verification_document_failed_greyscale`
            Document seems to be in grayscale or black and white. Provide a full color photo of the document for verification.

          - `verification_document_failed_other`
            The document could not be verified for an unknown reason. Ensure that the document follows the [guidelines for document uploads](https://docs.stripe.com/acceptable-verification-documents.md).

          - `verification_document_failed_test_mode`
            A test data helper was supplied to simulate verification failure. Refer to the documentation for [test file tokens](https://docs.stripe.com/connect/testing.md#test-file-tokens).

          - `verification_document_fraudulent`
            Document seems to be altered. This could be because it’s fraudulent.

          - `verification_document_id_number_mismatch`
            Tax ID number on the account doesn’t match the verification document. Update the account to match the verification document and upload it again.

          - `verification_document_id_number_missing`
            The company ID number was missing on the document. Upload a document that includes the ID number.

          - `verification_document_incomplete`
            Document doesn’t include required information. Make sure all pages and sections are complete.

          - `verification_document_invalid`
            Document isn’t an acceptable form of identification in this account’s country or region. Ensure that the document follows the [guidelines for document uploads](https://docs.stripe.com/acceptable-verification-documents.md).

          - `verification_document_issue_or_expiry_date_missing`
            Document is missing an expiration date. Provide a document with an expiration date.

          - `verification_document_manipulated`
            Document seems to be altered. This could be because it’s fraudulent.

          - `verification_document_missing_back`
            The back of the document is missing. Provide both sides of the document for verification.

          - `verification_document_missing_front`
            The front of the document is missing. Provide both sides of the document for verification.

          - `verification_document_name_mismatch`
            The name on the account does not match the name on the document. Update the account to match the document and upload it again.

          - `verification_document_name_missing`
            The company name was missing on the document. Upload a document that includes the company name.

          - `verification_document_nationality_mismatch`
            The nationality on the document did not match the person’s stated nationality. Update the person’s stated nationality, or upload a document that matches it.

          - `verification_document_not_readable`
            Document isn’t readable. This could be because it’s blurry or dark, or because the document was obstructed.

          - `verification_document_not_signed`
            Document doesn’t seem to be signed. Provide a signed document.

          - `verification_document_not_uploaded`
            Document didn’t upload because of a problem with the file.

          - `verification_document_photo_mismatch`
            ID photo on the document doesn’t match the selfie provided by this account.

          - `verification_document_too_large`
            Document file is too large. Upload one that’s 10MB or less.

          - `verification_document_type_not_supported`
            The provided document type is not accepted. Ensure that the document follows the [guidelines for document uploads](https://docs.stripe.com/acceptable-verification-documents.md).

          - `verification_extraneous_directors`
            Extraneous directors have been added to the account. Update the account and upload a registration document with current directors.

          - `verification_failed_address_match`
            The address on the account could not be verified. Correct any errors in the address field or upload a document that includes the address.

          - `verification_failed_business_iec_number`
            The Importer Exporter Code (IEC) number on your account could not be verified. Either correct any possible errors in the company name or IEC number. Refer to the support article for [accepting international payments in India](https://support.stripe.com/questions/accepting-international-payments-from-stripe-accounts-in-india).

          - `verification_failed_document_match`
            The document could not be verified. Upload a document that includes the company name, ID number, and address fields.

          - `verification_failed_id_number_match`
            ID number on the document doesn’t match the ID number provided by this account.

          - `verification_failed_keyed_identity`
            The person’s keyed-in identity information could not be verified. Correct any errors or upload a document that matches the identity fields (e.g., name and date of birth) entered.

          - `verification_failed_keyed_match`
            The keyed-in information on the account could not be verified. Correct any errors in the company name, ID number, or address fields. You can also upload a document that includes those fields.

          - `verification_failed_name_match`
            The company name on the account could not be verified. Correct any errors in the company name field or upload a document that includes the company name.

          - `verification_failed_other`
            Verification failed for an unknown reason. Correct any errors and resubmit the required fields.

          - `verification_failed_representative_authority`
            The authority of the account representative could not be verified. Please change the account representative to a person who is registered as an authorized representative. Please refer to [this support article](https://support.stripe.com/questions/representative-authority-verification).

          - `verification_failed_residential_address`
            We could not verify that the person resides at the provided address. The address must be a valid physical address where the individual resides and cannot be a P.O. Box.

          - `verification_failed_tax_id_match`
            The tax ID on the account cannot be verified by the IRS. Either correct any possible errors in the company name or tax ID, or upload a document that contains those fields.

          - `verification_failed_tax_id_not_issued`
            The tax ID on the account was not recognized by the IRS. Refer to the support article for [newly-issued tax ID numbers](https://support.stripe.com/questions/newly-issued-us-tax-id-number-tin-not-verifying).

          - `verification_missing_directors`
            Directors are missing from the account. Update the account and upload a registration document with current directors.

          - `verification_missing_executives`
            We have identified executives that haven’t been added on the account. Add any missing executives to the account.

          - `verification_missing_owners`
            We have identified owners that haven’t been added on the account. Add any missing owners to the account.

          - `verification_requires_additional_memorandum_of_associations`
            We have identified holding companies with significant percentage ownership. Upload a Memorandum of Association for each of the holding companies.

          - `verification_requires_additional_proof_of_registration`
            The uploaded document contains holding companies with significant percentage ownership. Upload a proof of registration for each of the holding companies.

          - `verification_selfie_document_missing_photo`
            Photo is missing from the document. Provide a document with a photo.

          - `verification_selfie_face_mismatch`
            Selfie doesn’t match the photo on the document. Provide a clear, well-lit, and unobstructed selfie.

          - `verification_selfie_manipulated`
            Selfie seems to be altered. This could be because it’s fraudulent.

          - `verification_selfie_unverified_other`
            Selfie couldn’t be verified. Provide a clear, well-lit, and unobstructed selfie that matches the photo on the identity document.

          - `verification_supportability`
            We can’t accept payments for this business under the Stripe Services Agreement without additional verification, as mentioned in the [prohibited and restricted businesses list](https://stripe.com/legal/restricted-businesses).

          - `verification_token_stale`
            The eID token submitted for liveness verification must be submitted within 5 minutes of obtaining it from the partner.

        - `data.requirements.entries.errors.description` (string)
          Human-readable description of the error.

      - `data.requirements.entries.impact` (object)
        A hash describing the impact of not collecting the requirement, or Stripe not being able to verify the collected information.

        - `data.requirements.entries.impact.restricts_capabilities` (array of objects, nullable)
          The Capabilities that will be restricted if the requirement is not collected and satisfactory to Stripe.

          - `data.requirements.entries.impact.restricts_capabilities.capability` (enum)
            The name of the Capability which will be restricted.
Possible enum values:
            - `ach_debit_payments`
              Capability to use ACH Debit payments.

            - `acss_debit_payments`
              Capability to use ACSS Debit payments.

            - `affirm_payments`
              Capability to use Affirm payments.

            - `afterpay_clearpay_payments`
              Capability to use Afterpay Clearpay payments.

            - `alma_payments`
              Capability to use Alma payments.

            - `amazon_pay_payments`
              Capability to use Amazon Pay payments.

            - `au_becs_debit_payments`
              Capability to use AU BECS Debit payments.

            - `automatic_indirect_tax`
              Capability to have taxes automatically corrected.

            - `bacs_debit_payments`
              Capability to use BACS Direct Debit payments.

            - `bancontact_payments`
              Capability to use Bancontact payments.

            - `bank_accounts.local`
              Capability to use Bank Accounts Local payouts.

            - `bank_accounts.wire`
              Capability to use Bank Accounts Wire payouts.

            - `blik_payments`
              Capability to use BLIK payments.

            - `boleto_payments`
              Capability to use Boleto payments.

            - `card_payments`
              Capability to collect card payments.

            - `cards`
              Capability to use Card payouts.

            - `cartes_bancaires_payments`
              Capability to use Cartes Bancaires payments.

            - `cashapp_payments`
              Capability to use CashApp payments.

            - `eps_payments`
              Capability to use EPS payments.

            - `fpx_payments`
              Capability to use FPX payments.

            - `gb_bank_transfer_payments`
              Capability to use GB bank transfer payments.

            - `grabpay_payments`
              Capability to use GrabPay payments.

            - `ideal_payments`
              Capability to use IDEAL payments.

            - `jcb_payments`
              Capability to use JCB payments.

            - `jp_bank_transfer_payments`
              Capability to use JP bank transfer payments.

            - `kakao_pay_payments`
              Capability to use Kakao Pay payments.

            - `klarna_payments`
              Capability to use Klarna payments.

            - `konbini_payments`
              Capability to use Konbini payments.

            - `kr_card_payments`
              Capability to use KR card payments.

            - `link_payments`
              Capability to use Link payments.

            - `mobilepay_payments`
              Capability to use MobilePay payments.

            - `multibanco_payments`
              Capability to use Multibanco payments.

            - `mx_bank_transfer_payments`
              Capability to use MX bank transfer payments.

            - `naver_pay_payments`
              Capability to use Naver Pay payments.

            - `oxxo_payments`
              Capability to use OXXO payments.

            - `p24_payments`
              Capability to use P24 payments.

            - `pay_by_bank_payments`
              Capability to use Pay by Bank payments.

            - `payco_payments`
              Capability to use Payco payments.

            - `paynow_payments`
              Capability to use PayNow payments.

            - `promptpay_payments`
              Capability to use PromptPay payments.

            - `revolut_pay_payments`
              Capability to use Revolut Pay payments.

            - `samsung_pay_payments`
              Capability to use Samsung Pay payments.

            - `sepa_bank_transfer_payments`
              Capability to use SEPA bank transfer payments.

            - `sepa_debit_payments`
              Capability to use SEPA Debit payments.

            - `stripe_balance.payouts`
              Capability to do payouts from the user’s Stripe balance.

            - `stripe_balance.stripe_transfers`
              Capability to receive transfers to the user’s Stripe balance.

            - `swish_payments`
              Capability to use Swish payments.

            - `twint_payments`
              Capability to use Twint payments.

            - `us_bank_transfer_payments`
              Capability to use US bank transfer payments.

            - `zip_payments`
              Capability to use Zip payments.

          - `data.requirements.entries.impact.restricts_capabilities.configuration` (enum)
            The configuration which specifies the Capability which will be restricted.
Possible enum values:
            - `customer`
              Customer configuration.

            - `merchant`
              Merchant configuration.

            - `recipient`
              Recipient configuration.

          - `data.requirements.entries.impact.restricts_capabilities.deadline` (object)
            Details about when in the account lifecycle the requirement must be collected by the avoid the Capability restriction.

            - `data.requirements.entries.impact.restricts_capabilities.deadline.status` (enum)
              The current status of the requirement’s impact.
Possible enum values:
              - `currently_due`
                The requirement needs to be collected to keep the account enabled.

              - `eventually_due`
                The requirement needs to be collected assuming all volume thresholds are met.

              - `past_due`
                The requirement needs to be collected to enable the account.

      - `data.requirements.entries.minimum_deadline` (object)
        The soonest point when the account will be impacted by not providing the requirement.

        - `data.requirements.entries.minimum_deadline.status` (enum)
          The current status of the requirement’s impact.
Possible enum values:
          - `currently_due`
            The requirement needs to be collected to keep the account enabled.

          - `eventually_due`
            The requirement needs to be collected assuming all volume thresholds are met.

          - `past_due`
            The requirement needs to be collected to enable the account.

      - `data.requirements.entries.reference` (object, nullable)
        A reference to the location of the requirement.

        - `data.requirements.entries.reference.inquiry` (string, nullable)
          If `inquiry` is the type, the inquiry token.

        - `data.requirements.entries.reference.resource` (string, nullable)
          If `resource` is the type, the resource token.

        - `data.requirements.entries.reference.type` (enum)
          The type of the reference. If the type is “inquiry”, the inquiry token can be found in the “inquiry” field. Otherwise the type is an API resource, the token for which can be found in the “resource” field.
Possible enum values:
          - `inquiry`
            An inquiry from Stripe.

          - `payment_method`
            A payment method.

          - `person`
            A person resource.

      - `data.requirements.entries.requested_reasons` (array of objects)
        A list of reasons why Stripe is collecting the requirement.

        - `data.requirements.entries.requested_reasons.code` (enum)
          Machine-readable description of Stripe’s reason for collecting the requirement.
Possible enum values:
          - `routine_onboarding`
            Stripe needs a basic set of information.

          - `routine_verification`
            Stripe needs to review provided information.

    - `data.requirements.summary` (object, nullable)
      An object containing an overview of requirements for the Account.

      - `data.requirements.summary.minimum_deadline` (object, nullable)
        The soonest date and time a requirement on the Account will become `past due`. Represented as a RFC 3339 date & time UTC value in millisecond precision, for example: `2022-09-18T13:22:18.123Z`.

        - `data.requirements.summary.minimum_deadline.status` (enum)
          The current strictest status of all requirements on the Account.
Possible enum values:
          - `currently_due`
            The requirement needs to be collected to keep the account enabled.

          - `eventually_due`
            The requirement needs to be collected assuming all volume thresholds are met.

          - `past_due`
            The requirement needs to be collected to enable the account.

        - `data.requirements.summary.minimum_deadline.time` (timestamp, nullable)
          The soonest RFC3339 date & time UTC value a requirement can impact the Account.

- `next_page_url` (string, nullable)
  URL with page token to navigate to next batch of accounts given by the list request.

- `previous_page_url` (string, nullable)
  URL with page token to navigate to previous batch of accounts given by the list request.

## Error Codes

| HTTP status code | Code                       | Description                                   |
| ---------------- | -------------------------- | --------------------------------------------- |
| 400              | accounts_v2_access_blocked | Accounts v2 is not enabled for your platform. |

```curl
curl -G https://api.stripe.com/v2/core/accounts \
  -H "Authorization: Bearer <<YOUR_SECRET_KEY>>" \
  -H "Stripe-Version: {{STRIPE_API_VERSION}}" \
  -d limit=2 \
  -d "applied_configurations[0]"=customer
```

```cli
stripe v2 core accounts list  \
  --limit=2 \
  --applied-configurations=customer
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

accounts = client.v2.core.accounts.list({
  limit: 2,
  applied_configurations: ['customer'],
})
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

accounts = client.v2.core.accounts.list({
  "limit": 2,
  "applied_configurations": ["customer"],
})
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$accounts = $stripe->v2->core->accounts->all([
  'limit' => 2,
  'applied_configurations' => ['customer'],
]);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

AccountListParams params =
  AccountListParams.builder()
    .setLimit(2L)
    .addAppliedConfiguration(AccountListParams.AppliedConfiguration.CUSTOMER)
    .build();

StripeCollection<Account> stripeCollection =
  client.v2().core().accounts().list(params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const accounts = await stripe.v2.core.accounts.list({
  limit: 2,
  applied_configurations: ['customer'],
});
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.V2CoreAccountListParams{
  AppliedConfigurations: []*string{stripe.String("customer")},
}
params.Limit = stripe.Int64(2)
result := sc.V2CoreAccounts.List(context.TODO(), params)
```

```dotnet
var options = new Stripe.V2.Core.AccountListOptions
{
    Limit = 2,
    AppliedConfigurations = new List<string> { "customer" },
};
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V2.Core.Accounts;
Stripe.V2.StripeList<Stripe.V2.Core.Account> accounts = service.List(options);
```

### Response

```json
{
  "data": [
    {
      "id": "acct_1QP3oLBUFVXWiKFB",
      "object": "v2.core.account",
      "applied_configurations": [
        "customer"
      ],
      "contact_email": "jenny.rosen@example.com",
      "created": "2024-11-25T15:02:50.000Z",
      "display_name": "Jenny Rosen",
      "livemode": true,
      "metadata": {}
    },
    {
      "id": "acct_1QO24tPeVxUa6gV6",
      "object": "v2.core.account",
      "applied_configurations": [
        "recipient",
        "customer",
        "merchant"
      ],
      "contact_email": "jenny.rosen@example.com",
      "created": "2024-11-22T18:59:45.000Z",
      "dashboard": "none",
      "display_name": "Jenny Rosen 2",
      "livemode": true,
      "metadata": {
        "my_key": "my_value"
      }
    }
  ],
  "next_page_url": "/v2/core/accounts?page=page_5dr8SFDbv7rZ2aj4ZSGuf4J1Dv58yE0YM4BhBqb2tg94CD5PDoUA7RD2AE7VBEH5C0E0qGJi1wMFPf9MEBbh6M125&limit=2&applied_configurations=customer"
}
```