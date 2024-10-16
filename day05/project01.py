import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '*']

no_of_letters = int(input("How many letters would you like in your password:"))
no_of_numbers = int(input("How many numbers would you like in your password:"))
no_of_symbols = int(input("How many symbols would you like in your password:"))

# Easy Version
easy_password = ""
for char in range(0, no_of_letters):
    easy_password += random.choice(letters)
for symbol in range(0, no_of_symbols):
    easy_password += random.choice(symbols)
for num in range(0, no_of_numbers):
    easy_password += random.choice(numbers)
print("Easy Password:", easy_password)

# Hard Version
hard_password = []
for char in range(0, no_of_letters):
    hard_password.append(random.choice(letters))
for symbol in range(0, no_of_symbols):
    hard_password.append(random.choice(symbols))
for num in range(0, no_of_numbers):
    hard_password.append(random.choice(numbers))
random.shuffle(hard_password)
hard_pass = ""
for char in hard_password:
    hard_pass += char
print("Hard Password:", hard_pass)