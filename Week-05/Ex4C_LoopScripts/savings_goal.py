# savings_goal.py

starting_balance = 100
savings_goal = 1000
weekly_savings = 150
treat_cost = 25

balance = starting_balance

# Loop until goal is reached
while balance < savings_goal:

    # Add weekly savings
    balance += weekly_savings

    # 75% of goal
    if balance >= savings_goal * 0.75:
        balance -= treat_cost
        print(f"So close! After treating myself, my balance is up to ${balance:.2f}")

    # More than halfway
    elif balance > savings_goal / 2:
        print(f"Almost there! This week my balance is up to ${balance:.2f}")

    # Regular message
    else:
        print(f"This week my balance increased to ${balance:.2f}")

# Goal reached
print(f"Goal met! My current balance is ${balance:.2f}")