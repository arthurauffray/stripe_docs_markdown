# The Terminal Hardware Shipping Method object

## Attributes

- `id` (string)
  Unique identifier for the object.

- `object` (string)
  String representing the object’s type. Objects of the same type share the same value.

- `country` (enum)
  The country in which this Shipping Method is available.
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

- `estimated_delivery_window` (object)
  The estimated delivery period containing the estimated minimum and maximum delivery dates. These dates are not guaranteed.

  - `estimated_delivery_window.maximum_date` (string)
    Maximum estimated delivery date in ISO 8601 format.

  - `estimated_delivery_window.minimum_date` (string)
    Minimum estimated delivery date in ISO 8601 format.

- `name` (enum)
  The name of the Terminal Hardware Shipping Method.
Possible enum values:
  - `express`
    Express

  - `priority`
    Priority

  - `standard`
    Standard

- `provider` (enum, nullable)
  The provider associated with this ShippingMethod.
Possible enum values:
  - `stripe`
    The Stripe provider

- `status` (enum)
  The Shipping Method’s status.
Possible enum values:
  - `available`
    Available for new orders.

  - `unavailable`
    Can no longer be used for order creation.

- `unavailable_after` (integer, nullable)
  A UNIX timestamp, after which time this Shipping Method has a status of `unavailable` and it can’t be used for order creation. If absent, we have no plans to make this Shipping Method unavailable.

### The Terminal Hardware Shipping Method object

```json
{
  "id": "thsm_MfuTjLaPEgXMa4",
  "object": "terminal.hardware_shipping_method",
  "country": "US",
  "estimated_delivery_window": {
    "maximum_date": "2023-10-03",
    "minimum_date": "2023-10-03"
  },
  "name": "standard",
  "status": "available",
  "unavailable_after": null
}
```