# greeting.py

hour = 14

# Late night condition
if hour >= 23 or hour < 4:
    print("What are you doing up so late??")

# Morning
elif hour < 10:
    print("Good morning!")

# Daytime
elif hour < 17:
    print("Good day!")

# Evening
else:
    print("Good evening!")