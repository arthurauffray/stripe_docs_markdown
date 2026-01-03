# Retrieve a person

Retrieves a Person associated with an Account.

## Parameters

- `account_id` (string, required)
  The Account the Person is associated with.

- `id` (string, required)
  The ID of the Person to retrieve.

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

| HTTP status code | Code                               | Description                                       |
| ---------------- | ---------------------------------- | ------------------------------------------------- |
| 400              | account_not_yet_compatible_with_v2 | Account is not yet compatible with V2 APIs.       |
| 400              | accounts_v2_access_blocked         | Accounts v2 is not enabled for your platform.     |
| 400              | v1_account_instead_of_v2_account   | V1 Account ID cannot be used in V2 Account APIs.  |
| 400              | v1_customer_instead_of_v2_account  | V1 Customer ID cannot be used in V2 Account APIs. |
| 404              | not_found                          | The resource wasn’t found.                        |

```curl
curl https://api.stripe.com/v2/core/accounts/acct_1Nv0FGQ9RKHgCVdK/persons/person_test_61RS0CgWt1xBt8M1Q16RS0Cg0WSQO5ZXUVpZxZ9tAIbY \
  -H "Authorization: Bearer <<YOUR_SECRET_KEY>>" \
  -H "Stripe-Version: {{STRIPE_API_VERSION}}"
```

```cli
stripe v2 core accounts persons retrieve acct_1Nv0FGQ9RKHgCVdK person_test_61RS0CgWt1xBt8M1Q16RS0Cg0WSQO5ZXUVpZxZ9tAIbY
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

account_person = client.v2.core.accounts.persons.retrieve(
  'acct_1Nv0FGQ9RKHgCVdK',
  'person_test_61RS0CgWt1xBt8M1Q16RS0Cg0WSQO5ZXUVpZxZ9tAIbY',
)
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

account_person = client.v2.core.accounts.persons.retrieve(
  "acct_1Nv0FGQ9RKHgCVdK",
  "person_test_61RS0CgWt1xBt8M1Q16RS0Cg0WSQO5ZXUVpZxZ9tAIbY",
)
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$accountPerson = $stripe->v2->core->accounts->persons->retrieve(
  'acct_1Nv0FGQ9RKHgCVdK',
  'person_test_61RS0CgWt1xBt8M1Q16RS0Cg0WSQO5ZXUVpZxZ9tAIbY',
  []
);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

AccountPerson accountPerson =
  client.v2().core().accounts().persons().retrieve(
    "acct_1Nv0FGQ9RKHgCVdK",
    "person_test_61RS0CgWt1xBt8M1Q16RS0Cg0WSQO5ZXUVpZxZ9tAIbY"
  );
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const accountPerson = await stripe.v2.core.accounts.persons.retrieve(
  'acct_1Nv0FGQ9RKHgCVdK',
  'person_test_61RS0CgWt1xBt8M1Q16RS0Cg0WSQO5ZXUVpZxZ9tAIbY'
);
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.V2CoreAccountsPersonRetrieveParams{
  AccountID: stripe.String("acct_1Nv0FGQ9RKHgCVdK"),
}
result, err := sc.V2CoreAccountsPersons.Retrieve(
  context.TODO(), "person_test_61RS0CgWt1xBt8M1Q16RS0Cg0WSQO5ZXUVpZxZ9tAIbY", params)
```

```dotnet
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V2.Core.Accounts.Persons;
Stripe.V2.Core.AccountPerson accountPerson = service.Get(
    "acct_1Nv0FGQ9RKHgCVdK",
    "person_test_61RS0CgWt1xBt8M1Q16RS0Cg0WSQO5ZXUVpZxZ9tAIbY");
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
  "date_of_birth": {
    "day": 28,
    "month": 1,
    "year": 2000
  },
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
  "updated": "2024-11-26T17:12:55.000Z"
}
```