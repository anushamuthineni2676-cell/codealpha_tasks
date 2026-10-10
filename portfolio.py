# Stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "AMZN": 170,
    "MSFT": 400
}

total_investment = 0

print("📈 Stock Portfolio Tracker")
print("--------------------------")

while True:
    stock = input("Enter stock name (or 'done' to finish): ").upper()

    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("❌ Stock not available.")
        print("Available stocks:", ", ".join(stock_prices.keys()))
        continue

    quantity = int(input("Enter quantity: "))

    investment = stock_prices[stock] * quantity
    total_investment += investment

    print(f"{stock}: {quantity} shares × ${stock_prices[stock]} = ${investment}")

print("\n--------------------------")
print(f"💰 Total Investment: ${total_investment}")
print("--------------------------")

# Save result to a text file
with open("portfolio.txt", "w") as file:
    file.write("Stock Portfolio Report\n")
    file.write("----------------------\n")
    file.write(f"Total Investment: ${total_investment}\n")

print("✅ Report saved as portfolio.txt")