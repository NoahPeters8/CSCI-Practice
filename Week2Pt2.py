# Ask the user how much money they have
money = float(input("How much money do you have? "))

# Ask the user for the price of the item
price = float(input("What is the price of the item? "))

# Show the data type (just to use type())
print("Type of money:", type(money))
print("Type of price:", type(price))

# Check if the user can afford the item
if money >= price:
    print("You can afford it!")
else:
    print("You do NOT have enough money.")
