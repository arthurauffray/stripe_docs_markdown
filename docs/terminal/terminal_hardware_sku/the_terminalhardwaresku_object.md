# The TerminalHardwareSKU object

## Attributes

- `id` (string)
  Unique identifier for the object.

- `object` (string)
  String representing the object’s type. Objects of the same type share the same value.

- `amount` (integer)
  The price of this SKU.

- `country` (enum)
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

- `currency` (enum)
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

- `orderable` (integer)
  The maximum quantity of this TerminalHardwareSKU that can be ordered. This will change over time due to inventory and other constraints.

- `product` (string)
  ID of the product for this SKU.

- `provider` (enum, nullable)
  The provider associated with this SKU.
Possible enum values:
  - `stripe`
    The Stripe provider

- `status` (enum)
  The SKU’s status.
Possible enum values:
  - `available`
    Available for new orders.

  - `unavailable`
    Can no longer be used for order creation.

- `unavailable_after` (integer, nullable)
  A UNIX timestamp, after which time this SKU has a status of `unavailable` and it can’t be used for order creation. If absent, we have no plans to make this SKU unavailable.

### The TerminalHardwareSKU object

```json
{
  "id": "thsku_OEu70OWVaQ0DG3",
  "object": "terminal.hardware_sku",
  "amount": 450,
  "country": "US",
  "currency": "usd",
  "orderable": 100,
  "product": "thpr_NGubNsbUoS1oik",
  "status": "available",
  "unavailable_after": null
}
```