# Create a person

Create a Person. Adds an individual to an Account’s identity. You can set relationship attributes and identity information at creation.

## Parameters

- `account_id` (string, required)
  Account the Person should be associated with.

- `additional_addresses` (array of objects, optional)
  Additional addresses associated with the person.

  - `additional_addresses.city` (string, optional)
    City, district, suburb, town, or village.

  - `additional_addresses.country` (enum, required)
    Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

  - `additional_addresses.line1` (string, optional)
    Address line 1 (e.g., street, PO Box, or company name).

  - `additional_addresses.line2` (string, optional)
    Address line 2 (e.g., apartment, suite, unit, or building).

  - `additional_addresses.postal_code` (string, optional)
    ZIP or postal code.

  - `additional_addresses.purpose` (enum, required)
    Purpose of additional address.
Possible enum values:
    - `registered`
      The registered address.

  - `additional_addresses.state` (string, optional)
    State, county, province, or region.

  - `additional_addresses.town` (string, optional)
    Town or district.

- `additional_names` (array of objects, optional)
  Additional names (e.g. aliases) associated with the person.

  - `additional_names.full_name` (string, optional)
    The person’s full name.

  - `additional_names.given_name` (string, optional)
    The person’s first or given name.

  - `additional_names.purpose` (enum, required)
    The purpose or type of the additional name.
Possible enum values:
    - `alias`
      An alias for the individual’s name.

    - `maiden`
      The maiden name of the individual.

  - `additional_names.surname` (string, optional)
    The person’s last or family name.

- `additional_terms_of_service` (object, optional)
  Attestations of accepted terms of service agreements.

  - `additional_terms_of_service.account` (object, optional)
    Stripe terms of service agreement.

    - `additional_terms_of_service.account.date` (timestamp, required)
      The time when the Account’s representative accepted the terms of service. Represented as a RFC 3339 date & time UTC value in millisecond precision, for example: 2022-09-18T13:22:18.123Z.

    - `additional_terms_of_service.account.ip` (string, required)
      The IP address from which the Account’s representative accepted the terms of service.

    - `additional_terms_of_service.account.user_agent` (string, optional)
      The user agent of the browser from which the Account’s representative accepted the terms of service.

- `address` (object, optional)
  The person’s residential address.

  - `address.city` (string, optional)
    City, district, suburb, town, or village.

  - `address.country` (enum, required)
    Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

  - `address.line1` (string, optional)
    Address line 1 (e.g., street, PO Box, or company name).

  - `address.line2` (string, optional)
    Address line 2 (e.g., apartment, suite, unit, or building).

  - `address.postal_code` (string, optional)
    ZIP or postal code.

  - `address.state` (string, optional)
    State, county, province, or region.

  - `address.town` (string, optional)
    Town or district.

- `date_of_birth` (object, optional)
  The person’s date of birth.

  - `date_of_birth.day` (integer, required)
    The day of birth.

  - `date_of_birth.month` (integer, required)
    The month of birth.

  - `date_of_birth.year` (integer, required)
    The year of birth.

