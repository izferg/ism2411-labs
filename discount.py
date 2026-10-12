# Exercise 1

total = float(input("Enter cart total: $"))

# Add your if/elif/else here
if total >= 500:
    discount = 0.15
elif total >= 200:
    discount = 0.10
elif total >= 100:
    discount = 0.05
else:
    discount = 0

final = total * (1 - discount)
print(f"Discount: {discount * 100:.0f}%")
print(f"Final price: ${final:.2f}")

# Exercise 2
if final > 1000:
    status = "manager_approval_required"
else:
    status = "auto-approved"

print(f"Status: {status}")

# Exercise 3

region = "South"
ex3_total = 250.0

if ex3_total >= 500:
    ex3_discount = 0.15
elif ex3_total >= 200:
    ex3_discount = 0.10
elif ex3_total >= 100:
    ex3_discount = 0.05
else:
    ex3_discount = 0.00

if region == "South" and ex3_total >= 100:
    print("Region bonus applied: additional 2% off")
    ex3_discount += 0.02

ex3_final = ex3_total * (1 - ex3_discount)
print(f"Final discount: {ex3_discount * 100:.0f}%")
print(f"Final price: ${ex3_final:.2f}")

# Exercise 4
customer_type = "wholesale"
if region == "South" and total > 100 and customer_type == "wholesale":
    extra_discount = 0.03

# Exercise 5
amounts_to_test = [-50, 500, 15000]

for amount in amounts_to_test:
    if amount <= 0:
        flag = "SUSPICIOUS"
    elif 1 <= amount <= 9999:
        flag = "NORMAL"
    else:
        flag = "LARGE — REVIEW REQUIRED"
    print(f"Amount {amount}: {flag}")

# Exercise 6
yearly_spent = 2500
orders_placed = 12
has_outstanding_balance = False

qualifies_for_vip = (yearly_spent > 2000 or orders_placed > 10) and not has_outstanding_balance
print(f"VIP Upgrade Qualified: {qualifies_for_vip}")

# SELF ASSESSMENT
#1. Tracing order_total = 350:
   # - First condition: `order_total >= 500` -> 350 is NOT >= 500, so it skips to the next check.
   # - Second condition: `order_total >= 200` -> 350 IS >= 200 (True).
   # - Python assigns the discount of 10% (0.10) and exits the if/elif/else block without evaluating further conditions.

# 2. Difference between combined condition and two separate `if` statements:
 # - `if total > 100 and total < 500:` checks both boundaries together. If true, the body executes once.
 # - Two separate `if` statements (`if total > 100:` and `if total < 500:`) evaluate independently. A value like 250 meets both conditions, causing both code blocks to execute sequentially (which could accidentally overwrite variables or double-apply logic).

# 3. Everyday tiered conditional logic:
   # - Systems like income tax brackets, mobile data plan tiers, streaming subscription tiers, and credit card cashback categories rely on these exact decision structures. Understanding Python conditionals helps clarify how underlying software processes financial rules, calculates fees, and handles edge cases systematically.
