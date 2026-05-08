# Calculate van rentals

import math

people = int(input("Enter number of tourists: "))

# Each van seats 15 people
vans = math.ceil(people / 15)

# Each van costs $250
total_cost = vans * 250

# Cost per person
cost_per_person = total_cost / people

print("Vans needed:", vans)
print("Total van cost: $", format(total_cost, ".2f"))
print("Cost per person: $", format(cost_per_person, ".2f"))