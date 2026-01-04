# The TerminalHardwareOrder object

## Attributes

- `id` (string)
  Unique identifier for the object.

- `object` (string)
  String representing the object’s type. Objects of the same type share the same value.

- `amount` (integer)
  A positive integer in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal). Represents the total cost for the order.

- `created` (timestamp)
  Time at which the object was created. Measured in seconds since the Unix epoch.

- `currency` (enum)
  Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

- `hardware_order_items` (array of objects)
  An array of line items ordered.

  - `hardware_order_items.amount` (integer)
    A positive integer that represents the cost of the order in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal).

  - `hardware_order_items.currency` (enum)
    Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

  - `hardware_order_items.quantity` (integer)
    The quantity to be ordered.

  - `hardware_order_items.terminal_hardware_sku` (object)
    The `TerminalHardwareSKU`.

    - `hardware_order_items.terminal_hardware_sku.id` (string)
      Unique identifier for the object.

    - `hardware_order_items.terminal_hardware_sku.amount` (integer)
      The price of this SKU.

    - `hardware_order_items.terminal_hardware_sku.country` (enum)
      The country in which this SKU is available.
Possible enum values:
      - `AD`
      - `AE`
      - `AF`
      - `AG`
      - `AI`
      - `AL`
      - `AM`
      - `AO`
      - `AQ`
      - `AR`
      - `AS`
      - `AT`
      - `AU`
      - `AW`
      - `AX`
      - `AZ`
      - `BA`
      - `BB`
      - `BD`
      - `BE`
      - `BF`
      - `BG`
      - `BH`
      - `BI`
      - `BJ`
      - `BL`
      - `BM`
      - `BN`
      - `BO`
      - `BQ`
      - `BR`
      - `BS`
      - `BT`
      - `BV`
      - `BW`
      - `BY`
      - `BZ`
      - `CA`
      - `CC`
      - `CD`
      - `CF`
      - `CG`
      - `CH`
      - `CI`
      - `CK`
      - `CL`
      - `CM`
      - `CN`
      - `CO`
      - `CR`
      - `CU`
      - `CV`
      - `CW`
      - `CX`
      - `CY`
      - `CZ`
      - `DE`
      - `DJ`
      - `DK`
      - `DM`
      - `DO`
      - `DZ`
      - `EC`
      - `EE`
      - `EG`
      - `EH`
      - `ER`
      - `ES`
      - `ET`
      - `FI`
      - `FJ`
      - `FK`
      - `FM`
      - `FO`
      - `FR`
      - `GA`
      - `GB`
      - `GD`
      - `GE`
      - `GF`
      - `GG`
      - `GH`
      - `GI`
      - `GL`
      - `GM`
      - `GN`
      - `GP`
      - `GQ`
      - `GR`
      - `GS`
      - `GT`
      - `GU`
      - `GW`
      - `GY`
      - `HK`
      - `HM`
      - `HN`
      - `HR`
      - `HT`
      - `HU`
      - `ID`
      - `IE`
      - `IL`
      - `IM`
      - `IN`
      - `IO`
      - `IQ`
      - `IR`
      - `IS`
      - `IT`
      - `JE`
      - `JM`
      - `JO`
      - `JP`
      - `KE`
      - `KG`
      - `KH`
      - `KI`
      - `KM`
      - `KN`
      - `KP`
      - `KR`
      - `KW`
      - `KY`
      - `KZ`
      - `LA`
      - `LB`
      - `LC`
      - `LI`
      - `LK`
      - `LR`
      - `LS`
      - `LT`
      - `LU`
      - `LV`
      - `LY`
      - `MA`
      - `MC`
      - `MD`
      - `ME`
      - `MF`
      - `MG`
      - `MH`
      - `MK`
      - `ML`
      - `MM`
      - `MN`
      - `MO`
      - `MP`
      - `MQ`
      - `MR`
      - `MS`
      - `MT`
      - `MU`
      - `MV`
      - `MW`
      - `MX`
      - `MY`
      - `MZ`
      - `NA`
      - `NC`
      - `NE`
      - `NF`
      - `NG`
      - `NI`
      - `NL`
      - `NO`
      - `NP`
      - `NR`
      - `NU`
      - `NZ`
      - `OM`
      - `PA`
      - `PE`
      - `PF`
      - `PG`
      - `PH`
      - `PK`
      - `PL`
      - `PM`
      - `PN`
      - `PR`
      - `PS`
      - `PT`
      - `PW`
      - `PY`
      - `QA`
      - `RE`
      - `RO`
      - `RS`
      - `RU`
      - `RW`
      - `SA`
      - `SB`
      - `SC`
      - `SD`
      - `SE`
      - `SG`
      - `SH`
      - `SI`
      - `SJ`
      - `SK`
      - `SL`
      - `SM`
      - `SN`
      - `SO`
      - `SR`
      - `SS`
      - `ST`
      - `SV`
      - `SX`
      - `SY`
      - `SZ`
      - `TC`
      - `TD`
      - `TF`
      - `TG`
      - `TH`
      - `TJ`
      - `TK`
      - `TL`
      - `TM`
      - `TN`
      - `TO`
      - `TR`
      - `TT`
      - `TV`
      - `TW`
      - `TZ`
      - `UA`
      - `UG`
      - `UM`
      - `US`
      - `UY`
      - `UZ`
      - `VA`
      - `VC`
      - `VE`
      - `VG`
      - `VI`
      - `VN`
      - `VU`
      - `WF`
      - `WS`
      - `YE`
      - `YT`
      - `ZA`
      - `ZM`
      - `ZW`

    - `hardware_order_items.terminal_hardware_sku.currency` (enum)
      Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
