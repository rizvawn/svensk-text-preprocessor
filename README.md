# Svensk Text Preprocessor

A foundational Python library for cleaning and normalizing Swedish text, designed as a shared dependency for government NLP projects.

## Overview

The library provides three main modules for handling Swedish text:

### normalizer.py

Handles Unicode normalization (NFC/NFD) and whitespace cleanup for Swedish characters (å, ä, ö). The module ensures consistent text representation by normalizing different Unicode forms and removing redundant whitespace.

### identities.py

Identifies and validates Swedish identity numbers using regex patterns and the Luhn algorithm. The module supports both personnummer and samordningsnummer in the formats YYMMDD-XXXX and YYYYMMDD-XXXX.

### pseudonymizer.py

Creates stable pseudonyms for identity numbers using the Faker library with se_SE locale. The same real identity number consistently maps to the same pseudonym through deterministic hashing.

## Swedish Identity Number Formats

**Personnummer**: Follows the format YYMMDD-XXXX or YYYYMMDD-XXXX where the last four digits include a checksum digit validated with the Luhn algorithm.

**Samordningsnummer**: Uses the same format as personnummer but with 60 added to the day field (for example, 19900161-XXXX for a person born on the 1st).

## Installation

The package is installed with pip:

```bash
pip install svensk-text-preprocessor
```

For development, the package is installed in editable mode:

```bash
pip install -e .
```

## Usage

```python
from svensk_text_preprocessor import normalizer, identities, pseudonymizer

# Normalize text with Swedish characters
text = normalizer.normalize("Some   text   with   extra   spaces")

# Validate personnummer
is_valid = identities.validate_personnummer("19900101-1234")

# Pseudonymize identity number
fake_id = pseudonymizer.pseudonymize("19900101-1234")
```

## Testing

The project uses pytest for testing with a target of at least 95% code coverage:

```bash
pytest tests/ -v --cov=.
```

## Technical Requirements

- Python 3.8+
- UTF-8 handling for Swedish characters
- Faker library with se_SE locale for pseudonymization
