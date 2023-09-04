import alpaca_trade_api as tradeapi

# Set your API credentials
API_KEY = 'YOUR_API_KEY'
API_SECRET = 'YOUR_API_SECRET'
BASE_URL = 'https://paper-api.alpaca.markets'  # Use 'https://api.alpaca.markets' for live trading

# Instantiate the API object
api = tradeapi.REST(API_KEY, API_SECRET, base_url=BASE_URL, api_version='v2')

def get_user_input():
    symbol = input("Enter the stock symbol: ")
    quantity = int(input("Enter the quantity: "))
    side = input("Enter the side (buy/sell): ")
    return symbol, quantity, side

def execute_trade(symbol, quantity, side):
    # Get account information
    account = api.get_account()
    print(f"Account equity: ${account.equity}")

    # Get the last price of a stock
    last_price = api.get_last_trade(symbol=symbol).price
    print(f"Last price of {symbol}: ${last_price}")

    # Implement your trading logic here
    # ...

    # Place a market order
    api.submit_order(
        symbol=symbol,
        qty=quantity,
        side=side,
        type='market',
        time_in_force='gtc'
    )
    print(f"{side.capitalize()} order placed for {quantity} share(s) of {symbol}.")

def main():
    symbol, quantity, side = get_user_input()
    execute_trade(symbol, quantity, side)

if __name__ == '__main__':
    main()