Possible enum values:
      - `aed`
      - `afn`
      - `all`
      - `amd`
      - `ang`
      - `aoa`
      - `ars`
      - `aud`
      - `awg`
      - `azn`
      - `bam`
      - `bbd`
      - `bdt`
      - `bgn`
      - `bhd`
      - `bif`
      - `bmd`
      - `bnd`
      - `bob`
      - `brl`
      - `bsd`
      - `btn`
      - `bwp`
      - `byn`
      - `bzd`
      - `cad`
      - `cdf`
      - `chf`
      - `clp`
      - `cny`
      - `cop`
      - `crc`
      - `cve`
      - `czk`
      - `djf`
      - `dkk`
      - `dop`
      - `dzd`
      - `eek`
      - `egp`
      - `etb`
      - `eur`
      - `fjd`
      - `fkp`
      - `gbp`
      - `gel`
      - `ghs`
      - `gip`
      - `gmd`
      - `gnf`
      - `gtq`
      - `gyd`
      - `hkd`
      - `hnl`
      - `hrk`
      - `htg`
      - `huf`
      - `idr`
      - `ils`
      - `inr`
      - `isk`
      - `jmd`
      - `jod`
      - `jpy`
      - `kes`
      - `kgs`
      - `khr`
      - `kmf`
      - `krw`
      - `kwd`
      - `kyd`
      - `kzt`
      - `lak`
      - `lbp`
      - `lkr`
      - `lrd`
      - `lsl`
      - `ltl`
      - `lvl`
      - `mad`
      - `mdl`
      - `mga`
      - `mkd`
      - `mmk`
      - `mnt`
      - `mop`
      - `mro`
      - `mur`
      - `mvr`
      - `mwk`
      - `mxn`
      - `myr`
      - `mzn`
      - `nad`
      - `ngn`
      - `nio`
      - `nok`
      - `npr`
      - `nzd`
      - `omr`
      - `pab`
      - `pen`
      - `pgk`
      - `php`
      - `pkr`
      - `pln`
      - `pyg`
      - `qar`
      - `ron`
      - `rsd`
      - `rub`
      - `rwf`
      - `sar`
      - `sbd`
      - `scr`
      - `sek`
      - `sgd`
      - `shp`
      - `sle`
      - `sll`
      - `sos`
      - `srd`
      - `std`
      - `svc`
      - `szl`
      - `thb`
      - `tjs`
      - `tnd`
      - `top`
      - `try`
      - `ttd`
      - `twd`
      - `tzs`
      - `uah`
      - `ugx`
      - `usd`
      - `usdc`
      - `uyu`
      - `uzs`
      - `vef`
      - `vnd`
      - `vuv`
      - `wst`
      - `xaf`
      - `xcd`
      - `xcg`
      - `xof`
      - `xpf`
      - `yer`
      - `zar`
      - `zmw`

    - `hardware_order_items.terminal_hardware_sku.product` (string)
      ID of the product for this SKU.

- `livemode` (boolean)
  Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.

- `metadata` (object, nullable)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

- `payment_type` (enum)
  The method of payment for this order.
Possible enum values:
  - `monthly_invoice`
    A consolidated invoice issued by Stripe at the end of each month.

  - `none`
    No charges apply.

  - `payment_intent`
    A one-time payment processed at the time of order creation in the dashboard.

- `po_number` (string, nullable)
  The purchase order number will appear on the packing slip, shipping label, and monthly billing invoice.

- `shipment_tracking` (array of objects)
  Returns the tracking information for each shipment.

  - `shipment_tracking.carrier` (enum)
    The name of the carrier delivering the order.
