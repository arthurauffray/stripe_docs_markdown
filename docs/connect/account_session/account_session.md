# Account Session

An AccountSession allows a Connect platform to grant access to a connected account in Connect embedded components.

We recommend that you create an AccountSession each time you need to display an embedded component to your user. Do not save AccountSessions to your database as they expire relatively quickly, and cannot be used more than once.

Related guide: [Connect embedded components](https://docs.stripe.com/docs/connect/get-started-connect-embedded-components.md)

## Endpoints

### Create an Account Session

- [POST /v1/account_sessions](https://docs.stripe.com/api/account_sessions/create.md)