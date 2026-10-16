prices = {"AAPL": 180, "TSLA": 250, "GOOG": 140}

total = 0
result = ""

print("Stocks available:", list(prices.keys()))
n = int(input("How many different stocks do you have? "))

for i in range(n):
    name = input("Enter stock name: ").upper()
    qty = int(input("Enter quantity: "))
    if name in prices:
        value = prices[name] * qty
        total = total + value
        result = result + name + " x " + str(qty) + " = " + str(value) + "\n"
    else:
        print("Stock not found, skipping")

print(result)
print("Total investment:", total)

save = input("Save to file? (yes/no): ")
if save == "yes":
    file = open("portfolio.txt", "w")
    file.write(result)
    file.write("Total investment: " + str(total))
    file.close()
    print("Saved in portfolio.txt")
