# The Person object

## Attributes

- `id` (string)
  Unique identifier for the object.

- `object` (string)
  String representing the object’s type. Objects of the same type share the same value.

- `account` (string)
  The account the person is associated with.

- `additional_tos_acceptances` (object)
  Details on the legal guardian’s acceptance of the required Stripe service agreements.

  - `additional_tos_acceptances.account` (object, nullable)
    Details on the legal guardian’s acceptance of the main Stripe service agreement.

    - `additional_tos_acceptances.account.date` (timestamp, nullable)
      The Unix timestamp marking when the legal guardian accepted the service agreement.

    - `additional_tos_acceptances.account.ip` (string, nullable)
      The IP address from which the legal guardian accepted the service agreement.

    - `additional_tos_acceptances.account.user_agent` (string, nullable)
      The user agent of the browser from which the legal guardian accepted the service agreement.

- `address` (object, nullable)
  The person’s address.

  - `address.city` (string, nullable)
    City, district, suburb, town, or village.

  - `address.country` (string, nullable)
    Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

  - `address.line1` (string, nullable)
    Address line 1, such as the street, PO Box, or company name.

  - `address.line2` (string, nullable)
    Address line 2, such as the apartment, suite, unit, or building.

  - `address.postal_code` (string, nullable)
    ZIP or postal code.

  - `address.state` (string, nullable)
    State, county, province, or region ([ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2)).

- `address_kana` (object, nullable)
  The Kana variation of the person’s address (Japan only).

  - `address_kana.city` (string, nullable)
    City/Ward.

  - `address_kana.country` (string, nullable)
    Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

  - `address_kana.line1` (string, nullable)
    Block/Building number.

  - `address_kana.line2` (string, nullable)
    Building details.

  - `address_kana.postal_code` (string, nullable)
    ZIP or postal code.

  - `address_kana.state` (string, nullable)
    Prefecture.

  - `address_kana.town` (string, nullable)
    Town/cho-me.

- `address_kanji` (object, nullable)
  The Kanji variation of the person’s address (Japan only).

  - `address_kanji.city` (string, nullable)
    City/Ward.

  - `address_kanji.country` (string, nullable)
    Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

  - `address_kanji.line1` (string, nullable)
    Block/Building number.

  - `address_kanji.line2` (string, nullable)
    Building details.

  - `address_kanji.postal_code` (string, nullable)
    ZIP or postal code.

  - `address_kanji.state` (string, nullable)
    Prefecture.

  - `address_kanji.town` (string, nullable)
    Town/cho-me.

- `created` (timestamp)
  Time at which the object was created. Measured in seconds since the Unix epoch.

- `dob` (object, nullable)
  The person’s date of birth.

  - `dob.day` (integer, nullable)
    The day of birth, between 1 and 31.

  - `dob.month` (integer, nullable)
    The month of birth, between 1 and 12.

  - `dob.year` (integer, nullable)
    The four-digit year of birth.

