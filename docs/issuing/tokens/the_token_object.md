# The Token object

## Attributes

- `id` (string)
  Unique identifier for the object.

- `object` (string)
  String representing the object’s type. Objects of the same type share the same value.

- `card` (string)
  Card associated with this token.

- `created` (timestamp)
  Time at which the object was created. Measured in seconds since the Unix epoch.

- `device_fingerprint` (string, nullable)
  The hashed ID derived from the device ID from the card network associated with the token.

- `last4` (string, nullable)
  The last four digits of the token.

- `livemode` (boolean)
  Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.

- `network` (enum)
  The token service provider / card network associated with the token.
Possible enum values:
  - `mastercard`
    MasterCard token service provider.

  - `visa`
    Visa token service provider.

- `network_data` (object, nullable)
  Additional details obtained from the network about the token, primarily related to the token creation process. For security reasons, this is only available to view in the first 24 hours after token creation, based on the `created` value, and will be omitted unless you explicitly request it with [the `expand` parameter](https://docs.stripe.com/docs/api/expanding_objects.md). Additionally, it’s only available via the [“Retrieve a token” endpoint](https://docs.stripe.com/docs/api/issuing/tokens/retrieve.md) and [“Update a token status” endpoint](https://docs.stripe.com/docs/api/issuing/tokens/update.md).

  - `network_data.device` (object, nullable)
    Data about the device at the instance of provisioning this token.

    - `network_data.device.device_fingerprint` (string, nullable)
      An obfuscated ID derived from the device ID.

    - `network_data.device.ip_address` (string, nullable)
      The IP address of the device at provisioning time.

    - `network_data.device.location` (string, nullable)
      The geographic latitude/longitude coordinates of the device at provisioning time. The format is [±]decimal/[±]decimal.

    - `network_data.device.name` (string, nullable)
      The name of the device used for tokenization.

    - `network_data.device.phone_number` (string, nullable)
      The phone number of the device used for tokenization.

    - `network_data.device.type` (enum, nullable)
      The type of device used for tokenization.
Possible enum values:
      - `other`
        Device is some other form factor, such as tablet or laptop.

      - `phone`
        Device is a mobile phone or phone form factor.

      - `watch`
        Device is a watch or watch form factor.

  - `network_data.mastercard` (object, nullable)
    If this is a `mastercard` network token, this hash contains tokenization data specific to this card network.

    - `network_data.mastercard.card_reference_id` (string, nullable)
      A unique reference ID from MasterCard to represent the card account number.

    - `network_data.mastercard.token_reference_id` (string)
      The network-unique identifier for the token.

    - `network_data.mastercard.token_requestor_id` (string)
      The ID of the entity requesting tokenization, specific to MasterCard.

    - `network_data.mastercard.token_requestor_name` (string, nullable)
      The name of the entity requesting tokenization, if known. This is directly provided from MasterCard.

  - `network_data.type` (enum)
    The network that the token is associated with. An additional hash is included with a name matching this value, containing tokenization data specific to the card network.
Possible enum values:
    - `mastercard`
      MasterCard token service provider.

    - `visa`
      Visa token service provider.

  - `network_data.visa` (object, nullable)
    If this is a `visa` network token, this hash contains tokenization data specific to this card network.

    - `network_data.visa.card_reference_id` (string)
      A unique reference ID from Visa to represent the card account number.

    - `network_data.visa.token_reference_id` (string)
      The network-unique identifier for the token.

    - `network_data.visa.token_requestor_id` (string)
      The ID of the entity requesting tokenization, specific to Visa.

    - `network_data.visa.token_risk_score` (string, nullable)
      Degree of risk associated with the token between `01` and `99`, with higher number indicating higher risk. A `00` value indicates the token was not scored by Visa.

  - `network_data.wallet_provider` (object, nullable)
    The digital wallet used for provisioning this token.

    - `network_data.wallet_provider.account_id` (string, nullable)
      The wallet provider-given account ID of the digital wallet the token belongs to.

    - `network_data.wallet_provider.account_trust_score` (integer, nullable)
      An evaluation on the trustworthiness of the wallet account between 1 and 5. A higher score indicates more trustworthy.

    - `network_data.wallet_provider.card_number_source` (enum, nullable)
      The method used for tokenizing a card.
Possible enum values:
      - `app`
        The card was provisioned from a mobile application.

      - `manual`
        The card details were manually provided to the wallet provider. This includes manual card number entry by the cardholder, card number detection via OCR, and tapping a physical contactless card on a mobile device.

      - `on_file`
        The card data stored on file was used for provisioning.

      - `other`
        The token was provisioned by another method.

    - `network_data.wallet_provider.cardholder_address` (object, nullable)
      The address of the cardholder tokenizing the card.

      - `network_data.wallet_provider.cardholder_address.line1` (string)
        The street address of the cardholder tokenizing the card.

      - `network_data.wallet_provider.cardholder_address.postal_code` (string)
        The postal code of the cardholder tokenizing the card.

    - `network_data.wallet_provider.cardholder_name` (string, nullable)
      The name of the cardholder tokenizing the card.

    - `network_data.wallet_provider.device_trust_score` (integer, nullable)
      An evaluation on the trustworthiness of the device. A higher score indicates more trustworthy.

    - `network_data.wallet_provider.hashed_account_email_address` (string, nullable)
      The hashed email address of the cardholder’s account with the wallet provider.

    - `network_data.wallet_provider.reason_codes` (array of enums, nullable)
      The reasons for suggested tokenization given by the card network.
Possible enum values:
      - `account_card_too_new`
        Cardholders’ wallet account/card pair is newer than date threshold.

      - `account_recently_changed`
        Changes made to account data within the date threshold.

      - `account_too_new`
        Cardholders’ wallet account is too new relative to provisioning request.

      - `account_too_new_since_launch`
        Cardholders’ wallet account is too new relative to launch.

      - `additional_device`
        The digitization is for an additional device for the same Account PAN and consumer account. There must be a currently active (not suspended) Token that was previously digitized and activated on an existing device for the same Account PAN and consumer account.

      - `data_expired`
        Issuer encrypted payment instrument data has expired.

      - `defer_id_v_decision`
        Issuer preferred to defer ID&V decision to token creation time.

      - `device_recently_lost`
        Device was put in lost mode.

      - `good_activity_history`
        There has been financial activity linked to the account for at least and within a period of not less than six months; no suspicious activity is linked to the account within a period of at least one year.

      - `has_suspended_tokens`
        Suspended cards in the secure element.

      - `high_risk`
        Suspect fraud.

      - `inactive_account`
        Account has not had activity in the last year.

      - `long_account_tenure`
        Account has existed for an extended period of not less than one year. A Payment App Provider may determine a longer account tenure to qualify for this reason.

      - `low_account_score`
        The account trust score is low.

      - `low_device_score`
        The device trust score is low.

      - `low_phone_number_score`
        Phone score is low.

      - `network_service_error`
        Errors between Stripe and network unrelated to content. Can be related to formatting/schema.

      - `outside_home_territory`
        Device provisioning location outside of the cardholder’s wallet account home country.

      - `provisioning_cardholder_mismatch`
        Pushing to a different user than the cardholder. If a passcode was included in issuer’s encrypted payment instrument data, then it matched the user provided value.

      - `provisioning_device_and_cardholder_mismatch`
        User/device that was intended to receive the encrypted payment instrument data is different than the one that is provisioning the token.

      - `provisioning_device_mismatch`
        Sending and receiving devices are different. If a passcode was included in issuer’s encrypted payment instrument data, then it matched the user provided value.

      - `same_device_no_prior_authentication`
        Sending and receiving devices are the same, but without any upfront authentication or passcode verification.

      - `same_device_successful_prior_authentication`
        Sending and receiving devices are the same, but with successful upfront authentication or passcode verification.

      - `software_update`
        The digitization has been requested due to an authenticated operating system or other software update being installed on the device, causing mobile payment data to be wiped and unable to be restored. This digitization must be for the same device ID to which a Token was previously digitized and activated for the same Account PAN and consumer account.

      - `suspicious_activity`
        Suspicious transactions linked to this account.

      - `too_many_different_cardholders`
        The card provisioning request contains a distinct name in excess of the permitted threshold.

      - `too_many_recent_attempts`
        The number of provisioning attempts on this device exceeds threshold.

      - `too_many_recent_tokens`
        There have been more than the threshold number of different cards attempted at provisioning to this phone.

    - `network_data.wallet_provider.suggested_decision` (enum, nullable)
      The recommendation on responding to the tokenization request.
Possible enum values:
      - `approve`
        The card network suggests approving the provisioning request.

      - `decline`
        The card network suggests declining the provisioning request.

      - `require_auth`
        The card network suggests performing additional identity verification in order to approve tokenization.

    - `network_data.wallet_provider.suggested_decision_version` (string, nullable)
      The version of the standard for mapping reason codes followed by the wallet provider.

- `network_updated_at` (timestamp)
  Time at which the token was last updated by the card network. Measured in seconds since the Unix epoch.

- `status` (enum)
  The usage state of the token.
Possible enum values:
  - `active`
    Token is provisioned and usable for payments.

  - `deleted`
    Terminal state. Token can no longer be used.

  - `requested`
    Token has been requested to be provisioned, but has not completed the activation process.

  - `suspended`
    Token temporarily cannot be used for payments.

- `wallet_provider` (enum, nullable)
  The digital wallet for this token, if one was used.
Possible enum values:
  - `apple_pay`
    Apple Pay.

  - `google_pay`
    Google Pay.

  - `samsung_pay`
    Samsung Pay.

### The Token object

```json
{
  "id": "intok_1MzDbE2eZvKYlo2C26a98MDg",
  "object": "issuing.token",
  "card": "ic_1MytUz2eZvKYlo2CZCn5fuvZ",
  "created": 1682059060,
  "network_updated_at": 1682059060,
  "livemode": false,
  "status": "active",
  "last4": "2424",
  "token_service_provider": "visa",
  "wallet_provider": "apple_pay",
  "device_fingerprint": "intd_1MzDbE2eZvKYcp3095svdf"
}
```