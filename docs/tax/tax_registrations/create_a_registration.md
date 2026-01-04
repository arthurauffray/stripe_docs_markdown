# Create a registration

Creates a new Tax `Registration` object.

## Returns

A Tax `Registration` object.

## Parameters

- `active_from` (string | timestamp, required)
  Time at which the Tax Registration becomes active. It can be either `now` to indicate the current time, or a future timestamp measured in seconds since the Unix epoch.

- `country` (string, required)
  Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

- `country_options` (object, required)
  Specific options for a registration in the specified `country`.

  - `country_options.ae` (object, required if country is ae)
    Options for the registration in AE.

    - `country_options.ae.type` (enum, required)
      Type of registration to be created in `country`.
Possible enum values:
      - `standard`
        A standard Tax Registration in the specified country.

    - `country_options.ae.standard` (object, required if type is standard)
      Options for the standard registration.

      - `country_options.ae.standard.place_of_supply_scheme` (enum, optional)
        Place of supply scheme used in an standard registration.
Possible enum values:
        - `inbound_goods`
          Inbound goods place of supply scheme in which the tax is collected at destination for inbound physical goods.

        - `standard`
          Standard place of supply scheme in which tax is applied to sales in this country only.

  - `country_options.al` (object, required if country is al)
    Options for the registration in AL.

    - `country_options.al.type` (enum, required)
      Type of registration to be created in `country`.
Possible enum values:
      - `standard`
        A standard Tax Registration in the specified country.

    - `country_options.al.standard` (object, required if type is standard)
      Options for the standard registration.

      - `country_options.al.standard.place_of_supply_scheme` (enum, optional)
        Place of supply scheme used in an standard registration.
Possible enum values:
        - `inbound_goods`
          Inbound goods place of supply scheme in which the tax is collected at destination for inbound physical goods.

        - `standard`
          Standard place of supply scheme in which tax is applied to sales in this country only.

  - `country_options.am` (object, required if country is am)
    Options for the registration in AM.

    - `country_options.am.type` (enum, required)
      Type of registration to be created in `country`.
Possible enum values:
      - `simplified`
        A simplified Tax Registration in the specified country.

  - `country_options.ao` (object, required if country is ao)
    Options for the registration in AO.

    - `country_options.ao.type` (enum, required)
      Type of registration to be created in `country`.
Possible enum values:
      - `standard`
        A standard Tax Registration in the specified country.

    - `country_options.ao.standard` (object, required if type is standard)
      Options for the standard registration.

      - `country_options.ao.standard.place_of_supply_scheme` (enum, optional)
        Place of supply scheme used in an standard registration.
Possible enum values:
        - `inbound_goods`
          Inbound goods place of supply scheme in which the tax is collected at destination for inbound physical goods.

        - `standard`
          Standard place of supply scheme in which tax is applied to sales in this country only.

  - `country_options.at` (object, required if country is at)
    Options for the registration in AT.

    - `country_options.at.type` (enum, required)
      Type of registration to be created in an EU country.
Possible enum values:
      - `ioss`
        Common for businesses shipping goods below EUR 150 from non-EU countries to EU customers.

      - `oss_non_union`
        Common for businesses established outside of the EU selling services to customers in the EU.

      - `oss_union`
        Common for businesses established in the EU selling goods and services to customers in the EU.

      - `standard`
        Common for businesses selling goods and services to customers in this country.

    - `country_options.at.standard` (object, required if type is standard)
      Options for the standard registration.

      - `country_options.at.standard.place_of_supply_scheme` (enum, required)
        Place of supply scheme used in an EU standard registration.
Possible enum values:
        - `inbound_goods`
          Inbound goods place of supply scheme in which the tax is collected at destination for inbound physical goods.

        - `small_seller`
          Small seller place of supply scheme in which the seller’s tax rate is applied to sales across the EU.

        - `standard`
          Standard place of supply scheme in which tax is applied to sales in this country only.

  - `country_options.au` (object, required if country is au)
    Options for the registration in AU.

    - `country_options.au.type` (enum, required)
      Type of registration to be created in `country`.
Possible enum values:
      - `standard`
        A standard Tax Registration in the specified country.

    - `country_options.au.standard` (object, required if type is standard)
      Options for the standard registration.

      - `country_options.au.standard.place_of_supply_scheme` (enum, optional)
        Place of supply scheme used in an standard registration.
Possible enum values:
        - `inbound_goods`
          Inbound goods place of supply scheme in which the tax is collected at destination for inbound physical goods.

        - `standard`
          Standard place of supply scheme in which tax is applied to sales in this country only.

  - `country_options.aw` (object, required if country is aw)
    Options for the registration in AW.

    - `country_options.aw.type` (enum, required)
      Type of registration to be created in `country`.
Possible enum values:
      - `standard`
        A standard Tax Registration in the specified country.

    - `country_options.aw.standard` (object, required if type is standard)
      Options for the standard registration.

      - `country_options.aw.standard.place_of_supply_scheme` (enum, optional)
        Place of supply scheme used in an standard registration.
Possible enum values:
        - `inbound_goods`
          Inbound goods place of supply scheme in which the tax is collected at destination for inbound physical goods.

        - `standard`
          Standard place of supply scheme in which tax is applied to sales in this country only.

  - `country_options.az` (object, required if country is az)
    Options for the registration in AZ.

    - `country_options.az.type` (enum, required)
      Type of registration to be created in `country`.
Possible enum values:
      - `simplified`
        A simplified Tax Registration in the specified country.

  - `country_options.ba` (object, required if country is ba)
    Options for the registration in BA.

    - `country_options.ba.type` (enum, required)
      Type of registration to be created in `country`.
Possible enum values:
      - `standard`
        A standard Tax Registration in the specified country.

    - `country_options.ba.standard` (object, required if type is standard)
      Options for the standard registration.

      - `country_options.ba.standard.place_of_supply_scheme` (enum, optional)
        Place of supply scheme used in an standard registration.
Possible enum values:
        - `inbound_goods`
          Inbound goods place of supply scheme in which the tax is collected at destination for inbound physical goods.

        - `standard`
          Standard place of supply scheme in which tax is applied to sales in this country only.

  - `country_options.bb` (object, required if country is bb)
    Options for the registration in BB.

    - `country_options.bb.type` (enum, required)
      Type of registration to be created in `country`.
Possible enum values:
      - `standard`
        A standard Tax Registration in the specified country.

    - `country_options.bb.standard` (object, required if type is standard)
      Options for the standard registration.

      - `country_options.bb.standard.place_of_supply_scheme` (enum, optional)
        Place of supply scheme used in an standard registration.
Possible enum values:
        - `inbound_goods`
          Inbound goods place of supply scheme in which the tax is collected at destination for inbound physical goods.

        - `standard`
          Standard place of supply scheme in which tax is applied to sales in this country only.

  - `country_options.bd` (object, required if country is bd)
    Options for the registration in BD.

    - `country_options.bd.type` (enum, required)
      Type of registration to be created in `country`.
Possible enum values:
      - `standard`
        A standard Tax Registration in the specified country.

    - `country_options.bd.standard` (object, required if type is standard)
      Options for the standard registration.

      - `country_options.bd.standard.place_of_supply_scheme` (enum, optional)
        Place of supply scheme used in an standard registration.
Possible enum values:
        - `inbound_goods`
          Inbound goods place of supply scheme in which the tax is collected at destination for inbound physical goods.

        - `standard`
          Standard place of supply scheme in which tax is applied to sales in this country only.

  - `country_options.be` (object, required if country is be)
    Options for the registration in BE.

    - `country_options.be.type` (enum, required)
      Type of registration to be created in an EU country.
Possible enum values:
      - `ioss`
        Common for businesses shipping goods below EUR 150 from non-EU countries to EU customers.

      - `oss_non_union`
        Common for businesses established outside of the EU selling services to customers in the EU.

      - `oss_union`
        Common for businesses established in the EU selling goods and services to customers in the EU.

      - `standard`
        Common for businesses selling goods and services to customers in this country.

    - `country_options.be.standard` (object, required if type is standard)
      Options for the standard registration.

      - `country_options.be.standard.place_of_supply_scheme` (enum, required)
        Place of supply scheme used in an EU standard registration.
