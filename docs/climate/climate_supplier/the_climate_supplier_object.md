# The Climate supplier object

## Attributes

- `id` (string)
  Unique identifier for the object.

- `object` (string)
  String representing the object’s type. Objects of the same type share the same value.

- `info_url` (string)
  Link to a webpage to learn more about the supplier.

- `livemode` (boolean)
  Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.

- `locations` (array of objects)
  The locations in which this supplier operates.

  - `locations.city` (string, nullable)
    The city where the supplier is located.

  - `locations.country` (string)
    Two-letter ISO code representing the country where the supplier is located.

  - `locations.latitude` (float, nullable)
    The geographic latitude where the supplier is located.

  - `locations.longitude` (float, nullable)
    The geographic longitude where the supplier is located.

  - `locations.region` (string, nullable)
    The state/county/province/region where the supplier is located.

- `name` (string)
  Name of this carbon removal supplier.

- `removal_pathway` (enum)
  The scientific pathway used for carbon removal.
Possible enum values:
  - `biomass_carbon_removal_and_storage`
    Biomass carbon removal and storage

  - `direct_air_capture`
    Direct air capture

  - `enhanced_weathering`
    Enhanced weathering

### The Climate supplier object

```json
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
```