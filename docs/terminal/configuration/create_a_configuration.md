# Create a Configuration

Creates a new `Configuration` object.

## Returns

Returns a `Configuration` object if creation succeeds.

## Parameters

- `bbpos_wisepad3` (object, optional)
  An object containing device type specific settings for BBPOS WisePad 3 readers.

  - `bbpos_wisepad3.splashscreen` (string, optional)
    A File ID representing an image you want to display on the reader.

- `bbpos_wisepos_e` (object, optional)
  An object containing device type specific settings for BBPOS WisePOS E readers.

  - `bbpos_wisepos_e.splashscreen` (string, optional)
    A File ID representing an image to display on the reader

- `name` (string, optional)
  Name of the configuration

  The maximum length is 100 characters.

- `offline` (object, optional)
  Configurations for collecting transactions offline.

  - `offline.enabled` (boolean, required)
    Determines whether to allow transactions to be collected while reader is offline. Defaults to false.

- `reader_security` (object, optional)
  Configurations for reader security settings.

  - `reader_security.admin_menu_passcode` (string, optional)
    Passcode used to access a reader’s admin menu.

- `reboot_window` (object, optional)
  Reboot time settings for readers. that support customized reboot time configuration.

  - `reboot_window.end_hour` (integer, required)
    Integer between 0 to 23 that represents the end hour of the reboot time window. The value must be different than the start_hour.

  - `reboot_window.start_hour` (integer, required)
    Integer between 0 to 23 that represents the start hour of the reboot time window.

- `stripe_s700` (object, optional)
  An object containing device type specific settings for Stripe S700 readers.

  - `stripe_s700.splashscreen` (string, optional)
    A File ID representing an image you want to display on the reader.