Possible enum values:
        - `inbound_goods`
          Inbound goods place of supply scheme in which the tax is collected at destination for inbound physical goods.

        - `small_seller`
          Small seller place of supply scheme in which the seller’s tax rate is applied to sales across the EU.

        - `standard`
          Standard place of supply scheme in which tax is applied to sales in this country only.

  - `country_options.bf` (object, required if country is bf)
    Options for the registration in BF.

    - `country_options.bf.type` (enum, required)
      Type of registration to be created in `country`.
Possible enum values:
      - `standard`
        A standard Tax Registration in the specified country.

    - `country_options.bf.standard` (object, required if type is standard)
      Options for the standard registration.

      - `country_options.bf.standard.place_of_supply_scheme` (enum, optional)
        Place of supply scheme used in an standard registration.
Possible enum values:
        - `inbound_goods`
          Inbound goods place of supply scheme in which the tax is collected at destination for inbound physical goods.

        - `standard`
          Standard place of supply scheme in which tax is applied to sales in this country only.

  - `country_options.bg` (object, required if country is bg)
    Options for the registration in BG.

    - `country_options.bg.type` (enum, required)
      Type of registration to be created in an EU country.
Possible enum values:
      - `ioss`
        Common for businesses shipping goods below EUR 150 from non-EU countries to EU customers.

      - `oss_non_union`
        Common for businesses established outside of the EU selling services to customers in the EU.

      - `oss_union`
        Common for businesses established in the EU selling goods and services to customers in the EU.

      - `standard`
        Common for businesses selling goods and services to customers in this country.

    - `country_options.bg.standard` (object, required if type is standard)
      Options for the standard registration.

      - `country_options.bg.standard.place_of_supply_scheme` (enum, required)
        Place of supply scheme used in an EU standard registration.
Possible enum values:
        - `inbound_goods`
          Inbound goods place of supply scheme in which the tax is collected at destination for inbound physical goods.

        - `small_seller`
          Small seller place of supply scheme in which the seller’s tax rate is applied to sales across the EU.

        - `standard`
          Standard place of supply scheme in which tax is applied to sales in this country only.

  - `country_options.bh` (object, required if country is bh)
    Options for the registration in BH.

    - `country_options.bh.type` (enum, required)
      Type of registration to be created in `country`.
Possible enum values:
      - `standard`
        A standard Tax Registration in the specified country.

    - `country_options.bh.standard` (object, required if type is standard)
      Options for the standard registration.

      - `country_options.bh.standard.place_of_supply_scheme` (enum, optional)
        Place of supply scheme used in an standard registration.
Possible enum values:
        - `inbound_goods`
          Inbound goods place of supply scheme in which the tax is collected at destination for inbound physical goods.

        - `standard`
          Standard place of supply scheme in which tax is applied to sales in this country only.

  - `country_options.bj` (object, required if country is bj)
    Options for the registration in BJ.

    - `country_options.bj.type` (enum, required)
      Type of registration to be created in `country`.
Possible enum values:
      - `simplified`
        A simplified Tax Registration in the specified country.

  - `country_options.bs` (object, required if country is bs)
    Options for the registration in BS.

    - `country_options.bs.type` (enum, required)
      Type of registration to be created in `country`.
Possible enum values:
      - `standard`
        A standard Tax Registration in the specified country.

    - `country_options.bs.standard` (object, required if type is standard)
      Options for the standard registration.

      - `country_options.bs.standard.place_of_supply_scheme` (enum, optional)
        Place of supply scheme used in an standard registration.
Possible enum values:
        - `inbound_goods`
          Inbound goods place of supply scheme in which the tax is collected at destination for inbound physical goods.

        - `standard`
          Standard place of supply scheme in which tax is applied to sales in this country only.

  - `country_options.by` (object, required if country is by)
    Options for the registration in BY.

    - `country_options.by.type` (enum, required)
      Type of registration to be created in `country`.
Possible enum values:
      - `simplified`
        A simplified Tax Registration in the specified country.

  - `country_options.ca` (object, required if country is CA)
    Options for the registration in CA.

    - `country_options.ca.type` (enum, required)
      Type of registration to be created in Canada.
Possible enum values:
      - `province_standard`
        A Tax Registration in the specified Canadian province to collect PST/RST/QST.

      - `simplified`
        A simplified Tax Registration in Canada to collect GST/HST.

      - `standard`
        A standard Tax Registration in Canada to collect GST/HST.

    - `country_options.ca.province_standard` (object, required if type is province_standard)
      Options for the provincial tax registration.

      - `country_options.ca.province_standard.province` (string, required)
        Two-letter CA province code ([ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2)).

  - `country_options.cd` (object, required if country is cd)
    Options for the registration in CD.

    - `country_options.cd.type` (enum, required)
      Type of registration to be created in `country`.
Possible enum values:
      - `standard`
        A standard Tax Registration in the specified country.

    - `country_options.cd.standard` (object, required if type is standard)
      Options for the standard registration.

      - `country_options.cd.standard.place_of_supply_scheme` (enum, optional)
        Place of supply scheme used in an standard registration.
Possible enum values:
        - `inbound_goods`
          Inbound goods place of supply scheme in which the tax is collected at destination for inbound physical goods.

        - `standard`
          Standard place of supply scheme in which tax is applied to sales in this country only.

  - `country_options.ch` (object, required if country is ch)
    Options for the registration in CH.

    - `country_options.ch.type` (enum, required)
      Type of registration to be created in `country`.
Possible enum values:
      - `standard`
        A standard Tax Registration in the specified country.

    - `country_options.ch.standard` (object, required if type is standard)
      Options for the standard registration.

      - `country_options.ch.standard.place_of_supply_scheme` (enum, optional)
        Place of supply scheme used in an standard registration.
Possible enum values:
        - `inbound_goods`
          Inbound goods place of supply scheme in which the tax is collected at destination for inbound physical goods.

        - `standard`
          Standard place of supply scheme in which tax is applied to sales in this country only.

  - `country_options.cl` (object, required if country is cl)
    Options for the registration in CL.

    - `country_options.cl.type` (enum, required)
      Type of registration to be created in `country`.
Possible enum values:
      - `simplified`
        A simplified Tax Registration in the specified country.

  - `country_options.cm` (object, required if country is cm)
    Options for the registration in CM.

    - `country_options.cm.type` (enum, required)
      Type of registration to be created in `country`.
Possible enum values:
      - `simplified`
        A simplified Tax Registration in the specified country.

  - `country_options.co` (object, required if country is co)
    Options for the registration in CO.

    - `country_options.co.type` (enum, required)
      Type of registration to be created in `country`.
Possible enum values:
      - `simplified`
        A simplified Tax Registration in the specified country.

  - `country_options.cr` (object, required if country is cr)
    Options for the registration in CR.

    - `country_options.cr.type` (enum, required)
      Type of registration to be created in `country`.
Possible enum values:
      - `simplified`
        A simplified Tax Registration in the specified country.

  - `country_options.cv` (object, required if country is cv)
    Options for the registration in CV.

    - `country_options.cv.type` (enum, required)
      Type of registration to be created in `country`.
Possible enum values:
      - `simplified`
        A simplified Tax Registration in the specified country.

  - `country_options.cy` (object, required if country is cy)
    Options for the registration in CY.

    - `country_options.cy.type` (enum, required)
      Type of registration to be created in an EU country.
Possible enum values:
      - `ioss`
        Common for businesses shipping goods below EUR 150 from non-EU countries to EU customers.

      - `oss_non_union`
        Common for businesses established outside of the EU selling services to customers in the EU.

      - `oss_union`
        Common for businesses established in the EU selling goods and services to customers in the EU.

      - `standard`
        Common for businesses selling goods and services to customers in this country.

    - `country_options.cy.standard` (object, required if type is standard)
      Options for the standard registration.

      - `country_options.cy.standard.place_of_supply_scheme` (enum, required)
        Place of supply scheme used in an EU standard registration.
Possible enum values:
        - `inbound_goods`
          Inbound goods place of supply scheme in which the tax is collected at destination for inbound physical goods.

        - `small_seller`
          Small seller place of supply scheme in which the seller’s tax rate is applied to sales across the EU.

        - `standard`
          Standard place of supply scheme in which tax is applied to sales in this country only.

  - `country_options.cz` (object, required if country is cz)
    Options for the registration in CZ.

    - `country_options.cz.type` (enum, required)
      Type of registration to be created in an EU country.
