# pay_rules.py

pay_rate = float(input("Enter pay rate: "))
hours_worked = float(input("Enter hours worked: "))

# Regular pay
if hours_worked <= 40:
    gross_pay = pay_rate * hours_worked

# Overtime pay
else:
    regular_pay = pay_rate * 40
    overtime_hours = hours_worked - 40
    overtime_pay = overtime_hours * (pay_rate * 1.5)

    gross_pay = regular_pay + overtime_pay

print(f"Gross pay is ${gross_pay:.2f}")