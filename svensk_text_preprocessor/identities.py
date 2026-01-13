import re

IDENTITY_PATTERN = r"^(\d{6}|\d{8})-\d{4}$"


def is_valid_format(id_number: str) -> bool:
    """Verify if personnummer OR samordningsnummer"""
    match = re.match(IDENTITY_PATTERN, id_number)
    if not match:
        return False
    day = int(match.group(1)[-2:])
    return 1 <= day <= 31 or 61 <= day <= 91


def validate_luhn(number_string: str) -> bool:
    digits = [int(d) for d in number_string if d.isdigit()]

    digits = digits[::-1]

    for i in range(1, len(digits), 2):
        digits[i] *= 2
        if digits[i] > 9:
            digits[i] -= 9

    return sum(digits) % 10 == 0


def validate_personnummer(id_number: str) -> bool:
    if not is_valid_format(id_number):
        return False

    return validate_luhn(id_number)
