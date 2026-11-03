import math

print("CAMPUS EVENT FINANCIAL PLANNING")

# Input
venue = float(input("Enter venue cost: "))
equipment = float(input("Enter equipment cost: "))
catering = float(input("Enter catering cost per person: "))
transport = float(input("Enter transport cost: "))
certificate = float(input("Enter certificate cost per person: "))

participants = int(input("Enter number of participants: "))
fee = float(input("Enter registration fee per person: "))

sponsor_target = float(input("Enter sponsorship target: "))
sponsor_received = float(input("Enter sponsorship received: "))

# Process
total_catering = catering * participants
total_certificate = certificate * participants

total_cost = venue + equipment + total_catering + transport + total_certificate

contribution = participants * fee

sponsorship_shortfall = sponsor_target - sponsor_received

total_income = contribution + sponsor_received

balance = total_income - total_cost

fixed_cost = venue + equipment + transport

variable_cost = catering + certificate

remaining_cost = fixed_cost - sponsor_received

if fee > variable_cost:
    break_even = math.ceil(remaining_cost / (fee - variable_cost))
else:
    break_even = 0

# Output
print("\n----- EVENT FINANCIAL REPORT -----")

print("Total Event Cost:", total_cost)
print("Participant Contribution:", contribution)
print("Sponsorship Shortfall:", max(0, sponsorship_shortfall))
print("Total Income:", total_income)
print("Remaining Balance:", balance)

print("Minimum Registrations for Break Even:", break_even)

if balance >= 0:
    print("Result: Event is within budget.")
else:
    print("Result: Event is over budget.")
