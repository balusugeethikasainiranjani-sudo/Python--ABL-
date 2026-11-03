# Employee Payroll and Deduction Analysis

basic = float(input("Enter basic salary: "))
allowances = float(input("Enter allowances: "))
overtime = float(input("Enter overtime pay: "))
incentives = float(input("Enter incentives: "))

gross = basic + allowances + overtime + incentives

if gross <= 20000:
    deduction = gross * 0.05
elif gross <= 50000:
    deduction = gross * 0.10
else:
    deduction = gross * 0.15

net = gross - deduction

print("Basic Salary:", basic)
print("Allowances:", allowances)
print("Overtime Pay:", overtime)
print("Incentives:", incentives)
print("Gross Salary:", gross)
print("Deduction:", deduction)
print("Net Salary:", net)
