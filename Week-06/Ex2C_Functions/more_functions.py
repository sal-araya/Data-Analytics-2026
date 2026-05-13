# -----------------------------------
# Function 1: Mailing Label
# -----------------------------------

def display_mailing_label(name, address, city, state, zip_code):
    print(name)
    print(address)
    print(f"{city}, {state} {zip_code}")
    print()


# -----------------------------------
# Function 2: Add Numbers
# -----------------------------------

def add_numbers(*numbers):
    total = sum(numbers)

    # Convert numbers to strings and join with +
    equation = " + ".join(str(num) for num in numbers)

    print(f"{equation} = {total}")
    print()


# -----------------------------------
# Function 3: Display Receipt
# -----------------------------------

def display_receipt(total_due, amount_paid):

    print(f"Total Due: ${total_due:.2f}")
    print(f"Amount Paid: ${amount_paid:.2f}")

    if amount_paid > total_due:
        change = amount_paid - total_due
        print(f"Change Due: ${change:.2f}")

    elif amount_paid == total_due:
        print("Change Due: $0.00")

    else:
        balance = total_due - amount_paid
        print(f"Remaining Balance: ${balance:.2f}")

    print()


# -----------------------------------
# Test display_mailing_label()
# -----------------------------------

display_mailing_label(
    "Saliem Araya",
    "123 Main Street",
    "Charlotte",
    "NC",
    "28202"
)

display_mailing_label(
    "John Smith",
    "456 Oak Avenue",
    "Atlanta",
    "GA",
    "30301"
)


# -----------------------------------
# Test add_numbers()
# -----------------------------------

add_numbers(5)

add_numbers(5, 10)

add_numbers(2, 4, 6, 8, 10)


# -----------------------------------
# Test display_receipt()
# -----------------------------------

# Overpay
display_receipt(45.50, 60.00)

# Exact payment
display_receipt(25.00, 25.00)

# Underpay
display_receipt(80.00, 50.00)


# -----------------------------------
# BONUS Function 1
# Mailing label with optional address line 2
# -----------------------------------

def display_mailing_label2(name, address1, city, state, zip_code, address2=""):

    print(name)
    print(address1)

    if address2 != "":
        print(address2)

    print(f"{city}, {state} {zip_code}")
    print()


# BONUS test
display_mailing_label2(
    "Tech Company",
    "100 Business Rd",
    "Dallas",
    "TX",
    "75001",
    "Suite 500"
)


# -----------------------------------
# BONUS Function 2
# Multiple balances for receipts
# -----------------------------------

def display_receipt2(amount_paid, *balances):

    total_due = sum(balances)

    print(f"Total Due: ${total_due:.2f}")
    print(f"Amount Paid: ${amount_paid:.2f}")

    if amount_paid > total_due:
        change = amount_paid - total_due
        print(f"Change Due: ${change:.2f}")

    elif amount_paid == total_due:
        print("Change Due: $0.00")

    else:
        balance = total_due - amount_paid
        print(f"Remaining Balance: ${balance:.2f}")

    print()


# BONUS test
display_receipt2(150, 40, 35, 25)