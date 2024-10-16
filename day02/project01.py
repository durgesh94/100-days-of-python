print("Welcome to the tip calculator")
paid_bill = float(input("What was the total bill?\n"))
total_tip = int(input("How much tip would you like to give? 10, 20 or 30?\n"))
no_of_people = int(input("How many people to split the bill?\n"))
total_bill = paid_bill + total_tip
per_person_total_pay = round(total_bill / no_of_people)
print(f"Each person should pay: {per_person_total_pay}")