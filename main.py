print()

cost = float(input("Enter cost: "))
percent = float(input("Enter tip percent: "))
tip = cost * percent / 100

print(f"\nThe tip is {tip}, the total cost is {cost + tip}.")
