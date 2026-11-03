# Railway Fare and Reservation Calculator

distance = float(input("Enter distance in km: "))
age = int(input("Enter passenger age: "))
print("1. Sleeper")
print("2. AC")
choice = int(input("Select travel class: "))

if distance <= 100:
    fare = distance * 2
elif distance <= 500:
    fare = distance * 1.5
else:
    fare = distance * 1

if choice == 1:
    fare = fare + 100
else:
    fare = fare + 300

if age < 12:
    fare = fare * 0.5
elif age >= 60:
    fare = fare * 0.7

reservation = 50
total = fare + reservation

print("Ticket Fare:", fare)
print("Reservation Fee:", reservation)
print("Total Fare:", total)

cancel = input("Cancel ticket? (yes/no): ")

if cancel == "yes":
    penalty = total * 0.2
    print("Cancellation Penalty:", penalty)
    print("Refund Amount:", total - penalty)
else:
    print("Ticket Confirmed")
