import requests


def get_currency_rate(currency_code, table="A"):
    url = f"https://api.nbp.pl/api/exchangerates/rates/{table}/{currency_code}/?format=json"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Handle HTTP errors
        data = response.json()
        rate_info = data["rates"][0]
        return {

            "Date": rate_info["effectiveDate"],
            "Currency": currency_code.upper(),
            "Rate": rate_info["mid"]

        }
    except requests.exceptions.RequestException as e:
        print(f"Error fetching exchange rate: {e}")
        return None
