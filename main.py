print()

cost = float(input("Enter the cost: $"))
percent = float(input("Enter the tip percent: "))

decimal = percent / 100
tip = cost * decimal
total_cost = cost + tip

print(f"\nTip: ${tip:.2f}")
print(f"Total cost: ${total_cost:.2f}")
