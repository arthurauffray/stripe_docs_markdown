# The Tax Registration object

## Attributes

- `id` (string)
  Unique identifier for the object.

- `object` (string)
  String representing the object’s type. Objects of the same type share the same value.

- `active_from` (timestamp)
  Time at which the registration becomes active. Measured in seconds since the Unix epoch.

- `country` (string)
  Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

- `country_options` (object)
  Specific options for a registration in the specified `country`.

  - `country_options.id` (object, nullable)
    Options for the registration in ID.

    - `country_options.id.type` (enum)
      Type of registration in `country`.
Possible enum values:
      - `simplified`
        A simplified Tax Registration in the specified country.

  - `country_options.ae` (object, nullable)
    Options for the registration in AE.

    - `country_options.ae.standard` (object, nullable)
      Options for the standard registration.

      - `country_options.ae.standard.place_of_supply_scheme` (enum)
        Place of supply scheme used in an Default standard registration.
Possible enum values:
        - `inbound_goods`
          Inbound goods place of supply scheme in which the tax is collected at destination for inbound physical goods.

        - `standard`
          Standard place of supply scheme in which tax is applied to sales in this country only.

    - `country_options.ae.type` (enum)
      Type of registration in `country`.
Possible enum values:
      - `standard`
        A standard Tax Registration in the specified country.

  - `country_options.al` (object, nullable)
    Options for the registration in AL.

    - `country_options.al.type` (enum)
      Type of registration in `country`.
Possible enum values:
      - `standard`
        A standard Tax Registration in the specified country.

  - `country_options.am` (object, nullable)
    Options for the registration in AM.

    - `country_options.am.type` (enum)
      Type of registration in `country`.
Possible enum values:
      - `simplified`
        A simplified Tax Registration in the specified country.

  - `country_options.ao` (object, nullable)
    Options for the registration in AO.

    - `country_options.ao.type` (enum)
      Type of registration in `country`.
Possible enum values:
      - `standard`
        A standard Tax Registration in the specified country.

  - `country_options.at` (object, nullable)
    Options for the registration in AT.

    - `country_options.at.standard` (object, nullable)
      Options for the standard registration.

      - `country_options.at.standard.place_of_supply_scheme` (enum)
        Place of supply scheme used in an EU standard registration.
Possible enum values:
        - `inbound_goods`
          Inbound goods place of supply scheme in which the tax is collected at destination for inbound physical goods.

        - `small_seller`
          Small seller place of supply scheme in which the seller’s tax rate is applied to sales across the EU.

        - `standard`
          Standard place of supply scheme in which tax is applied to sales in this country only.

    - `country_options.at.type` (enum)
      Type of registration in an EU country.
Possible enum values:
      - `ioss`
        Common for businesses shipping goods below EUR 150 from non-EU countries to EU customers.

      - `oss_non_union`
        Common for businesses established outside of the EU selling services to customers in the EU.

      - `oss_union`
        Common for businesses established in the EU selling goods and services to customers in the EU.

      - `standard`
        Common for businesses selling goods and services to customers in this country.

  - `country_options.au` (object, nullable)
    Options for the registration in AU.

    - `country_options.au.standard` (object, nullable)
      Options for the standard registration.

      - `country_options.au.standard.place_of_supply_scheme` (enum)
        Place of supply scheme used in an Default standard registration.
Possible enum values:
        - `inbound_goods`
          Inbound goods place of supply scheme in which the tax is collected at destination for inbound physical goods.

        - `standard`
          Standard place of supply scheme in which tax is applied to sales in this country only.

    - `country_options.au.type` (enum)
      Type of registration in `country`.
Possible enum values:
      - `standard`
        A standard Tax Registration in the specified country.

  - `country_options.aw` (object, nullable)
    Options for the registration in AW.

    - `country_options.aw.type` (enum)
      Type of registration in `country`.
Possible enum values:
      - `standard`
        A standard Tax Registration in the specified country.

  - `country_options.az` (object, nullable)
    Options for the registration in AZ.

    - `country_options.az.type` (enum)
      Type of registration in `country`.
Possible enum values:
      - `simplified`
        A simplified Tax Registration in the specified country.

  - `country_options.ba` (object, nullable)
    Options for the registration in BA.

    - `country_options.ba.type` (enum)
      Type of registration in `country`.
Possible enum values:
      - `standard`
        A standard Tax Registration in the specified country.

  - `country_options.bb` (object, nullable)
    Options for the registration in BB.

    - `country_options.bb.type` (enum)
      Type of registration in `country`.
Possible enum values:
      - `standard`
        A standard Tax Registration in the specified country.

  - `country_options.bd` (object, nullable)
    Options for the registration in BD.

    - `country_options.bd.type` (enum)
      Type of registration in `country`.
Possible enum values:
      - `standard`
        A standard Tax Registration in the specified country.

  - `country_options.be` (object, nullable)
    Options for the registration in BE.

    - `country_options.be.standard` (object, nullable)
      Options for the standard registration.

      - `country_options.be.standard.place_of_supply_scheme` (enum)
        Place of supply scheme used in an EU standard registration.
Possible enum values:
        - `inbound_goods`
          Inbound goods place of supply scheme in which the tax is collected at destination for inbound physical goods.

        - `small_seller`
          Small seller place of supply scheme in which the seller’s tax rate is applied to sales across the EU.

        - `standard`
          Standard place of supply scheme in which tax is applied to sales in this country only.

    - `country_options.be.type` (enum)
      Type of registration in an EU country.
Possible enum values:
      - `ioss`
        Common for businesses shipping goods below EUR 150 from non-EU countries to EU customers.

      - `oss_non_union`
        Common for businesses established outside of the EU selling services to customers in the EU.

      - `oss_union`
        Common for businesses established in the EU selling goods and services to customers in the EU.

      - `standard`
        Common for businesses selling goods and services to customers in this country.

  - `country_options.bf` (object, nullable)
    Options for the registration in BF.

    - `country_options.bf.type` (enum)
      Type of registration in `country`.
Possible enum values:
      - `standard`
        A standard Tax Registration in the specified country.

  - `country_options.bg` (object, nullable)
    Options for the registration in BG.

    - `country_options.bg.standard` (object, nullable)
      Options for the standard registration.

      - `country_options.bg.standard.place_of_supply_scheme` (enum)
        Place of supply scheme used in an EU standard registration.
