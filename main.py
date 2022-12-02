import requests

# Set the target price and the amount of Ethereum to buy
target_price = 500
eth_to_buy = 10
eth_bought = 0

# Set your Binance API key and secret
api_key = "YOUR_API_KEY"
api_secret = "YOUR_API_SECRET"

# Keep buying Ethereum until the total amount is purchased
while eth_bought < eth_to_buy:
    # Check the current price of Ethereum on Binance
    current_price = requests.get("https://api.binance.com/api/v3/ticker/price?symbol=ETHUSDT").json()["price"]

    # If the current price is equal to or greater than the target price, buy Ethereum
    if current_price >= target_price:
        # Place the buy order for 1 ETH using the Binance API
        buy_order = requests.post("https://api.binance.com/api/v3/order", json={"symbol": "ETHUSDT", "side": "BUY", "type": "MARKET", "quantity": 1}, headers={"X-MBX-APIKEY": api_key})

        # Print a success message if the order was placed successfully
        if buy_order.status_code == 200:
            print(f"Successfully bought 1 ETH for {current_price} USDC!")
            eth_bought += 1
        else:
            print("Failed to place buy order. Check your API key and try again.")
    else:
        print(f"Current price is {current_price}. Target price not reached. Waiting to buy.")
