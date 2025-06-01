

# Define stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "AMZN": 120
}

# Create an empty dictionary to store user's stocks
portfolio = {}

# Get input from user
print("Enter your stock investments. Type 'done' to finish.")

while True:
    stock_name = input("Enter stock name (e.g., AAPL): ").upper()
    if stock_name == 'DONE':
        break
    if stock_name in stock_prices:
        try:
            quantity = int(input(f"Enter quantity of {stock_name}: "))
            portfolio[stock_name] = quantity
        except ValueError:
            print("Please enter a valid number.")
    else:
        print("Stock not found. Please enter a valid stock.")

# Calculate total investment
total = 0
for stock, quantity in portfolio.items():
    price = stock_prices[stock]
    investment = price * quantity
    print(f"{stock}: {quantity} x {price} = {investment}")
    total += investment

print(f"\nTotal Investment: ${total}")

# Save to file
save_option = input("Do you want to save the result to a file? (yes/no): ").lower()
if save_option == 'yes':
    with open("portfolio_result.txt", "w") as file:
        for stock, quantity in portfolio.items():
            file.write(f"{stock}: {quantity} x {stock_prices[stock]} = {stock_prices[stock] * quantity}\n")
        file.write(f"\nTotal Investment: ${total}")
    print("Results saved to 'portfolio_result.txt'")