Possible enum values:
    - `abf_freight`
      ABF Freight

    - `australia_post`
      Australia Post

    - `canada_post`
      Canada Post

    - `dhl`
      DHL

    - `dpd`
      DPD

    - `estes_express`
      Estes Express

    - `exact_logistics`
      Exact Logistics / Pallex

    - `fedex`
      FedEx

    - `fedex_freight`
      Fedex Freight

    - `other`
      A placeholder to catch new carriers in your integration as we introduce them.

    - `palletforce`
      Palletforce

    - `purolator`
      Purolator

    - `royal_mail`
      Royal Mail

    - `tforce_freight`
      TForce Freight

    - `tnt_australia`
      TNT Australia

    - `ups`
      UPS

    - `ups_freight`
      UPS Freight

    - `usps`
      USPS

  - `shipment_tracking.tracking_number` (string)
    The number used to identify the shipment with the carrier responsible for delivery.

- `shipping` (object)
  Shipping address for the order.

  - `shipping.address` (object)
    Shipping address.

    - `shipping.address.city` (string, nullable)
      City, district, suburb, town, or village.

    - `shipping.address.country` (string, nullable)
      Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

    - `shipping.address.line1` (string, nullable)
      Address line 1 (e.g., street, or company name).

    - `shipping.address.line2` (string, nullable)
      Address line 2, such as the apartment, suite, unit, or building.

    - `shipping.address.postal_code` (string, nullable)
      ZIP or postal code.

    - `shipping.address.state` (string, nullable)
      State, county, province, or region ([ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2)).

  - `shipping.amount` (integer)
    A positive integer in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal). Represents the cost for shippingthe order.

  - `shipping.company` (string, nullable)
    Company name.

  - `shipping.currency` (enum)
    Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

  - `shipping.email` (string)
    Customer email. This email will receive Stripe-branded update emails when the status of the order changes.

  - `shipping.name` (string)
    Customer name.

  - `shipping.phone` (string)
    Customer phone (including extension).

- `shipping_method` (string)
  The [Shipping Method](https://docs.stripe.com/docs/api/terminal/hardware_shipping_methods/object.md) for the order.

- `status` (enum)
  The status of the terminal hardware order.
Possible enum values:
  - `canceled`
    Order was canceled. Please create a new order to receive these items.

  - `delivered`
    Order has been delivered!

  - `pending`
    Order has been received and can still be canceled.

  - `ready_to_ship`
    Order has been confirmed and is pending shipment. It cannot be canceled.

  - `shipped`
    Order has been shipped, and can no longer be canceled.

  - `undeliverable`
    One or more of the order’s items could not be delivered.

- `tax` (integer)
  The amount of tax on this order, summed from all the tax amounts.

- `total_tax_amounts` (array of objects)
  The aggregate amounts calculated per tax rate for all of the items on the order.

  - `total_tax_amounts.amount` (integer)
    A positive integer that represents the cost of tax in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal).

  - `total_tax_amounts.inclusive` (boolean)
    Whether the tax rate is inclusive or exclusive

  - `total_tax_amounts.rate` (object)
    The tax rate that applies to this order.

    - `total_tax_amounts.rate.display_name` (string)
      The display name of the tax rate.

    - `total_tax_amounts.rate.jurisdiction` (string, nullable)
      Tax jurisdiction.

    - `total_tax_amounts.rate.percentage` (float)
      The percentage associated with the tax rate.

- `updated` (timestamp, nullable)
  Time at which the object was last updated. Measured in seconds since the Unix epoch.

### The TerminalHardwareOrder object

```json
{
  "id": "thor_1Nj6mu2eZvKYlo2CRG74vB9n",
  "object": "terminal.hardware_order",
  "amount": 13602,
  "created": 1692995962,
  "currency": "usd",
  "hardware_order_items": [
    {
      "amount": 11800,
      "currency": "usd",
      "quantity": 2,
      "terminal_hardware_sku": {
        "id": "thsku_OEu70OWVaQ0DG3",
        "amount": 450,
        "country": "US",
        "currency": "usd",
        "product": "thpr_NGubNsbUoS1oik"
      }
    }
  ],
  "livemode": true,
  "metadata": {},
  "payment_type": "monthly_invoice",
  "po_number": null,
  "shipment_tracking": [],
  "shipping": {
    "address": {
      "city": "San Francisco",
      "country": "US",
      "line1": "1234 Main Street",
      "line2": "",
      "postal_code": "94111",
      "state": "CA"
    },
    "amount": 800,
    "company": "Rocket Rides",
    "currency": "usd",
    "email": "test@example.com",
    "name": "Jenny Rosen",
    "phone": "15555555555"
  },
  "shipping_method": "standard",
  "status": "pending",
  "tax": 1002,
  "total_tax_amounts": [
    {
      "amount": 1002,
      "inclusive": false,
      "rate": {
        "display_name": "Sales Tax",
        "jurisdiction": "LOS ANGELES",
        "percentage": 8.25
      }
    }
  ],
  "updated": null
}
```