Possible enum values:
      - `ioss`
        Common for businesses shipping goods below EUR 150 from non-EU countries to EU customers.

      - `oss_non_union`
        Common for businesses established outside of the EU selling services to customers in the EU.

      - `oss_union`
        Common for businesses established in the EU selling goods and services to customers in the EU.

      - `standard`
        Common for businesses selling goods and services to customers in this country.

    - `country_options.cz.standard` (object, required if type is standard)
      Options for the standard registration.

      - `country_options.cz.standard.place_of_supply_scheme` (enum, required)
        Place of supply scheme used in an EU standard registration.
Possible enum values:
        - `inbound_goods`
          Inbound goods place of supply scheme in which the tax is collected at destination for inbound physical goods.

        - `small_seller`
          Small seller place of supply scheme in which the seller’s tax rate is applied to sales across the EU.

        - `standard`
          Standard place of supply scheme in which tax is applied to sales in this country only.

  - `country_options.de` (object, required if country is de)
    Options for the registration in DE.

    - `country_options.de.type` (enum, required)
      Type of registration to be created in an EU country.
Possible enum values:
      - `ioss`
        Common for businesses shipping goods below EUR 150 from non-EU countries to EU customers.

      - `oss_non_union`
        Common for businesses established outside of the EU selling services to customers in the EU.

      - `oss_union`
        Common for businesses established in the EU selling goods and services to customers in the EU.

      - `standard`
        Common for businesses selling goods and services to customers in this country.

    - `country_options.de.standard` (object, required if type is standard)
      Options for the standard registration.

      - `country_options.de.standard.place_of_supply_scheme` (enum, required)
        Place of supply scheme used in an EU standard registration.
Possible enum values:
        - `inbound_goods`
          Inbound goods place of supply scheme in which the tax is collected at destination for inbound physical goods.

        - `small_seller`
          Small seller place of supply scheme in which the seller’s tax rate is applied to sales across the EU.

        - `standard`
          Standard place of supply scheme in which tax is applied to sales in this country only.

  - `country_options.dk` (object, required if country is dk)
    Options for the registration in DK.

    - `country_options.dk.type` (enum, required)
      Type of registration to be created in an EU country.
Possible enum values:
      - `ioss`
        Common for businesses shipping goods below EUR 150 from non-EU countries to EU customers.

      - `oss_non_union`
        Common for businesses established outside of the EU selling services to customers in the EU.

      - `oss_union`
        Common for businesses established in the EU selling goods and services to customers in the EU.

      - `standard`
        Common for businesses selling goods and services to customers in this country.

    - `country_options.dk.standard` (object, required if type is standard)
      Options for the standard registration.

      - `country_options.dk.standard.place_of_supply_scheme` (enum, required)
        Place of supply scheme used in an EU standard registration.
Possible enum values:
        - `inbound_goods`
          Inbound goods place of supply scheme in which the tax is collected at destination for inbound physical goods.

        - `small_seller`
          Small seller place of supply scheme in which the seller’s tax rate is applied to sales across the EU.

        - `standard`
          Standard place of supply scheme in which tax is applied to sales in this country only.

  - `country_options.ec` (object, required if country is ec)
    Options for the registration in EC.

    - `country_options.ec.type` (enum, required)
      Type of registration to be created in `country`.
Possible enum values:
      - `simplified`
        A simplified Tax Registration in the specified country.

  - `country_options.ee` (object, required if country is ee)
    Options for the registration in EE.

    - `country_options.ee.type` (enum, required)
      Type of registration to be created in an EU country.
Possible enum values:
      - `ioss`
        Common for businesses shipping goods below EUR 150 from non-EU countries to EU customers.

      - `oss_non_union`
        Common for businesses established outside of the EU selling services to customers in the EU.

      - `oss_union`
        Common for businesses established in the EU selling goods and services to customers in the EU.

      - `standard`
        Common for businesses selling goods and services to customers in this country.

    - `country_options.ee.standard` (object, required if type is standard)
      Options for the standard registration.

      - `country_options.ee.standard.place_of_supply_scheme` (enum, required)
        Place of supply scheme used in an EU standard registration.
Possible enum values:
        - `inbound_goods`
          Inbound goods place of supply scheme in which the tax is collected at destination for inbound physical goods.

        - `small_seller`
          Small seller place of supply scheme in which the seller’s tax rate is applied to sales across the EU.

        - `standard`
          Standard place of supply scheme in which tax is applied to sales in this country only.

  - `country_options.eg` (object, required if country is eg)
    Options for the registration in EG.

    - `country_options.eg.type` (enum, required)
      Type of registration to be created in `country`.
Possible enum values:
      - `simplified`
        A simplified Tax Registration in the specified country.

  - `country_options.es` (object, required if country is es)
    Options for the registration in ES.

    - `country_options.es.type` (enum, required)
      Type of registration to be created in an EU country.
Possible enum values:
      - `ioss`
        Common for businesses shipping goods below EUR 150 from non-EU countries to EU customers.

      - `oss_non_union`
        Common for businesses established outside of the EU selling services to customers in the EU.

      - `oss_union`
        Common for businesses established in the EU selling goods and services to customers in the EU.

      - `standard`
        Common for businesses selling goods and services to customers in this country.

    - `country_options.es.standard` (object, required if type is standard)
      Options for the standard registration.

      - `country_options.es.standard.place_of_supply_scheme` (enum, required)
        Place of supply scheme used in an EU standard registration.
Possible enum values:
        - `inbound_goods`
          Inbound goods place of supply scheme in which the tax is collected at destination for inbound physical goods.

        - `small_seller`
          Small seller place of supply scheme in which the seller’s tax rate is applied to sales across the EU.

        - `standard`
          Standard place of supply scheme in which tax is applied to sales in this country only.

  - `country_options.et` (object, required if country is et)
    Options for the registration in ET.

    - `country_options.et.type` (enum, required)
      Type of registration to be created in `country`.
Possible enum values:
      - `standard`
        A standard Tax Registration in the specified country.

    - `country_options.et.standard` (object, required if type is standard)
      Options for the standard registration.

      - `country_options.et.standard.place_of_supply_scheme` (enum, optional)
        Place of supply scheme used in an standard registration.
Possible enum values:
        - `inbound_goods`
          Inbound goods place of supply scheme in which the tax is collected at destination for inbound physical goods.

        - `standard`
          Standard place of supply scheme in which tax is applied to sales in this country only.

  - `country_options.fi` (object, required if country is fi)
    Options for the registration in FI.

    - `country_options.fi.type` (enum, required)
      Type of registration to be created in an EU country.
Possible enum values:
      - `ioss`
        Common for businesses shipping goods below EUR 150 from non-EU countries to EU customers.

      - `oss_non_union`
        Common for businesses established outside of the EU selling services to customers in the EU.

      - `oss_union`
        Common for businesses established in the EU selling goods and services to customers in the EU.

      - `standard`
        Common for businesses selling goods and services to customers in this country.

    - `country_options.fi.standard` (object, required if type is standard)
      Options for the standard registration.

      - `country_options.fi.standard.place_of_supply_scheme` (enum, required)
        Place of supply scheme used in an EU standard registration.
Possible enum values:
        - `inbound_goods`
          Inbound goods place of supply scheme in which the tax is collected at destination for inbound physical goods.

        - `small_seller`
          Small seller place of supply scheme in which the seller’s tax rate is applied to sales across the EU.

        - `standard`
          Standard place of supply scheme in which tax is applied to sales in this country only.

  - `country_options.fr` (object, required if country is fr)
    Options for the registration in FR.

    - `country_options.fr.type` (enum, required)
      Type of registration to be created in an EU country.
Possible enum values:
      - `ioss`
        Common for businesses shipping goods below EUR 150 from non-EU countries to EU customers.

      - `oss_non_union`
        Common for businesses established outside of the EU selling services to customers in the EU.

      - `oss_union`
        Common for businesses established in the EU selling goods and services to customers in the EU.

      - `standard`
        Common for businesses selling goods and services to customers in this country.

    - `country_options.fr.standard` (object, required if type is standard)
      Options for the standard registration.

      - `country_options.fr.standard.place_of_supply_scheme` (enum, required)
        Place of supply scheme used in an EU standard registration.
Possible enum values:
        - `inbound_goods`
          Inbound goods place of supply scheme in which the tax is collected at destination for inbound physical goods.

        - `small_seller`
          Small seller place of supply scheme in which the seller’s tax rate is applied to sales across the EU.

        - `standard`
          Standard place of supply scheme in which tax is applied to sales in this country only.

  - `country_options.gb` (object, required if country is gb)
    Options for the registration in GB.

    - `country_options.gb.type` (enum, required)
      Type of registration to be created in `country`.
