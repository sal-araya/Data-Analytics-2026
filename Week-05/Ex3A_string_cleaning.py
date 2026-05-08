# Description: This script cleans string data
# Author: Sam Q. Newprogrammer

# Contact records
name_1 = "PRIYA SHARMA"
name_2 = "bob NGUYEN"
name_3 = "LaTonya Williams"

salary_1 = "$82,500"
salary_2 = "$74,000"

# -------------------------
# Convert names to lowercase
# -------------------------

print(name_1.lower())
print(name_2.lower())
print(name_3.lower())

# -------------------------
# Convert names to title case
# -------------------------

print(name_1.title())
print(name_2.title())
print(name_3.title())

# -------------------------
# Remove $ from salary strings
# -------------------------

salary_1_clean = salary_1.replace("$", "")
salary_2_clean = salary_2.replace("$", "")

print(salary_1_clean)
print(salary_2_clean)

# Check data types
print(type(salary_1_clean))
print(type(salary_2_clean))

# The values are still strings.
# To perform math, we must convert them into integers.

# -------------------------
# Convert salary_1 into integer
# -------------------------

salary_1_int = int(salary_1.replace("$", "").replace(",", ""))

print(salary_1_int)
print(type(salary_1_int))