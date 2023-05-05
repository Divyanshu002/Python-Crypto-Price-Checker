import requests
from prettytable import PrettyTable

# Define the cryptocurrencies to fetch prices for
cryptos = ['bitcoin', 'ethereum', 'litecoin']

# Define the currency to display prices in
vs_currency = 'usd'

# Construct the API request URL with the specified cryptocurrencies and currency
api_url = f'https://api.coingecko.com/api/v3/simple/price?ids={",".join(cryptos)}&vs_currencies={vs_currency}'

# Make a GET request to the CoinGecko API
response = requests.get(api_url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the response JSON data
    data = response.json()
    # Create a table to display the prices
    table = PrettyTable()
    table.field_names = ['Crypto', f'Price ({vs_currency.upper()})']
    # Add rows to the table for each cryptocurrency
    for crypto in cryptos:
        price = data[crypto][vs_currency]
        table.add_row([crypto.capitalize(), f'${price:.2f}'])
    # Print the table
    print(table)
    # Ask the user if they want to quit
    while True:
        choice = input("Do you want to quit? (y/n): ").strip().lower()
        if choice == 'y':
            break
        elif choice == 'n':
            continue
        else:
            print("Invalid input. Please enter 'y' or 'n'.")
else:
    # Display an error message if the request failed
    print(f"Error: {response.status_code}")