Possible enum values:
        - `inbound_goods`
          Inbound goods place of supply scheme in which the tax is collected at destination for inbound physical goods.

        - `small_seller`
          Small seller place of supply scheme in which the seller’s tax rate is applied to sales across the EU.

        - `standard`
          Standard place of supply scheme in which tax is applied to sales in this country only.

    - `country_options.bg.type` (enum)
      Type of registration in an EU country.
Possible enum values:
      - `ioss`
        Common for businesses shipping goods below EUR 150 from non-EU countries to EU customers.

      - `oss_non_union`
        Common for businesses established outside of the EU selling services to customers in the EU.

      - `oss_union`
        Common for businesses established in the EU selling goods and services to customers in the EU.

      - `standard`
        Common for businesses selling goods and services to customers in this country.

  - `country_options.bh` (object, nullable)
    Options for the registration in BH.

    - `country_options.bh.type` (enum)
      Type of registration in `country`.
Possible enum values:
      - `standard`
        A standard Tax Registration in the specified country.

  - `country_options.bj` (object, nullable)
    Options for the registration in BJ.

    - `country_options.bj.type` (enum)
      Type of registration in `country`.
Possible enum values:
      - `simplified`
        A simplified Tax Registration in the specified country.

  - `country_options.bs` (object, nullable)
    Options for the registration in BS.

    - `country_options.bs.type` (enum)
      Type of registration in `country`.
Possible enum values:
      - `standard`
        A standard Tax Registration in the specified country.

  - `country_options.by` (object, nullable)
    Options for the registration in BY.

    - `country_options.by.type` (enum)
      Type of registration in `country`.
Possible enum values:
      - `simplified`
        A simplified Tax Registration in the specified country.

  - `country_options.ca` (object, nullable)
    Options for the registration in CA.

    - `country_options.ca.province_standard` (object, nullable)
      Options for the provincial tax registration.

      - `country_options.ca.province_standard.province` (string)
        Two-letter CA province code ([ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2)).

    - `country_options.ca.type` (enum)
      Type of registration in Canada.
Possible enum values:
      - `province_standard`
        A Tax Registration in the specified Canadian province to collect PST/RST/QST.

      - `simplified`
        A simplified Tax Registration in Canada to collect GST/HST.

      - `standard`
        A standard Tax Registration in Canada to collect GST/HST.

  - `country_options.cd` (object, nullable)
    Options for the registration in CD.

    - `country_options.cd.type` (enum)
      Type of registration in `country`.
Possible enum values:
      - `standard`
        A standard Tax Registration in the specified country.

  - `country_options.ch` (object, nullable)
    Options for the registration in CH.

    - `country_options.ch.standard` (object, nullable)
      Options for the standard registration.

      - `country_options.ch.standard.place_of_supply_scheme` (enum)
        Place of supply scheme used in an Default standard registration.
Possible enum values:
        - `inbound_goods`
          Inbound goods place of supply scheme in which the tax is collected at destination for inbound physical goods.

        - `standard`
          Standard place of supply scheme in which tax is applied to sales in this country only.

    - `country_options.ch.type` (enum)
      Type of registration in `country`.
Possible enum values:
      - `standard`
        A standard Tax Registration in the specified country.

  - `country_options.cl` (object, nullable)
    Options for the registration in CL.

    - `country_options.cl.type` (enum)
      Type of registration in `country`.
Possible enum values:
      - `simplified`
        A simplified Tax Registration in the specified country.

  - `country_options.cm` (object, nullable)
    Options for the registration in CM.

    - `country_options.cm.type` (enum)
      Type of registration in `country`.
Possible enum values:
      - `simplified`
        A simplified Tax Registration in the specified country.

  - `country_options.co` (object, nullable)
    Options for the registration in CO.

    - `country_options.co.type` (enum)
      Type of registration in `country`.
Possible enum values:
      - `simplified`
        A simplified Tax Registration in the specified country.

  - `country_options.cr` (object, nullable)
    Options for the registration in CR.

    - `country_options.cr.type` (enum)
      Type of registration in `country`.
Possible enum values:
      - `simplified`
        A simplified Tax Registration in the specified country.

  - `country_options.cv` (object, nullable)
    Options for the registration in CV.

    - `country_options.cv.type` (enum)
      Type of registration in `country`.
Possible enum values:
      - `simplified`
        A simplified Tax Registration in the specified country.

  - `country_options.cy` (object, nullable)
    Options for the registration in CY.

    - `country_options.cy.standard` (object, nullable)
      Options for the standard registration.

      - `country_options.cy.standard.place_of_supply_scheme` (enum)
        Place of supply scheme used in an EU standard registration.
Possible enum values:
        - `inbound_goods`
          Inbound goods place of supply scheme in which the tax is collected at destination for inbound physical goods.

        - `small_seller`
          Small seller place of supply scheme in which the seller’s tax rate is applied to sales across the EU.

        - `standard`
          Standard place of supply scheme in which tax is applied to sales in this country only.

    - `country_options.cy.type` (enum)
      Type of registration in an EU country.
Possible enum values:
      - `ioss`
        Common for businesses shipping goods below EUR 150 from non-EU countries to EU customers.

      - `oss_non_union`
        Common for businesses established outside of the EU selling services to customers in the EU.

      - `oss_union`
        Common for businesses established in the EU selling goods and services to customers in the EU.

      - `standard`
        Common for businesses selling goods and services to customers in this country.

  - `country_options.cz` (object, nullable)
    Options for the registration in CZ.

    - `country_options.cz.standard` (object, nullable)
      Options for the standard registration.

      - `country_options.cz.standard.place_of_supply_scheme` (enum)
        Place of supply scheme used in an EU standard registration.
Possible enum values:
        - `inbound_goods`
          Inbound goods place of supply scheme in which the tax is collected at destination for inbound physical goods.

        - `small_seller`
          Small seller place of supply scheme in which the seller’s tax rate is applied to sales across the EU.

        - `standard`
          Standard place of supply scheme in which tax is applied to sales in this country only.

    - `country_options.cz.type` (enum)
      Type of registration in an EU country.
Possible enum values:
      - `ioss`
        Common for businesses shipping goods below EUR 150 from non-EU countries to EU customers.

      - `oss_non_union`
        Common for businesses established outside of the EU selling services to customers in the EU.

      - `oss_union`
        Common for businesses established in the EU selling goods and services to customers in the EU.

      - `standard`
        Common for businesses selling goods and services to customers in this country.

  - `country_options.de` (object, nullable)
    Options for the registration in DE.

    - `country_options.de.standard` (object, nullable)
      Options for the standard registration.

      - `country_options.de.standard.place_of_supply_scheme` (enum)
        Place of supply scheme used in an EU standard registration.
