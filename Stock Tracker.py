# 1. The Portfolio
# This dictionary holds the stock symbol, and nested inside
# is another dictionary for the number of shares and price.
def main():

    portfolio = {
    "AAPL": {"shares": 10, "price": 170},
    "TSLA": {"shares": 4, "price": 250},
    "AMZN": {"shares": 2, "price": 130}
    }

    total_value = 0

    print("--- Portfolio Summary ---")

    # 2. Loop through each stock in the portfolio
    for stock in portfolio:
        # Extract the shares and price for the current stock
        shares = portfolio[stock]["shares"]
        price = portfolio[stock]["price"]
        
        # Calculate the value for this specific stock
        stock_value = shares * price
        
        # Add this stock's value to the total
        total_value += stock_value
        
        print(f"{stock}: {shares} shares @ ${price} = ${stock_value}")

    # 3. Print the final results
    print("-" * 25)
    print(f"Total Portfolio Value: ${total_value}")

main()