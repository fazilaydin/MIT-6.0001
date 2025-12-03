annual_salary = int(input("Enter your starting annual salary: "))
portion_saved = float(input("Enter the percent of your salary, as a decimal: "))
total_cost = int(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal: "))
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

        if total_months % 6 == 0:
            annual_salary += semi_annual_raise*annual_salary

print("Number of months:", total_months)