Possible enum values:
        - `inbound_goods`
          Inbound goods place of supply scheme in which the tax is collected at destination for inbound physical goods.

        - `small_seller`
          Small seller place of supply scheme in which the seller’s tax rate is applied to sales across the EU.

        - `standard`
          Standard place of supply scheme in which tax is applied to sales in this country only.

    - `country_options.de.type` (enum)
      Type of registration in an EU country.
Possible enum values:
      - `ioss`
        Common for businesses shipping goods below EUR 150 from non-EU countries to EU customers.

      - `oss_non_union`
        Common for businesses established outside of the EU selling services to customers in the EU.

      - `oss_union`
        Common for businesses established in the EU selling goods and services to customers in the EU.

      - `standard`
        Common for businesses selling goods and services to customers in this country.

  - `country_options.dk` (object, nullable)
    Options for the registration in DK.

    - `country_options.dk.standard` (object, nullable)
      Options for the standard registration.

      - `country_options.dk.standard.place_of_supply_scheme` (enum)
        Place of supply scheme used in an EU standard registration.
Possible enum values:
        - `inbound_goods`
          Inbound goods place of supply scheme in which the tax is collected at destination for inbound physical goods.

        - `small_seller`
          Small seller place of supply scheme in which the seller’s tax rate is applied to sales across the EU.

        - `standard`
          Standard place of supply scheme in which tax is applied to sales in this country only.

    - `country_options.dk.type` (enum)
      Type of registration in an EU country.
Possible enum values:
      - `ioss`
        Common for businesses shipping goods below EUR 150 from non-EU countries to EU customers.

      - `oss_non_union`
        Common for businesses established outside of the EU selling services to customers in the EU.

      - `oss_union`
        Common for businesses established in the EU selling goods and services to customers in the EU.

      - `standard`
        Common for businesses selling goods and services to customers in this country.

  - `country_options.ec` (object, nullable)
    Options for the registration in EC.

    - `country_options.ec.type` (enum)
      Type of registration in `country`.
Possible enum values:
      - `simplified`
        A simplified Tax Registration in the specified country.

  - `country_options.ee` (object, nullable)
    Options for the registration in EE.

    - `country_options.ee.standard` (object, nullable)
      Options for the standard registration.

      - `country_options.ee.standard.place_of_supply_scheme` (enum)
        Place of supply scheme used in an EU standard registration.
Possible enum values:
        - `inbound_goods`
          Inbound goods place of supply scheme in which the tax is collected at destination for inbound physical goods.

        - `small_seller`
          Small seller place of supply scheme in which the seller’s tax rate is applied to sales across the EU.

        - `standard`
          Standard place of supply scheme in which tax is applied to sales in this country only.

    - `country_options.ee.type` (enum)
      Type of registration in an EU country.
Possible enum values:
      - `ioss`
        Common for businesses shipping goods below EUR 150 from non-EU countries to EU customers.

      - `oss_non_union`
        Common for businesses established outside of the EU selling services to customers in the EU.

      - `oss_union`
        Common for businesses established in the EU selling goods and services to customers in the EU.

      - `standard`
        Common for businesses selling goods and services to customers in this country.

  - `country_options.eg` (object, nullable)
    Options for the registration in EG.

    - `country_options.eg.type` (enum)
      Type of registration in `country`.
Possible enum values:
      - `simplified`
        A simplified Tax Registration in the specified country.

  - `country_options.es` (object, nullable)
    Options for the registration in ES.

    - `country_options.es.standard` (object, nullable)
      Options for the standard registration.

      - `country_options.es.standard.place_of_supply_scheme` (enum)
        Place of supply scheme used in an EU standard registration.
Possible enum values:
        - `inbound_goods`
          Inbound goods place of supply scheme in which the tax is collected at destination for inbound physical goods.

        - `small_seller`
          Small seller place of supply scheme in which the seller’s tax rate is applied to sales across the EU.

        - `standard`
          Standard place of supply scheme in which tax is applied to sales in this country only.

    - `country_options.es.type` (enum)
      Type of registration in an EU country.
Possible enum values:
      - `ioss`
        Common for businesses shipping goods below EUR 150 from non-EU countries to EU customers.

      - `oss_non_union`
        Common for businesses established outside of the EU selling services to customers in the EU.

      - `oss_union`
        Common for businesses established in the EU selling goods and services to customers in the EU.

      - `standard`
        Common for businesses selling goods and services to customers in this country.

  - `country_options.et` (object, nullable)
    Options for the registration in ET.

    - `country_options.et.type` (enum)
      Type of registration in `country`.
Possible enum values:
      - `standard`
        A standard Tax Registration in the specified country.

  - `country_options.fi` (object, nullable)
    Options for the registration in FI.

    - `country_options.fi.standard` (object, nullable)
      Options for the standard registration.

      - `country_options.fi.standard.place_of_supply_scheme` (enum)
        Place of supply scheme used in an EU standard registration.
Possible enum values:
        - `inbound_goods`
          Inbound goods place of supply scheme in which the tax is collected at destination for inbound physical goods.

        - `small_seller`
          Small seller place of supply scheme in which the seller’s tax rate is applied to sales across the EU.

        - `standard`
          Standard place of supply scheme in which tax is applied to sales in this country only.

    - `country_options.fi.type` (enum)
      Type of registration in an EU country.
Possible enum values:
      - `ioss`
        Common for businesses shipping goods below EUR 150 from non-EU countries to EU customers.

      - `oss_non_union`
        Common for businesses established outside of the EU selling services to customers in the EU.

      - `oss_union`
        Common for businesses established in the EU selling goods and services to customers in the EU.

      - `standard`
        Common for businesses selling goods and services to customers in this country.

  - `country_options.fr` (object, nullable)
    Options for the registration in FR.

    - `country_options.fr.standard` (object, nullable)
      Options for the standard registration.

      - `country_options.fr.standard.place_of_supply_scheme` (enum)
        Place of supply scheme used in an EU standard registration.
Possible enum values:
        - `inbound_goods`
          Inbound goods place of supply scheme in which the tax is collected at destination for inbound physical goods.

        - `small_seller`
          Small seller place of supply scheme in which the seller’s tax rate is applied to sales across the EU.

        - `standard`
          Standard place of supply scheme in which tax is applied to sales in this country only.

    - `country_options.fr.type` (enum)
      Type of registration in an EU country.
