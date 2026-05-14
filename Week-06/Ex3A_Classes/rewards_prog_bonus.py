# Global customer list
cust_list = []


class RewardsProgram:
    """
    This class stores customer information for a restaurant rewards program.
    """

    def __init__(self, cust_name, phone, email):
        self.cust_name = cust_name
        self.phone = phone
        self.email = email

    # Display customer profile
    def profile(self):
        print(f"Name: {self.cust_name}")
        print(f"Phone: {self.phone}")
        print(f"Email: {self.email}")

    # Thank-you message
    def thank_you(self):
        print(f"Thank you, {self.cust_name}, for visiting our restaurant!")

    # Add customer info to global list
    def add_to_cust_list(self):
        cust_list.append((self.cust_name, self.phone, self.email))


# Create customer objects
customer1 = RewardsProgram(
    "John Kevin",
    "555-1234",
    "john@email.com"
)

customer2 = RewardsProgram(
    "Lopez Asasa",
    "555-5678",
    "lopez@email.com"
)

customer3 = RewardsProgram(
    "David Yeung",
    "555-9012",
    "david@email.com"
)


# Run methods for customer 1
customer1.profile()
customer1.thank_you()
customer1.add_to_cust_list()

print()


# Run methods for customer 2
customer2.profile()
customer2.thank_you()
customer2.add_to_cust_list()

print()


# Run methods for customer 3
customer3.profile()
customer3.thank_you()
customer3.add_to_cust_list()

print()


# Print final customer list
print("Customer List:")
print(cust_list)