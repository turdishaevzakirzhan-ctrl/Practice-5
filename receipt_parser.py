import re
import json

with open("raw.txt", "r", encoding="utf-8") as f:
    text = f.read()

price_strings = re.findall(r'\d[\d\s]*,\d{2}', text)
prices = [float(p.replace(" ", "").replace(",", ".")) for p in price_strings]

product_blocks = re.findall(r'\d+\.\n(.*?)\n\d', text, re.DOTALL)
products = [p.strip().replace("\n", " ") for p in product_blocks]

total_match = re.search(r'Иотго:\n([\d\s]+,\d{2})', text)
total = float(total_match.group(1).replace(" ", "").replace(",", ".")) if total_match else 0

datetime_match = re.search(r'Время:\s*(\d{2}\.\d{2}\.\d{4}\s\d{2}:\d{2}:\d{2})', text)
datetime = datetime_match.group(1) if datetime_match else ""

payment_match = re.search(r'Банковская карта', text)
payment = payment_match.group(0) if payment_match else ""

result = {
    "products": products,
    "prices": prices,
    "total": total,
    "datetime": datetime,
    "payment_method": payment
}

print(json.dumps(result, indent=4, ensure_ascii=False))