Possible enum values:
      - `ioss`
        Common for businesses shipping goods below EUR 150 from non-EU countries to EU customers.

      - `oss_non_union`
        Common for businesses established outside of the EU selling services to customers in the EU.

      - `oss_union`
        Common for businesses established in the EU selling goods and services to customers in the EU.

      - `standard`
        Common for businesses selling goods and services to customers in this country.

  - `country_options.gb` (object, nullable)
    Options for the registration in GB.

    - `country_options.gb.standard` (object, nullable)
      Options for the standard registration.

      - `country_options.gb.standard.place_of_supply_scheme` (enum)
        Place of supply scheme used in an Default standard registration.
Possible enum values:
        - `inbound_goods`
          Inbound goods place of supply scheme in which the tax is collected at destination for inbound physical goods.

        - `standard`
          Standard place of supply scheme in which tax is applied to sales in this country only.

    - `country_options.gb.type` (enum)
      Type of registration in `country`.
Possible enum values:
      - `standard`
        A standard Tax Registration in the specified country.

  - `country_options.ge` (object, nullable)
    Options for the registration in GE.

    - `country_options.ge.type` (enum)
      Type of registration in `country`.
Possible enum values:
      - `simplified`
        A simplified Tax Registration in the specified country.

  - `country_options.gn` (object, nullable)
    Options for the registration in GN.

    - `country_options.gn.type` (enum)
      Type of registration in `country`.
Possible enum values:
      - `standard`
        A standard Tax Registration in the specified country.

  - `country_options.gr` (object, nullable)
    Options for the registration in GR.

    - `country_options.gr.standard` (object, nullable)
      Options for the standard registration.

      - `country_options.gr.standard.place_of_supply_scheme` (enum)
        Place of supply scheme used in an EU standard registration.
Possible enum values:
        - `inbound_goods`
          Inbound goods place of supply scheme in which the tax is collected at destination for inbound physical goods.

        - `small_seller`
          Small seller place of supply scheme in which the seller’s tax rate is applied to sales across the EU.

        - `standard`
          Standard place of supply scheme in which tax is applied to sales in this country only.

    - `country_options.gr.type` (enum)
      Type of registration in an EU country.
Possible enum values:
      - `ioss`
        Common for businesses shipping goods below EUR 150 from non-EU countries to EU customers.

      - `oss_non_union`
        Common for businesses established outside of the EU selling services to customers in the EU.

      - `oss_union`
        Common for businesses established in the EU selling goods and services to customers in the EU.

      - `standard`
        Common for businesses selling goods and services to customers in this country.

  - `country_options.hr` (object, nullable)
    Options for the registration in HR.

    - `country_options.hr.standard` (object, nullable)
      Options for the standard registration.

      - `country_options.hr.standard.place_of_supply_scheme` (enum)
        Place of supply scheme used in an EU standard registration.
Possible enum values:
        - `inbound_goods`
          Inbound goods place of supply scheme in which the tax is collected at destination for inbound physical goods.

        - `small_seller`
          Small seller place of supply scheme in which the seller’s tax rate is applied to sales across the EU.

        - `standard`
          Standard place of supply scheme in which tax is applied to sales in this country only.

    - `country_options.hr.type` (enum)
      Type of registration in an EU country.
Possible enum values:
      - `ioss`
        Common for businesses shipping goods below EUR 150 from non-EU countries to EU customers.

      - `oss_non_union`
        Common for businesses established outside of the EU selling services to customers in the EU.

      - `oss_union`
        Common for businesses established in the EU selling goods and services to customers in the EU.

      - `standard`
        Common for businesses selling goods and services to customers in this country.

  - `country_options.hu` (object, nullable)
    Options for the registration in HU.

    - `country_options.hu.standard` (object, nullable)
      Options for the standard registration.

      - `country_options.hu.standard.place_of_supply_scheme` (enum)
        Place of supply scheme used in an EU standard registration.
Possible enum values:
        - `inbound_goods`
          Inbound goods place of supply scheme in which the tax is collected at destination for inbound physical goods.

        - `small_seller`
          Small seller place of supply scheme in which the seller’s tax rate is applied to sales across the EU.

        - `standard`
          Standard place of supply scheme in which tax is applied to sales in this country only.

    - `country_options.hu.type` (enum)
      Type of registration in an EU country.
Possible enum values:
      - `ioss`
        Common for businesses shipping goods below EUR 150 from non-EU countries to EU customers.

      - `oss_non_union`
        Common for businesses established outside of the EU selling services to customers in the EU.

      - `oss_union`
        Common for businesses established in the EU selling goods and services to customers in the EU.

      - `standard`
        Common for businesses selling goods and services to customers in this country.

  - `country_options.ie` (object, nullable)
    Options for the registration in IE.

    - `country_options.ie.standard` (object, nullable)
      Options for the standard registration.

      - `country_options.ie.standard.place_of_supply_scheme` (enum)
        Place of supply scheme used in an EU standard registration.
Possible enum values:
        - `inbound_goods`
          Inbound goods place of supply scheme in which the tax is collected at destination for inbound physical goods.

        - `small_seller`
          Small seller place of supply scheme in which the seller’s tax rate is applied to sales across the EU.

        - `standard`
          Standard place of supply scheme in which tax is applied to sales in this country only.

    - `country_options.ie.type` (enum)
      Type of registration in an EU country.
Possible enum values:
      - `ioss`
        Common for businesses shipping goods below EUR 150 from non-EU countries to EU customers.

      - `oss_non_union`
        Common for businesses established outside of the EU selling services to customers in the EU.

      - `oss_union`
        Common for businesses established in the EU selling goods and services to customers in the EU.

      - `standard`
        Common for businesses selling goods and services to customers in this country.

  - `country_options.in` (object, nullable)
    Options for the registration in IN.

    - `country_options.in.type` (enum)
      Type of registration in `country`.
Possible enum values:
      - `simplified`
        A simplified Tax Registration in the specified country.

  - `country_options.is` (object, nullable)
    Options for the registration in IS.

    - `country_options.is.type` (enum)
      Type of registration in `country`.
Possible enum values:
      - `standard`
        A standard Tax Registration in the specified country.

  - `country_options.it` (object, nullable)
    Options for the registration in IT.

    - `country_options.it.standard` (object, nullable)
      Options for the standard registration.

      - `country_options.it.standard.place_of_supply_scheme` (enum)
        Place of supply scheme used in an EU standard registration.