Possible enum values:
      - `standard`
        A standard Tax Registration in the specified country.

    - `country_options.gb.standard` (object, required if type is standard)
      Options for the standard registration.

      - `country_options.gb.standard.place_of_supply_scheme` (enum, optional)
        Place of supply scheme used in an standard registration.
Possible enum values:
        - `inbound_goods`
          Inbound goods place of supply scheme in which the tax is collected at destination for inbound physical goods.

        - `standard`
          Standard place of supply scheme in which tax is applied to sales in this country only.

  - `country_options.ge` (object, required if country is ge)
    Options for the registration in GE.

    - `country_options.ge.type` (enum, required)
      Type of registration to be created in `country`.
Possible enum values:
      - `simplified`
        A simplified Tax Registration in the specified country.

  - `country_options.gn` (object, required if country is gn)
    Options for the registration in GN.

    - `country_options.gn.type` (enum, required)
      Type of registration to be created in `country`.
Possible enum values:
      - `standard`
        A standard Tax Registration in the specified country.

    - `country_options.gn.standard` (object, required if type is standard)
      Options for the standard registration.

      - `country_options.gn.standard.place_of_supply_scheme` (enum, optional)
        Place of supply scheme used in an standard registration.
Possible enum values:
        - `inbound_goods`
          Inbound goods place of supply scheme in which the tax is collected at destination for inbound physical goods.

        - `standard`
          Standard place of supply scheme in which tax is applied to sales in this country only.

  - `country_options.gr` (object, required if country is gr)
    Options for the registration in GR.

    - `country_options.gr.type` (enum, required)
      Type of registration to be created in an EU country.
Possible enum values:
      - `ioss`
        Common for businesses shipping goods below EUR 150 from non-EU countries to EU customers.

      - `oss_non_union`
        Common for businesses established outside of the EU selling services to customers in the EU.

      - `oss_union`
        Common for businesses established in the EU selling goods and services to customers in the EU.

      - `standard`
        Common for businesses selling goods and services to customers in this country.

    - `country_options.gr.standard` (object, required if type is standard)
      Options for the standard registration.

      - `country_options.gr.standard.place_of_supply_scheme` (enum, required)
        Place of supply scheme used in an EU standard registration.
Possible enum values:
        - `inbound_goods`
          Inbound goods place of supply scheme in which the tax is collected at destination for inbound physical goods.

        - `small_seller`
          Small seller place of supply scheme in which the seller’s tax rate is applied to sales across the EU.

        - `standard`
          Standard place of supply scheme in which tax is applied to sales in this country only.

  - `country_options.hr` (object, required if country is hr)
    Options for the registration in HR.

    - `country_options.hr.type` (enum, required)
      Type of registration to be created in an EU country.
Possible enum values:
      - `ioss`
        Common for businesses shipping goods below EUR 150 from non-EU countries to EU customers.

      - `oss_non_union`
        Common for businesses established outside of the EU selling services to customers in the EU.

      - `oss_union`
        Common for businesses established in the EU selling goods and services to customers in the EU.

      - `standard`
        Common for businesses selling goods and services to customers in this country.

    - `country_options.hr.standard` (object, required if type is standard)
      Options for the standard registration.

      - `country_options.hr.standard.place_of_supply_scheme` (enum, required)
        Place of supply scheme used in an EU standard registration.
Possible enum values:
        - `inbound_goods`
          Inbound goods place of supply scheme in which the tax is collected at destination for inbound physical goods.

        - `small_seller`
          Small seller place of supply scheme in which the seller’s tax rate is applied to sales across the EU.

        - `standard`
          Standard place of supply scheme in which tax is applied to sales in this country only.

  - `country_options.hu` (object, required if country is hu)
    Options for the registration in HU.

    - `country_options.hu.type` (enum, required)
      Type of registration to be created in an EU country.
Possible enum values:
      - `ioss`
        Common for businesses shipping goods below EUR 150 from non-EU countries to EU customers.

      - `oss_non_union`
        Common for businesses established outside of the EU selling services to customers in the EU.

      - `oss_union`
        Common for businesses established in the EU selling goods and services to customers in the EU.

      - `standard`
        Common for businesses selling goods and services to customers in this country.

    - `country_options.hu.standard` (object, required if type is standard)
      Options for the standard registration.

      - `country_options.hu.standard.place_of_supply_scheme` (enum, required)
        Place of supply scheme used in an EU standard registration.
Possible enum values:
        - `inbound_goods`
          Inbound goods place of supply scheme in which the tax is collected at destination for inbound physical goods.

        - `small_seller`
          Small seller place of supply scheme in which the seller’s tax rate is applied to sales across the EU.

        - `standard`
          Standard place of supply scheme in which tax is applied to sales in this country only.

  - `country_options.id` (object, required if country is id)
    Options for the registration in ID.

    - `country_options.id.type` (enum, required)
      Type of registration to be created in `country`.
Possible enum values:
      - `simplified`
        A simplified Tax Registration in the specified country.

  - `country_options.ie` (object, required if country is ie)
    Options for the registration in IE.

    - `country_options.ie.type` (enum, required)
      Type of registration to be created in an EU country.
Possible enum values:
      - `ioss`
        Common for businesses shipping goods below EUR 150 from non-EU countries to EU customers.

      - `oss_non_union`
        Common for businesses established outside of the EU selling services to customers in the EU.

      - `oss_union`
        Common for businesses established in the EU selling goods and services to customers in the EU.

      - `standard`
        Common for businesses selling goods and services to customers in this country.

    - `country_options.ie.standard` (object, required if type is standard)
      Options for the standard registration.

      - `country_options.ie.standard.place_of_supply_scheme` (enum, required)
        Place of supply scheme used in an EU standard registration.
Possible enum values:
        - `inbound_goods`
          Inbound goods place of supply scheme in which the tax is collected at destination for inbound physical goods.

        - `small_seller`
          Small seller place of supply scheme in which the seller’s tax rate is applied to sales across the EU.

        - `standard`
          Standard place of supply scheme in which tax is applied to sales in this country only.

  - `country_options.in` (object, required if country is in)
    Options for the registration in IN.

    - `country_options.in.type` (enum, required)
      Type of registration to be created in `country`.
Possible enum values:
      - `simplified`
        A simplified Tax Registration in the specified country.

  - `country_options.is` (object, required if country is is)
    Options for the registration in IS.

    - `country_options.is.type` (enum, required)
      Type of registration to be created in `country`.
Possible enum values:
      - `standard`
        A standard Tax Registration in the specified country.

    - `country_options.is.standard` (object, required if type is standard)
      Options for the standard registration.

      - `country_options.is.standard.place_of_supply_scheme` (enum, optional)
        Place of supply scheme used in an standard registration.
Possible enum values:
        - `inbound_goods`
          Inbound goods place of supply scheme in which the tax is collected at destination for inbound physical goods.

        - `standard`
          Standard place of supply scheme in which tax is applied to sales in this country only.

  - `country_options.it` (object, required if country is it)
    Options for the registration in IT.

    - `country_options.it.type` (enum, required)
      Type of registration to be created in an EU country.
Possible enum values:
      - `ioss`
        Common for businesses shipping goods below EUR 150 from non-EU countries to EU customers.

      - `oss_non_union`
        Common for businesses established outside of the EU selling services to customers in the EU.

      - `oss_union`
        Common for businesses established in the EU selling goods and services to customers in the EU.

      - `standard`
        Common for businesses selling goods and services to customers in this country.

    - `country_options.it.standard` (object, required if type is standard)
      Options for the standard registration.

      - `country_options.it.standard.place_of_supply_scheme` (enum, required)
        Place of supply scheme used in an EU standard registration.
Possible enum values:
        - `inbound_goods`
          Inbound goods place of supply scheme in which the tax is collected at destination for inbound physical goods.

        - `small_seller`
          Small seller place of supply scheme in which the seller’s tax rate is applied to sales across the EU.

        - `standard`
          Standard place of supply scheme in which tax is applied to sales in this country only.

  - `country_options.jp` (object, required if country is jp)
    Options for the registration in JP.

    - `country_options.jp.type` (enum, required)
      Type of registration to be created in `country`.
