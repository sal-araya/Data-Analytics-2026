# Ask the user for input values
bill = float(input("What is the restaurant bill amount? "))
tip_percent = float(input("What is the tip percentage? (Example: 0.18 for 18%) "))

# Calculate the tip
tip = bill * tip_percent

# Display the result
print("The tip on a $" + str(bill) + " restaurant bill is $" + str(round(tip, 2)))

# Observations about input():
# 1. input() always stores values as text (string).
# 2. We must use float() to convert numbers with decimals.
# 3. If the user enters words instead of numbers, the program will show an error.
# 4. If the user forgets to type a value, the calculation cannot continue correctly.