Possible enum values:
        - `inbound_goods`
          Inbound goods place of supply scheme in which the tax is collected at destination for inbound physical goods.

        - `small_seller`
          Small seller place of supply scheme in which the seller’s tax rate is applied to sales across the EU.

        - `standard`
          Standard place of supply scheme in which tax is applied to sales in this country only.

    - `country_options.it.type` (enum)
      Type of registration in an EU country.
Possible enum values:
      - `ioss`
        Common for businesses shipping goods below EUR 150 from non-EU countries to EU customers.

      - `oss_non_union`
        Common for businesses established outside of the EU selling services to customers in the EU.

      - `oss_union`
        Common for businesses established in the EU selling goods and services to customers in the EU.

      - `standard`
        Common for businesses selling goods and services to customers in this country.

  - `country_options.jp` (object, nullable)
    Options for the registration in JP.

    - `country_options.jp.standard` (object, nullable)
      Options for the standard registration.

      - `country_options.jp.standard.place_of_supply_scheme` (enum)
        Place of supply scheme used in an Default standard registration.
Possible enum values:
        - `inbound_goods`
          Inbound goods place of supply scheme in which the tax is collected at destination for inbound physical goods.

        - `standard`
          Standard place of supply scheme in which tax is applied to sales in this country only.

    - `country_options.jp.type` (enum)
      Type of registration in `country`.
Possible enum values:
      - `standard`
        A standard Tax Registration in the specified country.

  - `country_options.ke` (object, nullable)
    Options for the registration in KE.

    - `country_options.ke.type` (enum)
      Type of registration in `country`.
Possible enum values:
      - `simplified`
        A simplified Tax Registration in the specified country.

  - `country_options.kg` (object, nullable)
    Options for the registration in KG.

    - `country_options.kg.type` (enum)
      Type of registration in `country`.
Possible enum values:
      - `simplified`
        A simplified Tax Registration in the specified country.

  - `country_options.kh` (object, nullable)
    Options for the registration in KH.

    - `country_options.kh.type` (enum)
      Type of registration in `country`.
Possible enum values:
      - `simplified`
        A simplified Tax Registration in the specified country.

  - `country_options.kr` (object, nullable)
    Options for the registration in KR.

    - `country_options.kr.type` (enum)
      Type of registration in `country`.
Possible enum values:
      - `simplified`
        A simplified Tax Registration in the specified country.

  - `country_options.kz` (object, nullable)
    Options for the registration in KZ.

    - `country_options.kz.type` (enum)
      Type of registration in `country`.
Possible enum values:
      - `simplified`
        A simplified Tax Registration in the specified country.

  - `country_options.la` (object, nullable)
    Options for the registration in LA.

    - `country_options.la.type` (enum)
      Type of registration in `country`.
Possible enum values:
      - `simplified`
        A simplified Tax Registration in the specified country.

  - `country_options.lt` (object, nullable)
    Options for the registration in LT.

    - `country_options.lt.standard` (object, nullable)
      Options for the standard registration.

      - `country_options.lt.standard.place_of_supply_scheme` (enum)
        Place of supply scheme used in an EU standard registration.
Possible enum values:
        - `inbound_goods`
          Inbound goods place of supply scheme in which the tax is collected at destination for inbound physical goods.

        - `small_seller`
          Small seller place of supply scheme in which the seller’s tax rate is applied to sales across the EU.

        - `standard`
          Standard place of supply scheme in which tax is applied to sales in this country only.

    - `country_options.lt.type` (enum)
      Type of registration in an EU country.
Possible enum values:
      - `ioss`
        Common for businesses shipping goods below EUR 150 from non-EU countries to EU customers.

      - `oss_non_union`
        Common for businesses established outside of the EU selling services to customers in the EU.

      - `oss_union`
        Common for businesses established in the EU selling goods and services to customers in the EU.

      - `standard`
        Common for businesses selling goods and services to customers in this country.

  - `country_options.lu` (object, nullable)
    Options for the registration in LU.

    - `country_options.lu.standard` (object, nullable)
      Options for the standard registration.

      - `country_options.lu.standard.place_of_supply_scheme` (enum)
        Place of supply scheme used in an EU standard registration.
Possible enum values:
        - `inbound_goods`
          Inbound goods place of supply scheme in which the tax is collected at destination for inbound physical goods.

        - `small_seller`
          Small seller place of supply scheme in which the seller’s tax rate is applied to sales across the EU.

        - `standard`
          Standard place of supply scheme in which tax is applied to sales in this country only.

    - `country_options.lu.type` (enum)
      Type of registration in an EU country.
Possible enum values:
      - `ioss`
        Common for businesses shipping goods below EUR 150 from non-EU countries to EU customers.

      - `oss_non_union`
        Common for businesses established outside of the EU selling services to customers in the EU.

      - `oss_union`
        Common for businesses established in the EU selling goods and services to customers in the EU.

      - `standard`
        Common for businesses selling goods and services to customers in this country.

  - `country_options.lv` (object, nullable)
    Options for the registration in LV.

    - `country_options.lv.standard` (object, nullable)
      Options for the standard registration.

      - `country_options.lv.standard.place_of_supply_scheme` (enum)
        Place of supply scheme used in an EU standard registration.
Possible enum values:
        - `inbound_goods`
          Inbound goods place of supply scheme in which the tax is collected at destination for inbound physical goods.

        - `small_seller`
          Small seller place of supply scheme in which the seller’s tax rate is applied to sales across the EU.

        - `standard`
          Standard place of supply scheme in which tax is applied to sales in this country only.

    - `country_options.lv.type` (enum)
      Type of registration in an EU country.
Possible enum values:
      - `ioss`
        Common for businesses shipping goods below EUR 150 from non-EU countries to EU customers.

      - `oss_non_union`
        Common for businesses established outside of the EU selling services to customers in the EU.

      - `oss_union`
        Common for businesses established in the EU selling goods and services to customers in the EU.

      - `standard`
        Common for businesses selling goods and services to customers in this country.

  - `country_options.ma` (object, nullable)
    Options for the registration in MA.

    - `country_options.ma.type` (enum)
      Type of registration in `country`.
Possible enum values:
      - `simplified`
        A simplified Tax Registration in the specified country.

  - `country_options.md` (object, nullable)
    Options for the registration in MD.

    - `country_options.md.type` (enum)
      Type of registration in `country`.
