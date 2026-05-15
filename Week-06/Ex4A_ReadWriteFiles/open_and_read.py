# Open file
f = open("about_me.txt", "r")

# First 50 characters
first_part = f.read(50)

# Next four lines
next_lines = []

for i in range(4):
    next_lines.append(f.readline())

# Next 100 characters
last_part = f.readlines(100)

# Print results
print("First 50 characters:")
print(first_part)

print("\nNext four lines, as list by line:")
print(next_lines)

print("\nNext 100 characters, as list by line, rounded up to complete lines:")
print(last_part)

# Close file
f.close()