# sales_performance.py

sales_data = [
    ('Marcus Webb', 'East', 4250.00),
    ('Priya Sharma', 'West', 5875.50),
    ('DeShawn Carter', 'East', 3100.75),
    ('LaTonya Rivers', 'South', 6420.00),
    ('Bob Nguyen', 'West', 4980.25),
]

# Bonus total sales variable
total_sales = 0

# Loop through records
for name, region, sales in sales_data:

    # Add to total sales
    total_sales += sales

    # Print summary line
    print(f"{name} ({region}): ${sales:,.2f}")

    # Top performer check
    if sales > 5000:
        print("^ Top performer!")

# Bonus output
print(f"\nOverall Total Sales: ${total_sales:,.2f}")