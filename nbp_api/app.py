import os
from csv_saver import save_to_csv
from from_csv_reader import read_last_5_rows
from api import get_currency_rate

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_FILE = os.path.join(BASE_DIR, "exchange_rates.csv")
"""
CSV_FILE = "/home/innewiadro/nbp_api/exchange_rates.csv
"""
rates_to_save = []
currency = ["USD", "EUR", "GBP", "CHF", "JPY"]

old_data = read_last_5_rows(CSV_FILE)
print('a', old_data)

i = 0
for curr in currency:

    rate_data = get_currency_rate(curr)
    rate_diff = float(rate_data['Rate']) - float(old_data[i]["Rate"])
    if rate_data:
        print(f"Exchange rate for {rate_data['Currency']} on {rate_data['Date']}: {rate_data['Rate']} Daily change: {rate_diff:.2f} PLN")
        rates_to_save.append(rate_data)
        i += 1
print('b', rates_to_save)


if __name__ == "__main__":
    if rates_to_save:
        print("1")
        save_to_csv(rates_to_save)
        print(f"Saved {len(rates_to_save)} exchange rates to {CSV_FILE}")
