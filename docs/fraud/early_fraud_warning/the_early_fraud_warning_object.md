# The Early Fraud Warning object

## Attributes

- `id` (string)
  Unique identifier for the object.

- `object` (string)
  String representing the object’s type. Objects of the same type share the same value.

- `actionable` (boolean)
  An EFW is actionable if it has not received a dispute and has not been fully refunded. You may wish to proactively refund a charge that receives an EFW, in order to avoid receiving a dispute later.

- `charge` (string)
  ID of the charge this early fraud warning is for, optionally expanded.

- `created` (timestamp)
  Time at which the object was created. Measured in seconds since the Unix epoch.

- `fraud_type` (string)
  The type of fraud labelled by the issuer. One of `card_never_received`, `fraudulent_card_application`, `made_with_counterfeit_card`, `made_with_lost_card`, `made_with_stolen_card`, `misc`, `unauthorized_use_of_card`.

- `livemode` (boolean)
  Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.

- `payment_intent` (string, nullable)
  ID of the Payment Intent this early fraud warning is for, optionally expanded.

### The Early Fraud Warning object

```json
{
  "id": "issfr_1NnrwHBw2dPENLoi9lnhV3RQ",
  "object": "radar.early_fraud_warning",
  "actionable": true,
  "charge": "ch_1234",
  "created": 123456789,
  "fraud_type": "misc",
  "livemode": false
}
```