Possible enum values:
      - `standard`
        A standard Tax Registration in the specified country.

    - `country_options.jp.standard` (object, required if type is standard)
      Options for the standard registration.

      - `country_options.jp.standard.place_of_supply_scheme` (enum, optional)
        Place of supply scheme used in an standard registration.
Possible enum values:
        - `inbound_goods`
          Inbound goods place of supply scheme in which the tax is collected at destination for inbound physical goods.

        - `standard`
          Standard place of supply scheme in which tax is applied to sales in this country only.

  - `country_options.ke` (object, required if country is ke)
    Options for the registration in KE.

    - `country_options.ke.type` (enum, required)
      Type of registration to be created in `country`.
Possible enum values:
      - `simplified`
        A simplified Tax Registration in the specified country.

  - `country_options.kg` (object, required if country is kg)
    Options for the registration in KG.

    - `country_options.kg.type` (enum, required)
      Type of registration to be created in `country`.
Possible enum values:
      - `simplified`
        A simplified Tax Registration in the specified country.

  - `country_options.kh` (object, required if country is kh)
    Options for the registration in KH.

    - `country_options.kh.type` (enum, required)
      Type of registration to be created in `country`.
Possible enum values:
      - `simplified`
        A simplified Tax Registration in the specified country.

  - `country_options.kr` (object, required if country is kr)
    Options for the registration in KR.

    - `country_options.kr.type` (enum, required)
      Type of registration to be created in `country`.
Possible enum values:
      - `simplified`
        A simplified Tax Registration in the specified country.

  - `country_options.kz` (object, required if country is kz)
    Options for the registration in KZ.

    - `country_options.kz.type` (enum, required)
      Type of registration to be created in `country`.
Possible enum values:
      - `simplified`
        A simplified Tax Registration in the specified country.

  - `country_options.la` (object, required if country is la)
    Options for the registration in LA.

    - `country_options.la.type` (enum, required)
      Type of registration to be created in `country`.
Possible enum values:
      - `simplified`
        A simplified Tax Registration in the specified country.

  - `country_options.lt` (object, required if country is lt)
    Options for the registration in LT.

    - `country_options.lt.type` (enum, required)
      Type of registration to be created in an EU country.
Possible enum values:
      - `ioss`
        Common for businesses shipping goods below EUR 150 from non-EU countries to EU customers.

      - `oss_non_union`
        Common for businesses established outside of the EU selling services to customers in the EU.

      - `oss_union`
        Common for businesses established in the EU selling goods and services to customers in the EU.

      - `standard`
        Common for businesses selling goods and services to customers in this country.

    - `country_options.lt.standard` (object, required if type is standard)
      Options for the standard registration.

      - `country_options.lt.standard.place_of_supply_scheme` (enum, required)
        Place of supply scheme used in an EU standard registration.
Possible enum values:
        - `inbound_goods`
          Inbound goods place of supply scheme in which the tax is collected at destination for inbound physical goods.

        - `small_seller`
          Small seller place of supply scheme in which the seller’s tax rate is applied to sales across the EU.

        - `standard`
          Standard place of supply scheme in which tax is applied to sales in this country only.

  - `country_options.lu` (object, required if country is lu)
    Options for the registration in LU.

    - `country_options.lu.type` (enum, required)
      Type of registration to be created in an EU country.
Possible enum values:
      - `ioss`
        Common for businesses shipping goods below EUR 150 from non-EU countries to EU customers.

      - `oss_non_union`
        Common for businesses established outside of the EU selling services to customers in the EU.

      - `oss_union`
        Common for businesses established in the EU selling goods and services to customers in the EU.

      - `standard`
        Common for businesses selling goods and services to customers in this country.

    - `country_options.lu.standard` (object, required if type is standard)
      Options for the standard registration.

      - `country_options.lu.standard.place_of_supply_scheme` (enum, required)
        Place of supply scheme used in an EU standard registration.
Possible enum values:
        - `inbound_goods`
          Inbound goods place of supply scheme in which the tax is collected at destination for inbound physical goods.

        - `small_seller`
          Small seller place of supply scheme in which the seller’s tax rate is applied to sales across the EU.

        - `standard`
          Standard place of supply scheme in which tax is applied to sales in this country only.

  - `country_options.lv` (object, required if country is lv)
    Options for the registration in LV.

    - `country_options.lv.type` (enum, required)
      Type of registration to be created in an EU country.
Possible enum values:
      - `ioss`
        Common for businesses shipping goods below EUR 150 from non-EU countries to EU customers.

      - `oss_non_union`
        Common for businesses established outside of the EU selling services to customers in the EU.

      - `oss_union`
        Common for businesses established in the EU selling goods and services to customers in the EU.

      - `standard`
        Common for businesses selling goods and services to customers in this country.

    - `country_options.lv.standard` (object, required if type is standard)
      Options for the standard registration.

      - `country_options.lv.standard.place_of_supply_scheme` (enum, required)
        Place of supply scheme used in an EU standard registration.
Possible enum values:
        - `inbound_goods`
          Inbound goods place of supply scheme in which the tax is collected at destination for inbound physical goods.

        - `small_seller`
          Small seller place of supply scheme in which the seller’s tax rate is applied to sales across the EU.

        - `standard`
          Standard place of supply scheme in which tax is applied to sales in this country only.

  - `country_options.ma` (object, required if country is ma)
    Options for the registration in MA.

    - `country_options.ma.type` (enum, required)
      Type of registration to be created in `country`.
Possible enum values:
      - `simplified`
        A simplified Tax Registration in the specified country.

  - `country_options.md` (object, required if country is md)
    Options for the registration in MD.

    - `country_options.md.type` (enum, required)
      Type of registration to be created in `country`.
Possible enum values:
      - `simplified`
        A simplified Tax Registration in the specified country.

  - `country_options.me` (object, required if country is me)
    Options for the registration in ME.

    - `country_options.me.type` (enum, required)
      Type of registration to be created in `country`.
Possible enum values:
      - `standard`
        A standard Tax Registration in the specified country.

    - `country_options.me.standard` (object, required if type is standard)
      Options for the standard registration.

      - `country_options.me.standard.place_of_supply_scheme` (enum, optional)
        Place of supply scheme used in an standard registration.
Possible enum values:
        - `inbound_goods`
          Inbound goods place of supply scheme in which the tax is collected at destination for inbound physical goods.

        - `standard`
          Standard place of supply scheme in which tax is applied to sales in this country only.

  - `country_options.mk` (object, required if country is mk)
    Options for the registration in MK.

    - `country_options.mk.type` (enum, required)
      Type of registration to be created in `country`.
Possible enum values:
      - `standard`
        A standard Tax Registration in the specified country.

    - `country_options.mk.standard` (object, required if type is standard)
      Options for the standard registration.

      - `country_options.mk.standard.place_of_supply_scheme` (enum, optional)
        Place of supply scheme used in an standard registration.
Possible enum values:
        - `inbound_goods`
          Inbound goods place of supply scheme in which the tax is collected at destination for inbound physical goods.

        - `standard`
          Standard place of supply scheme in which tax is applied to sales in this country only.

  - `country_options.mr` (object, required if country is mr)
    Options for the registration in MR.

    - `country_options.mr.type` (enum, required)
      Type of registration to be created in `country`.
Possible enum values:
      - `standard`
        A standard Tax Registration in the specified country.

    - `country_options.mr.standard` (object, required if type is standard)
      Options for the standard registration.

      - `country_options.mr.standard.place_of_supply_scheme` (enum, optional)
        Place of supply scheme used in an standard registration.
Possible enum values:
        - `inbound_goods`
          Inbound goods place of supply scheme in which the tax is collected at destination for inbound physical goods.

        - `standard`
          Standard place of supply scheme in which tax is applied to sales in this country only.

  - `country_options.mt` (object, required if country is mt)
    Options for the registration in MT.

    - `country_options.mt.type` (enum, required)
      Type of registration to be created in an EU country.
Possible enum values:
      - `ioss`
        Common for businesses shipping goods below EUR 150 from non-EU countries to EU customers.

      - `oss_non_union`
        Common for businesses established outside of the EU selling services to customers in the EU.

      - `oss_union`
        Common for businesses established in the EU selling goods and services to customers in the EU.

      - `standard`
        Common for businesses selling goods and services to customers in this country.

    - `country_options.mt.standard` (object, required if type is standard)
      Options for the standard registration.

      - `country_options.mt.standard.place_of_supply_scheme` (enum, required)
        Place of supply scheme used in an EU standard registration.
