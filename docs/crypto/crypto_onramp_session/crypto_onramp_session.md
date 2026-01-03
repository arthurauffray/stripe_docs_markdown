# Crypto Onramp Session

A Crypto Onramp Session represents your customer’s session as they purchase cryptocurrency through Stripe. Once payment is successful, Stripe will fulfill the delivery of cryptocurrency to your user’s wallet and contain a reference to the crypto transaction ID.

You can create an onramp session on your server and embed the widget on your frontend. Alternatively, you can redirect your users to the standalone hosted onramp.

Related guide: [Integrate the onramp](https://docs.stripe.com/docs/crypto/integrate-the-onramp.md)

## Endpoints

### Create a CryptoOnrampSession

- [POST /v1/crypto/onramp_sessions](https://docs.stripe.com/api/crypto/onramp_sessions/create.md)

### Retrieve a CryptoOnrampSession

- [GET /v1/crypto/onramp_sessions/:id](https://docs.stripe.com/api/crypto/onramp_sessions/retrieve.md)

### List CryptoOnrampSessions

- [GET /v1/crypto/onramp_sessions](https://docs.stripe.com/api/crypto/onramp_sessions/list.md)