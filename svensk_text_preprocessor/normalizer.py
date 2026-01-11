import unicodedata
import re
from typing import Literal


def normalize_text(
    text: str, form: Literal["NFC", "NFKC", "NFD", "NFKD"] = "NFC"
) -> str:
    normalized = unicodedata.normalize(form, text)

    cleaned = re.sub(r"\s+", " ", normalized)

    return cleaned.strip()


print("Svensk Text Preprocessor\n========================")
text = ""

while text == "":
    text = input("Provide the text to normalize: ")

choice = ""
form = "NFC"

while choice not in ["1", "2", "3", "4"]:
    choice = input(
        "Type 1-4 for the right normalization form: \n1 for NFC\n2 for NFKC\n3 for NFD\n4 for NFKD\n"
    )

if choice == "1":
    form = "NFC"
elif choice == "2":
    form = "NFKC"
elif choice == "3":
    form = "NFD"
elif choice == "4":
    form = "NFKD"

normalized = normalize_text(text, form)

print("Normalized text: ", normalized)