Possible enum values:
        - `inbound_goods`
          Inbound goods place of supply scheme in which the tax is collected at destination for inbound physical goods.

        - `small_seller`
          Small seller place of supply scheme in which the seller’s tax rate is applied to sales across the EU.

        - `standard`
          Standard place of supply scheme in which tax is applied to sales in this country only.

  - `country_options.mx` (object, required if country is mx)
    Options for the registration in MX.

    - `country_options.mx.type` (enum, required)
      Type of registration to be created in `country`.
Possible enum values:
      - `simplified`
        A simplified Tax Registration in the specified country.

  - `country_options.my` (object, required if country is my)
    Options for the registration in MY.

    - `country_options.my.type` (enum, required)
      Type of registration to be created in `country`.
Possible enum values:
      - `simplified`
        A simplified Tax Registration in the specified country.

  - `country_options.ng` (object, required if country is ng)
    Options for the registration in NG.

    - `country_options.ng.type` (enum, required)
      Type of registration to be created in `country`.
Possible enum values:
      - `simplified`
        A simplified Tax Registration in the specified country.

  - `country_options.nl` (object, required if country is nl)
    Options for the registration in NL.

    - `country_options.nl.type` (enum, required)
      Type of registration to be created in an EU country.
Possible enum values:
      - `ioss`
        Common for businesses shipping goods below EUR 150 from non-EU countries to EU customers.

      - `oss_non_union`
        Common for businesses established outside of the EU selling services to customers in the EU.

      - `oss_union`
        Common for businesses established in the EU selling goods and services to customers in the EU.

      - `standard`
        Common for businesses selling goods and services to customers in this country.

    - `country_options.nl.standard` (object, required if type is standard)
      Options for the standard registration.

      - `country_options.nl.standard.place_of_supply_scheme` (enum, required)
        Place of supply scheme used in an EU standard registration.
Possible enum values:
        - `inbound_goods`
          Inbound goods place of supply scheme in which the tax is collected at destination for inbound physical goods.

        - `small_seller`
          Small seller place of supply scheme in which the seller’s tax rate is applied to sales across the EU.

        - `standard`
          Standard place of supply scheme in which tax is applied to sales in this country only.

  - `country_options.no` (object, required if country is no)
    Options for the registration in NO.

    - `country_options.no.type` (enum, required)
      Type of registration to be created in `country`.
Possible enum values:
      - `standard`
        A standard Tax Registration in the specified country.

    - `country_options.no.standard` (object, required if type is standard)
      Options for the standard registration.

      - `country_options.no.standard.place_of_supply_scheme` (enum, optional)
        Place of supply scheme used in an standard registration.
Possible enum values:
        - `inbound_goods`
          Inbound goods place of supply scheme in which the tax is collected at destination for inbound physical goods.

        - `standard`
          Standard place of supply scheme in which tax is applied to sales in this country only.

  - `country_options.np` (object, required if country is np)
    Options for the registration in NP.

    - `country_options.np.type` (enum, required)
      Type of registration to be created in `country`.
Possible enum values:
      - `simplified`
        A simplified Tax Registration in the specified country.

  - `country_options.nz` (object, required if country is nz)
    Options for the registration in NZ.

    - `country_options.nz.type` (enum, required)
      Type of registration to be created in `country`.
Possible enum values:
      - `standard`
        A standard Tax Registration in the specified country.

    - `country_options.nz.standard` (object, required if type is standard)
      Options for the standard registration.

      - `country_options.nz.standard.place_of_supply_scheme` (enum, optional)
        Place of supply scheme used in an standard registration.
Possible enum values:
        - `inbound_goods`
          Inbound goods place of supply scheme in which the tax is collected at destination for inbound physical goods.

        - `standard`
          Standard place of supply scheme in which tax is applied to sales in this country only.

  - `country_options.om` (object, required if country is om)
    Options for the registration in OM.

    - `country_options.om.type` (enum, required)
      Type of registration to be created in `country`.
Possible enum values:
      - `standard`
        A standard Tax Registration in the specified country.

    - `country_options.om.standard` (object, required if type is standard)
      Options for the standard registration.

      - `country_options.om.standard.place_of_supply_scheme` (enum, optional)
        Place of supply scheme used in an standard registration.
Possible enum values:
        - `inbound_goods`
          Inbound goods place of supply scheme in which the tax is collected at destination for inbound physical goods.

        - `standard`
          Standard place of supply scheme in which tax is applied to sales in this country only.

  - `country_options.pe` (object, required if country is pe)
    Options for the registration in PE.

    - `country_options.pe.type` (enum, required)
      Type of registration to be created in `country`.
Possible enum values:
      - `simplified`
        A simplified Tax Registration in the specified country.

  - `country_options.ph` (object, required if country is ph)
    Options for the registration in PH.

    - `country_options.ph.type` (enum, required)
      Type of registration to be created in `country`.
Possible enum values:
      - `simplified`
        A simplified Tax Registration in the specified country.

  - `country_options.pl` (object, required if country is pl)
    Options for the registration in PL.

    - `country_options.pl.type` (enum, required)
      Type of registration to be created in an EU country.
Possible enum values:
      - `ioss`
        Common for businesses shipping goods below EUR 150 from non-EU countries to EU customers.

      - `oss_non_union`
        Common for businesses established outside of the EU selling services to customers in the EU.

      - `oss_union`
        Common for businesses established in the EU selling goods and services to customers in the EU.

      - `standard`
        Common for businesses selling goods and services to customers in this country.

    - `country_options.pl.standard` (object, required if type is standard)
      Options for the standard registration.

      - `country_options.pl.standard.place_of_supply_scheme` (enum, required)
        Place of supply scheme used in an EU standard registration.
Possible enum values:
        - `inbound_goods`
          Inbound goods place of supply scheme in which the tax is collected at destination for inbound physical goods.

        - `small_seller`
          Small seller place of supply scheme in which the seller’s tax rate is applied to sales across the EU.

        - `standard`
          Standard place of supply scheme in which tax is applied to sales in this country only.

  - `country_options.pt` (object, required if country is pt)
    Options for the registration in PT.

    - `country_options.pt.type` (enum, required)
      Type of registration to be created in an EU country.
Possible enum values:
      - `ioss`
        Common for businesses shipping goods below EUR 150 from non-EU countries to EU customers.

      - `oss_non_union`
        Common for businesses established outside of the EU selling services to customers in the EU.

      - `oss_union`
        Common for businesses established in the EU selling goods and services to customers in the EU.

      - `standard`
        Common for businesses selling goods and services to customers in this country.

    - `country_options.pt.standard` (object, required if type is standard)
      Options for the standard registration.

      - `country_options.pt.standard.place_of_supply_scheme` (enum, required)
        Place of supply scheme used in an EU standard registration.
Possible enum values:
        - `inbound_goods`
          Inbound goods place of supply scheme in which the tax is collected at destination for inbound physical goods.

        - `small_seller`
          Small seller place of supply scheme in which the seller’s tax rate is applied to sales across the EU.

        - `standard`
          Standard place of supply scheme in which tax is applied to sales in this country only.

  - `country_options.ro` (object, required if country is ro)
    Options for the registration in RO.

    - `country_options.ro.type` (enum, required)
      Type of registration to be created in an EU country.
Possible enum values:
      - `ioss`
        Common for businesses shipping goods below EUR 150 from non-EU countries to EU customers.

      - `oss_non_union`
        Common for businesses established outside of the EU selling services to customers in the EU.

      - `oss_union`
        Common for businesses established in the EU selling goods and services to customers in the EU.

      - `standard`
        Common for businesses selling goods and services to customers in this country.

    - `country_options.ro.standard` (object, required if type is standard)
      Options for the standard registration.

      - `country_options.ro.standard.place_of_supply_scheme` (enum, required)
        Place of supply scheme used in an EU standard registration.
Possible enum values:
        - `inbound_goods`
          Inbound goods place of supply scheme in which the tax is collected at destination for inbound physical goods.

        - `small_seller`
          Small seller place of supply scheme in which the seller’s tax rate is applied to sales across the EU.

        - `standard`
          Standard place of supply scheme in which tax is applied to sales in this country only.

  - `country_options.rs` (object, required if country is rs)
    Options for the registration in RS.

    - `country_options.rs.type` (enum, required)
      Type of registration to be created in `country`.
