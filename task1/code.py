print("Progressive Electricity Billing")

bills = []

for i in range(3):
    units = int(input("Enter electricity units: "))

    if units <= 100:
        amount = units * 1.5
    elif units <= 200:
        amount = (100 * 1.5) + (units - 100) * 2.5
    else:
        amount = (100 * 1.5) + (100 * 2.5) + (units - 200) * 4

    fixed_charge = 50
    surcharge = amount * 0.05

    if units <= 100:
        rebate = 20
    else:
        rebate = 0

    total = amount + fixed_charge + surcharge - rebate

    bills.append(total)

    print("Electricity Bill:", total)

print("\nMonthly Bill Comparison")

for i in range(1, 3):
    if bills[i] > bills[i-1] * 1.3:
        print("Unusual increase in month", i+1)
    else:
        print("Normal bill in month", i+1)