Possible enum values:
      - `simplified`
        A simplified Tax Registration in the specified country.

  - `country_options.me` (object, nullable)
    Options for the registration in ME.

    - `country_options.me.type` (enum)
      Type of registration in `country`.
Possible enum values:
      - `standard`
        A standard Tax Registration in the specified country.

  - `country_options.mk` (object, nullable)
    Options for the registration in MK.

    - `country_options.mk.type` (enum)
      Type of registration in `country`.
Possible enum values:
      - `standard`
        A standard Tax Registration in the specified country.

  - `country_options.mr` (object, nullable)
    Options for the registration in MR.

    - `country_options.mr.type` (enum)
      Type of registration in `country`.
Possible enum values:
      - `standard`
        A standard Tax Registration in the specified country.

  - `country_options.mt` (object, nullable)
    Options for the registration in MT.

    - `country_options.mt.standard` (object, nullable)
      Options for the standard registration.

      - `country_options.mt.standard.place_of_supply_scheme` (enum)
        Place of supply scheme used in an EU standard registration.
Possible enum values:
        - `inbound_goods`
          Inbound goods place of supply scheme in which the tax is collected at destination for inbound physical goods.

        - `small_seller`
          Small seller place of supply scheme in which the seller’s tax rate is applied to sales across the EU.

        - `standard`
          Standard place of supply scheme in which tax is applied to sales in this country only.

    - `country_options.mt.type` (enum)
      Type of registration in an EU country.
Possible enum values:
      - `ioss`
        Common for businesses shipping goods below EUR 150 from non-EU countries to EU customers.

      - `oss_non_union`
        Common for businesses established outside of the EU selling services to customers in the EU.

      - `oss_union`
        Common for businesses established in the EU selling goods and services to customers in the EU.

      - `standard`
        Common for businesses selling goods and services to customers in this country.

  - `country_options.mx` (object, nullable)
    Options for the registration in MX.

    - `country_options.mx.type` (enum)
      Type of registration in `country`.
Possible enum values:
      - `simplified`
        A simplified Tax Registration in the specified country.

  - `country_options.my` (object, nullable)
    Options for the registration in MY.

    - `country_options.my.type` (enum)
      Type of registration in `country`.
Possible enum values:
      - `simplified`
        A simplified Tax Registration in the specified country.

  - `country_options.ng` (object, nullable)
    Options for the registration in NG.

    - `country_options.ng.type` (enum)
      Type of registration in `country`.
Possible enum values:
      - `simplified`
        A simplified Tax Registration in the specified country.

  - `country_options.nl` (object, nullable)
    Options for the registration in NL.

    - `country_options.nl.standard` (object, nullable)
      Options for the standard registration.

      - `country_options.nl.standard.place_of_supply_scheme` (enum)
        Place of supply scheme used in an EU standard registration.
Possible enum values:
        - `inbound_goods`
          Inbound goods place of supply scheme in which the tax is collected at destination for inbound physical goods.

        - `small_seller`
          Small seller place of supply scheme in which the seller’s tax rate is applied to sales across the EU.

        - `standard`
          Standard place of supply scheme in which tax is applied to sales in this country only.

    - `country_options.nl.type` (enum)
      Type of registration in an EU country.
Possible enum values:
      - `ioss`
        Common for businesses shipping goods below EUR 150 from non-EU countries to EU customers.

      - `oss_non_union`
        Common for businesses established outside of the EU selling services to customers in the EU.

      - `oss_union`
        Common for businesses established in the EU selling goods and services to customers in the EU.

      - `standard`
        Common for businesses selling goods and services to customers in this country.

  - `country_options.no` (object, nullable)
    Options for the registration in NO.

    - `country_options.no.standard` (object, nullable)
      Options for the standard registration.

      - `country_options.no.standard.place_of_supply_scheme` (enum)
        Place of supply scheme used in an Default standard registration.
Possible enum values:
        - `inbound_goods`
          Inbound goods place of supply scheme in which the tax is collected at destination for inbound physical goods.

        - `standard`
          Standard place of supply scheme in which tax is applied to sales in this country only.

    - `country_options.no.type` (enum)
      Type of registration in `country`.
Possible enum values:
      - `standard`
        A standard Tax Registration in the specified country.

  - `country_options.np` (object, nullable)
    Options for the registration in NP.

    - `country_options.np.type` (enum)
      Type of registration in `country`.
Possible enum values:
      - `simplified`
        A simplified Tax Registration in the specified country.

  - `country_options.nz` (object, nullable)
    Options for the registration in NZ.

    - `country_options.nz.standard` (object, nullable)
      Options for the standard registration.

      - `country_options.nz.standard.place_of_supply_scheme` (enum)
        Place of supply scheme used in an Default standard registration.
Possible enum values:
        - `inbound_goods`
          Inbound goods place of supply scheme in which the tax is collected at destination for inbound physical goods.

        - `standard`
          Standard place of supply scheme in which tax is applied to sales in this country only.

    - `country_options.nz.type` (enum)
      Type of registration in `country`.
Possible enum values:
      - `standard`
        A standard Tax Registration in the specified country.

  - `country_options.om` (object, nullable)
    Options for the registration in OM.

    - `country_options.om.type` (enum)
      Type of registration in `country`.
Possible enum values:
      - `standard`
        A standard Tax Registration in the specified country.

  - `country_options.pe` (object, nullable)
    Options for the registration in PE.

    - `country_options.pe.type` (enum)
      Type of registration in `country`.
Possible enum values:
      - `simplified`
        A simplified Tax Registration in the specified country.

  - `country_options.ph` (object, nullable)
    Options for the registration in PH.

    - `country_options.ph.type` (enum)
      Type of registration in `country`.
Possible enum values:
      - `simplified`
        A simplified Tax Registration in the specified country.

  - `country_options.pl` (object, nullable)
    Options for the registration in PL.

    - `country_options.pl.standard` (object, nullable)
      Options for the standard registration.

      - `country_options.pl.standard.place_of_supply_scheme` (enum)
        Place of supply scheme used in an EU standard registration.
Possible enum values:
        - `inbound_goods`
          Inbound goods place of supply scheme in which the tax is collected at destination for inbound physical goods.

        - `small_seller`
          Small seller place of supply scheme in which the seller’s tax rate is applied to sales across the EU.

        - `standard`
          Standard place of supply scheme in which tax is applied to sales in this country only.

    - `country_options.pl.type` (enum)
      Type of registration in an EU country.