Possible enum values:
      - `standard`
        A standard Tax Registration in the specified country.

    - `country_options.rs.standard` (object, required if type is standard)
      Options for the standard registration.

      - `country_options.rs.standard.place_of_supply_scheme` (enum, optional)
        Place of supply scheme used in an standard registration.
Possible enum values:
        - `inbound_goods`
          Inbound goods place of supply scheme in which the tax is collected at destination for inbound physical goods.

        - `standard`
          Standard place of supply scheme in which tax is applied to sales in this country only.

  - `country_options.ru` (object, required if country is ru)
    Options for the registration in RU.

    - `country_options.ru.type` (enum, required)
      Type of registration to be created in `country`.
Possible enum values:
      - `simplified`
        A simplified Tax Registration in the specified country.

  - `country_options.sa` (object, required if country is sa)
    Options for the registration in SA.

    - `country_options.sa.type` (enum, required)
      Type of registration to be created in `country`.
Possible enum values:
      - `simplified`
        A simplified Tax Registration in the specified country.

  - `country_options.se` (object, required if country is se)
    Options for the registration in SE.

    - `country_options.se.type` (enum, required)
      Type of registration to be created in an EU country.
Possible enum values:
      - `ioss`
        Common for businesses shipping goods below EUR 150 from non-EU countries to EU customers.

      - `oss_non_union`
        Common for businesses established outside of the EU selling services to customers in the EU.

      - `oss_union`
        Common for businesses established in the EU selling goods and services to customers in the EU.

      - `standard`
        Common for businesses selling goods and services to customers in this country.

    - `country_options.se.standard` (object, required if type is standard)
      Options for the standard registration.

      - `country_options.se.standard.place_of_supply_scheme` (enum, required)
        Place of supply scheme used in an EU standard registration.
Possible enum values:
        - `inbound_goods`
          Inbound goods place of supply scheme in which the tax is collected at destination for inbound physical goods.

        - `small_seller`
          Small seller place of supply scheme in which the seller’s tax rate is applied to sales across the EU.

        - `standard`
          Standard place of supply scheme in which tax is applied to sales in this country only.

  - `country_options.sg` (object, required if country is sg)
    Options for the registration in SG.

    - `country_options.sg.type` (enum, required)
      Type of registration to be created in `country`.
Possible enum values:
      - `standard`
        A standard Tax Registration in the specified country.

    - `country_options.sg.standard` (object, required if type is standard)
      Options for the standard registration.

      - `country_options.sg.standard.place_of_supply_scheme` (enum, optional)
        Place of supply scheme used in an standard registration.
Possible enum values:
        - `inbound_goods`
          Inbound goods place of supply scheme in which the tax is collected at destination for inbound physical goods.

        - `standard`
          Standard place of supply scheme in which tax is applied to sales in this country only.

  - `country_options.si` (object, required if country is si)
    Options for the registration in SI.

    - `country_options.si.type` (enum, required)
      Type of registration to be created in an EU country.
Possible enum values:
      - `ioss`
        Common for businesses shipping goods below EUR 150 from non-EU countries to EU customers.

      - `oss_non_union`
        Common for businesses established outside of the EU selling services to customers in the EU.

      - `oss_union`
        Common for businesses established in the EU selling goods and services to customers in the EU.

      - `standard`
        Common for businesses selling goods and services to customers in this country.

    - `country_options.si.standard` (object, required if type is standard)
      Options for the standard registration.

      - `country_options.si.standard.place_of_supply_scheme` (enum, required)
        Place of supply scheme used in an EU standard registration.
Possible enum values:
        - `inbound_goods`
          Inbound goods place of supply scheme in which the tax is collected at destination for inbound physical goods.

        - `small_seller`
          Small seller place of supply scheme in which the seller’s tax rate is applied to sales across the EU.

        - `standard`
          Standard place of supply scheme in which tax is applied to sales in this country only.

  - `country_options.sk` (object, required if country is sk)
    Options for the registration in SK.

    - `country_options.sk.type` (enum, required)
      Type of registration to be created in an EU country.
Possible enum values:
      - `ioss`
        Common for businesses shipping goods below EUR 150 from non-EU countries to EU customers.

      - `oss_non_union`
        Common for businesses established outside of the EU selling services to customers in the EU.

      - `oss_union`
        Common for businesses established in the EU selling goods and services to customers in the EU.

      - `standard`
        Common for businesses selling goods and services to customers in this country.

    - `country_options.sk.standard` (object, required if type is standard)
      Options for the standard registration.

      - `country_options.sk.standard.place_of_supply_scheme` (enum, required)
        Place of supply scheme used in an EU standard registration.
Possible enum values:
        - `inbound_goods`
          Inbound goods place of supply scheme in which the tax is collected at destination for inbound physical goods.

        - `small_seller`
          Small seller place of supply scheme in which the seller’s tax rate is applied to sales across the EU.

        - `standard`
          Standard place of supply scheme in which tax is applied to sales in this country only.

  - `country_options.sn` (object, required if country is sn)
    Options for the registration in SN.

    - `country_options.sn.type` (enum, required)
      Type of registration to be created in `country`.
Possible enum values:
      - `simplified`
        A simplified Tax Registration in the specified country.

  - `country_options.sr` (object, required if country is sr)
    Options for the registration in SR.

    - `country_options.sr.type` (enum, required)
      Type of registration to be created in `country`.
Possible enum values:
      - `standard`
        A standard Tax Registration in the specified country.

    - `country_options.sr.standard` (object, required if type is standard)
      Options for the standard registration.

      - `country_options.sr.standard.place_of_supply_scheme` (enum, optional)
        Place of supply scheme used in an standard registration.
Possible enum values:
        - `inbound_goods`
          Inbound goods place of supply scheme in which the tax is collected at destination for inbound physical goods.

        - `standard`
          Standard place of supply scheme in which tax is applied to sales in this country only.

  - `country_options.th` (object, required if country is TH)
    Options for the registration in TH.

    - `country_options.th.type` (enum, required)
      Type of registration to be created in `country`.
Possible enum values:
      - `simplified`
        A simplified Tax Registration in Thailand to collect VAT.

  - `country_options.tj` (object, required if country is tj)
    Options for the registration in TJ.

    - `country_options.tj.type` (enum, required)
      Type of registration to be created in `country`.
Possible enum values:
      - `simplified`
        A simplified Tax Registration in the specified country.

  - `country_options.tr` (object, required if country is tr)
    Options for the registration in TR.

    - `country_options.tr.type` (enum, required)
      Type of registration to be created in `country`.
Possible enum values:
      - `simplified`
        A simplified Tax Registration in the specified country.

  - `country_options.tw` (object, required if country is tw)
    Options for the registration in TW.

    - `country_options.tw.type` (enum, required)
      Type of registration to be created in `country`.
Possible enum values:
      - `simplified`
        A simplified Tax Registration in the specified country.

  - `country_options.tz` (object, required if country is tz)
    Options for the registration in TZ.

    - `country_options.tz.type` (enum, required)
      Type of registration to be created in `country`.
Possible enum values:
      - `simplified`
        A simplified Tax Registration in the specified country.

  - `country_options.ua` (object, required if country is ua)
    Options for the registration in UA.

    - `country_options.ua.type` (enum, required)
      Type of registration to be created in `country`.
Possible enum values:
      - `simplified`
        A simplified Tax Registration in the specified country.

  - `country_options.ug` (object, required if country is ug)
    Options for the registration in UG.

    - `country_options.ug.type` (enum, required)
      Type of registration to be created in `country`.
Possible enum values:
      - `simplified`
        A simplified Tax Registration in the specified country.

  - `country_options.us` (object, required if country is US)
    Options for the registration in US.

    - `country_options.us.state` (string, required)
      Two-letter US state code ([ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2)).

    - `country_options.us.type` (enum, required)
      Type of registration to be created in the US.
