# Delete a subscription item

Deletes an item from the subscription. Removing a subscription item from a subscription will not cancel the subscription.

## Returns

An subscription item object with a deleted flag upon success. Otherwise, this call raises [an error](https://docs.stripe.com/api/subscription_items/delete.md#errors), such as if the subscription item has already been deleted.

## Parameters

- `clear_usage` (boolean, optional)
  Delete all usage for the given subscription item. Allowed only when the current plan’s `usage_type` is `metered`.

- `proration_behavior` (enum, optional)
  Determines how to handle [prorations](https://docs.stripe.com/docs/billing/subscriptions/prorations.md) when the billing cycle changes (e.g., when switching plans, resetting `billing_cycle_anchor=now`, or starting a trial), or if an item’s `quantity` changes. The default value is `create_prorations`.
Possible enum values:
  - `always_invoice`
    Always invoice immediately for prorations.

  - `create_prorations`
    Will cause proration invoice items to be created when applicable. These proration items will only be invoiced immediately under [certain conditions](https://docs.stripe.com/docs/subscriptions/upgrading-downgrading.md#immediate-payment).

  - `none`
    Disable creating prorations in this request.

- `proration_date` (timestamp, optional)
  If set, the proration will be calculated as though the subscription was updated at the given time. This can be used to apply the same proration that was previewed with the [upcoming invoice](https://docs.stripe.com/api/subscription_items/delete.md#retrieve_customer_invoice) endpoint.

```curl
curl -X DELETE https://api.stripe.com/v1/subscription_items/si_NcLYdDxLHxlFo7 \
  -u "<<YOUR_SECRET_KEY>>"
```

```cli
stripe subscription_items delete si_NcLYdDxLHxlFo7
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

deleted = client.v1.subscription_items.delete('si_NcLYdDxLHxlFo7')
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

deleted = client.v1.subscription_items.delete("si_NcLYdDxLHxlFo7")
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$deleted = $stripe->subscriptionItems->delete('si_NcLYdDxLHxlFo7', []);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

SubscriptionItemDeleteParams params = SubscriptionItemDeleteParams.builder().build();

SubscriptionItem subscriptionItem =
  client.v1().subscriptionItems().delete("si_NcLYdDxLHxlFo7", params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const deleted = await stripe.subscriptionItems.del('si_NcLYdDxLHxlFo7');
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.SubscriptionItemDeleteParams{}
result, err := sc.V1SubscriptionItems.Delete(
  context.TODO(), "si_NcLYdDxLHxlFo7", params)
```

```dotnet
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.SubscriptionItems;
SubscriptionItem deleted = service.Delete("si_NcLYdDxLHxlFo7");
```

### Response

```json
{
  "id": "si_NcLYdDxLHxlFo7",
  "object": "subscription_item",
  "deleted": true
}
```