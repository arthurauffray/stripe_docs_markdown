# The Climate product object

## Attributes

- `id` (string)
  Unique identifier for the object. For convenience, Climate product IDs are human-readable strings that start with `climsku_`. See [carbon removal inventory](https://stripe.com/docs/climate/orders/carbon-removal-inventory) for a list of available carbon removal products.

- `object` (string)
  String representing the object’s type. Objects of the same type share the same value.

- `created` (timestamp)
  Time at which the object was created. Measured in seconds since the Unix epoch.

- `current_prices_per_metric_ton` (object)
  Current prices for a metric ton of carbon removal in a currency’s smallest unit.

  - `current_prices_per_metric_ton.<currency>.amount_fees` (integer)
    Fees for one metric ton of carbon removal in the currency’s smallest unit.

  - `current_prices_per_metric_ton.<currency>.amount_subtotal` (integer)
    Subtotal for one metric ton of carbon removal (excluding fees) in the currency’s smallest unit.

  - `current_prices_per_metric_ton.<currency>.amount_total` (integer)
    Total for one metric ton of carbon removal (including fees) in the currency’s smallest unit.

- `delivery_year` (integer, nullable)
  The year in which the carbon removal is expected to be delivered.

- `livemode` (boolean)
  Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.

- `metric_tons_available` (decimal string)
  The quantity of metric tons available for reservation.

- `name` (string)
  The Climate product’s name.

- `suppliers` (array of objects)
  The carbon removal suppliers that fulfill orders for this Climate product.

  - `suppliers.id` (string)
    Unique identifier for the object.

  - `suppliers.object` (string)
    String representing the object’s type. Objects of the same type share the same value.

  - `suppliers.info_url` (string)
    Link to a webpage to learn more about the supplier.

  - `suppliers.livemode` (boolean)
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.

  - `suppliers.locations` (array of objects)
    The locations in which this supplier operates.

    - `suppliers.locations.city` (string, nullable)
      The city where the supplier is located.

    - `suppliers.locations.country` (string)
      Two-letter ISO code representing the country where the supplier is located.

    - `suppliers.locations.latitude` (float, nullable)
      The geographic latitude where the supplier is located.

    - `suppliers.locations.longitude` (float, nullable)
      The geographic longitude where the supplier is located.

    - `suppliers.locations.region` (string, nullable)
      The state/county/province/region where the supplier is located.

  - `suppliers.name` (string)
    Name of this carbon removal supplier.

  - `suppliers.removal_pathway` (enum)
    The scientific pathway used for carbon removal.
Possible enum values:
    - `biomass_carbon_removal_and_storage`
      Biomass carbon removal and storage

    - `direct_air_capture`
      Direct air capture

    - `enhanced_weathering`
      Enhanced weathering

### The Climate product object

```json
{
  "id": "climsku_frontier_offtake_portfolio_2027",
  "object": "climate.product",
  "created": 1881439203,
  "current_prices_per_metric_ton": {
    "usd": {
      "amount_fees": 1650,
      "amount_subtotal": 55000,
      "amount_total": 56650
    }
  },
  "delivery_year": 2027,
  "livemode": false,
  "metric_tons_available": "18000",
  "name": "Frontier's 2027 offtake portfolio",
  "suppliers": [
    {
      "id": "climsup_charm_industrial",
      "object": "climate.supplier",
      "info_url": "https://frontierclimate.com/portfolio/charm-industrial",
      "livemode": false,
      "locations": [
        {
          "city": "San Francisco",
          "country": "US",
          "latitude": 37.7749,
          "longitude": -122.4194,
          "region": "CA"
        }
      ],
      "name": "Charm Industrial",
      "removal_pathway": "biomass_carbon_removal_and_storage"
    }
  ]
}
```