Possible enum values:
      - `ioss`
        Common for businesses shipping goods below EUR 150 from non-EU countries to EU customers.

      - `oss_non_union`
        Common for businesses established outside of the EU selling services to customers in the EU.

      - `oss_union`
        Common for businesses established in the EU selling goods and services to customers in the EU.

      - `standard`
        Common for businesses selling goods and services to customers in this country.

  - `country_options.pt` (object, nullable)
    Options for the registration in PT.

    - `country_options.pt.standard` (object, nullable)
      Options for the standard registration.

      - `country_options.pt.standard.place_of_supply_scheme` (enum)
        Place of supply scheme used in an EU standard registration.
Possible enum values:
        - `inbound_goods`
          Inbound goods place of supply scheme in which the tax is collected at destination for inbound physical goods.

        - `small_seller`
          Small seller place of supply scheme in which the seller’s tax rate is applied to sales across the EU.

        - `standard`
          Standard place of supply scheme in which tax is applied to sales in this country only.

    - `country_options.pt.type` (enum)
      Type of registration in an EU country.
Possible enum values:
      - `ioss`
        Common for businesses shipping goods below EUR 150 from non-EU countries to EU customers.

      - `oss_non_union`
        Common for businesses established outside of the EU selling services to customers in the EU.

      - `oss_union`
        Common for businesses established in the EU selling goods and services to customers in the EU.

      - `standard`
        Common for businesses selling goods and services to customers in this country.

  - `country_options.ro` (object, nullable)
    Options for the registration in RO.

    - `country_options.ro.standard` (object, nullable)
      Options for the standard registration.

      - `country_options.ro.standard.place_of_supply_scheme` (enum)
        Place of supply scheme used in an EU standard registration.
Possible enum values:
        - `inbound_goods`
          Inbound goods place of supply scheme in which the tax is collected at destination for inbound physical goods.

        - `small_seller`
          Small seller place of supply scheme in which the seller’s tax rate is applied to sales across the EU.

        - `standard`
          Standard place of supply scheme in which tax is applied to sales in this country only.

    - `country_options.ro.type` (enum)
      Type of registration in an EU country.
Possible enum values:
      - `ioss`
        Common for businesses shipping goods below EUR 150 from non-EU countries to EU customers.

      - `oss_non_union`
        Common for businesses established outside of the EU selling services to customers in the EU.

      - `oss_union`
        Common for businesses established in the EU selling goods and services to customers in the EU.

      - `standard`
        Common for businesses selling goods and services to customers in this country.

  - `country_options.rs` (object, nullable)
    Options for the registration in RS.

    - `country_options.rs.type` (enum)
      Type of registration in `country`.
Possible enum values:
      - `standard`
        A standard Tax Registration in the specified country.

  - `country_options.ru` (object, nullable)
    Options for the registration in RU.

    - `country_options.ru.type` (enum)
      Type of registration in `country`.
Possible enum values:
      - `simplified`
        A simplified Tax Registration in the specified country.

  - `country_options.sa` (object, nullable)
    Options for the registration in SA.

    - `country_options.sa.type` (enum)
      Type of registration in `country`.
Possible enum values:
      - `simplified`
        A simplified Tax Registration in the specified country.

  - `country_options.se` (object, nullable)
    Options for the registration in SE.

    - `country_options.se.standard` (object, nullable)
      Options for the standard registration.

      - `country_options.se.standard.place_of_supply_scheme` (enum)
        Place of supply scheme used in an EU standard registration.
Possible enum values:
        - `inbound_goods`
          Inbound goods place of supply scheme in which the tax is collected at destination for inbound physical goods.

        - `small_seller`
          Small seller place of supply scheme in which the seller’s tax rate is applied to sales across the EU.

        - `standard`
          Standard place of supply scheme in which tax is applied to sales in this country only.

    - `country_options.se.type` (enum)
      Type of registration in an EU country.
Possible enum values:
      - `ioss`
        Common for businesses shipping goods below EUR 150 from non-EU countries to EU customers.

      - `oss_non_union`
        Common for businesses established outside of the EU selling services to customers in the EU.

      - `oss_union`
        Common for businesses established in the EU selling goods and services to customers in the EU.

      - `standard`
        Common for businesses selling goods and services to customers in this country.

  - `country_options.sg` (object, nullable)
    Options for the registration in SG.

    - `country_options.sg.standard` (object, nullable)
      Options for the standard registration.

      - `country_options.sg.standard.place_of_supply_scheme` (enum)
        Place of supply scheme used in an Default standard registration.
Possible enum values:
        - `inbound_goods`
          Inbound goods place of supply scheme in which the tax is collected at destination for inbound physical goods.

        - `standard`
          Standard place of supply scheme in which tax is applied to sales in this country only.

    - `country_options.sg.type` (enum)
      Type of registration in `country`.
Possible enum values:
      - `standard`
        A standard Tax Registration in the specified country.

  - `country_options.si` (object, nullable)
    Options for the registration in SI.

    - `country_options.si.standard` (object, nullable)
      Options for the standard registration.

      - `country_options.si.standard.place_of_supply_scheme` (enum)
        Place of supply scheme used in an EU standard registration.
Possible enum values:
        - `inbound_goods`
          Inbound goods place of supply scheme in which the tax is collected at destination for inbound physical goods.

        - `small_seller`
          Small seller place of supply scheme in which the seller’s tax rate is applied to sales across the EU.

        - `standard`
          Standard place of supply scheme in which tax is applied to sales in this country only.

    - `country_options.si.type` (enum)
      Type of registration in an EU country.
Possible enum values:
      - `ioss`
        Common for businesses shipping goods below EUR 150 from non-EU countries to EU customers.

      - `oss_non_union`
        Common for businesses established outside of the EU selling services to customers in the EU.

      - `oss_union`
        Common for businesses established in the EU selling goods and services to customers in the EU.

      - `standard`
        Common for businesses selling goods and services to customers in this country.

  - `country_options.sk` (object, nullable)
    Options for the registration in SK.

    - `country_options.sk.standard` (object, nullable)
      Options for the standard registration.

      - `country_options.sk.standard.place_of_supply_scheme` (enum)
        Place of supply scheme used in an EU standard registration.
