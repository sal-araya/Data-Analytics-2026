# ranked_list.py

foods = [
    "tacos",
    "ramen",
    "jerk chicken",
    "injera",
    "pierogi"
]

# Print numbered list
for index, food in enumerate(foods, start=1):

    # Top pick
    if index == 1:
        print(f"{index}. {food} <- top pick!")

    else:
        print(f"{index}. {food}")

# Bonus - reverse order
print("\nReverse Order List:")

reversed_foods = list(reversed(foods))

for index, food in enumerate(reversed_foods, start=1):

    if index == 1:
        print(f"{index}. {food} <- top pick!")

    else:
        print(f"{index}. {food}")