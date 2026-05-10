# User input
pay_rate = float(input("Enter hourly pay rate: "))
hours_worked = float(input("Enter hours worked: "))
filing_status = input("Enter filing status (single or joint): ")

# Calculate weekly gross pay
if hours_worked <= 40:
    gross_weekly_pay = pay_rate * hours_worked

else:
    regular_pay = pay_rate * 40
    overtime_hours = hours_worked - 40
    overtime_pay = overtime_hours * (pay_rate * 1.5)

    gross_weekly_pay = regular_pay + overtime_pay

# Calculate annual gross pay
annual_gross_pay = gross_weekly_pay * 52

# Determine tax rate
if filing_status == "single":

    if annual_gross_pay < 12000:
        tax_rate = 0.05

    elif annual_gross_pay < 25000:
        tax_rate = 0.10

    elif annual_gross_pay < 75000:
        tax_rate = 0.15

    else:
        tax_rate = 0.20

elif filing_status == "joint":

    if annual_gross_pay < 12000:
        tax_rate = 0.00

    elif annual_gross_pay < 25000:
        tax_rate = 0.06

    elif annual_gross_pay < 75000:
        tax_rate = 0.11

    else:
        tax_rate = 0.20

else:
    print("Invalid filing status")
    tax_rate = 0

# Calculate weekly tax withholding
tax_withholding = gross_weekly_pay * tax_rate

# Calculate net pay
net_pay = gross_weekly_pay - tax_withholding

# Display results
print(f"\nYou worked {hours_worked} hours this period.")
print(f"Because you earn ${pay_rate:.2f} per hour, your gross weekly pay is ${gross_weekly_pay:.2f}")
print(f"Your filing status is {filing_status}")
print(f"Your tax withholding for the week is ${tax_withholding:.2f}")
print(f"Your net pay is ${net_pay:.2f}")