Possible enum values:
        - `inbound_goods`
          Inbound goods place of supply scheme in which the tax is collected at destination for inbound physical goods.

        - `small_seller`
          Small seller place of supply scheme in which the seller’s tax rate is applied to sales across the EU.

        - `standard`
          Standard place of supply scheme in which tax is applied to sales in this country only.

    - `country_options.sk.type` (enum)
      Type of registration in an EU country.
Possible enum values:
      - `ioss`
        Common for businesses shipping goods below EUR 150 from non-EU countries to EU customers.

      - `oss_non_union`
        Common for businesses established outside of the EU selling services to customers in the EU.

      - `oss_union`
        Common for businesses established in the EU selling goods and services to customers in the EU.

      - `standard`
        Common for businesses selling goods and services to customers in this country.

  - `country_options.sn` (object, nullable)
    Options for the registration in SN.

    - `country_options.sn.type` (enum)
      Type of registration in `country`.
Possible enum values:
      - `simplified`
        A simplified Tax Registration in the specified country.

  - `country_options.sr` (object, nullable)
    Options for the registration in SR.

    - `country_options.sr.type` (enum)
      Type of registration in `country`.
Possible enum values:
      - `standard`
        A standard Tax Registration in the specified country.

  - `country_options.th` (object, nullable)
    Options for the registration in TH.

    - `country_options.th.type` (enum)
      Type of registration in `country`.
Possible enum values:
      - `simplified`
        A simplified Tax Registration in Thailand to collect VAT.

  - `country_options.tj` (object, nullable)
    Options for the registration in TJ.

    - `country_options.tj.type` (enum)
      Type of registration in `country`.
Possible enum values:
      - `simplified`
        A simplified Tax Registration in the specified country.

  - `country_options.tr` (object, nullable)
    Options for the registration in TR.

    - `country_options.tr.type` (enum)
      Type of registration in `country`.
Possible enum values:
      - `simplified`
        A simplified Tax Registration in the specified country.

  - `country_options.tw` (object, nullable)
    Options for the registration in TW.

    - `country_options.tw.type` (enum)
      Type of registration in `country`.
Possible enum values:
      - `simplified`
        A simplified Tax Registration in the specified country.

  - `country_options.tz` (object, nullable)
    Options for the registration in TZ.

    - `country_options.tz.type` (enum)
      Type of registration in `country`.
Possible enum values:
      - `simplified`
        A simplified Tax Registration in the specified country.

  - `country_options.ua` (object, nullable)
    Options for the registration in UA.

    - `country_options.ua.type` (enum)
      Type of registration in `country`.
Possible enum values:
      - `simplified`
        A simplified Tax Registration in the specified country.

  - `country_options.ug` (object, nullable)
    Options for the registration in UG.

    - `country_options.ug.type` (enum)
      Type of registration in `country`.
Possible enum values:
      - `simplified`
        A simplified Tax Registration in the specified country.

  - `country_options.us` (object, nullable)
    Options for the registration in US.

    - `country_options.us.local_amusement_tax` (object, nullable)
      Options for the local amusement tax registration.

      - `country_options.us.local_amusement_tax.jurisdiction` (string)
        A [FIPS code](https://www.census.gov/library/reference/code-lists/ansi.html) representing the local jurisdiction.

    - `country_options.us.local_lease_tax` (object, nullable)
      Options for the local lease tax registration.

      - `country_options.us.local_lease_tax.jurisdiction` (string)
        A [FIPS code](https://www.census.gov/library/reference/code-lists/ansi.html) representing the local jurisdiction.

    - `country_options.us.state` (string)
      Two-letter US state code ([ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2)).

    - `country_options.us.state_sales_tax` (object, nullable)
      Options for the state sales tax registration.

      - `country_options.us.state_sales_tax.elections` (array of objects)
        Elections for the state sales tax registration.

        - `country_options.us.state_sales_tax.elections.jurisdiction` (string, nullable)
          A [FIPS code](https://www.census.gov/library/reference/code-lists/ansi.html) representing the local jurisdiction.

        - `country_options.us.state_sales_tax.elections.type` (enum)
          The type of the election for the state sales tax registration.
Possible enum values:
          - `local_use_tax`
            Use Tax in Pennsylvania for the city of Philadelphia or Allegheny county which can be collected by remote sellers outside of these locations.

          - `simplified_sellers_use_tax`
            Simplified Sellers Use Tax which can be collected by remote sellers with no physical presence in Alabama.

          - `single_local_use_tax`
            Single Local Use Tax Rate which can be collected by remote sellers with no physical presence in Texas.

    - `country_options.us.type` (enum)
      Type of registration in the US.
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

  - `country_options.uy` (object, nullable)
    Options for the registration in UY.

    - `country_options.uy.type` (enum)
      Type of registration in `country`.
Possible enum values:
      - `standard`
        A standard Tax Registration in the specified country.

  - `country_options.uz` (object, nullable)
    Options for the registration in UZ.

    - `country_options.uz.type` (enum)
      Type of registration in `country`.
Possible enum values:
      - `simplified`
        A simplified Tax Registration in the specified country.

  - `country_options.vn` (object, nullable)
    Options for the registration in VN.

    - `country_options.vn.type` (enum)
      Type of registration in `country`.
Possible enum values:
      - `simplified`
        A simplified Tax Registration in the specified country.

  - `country_options.za` (object, nullable)
    Options for the registration in ZA.

    - `country_options.za.type` (enum)
      Type of registration in `country`.
Possible enum values:
      - `standard`
        A standard Tax Registration in the specified country.

  - `country_options.zm` (object, nullable)
    Options for the registration in ZM.

    - `country_options.zm.type` (enum)
      Type of registration in `country`.
Possible enum values:
      - `simplified`
        A simplified Tax Registration in the specified country.

  - `country_options.zw` (object, nullable)
    Options for the registration in ZW.

    - `country_options.zw.type` (enum)
      Type of registration in `country`.
Possible enum values:
      - `standard`
        A standard Tax Registration in the specified country.

- `created` (timestamp)
  Time at which the object was created. Measured in seconds since the Unix epoch.

- `expires_at` (timestamp, nullable)
  If set, the registration stops being active at this time. If not set, the registration will be active indefinitely. Measured in seconds since the Unix epoch.

- `livemode` (boolean)
  Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.

- `status` (enum)
  The status of the registration. This field is present for convenience and can be deduced from `active_from` and `expires_at`.
Possible enum values:
  - `active`
    The Tax Registration is currently active.

  - `expired`
    The Tax Registration is no longer active.

  - `scheduled`
    The Tax Registration will become active in the future.

### The Tax Registration object

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