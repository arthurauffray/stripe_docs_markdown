# The Configuration object

## Attributes

- `id` (string)
  Unique identifier for the object.

- `object` (string)
  String representing the object’s type. Objects of the same type share the same value.

- `bbpos_wisepad3` (object, nullable)
  An object containing device type specific settings for BBPOS WisePad 3

  - `bbpos_wisepad3.splashscreen` (string, nullable)
    A File ID representing an image to display on the reader

- `bbpos_wisepos_e` (object, nullable)
  An object containing device type specific settings for BBPOS WisePOS E

  - `bbpos_wisepos_e.splashscreen` (string, nullable)
    A File ID representing an image to display on the reader

- `is_account_default` (boolean, nullable)
  Whether this Configuration is the default for your account

- `livemode` (boolean)
  Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.

- `name` (string, nullable)
  String indicating the name of the Configuration object, set by the user

- `offline` (object, nullable)
  Configurations for collecting transactions offline.

  - `offline.enabled` (boolean, nullable)
    Determines whether to allow transactions to be collected while reader is offline. Defaults to false.

- `reader_security` (object, nullable)
  Configurations for reader security settings.

  - `reader_security.admin_menu_passcode` (string)
    Passcode used to access a reader’s admin menu.

- `reboot_window` (object, nullable)
  Reboot time settings for readers that support customized reboot time configuration.

  - `reboot_window.end_hour` (integer)
    Integer between 0 to 23 that represents the end hour of the reboot time window. The value must be different than the start_hour.

  - `reboot_window.start_hour` (integer)
    Integer between 0 to 23 that represents the start hour of the reboot time window.

- `stripe_s700` (object, nullable)
  An object containing device type specific settings for Stripe S700

  - `stripe_s700.splashscreen` (string, nullable)
    A File ID representing an image to display on the reader

