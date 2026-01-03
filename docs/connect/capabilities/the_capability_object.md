# The Capability object

## Attributes

- `id` (string)
  The identifier for the capability.

- `object` (string)
  String representing the object’s type. Objects of the same type share the same value.

- `account` (string)
  The account for which the capability enables functionality.

- `future_requirements` (object)
  Information about the [upcoming new requirements for the capability](https://docs.stripe.com/docs/connect/custom-accounts/future-requirements.md), including what information needs to be collected, and by when.

  - `future_requirements.alternatives` (array of objects, nullable)
    Fields that are due and can be resolved by providing the corresponding alternative fields instead. Multiple alternatives can reference the same `original_fields_due`. When this happens, any of these alternatives can serve as a pathway for attempting to resolve the fields. Additionally, providing `original_fields_due` again also serves as a pathway for attempting to resolve the fields.

    - `future_requirements.alternatives.alternative_fields_due` (array of strings)
      Fields that can be provided to resolve all fields in `original_fields_due`.

    - `future_requirements.alternatives.original_fields_due` (array of strings)
      Fields that are due and can be resolved by providing all fields in `alternative_fields_due`.

  - `future_requirements.current_deadline` (timestamp, nullable)
    Date on which `future_requirements` becomes the main `requirements` hash and `future_requirements` becomes empty. After the transition, `currently_due` requirements may immediately become `past_due`, but the account may also be given a grace period depending on the capability’s enablement state prior to transitioning.

  - `future_requirements.currently_due` (array of strings)
    Fields that need to be resolved to keep the capability enabled. If not resolved by `future_requirements[current_deadline]`, these fields will transition to the main `requirements` hash.

  - `future_requirements.disabled_reason` (enum, nullable)
    This is typed as an enum for consistency with `requirements.disabled_reason`, but it safe to assume `future_requirements.disabled_reason` is null because fields in `future_requirements` will never disable the account.
Possible enum values:
    - `other`
      The capability has been disabled for another reason. Visit [Accounts to review](https://docs.stripe.com/connect/dashboard/review-actionable-accounts.md) to learn more.

    - `paused.inactivity`
      The capability has been paused for inactivity.

    - `pending.onboarding`
      The capability is pending onboarding.

    - `pending.review`
      The capability is pending review.

    - `platform_disabled`
      The capability has been disabled by the platform.

    - `platform_paused`
      The capability has been paused by the platform.

    - `rejected.inactivity`
      The capability has been rejected for inactivity. This disabled reason currently only applies to the Issuing capability. See [Issuing: Managing Inactive Connects](https://support.stripe.com/questions/issuing-managing-inactive-connect-accounts) for more details.

    - `rejected.other`
      The capability has been rejected for another reason. Visit [Accounts to review](https://docs.stripe.com/connect/dashboard/review-actionable-accounts.md) to learn more.

    - `rejected.unsupported_business`
      The account’s business is not supported by the capability. For example, payment methods may restrict the businesses they support in their terms of service, such as in [Afterpay Clearpay’s terms of service](https://docs.stripe.com/afterpay-clearpay/legal.md#restricted-businesses). If you believe that a rejection is in error, please [contact support](https://support.stripe.com/contact/) for assistance.

    - `requirements.fields_needed`
      The capability requires more information.

  - `future_requirements.errors` (array of objects)
    Details about validation and verification failures for `due` requirements that must be resolved.

    - `future_requirements.errors.code` (enum)
      The code for the type of error.
Possible enum values:
      - `information_missing`
        The requirement associated with this error is missing critical information. The associated error reason provides more details.

      - `invalid_address_city_state_postal_code`
        The combination of the city, state, and postal code in the provided address could not be validated.

      - `invalid_address_cmra_address`
        The address you provided appears to be associated with a mailbox or virtual address service, which we can’t accept. Please update your address to proceed.

      - `invalid_address_highway_contract_box`
        Invalid address. Your business address must be a valid physical address from which you conduct business and cannot be a Highway Contract Box.

      - `invalid_address_private_mailbox`
        Invalid address. Your business address must be a valid physical address from which you conduct business and cannot be a private mailbox.

      - `invalid_address_registered_agent_address`
        The address you provided appears to be associated with a registered agent, which we can’t accept. Please update your address to proceed. If you believe this is an error, you can submit a proof of address document for review.

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

      - `invalid_signator`
        We could not verify the professional certifying body of this document.

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
        The provided tax ID must have 9 digits

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
        Your website seems to be missing some required information. [Learn about the requirements](https://support.stripe.com/questions/information-required-on-your-business-website-to-use-stripe)

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

      - `unsupported_business_type`
        The business type you provided isn’t supported in this country.

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

      - `verification_failed_authorizer_authority`
        The account authorizer is not a registered authorized representative. Refer to [this support article](https://support.stripe.com/questions/representative-authority-verification) for more information.

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

      - `verification_legal_entity_structure_mismatch`
        Business type or structure seems to be incorrect. Provide the correct business type and structure for this account.

      - `verification_missing_directors`
        We identified that your business has directors that have not been added to the account. Please add missing directors to your account.

      - `verification_missing_executives`
        We have identified executives that haven’t been added on the account. Add any missing executives to the account.

      - `verification_missing_owners`
        We have identified owners that haven’t been added on the account. Add any missing owners to the account.

      - `verification_rejected_ownership_exemption_reason`
        The ownership exemption reason was rejected.

      - `verification_requires_additional_memorandum_of_associations`
        We have identified holding companies with significant percentage ownership. Upload a Memorandum of Association for each of the holding companies.

      - `verification_requires_additional_proof_of_registration`
        The uploaded document contains holding companies with significant percentage ownership. Upload a proof of registration for each of the holding companies.

      - `verification_supportability`
        We can’t accept payments for this business under the Stripe Services Agreement without additional verification, as mentioned in the [prohibited and restricted businesses list](https://stripe.com/legal/restricted-businesses).

    - `future_requirements.errors.reason` (string)
      An informative message that indicates the error type and provides additional details about the error.

    - `future_requirements.errors.requirement` (string)
      The specific user onboarding requirement field (in the requirements hash) that needs to be resolved.

  - `future_requirements.eventually_due` (array of strings)
    Fields you must collect when all thresholds are reached. As they become required, they appear in `currently_due` as well.

  - `future_requirements.past_due` (array of strings)
    Fields that haven’t been resolved by `requirements.current_deadline`. These fields need to be resolved to enable the capability on the account. `future_requirements.past_due` is a subset of `requirements.past_due`.

  - `future_requirements.pending_verification` (array of strings)
    Fields that are being reviewed, or might become required depending on the results of a review. If the review fails, these fields can move to `eventually_due`, `currently_due`, `past_due` or `alternatives`. Fields might appear in `eventually_due`, `currently_due`, `past_due` or `alternatives` and in `pending_verification` if one verification fails but another is still pending.

- `requested` (boolean)
  Whether the capability has been requested.

- `requested_at` (timestamp, nullable)
  Time at which the capability was requested. Measured in seconds since the Unix epoch.

- `requirements` (object)
  Information about the requirements for the capability, including what information needs to be collected, and by when.

  - `requirements.alternatives` (array of objects, nullable)
    Fields that are due and can be resolved by providing the corresponding alternative fields instead. Multiple alternatives can reference the same `original_fields_due`. When this happens, any of these alternatives can serve as a pathway for attempting to resolve the fields. Additionally, providing `original_fields_due` again also serves as a pathway for attempting to resolve the fields.

    - `requirements.alternatives.alternative_fields_due` (array of strings)
      Fields that can be provided to resolve all fields in `original_fields_due`.

    - `requirements.alternatives.original_fields_due` (array of strings)
      Fields that are due and can be resolved by providing all fields in `alternative_fields_due`.

  - `requirements.current_deadline` (timestamp, nullable)
    The date by which all required account information must be both submitted and verified. This includes fields listed in `currently_due` as well as those in `pending_verification`. If any required information is missing or unverified by this date, the account may be disabled. Note that `current_deadline` may change if additional `currently_due` requirements are requested.

  - `requirements.currently_due` (array of strings)
    Fields that need to be resolved to keep the capability enabled. If not resolved by `current_deadline`, these fields will appear in `past_due` as well, and the capability is disabled.

  - `requirements.disabled_reason` (enum, nullable)
    Description of why the capability is disabled. [Learn more about handling verification issues](https://docs.stripe.com/docs/connect/handling-api-verification.md).
Possible enum values:
    - `other`
      The capability has been disabled for another reason. Visit [Accounts to review](https://docs.stripe.com/connect/dashboard/review-actionable-accounts.md) to learn more.

    - `paused.inactivity`
      The capability has been paused for inactivity.

    - `pending.onboarding`
      The capability is pending onboarding.

    - `pending.review`
      The capability is pending review.

    - `platform_disabled`
      The capability has been disabled by the platform.

    - `platform_paused`
      The capability has been paused by the platform.

    - `rejected.inactivity`
      The capability has been rejected for inactivity. This disabled reason currently only applies to the Issuing capability. See [Issuing: Managing Inactive Connects](https://support.stripe.com/questions/issuing-managing-inactive-connect-accounts) for more details.

    - `rejected.other`
      The capability has been rejected for another reason. Visit [Accounts to review](https://docs.stripe.com/connect/dashboard/review-actionable-accounts.md) to learn more.

    - `rejected.unsupported_business`
      The account’s business is not supported by the capability. For example, payment methods may restrict the businesses they support in their terms of service, such as in [Afterpay Clearpay’s terms of service](https://docs.stripe.com/afterpay-clearpay/legal.md#restricted-businesses). If you believe that a rejection is in error, please [contact support](https://support.stripe.com/contact/) for assistance.

    - `requirements.fields_needed`
      The capability requires more information.

  - `requirements.errors` (array of objects)
    Details about validation and verification failures for `due` requirements that must be resolved.

    - `requirements.errors.code` (enum)
      The code for the type of error.
Possible enum values:
      - `information_missing`
        The requirement associated with this error is missing critical information. The associated error reason provides more details.

      - `invalid_address_city_state_postal_code`
        The combination of the city, state, and postal code in the provided address could not be validated.

      - `invalid_address_cmra_address`
        The address you provided appears to be associated with a mailbox or virtual address service, which we can’t accept. Please update your address to proceed.

      - `invalid_address_highway_contract_box`
        Invalid address. Your business address must be a valid physical address from which you conduct business and cannot be a Highway Contract Box.

      - `invalid_address_private_mailbox`
        Invalid address. Your business address must be a valid physical address from which you conduct business and cannot be a private mailbox.

      - `invalid_address_registered_agent_address`
        The address you provided appears to be associated with a registered agent, which we can’t accept. Please update your address to proceed. If you believe this is an error, you can submit a proof of address document for review.

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

      - `invalid_signator`
        We could not verify the professional certifying body of this document.

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
        The provided tax ID must have 9 digits

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
        Your website seems to be missing some required information. [Learn about the requirements](https://support.stripe.com/questions/information-required-on-your-business-website-to-use-stripe)

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

      - `unsupported_business_type`
        The business type you provided isn’t supported in this country.

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

      - `verification_failed_authorizer_authority`
        The account authorizer is not a registered authorized representative. Refer to [this support article](https://support.stripe.com/questions/representative-authority-verification) for more information.

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

      - `verification_legal_entity_structure_mismatch`
        Business type or structure seems to be incorrect. Provide the correct business type and structure for this account.

      - `verification_missing_directors`
        We identified that your business has directors that have not been added to the account. Please add missing directors to your account.

      - `verification_missing_executives`
        We have identified executives that haven’t been added on the account. Add any missing executives to the account.

      - `verification_missing_owners`
        We have identified owners that haven’t been added on the account. Add any missing owners to the account.

      - `verification_rejected_ownership_exemption_reason`
        The ownership exemption reason was rejected.

      - `verification_requires_additional_memorandum_of_associations`
        We have identified holding companies with significant percentage ownership. Upload a Memorandum of Association for each of the holding companies.

      - `verification_requires_additional_proof_of_registration`
        The uploaded document contains holding companies with significant percentage ownership. Upload a proof of registration for each of the holding companies.

      - `verification_supportability`
        We can’t accept payments for this business under the Stripe Services Agreement without additional verification, as mentioned in the [prohibited and restricted businesses list](https://stripe.com/legal/restricted-businesses).

    - `requirements.errors.reason` (string)
      An informative message that indicates the error type and provides additional details about the error.

    - `requirements.errors.requirement` (string)
      The specific user onboarding requirement field (in the requirements hash) that needs to be resolved.

  - `requirements.eventually_due` (array of strings)
    Fields you must collect when all thresholds are reached. As they become required, they appear in `currently_due` as well, and `current_deadline` becomes set.

  - `requirements.past_due` (array of strings)
    Fields that haven’t been resolved by `current_deadline`. These fields need to be resolved to enable the capability on the account.

  - `requirements.pending_verification` (array of strings)
    Fields that are being reviewed, or might become required depending on the results of a review. If the review fails, these fields can move to `eventually_due`, `currently_due`, `past_due` or `alternatives`. Fields might appear in `eventually_due`, `currently_due`, `past_due` or `alternatives` and in `pending_verification` if one verification fails but another is still pending.

- `status` (enum)
  The status of the capability.
Possible enum values:
  - `active`
    The capability is active.

  - `inactive`
    The capability is inactive.

  - `pending`
    The capability is inactive with requirements pending verification.

  - `unrequested`
    The capability is unrequested.

### The Capability object

```json
{
  "id": "card_payments",
  "object": "capability",
  "account": "acct_1032D82eZvKYlo2C",
  "future_requirements": {
    "alternatives": [],
    "current_deadline": null,
    "currently_due": [],
    "disabled_reason": null,
    "errors": [],
    "eventually_due": [],
    "past_due": [],
    "pending_verification": []
  },
  "requested": true,
  "requested_at": 1688491010,
  "requirements": {
    "alternatives": [],
    "current_deadline": null,
    "currently_due": [],
    "disabled_reason": null,
    "errors": [],
    "eventually_due": [],
    "past_due": [],
    "pending_verification": []
  },
  "status": "inactive"
}
```