- `tipping` (object, optional)
  Tipping configurations for readers. supporting on-reader tips

  - `tipping.aed` (object, optional)
    Tipping configuration for AED

    - `tipping.aed.fixed_amounts` (array of integers, optional)
      Fixed amounts displayed when collecting a tip

    - `tipping.aed.percentages` (array of integers, optional)
      Percentages displayed when collecting a tip

    - `tipping.aed.smart_tip_threshold` (integer, optional)
      Below this amount, fixed amounts will be displayed; above it, percentages will be displayed

  - `tipping.aud` (object, optional)
    Tipping configuration for AUD

    - `tipping.aud.fixed_amounts` (array of integers, optional)
      Fixed amounts displayed when collecting a tip

    - `tipping.aud.percentages` (array of integers, optional)
      Percentages displayed when collecting a tip

    - `tipping.aud.smart_tip_threshold` (integer, optional)
      Below this amount, fixed amounts will be displayed; above it, percentages will be displayed

  - `tipping.bgn` (object, optional)
    Tipping configuration for BGN

    - `tipping.bgn.fixed_amounts` (array of integers, optional)
      Fixed amounts displayed when collecting a tip

    - `tipping.bgn.percentages` (array of integers, optional)
      Percentages displayed when collecting a tip

    - `tipping.bgn.smart_tip_threshold` (integer, optional)
      Below this amount, fixed amounts will be displayed; above it, percentages will be displayed

  - `tipping.cad` (object, optional)
    Tipping configuration for CAD

    - `tipping.cad.fixed_amounts` (array of integers, optional)
      Fixed amounts displayed when collecting a tip

    - `tipping.cad.percentages` (array of integers, optional)
      Percentages displayed when collecting a tip

    - `tipping.cad.smart_tip_threshold` (integer, optional)
      Below this amount, fixed amounts will be displayed; above it, percentages will be displayed

  - `tipping.chf` (object, optional)
    Tipping configuration for CHF

    - `tipping.chf.fixed_amounts` (array of integers, optional)
      Fixed amounts displayed when collecting a tip

    - `tipping.chf.percentages` (array of integers, optional)
      Percentages displayed when collecting a tip

    - `tipping.chf.smart_tip_threshold` (integer, optional)
      Below this amount, fixed amounts will be displayed; above it, percentages will be displayed

  - `tipping.czk` (object, optional)
    Tipping configuration for CZK

    - `tipping.czk.fixed_amounts` (array of integers, optional)
      Fixed amounts displayed when collecting a tip

    - `tipping.czk.percentages` (array of integers, optional)
      Percentages displayed when collecting a tip

    - `tipping.czk.smart_tip_threshold` (integer, optional)
      Below this amount, fixed amounts will be displayed; above it, percentages will be displayed

  - `tipping.dkk` (object, optional)
    Tipping configuration for DKK

    - `tipping.dkk.fixed_amounts` (array of integers, optional)
      Fixed amounts displayed when collecting a tip

    - `tipping.dkk.percentages` (array of integers, optional)
      Percentages displayed when collecting a tip

    - `tipping.dkk.smart_tip_threshold` (integer, optional)
      Below this amount, fixed amounts will be displayed; above it, percentages will be displayed

  - `tipping.eur` (object, optional)
    Tipping configuration for EUR

    - `tipping.eur.fixed_amounts` (array of integers, optional)
      Fixed amounts displayed when collecting a tip

    - `tipping.eur.percentages` (array of integers, optional)
      Percentages displayed when collecting a tip

    - `tipping.eur.smart_tip_threshold` (integer, optional)
      Below this amount, fixed amounts will be displayed; above it, percentages will be displayed

  - `tipping.gbp` (object, optional)
    Tipping configuration for GBP

    - `tipping.gbp.fixed_amounts` (array of integers, optional)
      Fixed amounts displayed when collecting a tip

    - `tipping.gbp.percentages` (array of integers, optional)
      Percentages displayed when collecting a tip

    - `tipping.gbp.smart_tip_threshold` (integer, optional)
      Below this amount, fixed amounts will be displayed; above it, percentages will be displayed

  - `tipping.gip` (object, optional)
    Tipping configuration for GIP

    - `tipping.gip.fixed_amounts` (array of integers, optional)
      Fixed amounts displayed when collecting a tip

    - `tipping.gip.percentages` (array of integers, optional)
      Percentages displayed when collecting a tip

    - `tipping.gip.smart_tip_threshold` (integer, optional)
      Below this amount, fixed amounts will be displayed; above it, percentages will be displayed

  - `tipping.hkd` (object, optional)
    Tipping configuration for HKD

    - `tipping.hkd.fixed_amounts` (array of integers, optional)
      Fixed amounts displayed when collecting a tip

    - `tipping.hkd.percentages` (array of integers, optional)
      Percentages displayed when collecting a tip

    - `tipping.hkd.smart_tip_threshold` (integer, optional)
      Below this amount, fixed amounts will be displayed; above it, percentages will be displayed

  - `tipping.huf` (object, optional)
    Tipping configuration for HUF

    - `tipping.huf.fixed_amounts` (array of integers, optional)
      Fixed amounts displayed when collecting a tip

    - `tipping.huf.percentages` (array of integers, optional)
      Percentages displayed when collecting a tip

    - `tipping.huf.smart_tip_threshold` (integer, optional)
      Below this amount, fixed amounts will be displayed; above it, percentages will be displayed

  - `tipping.jpy` (object, optional)
    Tipping configuration for JPY

    - `tipping.jpy.fixed_amounts` (array of integers, optional)
      Fixed amounts displayed when collecting a tip

    - `tipping.jpy.percentages` (array of integers, optional)
      Percentages displayed when collecting a tip

    - `tipping.jpy.smart_tip_threshold` (integer, optional)
      Below this amount, fixed amounts will be displayed; above it, percentages will be displayed

  - `tipping.mxn` (object, optional)
    Tipping configuration for MXN

    - `tipping.mxn.fixed_amounts` (array of integers, optional)
      Fixed amounts displayed when collecting a tip

    - `tipping.mxn.percentages` (array of integers, optional)
      Percentages displayed when collecting a tip

    - `tipping.mxn.smart_tip_threshold` (integer, optional)
      Below this amount, fixed amounts will be displayed; above it, percentages will be displayed

  - `tipping.myr` (object, optional)
    Tipping configuration for MYR

    - `tipping.myr.fixed_amounts` (array of integers, optional)
      Fixed amounts displayed when collecting a tip

    - `tipping.myr.percentages` (array of integers, optional)
      Percentages displayed when collecting a tip

    - `tipping.myr.smart_tip_threshold` (integer, optional)
      Below this amount, fixed amounts will be displayed; above it, percentages will be displayed

  - `tipping.nok` (object, optional)
    Tipping configuration for NOK

    - `tipping.nok.fixed_amounts` (array of integers, optional)
      Fixed amounts displayed when collecting a tip

    - `tipping.nok.percentages` (array of integers, optional)
      Percentages displayed when collecting a tip

    - `tipping.nok.smart_tip_threshold` (integer, optional)
      Below this amount, fixed amounts will be displayed; above it, percentages will be displayed

  - `tipping.nzd` (object, optional)
    Tipping configuration for NZD

    - `tipping.nzd.fixed_amounts` (array of integers, optional)
      Fixed amounts displayed when collecting a tip

    - `tipping.nzd.percentages` (array of integers, optional)
      Percentages displayed when collecting a tip

    - `tipping.nzd.smart_tip_threshold` (integer, optional)
      Below this amount, fixed amounts will be displayed; above it, percentages will be displayed

  - `tipping.pln` (object, optional)
    Tipping configuration for PLN

    - `tipping.pln.fixed_amounts` (array of integers, optional)
      Fixed amounts displayed when collecting a tip

    - `tipping.pln.percentages` (array of integers, optional)
      Percentages displayed when collecting a tip

    - `tipping.pln.smart_tip_threshold` (integer, optional)
      Below this amount, fixed amounts will be displayed; above it, percentages will be displayed

  - `tipping.ron` (object, optional)
    Tipping configuration for RON

    - `tipping.ron.fixed_amounts` (array of integers, optional)
      Fixed amounts displayed when collecting a tip

    - `tipping.ron.percentages` (array of integers, optional)
      Percentages displayed when collecting a tip

    - `tipping.ron.smart_tip_threshold` (integer, optional)
      Below this amount, fixed amounts will be displayed; above it, percentages will be displayed

  - `tipping.sek` (object, optional)
    Tipping configuration for SEK

    - `tipping.sek.fixed_amounts` (array of integers, optional)
      Fixed amounts displayed when collecting a tip

    - `tipping.sek.percentages` (array of integers, optional)
      Percentages displayed when collecting a tip

    - `tipping.sek.smart_tip_threshold` (integer, optional)
      Below this amount, fixed amounts will be displayed; above it, percentages will be displayed

  - `tipping.sgd` (object, optional)
    Tipping configuration for SGD

    - `tipping.sgd.fixed_amounts` (array of integers, optional)
      Fixed amounts displayed when collecting a tip

    - `tipping.sgd.percentages` (array of integers, optional)
      Percentages displayed when collecting a tip

    - `tipping.sgd.smart_tip_threshold` (integer, optional)
      Below this amount, fixed amounts will be displayed; above it, percentages will be displayed

  - `tipping.usd` (object, optional)
    Tipping configuration for USD

    - `tipping.usd.fixed_amounts` (array of integers, optional)
      Fixed amounts displayed when collecting a tip

    - `tipping.usd.percentages` (array of integers, optional)
      Percentages displayed when collecting a tip

    - `tipping.usd.smart_tip_threshold` (integer, optional)
      Below this amount, fixed amounts will be displayed; above it, percentages will be displayed

