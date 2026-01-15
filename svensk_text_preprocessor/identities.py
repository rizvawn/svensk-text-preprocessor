import re
from datetime import datetime

IDENTITY_PATTERN = r"^(\d{6}|\d{8})-\d{4}$"


def is_valid_date(year: str, month: str, day: int) -> bool:
    if len(year) == 2 and int(year) > datetime.now().year % 100:
        year = "19" + year
    else:
        year = "20" + year

    try:
        datetime(int(year), int(month), day)
        return True
    except ValueError:
        return False


def is_valid_format(id_number: str) -> bool:
    """Verify if personnummer OR samordningsnummer"""

    match = re.match(IDENTITY_PATTERN, id_number)
    if not match:
        return False

    day = int(match.group(1)[-2:])
    month = match.group(1)[-4:-2]
    year = match.group(1)[0:-4]

    if not (1 <= day <= 31 or 61 <= day <= 91):
        return False
    day = day - 60 if day > 60 else day

    return is_valid_date(year, month, day)


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

    digits_str = "".join(d for d in id_number if d.isdigit())[-10:]
    return validate_luhn(digits_str)
