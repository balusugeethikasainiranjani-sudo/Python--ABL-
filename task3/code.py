print("HOSPITAL BILLING SYSTEM")

# Input
patient_name = input("Enter patient name: ")
consultation = float(input("Enter consultation charges: "))
diagnostic = float(input("Enter diagnostic charges: "))
treatment = float(input("Enter treatment charges: "))

# Process
total = consultation + diagnostic + treatment

# Apply concession
if total >= 5000:
    discount = total * 0.10
else:
    discount = 0

final_bill = total - discount

# Validate billing constraints
if consultation < 0 or diagnostic < 0 or treatment < 0:
    print("Invalid billing amount")

else:
    print("\n----- BILL DETAILS -----")
    print("Patient Name:", patient_name)
    print("Total Charges:", total)
    print("Discount:", discount)
    print("Final Bill:", final_bill)

    # Patient Classification
    if final_bill >= 5000:
        print("Patient Category: High Payment")
    elif final_bill >= 2000:
        print("Patient Category: Medium Payment")
    else:
        print("Patient Category: Low Payment")
