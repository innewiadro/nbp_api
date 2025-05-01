import os
import csv

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_FILE = os.path.join(BASE_DIR, "exchange_rates.csv")



def save_to_csv(data):
    """Saves exchange rate data to CSV."""
    file_exists = os.path.isfile(CSV_FILE)

    with open(CSV_FILE, mode="a", newline="") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow(["Date", "Currency", "Rate"])

        for row in data:
            writer.writerow([row["Date"], row["Currency"], row["Rate"]])
