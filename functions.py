# Exercise 1: 

# Define a function
def calculate_tax(price, rate):
    return price * rate

# Calling the function
tax1 = calculate_tax(100, 0.07)
tax2 = calculate_tax(200, 0.10)

print(f"Tax on $100 at 7%: ${tax1:.2f}")
print(f"Tax on $200 at 10%: ${tax2:.2f}")
print(f"Tax for $350 at 5%: ${calculate_tax(350, 0.05):.2f}")

# Exercise 2: 
def apply_discount(price, tier):
    if tier == "gold":
        return price * 0.85
    elif tier == "silver":
        return price * 0.90
    elif tier == "bronze": 
        return price * 0.95
    elif tier == "none":
        return price 

# Calling the function with different tiers
original_price = 200

for tier in ["gold", "silver", "bronze"]:
    print(f"Price for {tier} tier: ${apply_discount(original_price, tier):.2f}")
   
# Exercise 3: 
def final_price(price, tier, tax_rate):
    discounted = apply_discount(price, tier)
    return discounted + calculate_tax(discounted, tax_rate)

# Calling the function with different tiers and tax rates
for tier in ["gold", "silver", "bronze"]:
    print(f"Final price for {tier} tier at 7% tax: ${final_price(original_price, tier, 0.07):.2f}")

# Exercise 4: 

orders = [(200, 'gold'), (150, 'silver'), (80, 'bronze'), (500, 'none')]

rate = 0.07
for price, tier in orders:
    print(f"Final price for order of ${price} with {tier} at {rate*100:.0f}% tax: ${final_price(price, tier, rate):.2f}")
   
# Exercise 5: 

# Excercise 6:

x = 100 # global x

def double_it():
    x = 999 # local x
    return x * 2

print(x)
print(double_it())
print(x)

# Function calculates and outputs the new price after applying the discount percentage based on the membership tier.