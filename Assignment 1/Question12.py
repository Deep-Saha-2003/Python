# Question12 #Assignment1
# If the total selling price of 15 items and the total profit earned on them is input through the keyboard, write a program to find the cost price of one item

# Input total selling price and total profit
total_selling_price = float(input("Enter the total selling price of 15 items: "))
total_profit = float(input("Enter the total profit earned on 15 items: "))

# Calculate the total cost price of 15 items
total_cost_price = total_selling_price - total_profit

# Calculate the cost price of one item
cost_price_per_item = total_cost_price / 15

print(f"The cost price of one item is: {cost_price_per_item:.2f}")