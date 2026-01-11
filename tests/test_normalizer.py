from svensk_text_preprocessor.normalizer import normalize_text


def test_normalize_basic_text():
    result = normalize_text("hello world")
    assert result == "hello world"


def test_normalize_swedish_characters_nfc():
    text = "Jag tycker om åäö"
    result = normalize_text(text, form="NFC")
    assert result == "Jag tycker om åäö"
    assert len(result) == 17


def test_normalize_swedish_characters_nfd():
    text = "Jag tycker om åäö"
    result = normalize_text(text, form="NFD")
    assert result == "Jag tycker om åäö"
    assert len(result) > len(text)


def test_multiple_whitespaces_types():
    text = "hello\t\tworld\n\ntest"
    result = normalize_text(text)
    assert result == "hello world test"


def test_empty_string():
    assert normalize_text("") == ""


def test_whitespace_only():
    assert normalize_text("  \t\n  ") == ""