Possible enum values:
      - `local_amusement_tax`
        A Tax Registration in the specified US state to collect local amusement tax.

      - `local_lease_tax`
        A Tax Registration in the specified US state to collect local lease tax.

      - `state_communications_tax`
        A Tax Registration in the specified US state to collect communications tax.

      - `state_retail_delivery_fee`
        A Tax Registration in the specified US state to collect state retail delivery fee.

      - `state_sales_tax`
        A Tax Registration in the specified US state to collect sales tax.

    - `country_options.us.local_amusement_tax` (object, required if type is local_amusement_tax)
      Options for the local amusement tax registration.

      - `country_options.us.local_amusement_tax.jurisdiction` (string, required)
        A [FIPS code](https://www.census.gov/library/reference/code-lists/ansi.html) representing the local jurisdiction. Supported FIPS codes are: `14000` (Chicago), `02154` (Arlington Heights), `06613` (Bloomington), `10906` (Campton Hills), `21696` (East Dundee), `24582` (Evanston), `45421` (Lynwood), `48892` (Midlothian), `64343` (River Grove), and `68081` (Schiller Park).

    - `country_options.us.local_lease_tax` (object, required if type is local_lease_tax)
      Options for the local lease tax registration.

      - `country_options.us.local_lease_tax.jurisdiction` (string, required)
        A [FIPS code](https://www.census.gov/library/reference/code-lists/ansi.html) representing the local jurisdiction. Supported FIPS codes are: `14000` (Chicago).

    - `country_options.us.state_sales_tax` (object, optional)
      Options for the state sales tax registration.

      - `country_options.us.state_sales_tax.elections` (array of objects, required)
        Elections for the state sales tax registration.

        - `country_options.us.state_sales_tax.elections.type` (enum, required)
          The type of the election for the state sales tax registration.
Possible enum values:
          - `local_use_tax`
            Use Tax in Pennsylvania for the city of Philadelphia or Allegheny county which can be collected by remote sellers outside of these locations.

          - `simplified_sellers_use_tax`
            Simplified Sellers Use Tax which can be collected by remote sellers with no physical presence in Alabama.

          - `single_local_use_tax`
            Single Local Use Tax Rate which can be collected by remote sellers with no physical presence in Texas.

        - `country_options.us.state_sales_tax.elections.jurisdiction` (string, required if type is local_use_tax)
          A [FIPS code](https://www.census.gov/library/reference/code-lists/ansi.html) representing the local jurisdiction. Supported FIPS codes are: `003` (Allegheny County) and `60000` (Philadelphia City).

  - `country_options.uy` (object, required if country is uy)
    Options for the registration in UY.

    - `country_options.uy.type` (enum, required)
      Type of registration to be created in `country`.
Possible enum values:
      - `standard`
        A standard Tax Registration in the specified country.

    - `country_options.uy.standard` (object, required if type is standard)
      Options for the standard registration.

      - `country_options.uy.standard.place_of_supply_scheme` (enum, optional)
        Place of supply scheme used in an standard registration.
Possible enum values:
        - `inbound_goods`
          Inbound goods place of supply scheme in which the tax is collected at destination for inbound physical goods.

        - `standard`
          Standard place of supply scheme in which tax is applied to sales in this country only.

  - `country_options.uz` (object, required if country is uz)
    Options for the registration in UZ.

    - `country_options.uz.type` (enum, required)
      Type of registration to be created in `country`.
Possible enum values:
      - `simplified`
        A simplified Tax Registration in the specified country.

  - `country_options.vn` (object, required if country is vn)
    Options for the registration in VN.

    - `country_options.vn.type` (enum, required)
      Type of registration to be created in `country`.
Possible enum values:
      - `simplified`
        A simplified Tax Registration in the specified country.

  - `country_options.za` (object, required if country is za)
    Options for the registration in ZA.

    - `country_options.za.type` (enum, required)
      Type of registration to be created in `country`.
Possible enum values:
      - `standard`
        A standard Tax Registration in the specified country.

    - `country_options.za.standard` (object, required if type is standard)
      Options for the standard registration.

      - `country_options.za.standard.place_of_supply_scheme` (enum, optional)
        Place of supply scheme used in an standard registration.
Possible enum values:
        - `inbound_goods`
          Inbound goods place of supply scheme in which the tax is collected at destination for inbound physical goods.

        - `standard`
          Standard place of supply scheme in which tax is applied to sales in this country only.

  - `country_options.zm` (object, required if country is zm)
    Options for the registration in ZM.

    - `country_options.zm.type` (enum, required)
      Type of registration to be created in `country`.
Possible enum values:
      - `simplified`
        A simplified Tax Registration in the specified country.

  - `country_options.zw` (object, required if country is zw)
    Options for the registration in ZW.

    - `country_options.zw.type` (enum, required)
      Type of registration to be created in `country`.
Possible enum values:
      - `standard`
        A standard Tax Registration in the specified country.

    - `country_options.zw.standard` (object, required if type is standard)
      Options for the standard registration.

      - `country_options.zw.standard.place_of_supply_scheme` (enum, optional)
        Place of supply scheme used in an standard registration.
Possible enum values:
        - `inbound_goods`
          Inbound goods place of supply scheme in which the tax is collected at destination for inbound physical goods.

        - `standard`
          Standard place of supply scheme in which tax is applied to sales in this country only.

- `expires_at` (timestamp, optional)
  If set, the Tax Registration stops being active at this time. If not set, the Tax Registration will be active indefinitely. Timestamp measured in seconds since the Unix epoch.

```curl
curl https://api.stripe.com/v1/tax/registrations \
  -u "<<YOUR_SECRET_KEY>>" \
  -d country=US \
  -d "country_options[us][state]"=CA \
  -d "country_options[us][type]"=state_sales_tax \
  -d active_from=now
```

```cli
stripe tax registrations create  \
  --country=US \
  -d "country_options[us][state]"=CA \
  -d "country_options[us][type]"=state_sales_tax \
  --active-from=now
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

registration = client.v1.tax.registrations.create({
  country: 'US',
  country_options: {
    us: {
      state: 'CA',
      type: 'state_sales_tax',
    },
  },
  active_from: 'now',
})
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

registration = client.v1.tax.registrations.create({
  "country": "US",
  "country_options": {"us": {"state": "CA", "type": "state_sales_tax"}},
  "active_from": "now",
})
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$registration = $stripe->tax->registrations->create([
  'country' => 'US',
  'country_options' => [
    'us' => [
      'state' => 'CA',
      'type' => 'state_sales_tax',
    ],
  ],
  'active_from' => 'now',
]);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

RegistrationCreateParams params =
  RegistrationCreateParams.builder()
    .setCountry("US")
    .setCountryOptions(
      RegistrationCreateParams.CountryOptions.builder()
        .setUs(
          RegistrationCreateParams.CountryOptions.Us.builder()
            .setState("CA")
            .setType(RegistrationCreateParams.CountryOptions.Us.Type.STATE_SALES_TAX)
            .build()
        )
        .build()
    )
    .setActiveFrom(RegistrationCreateParams.ActiveFrom.NOW)
    .build();

Registration registration = client.v1().tax().registrations().create(params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const registration = await stripe.tax.registrations.create({
  country: 'US',
  country_options: {
    us: {
      state: 'CA',
      type: 'state_sales_tax',
    },
  },
  active_from: 'now',
});
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.TaxRegistrationCreateParams{
  Country: stripe.String("US"),
  CountryOptions: &stripe.TaxRegistrationCreateCountryOptionsParams{
    US: &stripe.TaxRegistrationCreateCountryOptionsUSParams{
      State: stripe.String("CA"),
      Type: stripe.String(stripe.TaxRegistrationCountryOptionsUSTypeStateSalesTax),
    },
  },
  ActiveFromNow: stripe.Bool(true),
}
result, err := sc.V1TaxRegistrations.Create(context.TODO(), params)
```

```dotnet
var options = new Stripe.Tax.RegistrationCreateOptions
{
    Country = "US",
    CountryOptions = new Stripe.Tax.RegistrationCountryOptionsOptions
    {
        Us = new Stripe.Tax.RegistrationCountryOptionsUsOptions
        {
            State = "CA",
            Type = "state_sales_tax",
        },
    },
    ActiveFrom = Stripe.Tax.RegistrationActiveFrom.Now,
};
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Tax.Registrations;
Stripe.Tax.Registration registration = service.Create(options);
```

### Response

```json
{
  "id": "taxreg_NkyGPRPytKq66j",
  "object": "tax.registration",
  "active_from": 1682036640,
  "country": "US",
  "country_options": {
    "us": {
      "state": "CA",
      "type": "state_sales_tax"
    }
  },
  "created": 1682006400,
  "expires_at": null,
  "livemode": false,
  "status": "active",
  "state": "CA",
  "type": "standard"
}
```