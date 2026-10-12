#  Exercise 1 
sales = [120, 80, 250, 175, 90, 410, 60, 215]
total = 0       # initialize
for sale in sales:
    total += sale   # update
print(f"Total: ${total}")

print()  # Line break for clean terminal formatting

#  Exercise 2 
sales = [120, 80, 250, 175, 90, 410, 60, 215]
total = 0
count = 0
for sale in sales:
    total += sale
    count += 1

average = total / count
print(f"Total: ${total}")
print(f"Count: {count}")
print(f"Average: ${average:.2f}")

print()

#  Exercise 3 
sales = [120, 80, 250, 175, 90, 410, 60, 215]
current_max = 0
for sale in sales:
    if sale > current_max:
        current_max = sale

print(f"Largest sale: ${current_max}")

print()

#  Exercise 4 
sales = [120, 80, 250, 175, 90, 410, 60, 215]
count_over_100 = 0
total_over_100 = 0

for sale in sales:
    if sale > 100:
        count_over_100 += 1
        total_over_100 += sale

print(f"Sales over $100: {count_over_100}")
print(f"Total of those sales: ${total_over_100}")

print()

#  Exercise 5 
sales = [120, 80, 250, 175, 90, 410, 60, 215]

for sale in sales:
    if sale > 400:
        print(f"Alert: outlier found — ${sale}. Stopping.")
        break
    if sale <= 100:
        continue
    print(f"${sale}")

print()

#  Exercise 6 
sales = [120, 80, 250, 175, 90, 410, 60, 215]
total = 0
i = 0            # index

while i < len(sales):
    total += sales[i]
    i += 1

print(f"Total: ${total}")
# Production choice: I would use the for loop in production because it is 
# more concise, less error-prone (no risk of forgetting to increment i), 
# and explicitly designed for sequence iteration in Python.

print()

#  Exercise 7 
sales = [120, 80, 250, 175, 90, 410, 60, 215]

for sale in sales:
    if sale >= 200:
        discount_pct = 10
        discount_rate = 0.10
    elif sale >= 100:
        discount_pct = 5
        discount_rate = 0.05
    else:
        discount_pct = 0
        discount_rate = 0.00
    
    discounted_price = sale * (1 - discount_rate)
    print(f"${sale:<3} → {discount_pct}% discount → ${discounted_price:.2f}")

# Self Assesment
# 1- A running total or combined result can be computed by processing a series of items one at a time using the accumulator pattern. These are the three steps:
  # - Initialize: To store the running result, set up a variable (such as total = 0) prior to the loop. This stage is important since it gives a starting point.
  # - Update: As each item is processed, change the accumulator variable inside the loop (total += sale, for example). This stage is important since it gathers data gradually.
  # - Output/Result: Use or output the final accumulator value once the loop terminates. 
  #   Because it provides you with the overall summary statistic, this step is important.
# 2- Compared to the succinct 'for sale in sales' approach, the while loop version needed more boilerplate code (initializing an index variable, writing the condition, manually indexing sales[i], and incrementing i).
   # - For loop: Preferred in production for iterating over collections since it is shorter, more readable, Pythonic, and prevents infinite loops.
   # - While loop: Better when the entire number of iterations is unknown in advance or dependent on a condition dynamically changing during execution.
# 3- A list of product stock quantities, such as inventory_counts = [45, 12, 0, 89, 3, 120], could be a dataset in a retail or e-commerce inventory environment. To determine the number of products with low stock (less than 15 units, for example) and the total number of units of low-stock inventory, a loop would cycle through the list. 