- `tipping` (object, nullable)
  On-reader tipping settings

  - `tipping.aed` (object, nullable)
    Tipping configuration for AED

    - `tipping.aed.fixed_amounts` (array of integers, nullable)
      Fixed amounts displayed when collecting a tip

    - `tipping.aed.percentages` (array of integers, nullable)
      Percentages displayed when collecting a tip

    - `tipping.aed.smart_tip_threshold` (integer, nullable)
      Below this amount, fixed amounts will be displayed; above it, percentages will be displayed

  - `tipping.aud` (object, nullable)
    Tipping configuration for AUD

    - `tipping.aud.fixed_amounts` (array of integers, nullable)
      Fixed amounts displayed when collecting a tip

    - `tipping.aud.percentages` (array of integers, nullable)
      Percentages displayed when collecting a tip

    - `tipping.aud.smart_tip_threshold` (integer, nullable)
      Below this amount, fixed amounts will be displayed; above it, percentages will be displayed

  - `tipping.bgn` (object, nullable)
    Tipping configuration for BGN

    - `tipping.bgn.fixed_amounts` (array of integers, nullable)
      Fixed amounts displayed when collecting a tip

    - `tipping.bgn.percentages` (array of integers, nullable)
      Percentages displayed when collecting a tip

    - `tipping.bgn.smart_tip_threshold` (integer, nullable)
      Below this amount, fixed amounts will be displayed; above it, percentages will be displayed

  - `tipping.cad` (object, nullable)
    Tipping configuration for CAD

    - `tipping.cad.fixed_amounts` (array of integers, nullable)
      Fixed amounts displayed when collecting a tip

    - `tipping.cad.percentages` (array of integers, nullable)
      Percentages displayed when collecting a tip

    - `tipping.cad.smart_tip_threshold` (integer, nullable)
      Below this amount, fixed amounts will be displayed; above it, percentages will be displayed

  - `tipping.chf` (object, nullable)
    Tipping configuration for CHF

    - `tipping.chf.fixed_amounts` (array of integers, nullable)
      Fixed amounts displayed when collecting a tip

    - `tipping.chf.percentages` (array of integers, nullable)
      Percentages displayed when collecting a tip

    - `tipping.chf.smart_tip_threshold` (integer, nullable)
      Below this amount, fixed amounts will be displayed; above it, percentages will be displayed

  - `tipping.czk` (object, nullable)
    Tipping configuration for CZK

    - `tipping.czk.fixed_amounts` (array of integers, nullable)
      Fixed amounts displayed when collecting a tip

    - `tipping.czk.percentages` (array of integers, nullable)
      Percentages displayed when collecting a tip

    - `tipping.czk.smart_tip_threshold` (integer, nullable)
      Below this amount, fixed amounts will be displayed; above it, percentages will be displayed

  - `tipping.dkk` (object, nullable)
    Tipping configuration for DKK

    - `tipping.dkk.fixed_amounts` (array of integers, nullable)
      Fixed amounts displayed when collecting a tip

    - `tipping.dkk.percentages` (array of integers, nullable)
      Percentages displayed when collecting a tip

    - `tipping.dkk.smart_tip_threshold` (integer, nullable)
      Below this amount, fixed amounts will be displayed; above it, percentages will be displayed

  - `tipping.eur` (object, nullable)
    Tipping configuration for EUR

    - `tipping.eur.fixed_amounts` (array of integers, nullable)
      Fixed amounts displayed when collecting a tip

    - `tipping.eur.percentages` (array of integers, nullable)
      Percentages displayed when collecting a tip

    - `tipping.eur.smart_tip_threshold` (integer, nullable)
      Below this amount, fixed amounts will be displayed; above it, percentages will be displayed

  - `tipping.gbp` (object, nullable)
    Tipping configuration for GBP

    - `tipping.gbp.fixed_amounts` (array of integers, nullable)
      Fixed amounts displayed when collecting a tip

    - `tipping.gbp.percentages` (array of integers, nullable)
      Percentages displayed when collecting a tip

    - `tipping.gbp.smart_tip_threshold` (integer, nullable)
      Below this amount, fixed amounts will be displayed; above it, percentages will be displayed

  - `tipping.gip` (object, nullable)
    Tipping configuration for GIP

    - `tipping.gip.fixed_amounts` (array of integers, nullable)
      Fixed amounts displayed when collecting a tip

    - `tipping.gip.percentages` (array of integers, nullable)
      Percentages displayed when collecting a tip

    - `tipping.gip.smart_tip_threshold` (integer, nullable)
      Below this amount, fixed amounts will be displayed; above it, percentages will be displayed

  - `tipping.hkd` (object, nullable)
    Tipping configuration for HKD

    - `tipping.hkd.fixed_amounts` (array of integers, nullable)
      Fixed amounts displayed when collecting a tip

    - `tipping.hkd.percentages` (array of integers, nullable)
      Percentages displayed when collecting a tip

    - `tipping.hkd.smart_tip_threshold` (integer, nullable)
      Below this amount, fixed amounts will be displayed; above it, percentages will be displayed

  - `tipping.huf` (object, nullable)
    Tipping configuration for HUF

    - `tipping.huf.fixed_amounts` (array of integers, nullable)
      Fixed amounts displayed when collecting a tip

    - `tipping.huf.percentages` (array of integers, nullable)
      Percentages displayed when collecting a tip

    - `tipping.huf.smart_tip_threshold` (integer, nullable)
      Below this amount, fixed amounts will be displayed; above it, percentages will be displayed

  - `tipping.jpy` (object, nullable)
    Tipping configuration for JPY

    - `tipping.jpy.fixed_amounts` (array of integers, nullable)
      Fixed amounts displayed when collecting a tip

    - `tipping.jpy.percentages` (array of integers, nullable)
      Percentages displayed when collecting a tip

    - `tipping.jpy.smart_tip_threshold` (integer, nullable)
      Below this amount, fixed amounts will be displayed; above it, percentages will be displayed

  - `tipping.mxn` (object, nullable)
    Tipping configuration for MXN

    - `tipping.mxn.fixed_amounts` (array of integers, nullable)
      Fixed amounts displayed when collecting a tip

    - `tipping.mxn.percentages` (array of integers, nullable)
      Percentages displayed when collecting a tip

    - `tipping.mxn.smart_tip_threshold` (integer, nullable)
      Below this amount, fixed amounts will be displayed; above it, percentages will be displayed

  - `tipping.myr` (object, nullable)
    Tipping configuration for MYR

    - `tipping.myr.fixed_amounts` (array of integers, nullable)
      Fixed amounts displayed when collecting a tip

    - `tipping.myr.percentages` (array of integers, nullable)
      Percentages displayed when collecting a tip

    - `tipping.myr.smart_tip_threshold` (integer, nullable)
      Below this amount, fixed amounts will be displayed; above it, percentages will be displayed

  - `tipping.nok` (object, nullable)
    Tipping configuration for NOK

    - `tipping.nok.fixed_amounts` (array of integers, nullable)
      Fixed amounts displayed when collecting a tip

    - `tipping.nok.percentages` (array of integers, nullable)
      Percentages displayed when collecting a tip

    - `tipping.nok.smart_tip_threshold` (integer, nullable)
      Below this amount, fixed amounts will be displayed; above it, percentages will be displayed

  - `tipping.nzd` (object, nullable)
    Tipping configuration for NZD

    - `tipping.nzd.fixed_amounts` (array of integers, nullable)
      Fixed amounts displayed when collecting a tip

    - `tipping.nzd.percentages` (array of integers, nullable)
      Percentages displayed when collecting a tip

    - `tipping.nzd.smart_tip_threshold` (integer, nullable)
      Below this amount, fixed amounts will be displayed; above it, percentages will be displayed

  - `tipping.pln` (object, nullable)
    Tipping configuration for PLN

    - `tipping.pln.fixed_amounts` (array of integers, nullable)
      Fixed amounts displayed when collecting a tip

    - `tipping.pln.percentages` (array of integers, nullable)
      Percentages displayed when collecting a tip

    - `tipping.pln.smart_tip_threshold` (integer, nullable)
      Below this amount, fixed amounts will be displayed; above it, percentages will be displayed

  - `tipping.ron` (object, nullable)
    Tipping configuration for RON

    - `tipping.ron.fixed_amounts` (array of integers, nullable)
      Fixed amounts displayed when collecting a tip

    - `tipping.ron.percentages` (array of integers, nullable)
      Percentages displayed when collecting a tip

    - `tipping.ron.smart_tip_threshold` (integer, nullable)
      Below this amount, fixed amounts will be displayed; above it, percentages will be displayed

  - `tipping.sek` (object, nullable)
    Tipping configuration for SEK

    - `tipping.sek.fixed_amounts` (array of integers, nullable)
      Fixed amounts displayed when collecting a tip

    - `tipping.sek.percentages` (array of integers, nullable)
      Percentages displayed when collecting a tip

    - `tipping.sek.smart_tip_threshold` (integer, nullable)
      Below this amount, fixed amounts will be displayed; above it, percentages will be displayed

  - `tipping.sgd` (object, nullable)
    Tipping configuration for SGD

    - `tipping.sgd.fixed_amounts` (array of integers, nullable)
      Fixed amounts displayed when collecting a tip

    - `tipping.sgd.percentages` (array of integers, nullable)
      Percentages displayed when collecting a tip

    - `tipping.sgd.smart_tip_threshold` (integer, nullable)
      Below this amount, fixed amounts will be displayed; above it, percentages will be displayed

  - `tipping.usd` (object, nullable)
    Tipping configuration for USD

    - `tipping.usd.fixed_amounts` (array of integers, nullable)
      Fixed amounts displayed when collecting a tip

    - `tipping.usd.percentages` (array of integers, nullable)
      Percentages displayed when collecting a tip

    - `tipping.usd.smart_tip_threshold` (integer, nullable)
      Below this amount, fixed amounts will be displayed; above it, percentages will be displayed

