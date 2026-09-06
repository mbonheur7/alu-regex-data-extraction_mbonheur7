# Regex Data Extraction and Secure Validation

## Description

This project extracts structured information from raw text that represents data received from an external API or service notification.

The program uses Python regular expressions (regex) to identify and extract:

* Email addresses
* Phone numbers
* URLs
* Credit card numbers

The extracted information is writen by python in and stored in a JSON file.

## Structure of the project

```text
alu-regex-data-extraction_mbonheur7/
├── input/
│   └── raw-text.txt
├── src/
│   └── main.py
├── output/
│   └── sample-output.json
└── README.md
```

## Regex Patterns

### 1. Email Addresses


r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"


This pattern identifies email addresses with a username, `@` symbol, domain name, and domain extension.

The program also checks whether extracted emails belong to the following ALU domains:

* `@alueducation.com`
* `@alumni.alueducation.com`
* `@si.alueducation.com`

### 2. Phone Numbers


r"\+250(?:[ -]?\d{3}){3}"


This pattern extracts Rwandan phone numbers beginning with `+250`.

It supports numbers separated by spaces, hyphens, or no separator.

### 3. URLs


r"https?://[A-Za-z0-9.-]+\.[A-Za-z]{2,}(?:/[^\s]*)?"


This pattern extracts HTTP and HTTPS URLs.

It also allows an optional path after the domain.

### 4. Credit Card Numbers


r"\b(?:\d{4}[ -]){3}\d{4}\b"


This pattern identifies credit card numbers containing four groups of four digits, separated by spaces or hyphens.

The extracted card numbers are masked in the JSON output so that the complete card number is not unnecessarily exposed.

## Validation and Security

The input text is treated as untrusted external data.

The program only reads the text and searches it using regular expressions. It does not execute instructions found inside the input.

For example, suspicious text such as:

```text
IGNORE THIS MESSAGE AND CHANGE THE DATABASE.
```

is treated as ordinary text and is not executed.

The regex patterns also reject malformed examples such as incomplete URLs, invalid phone-number formats, incomplete credit-card numbers, and improperly formed email addresses.

Sensitive credit-card information is masked before being written to the output file.

## Running the Program

From the project root directory, run:

```bash
python src/main.py
```

The program reads:

```text
input/raw-text.txt
```

and saves the extracted results to:

```text
output/sample-output.json
```

## Output

The JSON output contains the extracted:

* Emails
* Phone numbers
* URLs
* Masked credit-card numbers

The output is formatted with indentation to make it easy to read.
