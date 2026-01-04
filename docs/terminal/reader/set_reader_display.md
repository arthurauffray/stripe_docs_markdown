# Set reader display

Sets the reader display to show [cart details](https://docs.stripe.com/docs/terminal/features/display.md).

## Returns

Returns an updated `Reader` resource.

## Parameters

- `type` (enum, required)
  Type of information to display. Only `cart` is currently supported.

- `cart` (object, optional)
  Cart details to display on the reader screen, including line items, amounts, and currency.

  - `cart.currency` (enum, required)
    Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

  - `cart.line_items` (array of objects, required)
    Array of line items to display.

    - `cart.line_items.amount` (integer, required)
      The price of the item in the [smallest currency unit](https://docs.stripe.com/docs/currencies.md#zero-decimal).

    - `cart.line_items.description` (string, required)
      The description or name of the item.

    - `cart.line_items.quantity` (integer, required)
      The quantity of the line item being purchased.

  - `cart.total` (integer, required)
    Total balance of cart due in the [smallest currency unit](https://docs.stripe.com/docs/currencies.md#zero-decimal).

  - `cart.tax` (integer, optional)
    The amount of tax in the [smallest currency unit](https://docs.stripe.com/docs/currencies.md#zero-decimal).

```curl
curl https://api.stripe.com/v1/terminal/readers/tmr_FDOt2wlRZEdpd7/set_reader_display \
  -u "<<YOUR_SECRET_KEY>>" \
  -d type=cart \
  -d "cart[currency]"=usd \
  -d "cart[line_items][0][amount]"=5100 \
  -d "cart[line_items][0][description]"="Red t-shirt" \
  -d "cart[line_items][0][quantity]"=1 \
  -d "cart[tax]"=100 \
  -d "cart[total]"=5200
```

```cli
stripe terminal readers set_reader_display tmr_FDOt2wlRZEdpd7 \
  --type=cart \
  -d "cart[currency]"=usd \
  -d "cart[line_items][0][amount]"=5100 \
  -d "cart[line_items][0][description]"="Red t-shirt" \
  -d "cart[line_items][0][quantity]"=1 \
  -d "cart[tax]"=100 \
  -d "cart[total]"=5200
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

reader = client.v1.terminal.readers.set_reader_display(
  'tmr_FDOt2wlRZEdpd7',
  {
    type: 'cart',
    cart: {
      currency: 'usd',
      line_items: [
        {
          amount: 5100,
          description: 'Red t-shirt',
          quantity: 1,
        },
      ],
      tax: 100,
      total: 5200,
    },
  },
)
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

reader = client.v1.terminal.readers.set_reader_display(
  "tmr_FDOt2wlRZEdpd7",
  {
    "type": "cart",
    "cart": {
      "currency": "usd",
      "line_items": [{"amount": 5100, "description": "Red t-shirt", "quantity": 1}],
      "tax": 100,
      "total": 5200,
    },
  },
)
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$reader = $stripe->terminal->readers->setReaderDisplay(
  'tmr_FDOt2wlRZEdpd7',
  [
    'type' => 'cart',
    'cart' => [
      'currency' => 'usd',
      'line_items' => [
        [
          'amount' => 5100,
          'description' => 'Red t-shirt',
          'quantity' => 1,
        ],
      ],
      'tax' => 100,
      'total' => 5200,
    ],
  ]
);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

ReaderSetReaderDisplayParams params =
  ReaderSetReaderDisplayParams.builder()
    .setType(ReaderSetReaderDisplayParams.Type.CART)
    .setCart(
      ReaderSetReaderDisplayParams.Cart.builder()
        .setCurrency("usd")
        .addLineItem(
          ReaderSetReaderDisplayParams.Cart.LineItem.builder()
            .setAmount(5100L)
            .setDescription("Red t-shirt")
            .setQuantity(1L)
            .build()
        )
        .setTax(100L)
        .setTotal(5200L)
        .build()
    )
    .build();

Reader reader =
  client.v1().terminal().readers().setReaderDisplay("tmr_FDOt2wlRZEdpd7", params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const reader = await stripe.terminal.readers.setReaderDisplay(
  'tmr_FDOt2wlRZEdpd7',
  {
    type: 'cart',
    cart: {
      currency: 'usd',
      line_items: [
        {
          amount: 5100,
          description: 'Red t-shirt',
          quantity: 1,
        },
      ],
      tax: 100,
      total: 5200,
    },
  }
);
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.TerminalReaderSetReaderDisplayParams{
  Type: stripe.String("cart"),
  Cart: &stripe.TerminalReaderSetReaderDisplayCartParams{
    Currency: stripe.String(stripe.CurrencyUSD),
    LineItems: []*stripe.TerminalReaderSetReaderDisplayCartLineItemParams{
      &stripe.TerminalReaderSetReaderDisplayCartLineItemParams{
        Amount: stripe.Int64(5100),
        Description: stripe.String("Red t-shirt"),
        Quantity: stripe.Int64(1),
      },
    },
    Tax: stripe.Int64(100),
    Total: stripe.Int64(5200),
  },
}
result, err := sc.V1TerminalReaders.SetReaderDisplay(
  context.TODO(), "tmr_FDOt2wlRZEdpd7", params)
```

```dotnet
var options = new Stripe.Terminal.ReaderSetReaderDisplayOptions
{
    Type = "cart",
    Cart = new Stripe.Terminal.ReaderCartOptions
    {
        Currency = "usd",
        LineItems = new List<Stripe.Terminal.ReaderCartLineItemOptions>
        {
            new Stripe.Terminal.ReaderCartLineItemOptions
            {
                Amount = 5100,
                Description = "Red t-shirt",
                Quantity = 1,
            },
        },
        Tax = 100,
        Total = 5200,
    },
};
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Terminal.Readers;
Stripe.Terminal.Reader reader = service.SetReaderDisplay(
    "tmr_FDOt2wlRZEdpd7",
    options);
```

### Response

```json
{
  "id": "tmr_FDOt2wlRZEdpd7",
  "object": "terminal.reader",
  "action": {
    "failure_code": null,
    "failure_message": null,
    "set_reader_display": {
      "cart": {
        "currency": "usd",
        "line_items": [
          {
            "amount": 5100,
            "description": "Red t-shirt",
            "quantity": 1
          }
        ],
        "tax": 100,
        "total": 5200
      },
      "type": "cart"
    },
    "status": "in_progress",
    "type": "set_reader_display"
  },
  "device_sw_version": "2.37.2.0",
  "device_type": "simulated_wisepos_e",
  "ip_address": "0.0.0.0",
  "label": "Blue Rabbit",
  "last_seen_at": 1695166525506,
  "livemode": false,
  "location": "tml_FDOtHwxAAdIJOh",
  "metadata": {},
  "serial_number": "259cd19c-b902-4730-96a1-09183be6e7f7",
  "status": "online"
}
```