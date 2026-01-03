# Create an account token

Creates an Account Token.

## Parameters

- `contact_email` (string, optional)
  The default contact email address for the Account. Required when configuring the account as a merchant or recipient.

- `display_name` (string, optional)
  A descriptive name for the Account. This name will be surfaced in the Stripe Dashboard and on any invoices sent to the Account.

- `identity` (object, optional)
  Information about the company, individual, and business represented by the Account.

  - `identity.attestations` (object, optional)
    Attestations from the identity’s key people, e.g. owners, executives, directors, representatives.

    - `identity.attestations.directorship_declaration` (object, optional)
      This hash is used to attest that the directors information provided to Stripe is both current and correct; IP, date, and User Agent are expanded by Stripe.

      - `identity.attestations.directorship_declaration.attested` (boolean, optional)
        A boolean indicating if the directors information has been attested.

    - `identity.attestations.ownership_declaration` (object, optional)
      This hash is used to attest that the beneficial owner information provided to Stripe is both current and correct; IP, date, and User Agent are expanded by Stripe.

      - `identity.attestations.ownership_declaration.attested` (boolean, optional)
        A boolean indicating if the beneficial owner information has been attested.

    - `identity.attestations.persons_provided` (object, optional)
      Attestation that all Persons with a specific Relationship value have been provided.

      - `identity.attestations.persons_provided.directors` (boolean, optional)
        Whether the company’s directors have been provided. Set this Boolean to true after creating all the company’s directors with the [Persons API](https://docs.stripe.com/api/v2/core/accounts/createperson.md).

      - `identity.attestations.persons_provided.executives` (boolean, optional)
        Whether the company’s executives have been provided. Set this Boolean to true after creating all the company’s executives with the [Persons API](https://docs.stripe.com/api/v2/core/accounts/createperson.md).

      - `identity.attestations.persons_provided.owners` (boolean, optional)
        Whether the company’s owners have been provided. Set this Boolean to true after creating all the company’s owners with the [Persons API](https://docs.stripe.com/api/v2/core/accounts/createperson.md).

      - `identity.attestations.persons_provided.ownership_exemption_reason` (enum, optional)
        Reason for why the company is exempt from providing ownership information.
Possible enum values:
        - `qualified_entity_exceeds_ownership_threshold`
          A qualifying entity or group of qualifying entities own a significant enough share of the merchant’s business that they are exempt from providing ownership information based on regulatory guidelines in the merchant’s country.

        - `qualifies_as_financial_institution`
          A merchant is a financial institution.

    - `identity.attestations.representative_declaration` (object, optional)
      This hash is used to attest that the representative is authorized to act as the representative of their legal entity; IP, date, and User Agent are expanded by Stripe.

      - `identity.attestations.representative_declaration.attested` (boolean, optional)
        A boolean indicating if the representative is authorized to act as the representative of their legal entity.

    - `identity.attestations.terms_of_service` (object, optional)
      Attestations of accepted terms of service agreements.

      - `identity.attestations.terms_of_service.account` (object, optional)
        Details on the Account’s acceptance of the [Stripe Services Agreement]; IP, date, and User Agent are expanded by Stripe.

        - `identity.attestations.terms_of_service.account.shown_and_accepted` (boolean, optional)
          The boolean value indicating if the terms of service have been accepted.

  - `identity.business_details` (object, optional)
    Information about the company or business.

    - `identity.business_details.address` (object, optional)
      The business registration address of the business entity.

      - `identity.business_details.address.city` (string, optional)
        City, district, suburb, town, or village.

      - `identity.business_details.address.country` (enum, optional)
        Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

      - `identity.business_details.address.line1` (string, optional)
        Address line 1 (e.g., street, PO Box, or company name).

      - `identity.business_details.address.line2` (string, optional)
        Address line 2 (e.g., apartment, suite, unit, or building).

      - `identity.business_details.address.postal_code` (string, optional)
        ZIP or postal code.

      - `identity.business_details.address.state` (string, optional)
        State, county, province, or region.

      - `identity.business_details.address.town` (string, optional)
        Town or district.

    - `identity.business_details.annual_revenue` (object, optional)
      The business gross annual revenue for its preceding fiscal year.

      - `identity.business_details.annual_revenue.amount` (object, optional)
        A non-negative integer representing the amount in the smallest currency unit.

        - `identity.business_details.annual_revenue.amount.currency` (string, required)
          A lowercase alpha3 currency code like “usd”.

        - `identity.business_details.annual_revenue.amount.value` (integer, required)
          In minor units like 123 for 1.23 USD.

      - `identity.business_details.annual_revenue.fiscal_year_end` (string, optional)
        The close-out date of the preceding fiscal year in ISO 8601 format. E.g. 2023-12-31 for the 31st of December, 2023.

    - `identity.business_details.documents` (object, optional)
      A document verifying the business.

      - `identity.business_details.documents.bank_account_ownership_verification` (object, optional)
        One or more documents that support the bank account ownership verification requirement. Must be a document associated with the account’s primary active bank account that displays the last 4 digits of the account number, either a statement or a check.

        - `identity.business_details.documents.bank_account_ownership_verification.files` (array of strings, required)
          One or more document IDs returned by a [file upload](https://docs.stripe.com/api/persons/update.md#create_file) with a purpose value of `account_requirement`.

        - `identity.business_details.documents.bank_account_ownership_verification.type` (enum, required)
          The format of the document. Currently supports `files` only.
Possible enum values:
          - `files`
            Document type with multiple files.

      - `identity.business_details.documents.company_license` (object, optional)
        One or more documents that demonstrate proof of a company’s license to operate.

        - `identity.business_details.documents.company_license.files` (array of strings, required)
          One or more document IDs returned by a [file upload](https://docs.stripe.com/api/persons/update.md#create_file) with a purpose value of `account_requirement`.

        - `identity.business_details.documents.company_license.type` (enum, required)
          The format of the document. Currently supports `files` only.
Possible enum values:
          - `files`
            Document type with multiple files.

      - `identity.business_details.documents.company_memorandum_of_association` (object, optional)
        One or more documents showing the company’s Memorandum of Association.

        - `identity.business_details.documents.company_memorandum_of_association.files` (array of strings, required)
          One or more document IDs returned by a [file upload](https://docs.stripe.com/api/persons/update.md#create_file) with a purpose value of `account_requirement`.

        - `identity.business_details.documents.company_memorandum_of_association.type` (enum, required)
          The format of the document. Currently supports `files` only.
Possible enum values:
          - `files`
            Document type with multiple files.

      - `identity.business_details.documents.company_ministerial_decree` (object, optional)
        Certain countries only: One or more documents showing the ministerial decree legalizing the company’s establishment.

        - `identity.business_details.documents.company_ministerial_decree.files` (array of strings, required)
          One or more document IDs returned by a [file upload](https://docs.stripe.com/api/persons/update.md#create_file) with a purpose value of `account_requirement`.

        - `identity.business_details.documents.company_ministerial_decree.type` (enum, required)
          The format of the document. Currently supports `files` only.
Possible enum values:
          - `files`
            Document type with multiple files.

      - `identity.business_details.documents.company_registration_verification` (object, optional)
        One or more documents that demonstrate proof of a company’s registration with the appropriate local authorities.

        - `identity.business_details.documents.company_registration_verification.files` (array of strings, required)
          One or more document IDs returned by a [file upload](https://docs.stripe.com/api/persons/update.md#create_file) with a purpose value of `account_requirement`.

        - `identity.business_details.documents.company_registration_verification.type` (enum, required)
          The format of the document. Currently supports `files` only.
Possible enum values:
          - `files`
            Document type with multiple files.

      - `identity.business_details.documents.company_tax_id_verification` (object, optional)
        One or more documents that demonstrate proof of a company’s tax ID.

        - `identity.business_details.documents.company_tax_id_verification.files` (array of strings, required)
          One or more document IDs returned by a [file upload](https://docs.stripe.com/api/persons/update.md#create_file) with a purpose value of `account_requirement`.

        - `identity.business_details.documents.company_tax_id_verification.type` (enum, required)
          The format of the document. Currently supports `files` only.
Possible enum values:
          - `files`
            Document type with multiple files.

      - `identity.business_details.documents.primary_verification` (object, optional)
        A document verifying the business.

        - `identity.business_details.documents.primary_verification.front_back` (object, required)
          The [file upload](https://docs.stripe.com/api/persons/update.md#create_file) tokens referring to each side of the document.

          - `identity.business_details.documents.primary_verification.front_back.back` (string, optional)
            A [file upload](https://docs.stripe.com/api/persons/update.md#create_file) token representing the back of the verification document. The purpose of the uploaded file should be ‘identity_document’. The uploaded file needs to be a color image (smaller than 8,000px by 8,000px), in JPG, PNG, or PDF format, and less than 10 MB in size.

          - `identity.business_details.documents.primary_verification.front_back.front` (string, optional)
            A [file upload](https://docs.stripe.com/api/persons/update.md#create_file) token representing the front of the verification document. The purpose of the uploaded file should be ‘identity_document’. The uploaded file needs to be a color image (smaller than 8,000px by 8,000px), in JPG, PNG, or PDF format, and less than 10 MB in size.

        - `identity.business_details.documents.primary_verification.type` (enum, required)
          The format of the verification document. Currently supports `front_back` only.
Possible enum values:
          - `front_back`
            Document type with both front and back sides.

      - `identity.business_details.documents.proof_of_address` (object, optional)
        One or more documents that demonstrate proof of address.

        - `identity.business_details.documents.proof_of_address.files` (array of strings, required)
          One or more document IDs returned by a [file upload](https://docs.stripe.com/api/persons/update.md#create_file) with a purpose value of `account_requirement`.

        - `identity.business_details.documents.proof_of_address.type` (enum, required)
          The format of the document. Currently supports `files` only.
Possible enum values:
          - `files`
            Document type with multiple files.

      - `identity.business_details.documents.proof_of_registration` (object, optional)
        One or more documents showing the company’s proof of registration with the national business registry.

        - `identity.business_details.documents.proof_of_registration.files` (array of strings, required)
          One or more document IDs returned by a [file upload](https://docs.stripe.com/api/persons/update.md#create_file) with a purpose value of `account_requirement`.

        - `identity.business_details.documents.proof_of_registration.type` (enum, required)
          The format of the document. Currently supports `files` only.
Possible enum values:
          - `files`
            Document type with multiple files.

      - `identity.business_details.documents.proof_of_ultimate_beneficial_ownership` (object, optional)
        One or more documents that demonstrate proof of ultimate beneficial ownership.

        - `identity.business_details.documents.proof_of_ultimate_beneficial_ownership.files` (array of strings, required)
          One or more document IDs returned by a [file upload](https://docs.stripe.com/api/persons/update.md#create_file) with a purpose value of `account_requirement`.

        - `identity.business_details.documents.proof_of_ultimate_beneficial_ownership.type` (enum, required)
          The format of the document. Currently supports `files` only.
Possible enum values:
          - `files`
            Document type with multiple files.

    - `identity.business_details.estimated_worker_count` (integer, optional)
      Estimated maximum number of workers currently engaged by the business (including employees, contractors, and vendors).

    - `identity.business_details.id_numbers` (array of objects, optional)
      The ID numbers of a business entity.

      - `identity.business_details.id_numbers.registrar` (string, optional)
        The registrar of the ID number (Only valid for DE ID number types).

      - `identity.business_details.id_numbers.type` (enum, required)
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

      - `identity.business_details.id_numbers.value` (string, required)
        The value of the ID number.

    - `identity.business_details.monthly_estimated_revenue` (object, optional)
      An estimate of the monthly revenue of the business.

      - `identity.business_details.monthly_estimated_revenue.amount` (object, optional)
        A non-negative integer representing the amount in the smallest currency unit.

        - `identity.business_details.monthly_estimated_revenue.amount.currency` (string, required)
          A lowercase alpha3 currency code like “usd”.

        - `identity.business_details.monthly_estimated_revenue.amount.value` (integer, required)
          In minor units like 123 for 1.23 USD.

    - `identity.business_details.phone` (string, optional)
      The phone number of the Business Entity.

    - `identity.business_details.registered_name` (string, optional)
      The business legal name.

    - `identity.business_details.script_addresses` (object, optional)
      The business registration address of the business entity in non latin script.

      - `identity.business_details.script_addresses.kana` (object, optional)
        Kana Address.

        - `identity.business_details.script_addresses.kana.city` (string, optional)
          City, district, suburb, town, or village.

        - `identity.business_details.script_addresses.kana.country` (enum, optional)
          Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

        - `identity.business_details.script_addresses.kana.line1` (string, optional)
          Address line 1 (e.g., street, PO Box, or company name).

        - `identity.business_details.script_addresses.kana.line2` (string, optional)
          Address line 2 (e.g., apartment, suite, unit, or building).

        - `identity.business_details.script_addresses.kana.postal_code` (string, optional)
          ZIP or postal code.

        - `identity.business_details.script_addresses.kana.state` (string, optional)
          State, county, province, or region.

        - `identity.business_details.script_addresses.kana.town` (string, optional)
          Town or district.

      - `identity.business_details.script_addresses.kanji` (object, optional)
        Kanji Address.

        - `identity.business_details.script_addresses.kanji.city` (string, optional)
          City, district, suburb, town, or village.

        - `identity.business_details.script_addresses.kanji.country` (enum, optional)
          Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

        - `identity.business_details.script_addresses.kanji.line1` (string, optional)
          Address line 1 (e.g., street, PO Box, or company name).

        - `identity.business_details.script_addresses.kanji.line2` (string, optional)
          Address line 2 (e.g., apartment, suite, unit, or building).

        - `identity.business_details.script_addresses.kanji.postal_code` (string, optional)
          ZIP or postal code.

        - `identity.business_details.script_addresses.kanji.state` (string, optional)
          State, county, province, or region.

        - `identity.business_details.script_addresses.kanji.town` (string, optional)
          Town or district.

    - `identity.business_details.script_names` (object, optional)
      The business legal name in non latin script.

      - `identity.business_details.script_names.kana` (object, optional)
        Kana name.

        - `identity.business_details.script_names.kana.registered_name` (string, optional)
          Registered name of the business.

      - `identity.business_details.script_names.kanji` (object, optional)
        Kanji name.

        - `identity.business_details.script_names.kanji.registered_name` (string, optional)
          Registered name of the business.

    - `identity.business_details.structure` (enum, optional)
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

  - `identity.entity_type` (enum, optional)
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

  - `identity.individual` (object, optional)
    Information about the person represented by the account.

    - `identity.individual.additional_addresses` (array of objects, optional)
      Additional addresses associated with the individual.

      - `identity.individual.additional_addresses.city` (string, optional)
        City, district, suburb, town, or village.

      - `identity.individual.additional_addresses.country` (enum, optional)
        Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

      - `identity.individual.additional_addresses.line1` (string, optional)
        Address line 1 (e.g., street, PO Box, or company name).

      - `identity.individual.additional_addresses.line2` (string, optional)
        Address line 2 (e.g., apartment, suite, unit, or building).

      - `identity.individual.additional_addresses.postal_code` (string, optional)
        ZIP or postal code.

      - `identity.individual.additional_addresses.purpose` (enum, required)
        Purpose of additional address.
Possible enum values:
        - `registered`
          The registered address.

      - `identity.individual.additional_addresses.state` (string, optional)
        State, county, province, or region.

      - `identity.individual.additional_addresses.town` (string, optional)
        Town or district.

    - `identity.individual.additional_names` (array of objects, optional)
      Additional names (e.g. aliases) associated with the individual.

      - `identity.individual.additional_names.full_name` (string, optional)
        The person’s full name.

      - `identity.individual.additional_names.given_name` (string, optional)
        The person’s first or given name.

      - `identity.individual.additional_names.purpose` (enum, required)
        The purpose or type of the additional name.
Possible enum values:
        - `alias`
          An alias for the individual’s name.

        - `maiden`
          The maiden name of the individual.

      - `identity.individual.additional_names.surname` (string, optional)
        The person’s last or family name.

    - `identity.individual.address` (object, optional)
      The individual’s residential address.

      - `identity.individual.address.city` (string, optional)
        City, district, suburb, town, or village.

      - `identity.individual.address.country` (enum, optional)
        Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

      - `identity.individual.address.line1` (string, optional)
        Address line 1 (e.g., street, PO Box, or company name).

      - `identity.individual.address.line2` (string, optional)
        Address line 2 (e.g., apartment, suite, unit, or building).

      - `identity.individual.address.postal_code` (string, optional)
        ZIP or postal code.

      - `identity.individual.address.state` (string, optional)
        State, county, province, or region.

      - `identity.individual.address.town` (string, optional)
        Town or district.

    - `identity.individual.date_of_birth` (object, optional)
      The individual’s date of birth.

      - `identity.individual.date_of_birth.day` (integer, required)
        The day of the birth.

      - `identity.individual.date_of_birth.month` (integer, required)
        The month of birth.

      - `identity.individual.date_of_birth.year` (integer, required)
        The year of birth.

    - `identity.individual.documents` (object, optional)
      Documents that may be submitted to satisfy various informational requests.

      - `identity.individual.documents.company_authorization` (object, optional)
        One or more documents that demonstrate proof that this person is authorized to represent the company.

        - `identity.individual.documents.company_authorization.files` (array of strings, required)
          One or more document IDs returned by a [file upload](https://docs.stripe.com/api/persons/update.md#create_file) with a purpose value of `account_requirement`.

        - `identity.individual.documents.company_authorization.type` (enum, required)
          The format of the document. Currently supports `files` only.
Possible enum values:
          - `files`
            Document type with multiple files.

      - `identity.individual.documents.passport` (object, optional)
        One or more documents showing the person’s passport page with photo and personal data.

        - `identity.individual.documents.passport.files` (array of strings, required)
          One or more document IDs returned by a [file upload](https://docs.stripe.com/api/persons/update.md#create_file) with a purpose value of `account_requirement`.

        - `identity.individual.documents.passport.type` (enum, required)
          The format of the document. Currently supports `files` only.
Possible enum values:
          - `files`
            Document type with multiple files.

      - `identity.individual.documents.primary_verification` (object, optional)
        An identifying document showing the person’s name, either a passport or local ID card.

        - `identity.individual.documents.primary_verification.front_back` (object, required)
          The [file upload](https://docs.stripe.com/api/persons/update.md#create_file) tokens referring to each side of the document.

          - `identity.individual.documents.primary_verification.front_back.back` (string, optional)
            A [file upload](https://docs.stripe.com/api/persons/update.md#create_file) token representing the back of the verification document. The purpose of the uploaded file should be ‘identity_document’. The uploaded file needs to be a color image (smaller than 8,000px by 8,000px), in JPG, PNG, or PDF format, and less than 10 MB in size.

          - `identity.individual.documents.primary_verification.front_back.front` (string, optional)
            A [file upload](https://docs.stripe.com/api/persons/update.md#create_file) token representing the front of the verification document. The purpose of the uploaded file should be ‘identity_document’. The uploaded file needs to be a color image (smaller than 8,000px by 8,000px), in JPG, PNG, or PDF format, and less than 10 MB in size.

        - `identity.individual.documents.primary_verification.type` (enum, required)
          The format of the verification document. Currently supports `front_back` only.
Possible enum values:
          - `front_back`
            Document type with both front and back sides.

      - `identity.individual.documents.secondary_verification` (object, optional)
        A document showing address, either a passport, local ID card, or utility bill from a well-known utility company.

        - `identity.individual.documents.secondary_verification.front_back` (object, required)
          The [file upload](https://docs.stripe.com/api/persons/update.md#create_file) tokens referring to each side of the document.

          - `identity.individual.documents.secondary_verification.front_back.back` (string, optional)
            A [file upload](https://docs.stripe.com/api/persons/update.md#create_file) token representing the back of the verification document. The purpose of the uploaded file should be ‘identity_document’. The uploaded file needs to be a color image (smaller than 8,000px by 8,000px), in JPG, PNG, or PDF format, and less than 10 MB in size.

          - `identity.individual.documents.secondary_verification.front_back.front` (string, optional)
            A [file upload](https://docs.stripe.com/api/persons/update.md#create_file) token representing the front of the verification document. The purpose of the uploaded file should be ‘identity_document’. The uploaded file needs to be a color image (smaller than 8,000px by 8,000px), in JPG, PNG, or PDF format, and less than 10 MB in size.

        - `identity.individual.documents.secondary_verification.type` (enum, required)
          The format of the verification document. Currently supports `front_back` only.
Possible enum values:
          - `front_back`
            Document type with both front and back sides.

      - `identity.individual.documents.visa` (object, optional)
        One or more documents showing the person’s visa required for living in the country where they are residing.

        - `identity.individual.documents.visa.files` (array of strings, required)
          One or more document IDs returned by a [file upload](https://docs.stripe.com/api/persons/update.md#create_file) with a purpose value of `account_requirement`.

        - `identity.individual.documents.visa.type` (enum, required)
          The format of the document. Currently supports `files` only.
Possible enum values:
          - `files`
            Document type with multiple files.

    - `identity.individual.email` (string, optional)
      The individual’s email address.

    - `identity.individual.given_name` (string, optional)
      The individual’s first name.

    - `identity.individual.id_numbers` (array of objects, optional)
      The identification numbers (e.g., SSN) associated with the individual.

      - `identity.individual.id_numbers.type` (enum, required)
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

      - `identity.individual.id_numbers.value` (string, required)
        The value of the ID number.

    - `identity.individual.legal_gender` (enum, optional)
      The individual’s gender (International regulations require either “male” or “female”).
Possible enum values:
      - `female`
        Female gender person.

      - `male`
        Male gender person.

    - `identity.individual.metadata` (map, optional)
      Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

    - `identity.individual.nationalities` (array of enums, optional)
      The countries where the individual is a national. Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

    - `identity.individual.phone` (string, optional)
      The individual’s phone number.

    - `identity.individual.political_exposure` (enum, optional)
      The individual’s political exposure.
Possible enum values:
      - `existing`
        The person has disclosed that they do have political exposure.

      - `none`
        The person has disclosed that they have no political exposure.

    - `identity.individual.relationship` (object, optional)
      The relationship that this individual has with the account’s identity.

      - `identity.individual.relationship.director` (boolean, optional)
        Whether the person is a director of the account’s identity. Directors are typically members of the governing board of the company, or responsible for ensuring the company meets its regulatory obligations.

      - `identity.individual.relationship.executive` (boolean, optional)
        Whether the person has significant responsibility to control, manage, or direct the organization.

      - `identity.individual.relationship.owner` (boolean, optional)
        Whether the person is an owner of the account’s identity.

      - `identity.individual.relationship.percent_ownership` (decimal, optional)
        The percent owned by the person of the account’s legal entity.

      - `identity.individual.relationship.title` (string, optional)
        The person’s title (e.g., CEO, Support Engineer).

    - `identity.individual.script_addresses` (object, optional)
      The script addresses (e.g., non-Latin characters) associated with the individual.

      - `identity.individual.script_addresses.kana` (object, optional)
        Kana Address.

        - `identity.individual.script_addresses.kana.city` (string, optional)
          City, district, suburb, town, or village.

        - `identity.individual.script_addresses.kana.country` (enum, optional)
          Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

        - `identity.individual.script_addresses.kana.line1` (string, optional)
          Address line 1 (e.g., street, PO Box, or company name).

        - `identity.individual.script_addresses.kana.line2` (string, optional)
          Address line 2 (e.g., apartment, suite, unit, or building).

        - `identity.individual.script_addresses.kana.postal_code` (string, optional)
          ZIP or postal code.

        - `identity.individual.script_addresses.kana.state` (string, optional)
          State, county, province, or region.

        - `identity.individual.script_addresses.kana.town` (string, optional)
          Town or district.

      - `identity.individual.script_addresses.kanji` (object, optional)
        Kanji Address.

        - `identity.individual.script_addresses.kanji.city` (string, optional)
          City, district, suburb, town, or village.

        - `identity.individual.script_addresses.kanji.country` (enum, optional)
          Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

        - `identity.individual.script_addresses.kanji.line1` (string, optional)
          Address line 1 (e.g., street, PO Box, or company name).

        - `identity.individual.script_addresses.kanji.line2` (string, optional)
          Address line 2 (e.g., apartment, suite, unit, or building).

        - `identity.individual.script_addresses.kanji.postal_code` (string, optional)
          ZIP or postal code.

        - `identity.individual.script_addresses.kanji.state` (string, optional)
          State, county, province, or region.

        - `identity.individual.script_addresses.kanji.town` (string, optional)
          Town or district.

    - `identity.individual.script_names` (object, optional)
      The individuals primary name in non latin script.

      - `identity.individual.script_names.kana` (object, optional)
        Persons name in kana script.

        - `identity.individual.script_names.kana.given_name` (string, optional)
          The person’s first or given name.

        - `identity.individual.script_names.kana.surname` (string, optional)
          The person’s last or family name.

      - `identity.individual.script_names.kanji` (object, optional)
        Persons name in kanji script.

        - `identity.individual.script_names.kanji.given_name` (string, optional)
          The person’s first or given name.

        - `identity.individual.script_names.kanji.surname` (string, optional)
          The person’s last or family name.

    - `identity.individual.surname` (string, optional)
      The individual’s last name.

## Returns

## Response attributes

- `id` (string)
  Unique identifier for the token.

- `object` (string, value is "v2.core.account_token")
  String representing the object’s type. Objects of the same type share the same value of the object field.

- `created` (timestamp)
  Time at which the token was created. Represented as a RFC 3339 date & time UTC value in millisecond precision, for example: 2022-09-18T13:22:18.123Z.

- `expires_at` (timestamp)
  Time at which the token will expire.

- `livemode` (boolean)
  Has the value `true` if the token exists in live mode or the value `false` if the object exists in test mode.

- `used` (boolean)
  Determines if the token has already been used (tokens can only be used once).

## Error Codes

| HTTP status code | Code                                       | Description                                 |
| ---------------- | ------------------------------------------ | ------------------------------------------- |
| 400              | token_must_be_created_with_publishable_key | Token must be created with publishable key. |

```curl
curl -X POST https://api.stripe.com/v2/core/account_tokens \
  -H "Authorization: Bearer <<YOUR_SECRET_KEY>>" \
  -H "Stripe-Version: {{STRIPE_API_VERSION}}" \
  --json '{
    "contact_email": "furever@example.com",
    "display_name": "Furever",
    "identity": {
        "attestations": {
            "terms_of_service": {
                "account": {
                    "shown_and_accepted": true
                }
            }
        },
        "entity_type": "company",
        "business_details": {
            "registered_name": "Furever"
        }
    }
  }'
```

```cli
stripe v2 core account_tokens create  \
  --contact-email="furever@example.com" \
  --display-name=Furever \
  --identity.attestations.terms-of-service.account.shown-and-accepted=true \
  --identity.entity-type=company \
  --identity.business-details.registered-name=Furever
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

account_token = client.v2.core.account_tokens.create({
  contact_email: 'furever@example.com',
  display_name: 'Furever',
  identity: {
    attestations: {terms_of_service: {account: {shown_and_accepted: true}}},
    entity_type: 'company',
    business_details: {registered_name: 'Furever'},
  },
})
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

account_token = client.v2.core.account_tokens.create({
  "contact_email": "furever@example.com",
  "display_name": "Furever",
  "identity": {
    "attestations": {"terms_of_service": {"account": {"shown_and_accepted": True}}},
    "entity_type": "company",
    "business_details": {"registered_name": "Furever"},
  },
})
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$accountToken = $stripe->v2->core->accountTokens->create([
  'contact_email' => 'furever@example.com',
  'display_name' => 'Furever',
  'identity' => [
    'attestations' => [
      'terms_of_service' => ['account' => ['shown_and_accepted' => true]],
    ],
    'entity_type' => 'company',
    'business_details' => ['registered_name' => 'Furever'],
  ],
]);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

AccountTokenCreateParams params =
  AccountTokenCreateParams.builder()
    .setContactEmail("furever@example.com")
    .setDisplayName("Furever")
    .setIdentity(
      AccountTokenCreateParams.Identity.builder()
        .setAttestations(
          AccountTokenCreateParams.Identity.Attestations.builder()
            .setTermsOfService(
              AccountTokenCreateParams.Identity.Attestations.TermsOfService.builder()
                .setAccount(
                  AccountTokenCreateParams.Identity.Attestations.TermsOfService.Account.builder()
                    .setShownAndAccepted(true)
                    .build()
                )
                .build()
            )
            .build()
        )
        .setEntityType(AccountTokenCreateParams.Identity.EntityType.COMPANY)
        .setBusinessDetails(
          AccountTokenCreateParams.Identity.BusinessDetails.builder()
            .setRegisteredName("Furever")
            .build()
        )
        .build()
    )
    .build();

AccountToken accountToken = client.v2().core().accountTokens().create(params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const accountToken = await stripe.v2.core.accountTokens.create({
  contact_email: 'furever@example.com',
  display_name: 'Furever',
  identity: {
    attestations: {
      terms_of_service: {
        account: {
          shown_and_accepted: true,
        },
      },
    },
    entity_type: 'company',
    business_details: {
      registered_name: 'Furever',
    },
  },
});
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.V2CoreAccountTokenCreateParams{
  ContactEmail: stripe.String("furever@example.com"),
  DisplayName: stripe.String("Furever"),
  Identity: &stripe.V2CoreAccountTokenCreateIdentityParams{
    Attestations: &stripe.V2CoreAccountTokenCreateIdentityAttestationsParams{
      TermsOfService: &stripe.V2CoreAccountTokenCreateIdentityAttestationsTermsOfServiceParams{
        Account: &stripe.V2CoreAccountTokenCreateIdentityAttestationsTermsOfServiceAccountParams{
          ShownAndAccepted: stripe.Bool(true),
        },
      },
    },
    EntityType: stripe.String("company"),
    BusinessDetails: &stripe.V2CoreAccountTokenCreateIdentityBusinessDetailsParams{
      RegisteredName: stripe.String("Furever"),
    },
  },
}
result, err := sc.V2CoreAccountTokens.Create(context.TODO(), params)
```

```dotnet
var options = new Stripe.V2.Core.AccountTokenCreateOptions
{
    ContactEmail = "furever@example.com",
    DisplayName = "Furever",
    Identity = new Stripe.V2.Core.AccountTokenCreateIdentityOptions
    {
        Attestations = new Stripe.V2.Core.AccountTokenCreateIdentityAttestationsOptions
        {
            TermsOfService = new Stripe.V2.Core.AccountTokenCreateIdentityAttestationsTermsOfServiceOptions
            {
                Account = new Stripe.V2.Core.AccountTokenCreateIdentityAttestationsTermsOfServiceAccountOptions
                {
                    ShownAndAccepted = true,
                },
            },
        },
        EntityType = "company",
        BusinessDetails = new Stripe.V2.Core.AccountTokenCreateIdentityBusinessDetailsOptions
        {
            RegisteredName = "Furever",
        },
    },
};
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V2.Core.AccountTokens;
Stripe.V2.Core.AccountToken accountToken = service.Create(options);
```

### Response

```json
{
  "id": "accttok_61RS0CgWt1xBt8M1Q16RS0Cg0WSQO5ZXUVpZxZ9tAIbY",
  "object": "v2.core.account_token",
  "created": "2025-11-17T14:00:00.000Z",
  "expires_at": "2025-11-17T14:10:00.000Z",
  "livemode": true,
  "used": false
}
```