# SWAIG CLI

A command-line tool for testing SignalWire AI Gateway functions.

## Installation

To install the `swaig_cli` tool, download the latest release from the [official repository](#) and follow the installation instructions provided.

## Usage

### Basic Commands

```bash
# Interactive mode
swaig_cli --url URL --function FUNCTION_NAME

# Get signatures
swaig_cli --url URL --get-signatures [--function FUNCTION_NAME]

# Direct JSON mode
swaig_cli --url URL --json '{"function": "function_name", "argument": {"parsed": [{"key": "value"}]}}'
```

### Options

- `--url URL`: Specify the URL of the SWAIG server. This option is required for all operations.
- `--get-signatures`: Retrieve the function signatures from the SWAIG server.
- `--function FUNCTION_NAME`: Test a specific function by name (interactive mode).
- `--json JSON_PAYLOAD`: Send a direct JSON payload to the server. The JSON payload should include the function name and any necessary arguments.

### JSON Payload Structure

The `--json` option allows you to send a direct JSON payload to the SWAIG server. The JSON should be structured as follows:

```json
{
    "function": "function_name",
    "argument": {
        "parsed": [
            {
                "key": "value"
            }
        ]
    }
}
```

- `function`: The name of the function you want to test.
- `argument`: A dictionary containing the arguments for the function. The `parsed` key should contain a list of key-value pairs representing the arguments.

### Examples

#### Interactive Function Testing

```bash
swaig_cli --url http://example.com/swaig --function verify_insurance
```

#### Using JSON Payload

```bash
swaig_cli --url http://example.com/swaig --function verify_insurance --json '{
  "member_id": "123456789",
  "insurance_provider": "1",
  "date_of_birth": "1"
}'
```

#### Get Function Signatures

```bash
swaig_cli --url http://example.com/swaig --get-signatures --function verify_insurance
```

## Author

Written by Brian West.

## Reporting Bugs

Report bugs to [brian@signalwire.com](mailto:brian@signalwire.com).

## License

This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
```

This README provides a concise overview of the `swaig_cli` tool, its usage, options, and examples, based on the information from the man page.
