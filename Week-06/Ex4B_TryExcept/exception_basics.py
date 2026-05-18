# -----------------------------------
# ValueError Example
# -----------------------------------

try:
    score = int("nine")
except ValueError:
    print("ValueError: Cannot change words into numbers.")
else:
    print(score)
finally:
    print("Moving on...\n")


# -----------------------------------
# NameError Example
# -----------------------------------

try:
    print(student_name)
except NameError:
    print("NameError: That variable was never created.")
else:
    print(student_name)
finally:
    print("Moving on...\n")


# -----------------------------------
# TypeError Example
# -----------------------------------

try:
    total = 15 + "20"
except TypeError:
    print("TypeError: Numbers and text cannot be added together.")
else:
    print(total)
finally:
    print("Moving on...\n")


# -----------------------------------
# SyntaxError Example
# -----------------------------------

try:
    exec("for i in range(5) print(i)")
except SyntaxError:
    print("SyntaxError: Python syntax is written incorrectly.")
else:
    print("Code works.")
finally:
    print("Moving on...\n")


# -----------------------------------
# Another ValueError Example
# -----------------------------------

try:
    decimal = float("apple")
except ValueError:
    print("ValueError: Invalid decimal number.")
else:
    print(decimal)
finally:
    print("Moving on...\n")


# -----------------------------------
# Another TypeError Example
# -----------------------------------

try:
    answer = len(True)
except TypeError:
    print("TypeError: Boolean values do not have a length.")
else:
    print(answer)
finally:
    print("Moving on...\n")