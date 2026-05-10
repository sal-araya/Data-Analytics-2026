# min_max.py

a = 100
b = 45
c = 70

# Find the smallest number
if a <= b and a <= c:
    smallest = a

elif b <= a and b <= c:
    smallest = b

else:
    smallest = c

# Find the largest number
if a >= b and a >= c:
    largest = a

elif b >= a and b >= c:
    largest = b

else:
    largest = c

# Display results
print(f"The smallest number is {smallest}")
print(f"The largest number is {largest}")