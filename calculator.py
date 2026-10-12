# Revenue, Margins And Discount Calculator

# Reflection questions:
# 1. the code will evaluate the number to be 100 times higher than the actual percentage because the percentage is being multiplied by 100 in the f-string formatting.
# 2. Allocating work hours, for example, if you have 40 hours to allocate for shifts per week, you can split them into 5 shifts of 8 hours each, or 4 shifts of 10 hours each, etc. The floor division operator can be used to determine how many full shifts can be allocated based on the total hours available.
# 3. Checking/practcing code ensures that the code is functioning as expected and helps identify any errors or bugs. It also allows for optimization and improvement of the code, making it more efficient and effective.
# Exercise 1:

from itertools import product


price = 50
quantity = 12
revenue = price * quantity
#,.2f has two jobs- thousands seperator and gives us EXACTLY 2 decimal places.
print(f"Revenue: ${revenue:,.2f}")
      
# Exercise 2:

cost = 32
price = 50
margin = (price - cost) / price # margin stays a decimal
print(f"Margin: {margin:.1%}")

# Excercise 3: Boolean Logic
# Product A wins if margin_a > margin_b
# Product A margin 60%, Product B margin (80-60)/80 = 25%
margin_a = 0.6
margin_b = (80 - 60) / 80 
product_a_wins = margin_a > margin_b
print(f"Product A wins: {product_a_wins}")

# Exercise 4: Logic Combo

is_premium = price > 100 and margin > 0.3

price = 150
margin = .35
print(f"Is premium: {is_premium}")


# Exercise 5: Division + Mod

print(17 / 5) # 3.4
print(17 // 5) # 3
print(17 % 5) # 2

# Exercise 7:

BOX_SIZE = 24 # ALL CAPS because it is a constant
items_ordered = int(input("How many items are being ordered? "))
full_boxes = items_ordered // BOX_SIZE # Floor div. is not abstract, it is the whole number of boxes that can be filled
loose_items = items_ordered % BOX_SIZE # Modulo is not abstract, it is the remainder of the division
exact_fit = loose_items == 0
print(f"Full boxes: {full_boxes}")
print(f"Loose items: {loose_items}")
print(f"Exact fit: {exact_fit}")

# Exercise 6: 

product_name = input("What is the product name? ")
retail_price = float(input("What is the retail price? "))
quantity_sold = int(input("How many items were sold? "))
discounted_pct = int(input("What is the discount percentage? "))
cost = float(input("What is the cost of the item? "))

revenue = retail_price * quantity_sold
discounted_rev = revenue * (1 - discounted_pct / 100)
gross_margin = (retail_price - discounted_rev) / retail_price
net_profit = discounted_rev - (cost * quantity_sold ) # Assuming cost is 60% of retail price

# Output
print(f"Product: {product_name}")
print(f"Revenue: ${revenue:,.2f}")
print(f"Discounted Revenue: ${discounted_rev:,.2f}")
print(f"Gross Margin: {gross_margin:.1%}")
print(f"Net Profit: ${net_profit:,.2f}")
