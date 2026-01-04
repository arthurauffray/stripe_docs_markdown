# Collect inputs using a Reader

Initiates an [input collection flow](https://docs.stripe.com/docs/terminal/features/collect-inputs.md) on a Reader to display input forms and collect information from your customers.

## Returns

Returns an updated `Reader` resource.

## Parameters

- `inputs` (array of objects, required)
  List of inputs to be collected from the customer using the Reader. Maximum 5 inputs.

  - `inputs.custom_text` (object, required)
    Customize the text which will be displayed while collecting this input

    - `inputs.custom_text.title` (string, required)
      The title which will be displayed when collecting this input

      The maximum length is 40 characters.

    - `inputs.custom_text.description` (string, optional)
      The description which will be displayed when collecting this input

      The maximum length is 500 characters.

    - `inputs.custom_text.skip_button` (string, optional)
      Custom text for the skip button. Maximum 14 characters.

      The maximum length is 14 characters.

    - `inputs.custom_text.submit_button` (string, optional)
      Custom text for the submit button. Maximum 30 characters.

      The maximum length is 30 characters.

  - `inputs.type` (enum, required)
    The type of input to collect
Possible enum values:
    - `email`
      Collect an email

    - `numeric`
      Collect a number

    - `phone`
      Collect a phone number

    - `selection`
      Collect a selection from one or more choices

    - `signature`
      Collect a signature

    - `text`
      Collect text

  - `inputs.required` (boolean, optional)
    Indicate that this input is required, disabling the skip button

  - `inputs.selection` (object, optional)
    Options for the `selection` input

    - `inputs.selection.choices` (array of objects, required)
      List of choices for the `selection` input

      - `inputs.selection.choices.id` (string, required)
        The unique identifier for this choice

        The maximum length is 50 characters.

      - `inputs.selection.choices.text` (string, required)
        The text which will be shown on the button for this choice

        The maximum length is 30 characters.

      - `inputs.selection.choices.style` (enum, optional)
        The style of the button which will be shown for this choice. Can be `primary` or `secondary`.

  - `inputs.toggles` (array of objects, optional)
    List of toggles to be displayed and customization for the toggles

    - `inputs.toggles.default_value` (enum, optional)
      The default value of the toggle. Can be `enabled` or `disabled`.

    - `inputs.toggles.description` (string, optional)
      The description which will be displayed for the toggle. Maximum 50 characters. At least one of title or description must be provided.

      The maximum length is 50 characters.

    - `inputs.toggles.title` (string, optional)
      The title which will be displayed for the toggle. Maximum 50 characters. At least one of title or description must be provided.

      The maximum length is 50 characters.

- `metadata` (object, optional)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.

```curl
curl https://api.stripe.com/v1/terminal/readers/tmr_OXYJvwsea7PDiDHNciXRkytb/collect_inputs \
  -u "<<YOUR_SECRET_KEY>>" \
  -d "inputs[0][type]"=signature \
  -d "inputs[0][custom_text][title]"=Signature \
  -d "inputs[0][custom_text][description]"="Please sign below" \
  -d "inputs[0][custom_text][submit_button]"=Submit \
  -d "inputs[0][custom_text][skip_button]"=Skip \
  -d "inputs[0][required]"=false \
  -d "inputs[1][type]"=selection \
  -d "inputs[1][custom_text][title]"=Selection \
  -d "inputs[1][custom_text][description]"="Please select one" \
  -d "inputs[1][required]"=true \
  -d "inputs[1][selection][choices][0][style]"=primary \
  -d "inputs[1][selection][choices][0][text]"=choice_1 \
  -d "inputs[1][selection][choices][0][id]"=choice_1_id \
  -d "inputs[1][selection][choices][1][style]"=secondary \
  -d "inputs[1][selection][choices][1][text]"=choice_2 \
  -d "inputs[1][selection][choices][1][id]"=choice_2_id \
  -d "inputs[2][type]"=email \
  -d "inputs[2][custom_text][title]"="Enter your email" \
  --data-urlencode "inputs[2][custom_text][description]"="We'll send updates on your order and occasional deals" \
  -d "inputs[2][custom_text][submit_button]"=Submit \
  -d "inputs[2][custom_text][skip_button]"=Skip \
  -d "inputs[2][required]"=false
```

```cli
stripe terminal readers collect_inputs tmr_OXYJvwsea7PDiDHNciXRkytb \
  -d "inputs[0][type]"=signature \
  -d "inputs[0][custom_text][title]"=Signature \
  -d "inputs[0][custom_text][description]"="Please sign below" \
  -d "inputs[0][custom_text][submit_button]"=Submit \
  -d "inputs[0][custom_text][skip_button]"=Skip \
  -d "inputs[0][required]"=false \
  -d "inputs[1][type]"=selection \
  -d "inputs[1][custom_text][title]"=Selection \
  -d "inputs[1][custom_text][description]"="Please select one" \
  -d "inputs[1][required]"=true \
  -d "inputs[1][selection][choices][0][style]"=primary \
  -d "inputs[1][selection][choices][0][text]"=choice_1 \
  -d "inputs[1][selection][choices][0][id]"=choice_1_id \
  -d "inputs[1][selection][choices][1][style]"=secondary \
  -d "inputs[1][selection][choices][1][text]"=choice_2 \
  -d "inputs[1][selection][choices][1][id]"=choice_2_id \
  -d "inputs[2][type]"=email \
  -d "inputs[2][custom_text][title]"="Enter your email" \
  -d "inputs[2][custom_text][description]"="We'll send updates on your order and occasional deals" \
  -d "inputs[2][custom_text][submit_button]"=Submit \
  -d "inputs[2][custom_text][skip_button]"=Skip \
  -d "inputs[2][required]"=false
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

reader = client.v1.terminal.readers.collect_inputs(
  'tmr_OXYJvwsea7PDiDHNciXRkytb',
  {
    inputs: [
      {
        type: 'signature',
        custom_text: {
          title: 'Signature',
          description: 'Please sign below',
          submit_button: 'Submit',
          skip_button: 'Skip',
        },
        required: false,
      },
      {
        type: 'selection',
        custom_text: {
          title: 'Selection',
          description: 'Please select one',
        },
        required: true,
        selection: {
          choices: [
            {
              style: 'primary',
              text: 'choice_1',
              id: 'choice_1_id',
            },
            {
              style: 'secondary',
              text: 'choice_2',
              id: 'choice_2_id',
            },
          ],
        },
      },
      {
        type: 'email',
        custom_text: {
          title: 'Enter your email',
          description: 'We\'ll send updates on your order and occasional deals',
          submit_button: 'Submit',
          skip_button: 'Skip',
        },
        required: false,
      },
    ],
  },
)
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

reader = client.v1.terminal.readers.collect_inputs(
  "tmr_OXYJvwsea7PDiDHNciXRkytb",
  {
    "inputs": [
      {
        "type": "signature",
        "custom_text": {
          "title": "Signature",
          "description": "Please sign below",
          "submit_button": "Submit",
          "skip_button": "Skip",
        },
        "required": False,
      },
      {
        "type": "selection",
        "custom_text": {"title": "Selection", "description": "Please select one"},
        "required": True,
        "selection": {
          "choices": [
            {"style": "primary", "text": "choice_1", "id": "choice_1_id"},
            {"style": "secondary", "text": "choice_2", "id": "choice_2_id"},
          ],
        },
      },
      {
        "type": "email",
        "custom_text": {
          "title": "Enter your email",
          "description": "We'll send updates on your order and occasional deals",
          "submit_button": "Submit",
          "skip_button": "Skip",
        },
        "required": False,
      },
    ],
  },
)
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$reader = $stripe->terminal->readers->collectInputs(
  'tmr_OXYJvwsea7PDiDHNciXRkytb',
  [
    'inputs' => [
      [
        'type' => 'signature',
        'custom_text' => [
          'title' => 'Signature',
          'description' => 'Please sign below',
          'submit_button' => 'Submit',
          'skip_button' => 'Skip',
        ],
        'required' => false,
      ],
      [
        'type' => 'selection',
        'custom_text' => [
          'title' => 'Selection',
          'description' => 'Please select one',
        ],
        'required' => true,
        'selection' => [
          'choices' => [
            [
              'style' => 'primary',
              'text' => 'choice_1',
              'id' => 'choice_1_id',
            ],
            [
              'style' => 'secondary',
              'text' => 'choice_2',
              'id' => 'choice_2_id',
            ],
          ],
        ],
      ],
      [
        'type' => 'email',
        'custom_text' => [
          'title' => 'Enter your email',
          'description' => 'We\'ll send updates on your order and occasional deals',
          'submit_button' => 'Submit',
          'skip_button' => 'Skip',
        ],
        'required' => false,
      ],
    ],
  ]
);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

ReaderCollectInputsParams params =
  ReaderCollectInputsParams.builder()
    .addInput(
      ReaderCollectInputsParams.Input.builder()
        .setType(ReaderCollectInputsParams.Input.Type.SIGNATURE)
        .setCustomText(
          ReaderCollectInputsParams.Input.CustomText.builder()
            .setTitle("Signature")
            .setDescription("Please sign below")
            .setSubmitButton("Submit")
            .setSkipButton("Skip")
            .build()
        )
        .setRequired(false)
        .build()
    )
    .addInput(
      ReaderCollectInputsParams.Input.builder()
        .setType(ReaderCollectInputsParams.Input.Type.SELECTION)
        .setCustomText(
          ReaderCollectInputsParams.Input.CustomText.builder()
            .setTitle("Selection")
            .setDescription("Please select one")
            .build()
        )
        .setRequired(true)
        .setSelection(
          ReaderCollectInputsParams.Input.Selection.builder()
            .addChoice(
              ReaderCollectInputsParams.Input.Selection.Choice.builder()
                .setStyle(
                  ReaderCollectInputsParams.Input.Selection.Choice.Style.PRIMARY
                )
                .setText("choice_1")
                .setId("choice_1_id")
                .build()
            )
            .addChoice(
              ReaderCollectInputsParams.Input.Selection.Choice.builder()
                .setStyle(
                  ReaderCollectInputsParams.Input.Selection.Choice.Style.SECONDARY
                )
                .setText("choice_2")
                .setId("choice_2_id")
                .build()
            )
            .build()
        )
        .build()
    )
    .addInput(
      ReaderCollectInputsParams.Input.builder()
        .setType(ReaderCollectInputsParams.Input.Type.EMAIL)
        .setCustomText(
          ReaderCollectInputsParams.Input.CustomText.builder()
            .setTitle("Enter your email")
            .setDescription("We'll send updates on your order and occasional deals")
            .setSubmitButton("Submit")
            .setSkipButton("Skip")
            .build()
        )
        .setRequired(false)
        .build()
    )
    .build();

Reader reader =
  client.v1().terminal().readers().collectInputs(
    "tmr_OXYJvwsea7PDiDHNciXRkytb",
    params
  );
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const reader = await stripe.terminal.readers.collectInputs(
  'tmr_OXYJvwsea7PDiDHNciXRkytb',
  {
    inputs: [
      {
        type: 'signature',
        custom_text: {
          title: 'Signature',
          description: 'Please sign below',
          submit_button: 'Submit',
          skip_button: 'Skip',
        },
        required: false,
      },
      {
        type: 'selection',
        custom_text: {
          title: 'Selection',
          description: 'Please select one',
        },
        required: true,
        selection: {
          choices: [
            {
              style: 'primary',
              text: 'choice_1',
              id: 'choice_1_id',
            },
            {
              style: 'secondary',
              text: 'choice_2',
              id: 'choice_2_id',
            },
          ],
        },
      },
      {
        type: 'email',
        custom_text: {
          title: 'Enter your email',
          description: 'We\'ll send updates on your order and occasional deals',
          submit_button: 'Submit',
          skip_button: 'Skip',
        },
        required: false,
      },
    ],
  }
);
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.TerminalReaderCollectInputsParams{
  Inputs: []*stripe.TerminalReaderCollectInputsInputParams{
    &stripe.TerminalReaderCollectInputsInputParams{
      Type: stripe.String("signature"),
      CustomText: &stripe.TerminalReaderCollectInputsInputCustomTextParams{
        Title: stripe.String("Signature"),
        Description: stripe.String("Please sign below"),
        SubmitButton: stripe.String("Submit"),
        SkipButton: stripe.String("Skip"),
      },
      Required: stripe.Bool(false),
    },
    &stripe.TerminalReaderCollectInputsInputParams{
      Type: stripe.String("selection"),
      CustomText: &stripe.TerminalReaderCollectInputsInputCustomTextParams{
        Title: stripe.String("Selection"),
        Description: stripe.String("Please select one"),
      },
      Required: stripe.Bool(true),
      Selection: &stripe.TerminalReaderCollectInputsInputSelectionParams{
        Choices: []*stripe.TerminalReaderCollectInputsInputSelectionChoiceParams{
          &stripe.TerminalReaderCollectInputsInputSelectionChoiceParams{
            Style: stripe.String("primary"),
            Text: stripe.String("choice_1"),
            ID: stripe.String("choice_1_id"),
          },
          &stripe.TerminalReaderCollectInputsInputSelectionChoiceParams{
            Style: stripe.String("secondary"),
            Text: stripe.String("choice_2"),
            ID: stripe.String("choice_2_id"),
          },
        },
      },
    },
    &stripe.TerminalReaderCollectInputsInputParams{
      Type: stripe.String("email"),
      CustomText: &stripe.TerminalReaderCollectInputsInputCustomTextParams{
        Title: stripe.String("Enter your email"),
        Description: stripe.String("We'll send updates on your order and occasional deals"),
        SubmitButton: stripe.String("Submit"),
        SkipButton: stripe.String("Skip"),
      },
      Required: stripe.Bool(false),
    },
  },
}
result, err := sc.V1TerminalReaders.CollectInputs(
  context.TODO(), "tmr_OXYJvwsea7PDiDHNciXRkytb", params)
```

```dotnet
var options = new Stripe.Terminal.ReaderCollectInputsOptions
{
    Inputs = new List<Stripe.Terminal.ReaderInputOptions>
    {
        new Stripe.Terminal.ReaderInputOptions
        {
            Type = "signature",
            CustomText = new Stripe.Terminal.ReaderInputCustomTextOptions
            {
                Title = "Signature",
                Description = "Please sign below",
                SubmitButton = "Submit",
                SkipButton = "Skip",
            },
            Required = false,
        },
        new Stripe.Terminal.ReaderInputOptions
        {
            Type = "selection",
            CustomText = new Stripe.Terminal.ReaderInputCustomTextOptions
            {
                Title = "Selection",
                Description = "Please select one",
            },
            Required = true,
            Selection = new Stripe.Terminal.ReaderInputSelectionOptions
            {
                Choices = new List<Stripe.Terminal.ReaderInputSelectionChoiceOptions>
                {
                    new Stripe.Terminal.ReaderInputSelectionChoiceOptions
                    {
                        Style = "primary",
                        Text = "choice_1",
                        Id = "choice_1_id",
                    },
                    new Stripe.Terminal.ReaderInputSelectionChoiceOptions
                    {
                        Style = "secondary",
                        Text = "choice_2",
                        Id = "choice_2_id",
                    },
                },
            },
        },
        new Stripe.Terminal.ReaderInputOptions
        {
            Type = "email",
            CustomText = new Stripe.Terminal.ReaderInputCustomTextOptions
            {
                Title = "Enter your email",
                Description = "We'll send updates on your order and occasional deals",
                SubmitButton = "Submit",
                SkipButton = "Skip",
            },
            Required = false,
        },
    },
};
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Terminal.Readers;
Stripe.Terminal.Reader reader = service.CollectInputs(
    "tmr_OXYJvwsea7PDiDHNciXRkytb",
    options);
```

### Response

```json
{
  "id": "tmr_OXYJvwsea7PDiDHNciXRkytb",
  "object": "terminal.reader",
  "action": {
    "failure_code": null,
    "failure_message": null,
    "collect_inputs": {
      "inputs": [
        {
          "type": "signature",
          "custom_text": {
            "title": "Signature",
            "description": "Please sign below",
            "submit_button": "Submit",
            "skip_button": "Skip"
          },
          "required": false,
          "signature": {
            "value": null
          }
        },
        {
          "type": "selection",
          "custom_text": {
            "title": "Selection",
            "description": "Please select one"
          },
          "required": true,
          "selection": {
            "choices": [
              {
                "style": "primary",
                "text": "choice_1",
                "id": "choice_1_id"
              },
              {
                "style": "secondary",
                "text": "choice_2",
                "id": "choice_2_id"
              }
            ],
            "value": null
          }
        },
        {
          "type": "email",
          "custom_text": {
            "title": "Enter your email",
            "description": "We'll send updates on your order and occasional deals",
            "submit_button": "Submit",
            "skip_button": "Skip"
          },
          "required": false,
          "email": {
            "value": null
          }
        }
      ]
    },
    "status": "in_progress",
    "type": "collect_inputs"
  },
  "device_deploy_group": null,
  "device_sw_version": null,
  "device_type": "bbpos_wisepos_e",
  "ip_address": "192.168.2.2",
  "label": "Blue Rabbit",
  "livemode": false,
  "location": null,
  "metadata": {},
  "serial_number": "123-456-789",
  "software": null,
  "status": "online"
}
```