# SWAIG CLI Tool

## Overview

The `swaig_cli` is a command-line tool designed for testing SignalWire AI Gateway functions. It allows users to interact with the SWAIG server to retrieve function signatures and test specific functions by name.

## Installation

To install the `swaig_cli` tool, download the latest release from the [official repository](#) and follow the installation instructions provided.

## Usage

### Basic Command

```bash
swaig_cli [--url URL] [--get-signatures] [--function FUNCTION_NAME]
```

### Options

- `--url URL`: Specify the URL of the SWAIG server. This option is required for all operations.
- `--get-signatures`: Retrieve the function signatures from the SWAIG server. Outputs the signatures in JSON format.
- `--function FUNCTION_NAME`: Test a specific function by its name. The tool will prompt for required and optional arguments based on the function signature.

### Examples

#### Retrieve Function Signatures

To retrieve function signatures from the SWAIG server:

```bash
swaig_cli --url http://example.com --get-signatures --function myFunction
```

#### Test a Specific Function

To test a specific function:

```bash
swaig_cli --url http://example.com --function myFunction
```

### Example Requests and Responses

#### Example Request for Function Signatures

```json
{
  "functions": ["myFunction"],
  "action": "get_signature",
  "version": "2.0",
  "content_disposition": "function signature request",
  "content_type": "text/swaig"
}
```

#### Example Response for Function Signatures

```json
{
  "function": "myFunction",
  "argument": {
    "required": ["arg1", "arg2"],
    "properties": {
      "arg1": {"type": "string"},
      "arg2": {"type": "integer"}
    }
  }
}
```

#### Example Request for Testing a Function

```json
{
  "function": "myFunction",
  "argument": {"parsed": [{"arg1": "value1", "arg2": 42}]}
}
```

#### Example Response for Testing a Function

```json
{
  "response": "Output fed into the LLM"
}
```

## Author

Written by Brian West.

## Reporting Bugs

Report bugs to [brian@signalwire.com](mailto:brian@signalwire.com).

## License

This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

## See Also

- `curl(1)`
- `jq(1)`
```

This README provides a concise overview of the `swaig_cli` tool, its usage, options, and examples, based on the information from the man page.
