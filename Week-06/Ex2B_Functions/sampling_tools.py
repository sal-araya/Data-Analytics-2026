# Product inventory list
import random


products = [
    'Laptop',
    'Monitor',
    'Keyboard',
    'Mouse',
    'Webcam',
    'Headset',
    'Docking Station',
    'USB Hub',
    'Desk Lamp',
    'Surge Protector'
]

# a) Product of the Day
product_of_day = random.choice(products)
print("Product of the Day:")
print(product_of_day)

print()

# b) Select 3 products for survey
survey_products = random.sample(products, 3)
print("Survey Products:")
print(survey_products)

print()

# c) Shuffle product list
random.shuffle(products)
print("Shuffled Product List:")
print(products)

print()

# d) Simulated daily transaction count
transaction_count = random.randint(50, 300)
print("Daily Transaction Count:")
print(transaction_count)