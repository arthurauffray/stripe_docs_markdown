# The Climate order object

## Attributes

- `id` (string)
  Unique identifier for the object.

- `object` (string)
  String representing the object’s type. Objects of the same type share the same value.

- `amount_fees` (integer)
  Total amount of [Frontier](https://frontierclimate.com/)’s service fees in the currency’s smallest unit.

- `amount_subtotal` (integer)
  Total amount of the carbon removal in the currency’s smallest unit.

- `amount_total` (integer)
  Total amount of the order including fees in the currency’s smallest unit.

- `beneficiary` (object, nullable)
  Publicly sharable reference for the end beneficiary of carbon removal. Assumed to be the Stripe account if not set.

  - `beneficiary.public_name` (string)
    Publicly displayable name for the end beneficiary of carbon removal.

- `canceled_at` (timestamp, nullable)
  Time at which the order was canceled. Measured in seconds since the Unix epoch.

- `cancellation_reason` (enum, nullable)
  Reason for the cancellation of this order.
Possible enum values:
  - `expired`
    Order was not confirmed and expired automatically

  - `product_unavailable`
    Order could not be fulfilled because the product is no longer available

  - `requested`
    Order was canceled by a cancellation request

- `certificate` (string, nullable)
  For delivered orders, a URL to a delivery certificate for the order.

- `confirmed_at` (timestamp, nullable)
  Time at which the order was confirmed. Measured in seconds since the Unix epoch.

- `created` (timestamp)
  Time at which the object was created. Measured in seconds since the Unix epoch.

- `currency` (string)
  Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase, representing the currency for this order.

- `delayed_at` (timestamp, nullable)
  Time at which the order’s expected_delivery_year was delayed. Measured in seconds since the Unix epoch.

- `delivered_at` (timestamp, nullable)
  Time at which the order was delivered. Measured in seconds since the Unix epoch.

- `delivery_details` (array of objects)
  Details about the delivery of carbon removal for this order.

  - `delivery_details.delivered_at` (timestamp)
    Time at which the delivery occurred. Measured in seconds since the Unix epoch.

  - `delivery_details.location` (object, nullable)
    Specific location of this delivery.

    - `delivery_details.location.city` (string, nullable)
      The city where the supplier is located.

    - `delivery_details.location.country` (string)
      Two-letter ISO code representing the country where the supplier is located.

    - `delivery_details.location.latitude` (float, nullable)
      The geographic latitude where the supplier is located.

    - `delivery_details.location.longitude` (float, nullable)
      The geographic longitude where the supplier is located.

    - `delivery_details.location.region` (string, nullable)
      The state/county/province/region where the supplier is located.

  - `delivery_details.metric_tons` (string)
    Quantity of carbon removal supplied by this delivery.

  - `delivery_details.registry_url` (string, nullable)
    Once retired, a URL to the registry entry for the tons from this delivery.

  - `delivery_details.supplier` (object)
    ID of the `Supplier` responsible for this delivery.

    - `delivery_details.supplier.id` (string)
      Unique identifier for the object.

    - `delivery_details.supplier.object` (string)
      String representing the object’s type. Objects of the same type share the same value.

    - `delivery_details.supplier.info_url` (string)
      Link to a webpage to learn more about the supplier.

    - `delivery_details.supplier.livemode` (boolean)
      Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.

    - `delivery_details.supplier.locations` (array of objects)
      The locations in which this supplier operates.

      - `delivery_details.supplier.locations.city` (string, nullable)
        The city where the supplier is located.

      - `delivery_details.supplier.locations.country` (string)
        Two-letter ISO code representing the country where the supplier is located.

      - `delivery_details.supplier.locations.latitude` (float, nullable)
        The geographic latitude where the supplier is located.

      - `delivery_details.supplier.locations.longitude` (float, nullable)
        The geographic longitude where the supplier is located.

      - `delivery_details.supplier.locations.region` (string, nullable)
        The state/county/province/region where the supplier is located.

    - `delivery_details.supplier.name` (string)
      Name of this carbon removal supplier.

    - `delivery_details.supplier.removal_pathway` (enum)
      The scientific pathway used for carbon removal.
Possible enum values:
      - `biomass_carbon_removal_and_storage`
        Biomass carbon removal and storage

      - `direct_air_capture`
        Direct air capture

      - `enhanced_weathering`
        Enhanced weathering

- `expected_delivery_year` (integer)
  The year this order is expected to be delivered.

- `livemode` (boolean)
  Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.

- `metadata` (object)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

- `metric_tons` (decimal string)
  Quantity of carbon removal that is included in this order.

- `product` (string)
  Unique ID for the Climate `Product` this order is purchasing.

- `product_substituted_at` (timestamp, nullable)
  Time at which the order’s product was substituted for a different product. Measured in seconds since the Unix epoch.

- `status` (enum)
  The current status of this order.
Possible enum values:
  - `awaiting_funds`
    Status when an order has been attached to a funding_source and is awaiting it’s settlement

  - `canceled`
    Status when an order has been canceled

  - `confirmed`
    Status when an order has been successfully confirmed and payment has been made

  - `delivered`
    Status when an order has been delivered

### The Climate order object

```json
{
  "id": "climorder_1aTnU0B63jkB3XAQKUbA5yyl",
  "object": "climate.order",
  "amount_fees": 17,
  "amount_subtotal": 550,
  "amount_total": 567,
  "beneficiary": {
    "public_name": "{{YOUR_BUSINESS_NAME}}"
  },
  "canceled_at": null,
  "cancellation_reason": null,
  "certificate": null,
  "confirmed_at": 1881439205,
  "created": 1881439205,
  "currency": "usd",
  "delayed_at": null,
  "delivered_at": null,
  "delivery_details": [],
  "expected_delivery_year": 2027,
  "livemode": false,
  "metadata": {},
  "metric_tons": "0.01",
  "product": "climsku_frontier_offtake_portfolio_2027",
  "product_substituted_at": null,
  "status": "confirmed"
}
```