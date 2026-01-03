# The External Bank Account object

## Attributes

- `id` (string)
  Unique identifier for the object.

- `object` (string)
  String representing the object’s type. Objects of the same type share the same value.

- `account` (string, nullable)
  The account this bank account belongs to. Only applicable on Accounts (not customers or recipients) This property is only available when returned as an [External Account](https://docs.stripe.com/api/external_account_bank_accounts/object.md) where [controller.is_controller](https://docs.stripe.com/api/accounts/object.md#account_object-controller-is_controller) is `true`.

- `account_holder_name` (string, nullable)
  The name of the person or business that owns the bank account.

- `account_holder_type` (string, nullable)
  The type of entity that holds the account. This can be either `individual` or `company`.

- `account_type` (string, nullable)
  The bank account type. This can only be `checking` or `savings` in most countries. In Japan, this can only be `futsu` or `toza`.

- `available_payout_methods` (array of enums, nullable)
  A set of available payout methods for this bank account. Only values from this set should be passed as the `method` when creating a payout.
Possible enum values:
  - `instant`
  - `standard`

- `bank_name` (string, nullable)
  Name of the bank associated with the routing number (e.g., `WELLS FARGO`).

- `country` (string)
  Two-letter ISO code representing the country the bank account is located in.

- `currency` (enum)
  Three-letter [ISO code for the currency](https://stripe.com/docs/payouts) paid out to the bank account.

- `customer` (string, nullable)
  The ID of the customer that the bank account is associated with.

- `default_for_currency` (boolean, nullable)
  Whether this bank account is the default external account for its currency.

- `fingerprint` (string, nullable)
  Uniquely identifies this particular bank account. You can use this attribute to check whether two bank accounts are the same.

- `future_requirements` (object, nullable)
  Information about the [upcoming new requirements for the bank account](https://docs.stripe.com/docs/connect/custom-accounts/future-requirements.md), including what information needs to be collected, and by when.

  - `future_requirements.currently_due` (array of strings, nullable)
    Fields that need to be resolved to keep the external account enabled. If not resolved by `current_deadline`, these fields will appear in `past_due` as well, and the account is disabled.

  - `future_requirements.errors` (array of objects, nullable)
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

  - `future_requirements.past_due` (array of strings, nullable)
    Fields that haven’t been resolved by `current_deadline`. These fields need to be resolved to enable the external account.

  - `future_requirements.pending_verification` (array of strings, nullable)
    Fields that are being reviewed, or might become required depending on the results of a review. If the review fails, these fields can move to `eventually_due`, `currently_due`, `past_due` or `alternatives`. Fields might appear in `eventually_due`, `currently_due`, `past_due` or `alternatives` and in `pending_verification` if one verification fails but another is still pending.

- `last4` (string)
  The last four digits of the bank account number.

- `metadata` (object, nullable)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

- `requirements` (object, nullable)
  Information about the requirements for the bank account, including what information needs to be collected.

  - `requirements.currently_due` (array of strings, nullable)
    Fields that need to be resolved to keep the external account enabled. If not resolved by `current_deadline`, these fields will appear in `past_due` as well, and the account is disabled.

  - `requirements.errors` (array of objects, nullable)
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

  - `requirements.past_due` (array of strings, nullable)
    Fields that haven’t been resolved by `current_deadline`. These fields need to be resolved to enable the external account.

  - `requirements.pending_verification` (array of strings, nullable)
    Fields that are being reviewed, or might become required depending on the results of a review. If the review fails, these fields can move to `eventually_due`, `currently_due`, `past_due` or `alternatives`. Fields might appear in `eventually_due`, `currently_due`, `past_due` or `alternatives` and in `pending_verification` if one verification fails but another is still pending.

- `routing_number` (string, nullable)
  The routing transit number for the bank account.

- `status` (string)
  For bank accounts, possible values are `new`, `validated`, `verified`, `verification_failed`, `tokenized_account_number_deactivated` or `errored`. A bank account that hasn’t had any activity or validation performed is `new`. If Stripe can determine that the bank account exists, its status will be `validated`. Note that there often isn’t enough information to know (e.g., for smaller credit unions), and the validation is not always run. If customer bank account verification has succeeded, the bank account status will be `verified`. If the verification failed for any reason, such as microdeposit failure, the status will be `verification_failed`. If the status is `tokenized_account_number_deactivated`, the account utilizes a tokenized account number which has been deactivated due to expiration or revocation. This account will need to be reverified to continue using it for money movement. If a payout sent to this bank account fails, we’ll set the status to `errored` and will not continue to send [scheduled payouts](https://stripe.com/docs/payouts#payout-schedule) until the bank details are updated.

  For external accounts, possible values are `new`, `errored`, `verification_failed`, and `tokenized_account_number_deactivated`. If a payout fails, the status is set to `errored` and scheduled payouts are stopped until account details are updated. In the US and India, if we can’t [verify the owner of the bank account](https://support.stripe.com/questions/bank-account-ownership-verification), we’ll set the status to `verification_failed`. Other validations aren’t run against external accounts because they’re only used for payouts. This means the other statuses don’t apply.

### The External Bank Account object

```json
{
  "id": "ba_1N9DrD2eZvKYlo2C58f4DaIa",
  "object": "bank_account",
  "account": "acct_1032D82eZvKYlo2C",
  "account_holder_name": "Jane Austen",
  "account_holder_type": "individual",
  "account_type": null,
  "available_payout_methods": [
    "standard"
  ],
  "bank_name": "STRIPE TEST BANK",
  "country": "US",
  "currency": "usd",
  "fingerprint": "1JWtPxqbdX5Gamtz",
  "last4": "6789",
  "metadata": {},
  "routing_number": "110000000",
  "status": "new"
}
```