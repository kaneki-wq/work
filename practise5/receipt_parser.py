import re
import json
import os

# --- Получаем путь к raw.txt ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(BASE_DIR, "raw.txt")

with open(file_path, "r", encoding="utf-8") as f:
    data = f.read()

# -------------------------------------------------
# 1. извлекаем цены
# -------------------------------------------------

prices = re.findall(r"\d{1,3}(?: \d{3})*,\d{2}", data)

prices_clean = [
    float(p.replace(" ", "").replace(",", "."))
    for p in prices
]

# -------------------------------------------------
# 2. извлекаем имена
# -------------------------------------------------

product_names = re.findall(r"\d+\.\n(.+)", data)

# -------------------------------------------------
# 3. извлекаем сумму
# -------------------------------------------------

total_match = re.search(r"ИТОГО:\n([\d ]+,\d{2})", data)

if total_match:
    total_amount = float(
        total_match.group(1).replace(" ", "").replace(",", ".")
    )
else:
    total_amount = 0

# -------------------------------------------------
# 4. извлекаем время
# -------------------------------------------------

datetime_match = re.search(r"Время:\s([\d\.]+\s[\d:]+)", data)

date_time = datetime_match.group(1) if datetime_match else None

# -------------------------------------------------
# 5. извлекаем способ оплаты
# -------------------------------------------------

payment_match = re.search(r"(Банковская карта)", data)

payment_method = payment_match.group(1) if payment_match else None

# -------------------------------------------------
# 6. вывод
# -------------------------------------------------

receipt_data = {
    "products": product_names,
    "all_prices": prices_clean,
    "total_amount": total_amount,
    "date_time": date_time,
    "payment_method": payment_method
}

print(json.dumps(receipt_data, ensure_ascii=False, indent=4))