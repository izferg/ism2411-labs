#Python returned “53” instead of  “5” and “3” are strings and not numbers. When the + is used with strings python combines them and doesn’t add them.
# Exercise #1: Variables and Types

product = "Notebook"
unit_price = 4.99
quantity = 12
in_stock = True

print(type(product))  # Output: <class 'str'>
print(type(unit_price))  # Output: <class 'float'>
print(type(quantity))  # Output: <class 'int'>
print(type(in_stock))  # Output: <class 'bool'>

# Exercise #2: String Formatting

print(f"{quantity} units of {product} at ${unit_price:.2f} each will cost ${unit_price * quantity:.2f}.")


# Exercise #3: Conditional Statements

product_in = input("Product Name:")
price_in = float(input("Unit Price:"))
quantity_in = int(input("Quantity:"))

# print(f"{quantity_in} units of {product_in} at ${price_in:.2f} each will cost ${price_in * quantity_in:.2f}.")

# Exercise #4: Product Card

unit_cost = 2.50
revenue = unit_price * quantity
margin = (unit_price - unit_cost) / unit_price * 100

print(f"Product: {product}")
print(f"revenue: ${revenue:.2f}")
print(f"unit cost: ${unit_cost:.2f}")
print(f"margin: {margin:.2f}%")
# \n = New Line
print("="*20)
print(f"Product: {product}\nRevenue: ${revenue:.2f}\nUnit Cost: ${unit_cost:.2f}\nMargin: {margin:.2f}%")

print("5" + "3")
print(5 + 3)
print("5" * 3)