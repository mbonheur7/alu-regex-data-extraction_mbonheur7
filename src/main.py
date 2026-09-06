import re
import json

INPUT = "input/raw-text.txt"

with open (INPUT, "r") as file:
    text= file.read()

email = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"   # Email: username + @ + domain + domain extension
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

PHONE = r"\+250(?:[ -]?\d{3}){3}"                            # Phone: +250 followed by three groups of three digits 
                                                             # Spaces or hyphens between groups are optional
phones = re.findall(PHONE, text)

URL = r"https?://[A-Za-z0-9.-]+\.[A-Za-z]{2,}(?:/[^\s]*)?"                        # URL: accepts http:// or https://, followed by a domain
        

urls = re.findall(URL, text)                                                    # An optional path after the domain is also allowed

CREDIT = r"\b(?:\d{4}[ -]){3}\d{4}\b"                                 # Credit card: four groups of four digits

credits = re.findall(CREDIT, text)                                     # Groups can be separated by spaces or hyphens

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