- `documents` (object, optional)
  Documents that may be submitted to satisfy various informational requests.

  - `documents.company_authorization` (object, optional)
    One or more documents that demonstrate proof that this person is authorized to represent the company.

    - `documents.company_authorization.files` (array of strings, required)
      One or more document IDs returned by a [file upload](https://docs.stripe.com/api/persons/update.md#create_file) with a purpose value of `account_requirement`.

    - `documents.company_authorization.type` (enum, required)
      The format of the document. Currently supports `files` only.
Possible enum values:
      - `files`
        Document type with multiple files.

  - `documents.passport` (object, optional)
    One or more documents showing the person’s passport page with photo and personal data.

    - `documents.passport.files` (array of strings, required)
      One or more document IDs returned by a [file upload](https://docs.stripe.com/api/persons/update.md#create_file) with a purpose value of `account_requirement`.

    - `documents.passport.type` (enum, required)
      The format of the document. Currently supports `files` only.
Possible enum values:
      - `files`
        Document type with multiple files.

  - `documents.primary_verification` (object, optional)
    An identifying document showing the person’s name, either a passport or local ID card.

    - `documents.primary_verification.front_back` (object, required)
      The [file upload](https://docs.stripe.com/api/persons/update.md#create_file) tokens referring to each side of the document.

      - `documents.primary_verification.front_back.back` (string, optional)
        A [file upload](https://docs.stripe.com/api/persons/update.md#create_file) token representing the back of the verification document. The purpose of the uploaded file should be ‘identity_document’. The uploaded file needs to be a color image (smaller than 8,000px by 8,000px), in JPG, PNG, or PDF format, and less than 10 MB in size.

      - `documents.primary_verification.front_back.front` (string, required)
        A [file upload](https://docs.stripe.com/api/persons/update.md#create_file) token representing the front of the verification document. The purpose of the uploaded file should be ‘identity_document’. The uploaded file needs to be a color image (smaller than 8,000px by 8,000px), in JPG, PNG, or PDF format, and less than 10 MB in size.

    - `documents.primary_verification.type` (enum, required)
      The format of the verification document. Currently supports `front_back` only.
Possible enum values:
      - `front_back`
        Document type with both front and back sides.

  - `documents.secondary_verification` (object, optional)
    A document showing address, either a passport, local ID card, or utility bill from a well-known utility company.

    - `documents.secondary_verification.front_back` (object, required)
      The [file upload](https://docs.stripe.com/api/persons/update.md#create_file) tokens referring to each side of the document.

      - `documents.secondary_verification.front_back.back` (string, optional)
        A [file upload](https://docs.stripe.com/api/persons/update.md#create_file) token representing the back of the verification document. The purpose of the uploaded file should be ‘identity_document’. The uploaded file needs to be a color image (smaller than 8,000px by 8,000px), in JPG, PNG, or PDF format, and less than 10 MB in size.

      - `documents.secondary_verification.front_back.front` (string, required)
        A [file upload](https://docs.stripe.com/api/persons/update.md#create_file) token representing the front of the verification document. The purpose of the uploaded file should be ‘identity_document’. The uploaded file needs to be a color image (smaller than 8,000px by 8,000px), in JPG, PNG, or PDF format, and less than 10 MB in size.

    - `documents.secondary_verification.type` (enum, required)
      The format of the verification document. Currently supports `front_back` only.
Possible enum values:
      - `front_back`
        Document type with both front and back sides.

  - `documents.visa` (object, optional)
    One or more documents showing the person’s visa required for living in the country where they are residing.

    - `documents.visa.files` (array of strings, required)
      One or more document IDs returned by a [file upload](https://docs.stripe.com/api/persons/update.md#create_file) with a purpose value of `account_requirement`.

    - `documents.visa.type` (enum, required)
      The format of the document. Currently supports `files` only.
Possible enum values:
      - `files`
        Document type with multiple files.

- `email` (string, optional)
  Email.

- `given_name` (string, optional)
  The person’s first name.

- `id_numbers` (array of objects, optional)
  The identification numbers (e.g., SSN) associated with the person.

  - `id_numbers.type` (enum, required)
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

  - `id_numbers.value` (string, required)
    The value of the ID number.

- `legal_gender` (enum, optional)
  The person’s gender (International regulations require either “male” or “female”).
Possible enum values:
  - `female`
    Female gender person.

  - `male`
    Male gender person.

- `metadata` (map, optional)
  Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

- `nationalities` (array of enums, optional)
  The nationalities (countries) this person is associated with.

- `person_token` (string, optional)
  The person token generated by the person token api.

- `phone` (string, optional)
  The phone number for this person.

- `political_exposure` (enum, optional)
  The person’s political exposure.
Possible enum values:
  - `existing`
    The person has disclosed that they do have political exposure.

  - `none`
    The person has disclosed that they have no political exposure.

- `relationship` (object, optional)
  The relationship that this person has with the Account’s business or legal entity.

  - `relationship.authorizer` (boolean, optional)
    Whether the individual is an authorizer of the Account’s identity.

  - `relationship.director` (boolean, optional)
    Indicates whether the person is a director of the associated legal entity.

  - `relationship.executive` (boolean, optional)
    Indicates whether the person is an executive of the associated legal entity.

  - `relationship.legal_guardian` (boolean, optional)
    Indicates whether the person is a legal guardian of the associated legal entity.

  - `relationship.owner` (boolean, optional)
    Indicates whether the person is an owner of the associated legal entity.

  - `relationship.percent_ownership` (decimal, optional)
    The percentage of ownership the person has in the associated legal entity.

  - `relationship.representative` (boolean, optional)
    Indicates whether the person is a representative of the associated legal entity.

  - `relationship.title` (string, optional)
    The title or position the person holds in the associated legal entity.

- `script_addresses` (object, optional)
  The script addresses (e.g., non-Latin characters) associated with the person.

  - `script_addresses.kana` (object, optional)
    Kana Address.

    - `script_addresses.kana.city` (string, optional)
      City, district, suburb, town, or village.

    - `script_addresses.kana.country` (enum, required)
      Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

    - `script_addresses.kana.line1` (string, optional)
      Address line 1 (e.g., street, PO Box, or company name).

    - `script_addresses.kana.line2` (string, optional)
      Address line 2 (e.g., apartment, suite, unit, or building).

    - `script_addresses.kana.postal_code` (string, optional)
      ZIP or postal code.

    - `script_addresses.kana.state` (string, optional)
      State, county, province, or region.

    - `script_addresses.kana.town` (string, optional)
      Town or district.

  - `script_addresses.kanji` (object, optional)
    Kanji Address.

    - `script_addresses.kanji.city` (string, optional)
      City, district, suburb, town, or village.

    - `script_addresses.kanji.country` (enum, required)
      Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

    - `script_addresses.kanji.line1` (string, optional)
      Address line 1 (e.g., street, PO Box, or company name).

    - `script_addresses.kanji.line2` (string, optional)
      Address line 2 (e.g., apartment, suite, unit, or building).

    - `script_addresses.kanji.postal_code` (string, optional)
      ZIP or postal code.

    - `script_addresses.kanji.state` (string, optional)
      State, county, province, or region.

    - `script_addresses.kanji.town` (string, optional)
      Town or district.

- `script_names` (object, optional)
  The script names (e.g. non-Latin characters) associated with the person.

  - `script_names.kana` (object, optional)
    Persons name in kana script.

    - `script_names.kana.given_name` (string, optional)
      The person’s first or given name.

    - `script_names.kana.surname` (string, optional)
      The person’s last or family name.

  - `script_names.kanji` (object, optional)
    Persons name in kanji script.

    - `script_names.kanji.given_name` (string, optional)
      The person’s first or given name.

    - `script_names.kanji.surname` (string, optional)
      The person’s last or family name.

- `surname` (string, optional)
  The person’s last name.

## Returns

## Response attributes

- `id` (string)
  Unique identifier for the Person.

- `object` (string, value is "v2.core.account_person")
  String representing the object’s type. Objects of the same type share the same value of the object field.

- `account` (string)
  The account ID which the individual belongs to.

- `additional_addresses` (array of objects, nullable)
  Additional addresses associated with the person.

  - `additional_addresses.city` (string, nullable)
    City, district, suburb, town, or village.

  - `additional_addresses.country` (enum, nullable)
    Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

  - `additional_addresses.line1` (string, nullable)
    Address line 1 (e.g., street, PO Box, or company name).

  - `additional_addresses.line2` (string, nullable)
    Address line 2 (e.g., apartment, suite, unit, or building).

  - `additional_addresses.postal_code` (string, nullable)
    ZIP or postal code.

  - `additional_addresses.purpose` (enum)
    Purpose of additional address.
Possible enum values:
    - `registered`
      The registered address.

  - `additional_addresses.state` (string, nullable)
    State, county, province, or region.

  - `additional_addresses.town` (string, nullable)
    Town or district.

- `additional_names` (array of objects, nullable)
  Additional names (e.g. aliases) associated with the person.

  - `additional_names.full_name` (string, nullable)
    The individual’s full name.

  - `additional_names.given_name` (string, nullable)
    The individual’s first or given name.

  - `additional_names.purpose` (enum)
    The purpose or type of the additional name.
Possible enum values:
    - `alias`
      An alias for the individual’s name.

    - `maiden`
      The maiden name of the individual.

  - `additional_names.surname` (string, nullable)
    The individual’s last or family name.

- `additional_terms_of_service` (object, nullable)
  Attestations of accepted terms of service agreements.

  - `additional_terms_of_service.account` (object, nullable)
    Stripe terms of service agreement.

    - `additional_terms_of_service.account.date` (timestamp, nullable)
      The time when the Account’s representative accepted the terms of service. Represented as a RFC 3339 date & time UTC value in millisecond precision, for example: 2022-09-18T13:22:18.123Z.

    - `additional_terms_of_service.account.ip` (string, nullable)
      The IP address from which the Account’s representative accepted the terms of service.

    - `additional_terms_of_service.account.user_agent` (string, nullable)
      The user agent of the browser from which the Account’s representative accepted the terms of service.

- `address` (object, nullable)
  The person’s residential address.

  - `address.city` (string, nullable)
    City, district, suburb, town, or village.

  - `address.country` (enum, nullable)
    Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

  - `address.line1` (string, nullable)
    Address line 1 (e.g., street, PO Box, or company name).

  - `address.line2` (string, nullable)
    Address line 2 (e.g., apartment, suite, unit, or building).

  - `address.postal_code` (string, nullable)
    ZIP or postal code.

  - `address.state` (string, nullable)
    State, county, province, or region.

  - `address.town` (string, nullable)
    Town or district.

- `created` (timestamp)
  Time at which the object was created. Represented as a RFC 3339 date & time UTC value in millisecond precision, for example: 2022-09-18T13:22:18.123Z.

- `date_of_birth` (object, nullable)
  The person’s date of birth.

  - `date_of_birth.day` (integer)
    The day of birth, between 1 and 31.

  - `date_of_birth.month` (integer)
    The month of birth, between 1 and 12.

  - `date_of_birth.year` (integer)
    The four-digit year of birth.

- `documents` (object, nullable)
  Documents that may be submitted to satisfy various informational requests.

  - `documents.company_authorization` (object, nullable)
    One or more documents that demonstrate proof that this person is authorized to represent the company.

    - `documents.company_authorization.files` (array of strings)
      One or more document IDs returned by a [file upload](https://docs.stripe.com/api/persons/update.md#create_file) with a purpose value of `account_requirement`.

    - `documents.company_authorization.type` (enum)
      The format of the document. Currently supports `files` only.
Possible enum values:
      - `files`
        Document type with multiple files.

  - `documents.passport` (object, nullable)
    One or more documents showing the person’s passport page with photo and personal data.

    - `documents.passport.files` (array of strings)
      One or more document IDs returned by a [file upload](https://docs.stripe.com/api/persons/update.md#create_file) with a purpose value of `account_requirement`.

    - `documents.passport.type` (enum)
      The format of the document. Currently supports `files` only.
Possible enum values:
      - `files`
        Document type with multiple files.

  - `documents.primary_verification` (object, nullable)
    An identifying document showing the person’s name, either a passport or local ID card.

    - `documents.primary_verification.front_back` (object)
      The [file upload](https://docs.stripe.com/api/persons/update.md#create_file) tokens for the front and back of the verification document.

      - `documents.primary_verification.front_back.back` (string, nullable)
        A [file upload](https://docs.stripe.com/api/persons/update.md#create_file) token representing the back of the verification document. The purpose of the uploaded file should be ‘identity_document’. The uploaded file needs to be a color image (smaller than 8,000px by 8,000px), in JPG, PNG, or PDF format, and less than 10 MB in size.

      - `documents.primary_verification.front_back.front` (string)
        A [file upload](https://docs.stripe.com/api/persons/update.md#create_file) token representing the front of the verification document. The purpose of the uploaded file should be ‘identity_document’. The uploaded file needs to be a color image (smaller than 8,000px by 8,000px), in JPG, PNG, or PDF format, and less than 10 MB in size.

    - `documents.primary_verification.type` (enum)
      The format of the verification document. Currently supports `front_back` only.
Possible enum values:
      - `front_back`
        Document type with both front and back sides.

  - `documents.secondary_verification` (object, nullable)
    A document showing address, either a passport, local ID card, or utility bill from a well-known utility company.

    - `documents.secondary_verification.front_back` (object)
      The [file upload](https://docs.stripe.com/api/persons/update.md#create_file) tokens for the front and back of the verification document.

      - `documents.secondary_verification.front_back.back` (string, nullable)
        A [file upload](https://docs.stripe.com/api/persons/update.md#create_file) token representing the back of the verification document. The purpose of the uploaded file should be ‘identity_document’. The uploaded file needs to be a color image (smaller than 8,000px by 8,000px), in JPG, PNG, or PDF format, and less than 10 MB in size.

      - `documents.secondary_verification.front_back.front` (string)
        A [file upload](https://docs.stripe.com/api/persons/update.md#create_file) token representing the front of the verification document. The purpose of the uploaded file should be ‘identity_document’. The uploaded file needs to be a color image (smaller than 8,000px by 8,000px), in JPG, PNG, or PDF format, and less than 10 MB in size.

    - `documents.secondary_verification.type` (enum)
      The format of the verification document. Currently supports `front_back` only.
Possible enum values:
      - `front_back`
        Document type with both front and back sides.

  - `documents.visa` (object, nullable)
    One or more documents showing the person’s visa required for living in the country where they are residing.

    - `documents.visa.files` (array of strings)
      One or more document IDs returned by a [file upload](https://docs.stripe.com/api/persons/update.md#create_file) with a purpose value of `account_requirement`.

    - `documents.visa.type` (enum)
      The format of the document. Currently supports `files` only.
Possible enum values:
      - `files`
        Document type with multiple files.

- `email` (string, nullable)
  The person’s email address.

- `given_name` (string, nullable)
  The person’s first name.

- `id_numbers` (array of objects, nullable)
  The identification numbers (e.g., SSN) associated with the person.

  - `id_numbers.type` (enum)
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

- `legal_gender` (enum, nullable)
  The person’s gender (International regulations require either “male” or “female”).
Possible enum values:
  - `female`
    Female gender person.

  - `male`
    Male gender person.

- `livemode` (boolean)
  Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.

- `metadata` (map, nullable)
  Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

- `nationalities` (array of enums, nullable)
  The countries where the person is a national. Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

- `phone` (string, nullable)
  The person’s phone number.

- `political_exposure` (enum, nullable)
  The person’s political exposure.
Possible enum values:
  - `existing`
    The person has disclosed that they do have political exposure.

  - `none`
    The person has disclosed that they have no political exposure.

- `relationship` (object, nullable)
  The relationship that this person has with the Account’s business or legal entity.

  - `relationship.authorizer` (boolean, nullable)
    Whether the individual is an authorizer of the Account’s identity.

  - `relationship.director` (boolean, nullable)
    Whether the individual is a director of the Account’s identity. Directors are typically members of the governing board of the company or are responsible for making sure that the company meets its regulatory obligations.

  - `relationship.executive` (boolean, nullable)
    Whether the individual has significant responsibility to control, manage, or direct the organization.

  - `relationship.legal_guardian` (boolean, nullable)
    Whether the individual is the legal guardian of the Account’s representative.

  - `relationship.owner` (boolean, nullable)
    Whether the individual is an owner of the Account’s identity.

  - `relationship.percent_ownership` (decimal, nullable)
    The percentage of the Account’s identity that the individual owns.

  - `relationship.representative` (boolean, nullable)
    Whether the individual is authorized as the primary representative of the Account. This is the person nominated by the business to provide information about themselves, and general information about the account. There can only be one representative at any given time. At the time the account is created, this person should be set to the person responsible for opening the account.

  - `relationship.title` (string, nullable)
    The individual’s title (e.g., CEO, Support Engineer).

- `script_addresses` (object, nullable)
  The script addresses (e.g., non-Latin characters) associated with the person.

  - `script_addresses.kana` (object, nullable)
    Kana Address.

    - `script_addresses.kana.city` (string, nullable)
      City, district, suburb, town, or village.

    - `script_addresses.kana.country` (enum, nullable)
      Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

    - `script_addresses.kana.line1` (string, nullable)
      Address line 1 (e.g., street, PO Box, or company name).

    - `script_addresses.kana.line2` (string, nullable)
      Address line 2 (e.g., apartment, suite, unit, or building).

    - `script_addresses.kana.postal_code` (string, nullable)
      ZIP or postal code.

    - `script_addresses.kana.state` (string, nullable)
      State, county, province, or region.

    - `script_addresses.kana.town` (string, nullable)
      Town or district.

  - `script_addresses.kanji` (object, nullable)
    Kanji Address.

    - `script_addresses.kanji.city` (string, nullable)
      City, district, suburb, town, or village.

    - `script_addresses.kanji.country` (enum, nullable)
      Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

    - `script_addresses.kanji.line1` (string, nullable)
      Address line 1 (e.g., street, PO Box, or company name).

    - `script_addresses.kanji.line2` (string, nullable)
      Address line 2 (e.g., apartment, suite, unit, or building).

    - `script_addresses.kanji.postal_code` (string, nullable)
      ZIP or postal code.

    - `script_addresses.kanji.state` (string, nullable)
      State, county, province, or region.

    - `script_addresses.kanji.town` (string, nullable)
      Town or district.

- `script_names` (object, nullable)
  The script names (e.g. non-Latin characters) associated with the person.

  - `script_names.kana` (object, nullable)
    Persons name in kana script.

    - `script_names.kana.given_name` (string, nullable)
      The person’s first or given name.

    - `script_names.kana.surname` (string, nullable)
      The person’s last or family name.

  - `script_names.kanji` (object, nullable)
    Persons name in kanji script.

    - `script_names.kanji.given_name` (string, nullable)
      The person’s first or given name.

    - `script_names.kanji.surname` (string, nullable)
      The person’s last or family name.

- `surname` (string, nullable)
  The person’s last name.

- `updated` (timestamp)
  Time at which the object was last updated. Represented as a RFC 3339 date & time UTC value in millisecond precision, for example: 2022-09-18T13:22:18.123Z.

## Error Codes

| HTTP status code | Code                                                         | Description                                                                                           |
| ---------------- | ------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------- |
| 400              | account_not_yet_compatible_with_v2                           | Account is not yet compatible with V2 APIs.                                                           |
| 400              | accounts_v2_access_blocked                                   | Accounts v2 is not enabled for your platform.                                                         |
| 400              | additional_legal_guardian_not_allowed                        | More than one legal guardian is added to an account.                                                  |
| 400              | additional_representative_not_allowed                        | More than one representative is added to an account.                                                  |
| 400              | additional_tos_only_allowed_for_legal_guardian               | Additional terms of service are signed by someone other than the legal guardian.                      |
| 400              | address_characters_invalid                                   | Invalid characters are provided for address fields.                                                   |
| 400              | address_country_identity_country_mismatch                    | Address country doesn’t match identity country.                                                       |
| 400              | address_country_mismatch                                     | Registered/script address country doesn’t match residential address country.                          |
| 400              | address_country_required                                     | Address country is required but not provided.                                                         |
| 400              | address_postal_code_invalid                                  | Address postal code is invalid.                                                                       |
| 400              | address_state_invalid                                        | Address state is invalid.                                                                             |
| 400              | address_town_invalid                                         | Address town is invalid.                                                                              |
| 400              | authorizer_duplicate                                         | There can only be one authorizer.                                                                     |
| 400              | authorizer_relationship_invalid_for_representative           | An authorizer cannot be a representative.                                                             |
| 400              | date_of_birth_age_restriction                                | Representative date of birth does not meet the age limit.                                             |
| 400              | date_of_birth_invalid                                        | Representative date of birth is provided an invalid date or a future date.                            |
| 400              | document_invalid                                             | Provided file tokens for documents are invalid, not found, deleted, or belong to a different account. |
| 400              | document_purpose_invalid                                     | Provided file tokens for documents are of the wrong purpose.                                          |
| 400              | duplicate_person_not_allowed                                 | Duplicate person is added to an account.                                                              |
| 400              | email_domain_invalid_for_recipient                           | Email contains unsupported domain.                                                                    |
| 400              | email_invalid                                                | Incorrect email is provided.                                                                          |
| 400              | id_number_invalid                                            | Provided ID number is of the wrong format for the given type.                                         |
| 400              | identity_country_required                                    | The `identity.country` value is required but not provided.                                            |
| 400              | incorrect_account_for_person_token                           | A person token is created with one account but used on a different account.                           |
| 400              | incorrect_id_number_for_country                              | Incorrect ID number is provided for a country.                                                        |
| 400              | incorrect_token_wrong_type                                   | The incorrect token type is provided .                                                                |
| 400              | individual_additional_person_not_allowed                     | Additional person is added for an individual business type.                                           |
| 400              | invalid_relationship_for_identity_type_structure_and_country | Some relationships are specific to type, structure, and country.                                      |
| 400              | ip_address_invalid                                           | Invalid IP address is provided.                                                                       |
| 400              | legal_guardian_representative_not_allowed                    | Person is designated as both legal guardian and representative.                                       |
| 400              | legal_guardian_requires_existing_representative              | A legal guardian may not be added to the account without an existing representative.                  |
| 400              | non_jp_kana_kanji_address                                    | Kana Kanji script addresses must have JP country.                                                     |
| 400              | param_alongside_person_token                                 | Parameter cannot be passed alongside person_token.                                                    |
| 400              | person_percent_ownership_invalid                             | Error returned when relationship.owner is set to true but the ownership percentage is set to 0%.      |
| 400              | person_token_required                                        | Person token required for platforms in mandated countries (e.g., France).                             |
| 400              | phone_invalid                                                | Phone number is invalid.                                                                              |
| 400              | postal_code_required_for_jp_address                          | Postal code is required for Japanese addresses.                                                       |
| 400              | script_characters_invalid                                    | Provided script characters are invalid for the script.                                                |
| 400              | token_already_used                                           | The token is re-used with a different idempotency key.                                                |
| 400              | token_expired                                                | Token has expired.                                                                                    |
| 400              | total_person_ownership_exceeded                              | Total ownership percentages of all Persons on the account exceeds 100%.                               |
| 400              | unsupported_postal_code                                      | Address is in an unsupported postal code.                                                             |
| 400              | unsupported_state                                            | Address is in an unsupported state.                                                                   |
| 400              | v1_account_instead_of_v2_account                             | V1 Account ID cannot be used in V2 Account APIs.                                                      |
| 400              | v1_customer_instead_of_v2_account                            | V1 Customer ID cannot be used in V2 Account APIs.                                                     |
| 400              | v1_token_invalid_in_v2                                       | A v1 token ID is passed in v2 APIs.                                                                   |
| 403              | invalid_person_token                                         | Invalid person token.                                                                                 |

```curl
curl -X POST https://api.stripe.com/v2/core/accounts/acct_1Nv0FGQ9RKHgCVdK/persons \
  -H "Authorization: Bearer <<YOUR_SECRET_KEY>>" \
  -H "Stripe-Version: {{STRIPE_API_VERSION}}" \
  --json '{
    "given_name": "Jenny",
    "surname": "Rosen",
    "email": "jenny.rosen@example.com",
    "address": {
        "line1": "27 Fredrick Ave",
        "city": "Brothers",
        "postal_code": "97712",
        "state": "OR",
        "country": "us"
    },
    "id_numbers": [
        {
            "type": "us_ssn_last_4",
            "value": "0000"
        }
    ],
    "relationship": {
        "owner": true,
        "percent_ownership": "0.8",
        "representative": true,
        "title": "CEO"
    }
  }'
```

```cli
stripe v2 core accounts persons create acct_1Nv0FGQ9RKHgCVdK \
  --given-name=Jenny \
  --surname=Rosen \
  --email="jenny.rosen@example.com" \
  --address.line1="27 Fredrick Ave" \
  --address.city=Brothers \
  --address.postal-code=97712 \
  --address.state=OR \
  --address.country=us \
  --id-numbers.type=us_ssn_last_4 \
  --id-numbers.value=0000 \
  --relationship.owner=true \
  --relationship.percent-ownership="0.8" \
  --relationship.representative=true \
  --relationship.title=CEO
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

account_person = client.v2.core.accounts.persons.create(
  'acct_1Nv0FGQ9RKHgCVdK',
  {
    given_name: 'Jenny',
    surname: 'Rosen',
    email: 'jenny.rosen@example.com',
    address: {
      line1: '27 Fredrick Ave',
      city: 'Brothers',
      postal_code: '97712',
      state: 'OR',
      country: 'us',
    },
    id_numbers: [
      {
        type: 'us_ssn_last_4',
        value: '0000',
      },
    ],
    relationship: {
      owner: true,
      percent_ownership: '0.8',
      representative: true,
      title: 'CEO',
    },
  },
)
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

account_person = client.v2.core.accounts.persons.create(
  "acct_1Nv0FGQ9RKHgCVdK",
  {
    "given_name": "Jenny",
    "surname": "Rosen",
    "email": "jenny.rosen@example.com",
    "address": {
      "line1": "27 Fredrick Ave",
      "city": "Brothers",
      "postal_code": "97712",
      "state": "OR",
      "country": "us",
    },
    "id_numbers": [{"type": "us_ssn_last_4", "value": "0000"}],
    "relationship": {
      "owner": True,
      "percent_ownership": "0.8",
      "representative": True,
      "title": "CEO",
    },
  },
)
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$accountPerson = $stripe->v2->core->accounts->persons->create(
  'acct_1Nv0FGQ9RKHgCVdK',
  [
    'given_name' => 'Jenny',
    'surname' => 'Rosen',
    'email' => 'jenny.rosen@example.com',
    'address' => [
      'line1' => '27 Fredrick Ave',
      'city' => 'Brothers',
      'postal_code' => '97712',
      'state' => 'OR',
      'country' => 'us',
    ],
    'id_numbers' => [
      [
        'type' => 'us_ssn_last_4',
        'value' => '0000',
      ],
    ],
    'relationship' => [
      'owner' => true,
      'percent_ownership' => '0.8',
      'representative' => true,
      'title' => 'CEO',
    ],
  ]
);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

PersonCreateParams params =
  PersonCreateParams.builder()
    .setGivenName("Jenny")
    .setSurname("Rosen")
    .setEmail("jenny.rosen@example.com")
    .setAddress(
      PersonCreateParams.Address.builder()
        .setLine1("27 Fredrick Ave")
        .setCity("Brothers")
        .setPostalCode("97712")
        .setState("OR")
        .setCountry("us")
        .build()
    )
    .addIdNumber(
      PersonCreateParams.IdNumber.builder()
        .setType(PersonCreateParams.IdNumber.Type.US_SSN_LAST_4)
        .setValue("0000")
        .build()
    )
    .setRelationship(
      PersonCreateParams.Relationship.builder()
        .setOwner(true)
        .setPercentOwnership("0.8")
        .setRepresentative(true)
        .setTitle("CEO")
        .build()
    )
    .build();

AccountPerson accountPerson =
  client.v2().core().accounts().persons().create("acct_1Nv0FGQ9RKHgCVdK", params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const accountPerson = await stripe.v2.core.accounts.persons.create(
  'acct_1Nv0FGQ9RKHgCVdK',
  {
    given_name: 'Jenny',
    surname: 'Rosen',
    email: 'jenny.rosen@example.com',
    address: {
      line1: '27 Fredrick Ave',
      city: 'Brothers',
      postal_code: '97712',
      state: 'OR',
      country: 'us',
    },
    id_numbers: [
      {
        type: 'us_ssn_last_4',
        value: '0000',
      },
    ],
    relationship: {
      owner: true,
      percent_ownership: '0.8',
      representative: true,
      title: 'CEO',
    },
  }
);
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.V2CoreAccountsPersonCreateParams{
  GivenName: stripe.String("Jenny"),
  Surname: stripe.String("Rosen"),
  Email: stripe.String("jenny.rosen@example.com"),
  Address: &stripe.V2CoreAccountsPersonCreateAddressParams{
    Line1: stripe.String("27 Fredrick Ave"),
    City: stripe.String("Brothers"),
    PostalCode: stripe.String("97712"),
    State: stripe.String("OR"),
    Country: stripe.String("us"),
  },
  IDNumbers: []*stripe.V2CoreAccountsPersonCreateIDNumberParams{
    &stripe.V2CoreAccountsPersonCreateIDNumberParams{
      Type: stripe.String("us_ssn_last_4"),
      Value: stripe.String("0000"),
    },
  },
  Relationship: &stripe.PersonRelationshipParams{
    Owner: stripe.Bool(true),
    PercentOwnership: stripe.String("0.8"),
    Representative: stripe.Bool(true),
    Title: stripe.String("CEO"),
  },
  AccountID: stripe.String("acct_1Nv0FGQ9RKHgCVdK"),
}
result, err := sc.V2CoreAccountsPersons.Create(context.TODO(), params)
```

```dotnet
var options = new Stripe.V2.Core.Accounts.PersonCreateOptions
{
    GivenName = "Jenny",
    Surname = "Rosen",
    Email = "jenny.rosen@example.com",
    Address = new AddressJapanOptions
    {
        Line1 = "27 Fredrick Ave",
        City = "Brothers",
        PostalCode = "97712",
        State = "OR",
        Country = "us",
    },
    IdNumbers = new List<Stripe.V2.Core.Accounts.PersonCreateIdNumberOptions>
    {
        new Stripe.V2.Core.Accounts.PersonCreateIdNumberOptions
        {
            Type = "us_ssn_last_4",
            Value = "0000",
        },
    },
    Relationship = new Stripe.V2.Core.Accounts.PersonCreateRelationshipOptions
    {
        Owner = true,
        PercentOwnership = "0.8",
        Representative = true,
        Title = "CEO",
    },
};
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V2.Core.Accounts.Persons;
Stripe.V2.Core.AccountPerson accountPerson = service.Create(
    "acct_1Nv0FGQ9RKHgCVdK",
    options);
```

### Response

```json
{
  "id": "person_test_61RS0CgWt1xBt8M1Q16RS0Cg0WSQO5ZXUVpZxZ9tAIbY",
  "object": "v2.core.account_person",
  "account": "acct_1Nv0FGQ9RKHgCVdK",
  "additional_addresses": [],
  "additional_names": [],
  "address": {
    "city": "Brothers",
    "country": "us",
    "line1": "27 Fredrick Ave",
    "postal_code": "97712",
    "state": "OR"
  },
  "created": "2024-11-26T17:10:07.000Z",
  "email": "jenny.rosen@example.com",
  "given_name": "Jenny",
  "id_numbers": [
    {
      "type": "us_ssn_last_4"
    }
  ],
  "livemode": true,
  "metadata": {},
  "nationalities": [],
  "relationship": {
    "owner": true,
    "percent_ownership": "0.8",
    "representative": true,
    "title": "CEO"
  },
  "surname": "Rosen",
  "updated": "2024-11-26T17:10:07.000Z"
}
```