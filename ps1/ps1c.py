annual_salary = int(input("Enter the starting salary: "))
initial_annual_salary = annual_salary
total_cost = 1000000
semi_annual_raise = 0.07
portion_down_payment = 0.25
down_payment = total_cost * portion_down_payment
current_savings = 0
r = 0.04
min = 0
max = 10000
best_savings_rate = (min + max) // 2
steps = 1

while True:
    months = 0
    while months < 36:
        current_savings += current_savings * r / 12 + annual_salary / 12 * best_savings_rate / 10000
        months += 1

        if months % 6 == 0:
            annual_salary += semi_annual_raise * annual_salary

    if abs(current_savings - down_payment) > 100:
        if current_savings - down_payment < -100:
            min = best_savings_rate
        else:
            max = best_savings_rate

        last_best_savings_rate = best_savings_rate
        best_savings_rate = (min + max) // 2
        steps += 1
        annual_salary = initial_annual_salary
        current_savings = 0

    else:
        break

    if last_best_savings_rate == best_savings_rate:
        break

if best_savings_rate == 9999:
    print("It is not possible to pay the down payment in three years.")
else:
 print("Best savings rate: ", best_savings_rate/10000)
 print("Steps in bisection search: ", steps)