import requests
import sys

def main():
    try:
        n = float(sys.argv[1])
    except ValueError:
        print("Command-line argument is not a number")
        sys.exit(1)

    if len(sys.argv) != 2:
        print("Missing command-line argument")
        sys.exit(1)

    else:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        txt = response.json()
        bpi = txt["bpi"]
        USD = bpi["USD"]
        rate = USD["rate_float"]
        print(f"${(rate * n):,.4f}")

if __name__ == "__main__":
    main()
