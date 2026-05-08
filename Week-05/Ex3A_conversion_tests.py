# Description: This script tests various numeric
# conversion techniques
# Author: Sam Q. Newprogrammer

# Define variables
a = " 101.1 "
b = '55'
c = "402 Stevens"
d = 'Number 5 '

# -------------------------
# Variable a transformations
# -------------------------

# int(a) would produce an error because 101.1 is a decimal number
# a_int = int(a)   # ValueError

a_float = float(a)

# Convert to float first, then integer
a_float_to_int = int(float(a))

# Use slicing to get numeric portion as string
a_slice = a[1:6]

# Remove spaces using strip()
print(a.strip())

# -------------------------
# Variable b transformations
# -------------------------

b_int = int(b)

b_float = float(b)

# Slice numeric portion
b_slice = b[0:2]

# -------------------------
# Variable c transformations
# -------------------------

# int(c) would produce an error because of text
# c_int = int(c)   # ValueError

# float(c) would produce an error because of text
# c_float = float(c)   # ValueError

# Slice only numeric portion
c_slice = c[0:3]
c_number = int(c_slice)

# -------------------------
# Variable d transformations
# -------------------------

# int(d) would produce an error because of text
# d_int = int(d)   # ValueError

# float(d) would produce an error because of text
# d_float = float(d)   # ValueError

# Slice numeric portion
d_slice = d[7]

# Remove spaces using strip()
print(d.strip())

# -------------------------
# Print variables and types
# -------------------------

print(a, type(a))
print(a_float, type(a_float))
print(a_float_to_int, type(a_float_to_int))
print(a_slice, type(a_slice))

print(b, type(b))
print(b_int, type(b_int))
print(b_float, type(b_float))
print(b_slice, type(b_slice))

print(c, type(c))
print(c_slice, type(c_slice))
print(c_number, type(c_number))

print(d, type(d))
print(d_slice, type(d_slice))