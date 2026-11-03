# Manufacturing Cost and Profitability Analysis

material = float(input("Enter material cost: "))
labour = float(input("Enter labour charges: "))
wastage = float(input("Enter wastage cost: "))
machine = float(input("Enter machine cost: "))
quantity = int(input("Enter quantity produced: "))

total_cost = material + labour + wastage + machine
cost_per_unit = total_cost / quantity

selling_price = float(input("Enter selling price per unit: "))
profit = (selling_price * quantity) - total_cost
target = float(input("Enter profit target: "))

print("Total Manufacturing Cost:", total_cost)
print("Cost Per Unit:", cost_per_unit)
print("Total Selling Amount:", selling_price * quantity)
print("Total Profit:", profit)

if profit >= target:
    print("Profit Target Achieved")
else:
    print("Profit Target Not Achieved")
