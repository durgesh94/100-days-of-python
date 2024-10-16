print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm?\n"))

if height  >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age?"))
    if age <= 12:
        print("Pay 15 Rupees")
    elif age <= 18:
        print("Pay 25 Rupees")
    else:
        print("Pay 50 Rupees")
else:
    print("Sorry you have to grow taller before you can ride.")
