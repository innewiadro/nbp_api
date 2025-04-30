import csv


def read_last_5_rows(file_path):
    """Reads the last 5 rows from a CSV file and returns them as a list of dictionaries."""
    with open(file_path, mode="r", newline="") as file:
        reader = csv.DictReader(file, fieldnames=["Date", "Currency", "Rate"])
        rows = list(reader)
        return rows[-5:] if len(rows) >= 5 else rows
