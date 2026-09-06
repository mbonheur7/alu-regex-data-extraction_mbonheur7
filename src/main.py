import re
import json

INPUT = "input/raw-text.txt"

with open (INPUT, "r") as file:
    text= file.read()

email = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"
emails = re.findall(email, text)

for address in emails:
    if address.endswith("@alueducation.com"):
        print("ALU OFFICIAL:", address)
    elif address.endswith("@alumni.alueducation.com"):
        print("ALU ALUMNI:", address)
    elif address.endswith("@si.alueducation.com"):
        print("ALU SI:", address)
    else:
        print("OTHER:", address)

PHONE = r"\+250(?:[ -]?\d{3}){3}"

phones = re.findall(PHONE, text)

URL = r"https?://[A-Za-z0-9.-]+\.[A-Za-z]{2,}(?:/[^\s]*)?"

urls = re.findall(URL, text)

CREDIT = r"\b(?:\d{4}[ -]){3}\d{4}\b"

credits = re.findall(CREDIT, text)

masked_cards = []

for card in credits:
    masked_cards.append("**** **** **** " + card[-4:])

results = {
    "emails": emails,
    "phones": phones,
    "urls": urls,
    "credit_cards": masked_cards,
    "validation": {
        "status": "completed",
        "external_text_executed": False
    }
}
with open("output/sample-output.json", "w",) as file:
    json.dump(results, file, indent=4)