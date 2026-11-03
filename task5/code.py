# Retail Billing with Discounts

n = int(input("Enter number of products: "))
total = 0

for i in range(n):
    price = float(input("Enter product price: "))
    quantity = int(input("Enter quantity: "))

    amount = price * quantity

    if amount >= 1000:
        discount = amount * 0.10
    else:
        discount = amount * 0.05

    amount = amount - discount

    tax = amount * 0.05
    final_amount = amount + tax

    print("Product Amount:", price * quantity)
    print("Discount:", discount)
    print("Tax:", tax)
    print("Final Amount:", final_amount)

    total = total + final_amount

print("Total Bill:", total)

if total >= 5000:
    extra_discount = 500
else:
    extra_discount = 0

if extra_discount > 500:
    extra_discount = 500

print("Extra Discount:", extra_discount)
print("Final Bill Amount:", total - extra_discount)
