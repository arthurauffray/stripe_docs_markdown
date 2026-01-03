# The Event object

## Attributes

- `id` (string)
  Unique identifier for the object.

- `object` (string)
  String representing the object’s type. Objects of the same type share the same value.

- `account` (string, nullable)
  The connected account that originates the event.

- `api_version` (string, nullable)
  The Stripe API version used to render `data` when the event was created. The contents of `data` never change, so this value remains static regardless of the API version currently in use. This property is populated only for events created on or after October 31, 2014.

- `context` (string, nullable)
  Authentication context needed to fetch the event or related object.

- `created` (timestamp)
  Time at which the object was created. Measured in seconds since the Unix epoch.

- `data` (object)
  Object containing data associated with the event.

  - `data.object` (object)
    Object containing the API resource relevant to the event. For example, an `invoice.created` event will have a full [invoice object](https://docs.stripe.com/api/events/object.md#invoice_object) as the value of the object key.

  - `data.previous_attributes` (object, nullable)
    Object containing the names of the updated attributes and their values prior to the event (only included in events of type `*.updated`). If an array attribute has any updated elements, this object contains the entire array. In Stripe API versions 2017-04-06 or earlier, an updated array attribute in this object includes only the updated array elements.

- `livemode` (boolean)
  Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.

- `pending_webhooks` (integer)
  Number of webhooks that haven’t been successfully delivered (for example, to return a 20x response) to the URLs you specify.

- `request` (object, nullable)
  Information on the API request that triggers the event.

  - `request.id` (string, nullable)
    ID of the API request that caused the event. If null, the event was automatic (e.g., Stripe’s automatic subscription handling). Request logs are available in the [dashboard](https://dashboard.stripe.com/logs), but currently not in the API.

  - `request.idempotency_key` (string, nullable)
    The idempotency key transmitted during the request, if any. *Note: This property is populated only for events on or after May 23, 2017*.

- `type` (string)
  Description of the event (for example, `invoice.created` or `charge.refunded`).

### The Event object

```json
{
  "id": "evt_1NG8Du2eZvKYlo2CUI79vXWy",
  "object": "event",
  "api_version": "2019-02-19",
  "created": 1686089970,
  "data": {
    "object": {
      "id": "seti_1NG8Du2eZvKYlo2C9XMqbR0x",
      "object": "setup_intent",
      "application": null,
      "automatic_payment_methods": null,
      "cancellation_reason": null,
      "client_secret": "seti_1NG8Du2eZvKYlo2C9XMqbR0x_secret_O2CdhLwGFh2Aej7bCY7qp8jlIuyR8DJ",
      "created": 1686089970,
      "customer": null,
      "description": null,
      "flow_directions": null,
      "last_setup_error": null,
      "latest_attempt": null,
      "livemode": false,
      "mandate": null,
      "metadata": {},
      "next_action": null,
      "on_behalf_of": null,
      "payment_method": "pm_1NG8Du2eZvKYlo2CYzzldNr7",
      "payment_method_options": {
        "acss_debit": {
          "currency": "cad",
          "mandate_options": {
            "interval_description": "First day of every month",
            "payment_schedule": "interval",
            "transaction_type": "personal"
          },
          "verification_method": "automatic"
        }
      },
      "payment_method_types": [
        "acss_debit"
      ],
      "single_use_mandate": null,
      "status": "requires_confirmation",
      "usage": "off_session"
    }
  },
  "livemode": false,
  "pending_webhooks": 0,
  "request": {
    "id": null,
    "idempotency_key": null
  },
  "type": "setup_intent.created"
}
```