- `verifone_p400` (object, nullable)
  An object containing device type specific settings for Verifone P400

  - `verifone_p400.splashscreen` (string, nullable)
    A File ID representing an image to display on the reader

- `wifi` (object, nullable)
  Configurations for connecting to a WiFi network.

  - `wifi.enterprise_eap_peap` (object, nullable)
    Credentials for a WPA-Enterprise WiFi network using the EAP-PEAP authentication method.

    - `wifi.enterprise_eap_peap.ca_certificate_file` (string, nullable)
      A File ID representing a PEM file containing the server certificate

    - `wifi.enterprise_eap_peap.password` (string)
      Password for connecting to the WiFi network

    - `wifi.enterprise_eap_peap.ssid` (string)
      Name of the WiFi network

    - `wifi.enterprise_eap_peap.username` (string)
      Username for connecting to the WiFi network

  - `wifi.enterprise_eap_tls` (object, nullable)
    Credentials for a WPA-Enterprise WiFi network using the EAP-TLS authentication method.

    - `wifi.enterprise_eap_tls.ca_certificate_file` (string, nullable)
      A File ID representing a PEM file containing the server certificate

    - `wifi.enterprise_eap_tls.client_certificate_file` (string)
      A File ID representing a PEM file containing the client certificate

    - `wifi.enterprise_eap_tls.private_key_file` (string)
      A File ID representing a PEM file containing the client RSA private key

    - `wifi.enterprise_eap_tls.private_key_file_password` (string, nullable)
      Password for the private key file

    - `wifi.enterprise_eap_tls.ssid` (string)
      Name of the WiFi network

  - `wifi.personal_psk` (object, nullable)
    Credentials for a WPA-Personal WiFi network.

    - `wifi.personal_psk.password` (string)
      Password for connecting to the WiFi network

    - `wifi.personal_psk.ssid` (string)
      Name of the WiFi network

  - `wifi.type` (enum)
    Security type of the WiFi network. The hash with the corresponding name contains the credentials for this security type.
Possible enum values:
    - `enterprise_eap_peap`
      WPA-Enterprise network using EAP-PEAP authentication (username/password).

    - `enterprise_eap_tls`
      WPA-Enterprise network using EAP-TLS authentication (certificates).

    - `personal_psk`
      WPA-Personal network using PSK authentication (password).

### The Configuration object

```json
{
  "id": "tmc_FQqbaQCiy0m1xc",
  "object": "terminal.configuration",
  "is_account_default": false,
  "livemode": false
}
```