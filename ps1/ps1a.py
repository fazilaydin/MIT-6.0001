annual_salary = int(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary, as a decimal: "))
total_cost = int(input("Enter the cost of your dream home: "))
portion_down_payment = 0.25
current_savings = 0
r = 0.04
total_months = 0
down_payment = total_cost * portion_down_payment

while True:
    if current_savings >= down_payment:
        break
    else:
        current_savings += current_savings * r/12 + annual_salary/12 * portion_saved
        total_months += 1

print("Number of months:", total_months)

