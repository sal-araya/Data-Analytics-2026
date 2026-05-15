# restaurants_enhanced.py

class Restaurant:
    """A class used to represent a restaurant."""

    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine

        # New attributes
        self.number_served = 0
        self.customer_ratings = []

    def describe_rest(self):
        message = self.name + " serves " + self.cuisine + "."
        print(message)

    def rest_open(self):
        print(self.name + " is open.")

    def add_num_served(self, customers):
        """Add customers served."""
        self.number_served += customers

    def print_num_served(self):
        """Print total customers served."""
        print(self.name + " has served " +
              str(self.number_served) + " customers")

    def customer_rating(self, rating):
        """Add customer rating and calculate average."""

        if type(rating) == int and 1 <= rating <= 5:

            self.customer_ratings.append(rating)

            average = (
                sum(self.customer_ratings)
                / len(self.customer_ratings)
            )

            print(
                "Your rating was",
                rating,
                ". The average rating for this restaurant is",
                round(average, 2)
            )

        else:
            print("Invalid rating. Please enter a whole number 1-5.")


# List of restaurant objects
restaurants = [
    Restaurant("Applebapple's", "Grill Food"),
    Restaurant("Taco Baco", "Mexican Food"),
    Restaurant("A&A", "Root Beer and Burgers")
]


# Loop through restaurants
for rest in restaurants:

    # Old methods
    rest.describe_rest()
    rest.rest_open()

    # Initial customers served
    rest.print_num_served()

    # Add customers
    rest.add_num_served(20)
    rest.add_num_served(15)

    # Updated customers served
    rest.print_num_served()

    # Customer ratings
    rest.customer_rating(5)
    rest.customer_rating(4)

    # Invalid ratings
    rest.customer_rating(6)
    rest.customer_rating(2.5)
    rest.customer_rating("5 stars")

    print()