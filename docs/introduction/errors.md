# Errors

Stripe uses conventional HTTP response codes to indicate the success or failure of an API request. In general: Codes in the `2xx` range indicate success. Codes in the `4xx` range indicate an error that failed given the information provided (e.g., a required parameter was omitted, a charge failed, etc.). Codes in the `5xx` range indicate an error with Stripe’s servers (these are rare).

Some `4xx` errors that could be handled programmatically (e.g., a card is [declined](https://docs.stripe.com/declines.md)) include an [error code](https://docs.stripe.com/error-codes.md) that briefly explains the error reported.

## Attributes

- `advice_code` (string, nullable)
  For card errors resulting from a card issuer decline, a short string indicating [how to proceed with an error](https://docs.stripe.com/docs/declines.md#retrying-issuer-declines) if they provide one.

- `charge` (string, nullable)
  For card errors, the ID of the failed charge.

- `code` (string, nullable)
  For some errors that could be handled programmatically, a short string indicating the [error code](https://docs.stripe.com/docs/error-codes.md) reported.

- `decline_code` (string, nullable)
  For card errors resulting from a card issuer decline, a short string indicating the [card issuer’s reason for the decline](https://docs.stripe.com/docs/declines.md#issuer-declines) if they provide one.

- `doc_url` (string, nullable)
  A URL to more information about the [error code](https://docs.stripe.com/docs/error-codes.md) reported.

- `message` (string, nullable)
  A human-readable message providing more details about the error. For card errors, these messages can be shown to your users.

- `network_advice_code` (string, nullable)
  For card errors resulting from a card issuer decline, a 2 digit code which indicates the advice given to merchant by the card network on how to proceed with an error.

- `network_decline_code` (string, nullable)
  For payments declined by the network, an alphanumeric code which indicates the reason the payment failed.

- `param` (string, nullable)
  If the error is parameter-specific, the parameter related to the error. For example, you can use this to display a message near the correct form field.

- `payment_intent` (object, nullable)
  The [PaymentIntent object](https://docs.stripe.com/docs/api/payment_intents/object.md) for errors returned on a request involving a PaymentIntent.

- `payment_method` (object, nullable)
  The [PaymentMethod object](https://docs.stripe.com/docs/api/payment_methods/object.md) for errors returned on a request involving a PaymentMethod.

- `payment_method_type` (string, nullable)
  If the error is specific to the type of payment method, the payment method type that had a problem. This field is only populated for invoice-related errors.

- `request_log_url` (string, nullable)
  A URL to the request log entry in your dashboard.

- `setup_intent` (object, nullable)
  The [SetupIntent object](https://docs.stripe.com/docs/api/setup_intents/object.md) for errors returned on a request involving a SetupIntent.

- `source` (object, nullable)
  The [source object](https://docs.stripe.com/docs/api/sources/object.md) for errors returned on a request involving a source.

- `type` (enum)
  The type of error returned. One of `api_error`, `card_error`, `idempotency_error`, or `invalid_request_error`
Possible enum values:
  - `api_error`
  - `card_error`
  - `idempotency_error`
  - `invalid_request_error`

### HTTP Status Code Summary

| 200                | OK                         | Everything worked as expected.                                                                   |
| ------------------ | -------------------------- | ------------------------------------------------------------------------------------------------ |
| 400                | Bad Request                | The request was unacceptable, often due to missing a required parameter.                         |
| 401                | Unauthorized               | No valid API key provided.                                                                       |
| 402                | Request Failed             | The parameters were valid but the request failed.                                                |
| 403                | Forbidden                  | The API key doesn’t have permissions to perform the request.                                     |
| 404                | Not Found                  | The requested resource doesn’t exist.                                                            |
| 409                | Conflict                   | The request conflicts with another request (perhaps due to using the same idempotent key).       |
| 424                | External Dependency Failed | The request couldn’t be completed due to a failure in a dependency external to Stripe.           |
| 429                | Too Many Requests          | Too many requests hit the API too quickly. We recommend an exponential backoff of your requests. |
| 500, 502, 503, 504 | Server Errors              | Something went wrong on Stripe’s end. (These are rare.)                                          |

### Error Types

| `api_error`             | API errors cover any other type of problem (e.g., a temporary problem with Stripe’s servers), and are extremely uncommon.                                 |
| ----------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `card_error`            | Card errors are the most common type of error you should expect to handle. They result when the user enters a card that can’t be charged for some reason. |
| `idempotency_error`     | Idempotency errors occur when an `Idempotency-Key` is re-used on a request that does not match the first request’s API endpoint and parameters.           |
| `invalid_request_error` | Invalid request errors arise when your request has invalid parameters.                                                                                    |
----
# Handling errors

Our Client libraries raise exceptions for many reasons, such as a failed charge, invalid parameters, authentication errors, and network unavailability. We recommend writing code that gracefully handles all possible API exceptions.

- Related guide: [Error Handling](https://docs.stripe.com/error-handling.md)

```sh
# Select a client library to see examples of
# handling different kinds of errors.
```

```ruby
begin
  # Use Stripe's library to make requests...
rescue Stripe::CardError => e
  puts "Status is: #{e.http_status}"
  puts "Type is: #{e.error.type}"
  puts "Charge ID is: #{e.error.charge}"
  # The following fields are optional
  puts "Code is: #{e.error.code}" if e.error.code
  puts "Decline code is: #{e.error.decline_code}" if e.error.decline_code
  puts "Param is: #{e.error.param}" if e.error.param
  puts "Message is: #{e.error.message}" if e.error.message
rescue Stripe::RateLimitError => e
  # Too many requests made to the API too quickly
rescue Stripe::InvalidRequestError => e
  # Invalid parameters were supplied to Stripe's API
rescue Stripe::AuthenticationError => e
  # Authentication with Stripe's API failed
  # (maybe you changed API keys recently)
rescue Stripe::APIConnectionError => e
  # Network communication with Stripe failed
rescue Stripe::StripeError => e
  # Display a very generic error to the user, and maybe send
  # yourself an email
rescue => e
  # Something else happened, completely unrelated to Stripe
end
```

```sh
# Select a client library to see examples of
# handling different kinds of errors.
```

```python
try:
  # Use Stripe's library to make requests...
  pass
except stripe.error.CardError as e:
  # Since it's a decline, stripe.error.CardError will be caught

  print('Status is: %s' % e.http_status)
  print('Code is: %s' % e.code)
  # param is '' in this case
  print('Param is: %s' % e.param)
  print('Message is: %s' % e.user_message)
except stripe.error.RateLimitError as e:
  # Too many requests made to the API too quickly
  pass
except stripe.error.InvalidRequestError as e:
  # Invalid parameters were supplied to Stripe's API
  pass
except stripe.error.AuthenticationError as e:
  # Authentication with Stripe's API failed
  # (maybe you changed API keys recently)
  pass
except stripe.error.APIConnectionError as e:
  # Network communication with Stripe failed
  pass
except stripe.error.StripeError as e:
  # Display a very generic error to the user, and maybe send
  # yourself an email
  pass
except Exception as e:
  # Something else happened, completely unrelated to Stripe
  pass
```

```php
try {
  // Use Stripe's library to make requests...
} catch(\Stripe\Exception\CardException $e) {
  // Since it's a decline, \Stripe\Exception\CardException will be caught
  echo 'Status is:' . $e->getHttpStatus() . '\n';
  echo 'Type is:' . $e->getError()->type . '\n';
  echo 'Code is:' . $e->getError()->code . '\n';
  // param is '' in this case
  echo 'Param is:' . $e->getError()->param . '\n';
  echo 'Message is:' . $e->getError()->message . '\n';
} catch (\Stripe\Exception\RateLimitException $e) {
  // Too many requests made to the API too quickly
} catch (\Stripe\Exception\InvalidRequestException $e) {
  // Invalid parameters were supplied to Stripe's API
} catch (\Stripe\Exception\AuthenticationException $e) {
  // Authentication with Stripe's API failed
  // (maybe you changed API keys recently)
} catch (\Stripe\Exception\ApiConnectionException $e) {
  // Network communication with Stripe failed
} catch (\Stripe\Exception\ApiErrorException $e) {
  // Display a very generic error to the user, and maybe send
  // yourself an email
} catch (Exception $e) {
  // Something else happened, completely unrelated to Stripe
}
```

```java
try {
  // Use Stripe's library to make requests...
} catch (CardException e) {
  // Since it's a decline, CardException will be caught
  System.out.println("Status is: " + e.getCode());
  System.out.println("Message is: " + e.getMessage());
} catch (RateLimitException e) {
  // Too many requests made to the API too quickly
} catch (InvalidRequestException e) {
  // Invalid parameters were supplied to Stripe's API
} catch (AuthenticationException e) {
  // Authentication with Stripe's API failed
  // (maybe you changed API keys recently)
} catch (APIConnectionException e) {
  // Network communication with Stripe failed
} catch (StripeException e) {
  // Display a very generic error to the user, and maybe send
  // yourself an email
} catch (Exception e) {
  // Something else happened, completely unrelated to Stripe
}
```

```javascript
// Note: Node.js API does not throw exceptions, and instead prefers the
// asynchronous style of error handling described below.
//
// An error from the Stripe API or an otherwise asynchronous error
// will be available as the first argument of any Stripe method's callback:
// E.g. stripe.customers.create({...}, function(err, result) {});
//
// Or in the form of a rejected promise.
// E.g. stripe.customers.create({...}).then(
//        function(result) {},
//        function(err) {}
//      );

switch (err.type) {
  case 'StripeCardError':
    // A declined card error
    err.message; // => e.g. "Your card's expiration year is invalid."
    break;
  case 'StripeRateLimitError':
    // Too many requests made to the API too quickly
    break;
  case 'StripeInvalidRequestError':
    // Invalid parameters were supplied to Stripe's API
    break;
  case 'StripeAPIError':
    // An error occurred internally with Stripe's API
    break;
  case 'StripeConnectionError':
    // Some kind of error occurred during the HTTPS communication
    break;
  case 'StripeAuthenticationError':
    // You probably used an incorrect API key
    break;
  default:
    // Handle any other types of unexpected errors
    break;
}
```

```go
_, err := // Go library call

if err != nil {
  // Try to safely cast a generic error to a stripe.Error so that we can get at
  // some additional Stripe-specific information about what went wrong.
  if stripeErr, ok := err.(*stripe.Error); ok {
    // The Code field will contain a basic identifier for the failure.
    switch stripeErr.Code {
      case stripe.ErrorCodeCardDeclined:
      case stripe.ErrorCodeExpiredCard:
      case stripe.ErrorCodeIncorrectCVC:
      case stripe.ErrorCodeIncorrectZip:
      // etc.
    }

    // The Err field can be coerced to a more specific error type with a type
    // assertion. This technique can be used to get more specialized
    // information for certain errors.
    if cardErr, ok := stripeErr.Err.(*stripe.CardError); ok {
      fmt.Printf("Card was declined with code: %v\n", cardErr.DeclineCode)
    } else {
      fmt.Printf("Other Stripe error occurred: %v\n", stripeErr.Error())
    }
  } else {
    fmt.Printf("Other error occurred: %v\n", err.Error())
  }
}
```

```dotnet
try {
  // Use Stripe's library to make request
} catch (StripeException e) {
  switch (e.StripeError.Type)
  {
    case "card_error":
      Console.WriteLine("Code: " + e.StripeError.Code);
      Console.WriteLine("Message: " + e.StripeError.Message);
      break;
    case "api_connection_error":
      break;
    case "api_error":
      break;
    case "authentication_error":
      break;
    case "invalid_request_error":
      break;
    case "rate_limit_error":
      break;
    case "validation_error":
      break;
    default:
      // Unknown Error Type
      break;
  }
}
```