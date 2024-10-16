import random
print("Welcome to the rock-paper-scissors game!")
your_choice = int(input("What do you choose? Type 0-Rock, 1-Paper, 2-Scissors\n"))
computer_choice = random.randint(0,2)
print(f"Computer Chose: {computer_choice}")

if computer_choice == your_choice:
    print("It's a Draw!")
elif computer_choice == 0 and your_choice == 2:
    print("You Lose!")
elif your_choice == 2 and computer_choice == 0:
    print("You Win!")
elif computer_choice < your_choice:
    print("You Win!")
elif computer_choice > your_choice:
    print("You Lose!")
else:
    print("You types an invalid number. You Lose!")
