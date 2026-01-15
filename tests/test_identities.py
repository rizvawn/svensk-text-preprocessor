from svensk_text_preprocessor.identities import validate_personnummer


def test_valid_personnummer_10_digit():
    assert validate_personnummer("121212-1212")


def test_valid_personnummer_12_digits():
    assert validate_personnummer("19121212-1212")


def test_valid_samordningsnummer():
    assert validate_personnummer("19121272-1219")


def test_invalid_format_no_dash():
    assert not validate_personnummer("191212121212")


def test_invalid_format_wrong_length():
    assert not validate_personnummer("12121212")