- `verifone_p400` (object, optional)
  An object containing device type specific settings for Verifone P400 readers.

  - `verifone_p400.splashscreen` (string, optional)
    A File ID representing an image you want to display on the reader.

- `wifi` (object, optional)
  Configurations for connecting to a WiFi network.

  - `wifi.type` (enum, required)
    Security type of the WiFi network. Fill out the hash with the corresponding name to provide the set of credentials for this security type.
Possible enum values:
    - `enterprise_eap_peap`
      WPA-Enterprise network using EAP-PEAP authentication (username/password).

    - `enterprise_eap_tls`
      WPA-Enterprise network using EAP-TLS authentication (certificates).

    - `personal_psk`
      WPA-Personal network using PSK authentication (password).

  - `wifi.enterprise_eap_peap` (object, optional)
    Credentials for a WPA-Enterprise WiFi network using the EAP-PEAP authentication method.

    - `wifi.enterprise_eap_peap.password` (string, required)
      Password for connecting to the WiFi network

    - `wifi.enterprise_eap_peap.ssid` (string, required)
      Name of the WiFi network

    - `wifi.enterprise_eap_peap.username` (string, required)
      Username for connecting to the WiFi network

    - `wifi.enterprise_eap_peap.ca_certificate_file` (string, optional)
      A File ID representing a PEM file containing the server certificate

  - `wifi.enterprise_eap_tls` (object, optional)
    Credentials for a WPA-Enterprise WiFi network using the EAP-TLS authentication method.

    - `wifi.enterprise_eap_tls.client_certificate_file` (string, required)
      A File ID representing a PEM file containing the client certificate

    - `wifi.enterprise_eap_tls.private_key_file` (string, required)
      A File ID representing a PEM file containing the client RSA private key

    - `wifi.enterprise_eap_tls.ssid` (string, required)
      Name of the WiFi network

    - `wifi.enterprise_eap_tls.ca_certificate_file` (string, optional)
      A File ID representing a PEM file containing the server certificate

    - `wifi.enterprise_eap_tls.private_key_file_password` (string, optional)
      Password for the private key file

  - `wifi.personal_psk` (object, optional)
    Credentials for a WPA-Personal WiFi network.

    - `wifi.personal_psk.password` (string, required)
      Password for connecting to the WiFi network

      The maximum length is 63 characters.

    - `wifi.personal_psk.ssid` (string, required)
      Name of the WiFi network

```curl
curl -X POST https://api.stripe.com/v1/terminal/configurations \
  -u "<<YOUR_SECRET_KEY>>"
```

```cli
stripe terminal configurations create
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

configuration = client.v1.terminal.configurations.create()
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

configuration = client.v1.terminal.configurations.create()
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$configuration = $stripe->terminal->configurations->create([]);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

ConfigurationCreateParams params = ConfigurationCreateParams.builder().build();

Configuration configuration = client.v1().terminal().configurations().create(params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const configuration = await stripe.terminal.configurations.create();
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.TerminalConfigurationCreateParams{}
result, err := sc.V1TerminalConfigurations.Create(context.TODO(), params)
```

```dotnet
var options = new Stripe.Terminal.ConfigurationCreateOptions();
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Terminal.Configurations;
Stripe.Terminal.Configuration configuration = service.Create(options);
```

### Response

```json
{
  "id": "tmc_FQqbaQCiy0m1xc",
  "object": "terminal.configuration",
  "is_account_default": false,
  "livemode": false
}
```