- `email` (string, nullable)
  The person’s email address. Also available for accounts where [controller.requirement_collection](https://docs.stripe.com/api/accounts/object.md#account_object-controller-requirement_collection) is `stripe`.

- `first_name` (string, nullable)
  The person’s first name. Also available for accounts where [controller.requirement_collection](https://docs.stripe.com/api/accounts/object.md#account_object-controller-requirement_collection) is `stripe`.

- `first_name_kana` (string, nullable)
  The Kana variation of the person’s first name (Japan only). Also available for accounts where [controller.requirement_collection](https://docs.stripe.com/api/accounts/object.md#account_object-controller-requirement_collection) is `stripe`.

- `first_name_kanji` (string, nullable)
  The Kanji variation of the person’s first name (Japan only). Also available for accounts where [controller.requirement_collection](https://docs.stripe.com/api/accounts/object.md#account_object-controller-requirement_collection) is `stripe`.

- `full_name_aliases` (array of strings, nullable)
  A list of alternate names or aliases that the person is known by. Also available for accounts where [controller.requirement_collection](https://docs.stripe.com/api/accounts/object.md#account_object-controller-requirement_collection) is `stripe`.

- `future_requirements` (object, nullable)
  Information about the [upcoming new requirements for this person](https://docs.stripe.com/docs/connect/custom-accounts/future-requirements.md), including what information needs to be collected, and by when.

  - `future_requirements.alternatives` (array of objects, nullable)
    Fields that are due and can be resolved by providing the corresponding alternative fields instead. Many alternatives can list the same `original_fields_due`, and any of these alternatives can serve as a pathway for attempting to resolve the fields again. Re-providing `original_fields_due` also serves as a pathway for attempting to resolve the fields again.

    - `future_requirements.alternatives.alternative_fields_due` (array of strings)
      Fields that can be provided to resolve all fields in `original_fields_due`.

    - `future_requirements.alternatives.original_fields_due` (array of strings)
      Fields that are due and can be resolved by providing all fields in `alternative_fields_due`.

  - `future_requirements.currently_due` (array of strings)
    Fields that need to be resolved to keep the person’s account enabled. If not resolved by the account’s `future_requirements[current_deadline]`, these fields will transition to the main `requirements` hash, and may immediately become `past_due`, but the account may also be given a grace period depending on the account’s enablement state prior to transition.

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
    Fields you must collect when all thresholds are reached. As they become required, they appear in `currently_due` as well, and the account’s `future_requirements[current_deadline]` becomes set.

  - `future_requirements.past_due` (array of strings)
    Fields that haven’t been resolved by the account’s `requirements.current_deadline`. These fields need to be resolved to enable the person’s account. `future_requirements.past_due` is a subset of `requirements.past_due`.

  - `future_requirements.pending_verification` (array of strings)
    Fields that are being reviewed, or might become required depending on the results of a review. If the review fails, these fields can move to `eventually_due`, `currently_due`, `past_due` or `alternatives`. Fields might appear in `eventually_due`, `currently_due`, `past_due` or `alternatives` and in `pending_verification` if one verification fails but another is still pending.

- `gender` (enum, nullable)
  The person’s gender.

- `id_number_provided` (boolean)
  Whether the person’s `id_number` was provided. True if either the full ID number was provided or if only the required part of the ID number was provided (ex. last four of an individual’s SSN for the US indicated by `ssn_last_4_provided`).

- `id_number_secondary_provided` (boolean, nullable)
  Whether the person’s `id_number_secondary` was provided.

- `last_name` (string, nullable)
  The person’s last name. Also available for accounts where [controller.requirement_collection](https://docs.stripe.com/api/accounts/object.md#account_object-controller-requirement_collection) is `stripe`.

- `last_name_kana` (string, nullable)
  The Kana variation of the person’s last name (Japan only). Also available for accounts where [controller.requirement_collection](https://docs.stripe.com/api/accounts/object.md#account_object-controller-requirement_collection) is `stripe`.

- `last_name_kanji` (string, nullable)
  The Kanji variation of the person’s last name (Japan only). Also available for accounts where [controller.requirement_collection](https://docs.stripe.com/api/accounts/object.md#account_object-controller-requirement_collection) is `stripe`.

- `maiden_name` (string, nullable)
  The person’s maiden name.

- `metadata` (object)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

- `nationality` (string, nullable)
  The country where the person is a national.

- `phone` (string, nullable)
  The person’s phone number.

- `political_exposure` (enum, nullable)
  Indicates if the person or any of their representatives, family members, or other closely related persons, declares that they hold or have held an important public job or function, in any jurisdiction.
Possible enum values:
  - `existing`
    The person has disclosed that they do have political exposure

  - `none`
    The person has disclosed that they have no political exposure

- `registered_address` (object, nullable)
  The person’s registered address.

  - `registered_address.city` (string, nullable)
    City, district, suburb, town, or village.

  - `registered_address.country` (string, nullable)
    Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

  - `registered_address.line1` (string, nullable)
    Address line 1, such as the street, PO Box, or company name.

  - `registered_address.line2` (string, nullable)
    Address line 2, such as the apartment, suite, unit, or building.

  - `registered_address.postal_code` (string, nullable)
    ZIP or postal code.

  - `registered_address.state` (string, nullable)
    State, county, province, or region ([ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2)).

- `relationship` (object)
  Describes the person’s relationship to the account. Also available for accounts where [controller.requirement_collection](https://docs.stripe.com/api/accounts/object.md#account_object-controller-requirement_collection) is `stripe`.

  - `relationship.authorizer` (boolean, nullable)
    Whether the person is the authorizer of the account’s representative.

  - `relationship.director` (boolean, nullable)
    Whether the person is a director of the account’s legal entity. Directors are typically members of the governing board of the company, or responsible for ensuring the company meets its regulatory obligations.

  - `relationship.executive` (boolean, nullable)
    Whether the person has significant responsibility to control, manage, or direct the organization.

  - `relationship.legal_guardian` (boolean, nullable)
    Whether the person is the legal guardian of the account’s representative.

  - `relationship.owner` (boolean, nullable)
    Whether the person is an owner of the account’s legal entity.

  - `relationship.percent_ownership` (float, nullable)
    The percent owned by the person of the account’s legal entity.

  - `relationship.representative` (boolean, nullable)
    Whether the person is authorized as the primary representative of the account. This is the person nominated by the business to provide information about themselves, and general information about the account. There can only be one representative at any given time. At the time the account is created, this person should be set to the person responsible for opening the account.

  - `relationship.title` (string, nullable)
    The person’s title (e.g., CEO, Support Engineer).

- `requirements` (object, nullable)
  Information about the requirements for this person, including what information needs to be collected, and by when.

  - `requirements.alternatives` (array of objects, nullable)
    Fields that are due and can be resolved by providing the corresponding alternative fields instead. Many alternatives can list the same `original_fields_due`, and any of these alternatives can serve as a pathway for attempting to resolve the fields again. Re-providing `original_fields_due` also serves as a pathway for attempting to resolve the fields again.

    - `requirements.alternatives.alternative_fields_due` (array of strings)
      Fields that can be provided to resolve all fields in `original_fields_due`.

    - `requirements.alternatives.original_fields_due` (array of strings)
      Fields that are due and can be resolved by providing all fields in `alternative_fields_due`.

  - `requirements.currently_due` (array of strings)
    Fields that need to be resolved to keep the person’s account enabled. If not resolved by the account’s `current_deadline`, these fields will appear in `past_due` as well, and the account is disabled.

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
    Fields you must collect when all thresholds are reached. As they become required, they appear in `currently_due` as well, and the account’s `current_deadline` becomes set.

  - `requirements.past_due` (array of strings)
    Fields that haven’t been resolved by `current_deadline`. These fields need to be resolved to enable the person’s account.

  - `requirements.pending_verification` (array of strings)
    Fields that are being reviewed, or might become required depending on the results of a review. If the review fails, these fields can move to `eventually_due`, `currently_due`, `past_due` or `alternatives`. Fields might appear in `eventually_due`, `currently_due`, `past_due` or `alternatives` and in `pending_verification` if one verification fails but another is still pending.

- `ssn_last_4_provided` (boolean)
  Whether the last four digits of the person’s Social Security number have been provided (U.S. only).

- `us_cfpb_data` (object, nullable)
  Demographic data related to the person.

  - `us_cfpb_data.ethnicity_details` (object, nullable)
    The persons ethnicity details

    - `us_cfpb_data.ethnicity_details.ethnicity` (array of enums, nullable)
      The persons ethnicity

    - `us_cfpb_data.ethnicity_details.ethnicity_other` (string, nullable)
      Please specify your origin, when other is selected.

  - `us_cfpb_data.race_details` (object, nullable)
    The persons race details

    - `us_cfpb_data.race_details.race` (array of enums, nullable)
      The persons race.

    - `us_cfpb_data.race_details.race_other` (string, nullable)
      Please specify your race, when other is selected.

  - `us_cfpb_data.self_identified_gender` (string, nullable)
    The persons self-identified gender

- `verification` (object)
  The persons’s verification status.

  - `verification.additional_document` (object, nullable)
    A document showing address, either a passport, local ID card, or utility bill from a well-known utility company.

    - `verification.additional_document.back` (string, nullable)
      The back of an ID returned by a [file upload](https://docs.stripe.com/api/persons/object.md#create_file) with a `purpose` value of `identity_document`.

    - `verification.additional_document.details` (string, nullable)
      A user-displayable string describing the verification state of this document. For example, if a document is uploaded and the picture is too fuzzy, this may say “Identity document is too unclear to read”.

    - `verification.additional_document.details_code` (string, nullable)
      One of `document_corrupt`, `document_country_not_supported`, `document_expired`, `document_failed_copy`, `document_failed_other`, `document_failed_test_mode`, `document_fraudulent`, `document_failed_greyscale`, `document_incomplete`, `document_invalid`, `document_manipulated`, `document_missing_back`, `document_missing_front`, `document_not_readable`, `document_not_uploaded`, `document_photo_mismatch`, `document_too_large`, or `document_type_not_supported`. A machine-readable code specifying the verification state for this document.

    - `verification.additional_document.front` (string, nullable)
      The front of an ID returned by a [file upload](https://docs.stripe.com/api/persons/object.md#create_file) with a `purpose` value of `identity_document`.

  - `verification.details` (string, nullable)
    A user-displayable string describing the verification state for the person. For example, this may say “Provided identity information could not be verified”.

  - `verification.details_code` (string, nullable)
    One of `document_address_mismatch`, `document_dob_mismatch`, `document_duplicate_type`, `document_id_number_mismatch`, `document_name_mismatch`, `document_nationality_mismatch`, `failed_keyed_identity`, or `failed_other`. A machine-readable code specifying the verification state for the person.

  - `verification.document` (object)
    An identifying document for the person, either a passport or local ID card.

    - `verification.document.back` (string, nullable)
      The back of an ID returned by a [file upload](https://docs.stripe.com/api/persons/object.md#create_file) with a `purpose` value of `identity_document`.

    - `verification.document.details` (string, nullable)
      A user-displayable string describing the verification state of this document. For example, if a document is uploaded and the picture is too fuzzy, this may say “Identity document is too unclear to read”.

    - `verification.document.details_code` (string, nullable)
      One of `document_corrupt`, `document_country_not_supported`, `document_expired`, `document_failed_copy`, `document_failed_other`, `document_failed_test_mode`, `document_fraudulent`, `document_failed_greyscale`, `document_incomplete`, `document_invalid`, `document_manipulated`, `document_missing_back`, `document_missing_front`, `document_not_readable`, `document_not_uploaded`, `document_photo_mismatch`, `document_too_large`, or `document_type_not_supported`. A machine-readable code specifying the verification state for this document.

    - `verification.document.front` (string, nullable)
      The front of an ID returned by a [file upload](https://docs.stripe.com/api/persons/object.md#create_file) with a `purpose` value of `identity_document`.

  - `verification.status` (string)
    The state of verification for the person. Possible values are `unverified`, `pending`, or `verified`. Please refer [guide](https://docs.stripe.com/docs/connect/handling-api-verification.md) to handle verification updates.