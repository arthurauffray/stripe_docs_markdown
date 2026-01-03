# Files

This object represents files hosted on Stripe’s servers. You can upload files with the [create file](https://docs.stripe.com/api/files.md#create_file) request (for example, when uploading dispute evidence). Stripe also creates files independently (for example, the results of a [Sigma scheduled query](https://docs.stripe.com/api/files.md#scheduled_queries)).

Related guide: [File upload guide](https://docs.stripe.com/docs/file-upload.md)

## Endpoints

### Create a file

- [POST /v1/files](https://docs.stripe.com/api/files/create.md)

### Retrieve a file

- [GET /v1/files/:id](https://docs.stripe.com/api/files/retrieve.md)

### List all files

- [GET /v1/files](https://docs.stripe.com/api/files/list.md)