# -----------------------------------
# Doubler lambda
# -----------------------------------

doubler = lambda n: n * 2

# Test doubler
print("Testing doubler:")
print(doubler(8))
print(doubler(-4))
print(doubler('banana'))

print()


# -----------------------------------
# Tripler lambda
# -----------------------------------

tripler = lambda n: n * 3

# Test tripler
print("Testing tripler:")
print(tripler(8))
print(tripler(-4))
print(tripler('banana'))

print()


# -----------------------------------
# Function that creates multipliers
# -----------------------------------

def multiplier(x):
    return lambda n: n * x


# Create multiplier variables
quadrupler = multiplier(4)
quintupler = multiplier(5)
sextupler = multiplier(6)
septupler = multiplier(7)
octupler = multiplier(8)
nonupler = multiplier(9)
decupler = multiplier(10)


# -----------------------------------
# Test multiplier variables
# -----------------------------------

print("Testing quadrupler:")
print(quadrupler(2))

print()

print("Testing quintupler:")
print(quintupler(2))

print()

print("Testing sextupler:")
print(sextupler(2))

print()

print("Testing septupler:")
print(septupler(2))

print()

print("Testing octupler:")
print(octupler(2))

print()

print("Testing nonupler:")
print(nonupler(2))

print()

print("Testing decupler:")
print(decupler(2))