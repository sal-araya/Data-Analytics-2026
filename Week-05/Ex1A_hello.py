print("Hello World!")

message = "Hello World!"
print(message)
 # "Hello world!" print twice because there are two print statements:
 # one prints directly and the other prints the variable.

 # Displaying dollars and cents
dollars = 3
cents = 0.50

print(dollars + cents)

# The result is 3.5 instead of 3.50 because Python removes trailing zeros

cents = cents + 0.25
print(dollars + cents)

d_str =  "3 dollars"
c_str = "50 cents"

print(d_str + " " + c_str)