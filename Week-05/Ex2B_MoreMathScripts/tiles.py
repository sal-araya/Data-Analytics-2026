import math

length = float(input("Enter room length in feet: "))
width = float(input("Enter room width in feet: "))

area = length * width

# Add 10% extra tiles
total_tiles = area * 1.10

# 12 tiles per box
boxes = math.ceil(total_tiles / 12)

print("You need", boxes, "boxes of tiles.")