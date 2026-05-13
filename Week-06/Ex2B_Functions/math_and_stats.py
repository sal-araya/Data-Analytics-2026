import random
import math
import statistics

# Create starting variables
vals_1_100 = range(1, 100)

# Random sample of 75 unique values
vals_sample = random.sample(vals_1_100, 75)

# Random selection of 200 values with replacement
vals_choices = random.choices(vals_1_100, k=200)

# Random radius between 3 and 10
radius = random.randint(3, 10)

# Store pi value
pi = math.pi

# -----------------------------
# Calculations for sample values
# -----------------------------

sample_sum = sum(vals_sample)
sample_average = statistics.mean(vals_sample)
sample_median = statistics.median(vals_sample)

# -----------------------------
# Calculations for 200 values
# -----------------------------

choices_average = statistics.mean(vals_choices)
choices_median = statistics.median(vals_choices)
choices_mode = statistics.mode(vals_choices)
choices_stdev = statistics.stdev(vals_choices)
choices_variance = statistics.variance(vals_choices)

# -----------------------------
# Circle calculations
# area = pi * radius squared
# -----------------------------

area = pi * (radius ** 2)

# Round area up and down
area_up = math.ceil(area)
area_down = math.floor(area)

# -----------------------------
# Output
# -----------------------------

print("_Experimenting with a subset of integers 1-100:")

print(f"Sum of 75 sample values from 1 to 100: {sample_sum}")
print(f"Average of 75 sample values: {sample_average}")
print(f"Median of 75 sample values: {sample_median}")

print('\n')

print("_Experimenting with a superset of 200 values, integers 1-100:")

print(f"Average of 200 values: {choices_average}")
print(f"Median of 200 values: {choices_median}")
print(f"Mode of 200 values: {choices_mode}")
print(f"Standard deviation of 200 values: {choices_stdev}")
print(f"Variance of 200 values: {choices_variance}")

print('\n')

print("_Modeling a random circle:")

print(f"Radius = {radius}, area = {area_up} (rounded up to the nearest integer)")
print(f"Radius = {radius}, area = {area_down} (rounded down to the nearest integer)")