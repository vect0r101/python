item = input("What is your order?: ")

price = float(input("What is the price?: "))

quantity = int(input("How many do you want?: "))

total = price * quantity


print(f"You have bought {quantity} {item} for a total of ₹{total}.")
print(f"your total is ₹{total}.")


