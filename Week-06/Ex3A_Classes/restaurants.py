# restaurants.py

class Restaurant:
    """A class used to represent a restaurant."""

    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine

    def describe_rest(self):
        message = self.name + " serves " + self.cuisine + "."
        print(message)

    def rest_open(self):
        print(self.name + " is open.")


# List of restaurant objects
restaurants = [
    Restaurant("Applebapple's", "Grill Food"),
    Restaurant("Taco Baco", "Mexican Food"),
    Restaurant("A&A", "Root Beer and Burgers")
]

# Loop through each restaurant
for rest in restaurants:
    rest.describe_rest()
    rest.rest_open()
    print()