import requests
import sys
import os

def main():
    if len(sys.argv) == 2:
        try:
            user = sys.argv[1]
            user = float(user)
            bit_price = float(get_data())
            final = bit_price * user
            print(conv(final))
        except ValueError:
            sys.exit("Command-line argument is not a number ")

    else:
        sys.exit("Missing command-line argument")


def conv(a):
    a = float(a)
    return f"${a:,.4f}"

def get_data():
    api = os.environ.get("COINCAP_API_KEY")
    if not api:
        sys.exit("Missing COINCAP_API_KEY environment variable")
    try:
        response = requests.get(f"https://rest.coincap.io/v3/assets/bitcoin?apiKey={api}")
        data = response.json()
        price = data['data']["priceUsd"]
        return price
    except requests.RequestException:
        pass


main()
