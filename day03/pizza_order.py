print("Welcome to Python Pizza Deliveries?!")
size = input("What size Pizza  do you want? S, M, L: ")
pepperoni = input("Do you want pepperoni on your Pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

final_total = 0

if size == 'L':
    final_total = 249
elif size == 'M':
    final_total = 149
else:
    final_total = 99

if pepperoni == 'Y':
    if size == 'S':
        final_total += 49
    else:
        final_total +=99

if extra_cheese == 'Y':
    final_total += 29

print(f"Please pay: {final_total}")