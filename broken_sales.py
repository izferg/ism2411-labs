# broken_sales.py - trace and diagnose before fixing anything.
sales = [120, 80, 250, 175, 90]

total = 0
for sale in sales:
    total += sale
print(f"Total: ${total}")

# Fix adds all of the sales to the total instead of just the last one

count = 0
for sale in sales: 
    count += 1
print(f"Count: {count}")

# Added missing colon

i = 0
while i < len(sales):
    print(sales[i])
    i += 1

# Added i = 0 to initialize the index before the while loop, and changed the <= to < to avoid index out of range error

# Used AI to help trace and diagnose the issues in the code.