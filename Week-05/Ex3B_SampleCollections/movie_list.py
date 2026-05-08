# Create a list of movies
movies = ["Inception", "Avatar", "Black Panther", "Titanic"]

# Print description statement using len()
print(f"The list movies includes my top {len(movies)} favorite movies")

# Print the complete list
print(movies)

# Part 4a - Using sorted()
print("\nUsing sorted():")
print(sorted(movies))

# Print original list again
print("Original list after sorted():")
print(movies)

# Part 4b - Using .sort()
movies.sort()

print("\nUsing .sort():")
print(movies)

# Part 5 - Add another movie using append()
movies.append("Interstellar")

# Print updated statement and list
print("\nAfter adding another movie:")
print(f"The list movies includes my top {len(movies)} favorite movies")
print(movies)