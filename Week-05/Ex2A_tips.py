# Define known values
food_cost = 79.25
tax = 6.54
tip = 12.00

# Calculate the unknown
total_due = food_cost + tax + tip

# The str() function converts numbers into strings so they can be combined with text in print statements.
# Without str(), Python would give an error when trying to join text and numbers.

# Original print statement (commented out)
# print("The total due is " + str(total_due)

# New print statements
print("Food cost is " + str(food_cost) + " and tax is " + str(tax))
# print("Tip is " + str(tip))  # old version (commented out)

# Improved formatting for tip (always shows 2 decimal places)
print("Tip is " + format(tip, ".2f"))

print(f"Total due is ${total_due:.2f}")
